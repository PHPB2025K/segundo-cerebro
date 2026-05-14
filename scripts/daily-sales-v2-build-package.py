#!/usr/bin/env python3
"""Daily Sales Report v2.5 — Fase 1: pacote validado por plataforma.

Gera um JSON canônico e auditável para alimentar o pipeline em camadas:
Estratégica → Tática → Operacional → Granular → Condensadora → Slack Writer → QA.

Este script NÃO chama LLM, NÃO gera Slack e NÃO envia nada. Ele só consolida dados
validados em janela BRT a partir de `orders`, preservando identidade real de pedidos
(ASIN/platform_item_id/título) para reduzir risco de produto errado.

Uso:
    python3 scripts/daily-sales-v2-build-package.py 2026-05-12 --write
    python3 scripts/daily-sales-v2-build-package.py 2026-05-12 --stdout
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

WORKSPACE = Path(__file__).resolve().parent.parent
ANALYZER_PATH = WORKSPACE / "scripts" / "daily-sales-v2-analyzer.py"
OUTPUT_BASE = WORKSPACE / "reports" / "daily-sales-report-v2" / "layered" / "packages"

RECIPIENTS = {
    "Lucas": {"platform": "shopee", "accounts": ["shopee-budamix-store", "shopee-budamix-oficial-2", "shopee-budamix-shop-3"]},
    "Yasmin": {"platform": "ml", "accounts": ["mercado-livre"]},
    "Leonardo": {"platform": "amazon", "accounts": ["amazon"]},
}

PROMPTS = {
    "strategic": "prompts/daily-sales/camada-1-estrategica.md",
    "tactical": "prompts/daily-sales/camada-2-tatica.md",
    "operational": "prompts/daily-sales/camada-3-operacional.md",
    "granular": "prompts/daily-sales/camada-4-granular.md",
    "condenser": "prompts/daily-sales/camada-5-condensadora.md",
    "slack_writer": "prompts/daily-sales/camada-6-slack-writer.md",
    "qa_gate": "prompts/daily-sales/camada-7-qa-gate.md",
}


def load_analyzer():
    spec = importlib.util.spec_from_file_location("daily_sales_v2_analyzer", ANALYZER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Não foi possível carregar analyzer em {ANALYZER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pct(current: float, baseline: float) -> float | None:
    if not baseline:
        return None
    return round(((current - baseline) / baseline) * 100, 1)


def json_safe(value: Any) -> Any:
    """Converte objetos básicos para JSON seguro."""
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [json_safe(v) for v in value]
    if isinstance(value, tuple):
        return [json_safe(v) for v in value]
    return value


def build_account_package(analyzer, sb, date_str: str, account_slug: str, canonical_by_platform: dict[str, Any]) -> dict[str, Any]:
    acct = analyzer.ACCOUNTS[account_slug]
    orders, cancelled = analyzer.fetch_orders(sb, date_str, account_slug)
    metrics = analyzer.compute_metrics(orders, cancelled)
    hist30 = analyzer.fetch_historical_orders(sb, date_str, 30, account_slug)
    hist60 = analyzer.fetch_historical_orders(sb, date_str, 60, account_slug)
    avg30 = analyzer.compute_historical_avg(hist30, 30)
    avg60 = analyzer.compute_historical_avg(hist60, 60)
    same_weekday = analyzer.fetch_same_weekday_orders(sb, date_str, account_slug, count=4)
    weekday_avg = {
        "avg_orders": round(sum(d["orders"] for d in same_weekday) / len(same_weekday), 2) if same_weekday else 0,
        "avg_gmv": round(sum(d["gmv"] for d in same_weekday) / len(same_weekday), 2) if same_weekday else 0,
    }
    weekday_avg["avg_ticket"] = round(weekday_avg["avg_gmv"] / weekday_avg["avg_orders"], 2) if weekday_avg["avg_orders"] else 0

    # Contas Shopee são subconjuntos do total da plataforma. Reconciliar cada
    # conta isolada contra o total Shopee cria falso bloqueio; a igualdade só
    # vale para plataformas sem divisão por shop_id (ML/Amazon) ou para o
    # consolidado do responsável.
    if "shop_id" in acct["filter"]:
        canonical = canonical_by_platform.get(acct["platform"], {})
        reconciliation = {
            "scope": "account_subset",
            "platform": acct["platform"],
            "canonical_orders": int(canonical.get("order_count") or 0),
            "canonical_revenue": round(float(canonical.get("total_revenue") or 0), 2),
            "orders_count": metrics["pedidos_validos"],
            "orders_revenue": round(metrics["gmv"], 2),
            "order_delta": None,
            "revenue_delta": None,
            "ok": (
                metrics["pedidos_validos"] <= int(canonical.get("order_count") or 0)
                and round(metrics["gmv"], 2) <= round(float(canonical.get("total_revenue") or 0), 2) + 1.00
            ),
            "note": "Conta Shopee é subconjunto do total da plataforma; igualdade deve ser validada no consolidado Lucas/Shopee.",
        }
    else:
        reconciliation = analyzer.reconciliation_for_platform(
            canonical_by_platform,
            acct["platform"],
            metrics["pedidos_validos"],
            metrics["gmv"],
        )

    memory_context = analyzer.read_account_memory(account_slug)
    memory_loaded = sorted(k for k in memory_context.keys() if k != "last_daily")

    return {
        "account_slug": account_slug,
        "account_name": acct["name"],
        "platform": acct["platform"],
        "responsavel": acct["responsavel"],
        "ads_owner": acct["ads"],
        "filter": acct["filter"],
        "metrics": metrics,
        "historical": {
            "avg_30d": avg30,
            "avg_60d": avg60,
            "same_weekday_last_4": same_weekday,
            "same_weekday_avg": weekday_avg,
            "changes": {
                "orders_vs_30d_pct": pct(metrics["pedidos_validos"], avg30.get("avg_orders") or 0),
                "gmv_vs_30d_pct": pct(metrics["gmv"], avg30.get("avg_gmv") or 0),
                "ticket_vs_30d_pct": pct(metrics["ticket_medio"], avg30.get("avg_ticket") or 0),
                "orders_vs_60d_pct": pct(metrics["pedidos_validos"], avg60.get("avg_orders") or 0),
                "gmv_vs_60d_pct": pct(metrics["gmv"], avg60.get("avg_gmv") or 0),
                "ticket_vs_60d_pct": pct(metrics["ticket_medio"], avg60.get("avg_ticket") or 0),
                "orders_vs_same_weekday_pct": pct(metrics["pedidos_validos"], weekday_avg.get("avg_orders") or 0),
                "gmv_vs_same_weekday_pct": pct(metrics["gmv"], weekday_avg.get("avg_gmv") or 0),
            },
        },
        "reconciliation": reconciliation,
        "memory": {
            "loaded_keys": memory_loaded,
            "last_daily_file": memory_context.get("last_daily_file"),
            "has_weekly": "weekly.md" in memory_context,
            "has_monthly": "monthly.md" in memory_context,
            "has_rules": "rules.md" in memory_context,
            "has_himmel_context": "account-himmel-context.md" in memory_context or "global-himmel-context.md" in memory_context,
            "has_marketplace_rules": "marketplace-rules-watch.md" in memory_context,
        },
        "quality_flags": quality_flags(acct, metrics, reconciliation, memory_context),
    }


def quality_flags(acct: dict[str, Any], metrics: dict[str, Any], reconciliation: dict[str, Any], memory_context: dict[str, Any]) -> list[dict[str, str]]:
    flags: list[dict[str, str]] = []
    if not reconciliation.get("ok"):
        if reconciliation.get("scope") == "account_subset":
            flags.append({"level": "critical", "code": "account_subset_exceeds_platform_total", "message": "Conta Shopee excede o total canônico da plataforma; provável erro de filtro/shop_id."})
        else:
            flags.append({"level": "critical", "code": "reconciliation_mismatch", "message": "Orders granular divergem da fonte canônica BRT."})
    if metrics.get("pedidos_validos", 0) == 0:
        flags.append({"level": "warning", "code": "no_orders", "message": "Sem pedidos válidos na janela BRT."})
    if metrics.get("top3_concentration", 0) >= 70:
        flags.append({"level": "warning", "code": "high_top3_concentration", "message": "Alta concentração nos top 3 produtos."})
    if acct["platform"] == "amazon":
        for product in metrics.get("top_products", []):
            if not product.get("platform_item_id") and not product.get("title"):
                flags.append({"level": "critical", "code": "amazon_product_identity_missing", "message": "Produto Amazon sem ASIN/platform_item_id e sem título real."})
                break
    if not memory_context.get("last_daily_file"):
        flags.append({"level": "info", "code": "no_previous_daily_memory", "message": "Sem análise diária anterior carregada."})
    return flags


def build_package(date_str: str) -> dict[str, Any]:
    analyzer = load_analyzer()
    sb = analyzer.get_supabase()
    canonical_by_platform = analyzer.fetch_v_daily_sales(sb, date_str)
    start_utc, end_utc = analyzer.brt_window(date_str)

    accounts: dict[str, Any] = {}
    for account_slug in analyzer.ACCOUNTS:
        accounts[account_slug] = build_account_package(analyzer, sb, date_str, account_slug, canonical_by_platform)

    recipients: dict[str, Any] = {}
    for recipient, cfg in RECIPIENTS.items():
        platform = cfg["platform"]
        account_slugs = cfg["accounts"]
        recipient_accounts = [accounts[slug] for slug in account_slugs]
        totals = {
            "orders": sum(a["metrics"]["pedidos_validos"] for a in recipient_accounts),
            "gmv": round(sum(a["metrics"]["gmv"] for a in recipient_accounts), 2),
            "cancelamentos": sum(a["metrics"]["cancelamentos"] for a in recipient_accounts),
        }
        totals["ticket_medio"] = round(totals["gmv"] / totals["orders"], 2) if totals["orders"] else 0
        recipients[recipient] = {
            "recipient": recipient,
            "platform": platform,
            "accounts": account_slugs,
            "totals": totals,
            "canonical_platform_total": canonical_by_platform.get(platform),
        }

    package = {
        "schema_version": "daily-sales-layered-package/v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "date": date_str,
        "brt_window": {"start_utc": start_utc, "end_utc": end_utc, "display": "00:00–23:59 BRT"},
        "source_of_truth": {
            "orders": "Supabase orders em janela BRT, cancelados excluídos dos totais válidos",
            "amazon_products": "orders.items/orderItems: platform_item_id/ASIN + título real do pedido",
            "shopee_accounts": "orders.shop_id",
        },
        "pipeline": {
            "mode": "preview/shadow-ready",
            "prompts": PROMPTS,
            "send_real_allowed": False,
        },
        "canonical_by_platform": canonical_by_platform,
        "accounts": accounts,
        "recipients": recipients,
    }
    return json_safe(package)


def write_package(package: dict[str, Any], date_str: str) -> Path:
    out_dir = OUTPUT_BASE / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "package.json"
    out_file.write_text(json.dumps(package, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return out_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Build validated Daily Sales layered package")
    parser.add_argument("date", help="Data analisada em YYYY-MM-DD (BRT)")
    parser.add_argument("--write", action="store_true", help="Salvar em reports/daily-sales-report-v2/layered/packages/YYYY-MM-DD/package.json")
    parser.add_argument("--stdout", action="store_true", help="Imprimir JSON no stdout")
    args = parser.parse_args()

    # valida formato cedo
    datetime.strptime(args.date, "%Y-%m-%d")
    package = build_package(args.date)

    out_file = None
    if args.write or not args.stdout:
        out_file = write_package(package, args.date)
    if args.stdout:
        print(json.dumps(package, ensure_ascii=False, indent=2, sort_keys=True))
    if out_file:
        print(f"Pacote validado salvo: {out_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
