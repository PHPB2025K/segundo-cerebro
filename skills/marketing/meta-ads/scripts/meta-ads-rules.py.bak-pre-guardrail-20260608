#!/usr/bin/env python3
"""
meta-ads-rules.py — Gerenciar Regras Automatizadas Meta Ads
GB Importadora / KOBE.OPENCLAW

Uso:
  python3 meta-ads-rules.py --list
  python3 meta-ads-rules.py --create-essentials
  python3 meta-ads-rules.py --create-essentials --dry-run
  python3 meta-ads-rules.py --delete RULE_ID
  python3 meta-ads-rules.py --pause RULE_ID
  python3 meta-ads-rules.py --resume RULE_ID
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("Erro: pip3 install requests tabulate")
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

# ─── Helpers ─────────────────────────────────────────────────────────────────

def get_token():
    try:
        result = subprocess.run(
            ["op", "read", TOKEN_OP_PATH],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            print(f"Erro 1Password: {result.stderr.strip()}")
            sys.exit(1)
        return result.stdout.strip()
    except FileNotFoundError:
        print("Erro: 'op' não encontrado.")
        sys.exit(1)


def api_request(method, url, payload=None, params=None, dry_run=False):
    """Faz requisição à API."""
    if dry_run and method in ("POST", "DELETE"):
        print(f"\n[DRY RUN] {method} {url}")
        if payload:
            # Remover token do log
            safe_payload = {k: v for k, v in payload.items() if k != "access_token"}
            print(json.dumps(safe_payload, indent=2, ensure_ascii=False))
        return {"id": "DRY_RUN_ID", "dry_run": True}

    try:
        if method == "GET":
            resp = requests.get(url, params=params, timeout=30)
        elif method == "POST":
            resp = requests.post(url, json=payload, timeout=30)
        elif method == "DELETE":
            resp = requests.delete(url, params=params or {}, timeout=30)
        else:
            raise ValueError(f"Método não suportado: {method}")

        data = resp.json()
        if "error" in data:
            print(f"\n❌ Erro API: {data['error'].get('message', str(data['error']))}")
            print(f"   Código: {data['error'].get('code')}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro conexão: {e}")
        return None


def paginate_get(url, params):
    """Coleta todas as páginas."""
    all_data = []
    while url:
        data = api_request("GET", url, params=params)
        if not data:
            break
        all_data.extend(data.get("data", []))
        paging = data.get("paging", {})
        url = paging.get("next")
        params = {}
    return all_data


# ─── Definição das regras essenciais ─────────────────────────────────────────

def get_essential_rules():
    """Retorna as 5 regras essenciais para a GB Importadora."""
    return [
        {
            "name": "[GB] 🛡️ Pausa CPA Alto (>R$150 / 7d / >1000 impr.)",
            "description": "Pausa Ad Sets com CPA acima de R$150 após dados suficientes",
            "evaluation_spec": {
                "evaluation_type": "SCHEDULE",
                "schedule_spec": {
                    "schedule_type": "DAILY",
                    "hours": [9],  # 9h UTC = 6h BRT
                    "timezone": "USER"
                },
                "filters": [
                    {"field": "entity_type", "value": "ADSET", "operator": "EQUAL"},
                    {"field": "time_preset", "value": "LAST_7_DAYS", "operator": "EQUAL"},
                    {"field": "impressions", "value": 1000, "operator": "GREATER_THAN"},
                    {"field": "cost_per", "value": 15000, "operator": "GREATER_THAN"},  # R$150 em centavos
                ]
            },
            "execution_spec": {
                "execution_type": "PAUSE"
            }
        },
        {
            "name": "[GB] 🚀 Escalar ROAS Alto (>3.5x / 3d / >R$50 gasto)",
            "description": "Aumenta budget 20% quando ROAS está acima de 3.5x por 3 dias",
            "evaluation_spec": {
                "evaluation_type": "SCHEDULE",
                "schedule_spec": {
                    "schedule_type": "DAILY",
                    "hours": [10],
                    "timezone": "USER"
                },
                "filters": [
                    {"field": "entity_type", "value": "ADSET", "operator": "EQUAL"},
                    {"field": "time_preset", "value": "LAST_3_DAYS", "operator": "EQUAL"},
                    {"field": "purchase_roas", "value": 3.5, "operator": "GREATER_THAN"},
                    {"field": "spend", "value": 5000, "operator": "GREATER_THAN"},  # R$50 mínimo
                ]
            },
            "execution_spec": {
                "execution_type": "ADJUST_BUDGET",
                "execution_options": {
                    "budget_type": "DAILY",
                    "budget_value": 1.20,
                    "budget_value_type": "MULTIPLIER"
                }
            }
        },
        {
            "name": "[GB] ⚠️ Alerta Frequência Alta (>3.0 / 7d)",
            "description": "Envia notificação quando frequência do Ad passa de 3.0",
            "evaluation_spec": {
                "evaluation_type": "CONTINUOUS",
                "filters": [
                    {"field": "entity_type", "value": "AD", "operator": "EQUAL"},
                    {"field": "time_preset", "value": "LAST_7_DAYS", "operator": "EQUAL"},
                    {"field": "frequency", "value": 3.0, "operator": "GREATER_THAN"},
                    {"field": "impressions", "value": 500, "operator": "GREATER_THAN"},
                ]
            },
            "execution_spec": {
                "execution_type": "SEND_EMAIL",
                "execution_options": {
                    "email_message": "[KOBE] Ad com frequência >3.0! Considere renovar o criativo ou ampliar a audiência."
                }
            }
        },
        {
            "name": "[GB] 💸 Pausa CTR Muito Baixo (<0.3% / 2k impr.)",
            "description": "Pausa Ads com CTR abaixo de 0.3% após 2.000 impressões",
            "evaluation_spec": {
                "evaluation_type": "SCHEDULE",
                "schedule_spec": {
                    "schedule_type": "DAILY",
                    "hours": [9],
                    "timezone": "USER"
                },
                "filters": [
                    {"field": "entity_type", "value": "AD", "operator": "EQUAL"},
                    {"field": "time_preset", "value": "LAST_7_DAYS", "operator": "EQUAL"},
                    {"field": "impressions", "value": 2000, "operator": "GREATER_THAN"},
                    {"field": "ctr", "value": 0.3, "operator": "SMALLER_THAN"},
                ]
            },
            "execution_spec": {
                "execution_type": "PAUSE"
            }
        },
        {
            "name": "[GB] 📉 Alerta Gasto Alto Sem Conversão (>R$200 / sem compra / 7d)",
            "description": "Alerta quando Ad Set gasta mais de R$200 sem nenhuma compra",
            "evaluation_spec": {
                "evaluation_type": "SCHEDULE",
                "schedule_spec": {
                    "schedule_type": "DAILY",
                    "hours": [9],
                    "timezone": "USER"
                },
                "filters": [
                    {"field": "entity_type", "value": "ADSET", "operator": "EQUAL"},
                    {"field": "time_preset", "value": "LAST_7_DAYS", "operator": "EQUAL"},
                    {"field": "spend", "value": 20000, "operator": "GREATER_THAN"},  # R$200
                    {"field": "actions:omni_purchase", "value": 0, "operator": "EQUAL"},
                ]
            },
            "execution_spec": {
                "execution_type": "SEND_EMAIL",
                "execution_options": {
                    "email_message": "[KOBE] ALERTA: Ad Set gastou mais de R$200 nos últimos 7 dias sem nenhuma compra registrada. Verificar Pixel e configuração de conversão."
                }
            }
        },
    ]


# ─── Operações ────────────────────────────────────────────────────────────────

def list_rules(token, account_id):
    """Lista todas as regras da conta."""
    url = f"{BASE_URL}/{account_id}/adrules_library"
    params = {
        "access_token": token,
        "fields": "id,name,status,evaluation_spec,execution_spec",
        "limit": 100,
    }
    rules = paginate_get(url, params)
    return rules


def print_rules(rules):
    """Imprime regras formatadas."""
    if not rules:
        print("\nNenhuma regra encontrada.")
        return

    print(f"\n{'='*80}")
    print(f"  REGRAS AUTOMATIZADAS ({len(rules)} total)")
    print(f"{'='*80}")

    rows = []
    for rule in rules:
        exec_spec = rule.get("execution_spec", {})
        eval_spec = rule.get("evaluation_spec", {})
        exec_type = exec_spec.get("execution_type", "?")
        eval_type = eval_spec.get("evaluation_type", "?")
        rows.append({
            "ID": rule.get("id", ""),
            "Nome": rule.get("name", "")[:50],
            "Status": rule.get("status", ""),
            "Avaliação": eval_type,
            "Ação": exec_type,
        })

    if HAS_TABULATE:
        print(tabulate(rows, headers="keys", tablefmt="rounded_outline"))
    else:
        for row in rows:
            print(f"  {row['ID']} | {row['Status']:8} | {row['Ação']:20} | {row['Nome']}")


def create_rule(token, account_id, rule_def, dry_run=False):
    """Cria uma regra."""
    name = rule_def["name"]
    print(f"\n  📏 Criando: {name}")

    payload = {
        "name": name,
        "evaluation_spec": json.dumps(rule_def["evaluation_spec"]),
        "execution_spec": json.dumps(rule_def["execution_spec"]),
        "access_token": token,
    }

    result = api_request("POST", f"{BASE_URL}/{account_id}/adrules_library",
                         payload=payload, dry_run=dry_run)
    if result:
        rule_id = result.get("id", "DRY_RUN_ID")
        print(f"     ✅ Criada: {rule_id}")
        return rule_id
    else:
        print(f"     ❌ Falhou")
        return None


def delete_rule(token, rule_id, dry_run=False):
    """Deleta uma regra."""
    result = api_request("DELETE", f"{BASE_URL}/{rule_id}",
                         params={"access_token": token}, dry_run=dry_run)
    if result is not None:
        print(f"✅ Regra {rule_id} deletada")
    else:
        print(f"❌ Falha ao deletar {rule_id}")


def update_rule_status(token, rule_id, status, dry_run=False):
    """Pausa ou reativa uma regra."""
    payload = {
        "status": status,
        "access_token": token,
    }
    result = api_request("POST", f"{BASE_URL}/{rule_id}", payload=payload, dry_run=dry_run)
    if result:
        print(f"✅ Regra {rule_id} → {status}")
    else:
        print(f"❌ Falha ao atualizar {rule_id}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Meta Ads Rules — GB Importadora",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  # Listar todas as regras ativas
  python3 meta-ads-rules.py --list

  # Criar as 5 regras essenciais da GB
  python3 meta-ads-rules.py --create-essentials

  # Simular criação sem chamar API
  python3 meta-ads-rules.py --create-essentials --dry-run

  # Ver detalhes das regras essenciais que seriam criadas
  python3 meta-ads-rules.py --show-essentials

  # Deletar uma regra
  python3 meta-ads-rules.py --delete 123456789

  # Pausar uma regra
  python3 meta-ads-rules.py --pause 123456789

  # Reativar uma regra
  python3 meta-ads-rules.py --resume 123456789
        """
    )

    parser.add_argument("--list", action="store_true",
                        help="Listar todas as regras da conta")
    parser.add_argument("--create-essentials", action="store_true",
                        help="Criar as 5 regras essenciais para GB Importadora")
    parser.add_argument("--show-essentials", action="store_true",
                        help="Mostrar definição das regras essenciais (sem criar)")
    parser.add_argument("--delete", type=str, metavar="RULE_ID",
                        help="Deletar regra pelo ID")
    parser.add_argument("--pause", type=str, metavar="RULE_ID",
                        help="Pausar regra pelo ID")
    parser.add_argument("--resume", type=str, metavar="RULE_ID",
                        help="Reativar regra pelo ID")
    parser.add_argument("--account", default=AD_ACCOUNT,
                        help=f"Ad Account (padrão: {AD_ACCOUNT})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Simular sem chamar a API")
    parser.add_argument("--detail", type=str, metavar="RULE_ID",
                        help="Ver detalhes completos de uma regra")

    args = parser.parse_args()

    # Show essentials não precisa de token
    if args.show_essentials:
        rules = get_essential_rules()
        print(f"\n📋 REGRAS ESSENCIAIS GB IMPORTADORA ({len(rules)} regras)\n")
        for i, rule in enumerate(rules, 1):
            print(f"\n{'─'*60}")
            print(f"Regra {i}: {rule['name']}")
            print(f"Descrição: {rule['description']}")
            print(f"\nEvaluation Spec:")
            print(json.dumps(rule['evaluation_spec'], indent=4, ensure_ascii=False))
            print(f"\nExecution Spec:")
            print(json.dumps(rule['execution_spec'], indent=4, ensure_ascii=False))
        return

    print(f"🔐 Obtendo token do 1Password...")
    token = get_token()
    print(f"✅ Token obtido")

    if args.dry_run:
        print(f"\n🔷 MODO DRY RUN\n")

    if args.list:
        print(f"\n📋 Listando regras da conta {args.account}...")
        rules = list_rules(token, args.account)
        print_rules(rules)
        return

    if args.detail:
        rules = list_rules(token, args.account)
        rule = next((r for r in rules if r.get("id") == args.detail), None)
        if rule:
            print(json.dumps(rule, indent=2, ensure_ascii=False))
        else:
            print(f"Regra {args.detail} não encontrada.")
        return

    if args.delete:
        print(f"\n🗑️  Deletando regra {args.delete}...")
        delete_rule(token, args.delete, args.dry_run)
        return

    if args.pause:
        print(f"\n⏸️  Pausando regra {args.pause}...")
        update_rule_status(token, args.pause, "PAUSED", args.dry_run)
        return

    if args.resume:
        print(f"\n▶️  Reativando regra {args.resume}...")
        update_rule_status(token, args.resume, "ENABLED", args.dry_run)
        return

    if args.create_essentials:
        print(f"\n🔧 Criando regras essenciais para GB Importadora...")
        print(f"   Conta: {args.account}")
        rules = get_essential_rules()
        created = []
        failed = []

        for rule in rules:
            rule_id = create_rule(token, args.account, rule, args.dry_run)
            if rule_id:
                created.append({"name": rule["name"], "id": rule_id})
            else:
                failed.append(rule["name"])

        print(f"\n{'='*60}")
        print(f"  RESULTADO")
        print(f"{'='*60}")
        print(f"  ✅ Criadas: {len(created)}")
        print(f"  ❌ Falhas: {len(failed)}")

        if created:
            print(f"\n  Regras criadas:")
            for r in created:
                print(f"    {r['id']}: {r['name'][:55]}")

        if failed:
            print(f"\n  Falhas:")
            for name in failed:
                print(f"    ❌ {name[:60]}")

        print(f"\n📋 Para ver todas as regras ativas:")
        print(f"   python3 meta-ads-rules.py --list")
        return

    # Default: mostrar ajuda
    parser.print_help()


if __name__ == "__main__":
    main()
