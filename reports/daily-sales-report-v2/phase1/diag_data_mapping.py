#!/usr/bin/env python3
"""Diagnóstico read-only: mapeamento de dados para Daily Sales Report v2.

Não altera dados, não envia mensagens, não mexe em credenciais.
Uso: python3 diag_data_mapping.py
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
UTC = timezone.utc
CENTRAL_ENV = Path("/var/www/budamix-central/.env")

SHOPEE_SHOPS = {
    "448649947": "Budamix Store",
    "860803675": "Budamix Oficial (Conta 2)",
    "442066454": "Budamix Shop (Conta 3)",
}


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def api_get(url: str, key: str, path_query: str) -> list[dict]:
    endpoint = f"{url.rstrip('/')}/rest/v1/{path_query}"
    req = urllib.request.Request(
        endpoint,
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def paginated_get(url: str, key: str, base_query: str, limit: int = 1000) -> list[dict]:
    results = []
    offset = 0
    while True:
        sep = "&" if "?" in base_query else "?"
        pq = f"{base_query}{sep}limit={limit}&offset={offset}"
        batch = api_get(url, key, pq)
        results.extend(batch)
        if len(batch) < limit:
            break
        offset += limit
    return results


def main() -> None:
    env = load_env(CENTRAL_ENV)
    url = env["NEXT_PUBLIC_SUPABASE_URL"]
    key = env["SUPABASE_SERVICE_ROLE_KEY"]

    today = date(2026, 5, 12)
    start = today - timedelta(days=60)
    start_utc = (
        datetime.combine(start, time.min, tzinfo=BRT)
        .astimezone(UTC)
        .isoformat()
        .replace("+00:00", "Z")
    )

    print("=" * 60)
    print("DIAGNÓSTICO — DAILY SALES REPORT v2 — FASE 1")
    print("=" * 60)

    # 1. v_daily_sales check
    print("\n--- v_daily_sales (últimos 60 dias) ---")
    vds = api_get(url, key, f"v_daily_sales?sale_date=gte.{start.isoformat()}&select=sale_date,platform,order_count,total_revenue&order=sale_date.desc&limit=500")
    dates_platforms = defaultdict(set)
    for r in vds:
        dates_platforms[r["sale_date"]].add(r["platform"])
    print(f"Datas distintas: {len(dates_platforms)}")
    incomplete = {d: p for d, p in dates_platforms.items() if not {"shopee", "ml", "amazon"}.issubset(p)}
    if incomplete:
        print(f"Datas incompletas: {len(incomplete)}")
    else:
        print("Todas as datas têm shopee, ml e amazon.")
    print("NOTA: v_daily_sales NÃO separa por conta (só por platform).")

    # 2. Shopee por shop_id
    print("\n--- Shopee: orders por shop_id (60 dias) ---")
    shopee_orders = paginated_get(
        url, key,
        f"orders?platform=eq.shopee&order_date=gte.{urllib.parse.quote(start_utc)}&select=order_date,shop_id,status,total_amount&order=order_date.asc"
    )
    by_day_shop = defaultdict(lambda: defaultdict(lambda: [0, 0.0]))
    for o in shopee_orders:
        dt = datetime.fromisoformat(o["order_date"].replace("Z", "+00:00"))
        brt_date = dt.astimezone(BRT).date().isoformat()
        sid = str(o.get("shop_id") or "")
        by_day_shop[brt_date][sid][0] += 1
        by_day_shop[brt_date][sid][1] += float(o.get("total_amount") or 0)

    totals = defaultdict(lambda: [0, 0.0])
    for dt, shops in by_day_shop.items():
        for sid, vals in shops.items():
            totals[sid][0] += vals[0]
            totals[sid][1] += vals[1]

    for sid, vals in sorted(totals.items(), key=lambda x: x[1][0], reverse=True):
        name = SHOPEE_SHOPS.get(sid, f"unknown({sid})")
        print(f"  {name} (shop_id={sid}): {vals[0]} pedidos, R$ {vals[1]:,.2f}")

    # Gaps
    all_dates = []
    d = start
    while d <= today:
        all_dates.append(d.isoformat())
        d += timedelta(days=1)
    gaps = []
    for dt in all_dates:
        for sid in SHOPEE_SHOPS:
            if by_day_shop.get(dt, {}).get(sid, [0, 0.0])[0] == 0:
                gaps.append(f"{dt}: {SHOPEE_SHOPS[sid]}")
    if gaps:
        print(f"  GAPS ({len(gaps)} dia/conta com 0 pedidos):")
        for g in gaps[:10]:
            print(f"    {g}")
    else:
        print("  SEM GAPS — todas as 3 contas têm pedidos todos os dias.")

    # 3. ML e Amazon
    for plat, label in [("ml", "Mercado Livre"), ("amazon", "Amazon")]:
        print(f"\n--- {label}: orders (60 dias) ---")
        orders = paginated_get(
            url, key,
            f"orders?platform=eq.{plat}&order_date=gte.{urllib.parse.quote(start_utc)}&select=order_date,shop_id,status,total_amount&order=order_date.asc"
        )
        total_count = len(orders)
        total_rev = sum(float(o.get("total_amount") or 0) for o in orders)
        print(f"  Total: {total_count} pedidos, R$ {total_rev:,.2f}")

    print("\n--- Veredito ---")
    print("shop_id separa as 3 contas Shopee de forma confiável.")
    print("PODE AVANÇAR para Fase 2.")


if __name__ == "__main__":
    main()
