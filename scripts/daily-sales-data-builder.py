#!/usr/bin/env python3
"""Daily Sales Data Builder — Layer 0 (Deterministic)

Produces a validated, auditable JSON data package for consumption by the
Daily Sales Analyst 7-layer analytical pipeline.

This script does NOT use LLM, does NOT send Slack, does NOT call any
external AI service.  It queries Supabase `orders`, validates data
quality, and emits a package with a deterministic Data Readiness status.

Usage:
    python3 scripts/daily-sales-data-builder.py YYYY-MM-DD --write
    python3 scripts/daily-sales-data-builder.py YYYY-MM-DD --stdout
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
import re

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DATA_BUILDER_VERSION = "v1.1"
SCHEMA_VERSION = "daily-sales-data-package/v1.1"
BRT = timezone(timedelta(hours=-3))

WORKSPACE = Path(__file__).resolve().parent.parent
OUTPUT_BASE = WORKSPACE / "reports" / "daily-sales-report-v2" / "layered" / "packages"

# Memory base: read from the main repo when available, fallback gracefully
MAIN_REPO = Path("/root/segundo-cerebro")
MEMORY_BASE = MAIN_REPO / "shared" / "trader" / "memory" / "projects" / "daily-sales-report"
ACCOUNTS_DIR = MEMORY_BASE / "accounts"

ACCOUNTS: dict[str, dict[str, Any]] = {
    "shopee-budamix-store": {
        "name": "Shopee \u2014 Budamix Store",
        "platform": "shopee",
        "filter": {"shop_id": "448649947"},
        "responsavel": "Lucas",
        "ads": "Himmel",
    },
    "shopee-budamix-oficial-2": {
        "name": "Shopee \u2014 Budamix Oficial / Conta 2",
        "platform": "shopee",
        "filter": {"shop_id": "860803675"},
        "responsavel": "Lucas",
        "ads": "Himmel",
    },
    "shopee-budamix-shop-3": {
        "name": "Shopee \u2014 Budamix Shop / Conta 3",
        "platform": "shopee",
        "filter": {"shop_id": "442066454"},
        "responsavel": "Lucas",
        "ads": "Himmel",
    },
    "mercado-livre": {
        "name": "Mercado Livre",
        "platform": "ml",
        "filter": {"platform": "ml"},
        "responsavel": "Yasmin",
        "ads": "Himmel",
    },
    "amazon": {
        "name": "Amazon",
        "platform": "amazon",
        "filter": {"platform": "amazon"},
        "responsavel": "Leonardo",
        "ads": "Pedro",
    },
}

RECIPIENTS: dict[str, dict[str, Any]] = {
    "Lucas": {
        "platform": "shopee",
        "accounts": [
            "shopee-budamix-store",
            "shopee-budamix-oficial-2",
            "shopee-budamix-shop-3",
        ],
    },
    "Yasmin": {"platform": "ml", "accounts": ["mercado-livre"]},
    "Leonardo": {"platform": "amazon", "accounts": ["amazon"]},
}

PLATFORM_LABELS = {"shopee": "Shopee", "ml": "Mercado Livre", "amazon": "Amazon"}

RECONCILIATION_ORDER_TOLERANCE = 0
RECONCILIATION_REVENUE_TOLERANCE = 1.00

# Data Readiness thresholds
VOLUME_BAND_30D_LOW = -40   # percent
VOLUME_BAND_30D_HIGH = 40   # percent
VOLUME_BAND_60D_LOW = -60   # percent
VOLUME_BAND_60D_HIGH = 60   # percent
VOLUME_CRITICAL_LOW = -70   # percent — below 30% of mean
DIVERGENCE_CRITICAL = 10    # percent
DIVERGENCE_MINOR = 5        # percent


# ---------------------------------------------------------------------------
# Supabase client
# ---------------------------------------------------------------------------

def load_env(path: str = "/var/www/budamix-central/.env") -> dict[str, str]:
    """Load .env without python-dotenv dependency."""
    env: dict[str, str] = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    except FileNotFoundError:
        pass
    return env


def get_supabase():
    from supabase import create_client

    env = load_env()
    url = env.get("NEXT_PUBLIC_SUPABASE_URL") or os.environ.get("NEXT_PUBLIC_SUPABASE_URL")
    key = env.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        print("ERRO: Credenciais Supabase nao encontradas.", file=sys.stderr)
        sys.exit(1)
    return create_client(url, key)


# ---------------------------------------------------------------------------
# BRT window helpers
# ---------------------------------------------------------------------------

def brt_window(date_str: str) -> tuple[str, str]:
    """Return (start_utc_iso, end_utc_iso) for a BRT business day."""
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=BRT)
    start = dt.astimezone(timezone.utc)
    end = (dt + timedelta(days=1)).astimezone(timezone.utc)
    return start.isoformat(), end.isoformat()


# ---------------------------------------------------------------------------
# Data fetching (paginated)
# ---------------------------------------------------------------------------

def _paginate(query, page_size: int = 1000) -> list[dict]:
    all_rows: list[dict] = []
    offset = 0
    while True:
        resp = query.range(offset, offset + page_size - 1).execute()
        data = resp.data or []
        all_rows.extend(data)
        if len(data) < page_size:
            break
        offset += page_size
    return all_rows


def fetch_canonical_by_platform(sb, date_str: str) -> dict[str, dict]:
    """Aggregate orders in BRT window by platform (canonical source)."""
    start, end = brt_window(date_str)
    q = sb.table("orders").select("platform,status,total_amount").gte("order_date", start).lt("order_date", end)
    all_orders = _paginate(q)

    grouped: dict[str, dict] = {}
    for row in all_orders:
        if "cancel" in (row.get("status") or "").lower():
            continue
        platform = row.get("platform")
        if not platform:
            continue
        bucket = grouped.setdefault(platform, {"platform": platform, "order_count": 0, "total_revenue": 0.0})
        bucket["order_count"] += 1
        bucket["total_revenue"] += float(row.get("total_amount") or 0)

    for bucket in grouped.values():
        bucket["total_revenue"] = round(bucket["total_revenue"], 2)
        bucket["avg_order_value"] = round(bucket["total_revenue"] / bucket["order_count"], 2) if bucket["order_count"] else 0
    return grouped


def fetch_orders(sb, date_str: str, account_slug: str) -> tuple[list[dict], list[dict]]:
    """Fetch valid and cancelled orders for an account on a given BRT day."""
    acct = ACCOUNTS[account_slug]
    start, end = brt_window(date_str)
    q = sb.table("orders").select("*").gte("order_date", start).lt("order_date", end)
    if "shop_id" in acct["filter"]:
        q = q.eq("shop_id", acct["filter"]["shop_id"])
    else:
        q = q.eq("platform", acct["filter"]["platform"])

    all_orders = _paginate(q)
    valid = [o for o in all_orders if "cancel" not in (o.get("status") or "").lower()]
    cancelled = [o for o in all_orders if "cancel" in (o.get("status") or "").lower()]
    return valid, cancelled


def fetch_historical(sb, date_str: str, days: int, account_slug: str) -> list[dict]:
    """Fetch valid orders for the N days before date_str."""
    acct = ACCOUNTS[account_slug]
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=BRT)
    start = (dt - timedelta(days=days)).astimezone(timezone.utc).isoformat()
    end = dt.astimezone(timezone.utc).isoformat()

    q = sb.table("orders").select("id,order_date,total_amount,items,status").gte("order_date", start).lt("order_date", end)
    if "shop_id" in acct["filter"]:
        q = q.eq("shop_id", acct["filter"]["shop_id"])
    else:
        q = q.eq("platform", acct["filter"]["platform"])

    all_orders = _paginate(q)
    return [o for o in all_orders if "cancel" not in (o.get("status") or "").lower()]


def fetch_same_weekday(sb, date_str: str, account_slug: str, count: int = 4) -> list[dict]:
    """Fetch metrics for the last `count` same weekdays."""
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=BRT)
    results: list[dict] = []
    for i in range(1, count + 1):
        target = dt - timedelta(weeks=i)
        target_str = target.strftime("%Y-%m-%d")
        orders, _ = fetch_orders(sb, target_str, account_slug)
        gmv = sum(float(o.get("total_amount") or 0) for o in orders)
        items = sum(sum(it.get("quantity", 1) for it in (o.get("items") or [])) for o in orders)
        results.append({"date": target_str, "orders": len(orders), "gmv": round(gmv, 2), "items": items})
    return results


# ---------------------------------------------------------------------------
# Metrics computation
# ---------------------------------------------------------------------------

SKU_SUFFIX_RE = re.compile(r"(_T|_BB|_B2|_B|_BAP)$", re.I)

PRODUCT_VARIATION_MAP: dict[str, dict[str, Any]] = {
    # Conjunto de 5 Potes Redondos de Vidro — variações por cor da tampa.
    # Regra Pedro 2026-05-15: não consolidar a família inteira em uma linha.
    # Consolidar SKUs filhos por variação vendável: IMB501P / IMB501C / IMB501V.
    "IMB501P": {
        "family": "IMB501",
        "variation_sku": "IMB501P",
        "display_name": "Conjunto 5 Potes de Vidro Redondos Tampa Preta",
        "color_terms": ["preto", "preta"],
    },
    "IMB501C": {
        "family": "IMB501",
        "variation_sku": "IMB501C",
        "display_name": "Conjunto 5 Potes de Vidro Redondos Tampa Cinza",
        "color_terms": ["cinza"],
    },
    "IMB501V": {
        "family": "IMB501",
        "variation_sku": "IMB501V",
        "display_name": "Conjunto 5 Potes de Vidro Redondos Tampa Vermelha",
        "color_terms": ["vermelho", "vermelha"],
    },
}


def normalize_sku(raw_sku: str) -> str:
    sku = (raw_sku or "").strip().upper()
    if not sku:
        return ""
    return SKU_SUFFIX_RE.sub("", sku)


def title_has_color(title_l: str, variation_sku: str) -> bool:
    return any(re.search(rf"\b{re.escape(term)}\b", title_l) for term in PRODUCT_VARIATION_MAP[variation_sku]["color_terms"])


def product_variation_key(raw_sku: str, title: str = "") -> dict[str, Any]:
    """Return canonical sellable-variation key for product ranking.

    Important: this intentionally groups children that represent the same
    sellable variation, but never collapses all color variations into one
    product family line. Example: IMB501P_T and KITIMB501P_T map to IMB501P;
    IMB501C_T maps to IMB501C; IMB501V_T maps to IMB501V.
    """
    sku = normalize_sku(raw_sku)
    raw_upper = (raw_sku or "").strip().upper()
    title_l = (title or "").lower()

    if "IMB501" in raw_upper or "IBM501" in raw_upper:
        # SKU is the strongest signal for this family. Color in title is only
        # fallback when SKU is generic/legacy.
        if "C" in sku[-3:] or title_has_color(title_l, "IMB501C"):
            return {**PRODUCT_VARIATION_MAP["IMB501C"], "key": "IMB501C"}
        if "V" in sku[-3:] or title_has_color(title_l, "IMB501V"):
            return {**PRODUCT_VARIATION_MAP["IMB501V"], "key": "IMB501V"}
        # PT, P, PRETO and unknown legacy variants default to black only when
        # the SKU itself belongs to the IMB501 family and does not signal C/V.
        return {**PRODUCT_VARIATION_MAP["IMB501P"], "key": "IMB501P"}

    return {
        "key": sku or (title or "unknown"),
        "family": sku or "unknown",
        "variation_sku": sku,
        "display_name": "",
    }

def compute_metrics(orders: list[dict], cancelled: list[dict]) -> dict[str, Any]:
    n = len(orders)
    gmv = sum(float(o.get("total_amount") or 0) for o in orders)
    ticket = gmv / n if n else 0

    total_items = 0
    product_counter: Counter = Counter()
    product_order_ids: dict[str, set[str]] = defaultdict(set)
    product_meta: dict[str, dict] = {}
    for order_idx, o in enumerate(orders):
        order_id = str(o.get("order_id") or o.get("id") or o.get("platform_order_id") or order_idx)
        for item in (o.get("items") or []):
            qty = item.get("quantity", 1)
            total_items += qty
            raw_sku = item.get("sku") or ""
            title = item.get("title") or item.get("name") or ""
            variation = product_variation_key(raw_sku, title)
            key = variation["key"]
            product_counter[key] += qty
            product_order_ids[key].add(order_id)
            if key not in product_meta:
                product_meta[key] = {
                    "sku": variation.get("variation_sku") or raw_sku or key,
                    "family": variation.get("family") or variation.get("variation_sku") or key,
                    "variation_sku": variation.get("variation_sku") or raw_sku or key,
                    "display_name": variation.get("display_name") or "",
                    "raw_skus": [],
                    "platform_item_id": item.get("platform_item_id") or item.get("asin") or "",
                    "title": variation.get("display_name") or title,
                }
            if raw_sku and raw_sku not in product_meta[key]["raw_skus"]:
                product_meta[key]["raw_skus"].append(raw_sku)

    # Rank by number of orders first, then units. This matches the Slack
    # wording/ranking expected by Pedro for marketplace reports.
    top_skus = sorted(product_counter.items(), key=lambda kv: (len(product_order_ids[kv[0]]), kv[1]), reverse=True)[:10]
    top_products = [
        {
            **product_meta.get(sku, {"sku": sku, "platform_item_id": "", "title": ""}),
            "orders": len(product_order_ids.get(sku, set())),
            "quantity": qty,
            "aggregation_level": "variation",
        }
        for sku, qty in top_skus
    ]
    total_orders_for_products = sum(len(v) for v in product_order_ids.values()) or 1
    top3_conc = sum(len(product_order_ids.get(sku, set())) for sku, _ in top_skus[:3]) / total_orders_for_products * 100 if top_skus else 0
    top5_conc = sum(len(product_order_ids.get(sku, set())) for sku, _ in top_skus[:5]) / total_orders_for_products * 100 if top_skus else 0

    hour_dist: Counter = Counter()
    for o in orders:
        od = o.get("order_date")
        if od:
            try:
                dt = datetime.fromisoformat(od).astimezone(BRT)
                hour_dist[dt.hour] += 1
            except Exception:
                pass

    fulfillment = {"shopee_full": 0, "amazon_fba": 0, "amazon_fbm": 0, "other": 0, "total": n}
    for o in orders:
        rp = o.get("raw_payload") or {}
        if isinstance(rp, str):
            try:
                rp = json.loads(rp)
            except Exception:
                rp = {}
        carrier = rp.get("shipping_carrier", "")
        if "shopee" in carrier.lower() and "fulfillment" in carrier.lower():
            fulfillment["shopee_full"] += 1
        fc = rp.get("FulfillmentChannel", "")
        if fc == "AFN":
            fulfillment["amazon_fba"] += 1
        elif fc == "MFN":
            fulfillment["amazon_fbm"] += 1

    return {
        "pedidos_validos": n,
        "cancelamentos": len(cancelled),
        "gmv": round(gmv, 2),
        "ticket_medio": round(ticket, 2),
        "itens_vendidos": total_items,
        "top_products": top_products,
        "top3_concentration": round(top3_conc, 1),
        "top5_concentration": round(top5_conc, 1),
        "hour_distribution": dict(sorted(hour_dist.items())),
        "fulfillment": fulfillment,
    }


def compute_historical_avg(historical_orders: list[dict], days: int) -> dict[str, Any]:
    if not historical_orders:
        return {"avg_orders": 0, "avg_gmv": 0, "avg_ticket": 0, "avg_items": 0, "days_with_data": 0}

    by_date: dict[str, list] = defaultdict(list)
    for o in historical_orders:
        od = o.get("order_date", "")
        if od:
            try:
                dt = datetime.fromisoformat(od).astimezone(BRT)
                by_date[dt.strftime("%Y-%m-%d")].append(o)
            except Exception:
                pass

    num_days = max(len(by_date), 1)
    total_orders = len(historical_orders)
    total_gmv = sum(float(o.get("total_amount") or 0) for o in historical_orders)
    total_items = sum(
        item.get("quantity", 1)
        for o in historical_orders
        for item in (o.get("items") or [])
    )

    avg_orders = total_orders / num_days
    avg_gmv = total_gmv / num_days
    avg_ticket = total_gmv / total_orders if total_orders else 0

    return {
        "avg_orders": round(avg_orders, 1),
        "avg_gmv": round(avg_gmv, 2),
        "avg_ticket": round(avg_ticket, 2),
        "avg_items": round(total_items / num_days, 1),
        "days_with_data": num_days,
    }


def pct(current: float, baseline: float) -> float | None:
    if not baseline:
        return None
    return round(((current - baseline) / baseline) * 100, 1)


# ---------------------------------------------------------------------------
# Reconciliation
# ---------------------------------------------------------------------------

def reconcile(canonical: dict, platform: str, orders_count: int, gmv: float, scope: str = "platform") -> dict[str, Any]:
    row = canonical.get(platform, {})
    c_orders = int(row.get("order_count") or 0)
    c_revenue = round(float(row.get("total_revenue") or 0), 2)

    if scope == "account_subset":
        ok = orders_count <= c_orders and round(gmv, 2) <= c_revenue + RECONCILIATION_REVENUE_TOLERANCE
        return {
            "scope": "account_subset",
            "platform": platform,
            "canonical_orders": c_orders,
            "canonical_revenue": c_revenue,
            "orders_count": orders_count,
            "orders_revenue": round(gmv, 2),
            "order_delta": None,
            "revenue_delta": None,
            "ok": ok,
            "note": "Conta Shopee e subconjunto do total da plataforma.",
        }

    order_delta = orders_count - c_orders
    revenue_delta = round(gmv - c_revenue, 2)
    ok = abs(order_delta) <= RECONCILIATION_ORDER_TOLERANCE and abs(revenue_delta) <= RECONCILIATION_REVENUE_TOLERANCE
    return {
        "scope": "platform",
        "platform": platform,
        "canonical_orders": c_orders,
        "canonical_revenue": c_revenue,
        "orders_count": orders_count,
        "orders_revenue": round(gmv, 2),
        "order_delta": order_delta,
        "revenue_delta": revenue_delta,
        "ok": ok,
    }


# ---------------------------------------------------------------------------
# Quality flags
# ---------------------------------------------------------------------------

def compute_quality_flags(acct: dict, metrics: dict, recon: dict, memory_ctx: dict) -> list[dict]:
    flags: list[dict] = []

    if not recon.get("ok"):
        if recon.get("scope") == "account_subset":
            flags.append({"level": "critical", "code": "account_subset_exceeds_platform", "message": "Conta Shopee excede total canonico da plataforma."})
        else:
            flags.append({"level": "critical", "code": "reconciliation_mismatch", "message": "Divergencia entre orders granular e fonte canonica BRT."})

    if metrics.get("pedidos_validos", 0) == 0:
        flags.append({"level": "warning", "code": "no_orders", "message": "Sem pedidos validos na janela BRT."})

    if metrics.get("top3_concentration", 0) >= 70:
        flags.append({"level": "warning", "code": "high_top3_concentration", "message": "Alta concentracao nos top 3 produtos (>=70%)."})

    if acct["platform"] == "amazon":
        for product in metrics.get("top_products", []):
            if not product.get("platform_item_id") and not product.get("title"):
                flags.append({"level": "critical", "code": "amazon_product_identity_missing", "message": "Produto Amazon sem ASIN e sem titulo real."})
                break

    if not memory_ctx.get("last_daily_file"):
        flags.append({"level": "info", "code": "no_previous_daily_memory", "message": "Sem analise diaria anterior carregada."})

    return flags


# ---------------------------------------------------------------------------
# Memory context (read-only)
# ---------------------------------------------------------------------------

def read_account_memory(account_slug: str) -> dict[str, Any]:
    acct_dir = ACCOUNTS_DIR / account_slug
    ctx: dict[str, Any] = {}

    for fname in ["weekly.md", "monthly.md", "rules.md", "himmel-context.md"]:
        fpath = acct_dir / fname
        if fpath.exists():
            key = fname if fname != "himmel-context.md" else "account-himmel-context.md"
            ctx[key] = fpath.read_text(encoding="utf-8")

    for fname in ["himmel-context.md", "marketplace-rules-watch.md", "OPERATING-RULES.md"]:
        fpath = MEMORY_BASE / fname
        if fpath.exists():
            key = fname if fname != "himmel-context.md" else "global-himmel-context.md"
            ctx[key] = fpath.read_text(encoding="utf-8")

    daily_dir = acct_dir / "daily"
    if daily_dir.exists():
        dailies = sorted(daily_dir.glob("*.md"), reverse=True)
        if dailies:
            ctx["last_daily_file"] = dailies[0].name

    return ctx


# ---------------------------------------------------------------------------
# Data Readiness
# ---------------------------------------------------------------------------

def evaluate_readiness(
    date_str: str,
    canonical: dict[str, dict],
    accounts_data: dict[str, dict],
    avg30_by_account: dict[str, dict],
    avg60_by_account: dict[str, dict],
) -> dict[str, Any]:
    """Evaluate Data Readiness status per the plan's criteria.

    Returns dict with:
      - status: DADOS_OK | DADOS_PARCIAIS | NOT_READY
      - data_quality: ok | partial | not_ready
      - checks: list of individual check results
    """
    checks: list[dict] = []
    has_critical = False
    has_partial = False

    # --- Check 1: Timezone BRT validated ---
    start_utc, end_utc = brt_window(date_str)
    tz_ok = "T03:00:00" in start_utc or "T02:00:00" in start_utc  # UTC offset for BRT -3
    checks.append({
        "check": "timezone_brt",
        "status": "ok" if tz_ok else "fail",
        "detail": f"BRT window: {start_utc} to {end_utc}",
    })
    if not tz_ok:
        has_critical = True

    # --- Check 2: Canonical source available ---
    platforms_expected = {"shopee", "ml", "amazon"}
    platforms_found = set(canonical.keys())
    missing_platforms = platforms_expected - platforms_found
    canonical_ok = len(missing_platforms) == 0
    checks.append({
        "check": "canonical_source_available",
        "status": "ok" if canonical_ok else "fail",
        "detail": f"Found: {sorted(platforms_found)}; Missing: {sorted(missing_platforms)}",
    })
    if not canonical_ok:
        has_critical = True

    # --- Check 3: Shopee separated by shop_id ---
    shopee_accounts = [slug for slug, a in ACCOUNTS.items() if a["platform"] == "shopee"]
    shopee_data_present = all(slug in accounts_data for slug in shopee_accounts)
    shopee_shop_ids = set()
    for slug in shopee_accounts:
        if slug in accounts_data:
            shopee_shop_ids.add(ACCOUNTS[slug]["filter"].get("shop_id"))
    shopee_separated = shopee_data_present and len(shopee_shop_ids) == 3
    checks.append({
        "check": "shopee_separated_by_shop_id",
        "status": "ok" if shopee_separated else "fail",
        "detail": f"shop_ids found: {sorted(shopee_shop_ids)}; all 3 present: {shopee_separated}",
    })
    if not shopee_separated:
        has_critical = True

    # --- Check 4: Volume within 30d band per account ---
    for slug, avg30 in avg30_by_account.items():
        acct_data = accounts_data.get(slug, {})
        today_orders = acct_data.get("metrics", {}).get("pedidos_validos", 0)
        avg_orders = avg30.get("avg_orders", 0)
        if avg_orders > 0:
            pct_change = ((today_orders - avg_orders) / avg_orders) * 100
            in_30d_band = VOLUME_BAND_30D_LOW <= pct_change <= VOLUME_BAND_30D_HIGH
            below_critical = pct_change < VOLUME_CRITICAL_LOW

            # Check 60d fallback
            avg60 = avg60_by_account.get(slug, {})
            avg60_orders = avg60.get("avg_orders", 0)
            in_60d_band = True
            if avg60_orders > 0:
                pct60 = ((today_orders - avg60_orders) / avg60_orders) * 100
                in_60d_band = VOLUME_BAND_60D_LOW <= pct60 <= VOLUME_BAND_60D_HIGH

            if below_critical:
                checks.append({
                    "check": f"volume_band_{slug}",
                    "status": "fail",
                    "detail": f"Orders {today_orders} vs avg30 {avg_orders} = {pct_change:+.1f}% (below critical negative threshold)",
                })
                has_critical = True
            elif not in_30d_band:
                # Positive spikes are treated as DADOS_PARCIAIS, not NOT_READY:
                # they may indicate a legitimately strong day and should lower confidence,
                # not block the whole pipeline. Negative moves outside both bands but above
                # the critical floor are also partial; only <30% of avg30 is critical.
                if pct_change > VOLUME_BAND_30D_HIGH:
                    detail = f"Orders {today_orders} vs avg30 {avg_orders} = {pct_change:+.1f}% (positive spike; partial confidence, not blocking)"
                elif in_60d_band:
                    detail = f"Orders {today_orders} vs avg30 {avg_orders} = {pct_change:+.1f}% (outside 30d band, within 60d band)"
                else:
                    detail = f"Orders {today_orders} vs avg30 {avg_orders} = {pct_change:+.1f}% (outside both bands but above critical floor; partial confidence)"
                checks.append({
                    "check": f"volume_band_{slug}",
                    "status": "partial",
                    "detail": detail,
                })
                has_partial = True
            else:
                checks.append({
                    "check": f"volume_band_{slug}",
                    "status": "ok",
                    "detail": f"Orders {today_orders} vs avg30 {avg_orders} = {pct_change:+.1f}%",
                })
        else:
            checks.append({
                "check": f"volume_band_{slug}",
                "status": "unknown",
                "detail": "No 30d average available for comparison",
            })

    # --- Check 5: Reconciliation (critical divergences) ---
    for slug, acct_data in accounts_data.items():
        recon = acct_data.get("reconciliation", {})
        if not recon.get("ok"):
            if recon.get("scope") == "account_subset":
                checks.append({
                    "check": f"reconciliation_{slug}",
                    "status": "fail",
                    "detail": "Account subset exceeds canonical platform total",
                })
                has_critical = True
            else:
                order_delta = abs(recon.get("order_delta") or 0)
                canonical_orders = recon.get("canonical_orders") or 1
                div_pct = (order_delta / canonical_orders) * 100 if canonical_orders else 0
                if div_pct > DIVERGENCE_CRITICAL:
                    checks.append({
                        "check": f"reconciliation_{slug}",
                        "status": "fail",
                        "detail": f"Divergence {div_pct:.1f}% > {DIVERGENCE_CRITICAL}% threshold",
                    })
                    has_critical = True
                elif div_pct > DIVERGENCE_MINOR:
                    checks.append({
                        "check": f"reconciliation_{slug}",
                        "status": "partial",
                        "detail": f"Minor divergence {div_pct:.1f}% (>{DIVERGENCE_MINOR}%, <{DIVERGENCE_CRITICAL}%)",
                    })
                    has_partial = True
                else:
                    checks.append({
                        "check": f"reconciliation_{slug}",
                        "status": "ok",
                        "detail": f"Divergence {div_pct:.1f}% within tolerance",
                    })
        else:
            checks.append({
                "check": f"reconciliation_{slug}",
                "status": "ok",
                "detail": "Reconciliation OK",
            })

    # --- Check 6: Amazon product identity ---
    amazon_data = accounts_data.get("amazon", {})
    amazon_metrics = amazon_data.get("metrics", {})
    top_products = amazon_metrics.get("top_products", [])
    amazon_identity_ok = True
    for p in top_products[:5]:
        if not p.get("platform_item_id") and not p.get("title"):
            amazon_identity_ok = False
            break
    checks.append({
        "check": "amazon_product_identity",
        "status": "ok" if amazon_identity_ok else "fail",
        "detail": f"Top 5 products identity check: {'all identified' if amazon_identity_ok else 'missing identity'}",
    })
    if not amazon_identity_ok:
        has_critical = True

    # --- Check 7: Sync freshness (not measurable from DB alone) ---
    checks.append({
        "check": "sync_freshness",
        "status": "not_measured",
        "detail": "Sync freshness metric not available from current database schema. Registered as not_measured per plan guidelines.",
    })

    # --- Determine overall status ---
    if has_critical:
        status = "NOT_READY"
        data_quality = "not_ready"
    elif has_partial:
        status = "DADOS_PARCIAIS"
        data_quality = "partial"
    else:
        status = "DADOS_OK"
        data_quality = "ok"

    return {
        "status": status,
        "data_quality": data_quality,
        "checks": checks,
    }


# ---------------------------------------------------------------------------
# Account package builder
# ---------------------------------------------------------------------------

def build_account_data(sb, date_str: str, slug: str, canonical: dict) -> tuple[dict, dict, dict]:
    """Build account-level data dict plus avg30 and avg60 for readiness.

    Returns (account_data, avg30, avg60).
    """
    acct = ACCOUNTS[slug]
    orders, cancelled = fetch_orders(sb, date_str, slug)
    metrics = compute_metrics(orders, cancelled)

    hist7 = fetch_historical(sb, date_str, 7, slug)
    hist30 = fetch_historical(sb, date_str, 30, slug)
    hist60 = fetch_historical(sb, date_str, 60, slug)
    avg7 = compute_historical_avg(hist7, 7)
    avg30 = compute_historical_avg(hist30, 30)
    avg60 = compute_historical_avg(hist60, 60)

    same_wd = fetch_same_weekday(sb, date_str, slug, count=4)
    wd_avg: dict[str, float] = {}
    if same_wd:
        wd_avg = {
            "avg_orders": round(sum(d["orders"] for d in same_wd) / len(same_wd), 2),
            "avg_gmv": round(sum(d["gmv"] for d in same_wd) / len(same_wd), 2),
        }
        wd_avg["avg_ticket"] = round(wd_avg["avg_gmv"] / wd_avg["avg_orders"], 2) if wd_avg["avg_orders"] else 0
    else:
        wd_avg = {"avg_orders": 0, "avg_gmv": 0, "avg_ticket": 0}

    # Reconciliation
    if "shop_id" in acct["filter"]:
        recon = reconcile(canonical, acct["platform"], metrics["pedidos_validos"], metrics["gmv"], scope="account_subset")
    else:
        recon = reconcile(canonical, acct["platform"], metrics["pedidos_validos"], metrics["gmv"], scope="platform")

    memory_ctx = read_account_memory(slug)
    flags = compute_quality_flags(acct, metrics, recon, memory_ctx)

    account_data = {
        "account_slug": slug,
        "account_name": acct["name"],
        "platform": acct["platform"],
        "responsavel": acct["responsavel"],
        "ads_owner": acct["ads"],
        "filter": acct["filter"],
        "metrics": metrics,
        "historical": {
            "avg_7d": avg7,
            "avg_30d": avg30,
            "avg_60d": avg60,
            "same_weekday_last_4": same_wd,
            "same_weekday_avg": wd_avg,
            "changes": {
                "orders_vs_7d_pct": pct(metrics["pedidos_validos"], avg7.get("avg_orders") or 0),
                "gmv_vs_7d_pct": pct(metrics["gmv"], avg7.get("avg_gmv") or 0),
                "orders_vs_30d_pct": pct(metrics["pedidos_validos"], avg30.get("avg_orders") or 0),
                "gmv_vs_30d_pct": pct(metrics["gmv"], avg30.get("avg_gmv") or 0),
                "ticket_vs_30d_pct": pct(metrics["ticket_medio"], avg30.get("avg_ticket") or 0),
                "orders_vs_60d_pct": pct(metrics["pedidos_validos"], avg60.get("avg_orders") or 0),
                "gmv_vs_60d_pct": pct(metrics["gmv"], avg60.get("avg_gmv") or 0),
                "ticket_vs_60d_pct": pct(metrics["ticket_medio"], avg60.get("avg_ticket") or 0),
                "orders_vs_same_weekday_pct": pct(metrics["pedidos_validos"], wd_avg.get("avg_orders") or 0),
                "gmv_vs_same_weekday_pct": pct(metrics["gmv"], wd_avg.get("avg_gmv") or 0),
            },
        },
        "reconciliation": recon,
        "memory": {
            "loaded_keys": sorted(k for k in memory_ctx if k not in ("last_daily", "last_daily_file")),
            "last_daily_file": memory_ctx.get("last_daily_file"),
            "has_weekly": "weekly.md" in memory_ctx,
            "has_monthly": "monthly.md" in memory_ctx,
            "has_rules": "rules.md" in memory_ctx,
        },
        "quality_flags": flags,
    }

    return account_data, avg30, avg60


# ---------------------------------------------------------------------------
# Full package builder
# ---------------------------------------------------------------------------

def json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(v) for v in value]
    return value


def build_package(date_str: str) -> dict[str, Any]:
    """Build the complete validated data package for a given BRT date."""
    sb = get_supabase()

    print(f"  Fetching canonical platform totals for {date_str}...")
    canonical = fetch_canonical_by_platform(sb, date_str)

    start_utc, end_utc = brt_window(date_str)

    accounts_data: dict[str, dict] = {}
    avg30_map: dict[str, dict] = {}
    avg60_map: dict[str, dict] = {}

    for slug in ACCOUNTS:
        print(f"  Building data for {slug}...")
        acct_data, avg30, avg60 = build_account_data(sb, date_str, slug, canonical)
        accounts_data[slug] = acct_data
        avg30_map[slug] = avg30
        avg60_map[slug] = avg60

    # Recipients
    recipients: dict[str, dict] = {}
    for name, cfg in RECIPIENTS.items():
        acct_slugs = cfg["accounts"]
        r_accounts = [accounts_data[s] for s in acct_slugs]
        totals = {
            "orders": sum(a["metrics"]["pedidos_validos"] for a in r_accounts),
            "gmv": round(sum(a["metrics"]["gmv"] for a in r_accounts), 2),
            "cancelamentos": sum(a["metrics"]["cancelamentos"] for a in r_accounts),
        }
        totals["ticket_medio"] = round(totals["gmv"] / totals["orders"], 2) if totals["orders"] else 0
        recipients[name] = {
            "recipient": name,
            "platform": cfg["platform"],
            "accounts": acct_slugs,
            "totals": totals,
            "canonical_platform_total": canonical.get(cfg["platform"]),
        }

    # Data Readiness
    print("  Evaluating Data Readiness...")
    readiness = evaluate_readiness(date_str, canonical, accounts_data, avg30_map, avg60_map)

    package: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "data_builder_version": DATA_BUILDER_VERSION,
        "date": date_str,
        "brt_window": {
            "start_utc": start_utc,
            "end_utc": end_utc,
            "display": "00:00\u201323:59 BRT",
            "timezone": "America/Sao_Paulo",
        },
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "data_readiness": readiness,
        "source_of_truth": {
            "canonical": "Supabase orders em janela BRT, cancelados excluidos dos totais validos",
            "amazon_products": "orders.items: platform_item_id/ASIN + titulo real do pedido",
            "shopee_accounts": "orders.shop_id",
        },
        "canonical_by_platform": canonical,
        "platforms": {
            slug: accounts_data[slug]
            for slug in ACCOUNTS
        },
        "recipients": recipients,
    }

    return json_safe(package)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def write_package(package: dict[str, Any], date_str: str) -> Path:
    out_dir = OUTPUT_BASE / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "package.json"
    out_file.write_text(
        json.dumps(package, ensure_ascii=False, indent=2, sort_keys=False),
        encoding="utf-8",
    )
    return out_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Daily Sales Data Builder — Layer 0")
    parser.add_argument("date", help="Data analisada em YYYY-MM-DD (BRT)")
    parser.add_argument("--write", action="store_true", help="Salvar package em reports/")
    parser.add_argument("--stdout", action="store_true", help="Imprimir JSON no stdout")
    args = parser.parse_args()

    # Validate date format
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print("ERRO: Data invalida. Use YYYY-MM-DD.", file=sys.stderr)
        return 1

    print(f"\n=== Daily Sales Data Builder {DATA_BUILDER_VERSION} ===")
    print(f"    Date: {args.date}")
    print(f"    Schema: {SCHEMA_VERSION}")

    package = build_package(args.date)

    readiness = package.get("data_readiness", {})
    print(f"\n  Data Readiness: {readiness.get('status')} (quality: {readiness.get('data_quality')})")
    for check in readiness.get("checks", []):
        icon = {"ok": "OK", "fail": "FAIL", "partial": "PARTIAL", "unknown": "??", "not_measured": "N/M"}.get(check["status"], "?")
        print(f"    [{icon}] {check['check']}: {check['detail']}")

    out_file = None
    if args.write or not args.stdout:
        out_file = write_package(package, args.date)
    if args.stdout:
        print(json.dumps(package, ensure_ascii=False, indent=2, sort_keys=False))
    if out_file:
        print(f"\n  Package saved: {out_file}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
