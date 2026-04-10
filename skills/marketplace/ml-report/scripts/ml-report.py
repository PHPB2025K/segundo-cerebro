#!/usr/bin/env python3
"""
Relatório de Performance ML — Budamix / GB Importadora
Orquestrador: carrega seções modulares, busca dados, combina HTML → PDF.

Uso:
    python3 ml-report.py --inicio 2026-03-01 --fim 2026-03-15
    python3 ml-report.py --inicio 2026-03-01 --fim 2026-03-15 --secoes 1,2,6
    python3 ml-report.py --inicio 2026-03-01 --fim 2026-03-15 --output /tmp/report.pdf --debug
"""

import argparse
import json
import logging
import os
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime

# ─── Config ──────────────────────────────────────────────────────────────────

USER_ID = 532562281
TOKEN_FILES = {
    'vendas': '/root/.openclaw/.ml-tokens.json',
    'finance': '/root/.openclaw/.ml-tokens-finance.json',
    'metrics': '/root/.openclaw/.ml-tokens-metrics.json',
}
REFRESH_SCRIPT = '/root/.openclaw/workspace/skills/ml-extrato/scripts/ml-refresh-token.sh'
DEFAULT_OUTPUT_DIR = os.path.expanduser('~/.openclaw/workspace/reports')

log = logging.getLogger('ml-report')

# ─── Section Registry ────────────────────────────────────────────────────────

SECTION_MODULES = {}

def load_sections():
    """Carrega todos os módulos de seção dinamicamente."""
    sections_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sections')
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    for i in range(1, 10):
        module_name = f"sections.s{i:02d}_"
        # Find the actual file
        for f in os.listdir(sections_dir):
            if f.startswith(f"s{i:02d}_") and f.endswith('.py'):
                mod_name = f"sections.{f[:-3]}"
                try:
                    mod = __import__(mod_name, fromlist=['build', 'needs_data'])
                    SECTION_MODULES[i] = mod
                    log.debug(f"Seção {i} carregada: {mod_name}")
                except Exception as e:
                    log.error(f"Erro ao carregar seção {i}: {e}")
                break

# ─── API Helpers ─────────────────────────────────────────────────────────────

def refresh_tokens():
    for app_type in ['vendas', 'finance', 'metrics']:
        try:
            result = subprocess.run(['bash', REFRESH_SCRIPT, app_type],
                                    capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                log.info(f"Token {app_type} renovado")
            else:
                log.warning(f"Falha refresh {app_type}: {result.stderr[:100]}")
        except Exception as e:
            log.warning(f"Erro refresh {app_type}: {e}")


def load_token(app_type):
    path = TOKEN_FILES[app_type]
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)['access_token']


def api_get(url, token, retries=2):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
            resp = urllib.request.urlopen(req, timeout=30)
            return json.loads(resp.read())
        except Exception as e:
            if attempt == retries:
                log.warning(f"API falhou: {url}: {e}")
                return None


def fetch_all_paginated(base_url, token, limit=50, max_pages=20):
    all_results = []
    offset = 0
    for _ in range(max_pages):
        sep = '&' if '?' in base_url else '?'
        data = api_get(f"{base_url}{sep}limit={limit}&offset={offset}", token)
        if not data: break
        results = data.get('results', [])
        all_results.extend(results)
        if offset + limit >= data.get('paging', {}).get('total', 0) or not results:
            break
        offset += limit
    return all_results

# ─── Data Fetchers ───────────────────────────────────────────────────────────

def fetch_orders(begin, end, token):
    url = (f"https://api.mercadolibre.com/orders/search?seller={USER_ID}"
           f"&order.date_created.from={begin}T00:00:00.000-03:00"
           f"&order.date_created.to={end}T23:59:59.000-03:00&sort=date_desc")
    return fetch_all_paginated(url, token)


def fetch_payments(begin, end, token):
    url = (f"https://api.mercadopago.com/v1/payments/search"
           f"?begin_date={begin}T00:00:00Z&end_date={end}T23:59:59Z"
           f"&sort=date_created&criteria=desc")
    return fetch_all_paginated(url, token)


def fetch_seller_info(token):
    return api_get(f"https://api.mercadolibre.com/users/{USER_ID}", token)


