#!/usr/bin/env python3
"""
meta-ads-report.py — Relatório de Performance Meta Ads
GB Importadora / KOBE.OPENCLAW

Uso:
  python3 meta-ads-report.py --days 7
  python3 meta-ads-report.py --days 30 --level adset
  python3 meta-ads-report.py --days 90 --level ad --output relatorio.json
  python3 meta-ads-report.py --campaign 120xxxxxxxxxx --days 14
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("Erro: requests não instalado. Execute: pip3 install requests tabulate")
    sys.exit(1)

try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

# ─── Configurações ──────────────────────────────────────────────────────────
AD_ACCOUNT = "act_323534883953033"
API_VERSION = "v21.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"
TOKEN_OP_PATH = "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/access_token"

DATE_PRESETS = {
    7: "last_7d",
    14: "last_14d",
    28: "last_28d",
    30: "last_30d",
    90: "last_90d",
}

FIELDS_BY_LEVEL = {
    "campaign": [
        "campaign_id",
        "campaign_name",
        "spend",
        "impressions",
        "reach",
        "clicks",
        "ctr",
        "cpm",
        "cpc",
        "frequency",
        "actions",
        "action_values",
        "purchase_roas",
        "cost_per_action_type",
    ],
    "adset": [
        "adset_id",
        "adset_name",
        "campaign_name",
        "spend",
        "impressions",
        "clicks",
        "ctr",
        "cpm",
        "cpc",
        "frequency",
        "actions",
        "purchase_roas",
        "cost_per_action_type",
    ],
    "ad": [
        "ad_id",
        "ad_name",
        "adset_name",
        "campaign_name",
        "spend",
        "impressions",
        "clicks",
        "ctr",
        "cpm",
        "cpc",
        "frequency",
        "actions",
        "purchase_roas",
    ],
}

# ─── Funções auxiliares ──────────────────────────────────────────────────────

def get_token():
    """Obtém token do 1Password via op read."""
    try:
        result = subprocess.run(
            ["op", "read", TOKEN_OP_PATH],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            print(f"Erro ao obter token do 1Password: {result.stderr.strip()}")
            print("Certifique-se que o 1Password CLI está instalado e autenticado.")
            sys.exit(1)
        return result.stdout.strip()
    except FileNotFoundError:
        print("Erro: 'op' (1Password CLI) não encontrado.")
        print("Instale: https://developer.1password.com/docs/cli/get-started/")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("Timeout ao consultar 1Password.")
        sys.exit(1)


def api_get(url, params, max_retries=3):
    """Faz GET com retry e exponential backoff."""
    import time, random
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, params=params, timeout=30)
            if resp.status_code == 429:
                wait = (2 ** attempt) + random.uniform(0, 1)
                print(f"Rate limit atingido. Aguardando {wait:.1f}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                print(f"Erro na requisição: {e}")
                sys.exit(1)
            time.sleep(2 ** attempt)
    return {}


def paginate(url, params):
    """Coleta todas as páginas de um endpoint paginado."""
    all_data = []
    while url:
        data = api_get(url, params)
        if "error" in data:
            print(f"Erro da API: {data['error'].get('message', data['error'])}")
            sys.exit(1)
        all_data.extend(data.get("data", []))
        # Seguir paginação
        paging = data.get("paging", {})
        url = paging.get("next")
        params = {}  # params já estão embutidos no next URL
    return all_data


def extract_action_value(actions, action_type):
    """Extrai valor de um tipo específico de ação."""
    if not actions:
        return None
    for action in actions:
        if action.get("action_type") == action_type:
            return action.get("value")
    return None


def format_currency(value):
    """Formata valor em R$."""
    if value is None:
        return "—"
    try:
        return f"R${float(value):.2f}"
    except (ValueError, TypeError):
        return str(value)


def format_percent(value):
    """Formata percentual."""
    if value is None:
        return "—"
    try:
        return f"{float(value):.2f}%"
    except (ValueError, TypeError):
        return str(value)


def format_roas(value):
    """Formata ROAS."""
    if value is None:
        return "—"
    try:
        if isinstance(value, list):
            # purchase_roas retorna lista
            for item in value:
                if item.get("action_type") == "omni_purchase":
                    return f"{float(item['value']):.2f}x"
            return "—"
        return f"{float(value):.2f}x"
    except (ValueError, TypeError):
        return str(value)


def build_summary_row(row, level):
    """Constrói linha da tabela de resumo."""
    actions = row.get("actions", [])
    purchase_roas = row.get("purchase_roas", [])
    cost_per_action = row.get("cost_per_action_type", [])

    purchases = extract_action_value(actions, "omni_purchase") or \
                extract_action_value(actions, "purchase")
    cpp = extract_action_value(cost_per_action, "omni_purchase") or \
          extract_action_value(cost_per_action, "purchase")

    if level == "campaign":
        name_field = row.get("campaign_name", row.get("campaign_id", "?"))
    elif level == "adset":
        name_field = row.get("adset_name", row.get("adset_id", "?"))
    else:
        name_field = row.get("ad_name", row.get("ad_id", "?"))

    return {
        "Nome": name_field[:50],
        "Gasto": format_currency(row.get("spend")),
        "Impressões": int(row.get("impressions", 0)),
        "Cliques": int(row.get("clicks", 0)),
        "CTR": format_percent(row.get("ctr")),
        "CPM": format_currency(row.get("cpm")),
        "CPC": format_currency(row.get("cpc")),
        "Freq.": f"{float(row.get('frequency', 0)):.2f}",
        "Compras": purchases or "—",
        "CPP": format_currency(cpp),
        "ROAS": format_roas(purchase_roas),
    }


def print_table(rows, title=""):
    """Imprime tabela formatada."""
    if not rows:
        print("Sem dados.")
        return
    if title:
        print(f"\n{'='*80}")
        print(f"  {title}")
        print(f"{'='*80}")
    if HAS_TABULATE:
        print(tabulate(rows, headers="keys", tablefmt="rounded_outline", floatfmt=".2f"))
    else:
        # Fallback sem tabulate
        if rows:
            headers = list(rows[0].keys())
            print(" | ".join(headers))
            print("-" * 120)
            for row in rows:
                print(" | ".join(str(v) for v in row.values()))


def get_insights(token, account_id, level, date_preset, campaign_id=None, since=None, until=None):
    """Busca insights da conta ou de uma campanha específica."""
    if campaign_id:
        url = f"{BASE_URL}/{campaign_id}/insights"
    else:
        url = f"{BASE_URL}/{account_id}/insights"

    fields = FIELDS_BY_LEVEL.get(level, FIELDS_BY_LEVEL["campaign"])

    params = {
        "access_token": token,
        "fields": ",".join(fields),
        "level": level,
        "limit": 100,
    }

    if since and until:
        import json as _json
        params["time_range"] = _json.dumps({"since": since, "until": until})
    else:
        params["date_preset"] = date_preset

    return paginate(url, params)


def get_campaigns_status(token, account_id):
    """Busca status atual das campanhas (não insights)."""
    url = f"{BASE_URL}/{account_id}/campaigns"
    params = {
        "access_token": token,
        "fields": "id,name,objective,status,daily_budget,lifetime_budget",
        "limit": 100,
    }
    return paginate(url, params)


def print_campaigns_status(campaigns):
    """Imprime status das campanhas."""
    print(f"\n{'='*80}")
    print("  STATUS DAS CAMPANHAS")
    print(f"{'='*80}")
    rows = []
    for c in campaigns:
        budget = c.get("daily_budget") or c.get("lifetime_budget")
        budget_str = format_currency(float(budget) / 100) if budget else "—"
        budget_type = "dia" if c.get("daily_budget") else "total" if c.get("lifetime_budget") else "—"
        rows.append({
            "ID": c.get("id", ""),
            "Nome": c.get("name", "")[:50],
            "Objetivo": c.get("objective", ""),
            "Status": c.get("status", ""),
            "Budget": f"{budget_str}/{budget_type}",
        })
    if HAS_TABULATE:
        print(tabulate(rows, headers="keys", tablefmt="rounded_outline"))
    else:
        for row in rows:
            print(row)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Report — GB Importadora",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Relatório de campanhas dos últimos 7 dias
  python3 meta-ads-report.py --days 7

  # Relatório de ad sets dos últimos 30 dias
  python3 meta-ads-report.py --days 30 --level adset

  # Relatório de ads (criativos) dos últimos 14 dias
  python3 meta-ads-report.py --days 14 --level ad

  # Relatório de uma campanha específica
  python3 meta-ads-report.py --campaign 120xxxxxxxxxx --days 7 --level adset

  # Salvar JSON
  python3 meta-ads-report.py --days 30 --output relatorio_mensal.json

  # Ver status atual das campanhas (sem métricas)
  python3 meta-ads-report.py --status-only
        """
    )
    parser.add_argument("--days", type=int, default=7,
                        choices=[7, 14, 28, 30, 90],
                        help="Período em dias (padrão: 7)")
    parser.add_argument("--since", type=str, default=None,
                        help="Data início YYYY-MM-DD (para range manual, ex: --since 2025-01-01 --until 2026-03-19)")
    parser.add_argument("--until", type=str, default=None,
                        help="Data fim YYYY-MM-DD (usar com --since)")
    parser.add_argument("--level", choices=["campaign", "adset", "ad"],
                        default="campaign",
                        help="Nível de análise (padrão: campaign)")
    parser.add_argument("--campaign", type=str, default=None,
                        help="ID de campanha específica (opcional)")
    parser.add_argument("--account", type=str, default=AD_ACCOUNT,
                        help=f"Ad Account ID (padrão: {AD_ACCOUNT})")
    parser.add_argument("--output", type=str, default=None,
                        help="Arquivo JSON para salvar os dados brutos")
    parser.add_argument("--status-only", action="store_true",
                        help="Apenas mostrar status das campanhas sem métricas")
    parser.add_argument("--raw", action="store_true",
                        help="Imprimir JSON bruto (sem tabela)")

    args = parser.parse_args()

    print(f"🔐 Obtendo token do 1Password...")
    token = get_token()
    print(f"✅ Token obtido")

    # Status only
    if args.status_only:
        print(f"\n📊 Buscando status das campanhas ({args.account})...")
        campaigns = get_campaigns_status(token, args.account)
        print_campaigns_status(campaigns)
        print(f"\nTotal: {len(campaigns)} campanhas")
        return

    # Resolver date_preset ou range manual
    date_preset = DATE_PRESETS.get(args.days, "last_7d")
    print(f"\n📊 Buscando insights...")
    print(f"   Conta: {args.account}")
    if args.since and args.until:
        print(f"   Período: {args.since} → {args.until}")
    else:
        print(f"   Período: últimos {args.days} dias ({date_preset})")
    print(f"   Nível: {args.level}")
    if args.campaign:
        print(f"   Campanha: {args.campaign}")

    data = get_insights(token, args.account, args.level, date_preset, args.campaign,
                        since=args.since, until=args.until)

    if not data:
        print("\n⚠️  Nenhum dado retornado. Possíveis causas:")
        print("   - Sem campanhas ativas no período")
        print("   - Sem gasto no período selecionado")
        print("   - Conta sem histórico de dados")
        return

    # Raw mode
    if args.raw:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    # Montar tabela
    rows = [build_summary_row(row, args.level) for row in data]

    # Calcular totais
    total_spend = sum(float(row.get("spend", 0)) for row in data)
    total_impressions = sum(int(row.get("impressions", 0)) for row in data)
    total_clicks = sum(int(row.get("clicks", 0)) for row in data)
    total_purchases = sum(
        float(extract_action_value(row.get("actions", []), "omni_purchase") or
              extract_action_value(row.get("actions", []), "purchase") or 0)
        for row in data
    )

    # Ordenar por gasto (maior primeiro)
    rows.sort(key=lambda x: float(str(x["Gasto"]).replace("R$", "").replace("—", "0").replace(",", ".")), reverse=True)

    title = f"PERFORMANCE POR {args.level.upper()} — Últimos {args.days} dias | {args.account}"
    print_table(rows, title)

    # Totais
    print(f"\n{'─'*80}")
    print(f"  TOTAIS | Gasto: {format_currency(total_spend)} | "
          f"Impressões: {total_impressions:,} | "
          f"Cliques: {total_clicks:,} | "
          f"Compras: {total_purchases:.0f}")
    avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
    print(f"  CTR médio: {avg_ctr:.2f}% | "
          f"CPP médio: {format_currency(total_spend/total_purchases if total_purchases > 0 else None)}")
    print(f"{'─'*80}")

    # Avisos
    for row in data:
        freq = float(row.get("frequency", 0))
        name = row.get("campaign_name") or row.get("adset_name") or row.get("ad_name", "?")
        if freq > 3.0:
            print(f"\n⚠️  Alta frequência ({freq:.2f}): {name[:60]}")

    print(f"\nTotal de {args.level}s: {len(data)}")

    # Salvar JSON
    if args.output:
        output_data = {
            "generated_at": datetime.now().isoformat(),
            "account": args.account,
            "period_days": args.days,
            "date_preset": date_preset,
            "level": args.level,
            "total_items": len(data),
            "totals": {
                "spend": total_spend,
                "impressions": total_impressions,
                "clicks": total_clicks,
                "purchases": total_purchases,
                "avg_ctr_pct": avg_ctr,
            },
            "data": data,
        }
        output_path = args.output
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"\n💾 Dados salvos em: {output_path}")
    else:
        # Salvar automaticamente em /tmp com timestamp
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        auto_output = f"/tmp/meta-ads-report-{ts}.json"
        output_data = {
            "generated_at": datetime.now().isoformat(),
            "account": args.account,
            "period_days": args.days,
            "data": data,
        }
        with open(auto_output, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"\n💾 JSON salvo automaticamente em: {auto_output}")


if __name__ == "__main__":
    main()
