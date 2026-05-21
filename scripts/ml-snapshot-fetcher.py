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

# Mapeamento dos logistic_type da API ML → buckets operacionais Budamix.
# IMPORTANTE: a nomenclatura ML diverge da nomenclatura operacional. Mapa correto:
#   fulfillment   = Full (estoque no ML, envio direto do CD ML)
#   cross_docking = COLETA (ML coleta na expedição da Budamix e distribui)
#   self_service  = FLEX real (lojista entrega no mesmo dia)
#   drop_off/xd_drop_off = AGÊNCIA (lojista leva pacote a uma agência ML)
# Confusão comum: "cross_docking" parece Flex mas NÃO é — é a Coleta ML.
ML_LOGISTIC_TYPE_TO_BUCKET = {
    "fulfillment": "full",
    "cross_docking": "cross_docking",
    "self_service": "flex",
    "drop_off": "drop_off",
    "xd_drop_off": "drop_off",
}

# Account overview: cobre 100% dos anúncios ativos (paginando)
ITEMS_SEARCH_PAGE_SIZE = 100  # max permitido pelo endpoint /users/{id}/items/search
ITEMS_SEARCH_MAX_PAGES = 20   # 20 * 100 = 2000 ids (defensivo; Budamix tem ~80 ativos)
MULTIGET_BATCH_SIZE = 20      # limite oficial do endpoint multi-get da API ML
LOW_HEALTH_THRESHOLD = 0.85   # health < 0.85 = anúncio com penalização visível

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
    counts = {"full": 0, "cross_docking": 0, "flex": 0, "drop_off": 0, "unknown": 0}
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

    def _pct(c):
        return round(100 * c / total_orders_counted, 1)

    return {
        "status": "ok",
        "full_pct": _pct(counts["full"]),
        "cross_docking_pct": _pct(counts["cross_docking"]),
        "flex_pct": _pct(counts["flex"]),
        "drop_off_pct": _pct(counts["drop_off"]),
        "unknown_pct": _pct(counts["unknown"]),
        "total_orders_resolved": total_orders_counted,
        "computed_from": "top_10_items_weighted_by_orders",
        "_glossary": {
            "full": "fulfillment — estoque no CD do ML, envio direto",
            "cross_docking": "ML coleta na expedição da Budamix e distribui",
            "flex": "self_service — lojista entrega no mesmo dia",
            "drop_off": "lojista posta em agência ML",
        },
    }


def _count_items_by_status(token, status):
    """Conta total de anúncios em um status (1 chamada, limit=1, pega paging.total)."""
    url = (
        f"https://api.mercadolibre.com/users/{ml_conn.USER_ID}/items/search"
        f"?status={status}&limit=1"
    )
    data = ml_conn.api_get(url, token)
    if not data:
        return None
    return (data.get("paging") or {}).get("total")


def _fetch_all_item_ids(token, status):
    """
    Pagina /users/{USER_ID}/items/search?status={status} até pegar TODOS os IDs.
    Retorna (lista_de_ids, total_reportado_pela_api).
    Se a API limitar paginação, devolve o que conseguir + warning no log.
    """
    all_ids = []
    total_reported = None
    offset = 0
    for page in range(ITEMS_SEARCH_MAX_PAGES):
        url = (
            f"https://api.mercadolibre.com/users/{ml_conn.USER_ID}/items/search"
            f"?status={status}&limit={ITEMS_SEARCH_PAGE_SIZE}&offset={offset}"
        )
        data = ml_conn.api_get(url, token)
        if not data:
            break
        if total_reported is None:
            total_reported = (data.get("paging") or {}).get("total")
        results = data.get("results", []) or []
        all_ids.extend(results)
        if not results or len(all_ids) >= (total_reported or 0):
            break
        offset += ITEMS_SEARCH_PAGE_SIZE
    if total_reported and len(all_ids) < total_reported:
        log.warning(
            f"Paginação cobriu {len(all_ids)}/{total_reported} ativos "
            f"(limite ITEMS_SEARCH_MAX_PAGES atingido)"
        )
    return all_ids, total_reported


def _multiget_items(token, item_ids, attributes):
    """
    Busca múltiplos items em batches de 20 (limite ML).
    Retorna lista de dicts (cada um é o body[i]['body'] do multiget).
    """
    results = []
    attr_str = ",".join(attributes)
    for i in range(0, len(item_ids), MULTIGET_BATCH_SIZE):
        batch = item_ids[i:i + MULTIGET_BATCH_SIZE]
        url = (
            f"https://api.mercadolibre.com/items"
            f"?ids={','.join(batch)}&attributes={attr_str}"
        )
        data = ml_conn.api_get(url, token)
        if not data:
            continue
        # multiget retorna lista de {"code": 200, "body": {...}}
        for entry in data:
            if entry.get("code") == 200 and entry.get("body"):
                results.append(entry["body"])
    return results


