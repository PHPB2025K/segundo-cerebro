#!/usr/bin/env python3
"""
backfill-ml-logistic-type.py — Preenche logistic_type retroativamente.

Roda 1 vez (manualmente). Pega todos os pedidos ML dos últimos N dias do
Supabase que estão com shipping_id mas SEM logistic_type, consulta
/shipments/{id} na API ML e popula a coluna.

Estimativa: ~6000 pedidos em 60 dias, ~10-15min com sleep defensivo.

Usage:
    python3 backfill-ml-logistic-type.py [--days 60] [--batch 100] [--sleep-ms 100]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

# === Config (mesma do sync-ml-orders.py) ===
SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_SERVICE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNxYmtvcHJjbW56bm16Yndkcm1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDM4MDQxNCwiZXhwIjoyMDg5OTU2NDE0fQ.-sTaIitEplNoBbW8U5nBHIjAlsIe20ImZ3SkLs17i6A"
ML_TOKEN_FILE = "/root/.openclaw/.ml-tokens.json"

# Reusa o connector existente pra refresh + ml_get
sys.path.insert(0, "/root/segundo-cerebro/skills/marketplace/marketplace-report/scripts/connectors")
import mercadolivre as ml_conn  # noqa: E402


# === Supabase helpers ===

def supabase_request(method, path, body=None, params=None):
    url = f"{SUPABASE_URL}/rest/v1/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    headers = {
        "apikey": SUPABASE_SERVICE_KEY,
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        body_resp = resp.read()
        return json.loads(body_resp) if body_resp else None
    except urllib.error.HTTPError as e:
        body_resp = e.read().decode()[:300]
        raise Exception(f"Supabase {method} {path} {e.code}: {body_resp}")


def fetch_orders_missing_logistic_type(days):
    """Busca pedidos ML últimos N dias COM shipping_id E SEM logistic_type."""
    since = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    all_orders = []
    # paginação manual via range header — vamos buscar em batches
    offset = 0
    page = 1000
    while True:
        params = {
            "select": "id,platform_order_id,shipping_id,order_date",
            "platform": "eq.ml",
            "order_date": f"gte.{since}",
            "shipping_id": "not.is.null",
            "logistic_type": "is.null",
            "order": "order_date.desc",
            "limit": str(page),
            "offset": str(offset),
        }
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


def update_order_logistic_type(order_id, logistic_type):
    """UPDATE orders SET logistic_type = ... WHERE id = ..."""
    params = {"id": f"eq.{order_id}"}
    url = f"{SUPABASE_URL}/rest/v1/orders?" + urllib.parse.urlencode(params)
    body = json.dumps({"logistic_type": logistic_type}).encode()
    req = urllib.request.Request(
        url, data=body, method="PATCH",
        headers={
            "apikey": SUPABASE_SERVICE_KEY,
            "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        },
    )
    urllib.request.urlopen(req, timeout=30)


def update_orders_batch(updates):
    """Atualiza múltiplos pedidos em paralelo via PATCH individual (fallback simples)."""
    for u in updates:
        try:
            update_order_logistic_type(u["id"], u["logistic_type"])
        except Exception as e:
            print(f"    ⚠ update fail {u['id']}: {str(e)[:80]}")


# === Main ===

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--batch", type=int, default=100, help="Pedidos por lote antes do flush no Supabase")
    ap.add_argument("--sleep-ms", type=int, default=100, help="ms entre chamadas /shipments/{id}")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print(f"Backfill ML logistic_type — últimos {args.days} dias")
    print()

    # 1. token
    print("Refresh token ML...")
    ml_conn.refresh_tokens()
    token = ml_conn.load_token("vendas")
    if not token:
        sys.exit("✗ token ML indisponível")

    # 2. pedidos pendentes
    print("Buscando pedidos com shipping_id mas SEM logistic_type...")
    orders = fetch_orders_missing_logistic_type(args.days)
    total = len(orders)
    print(f"  → {total} pedidos a backfillar")
    if total == 0:
        print("Nada a fazer.")
        return
    if args.dry_run:
        print("DRY-RUN — nada será gravado.")
        for o in orders[:5]:
            print(f"  ex: {o['platform_order_id']} ship={o['shipping_id']}")
        return

    # 3. fetch shipments + update
    sleep_s = args.sleep_ms / 1000.0
    cache = {}  # shipping_id -> logistic_type (evita duplicata se shipping aparece 2x)
    batch_updates = []
    success = 0
    skip = 0
    fail = 0
    start_ts = time.time()

    for i, o in enumerate(orders, 1):
        ship_id = o["shipping_id"]
        if ship_id in cache:
            lt = cache[ship_id]
        else:
            try:
                ship = ml_conn.api_get(
                    f"https://api.mercadolibre.com/shipments/{ship_id}", token
                )
                lt = (ship or {}).get("logistic_type")
                cache[ship_id] = lt
            except Exception as e:
                print(f"  ⚠ {i}/{total} shipment {ship_id} fail: {str(e)[:80]}")
                cache[ship_id] = None
                lt = None

        if lt is None:
            skip += 1
        else:
            batch_updates.append({"id": o["id"], "logistic_type": lt})

        # flush batch
        if len(batch_updates) >= args.batch:
            update_orders_batch(batch_updates)
            success += len(batch_updates)
            batch_updates = []

        if i % 100 == 0:
            elapsed = time.time() - start_ts
            rate = i / elapsed if elapsed > 0 else 0
            eta = (total - i) / rate if rate > 0 else 0
            print(f"  {i}/{total} ({round(100*i/total,1)}%) — {round(rate,1)}/s — ETA {round(eta/60,1)}min")

        time.sleep(sleep_s)

    # último flush
    if batch_updates:
        update_orders_batch(batch_updates)
        success += len(batch_updates)

    elapsed = time.time() - start_ts
    print()
    print(f"✓ Backfill concluído em {round(elapsed/60,1)}min")
    print(f"  atualizados: {success}")
    print(f"  sem logistic_type retornado (skip): {skip}")
    print(f"  cache hits: {sum(1 for v in cache.values() if v is not None)}")
    print()
    print("Próximo passo: rodar o ml-snapshot-fetcher.py para verificar fulfillment_mix_30d.")


if __name__ == "__main__":
    main()
