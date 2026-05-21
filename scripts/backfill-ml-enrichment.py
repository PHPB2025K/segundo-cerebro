#!/usr/bin/env python3
"""
backfill-ml-enrichment.py — Backfill completo de enriquecimento ML retroativo.

Substitui o backfill-ml-logistic-type.py antigo. Agora popula:
  - logistic_type (de /shipments/{id})
  - shipment_status_history
  - listing_type, is_catalog, free_shipping_at_sale,
    item_health_at_sale, item_available_qty_at_sale, item_category_id (de /items/{id})

Pra ser eficiente, faz 2 chamadas API por pedido novo (com cache pra dedup).
Estimativa: ~6000 pedidos em 60d, ~15-20min com sleep 80ms.

Usage:
    python3 backfill-ml-enrichment.py [--days 60] [--batch 100] [--sleep-ms 80] [--dry-run]

Critério de pedido a backfillar: tem shipping_id MAS está sem listing_type
(usa listing_type como flag de "já enriquecido", já que logistic_type pode
estar populado pelo backfill antigo).
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

# Config Supabase
SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_SERVICE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNxYmtvcHJjbW56bm16Yndkcm1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDM4MDQxNCwiZXhwIjoyMDg5OTU2NDE0fQ.-sTaIitEplNoBbW8U5nBHIjAlsIe20ImZ3SkLs17i6A"

# Reusa connector
sys.path.insert(0, "/root/segundo-cerebro/skills/marketplace/marketplace-report/scripts/connectors")
import mercadolivre as ml_conn  # noqa: E402


# === Supabase helpers ===

def fetch_orders_to_enrich(days):
    """
    Busca pedidos ML últimos N dias com shipping_id MAS sem listing_type
    (ainda não enriquecidos). Paginação manual via offset.
    """
    since = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    all_orders = []
    offset = 0
    page = 1000
    # Precisamos do raw_payload pra pegar item_id (primeiro item do pedido)
    base = [
        ("select", "id,platform_order_id,shipping_id,raw_payload"),
        ("platform", "eq.ml"),
        ("order_date", f"gte.{since}"),
        ("shipping_id", "not.is.null"),
        ("listing_type", "is.null"),
        ("order", "order_date.desc"),
    ]
    while True:
        params = list(base) + [("limit", str(page)), ("offset", str(offset))]
        url = f"{SUPABASE_URL}/rest/v1/orders?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={
            "apikey": SUPABASE_SERVICE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        })
        resp = urllib.request.urlopen(req, timeout=60)
        batch = json.loads(resp.read())
        if not batch:
            break
        all_orders.extend(batch)
        if len(batch) < page:
            break
        offset += page
    return all_orders


def update_order(order_id, fields):
    """PATCH em /orders?id=eq.{order_id}"""
    params = {"id": f"eq.{order_id}"}
    url = f"{SUPABASE_URL}/rest/v1/orders?" + urllib.parse.urlencode(params)
    body = json.dumps(fields).encode()
    req = urllib.request.Request(url, data=body, method="PATCH", headers={
        "apikey": SUPABASE_SERVICE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    })
    urllib.request.urlopen(req, timeout=30)


# === API ML helpers (mesmos do sync) ===

def fetch_shipment_data(token, shipping_id, cache):
    if not shipping_id:
        return {"logistic_type": None, "status_history": None}
    if shipping_id in cache:
        return cache[shipping_id]
    try:
        url = f"https://api.mercadolibre.com/shipments/{shipping_id}"
        data = ml_conn.api_get(url, token)
        if not data:
            result = {"logistic_type": None, "status_history": None}
        else:
            result = {
                "logistic_type": data.get("logistic_type"),
                "status_history": data.get("status_history"),
            }
        cache[shipping_id] = result
        return result
    except Exception:
        result = {"logistic_type": None, "status_history": None}
        cache[shipping_id] = result
        return result


def fetch_item_snapshot(token, item_id, cache):
    empty = {
        "listing_type": None, "is_catalog": None,
        "free_shipping_at_sale": None, "item_health_at_sale": None,
        "item_available_qty_at_sale": None, "item_category_id": None,
    }
    if not item_id:
        return empty
    if item_id in cache:
        return cache[item_id]
    try:
        url = f"https://api.mercadolibre.com/items/{item_id}"
        data = ml_conn.api_get(url, token)
        if not data:
            cache[item_id] = empty
            return empty
        shipping = data.get("shipping") or {}
        result = {
            "listing_type": data.get("listing_type_id"),
            "is_catalog": bool(data.get("catalog_listing")) if data.get("catalog_listing") is not None else None,
            "free_shipping_at_sale": shipping.get("free_shipping"),
            "item_health_at_sale": data.get("health"),
            "item_available_qty_at_sale": data.get("available_quantity"),
            "item_category_id": data.get("category_id"),
        }
        cache[item_id] = result
        return result
    except Exception:
        cache[item_id] = empty
        return empty


def get_first_item_id(raw_payload):
    items = (raw_payload or {}).get("order_items") or []
    if items:
        return (items[0].get("item") or {}).get("id")
    return None


# === Main ===

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--batch", type=int, default=100)
    ap.add_argument("--sleep-ms", type=int, default=80)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"Backfill ML enrichment — últimos {args.days} dias")
    print()

    print("Refresh token ML...")
    ml_conn.refresh_tokens()
    token = ml_conn.load_token("vendas")
    if not token:
        sys.exit("✗ token ML indisponível")

    print("Buscando pedidos com shipping_id mas SEM listing_type...")
    orders = fetch_orders_to_enrich(args.days)
    total = len(orders)
    print(f"  → {total} pedidos a enriquecer")
    if total == 0:
        print("Nada a fazer.")
        return
    if args.dry_run:
        print("DRY-RUN — nada será gravado.")
        for o in orders[:3]:
            item_id = get_first_item_id(o.get("raw_payload"))
            print(f"  ex: order {o['platform_order_id']} ship={o['shipping_id']} item={item_id}")
        return

    sleep_s = args.sleep_ms / 1000.0
    ship_cache = {}
    item_cache = {}
    success = 0
    fail = 0
    start = time.time()

    for i, o in enumerate(orders, 1):
        update_fields = {}

        # shipment data (logistic_type + status_history)
        if o.get("shipping_id"):
            ship_data = fetch_shipment_data(token, o["shipping_id"], ship_cache)
            update_fields["logistic_type"] = ship_data["logistic_type"]
            update_fields["shipment_status_history"] = ship_data["status_history"]
            time.sleep(sleep_s)

        # item snapshot
        item_id = get_first_item_id(o.get("raw_payload"))
        if item_id:
            item_data = fetch_item_snapshot(token, item_id, item_cache)
            update_fields.update(item_data)
            time.sleep(sleep_s)

        # update no Supabase
        if update_fields:
            try:
                update_order(o["id"], update_fields)
                success += 1
            except Exception as e:
                fail += 1
                print(f"  ⚠ update fail {o['id']}: {str(e)[:80]}")

        if i % 50 == 0:
            elapsed = time.time() - start
            rate = i / elapsed if elapsed else 0
            eta = (total - i) / rate if rate else 0
            print(f"  {i}/{total} ({round(100*i/total,1)}%) — {round(rate,1)}/s — "
                  f"ETA {round(eta/60,1)}min — cache hits ship:{len(ship_cache)} "
                  f"item:{len(item_cache)}")

    elapsed = time.time() - start
    print()
    print(f"✓ Backfill concluído em {round(elapsed/60,1)}min")
    print(f"  enriquecidos: {success}")
    print(f"  falhas update: {fail}")
    print(f"  cache shipment: {len(ship_cache)} entradas únicas")
    print(f"  cache item:     {len(item_cache)} entradas únicas")


if __name__ == "__main__":
    main()