def fetch_active_items(token):
    data = api_get(f"https://api.mercadolibre.com/users/{USER_ID}/items/search?status=active", token)
    if not data: return [], 0
    item_ids = data.get('results', [])
    total = data.get('paging', {}).get('total', 0)
    items = []
    for item_id in item_ids[:50]:
        item = api_get(f"https://api.mercadolibre.com/items/{item_id}", token)
        if item: items.append(item)
    return items, total

# ─── HTML Template ───────────────────────────────────────────────────────────

def get_css():
    """Retorna o CSS completo do relatório."""
    return '''
:root { --teal:#004D4D; --grafite:#132525; --dourado:#C7A35A; --terracota:#C56A4A;
        --sage:#7EADAD; --porcelana:#D9E6E6; --areia:#F7F4EF; --verde:#18794E; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:system-ui,-apple-system,'Segoe UI',sans-serif; color:var(--grafite); background:white; font-size:11pt; line-height:1.5; }
.page { page-break-after:always; padding:30px 40px; min-height:100vh; position:relative; }
.page:last-child { page-break-after:avoid; }
.cover-page { background:linear-gradient(135deg,var(--areia) 0%,white 100%); }
.cover-header { display:flex; align-items:center; gap:30px; margin-bottom:30px; padding-top:20px; }
.cover-logo { width:120px; height:auto; }
.cover-title h1 { font-size:28pt; color:var(--teal); font-weight:700; letter-spacing:-0.5px; }
.cover-title h2 { font-size:16pt; color:var(--sage); font-weight:400; }
.cover-period { font-size:12pt; color:var(--dourado); font-weight:600; margin-top:5px; }
.health-indicator { display:flex; align-items:center; gap:15px; padding:15px 25px; border-radius:12px; margin-bottom:25px; }
.health-excellent { background:#E8F5E9; border-left:4px solid var(--verde); }
.health-good { background:#FFF8E1; border-left:4px solid var(--dourado); }
.health-warning { background:#FFEBEE; border-left:4px solid var(--terracota); }
.health-emoji { font-size:24pt; } .health-label { font-size:13pt; color:var(--grafite); }
.health-detail { font-size:10pt; color:var(--sage); margin-left:auto; }
.section-header { display:flex; align-items:center; gap:15px; margin-bottom:25px; padding-bottom:12px; border-bottom:3px solid var(--teal); }
.section-number { font-size:28pt; font-weight:700; color:var(--dourado); line-height:1; }
.section-header h2 { font-size:18pt; color:var(--teal); }
.kpi-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:15px; margin-bottom:25px; }
.kpi-grid-4 { grid-template-columns:repeat(4,1fr); } .kpi-grid-3 { grid-template-columns:repeat(3,1fr); }
.kpi-card { background:var(--areia); border-radius:10px; padding:18px; text-align:center; border:1px solid var(--porcelana); }
.kpi-card.kpi-primary { background:var(--teal); color:white; }
.kpi-card.kpi-primary .kpi-label { color:var(--porcelana); }
.kpi-card.kpi-positive { border-left:4px solid var(--verde); }
.kpi-card.kpi-negative { border-left:4px solid var(--terracota); }
.kpi-card.kpi-warning { border-left:4px solid var(--dourado); }
.kpi-icon { font-size:18pt; display:block; margin-bottom:5px; }
.kpi-value { font-size:18pt; font-weight:700; display:block; }
.kpi-card:not(.kpi-primary) .kpi-value { color:var(--teal); }
.kpi-label { font-size:9pt; color:#757575; display:block; margin-top:4px; text-transform:uppercase; letter-spacing:0.5px; }
.chart-container { margin:20px 0; text-align:center; } .chart-img { max-width:100%; height:auto; }
.data-table { width:100%; border-collapse:collapse; margin:15px 0; font-size:10pt; }
.data-table thead th { background:var(--teal); color:white; padding:10px 12px; text-align:left; font-weight:600; font-size:9pt; text-transform:uppercase; letter-spacing:0.5px; }
.data-table tbody tr:nth-child(even) { background:var(--areia); }
.data-table tbody td { padding:8px 12px; border-bottom:1px solid var(--porcelana); }
.data-table .number { text-align:right; font-variant-numeric:tabular-nums; }
.data-table .rank { font-weight:700; color:var(--dourado); width:40px; }
.insight-box { display:flex; gap:12px; padding:18px; background:#E8F5E9; border-radius:10px; border-left:4px solid var(--verde); margin:20px 0; }
.insight-box.insight-warning { background:#FFF8E1; border-left-color:var(--dourado); }
.insight-box.insight-premium { background:linear-gradient(135deg,var(--teal),#006666); border-left:none; color:white; }
.insight-box.insight-premium .insight-content strong { color:var(--dourado); }
.insight-icon { font-size:20pt; line-height:1; } .insight-content { font-size:10pt; line-height:1.6; }
.insight-content strong { color:var(--teal); }
.badge { display:inline-block; padding:3px 10px; border-radius:20px; font-size:9pt; font-weight:600; }
.badge-positive { background:#E8F5E9; color:var(--verde); }
.badge-negative { background:#FFEBEE; color:var(--terracota); }
.badge-warning { background:#FFF8E1; color:#B8860B; }
.badge-neutral { background:var(--porcelana); color:var(--sage); }
.reputation-card { background:var(--areia); border-radius:12px; padding:25px; display:flex; justify-content:space-between; align-items:center; margin-bottom:25px; border:1px solid var(--porcelana); }
.rep-level { display:flex; align-items:center; gap:15px; } .rep-emoji { font-size:36pt; }
.rep-level h3 { font-size:16pt; color:var(--teal); } .rep-level p { color:#757575; }
.rep-stats { text-align:right; color:#757575; font-size:10pt; } .rep-stats span { display:block; }
.metrics-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:15px; margin:20px 0; }
.metric-card { background:white; border-radius:10px; padding:20px; border:1px solid var(--porcelana); text-align:center; }
.metric-card.metric-positive { border-top:3px solid var(--verde); }
.metric-card.metric-warning { border-top:3px solid var(--dourado); }
.metric-card.metric-negative { border-top:3px solid var(--terracota); }
.metric-header { display:flex; align-items:center; justify-content:center; gap:8px; margin-bottom:10px; }
.metric-title { font-weight:600; } .metric-value { font-size:24pt; font-weight:700; color:var(--teal); display:block; }
.metric-status { font-size:9pt; color:#757575; }
.strategy-section { display:grid; grid-template-columns:1fr; gap:15px; margin-bottom:20px; }
.strategy-block { padding:20px; border-radius:10px; } .strategy-block h3 { margin-bottom:10px; font-size:12pt; }
.strategy-block ul { margin-left:20px; font-size:10pt; } .strategy-block li { margin-bottom:5px; }
.strategy-wins { background:#E8F5E9; border-left:4px solid var(--verde); }
.strategy-problems { background:#FFEBEE; border-left:4px solid var(--terracota); }
.strategy-opportunities { background:#FFF3E0; border-left:4px solid var(--dourado); }
.na-section { text-align:center; padding:60px 40px; background:var(--areia); border-radius:12px; margin:30px 0; }
.na-icon { font-size:48pt; margin-bottom:15px; } .na-section h3 { color:var(--teal); margin-bottom:10px; }
.na-section p { color:#757575; margin-bottom:20px; }
.na-actions { text-align:left; max-width:500px; margin:0 auto; }
.na-actions h4 { color:var(--teal); margin-bottom:8px; } .na-actions ul { margin-left:20px; font-size:10pt; }
.na-note { font-size:9pt; color:var(--sage); margin-top:15px; } .na { color:var(--sage); font-style:italic; }
.executive-summary { background:white; border:1px solid var(--porcelana); border-radius:10px; padding:20px; margin-top:20px; }
.executive-summary h3 { color:var(--teal); margin-bottom:10px; }
.executive-summary ul { margin-left:20px; font-size:10pt; } .executive-summary li { margin-bottom:5px; }
@media print { .page { page-break-after:always; } body { -webkit-print-color-adjust:exact; print-color-adjust:exact; } }
'''