def build_account_overview_block(token):
    """
    Panorama de TODA a conta (não só top 10 do dia):
      - totais por status (active / paused / closed)
      - análise de 100% dos ativos com % Full/Flex/Coletado, frete grátis,
        listing_type, catálogo, fora de estoque, health baixo
    """
    # 1. contagens por status — 3 chamadas baratas (paused/closed para visibilidade)
    counts = {
        "active": _count_items_by_status(token, "active"),
        "paused": _count_items_by_status(token, "paused"),
        "closed": _count_items_by_status(token, "closed"),
    }

    if counts["active"] is None:
        return {
            "status": "unavailable",
            "error": "items/search status=active returned None",
        }

    # 2. pega TODOS os IDs ativos (paginando)
    active_ids, total_reported = _fetch_all_item_ids(token, "active")
    if not active_ids:
        return {
            "status": "partial",
            "totals": counts,
            "active_analysis": {"status": "unavailable", "error": "no active ids fetched"},
        }
    coverage_pct = round(100 * len(active_ids) / counts["active"], 1) if counts["active"] else 0.0

    # 3. multiget detalhes — atributos mínimos pra reduzir payload
    attributes = [
        "id", "status", "listing_type_id", "catalog_listing",
        "shipping", "available_quantity", "health", "sold_quantity",
    ]
    items = _multiget_items(token, active_ids, attributes)
    n = len(items)

    if n == 0:
        return {
            "status": "partial",
            "totals": counts,
            "active_analysis": {"status": "unavailable", "error": "multiget failed"},
        }

    # 4. agregações sobre 100% dos ativos
    fulfillment_counts = {"full": 0, "cross_docking": 0, "flex": 0, "drop_off": 0, "unknown": 0}
    listing_counts = {}
    catalog_count = 0
    free_shipping_count = 0
    out_of_stock_count = 0
    out_of_stock_ids = []
    low_health_count = 0
    no_health_data_count = 0

    for item in items:
        shipping = item.get("shipping") or {}
        bucket = ML_LOGISTIC_TYPE_TO_BUCKET.get(shipping.get("logistic_type"), "unknown")
        fulfillment_counts[bucket] += 1

        lt = item.get("listing_type_id") or "unknown"
        listing_counts[lt] = listing_counts.get(lt, 0) + 1

        if item.get("catalog_listing"):
            catalog_count += 1
        if shipping.get("free_shipping"):
            free_shipping_count += 1
        if (item.get("available_quantity") or 0) == 0:
            out_of_stock_count += 1
            out_of_stock_ids.append(item.get("id"))
        health = item.get("health")
        if health is None:
            no_health_data_count += 1
        elif health < LOW_HEALTH_THRESHOLD:
            low_health_count += 1

    def _pct(c):
        return round(100 * c / n, 1)

    return {
        "status": "ok",
        "totals": counts,
        "active_analysis": {
            "status": "ok",
            "analyzed": n,
            "total_active": counts["active"],
            "coverage_pct": coverage_pct,
            "fulfillment_mix": {
                "full_pct": _pct(fulfillment_counts["full"]),
                "cross_docking_pct": _pct(fulfillment_counts["cross_docking"]),
                "flex_pct": _pct(fulfillment_counts["flex"]),
                "drop_off_pct": _pct(fulfillment_counts["drop_off"]),
                "unknown_pct": _pct(fulfillment_counts["unknown"]),
                "_glossary": {
                    "full": "fulfillment — estoque no CD do ML",
                    "cross_docking": "ML coleta na expedição da Budamix",
                    "flex": "self_service — entrega no mesmo dia pelo lojista",
                    "drop_off": "lojista posta em agência ML",
                },
            },
            "listing_type_mix": {k: _pct(v) for k, v in listing_counts.items()},
            "catalog_pct": _pct(catalog_count),
            "free_shipping_pct": _pct(free_shipping_count),
            "out_of_stock_count": out_of_stock_count,
            "out_of_stock_ids": out_of_stock_ids,
            "low_health_count": low_health_count,
            "no_health_data_count": no_health_data_count,
            "low_health_threshold": LOW_HEALTH_THRESHOLD,
        },
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


def overall_status(reputation, fulfillment, items_details, ads, account_overview):
    """Decide o status global do snapshot."""
    block_statuses = [
        reputation.get("status"),
        fulfillment.get("status"),
        ads.get("status"),
        account_overview.get("status"),
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

    log.info("Buscando panorama da conta inteira (100% dos ativos)...")
    account_overview = build_account_overview_block(token)
    if account_overview.get("status") == "ok":
        totals = account_overview.get("totals", {})
        analysis = account_overview.get("active_analysis", {})
        log.info(
            f"  → ativos:{totals.get('active')} pausados:{totals.get('paused')} "
            f"fechados:{totals.get('closed')} "
            f"| analisados {analysis.get('analyzed')}/{analysis.get('total_active')} "
            f"({analysis.get('coverage_pct')}%)"
        )

    overall = overall_status(reputation, fulfillment, top_items, ads, account_overview)

    return {
        "schema_version": "ml-snapshot/v1",
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "date": date_str,
        "status": overall,
        "reputation": reputation,
        "fulfillment_mix": fulfillment,
        "top_items_details": top_items,
        "ads_summary": ads,
        "account_overview": account_overview,
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
                "account_overview": {"status": "unavailable"},
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
