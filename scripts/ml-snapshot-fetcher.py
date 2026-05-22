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
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
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

    transactions = rep.get("transactions") or {}
    ratings = transactions.get("ratings") or {}
    return {
        "status": "ok",
        "color": rep.get("level_id"),                   # ex: "5_green"
        "power_seller_status": rep.get("power_seller_status"),  # platinum|gold|silver|None
        "real_level": rep.get("real_level"),            # nível real durante proteção (geralmente null)
        "protection_end_date": rep.get("protection_end_date"),  # fim do período de proteção (geralmente null)
        "claims_rate": _rate("claims"),
        "cancellations_rate": _rate("cancellations"),
        "delayed_handling_rate": _rate("delayed_handling_time"),
        "transactions_completed": (metrics.get("sales") or {}).get("completed"),
        "transactions_canceled": (metrics.get("cancellations") or {}).get("value"),
        "ratings_positive": ratings.get("positive"),
        "ratings_neutral": ratings.get("neutral"),
        "ratings_negative": ratings.get("negative"),
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


def _load_supabase_creds():
    """Lê credenciais Supabase do .env do budamix-central (mesma fonte do data builder)."""
    env_path = "/var/www/budamix-central/.env"
    if not os.path.exists(env_path):
        return None, None
    env = {}
    for line in open(env_path):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return (
        env.get("NEXT_PUBLIC_SUPABASE_URL"),
        env.get("SUPABASE_SERVICE_ROLE_KEY"),
    )


def persist_account_snapshot_to_supabase(date_str, reputation, account_overview, mercadolider=None, raw_snapshot=None):
    """
    Salva o snapshot da conta (reputação + contagens de items + trajetória
    MercadoLíder) na tabela ml_account_snapshots no Supabase. Idempotente via
    upsert por snapshot_date. Falha silenciosa: log + return False.
    """
    sb_url, sb_key = _load_supabase_creds()
    if not sb_url or not sb_key:
        log.warning("Supabase creds indisponíveis, snapshot não persistido")
        return False

    if reputation.get("status") != "ok":
        log.warning("Reputação não disponível, snapshot persistido só com contagens")

    totals = (account_overview or {}).get("totals", {})
    ml_prog = mercadolider if (mercadolider and mercadolider.get("status") == "ok") else {}

    row = {
        "snapshot_date": date_str,
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "reputation_color": reputation.get("color"),
        "power_seller_status": reputation.get("power_seller_status"),
        "real_level": reputation.get("real_level"),
        "protection_end_date": reputation.get("protection_end_date"),
        "claims_rate": reputation.get("claims_rate"),
        "cancellations_rate": reputation.get("cancellations_rate"),
        "delayed_handling_rate": reputation.get("delayed_handling_rate"),
        "transactions_completed": reputation.get("transactions_completed"),
        "transactions_canceled": reputation.get("transactions_canceled"),
        "ratings_positive": reputation.get("ratings_positive"),
        "ratings_neutral": reputation.get("ratings_neutral"),
        "ratings_negative": reputation.get("ratings_negative"),
        "sales_60d_revenue_brl": ml_prog.get("sales_60d_revenue_brl"),
        "sales_60d_window_start": ml_prog.get("sales_60d_window_start"),
        "items_active": totals.get("active"),
        "items_paused": totals.get("paused"),
        "items_closed": totals.get("closed"),
        "raw_payload": raw_snapshot or {},
    }

    url = f"{sb_url}/rest/v1/ml_account_snapshots?on_conflict=snapshot_date"
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps([row]).encode(),
            method="POST",
            headers={
                "apikey": sb_key,
                "Authorization": f"Bearer {sb_key}",
                "Content-Type": "application/json",
                "Prefer": "resolution=merge-duplicates,return=minimal",
            },
        )
        urllib.request.urlopen(req, timeout=30)
        log.info(f"  → ml_account_snapshots upserted ({date_str})")
        return True
    except Exception as e:
        log.warning(f"  ⚠ falha persistir snapshot: {str(e)[:120]}")
        return False