def wrap_html(sections_html, periodo_display, periodo_footer):
    css = get_css()
    return f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>Relatório ML — Budamix</title>
<style>{css}</style></head><body>
{sections_html}
<script>
document.querySelectorAll('.page').forEach((page,i,all)=>{{
    const f=document.createElement('div');
    f.style.cssText='position:absolute;bottom:15px;left:40px;right:40px;display:flex;justify-content:space-between;font-size:8pt;color:#7EADAD;border-top:1px solid #D9E6E6;padding-top:5px;';
    f.innerHTML=`<span>Budamix · Relatório ML · {periodo_footer}</span><span>${{String(i+1).padStart(2,'0')}}/${{String(all.length).padStart(2,'0')}}</span>`;
    page.appendChild(f);
}});
</script></body></html>'''

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Relatório ML — Budamix")
    parser.add_argument("--inicio", required=True)
    parser.add_argument("--fim", required=True)
    parser.add_argument("--secoes", default="all")
    parser.add_argument("--output", default=None)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s')

    sections_to_build = list(range(1, 10)) if args.secoes == 'all' else [int(s) for s in args.secoes.split(',')]

    if not args.output:
        d1 = args.inicio[5:].replace('-', '')
        d2 = args.fim[5:].replace('-', '')
        args.output = os.path.join(DEFAULT_OUTPUT_DIR, f"relatorio-ml-{d1}-a-{d2}.pdf")

    log.info(f"📊 Relatório ML — {args.inicio} a {args.fim} — Seções: {sections_to_build}")

    # Load section modules
    load_sections()

    # Determine what data is needed
    needed = set()
    for s in sections_to_build:
        if s in SECTION_MODULES:
            needed.update(SECTION_MODULES[s].needs_data())
    log.info(f"   Dados necessários: {needed}")

    # Refresh & load tokens
    log.info("🔄 Renovando tokens...")
    refresh_tokens()
    token_vendas = load_token('vendas')
    token_finance = load_token('finance')

    # Fetch only what's needed
    data = {}
    if 'orders' in needed:
        log.info("   → Pedidos...")
        data['orders'] = fetch_orders(args.inicio, args.fim, token_vendas)
        log.info(f"     {len(data['orders'])} pedidos")
    if 'payments' in needed:
        log.info("   → Pagamentos...")
        data['payments'] = fetch_payments(args.inicio, args.fim, token_finance)
        log.info(f"     {len(data['payments'])} pagamentos")
    if 'seller_info' in needed:
        log.info("   → Info do vendedor...")
        data['seller_info'] = fetch_seller_info(token_vendas)
    if 'items' in needed or 'items_total' in needed:
        log.info("   → Anúncios...")
        items, total = fetch_active_items(token_vendas)
        data['items'] = items
        data['items_total'] = total
        log.info(f"     {total} ativos")

    # Build sections
    log.info("🔨 Construindo seções...")
    sections_html = ''
    for s in sections_to_build:
        if s not in SECTION_MODULES:
            log.warning(f"   Seção {s} não encontrada")
            continue
        log.info(f"   → Seção {s}...")
        try:
            sections_html += SECTION_MODULES[s].build(**data)
        except Exception as e:
            log.error(f"   Erro seção {s}: {e}")
            import traceback
            traceback.print_exc()
            sections_html += f'<div class="page"><div class="section-header"><span class="section-number">{s:02d}</span><h2>Erro</h2></div><p>{e}</p></div>'

    # Build HTML
    d1_display = datetime.strptime(args.inicio, '%Y-%m-%d').strftime('%d/%m/%Y')
    d2_display = datetime.strptime(args.fim, '%Y-%m-%d').strftime('%d/%m/%Y')
    periodo = f"{d1_display} a {d2_display}"

    sections_html = sections_html.replace('{{periodo_display}}', periodo)
    html = wrap_html(sections_html, periodo, periodo)

    # Save HTML
    html_path = args.output.replace('.pdf', '.html')
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # PDF
    log.info("📄 Gerando PDF...")
    try:
        subprocess.run([
            'wkhtmltopdf', '--page-size', 'A4',
            '--margin-top', '10mm', '--margin-bottom', '15mm',
            '--margin-left', '10mm', '--margin-right', '10mm',
            '--encoding', 'UTF-8', '--enable-local-file-access',
            '--javascript-delay', '1000', '--no-stop-slow-scripts',
            '--print-media-type', html_path, args.output
        ], capture_output=True, text=True, timeout=60)

        if os.path.exists(args.output):
            log.info(f"   ✅ PDF: {args.output}")
        else:
            log.error("   PDF não gerado")
    except Exception as e:
        log.error(f"   Erro PDF: {e}")

    if not args.debug and os.path.exists(html_path):
        os.remove(html_path)

    print(f"\n✅ Relatório: {args.output}")
    print(f"   Período: {periodo}")
    print(f"   Seções: {len(sections_to_build)}")


if __name__ == "__main__":
    main()
