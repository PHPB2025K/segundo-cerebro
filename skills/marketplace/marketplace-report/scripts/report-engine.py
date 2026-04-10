#!/usr/bin/env python3
"""
Report Engine — Marketplace Universal
Orquestrador: carrega connector + seções → HTML.

Uso:
    python3 report-engine.py --plataforma ml --inicio 2026-03-01 --fim 2026-03-15
    python3 report-engine.py --plataforma all --inicio 2026-03-01 --fim 2026-03-15
    python3 report-engine.py --plataforma ml --secoes 1,2,6 --inicio 2026-03-01 --fim 2026-03-15
"""

import argparse
import logging
import os
import subprocess
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

DEFAULT_OUTPUT_DIR = os.path.expanduser('~/.openclaw/workspace/reports')
log = logging.getLogger('report-engine')

# ─── Connector Registry ─────────────────────────────────────────────────────

CONNECTORS = {}

def load_connector(platform):
    if platform in CONNECTORS:
        return CONNECTORS[platform]
    try:
        mod = __import__(f"connectors.{platform}", fromlist=['fetch_all'])
        CONNECTORS[platform] = mod
        return mod
    except Exception as e:
        log.error(f"Connector {platform} não encontrado: {e}")
        return None

PLATFORM_MAP = {
    'ml': 'mercadolivre',
    'mercadolivre': 'mercadolivre',
    'amazon': 'amazon',
    'shopee': 'shopee',
}

# ─── Section Registry ────────────────────────────────────────────────────────

SECTION_MODULES = {}

def load_sections():
    sections_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sections')
    for i in range(1, 10):
        for f in os.listdir(sections_dir):
            if f.startswith(f"s{i:02d}_") and f.endswith('.py'):
                mod_name = f"sections.{f[:-3]}"
                try:
                    mod = __import__(mod_name, fromlist=['build', 'needs_data'])
                    SECTION_MODULES[i] = mod
                except Exception as e:
                    log.error(f"Erro seção {i}: {e}")
                break

# ─── CSS ─────────────────────────────────────────────────────────────────────


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Report Engine — Marketplaces")
    parser.add_argument("--plataforma", required=True, help="ml, amazon, shopee ou all")
    parser.add_argument("--inicio", required=True)
    parser.add_argument("--fim", required=True)
    parser.add_argument("--secoes", default="all")
    parser.add_argument("--output", default=None)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s')

    sections_to_build = list(range(1, 10)) if args.secoes == 'all' else [int(s) for s in args.secoes.split(',')]

    # Resolve platforms
    if args.plataforma == 'all':
        platforms = ['mercadolivre', 'amazon', 'shopee']
    else:
        p = PLATFORM_MAP.get(args.plataforma, args.plataforma)
        platforms = [p]

    if not args.output:
        d1 = args.inicio[5:].replace('-', '')
        d2 = args.fim[5:].replace('-', '')
        plat_label = args.plataforma.upper()
        args.output = os.path.join(DEFAULT_OUTPUT_DIR, f"relatorio-{plat_label}-{d1}-a-{d2}.html")

    log.info(f"📊 Relatório — {', '.join(platforms)} — {args.inicio} a {args.fim}")

    # Load sections
    load_sections()

    # Determine needed data
    needed = set()
    for s in sections_to_build:
        if s in SECTION_MODULES:
            needed.update(SECTION_MODULES[s].needs_data())
    log.info(f"   Dados necessários: {needed}")

    # Fetch data from each platform
    all_platform_data = {}
    for platform in platforms:
        connector = load_connector(platform)
        if connector:
            data = connector.fetch_all(args.inicio, args.fim, needed)
            all_platform_data[platform] = data

    # For single platform, use directly. For multi, merge later.
    if len(platforms) == 1:
        data = all_platform_data.get(platforms[0], {})
    else:
        # Merge: combine orders/payments/traffic/ads from all platforms
        data = {
            'platform': 'all',
            'platform_display': 'Todas as Plataformas',
            'orders': [],
            'payments': [],
            'seller_info': None,
            'items': [],
            'items_total': 0,
            'traffic': [],
            'ads': [],
        }
        for pdata in all_platform_data.values():
            data['orders'].extend(pdata.get('orders', []))
            data['payments'].extend(pdata.get('payments', []))
            if not data['seller_info'] and pdata.get('seller_info'):
                data['seller_info'] = pdata['seller_info']
            data['items'].extend(pdata.get('items', []))
            data['items_total'] += pdata.get('items_total', 0)
            data['traffic'].extend(pdata.get('traffic', []))
            data['ads'].extend(pdata.get('ads', []))
        log.info(f"   Dados combinados: {len(data['orders'])} pedidos, {len(data['payments'])} pagamentos, {len(data['traffic'])} traffic, {len(data['ads'])} ads")

    # Build sections
    log.info("🔨 Construindo seções...")
    sections_html = ''
    for s in sections_to_build:
        if s not in SECTION_MODULES:
            continue
        log.info(f"   → Seção {s}...")
        try:
            sections_html += SECTION_MODULES[s].build(**data)
        except Exception as e:
            log.error(f"   Erro seção {s}: {e}")
            import traceback
            traceback.print_exc()
            sections_html += f'<div class="page"><div class="section-header"><span class="section-number">{s:02d}</span><h2>Erro</h2></div><p>{e}</p></div>'

    # HTML
    d1_display = datetime.strptime(args.inicio, '%Y-%m-%d').strftime('%d/%m/%Y')
    d2_display = datetime.strptime(args.fim, '%Y-%m-%d').strftime('%d/%m/%Y')
    periodo = f"{d1_display} a {d2_display}"
    platform_name = data.get('platform_display', platforms[0])

    sections_html = sections_html.replace('{{periodo_display}}', periodo)
    sections_html = sections_html.replace('{{platform_display}}', platform_name)

    # Load template from file
    template_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))), 'templates', 'report-base.html')
    
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            html = f.read()
        html = html.replace('{{title}}', f'Relatório {platform_name}')
        html = html.replace('{{content}}', sections_html)
    else:
        # Fallback: inline minimal HTML
        log.warning(f"Template not found: {template_path}, using inline")
        html = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<title>Relatório {platform_name} — Budamix</title></head>
<body style="background:#0a0b10;color:#e8e9ed;font-family:Inter,sans-serif;">
<div style="max-width:860px;margin:0 auto;padding:40px 24px;">
{sections_html}
</div></body></html>'''

    # Output as HTML (not PDF)
    if not args.output:
        d1 = args.inicio[5:].replace('-', '')
        d2 = args.fim[5:].replace('-', '')
        plat_label = args.plataforma.upper()
        args.output = os.path.join(DEFAULT_OUTPUT_DIR, f"relatorio-{plat_label}-{d1}-a-{d2}.html")
    
    # Ensure .html extension
    if args.output.endswith('.pdf'):
        args.output = args.output.replace('.pdf', '.html')

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    log.info(f"   ✅ HTML: {args.output}")
    print(f"\n✅ Relatório: {args.output}")
    print(f"   Plataforma: {platform_name}")
    print(f"   Período: {periodo}")
    print(f"   Seções: {len(sections_to_build)}")


if __name__ == "__main__":
    main()
