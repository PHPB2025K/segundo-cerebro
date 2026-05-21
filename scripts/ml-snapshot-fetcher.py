#!/usr/bin/env python3
"""
ml-snapshot-fetcher.py — Snapshot diário da conta Mercado Livre.

Roda 1x por dia, ANTES do daily-sales-data-builder.py, e produz um JSON
com dados de ESTADO ATUAL da conta ML que o Supabase não tem:
  - Reputação (cor, power_seller_status, métricas)
  - Detalhes dos top 10 anúncios do dia (listing_type, catalog, status,
    free_shipping, logistic_type, health)
  - Mix de fulfillment calculado (% Full / Flex / Coletado dos top anúncios,
    ponderado por número de pedidos)
  - Resumo Mercado Ads (campanhas ativas, gasto, receita ADS)

O resultado é colado pelo data builder dentro de
  package.json -> platforms["mercado-livre"]["ml_snapshot"]

Filosofia:
  - Falha de uma API NÃO derruba o script. Cada bloco tem seu próprio
    "status" (ok | unavailable). Se tudo falhar, usa cache do último dia OK.
  - Top items são consultados APENAS pra os platform_item_ids do top_products
    do dia, vindos do package parcial passado em --top-items-from.

Uso:
    ./ml-snapshot-fetcher.py \\
        --date 2026-05-21 \\
        --top-items-from /tmp/package-parcial.json \\
        --output /tmp/ml-snapshot-2026-05-21.json
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Reusa connector existente — adiciona path do vault
CONNECTOR_DIR = Path(
    "/root/segundo-cerebro/skills/marketplace/marketplace-report/scripts/connectors"
)
if not CONNECTOR_DIR.exists():
    # fallback pra path local (desenvolvimento)
    CONNECTOR_DIR = Path.home() / "segundo-cerebro/skills/marketplace/marketplace-report/scripts/connectors"

sys.path.insert(0, str(CONNECTOR_DIR))

import mercadolivre as ml_conn  # noqa: E402

# ─── Logging ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("ml-snapshot")

# ─── Constants ────────────────────────────────────────────────────────────────

ML_LOGISTIC_TYPE_TO_BUCKET = {
    "fulfillment": "full",       # Mercado Envios Full
    "cross_docking": "flex",     # Mercado Envios Flex
    "self_service": "self_service",  # Coletado / Colocado
    "drop_off": "self_service",  # Postagem ag. Mercado Livre
    "xd_drop_off": "self_service",
}

# ─── Blocos do snapshot ───────────────────────────────────────────────────────


def build_reputation_block(token):
    """Chama /users/{USER_ID} e extrai reputação + métricas oficiais ML."""
    info = ml_conn.fetch_seller_info(token)
    if not info:
        return {"status": "unavailable", "error": "fetch_seller_info returned None"}

    rep = info.get("seller_reputation") or {}
    metrics = rep.get("metrics") or {}

    def _rate(key):
        node = metrics.get(key) or {}
        return node.get("rate")

    return {
        "status": "ok",
        "color": rep.get("level_id"),                   # ex: "5_green"
        "power_seller_status": rep.get("power_seller_status"),  # platinum|gold|silver|None
        "claims_rate": _rate("claims"),
        "cancellations_rate": _rate("cancellations"),
        "delayed_handling_rate": _rate("delayed_handling_time"),
        "transactions_completed": (metrics.get("sales") or {}).get("completed"),
        "transactions_canceled": (metrics.get("cancellations") or {}).get("value"),
    }


def build_top_items_block(token, top_products):
    """
    Para cada platform_item_id único nos top_products (max 10),
    chama /items/{id} e devolve o que importa pra L01.
    """
    seen = set()
    item_ids = []
    for p in top_products[:10]:
        pid = (p or {}).get("platform_item_id")
        if pid and pid not in seen:
            seen.add(pid)
            item_ids.append(pid)

    details = []
    for item_id in item_ids:
        item = ml_conn.api_get(
            f"https://api.mercadolibre.com/items/{item_id}", token
        )
        if not item:
            details.append({
                "platform_item_id": item_id,
                "status": "unavailable",
                "error": "items/{id} returned None",
            })
            continue

        shipping = item.get("shipping") or {}
        details.append({
            "platform_item_id": item_id,
            "title": item.get("title"),
            "listing_type": item.get("listing_type_id"),        # gold_pro=Premium, gold_special=Clássico, gold=Clássico antigo
            "is_catalog": bool(item.get("catalog_listing")),
            "catalog_product_id": item.get("catalog_product_id"),
            "status": item.get("status"),                       # active|paused|closed
            "free_shipping": shipping.get("free_shipping"),
            "logistic_type": shipping.get("logistic_type"),
            "health": item.get("health"),
            "available_quantity": item.get("available_quantity"),
            "sold_quantity": item.get("sold_quantity"),
            "category_id": item.get("category_id"),
        })

    return details


def compute_fulfillment_mix(top_items_details, top_products):
    """
    Agrega logistic_type dos top anúncios PONDERADO pelos pedidos do dia.
    Devolve % Full / Flex / Coletado / unknown.
    """
    counts = {"full": 0, "flex": 0, "self_service": 0, "unknown": 0}
    total_orders_counted = 0

    # mapa platform_item_id -> orders pra lookup rápido
    orders_by_pid = {
        (p or {}).get("platform_item_id"): (p or {}).get("orders", 0)
        for p in top_products
    }

    for item in top_items_details:
        if item.get("status") == "unavailable":
            continue
        pid = item.get("platform_item_id")
        orders = orders_by_pid.get(pid, 0)
        if orders == 0:
            continue
        bucket = ML_LOGISTIC_TYPE_TO_BUCKET.get(item.get("logistic_type"), "unknown")
        counts[bucket] += orders
        total_orders_counted += orders

    if total_orders_counted == 0:
        return {
            "status": "unavailable",
            "reason": "no_top_items_with_orders_resolved",
        }

    return {
        "status": "ok",
        "full_pct": round(100 * counts["full"] / total_orders_counted, 1),
        "flex_pct": round(100 * counts["flex"] / total_orders_counted, 1),
        "self_service_pct": round(100 * counts["self_service"] / total_orders_counted, 1),
        "unknown_pct": round(100 * counts["unknown"] / total_orders_counted, 1),
        "total_orders_resolved": total_orders_counted,
        "computed_from": "top_10_items_weighted_by_orders",
    }


def build_ads_block(token, date_str):
    """Chama API Mercado Ads pra trazer resumo do dia."""
    try:
        # busca ads do mesmo dia (begin == end == ontem analisado)
        campaigns = ml_conn.fetch_ads(date_str, date_str, token)
    except Exception as e:
        return {"status": "unavailable", "error": str(e)}

    if campaigns is None:
        return {"status": "unavailable", "error": "fetch_ads returned None"}

    active = [c for c in campaigns if (c.get("status") or "").lower() == "active"]
    total_spend = round(sum(c.get("cost", 0) for c in campaigns), 2)
    total_revenue = round(sum(c.get("revenue", 0) for c in campaigns), 2)
    avg_acos = round(
        sum(c.get("acos", 0) for c in campaigns) / len(campaigns), 2
    ) if campaigns else 0.0

    return {
        "status": "ok",
        "campaigns_total_count": len(campaigns),
        "campaigns_active_count": len(active),
        "spend_yesterday_brl": total_spend,
        "revenue_ads_yesterday_brl": total_revenue,
        "avg_acos_pct": avg_acos,
    }


# ─── Orquestração ─────────────────────────────────────────────────────────────


def read_top_products(package_path):
    """Lê top_products do package parcial."""
    if not os.path.exists(package_path):
        log.error(f"Package parcial não encontrado: {package_path}")
        return []
    with open(package_path) as f:
        pkg = json.load(f)
    return (
        pkg.get("platforms", {})
        .get("mercado-livre", {})
        .get("metrics", {})
        .get("top_products", [])
        or []
    )


def overall_status(reputation, fulfillment, items_details, ads):
    """Decide o status global do snapshot."""
    block_statuses = [
        reputation.get("status"),
        fulfillment.get("status"),
        ads.get("status"),
    ]
    has_items = any(d.get("status") != "unavailable" for d in items_details)
    if has_items:
        block_statuses.append("ok")
    else:
        block_statuses.append("unavailable")

    if all(s == "ok" for s in block_statuses):
        return "ok"
    if any(s == "ok" for s in block_statuses):
        return "partial"
    return "failed"


def build_snapshot(date_str, top_items_from):
    """Orquestra todos os blocos."""
    # 1. refresh + carrega token
    log.info("Refresh tokens ML...")
    ml_conn.refresh_tokens()
    token = ml_conn.load_token("vendas")
    if not token:
        raise RuntimeError("Token ML/vendas indisponível após refresh")

    # 2. lê top_products do package parcial
    top_products = read_top_products(top_items_from)
    log.info(f"Top products lidos: {len(top_products)}")

    # 3. monta cada bloco
    log.info("Buscando reputação...")
    reputation = build_reputation_block(token)

    log.info(f"Buscando detalhes de até 10 top items...")
    top_items = build_top_items_block(token, top_products)
    log.info(f"  → {len([i for i in top_items if i.get('status') != 'unavailable'])} items resolvidos")

    log.info("Calculando mix fulfillment...")
    fulfillment = compute_fulfillment_mix(top_items, top_products)

    log.info("Buscando resumo ADS...")
    ads = build_ads_block(token, date_str)

    overall = overall_status(reputation, fulfillment, top_items, ads)

    return {
        "schema_version": "ml-snapshot/v1",
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "date": date_str,
        "status": overall,
        "reputation": reputation,
        "fulfillment_mix": fulfillment,
        "top_items_details": top_items,
        "ads_summary": ads,
    }


# ─── Cache (fallback) ─────────────────────────────────────────────────────────


def cache_path(cache_dir, date_str):
    return Path(cache_dir) / f"ml-snapshot-{date_str}.json"


def save_to_cache(cache_dir, date_str, snapshot):
    """Salva snapshot OK no cache pra fallback futuro."""
    p = cache_path(cache_dir, date_str)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)
    log.info(f"Cache salvo: {p}")


def load_last_valid_cache(cache_dir, date_str):
    """Procura snapshot mais recente no cache (excluindo a data atual)."""
    cache_dir = Path(cache_dir)
    if not cache_dir.exists():
        return None
    candidates = sorted(cache_dir.glob("ml-snapshot-*.json"), reverse=True)
    for p in candidates:
        if date_str in p.name:
            continue
        try:
            with open(p) as f:
                snap = json.load(f)
            if snap.get("status") == "ok":
                log.warning(f"Usando snapshot de cache: {p.name}")
                return snap
        except Exception:
            continue
    return None


# ─── Main ─────────────────────────────────────────────────────────────────────


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", required=True, help="Data do snapshot (YYYY-MM-DD, BRT)")
    ap.add_argument("--top-items-from", required=True,
                    help="Path do package.json parcial pra ler top_products")
    ap.add_argument("--output", required=True, help="Path do JSON de saída")
    ap.add_argument("--cache-dir", default="/root/.openclaw/ml-snapshot-cache",
                    help="Diretório de cache pra fallback")
    args = ap.parse_args()

    try:
        snapshot = build_snapshot(args.date, args.top_items_from)
    except Exception as e:
        log.exception(f"Falha catastrófica: {e}")
        cached = load_last_valid_cache(args.cache_dir, args.date)
        if cached:
            cached["status"] = "failed_using_cache"
            cached["cache_origin_date"] = cached.get("date")
            cached["date"] = args.date
            cached["error"] = str(e)
            snapshot = cached
        else:
            snapshot = {
                "schema_version": "ml-snapshot/v1",
                "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
                "date": args.date,
                "status": "failed",
                "error": str(e),
                "reputation": {"status": "unavailable"},
                "fulfillment_mix": {"status": "unavailable"},
                "top_items_details": [],
                "ads_summary": {"status": "unavailable"},
            }

    # escreve output principal
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)

    # se foi sucesso completo, atualiza cache
    if snapshot.get("status") == "ok":
        save_to_cache(args.cache_dir, args.date, snapshot)

    log.info(f"✓ Snapshot escrito: {out_path} (status={snapshot.get('status')})")


if __name__ == "__main__":
    main()