def _supabase_count(sb_url, sb_key, params_list):
    """Faz HEAD com Prefer=count=exact e devolve o total da query."""
    url = f"{sb_url}/rest/v1/orders?" + urllib.parse.urlencode(params_list)
    req = urllib.request.Request(url, method="HEAD", headers={
        "apikey": sb_key,
        "Authorization": f"Bearer {sb_key}",
        "Prefer": "count=exact",
        "Range-Unit": "items",
        "Range": "0-0",
    })
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        cr = resp.headers.get("content-range", "")  # "0-0/N" ou "*/N"
        if "/" in cr:
            return int(cr.split("/")[-1])
    except Exception:
        pass
    return None


def _supabase_paginate(sb_url, sb_key, base_params, page_size=1000):
    """
    Pagina /orders trazendo todos os rows em lotes via Range header.
    base_params é uma lista de tuplas (chaves podem repetir, ex: order_date 2x).
    """
    all_rows = []
    offset = 0
    while True:
        params = list(base_params) + [("limit", str(page_size)), ("offset", str(offset))]
        url = f"{sb_url}/rest/v1/orders?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={
            "apikey": sb_key,
            "Authorization": f"Bearer {sb_key}",
        })
        resp = urllib.request.urlopen(req, timeout=60)
        rows = json.loads(resp.read())
        if not rows:
            break
        all_rows.extend(rows)
        if len(rows) < page_size:
            break
        offset += page_size
        if offset > 50_000:  # defensivo
            log.warning(f"Paginação cortada em {offset} rows")
            break
    return all_rows


def build_fulfillment_mix_window_block(date_str, days):
    """
    Calcula % logistic_type para a janela dos últimos N dias contando ATÉ date_str
    (inclusivo) usando a coluna orders.logistic_type do Supabase.
    Não chama API ML — é só query SQL via REST com paginação.
    """
    sb_url, sb_key = _load_supabase_creds()
    if not sb_url or not sb_key:
        return {"status": "unavailable", "error": "supabase creds not found"}

    end_dt = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)
    start_dt = end_dt - timedelta(days=days)
    since_iso = start_dt.strftime("%Y-%m-%dT00:00:00+00:00")
    until_iso = end_dt.strftime("%Y-%m-%dT00:00:00+00:00")

    # base params como lista de tuplas — permite duas condições em order_date
    base_params_with_lt = [
        ("select", "logistic_type"),
        ("platform", "eq.ml"),
        ("order_date", f"gte.{since_iso}"),
        ("order_date", f"lt.{until_iso}"),
        ("logistic_type", "not.is.null"),
    ]

    try:
        rows = _supabase_paginate(sb_url, sb_key, base_params_with_lt)
    except Exception as e:
        return {"status": "unavailable", "error": str(e)[:200]}

    if not rows:
        return {
            "status": "unavailable",
            "window_days": days,
            "since": since_iso,
            "reason": "no_orders_with_logistic_type_in_window",
        }

    counts = {"full": 0, "cross_docking": 0, "flex": 0, "drop_off": 0, "unknown": 0}
    for r in rows:
        bucket = ML_LOGISTIC_TYPE_TO_BUCKET.get(r.get("logistic_type"), "unknown")
        counts[bucket] += 1
    total = len(rows)

    # total geral da janela (com e sem logistic_type) pra reportar cobertura
    total_window = _supabase_count(sb_url, sb_key, [
        ("select", "count"),
        ("platform", "eq.ml"),
        ("order_date", f"gte.{since_iso}"),
        ("order_date", f"lt.{until_iso}"),
    ])

    def _pct(c):
        return round(100 * c / total, 1)

    return {
        "status": "ok",
        "window_days": days,
        "since": since_iso,
        "until": until_iso,
        "orders_with_logistic_type": total,
        "orders_total_in_window": total_window,
        "coverage_pct": round(100 * total / total_window, 1) if total_window else None,
        "full_pct": _pct(counts["full"]),
        "cross_docking_pct": _pct(counts["cross_docking"]),
        "flex_pct": _pct(counts["flex"]),
        "drop_off_pct": _pct(counts["drop_off"]),
        "unknown_pct": _pct(counts["unknown"]),
        "_glossary": {
            "full": "fulfillment — estoque no CD do ML",
            "cross_docking": "ML coleta na expedição da Budamix",
            "flex": "self_service — entrega no mesmo dia pelo lojista",
            "drop_off": "lojista posta em agência ML",
        },
    }


# ─── MercadoLíder — trajetória pra Platinum ───────────────────────────────────

# Thresholds oficiais ML (60 dias rolling)
PLATINUM_SALES_THRESHOLD = 1725
PLATINUM_REVENUE_THRESHOLD = 296000
GOLD_SALES_THRESHOLD = 575
GOLD_REVENUE_THRESHOLD = 118400
SILVER_SALES_THRESHOLD = 230
SILVER_REVENUE_THRESHOLD = 37000


def build_mercadolider_progress_block(date_str, reputation):
    """
    Calcula trajetória da Budamix em direção ao próximo nível MercadoLíder.

    Output:
      - sales_60d_revenue_brl: faturamento rolling 60d (orders paid no Supabase)
      - sales_60d_window_start / end: janela analisada
      - sales_60d_count_paid: pedidos pagos na janela
      - medalha_atual / proxima_medalha: silver/gold/platinum
      - platinum.gap_brl / progress_pct / ritmo_diario / eta_dias_estimado
      - ritmo_diario_atual: BRL/dia médio na janela 60d
      - status: 'ok' | 'unavailable'

    Fonte de revenue: Supabase orders (platform=ml, status=paid).
    Threshold Platinum: R$ 296.000 + 1.725 vendas concluídas em 60d rolling.
    """
    sb_url, sb_key = _load_supabase_creds()
    if not sb_url or not sb_key:
        return {"status": "unavailable", "error": "supabase creds not found"}

    end_dt = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)
    start_dt = end_dt - timedelta(days=60)
    since_iso = start_dt.strftime("%Y-%m-%dT00:00:00+00:00")
    until_iso = end_dt.strftime("%Y-%m-%dT00:00:00+00:00")

    base_params = [
        ("select", "total_amount"),
        ("platform", "eq.ml"),
        ("status", "eq.paid"),
        ("order_date", f"gte.{since_iso}"),
        ("order_date", f"lt.{until_iso}"),
    ]

    try:
        rows = _supabase_paginate(sb_url, sb_key, base_params)
    except Exception as e:
        log.warning(f"  ⚠ falha calcular revenue 60d: {str(e)[:120]}")
        return {"status": "unavailable", "error": str(e)[:200]}

    revenue_60d = round(sum(float(r.get("total_amount") or 0) for r in rows), 2)
    count_paid = len(rows)

    sales_completed_60d = reputation.get("transactions_completed") if reputation else None
    medalha_atual = reputation.get("power_seller_status") if reputation else None

    # qual é o próximo nível?
    if medalha_atual is None:
        proxima = "silver"
        threshold_sales = SILVER_SALES_THRESHOLD
        threshold_revenue = SILVER_REVENUE_THRESHOLD
    elif medalha_atual == "silver":
        proxima = "gold"
        threshold_sales = GOLD_SALES_THRESHOLD
        threshold_revenue = GOLD_REVENUE_THRESHOLD
    elif medalha_atual == "gold":
        proxima = "platinum"
        threshold_sales = PLATINUM_SALES_THRESHOLD
        threshold_revenue = PLATINUM_REVENUE_THRESHOLD
    else:
        proxima = None
        threshold_sales = None
        threshold_revenue = None

    # trajetória pra Platinum (mesmo se medalha já é gold/platinum — sempre útil)
    gap_brl_platinum = max(0, PLATINUM_REVENUE_THRESHOLD - revenue_60d)
    progress_pct_platinum = min(100, round(revenue_60d / PLATINUM_REVENUE_THRESHOLD * 100, 2)) if revenue_60d > 0 else 0
    ritmo_diario = round(revenue_60d / 60, 2) if revenue_60d > 0 else 0
    eta_dias_simples = round(gap_brl_platinum / ritmo_diario, 1) if (ritmo_diario > 0 and gap_brl_platinum > 0) else 0

    # trajetória pro próximo nível (pode ser != platinum)
    proxima_gap = None
    proxima_progress = None
    proxima_eta = None
    if proxima and threshold_revenue:
        proxima_gap = max(0, threshold_revenue - revenue_60d)
        proxima_progress = min(100, round(revenue_60d / threshold_revenue * 100, 2)) if revenue_60d > 0 else 0
        proxima_eta = round(proxima_gap / ritmo_diario, 1) if (ritmo_diario > 0 and proxima_gap > 0) else 0

    return {
        "status": "ok",
        "medalha_atual": medalha_atual,
        "proxima_medalha": proxima,
        "sales_60d_revenue_brl": revenue_60d,
        "sales_60d_window_start": start_dt.strftime("%Y-%m-%d"),
        "sales_60d_window_end": date_str,
        "sales_60d_count_paid": count_paid,
        "sales_60d_completed_api": sales_completed_60d,  # vem da API ML
        "ritmo_diario_brl": ritmo_diario,
        "platinum": {
            "threshold_revenue_brl": PLATINUM_REVENUE_THRESHOLD,
            "threshold_sales": PLATINUM_SALES_THRESHOLD,
            "gap_revenue_brl": gap_brl_platinum,
            "progress_pct": progress_pct_platinum,
            "eta_dias_estimado": eta_dias_simples,  # ignora rolling — estimativa grosseira
            "vendas_acima_threshold": (sales_completed_60d or 0) - PLATINUM_SALES_THRESHOLD if sales_completed_60d else None,
        },
        "proximo_nivel": {
            "alvo": proxima,
            "threshold_revenue_brl": threshold_revenue,
            "threshold_sales": threshold_sales,
            "gap_revenue_brl": proxima_gap,
            "progress_pct": proxima_progress,
            "eta_dias_estimado": proxima_eta,
        } if proxima else None,
        "_observacao_eta": (
            "ETA é estimativa grosseira mantendo o ritmo diário médio. "
            "Cálculo real precisa simular janela rolling dia a dia (entrada vs saída). "
            "Quando ritmo cair, ETA sobe; quando subir, ETA baixa."
        ),
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

    log.info("Calculando mix de envio em janelas de 7d e 30d (via Supabase)...")
    mix_7d = build_fulfillment_mix_window_block(date_str, 7)
    mix_30d = build_fulfillment_mix_window_block(date_str, 30)
    if mix_30d.get("status") == "ok":
        log.info(
            f"  → 30d: Full {mix_30d['full_pct']}% / Cross {mix_30d['cross_docking_pct']}% "
            f"/ Flex {mix_30d['flex_pct']}% "
            f"(cobertura {mix_30d.get('coverage_pct')}%)"
        )

    log.info("Calculando trajetória MercadoLíder (revenue 60d via Supabase)...")
    mercadolider = build_mercadolider_progress_block(date_str, reputation)
    if mercadolider.get("status") == "ok":
        plat = mercadolider.get("platinum", {})
        log.info(
            f"  → medalha={mercadolider.get('medalha_atual')} | "
            f"revenue 60d=R$ {mercadolider['sales_60d_revenue_brl']:.2f} | "
            f"gap Platinum=R$ {plat.get('gap_revenue_brl', 0):.2f} | "
            f"ETA~{plat.get('eta_dias_estimado', 0)}d"
        )

    overall = overall_status(reputation, fulfillment, top_items, ads, account_overview)

    snapshot_data = {
        "schema_version": "ml-snapshot/v2",
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "date": date_str,
        "status": overall,
        "reputation": reputation,
        "mercadolider": mercadolider,
        "fulfillment_mix_yesterday_top10": fulfillment,
        "fulfillment_mix_7d": mix_7d,
        "fulfillment_mix_30d": mix_30d,
        "top_items_details": top_items,
        "ads_summary": ads,
        "account_overview": account_overview,
    }

    # Persiste reputação + contagens no Supabase (histórico)
    log.info("Persistindo snapshot da conta no Supabase (ml_account_snapshots)...")
    persist_account_snapshot_to_supabase(
        date_str=date_str,
        reputation=reputation,
        account_overview=account_overview,
        mercadolider=mercadolider,
        raw_snapshot=snapshot_data,
    )

    return snapshot_data


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
                "fulfillment_mix_yesterday_top10": {"status": "unavailable"},
                "fulfillment_mix_7d": {"status": "unavailable"},
                "fulfillment_mix_30d": {"status": "unavailable"},
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
