#!/usr/bin/env python3
"""shopee-snapshot-fetcher.py — Snapshot diário por shop_id Shopee.

Roda 1x por dia ANTES do daily-sales-data-builder.py e produz um JSON
com dados de ESTADO ATUAL da loja Shopee que o Supabase não tem:
  - Saúde da Loja (Pontos de Penalidade, LSR, NFR, RR, PT, Avaliação)
  - Programas (Vendedor Indicado, Star, Shopee Mall)
  - Detalhes dos top 10 anúncios (status, FSP, Mall, Coins, cupom, logistics_type)
  - Mix de modalidade de envio (Full / SLS / Drop-off) — top10 + 7d + 30d
  - Shopee Ads (campanhas, spend, revenue, ACOS)
  - Panorama da conta (totais por status, % Mall, % FSP, % cupom, % Coins)

O resultado é colado pelo data builder dentro de
  package.json -> platforms["shopee-budamix-{slug}"]["shopee_snapshot"]

Filosofia:
  - Falha de uma API NÃO derruba o script. Cada bloco tem seu próprio
    "status" (ok | unavailable). Se tudo falhar, usa cache do último dia OK.
  - Top items são consultados APENAS para os platform_item_ids do top_products
    do dia, vindos do package parcial passado em --top-items-from.
  - Affiliate e Coins Cashback NÃO são expostos via Open API Shopee —
    blocos saem com status: "unavailable" sempre. Esperado pela L01.

Uso:
    ./shopee-snapshot-fetcher.py \\
        --shop-id 448649947 \\
        --date 2026-06-01 \\
        --top-items-from /tmp/package-parcial.json \\
        --output /tmp/shopee-snapshot-448649947-2026-06-01.json
"""

import argparse
import hashlib
import hmac
import json
import logging
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ─── Logging ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger("shopee-snapshot")

# ─── Constants ────────────────────────────────────────────────────────────────

PLATFORM = "shopee"
HOST = "https://partner.shopeemobile.com"
PARTNER_ID = 2031533
PARTNER_KEY_PATH = "/root/.openclaw/workspace/integrations/shopee/.env"
TOKENS_DIR = Path("/root/.openclaw/workspace/integrations/shopee")

# Mapeamento shop_id → slug interno usado pelo data builder.
SHOP_ID_TO_SLUG = {
    448649947: "budamix-store",
    860803675: "budamix-oficial-2",
    442066454: "budamix-shop-3",
}
SLUG_TO_TOKEN_FILE = {
    "budamix-store":     ".shopee-tokens-budamix-store.json",
    "budamix-oficial-2": ".shopee-tokens-budamix-store2.json",
    "budamix-shop-3":    ".shopee-tokens-budamix-shop.json",
}

# Bucketização do logistics_type da API Shopee → buckets operacionais.
# A nomenclatura Shopee varia entre endpoints; este mapa cobre os mais comuns.
SHOPEE_LOGISTICS_TO_BUCKET = {
    "fulfillment_by_shopee": "full",
    "fbs": "full",
    "shopee_logistics": "sls",
    "sls": "sls",
    "entrega padrão": "sls",
    "entrega padrao": "sls",
    "seller_own_logistics": "dropoff",
    "drop_off": "dropoff",
    "dropoff": "dropoff",
    "pickup": "dropoff",
    "retire": "dropoff",
}

# Pagination defensiva pra get_item_list.
ITEM_LIST_PAGE_SIZE = 100   # max permitido pelo endpoint Shopee
ITEM_LIST_MAX_PAGES = 30    # 30 * 100 = 3000 ids
ITEM_BASE_INFO_BATCH = 50   # max permitido pelo multi-get da API Shopee

# HTTP defaults.
HTTP_TIMEOUT = 30

# ─── Partner Key ──────────────────────────────────────────────────────────────


def _load_partner_key():
    """Lê SHOPEE_PARTNER_KEY do .env."""
    try:
        raw = open(PARTNER_KEY_PATH).read()
    except FileNotFoundError:
        log.error(f"Partner key file não encontrado: {PARTNER_KEY_PATH}")
        sys.exit(2)
    for line in raw.splitlines():
        if line.startswith("SHOPEE_PARTNER_KEY="):
            return line.split("=", 1)[1].strip()
    log.error("SHOPEE_PARTNER_KEY ausente no .env")
    sys.exit(2)


PARTNER_KEY = _load_partner_key()

# ─── HMAC sign + HTTP helpers ─────────────────────────────────────────────────


def shopee_sign(path, ts, access_token="", shop_id=0):
    """Assinatura HMAC SHA256 oficial Shopee."""
    base = f"{PARTNER_ID}{path}{ts}"
    if access_token:
        base += f"{access_token}{shop_id}"
    return hmac.new(PARTNER_KEY.encode(), base.encode(), hashlib.sha256).hexdigest()


def shopee_get(path, params, shop_id, access_token):
    """GET autenticado. Retorna dict com payload ou {"error": ...}."""
    ts = int(time.time())
    sign = shopee_sign(path, ts, access_token, shop_id)
    full = {
        "partner_id": str(PARTNER_ID),
        "timestamp": str(ts),
        "sign": sign,
        "shop_id": str(shop_id),
        "access_token": access_token,
        **{k: str(v) for k, v in params.items()},
    }
    url = f"{HOST}{path}?{urllib.parse.urlencode(full)}"
    req = urllib.request.Request(url)
    for attempt in range(4):
        try:
            resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
            data = json.loads(resp.read())
            if data.get("error") and "too many" in str(data.get("message", "")).lower():
                time.sleep(2 ** attempt)
                continue
            return data
        except urllib.error.HTTPError as e:
            if attempt == 3:
                return {"error": f"http_{e.code}", "message": str(e)}
            time.sleep(1)
        except Exception as e:
            if attempt == 3:
                return {"error": "exception", "message": str(e)}
            time.sleep(1)
    return {"error": "max_retries"}


def shopee_post(path, body, shop_id, access_token):
    """POST autenticado (raro — usado só pra refresh de token)."""
    ts = int(time.time())
    sign = shopee_sign(path, ts, access_token, shop_id)
    url = f"{HOST}{path}?partner_id={PARTNER_ID}&timestamp={ts}&sign={sign}"
    if access_token:
        url += f"&access_token={access_token}&shop_id={shop_id}"
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
        return json.loads(resp.read())
    except Exception as e:
        return {"error": "exception", "message": str(e)}


# ─── Token loader (com refresh) ───────────────────────────────────────────────


def load_token(slug):
    """Carrega tokens da conta a partir do JSON. Não faz refresh."""
    token_file = TOKENS_DIR / SLUG_TO_TOKEN_FILE[slug]
    with open(token_file) as f:
        return json.load(f)


def save_token(slug, tokens):
    token_file = TOKENS_DIR / SLUG_TO_TOKEN_FILE[slug]
    with open(token_file, "w") as f:
        json.dump(tokens, f, indent=2)


def refresh_token(slug, shop_id):
    """Renova access_token usando refresh_token."""
    tokens = load_token(slug)
    path = "/api/v2/auth/access_token/get"
    ts = int(time.time())
    sign = shopee_sign(path, ts)
    url = f"{HOST}{path}?partner_id={PARTNER_ID}&timestamp={ts}&sign={sign}"
    body = json.dumps({
        "refresh_token": tokens["refresh_token"],
        "partner_id": PARTNER_ID,
        "shop_id": shop_id,
    }).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
        data = json.loads(resp.read())
    except Exception as e:
        raise RuntimeError(f"Refresh falhou para {slug}: {e}")
    if data.get("error"):
        raise RuntimeError(f"Refresh erro Shopee {slug}: {data}")
    new = {
        "shop_id": shop_id,
        "access_token": data["access_token"],
        "refresh_token": data["refresh_token"],
        "access_token_expire_in": data.get("expire_in", 14400),
        "refresh_token_expire_in": 2592000,
        "token_obtained_at": int(time.time()),
        "partner_id": PARTNER_ID,
        "updated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    save_token(slug, new)
    log.info(f"  Token renovado: {slug}")
    return new


def ensure_valid_token(slug, shop_id):
    """Garante token válido, renovando se expirado/perto de expirar."""
    tokens = load_token(slug)
    obtained = tokens.get("token_obtained_at", 0)
    expire_in = tokens.get("access_token_expire_in", 0)
    # Refresh com 5min de folga (igual o sync existente).
    if time.time() > obtained + expire_in - 300:
        tokens = refresh_token(slug, shop_id)
    return tokens


# ─── Bloco 1 — Saúde da Loja (Shop Performance) ───────────────────────────────


def build_shop_performance_block(shop_id, access_token):
    """
    Coleta métricas de Shop Performance via /api/v2/account_health/shop_performance.
    Retorna dict com chaves PT-BR do glossário L01:
      penalty_points, late_shipment_rate_pct, non_fulfillment_rate_pct,
      response_rate_pct, preparation_time_days, shop_rating,
      cancellation_rate_seller_pct, status.
    """
    log.info("Buscando Saúde da Loja...")
    out = {
        "penalty_points": None,
        "late_shipment_rate_pct": None,
        "non_fulfillment_rate_pct": None,
        "response_rate_pct": None,
        "preparation_time_days": None,
        "shop_rating": None,
        "cancellation_rate_seller_pct": None,
        "status": "unavailable",
        "error": None,
    }

    # Shop Performance overall
    resp = shopee_get("/api/v2/account_health/shop_performance", {}, shop_id, access_token)
    if resp.get("error"):
        out["error"] = f"shop_performance: {resp.get('error')} — {resp.get('message','')}"
    else:
        body = resp.get("response", {}) or {}
        # Estrutura típica: response.overall_performance.{rating, sip_score}
        # + response.target_performance.metric_list[] com cada métrica.
        overall = body.get("overall_performance", {}) or {}
        out["shop_rating"] = overall.get("rating")
        metrics = body.get("target_performance", {}).get("metric_list", []) or []
        for m in metrics:
            name = (m.get("metric_name") or m.get("metric_id_name") or "").lower()
            cur = m.get("current_period", m.get("my_shop_performance"))
            if "late_shipment" in name or "lsr" in name:
                out["late_shipment_rate_pct"] = _as_pct(cur)
            elif "non_fulfill" in name or "nfr" in name:
                out["non_fulfillment_rate_pct"] = _as_pct(cur)
            elif "response_rate" in name:
                out["response_rate_pct"] = _as_pct(cur)
            elif "preparation" in name or "prep_time" in name:
                out["preparation_time_days"] = _as_float(cur)
            elif "cancellation_rate" in name:
                out["cancellation_rate_seller_pct"] = _as_pct(cur)
        out["status"] = "ok"

    # Penalty Points via /punishment/get_punishment_points
    pp = shopee_get("/api/v2/account_health/get_penalty_points", {}, shop_id, access_token)
    if not pp.get("error"):
        body = pp.get("response", {}) or {}
        # Estrutura típica: response.overall_penalty_points OU response.penalty_points
        out["penalty_points"] = (
            body.get("overall_penalty_points")
            or body.get("penalty_points")
            or 0
        )

    return out


def _as_float(v):
    try:
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def _as_pct(v):
    """Normaliza pra %. Aceita 0.045 (4.5%) ou 4.5."""
    f = _as_float(v)
    if f is None:
        return None
    return round(f * 100, 2) if f <= 1 else round(f, 2)


# ─── Bloco 2 — Programas (Vendedor Indicado / Shopee Mall) ────────────────────


def build_programs_block(shop_id, access_token):
    """
    Coleta status de Vendedor Indicado, Star e Shopee Mall.
    Endpoint: /api/v2/shop/get_shop_info
    """
    log.info("Buscando Programas (Vendedor Indicado / Shopee Mall)...")
    out = {
        "is_preferred_seller": None,
        "preferred_seller_eligibility_status": None,
        "is_star_seller": None,
        "is_star_plus": None,
        "mall_status": None,
        "next_preferred_seller_review_date": None,
        "shop_name": None,
        "status": "unavailable",
        "error": None,
    }
    resp = shopee_get("/api/v2/shop/get_shop_info", {}, shop_id, access_token)
    if resp.get("error"):
        out["error"] = f"shop_info: {resp.get('error')} — {resp.get('message','')}"
        return out

    body = resp
    out["shop_name"] = body.get("shop_name")

    # Mall status: shop_type ou is_shopee_mall
    is_mall = bool(body.get("is_shopee_mall") or body.get("is_official_shop"))
    is_brand = bool(body.get("is_brand_official"))
    if is_brand:
        out["mall_status"] = "mall_brand"
    elif is_mall:
        out["mall_status"] = "mall_shop"
    else:
        out["mall_status"] = "not_mall"

    # Preferred / Star — campos podem variar de versão da API.
    out["is_preferred_seller"] = bool(body.get("is_preferred_seller") or body.get("is_preferred_plus"))
    out["is_star_seller"] = bool(body.get("is_star_seller") or body.get("is_preferred_plus"))
    out["is_star_plus"] = bool(body.get("is_preferred_plus") or body.get("is_star_plus"))

    out["status"] = "ok"
    return out


# ─── Bloco 3 — Top items details ──────────────────────────────────────────────


def build_top_items_block(shop_id, access_token, top_products):
    """
    Para cada item_id do top 10 do dia, busca:
      title, status, is_mall, free_shipping_program_active, coupon_active,
      coins_cashback_pct, logistics_type, available_quantity, sold_quantity.
    """
    log.info(f"Buscando detalhes de até {len(top_products)} top items...")
    out = {"items": [], "status": "unavailable", "error": None}
    if not top_products:
        out["status"] = "ok"
        return out

    item_ids = []
    title_by_id = {}
    for p in top_products[:10]:
        pid = p.get("platform_item_id") or p.get("item_id")
        if not pid:
            continue
        try:
            pid_int = int(pid)
        except (TypeError, ValueError):
            continue
        item_ids.append(pid_int)
        title_by_id[pid_int] = p.get("title") or p.get("raw_title") or p.get("display_short")
    if not item_ids:
        out["status"] = "ok"
        return out

    # get_item_base_info aceita até 50 item_ids em CSV.
    chunk = item_ids[:ITEM_BASE_INFO_BATCH]
    resp = shopee_get(
        "/api/v2/product/get_item_base_info",
        {"item_id_list": ",".join(map(str, chunk))},
        shop_id,
        access_token,
    )
    if resp.get("error"):
        out["error"] = f"get_item_base_info: {resp.get('error')} — {resp.get('message','')}"
        return out

    items_resp = (resp.get("response") or {}).get("item_list", []) or []
    by_id = {it.get("item_id"): it for it in items_resp}

    # Sold/extra info em paralelo, se disponível
    extra_resp = shopee_get(
        "/api/v2/product/get_item_extra_info",
        {"item_id_list": ",".join(map(str, chunk))},
        shop_id,
        access_token,
    )
    extra_by_id = {}
    if not extra_resp.get("error"):
        for it in (extra_resp.get("response") or {}).get("item_list", []) or []:
            extra_by_id[it.get("item_id")] = it

    resolved = []
    for pid in item_ids:
        info = by_id.get(pid, {})
        extra = extra_by_id.get(pid, {})

        # Bucket logística: prioridade pro flag direto is_fulfillment_by_shopee.
        # Shopee BR não usa logistic_name="fulfillment_by_shopee"; usa esse boolean.
        if info.get("is_fulfillment_by_shopee"):
            logistics_bucket = "full"
            logistics_type_raw = "is_fulfillment_by_shopee=true"
        else:
            # Item não-Full: cai entre SLS / Drop-off conforme logistic_info habilitado.
            logistics_type_raw = None
            logistics_bucket = None
            for li in (info.get("logistic_info") or []):
                if li.get("enabled"):
                    name = li.get("logistic_name") or str(li.get("logistic_id") or "")
                    logistics_type_raw = name
                    logistics_bucket = _shopee_bucket(name)
                    if logistics_bucket:
                        break

        resolved.append({
            "platform_item_id": pid,
            "title": info.get("item_name") or title_by_id.get(pid),
            "is_mall": bool(info.get("has_mall_listing") or info.get("is_mall")),
            "status": (info.get("item_status") or "").lower() or None,
            "free_shipping_program_active": _detect_fsp_active(info),
            "coupon_active": None,  # cupom não vem em get_item_base_info; precisa endpoint dedicado
            "coins_cashback_pct": None,  # cashback ativo também precisa endpoint dedicado
            "logistics_type_raw": logistics_type_raw,
            "logistics_bucket": logistics_bucket,
            "available_quantity": _sum_stock(info),
            "sold_quantity": (extra.get("sold") or info.get("sold") or 0),
        })
    out["items"] = resolved
    out["status"] = "ok"
    log.info(f"  → {len(resolved)} items resolvidos")
    return out


def _shopee_bucket(raw):
    if not raw:
        return None
    key = str(raw).lower()
    for k, v in SHOPEE_LOGISTICS_TO_BUCKET.items():
        if k in key:
            return v
    return None


def _detect_fsp_active(info):
    """Heurística pra Programa de Frete Grátis."""
    if "is_free_shipping" in info:
        return bool(info["is_free_shipping"])
    return None


def _sum_stock(info):
    """Soma o estoque do anúncio (item-level + sum das variações)."""
    # Shopee retorna stock_info_v2 com seller_stock, shopee_stock etc.
    try:
        si = info.get("stock_info_v2") or {}
        summary = si.get("summary_info") or {}
        return summary.get("total_available_stock") or summary.get("total_reserved_stock") or 0
    except Exception:
        return 0


# ─── Bloco 4 — Account Overview (panorama de TODA a base) ─────────────────────


def build_account_overview_block(shop_id, access_token):
    """
    Conta anúncios por status (NORMAL, UNLIST, BANNED) e calcula stats
    de Mall, FSP, cupom, Coins na base ativa.
    """
    log.info("Buscando panorama da conta inteira...")
    out = {
        "totals": {"active": 0, "paused": 0, "unlisted": 0, "banned": 0},
        "active_analysis": {
            "fulfillment_mix": {"full_pct": None, "sls_pct": None, "dropoff_pct": None, "coverage_pct": 0},
            "mall_pct": None,
            "fsp_pct": None,
            "coupon_active_pct": None,
            "coins_active_avg_pct": None,
            "out_of_stock_count": 0,
            "out_of_stock_ids": [],
        },
        "status": "unavailable",
        "error": None,
    }

    # Conta itens por item_status. Status válidos da API Shopee:
    #   NORMAL, BANNED, DELETED, UNLIST, REVIEWING.
    counts = {}
    active_ids = []
    for status in ("NORMAL", "UNLIST", "BANNED"):
        ids = _fetch_all_item_ids(shop_id, access_token, status)
        counts[status] = len(ids)
        if status == "NORMAL":
            active_ids = ids

    out["totals"]["active"] = counts.get("NORMAL", 0)
    # Shopee não tem status "paused" oficial — UNLIST cobre.
    out["totals"]["unlisted"] = counts.get("UNLIST", 0)
    out["totals"]["banned"] = counts.get("BANNED", 0)

    if not active_ids:
        out["status"] = "ok"
        return out

    # Para os ativos, busca info em lotes pra calcular % Mall, FSP, out_of_stock.
    mall_count = 0
    fsp_count = 0
    out_of_stock = []
    bucket_counts = {"full": 0, "sls": 0, "dropoff": 0}
    covered = 0

    for i in range(0, len(active_ids), ITEM_BASE_INFO_BATCH):
        chunk = active_ids[i:i + ITEM_BASE_INFO_BATCH]
        resp = shopee_get(
            "/api/v2/product/get_item_base_info",
            {"item_id_list": ",".join(map(str, chunk))},
            shop_id,
            access_token,
        )
        if resp.get("error"):
            continue
        for it in (resp.get("response") or {}).get("item_list", []) or []:
            if it.get("has_mall_listing") or it.get("is_mall"):
                mall_count += 1
            if _detect_fsp_active(it):
                fsp_count += 1
            stock = _sum_stock(it)
            if stock == 0:
                out_of_stock.append(it.get("item_id"))

            # Bucket logística: prioridade pra is_fulfillment_by_shopee.
            if it.get("is_fulfillment_by_shopee"):
                bucket_counts["full"] += 1
                covered += 1
            else:
                for li in (it.get("logistic_info") or []):
                    if li.get("enabled"):
                        name = li.get("logistic_name") or str(li.get("logistic_id") or "")
                        bucket = _shopee_bucket(name)
                        if bucket:
                            bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
                            covered += 1
                            break

    total_active = out["totals"]["active"]
    if total_active > 0:
        out["active_analysis"]["mall_pct"] = round(mall_count * 100 / total_active, 1)
        out["active_analysis"]["fsp_pct"] = round(fsp_count * 100 / total_active, 1)
        out["active_analysis"]["out_of_stock_count"] = len(out_of_stock)
        out["active_analysis"]["out_of_stock_ids"] = out_of_stock[:50]  # cap
    if covered > 0:
        for k in ("full", "sls", "dropoff"):
            out["active_analysis"]["fulfillment_mix"][f"{k}_pct"] = round(bucket_counts[k] * 100 / covered, 1)
        out["active_analysis"]["fulfillment_mix"]["coverage_pct"] = round(covered * 100 / total_active, 1)

    out["status"] = "ok"
    log.info(
        f"  → ativos:{counts.get('NORMAL',0)} "
        f"unlisted:{counts.get('UNLIST',0)} banidos:{counts.get('BANNED',0)} "
        f"(coverage logistics {out['active_analysis']['fulfillment_mix']['coverage_pct']}%)"
    )
    return out


def _fetch_all_item_ids(shop_id, access_token, item_status):
    """Pagina /product/get_item_list pra um item_status específico."""
    all_ids = []
    offset = 0
    for _ in range(ITEM_LIST_MAX_PAGES):
        resp = shopee_get(
            "/api/v2/product/get_item_list",
            {
                "offset": offset,
                "page_size": ITEM_LIST_PAGE_SIZE,
                "item_status": item_status,
            },
            shop_id,
            access_token,
        )
        if resp.get("error"):
            log.warning(f"  get_item_list({item_status}) falhou: {resp.get('error')}")
            break
        body = resp.get("response", {}) or {}
        items = body.get("item", []) or []
        if not items:
            break
        all_ids.extend(it.get("item_id") for it in items if it.get("item_id"))
        if not body.get("has_next_page"):
            break
        offset += ITEM_LIST_PAGE_SIZE
    return all_ids


# ─── Bloco 5 — Fulfillment mix via Supabase (janelas 7d/30d) ──────────────────


def build_fulfillment_mix_window_block(shop_id, end_date_str, days):
    """
    Calcula mix de Full/SLS/Drop-off por janela usando dados já em Supabase
    (tabela orders ou shopee_orders).
    Espelha a lógica do ML fetcher.
    """
    log.info(f"Calculando mix de modalidade de envio em {days}d (Supabase)...")
    out = {
        "full_pct": None,
        "sls_pct": None,
        "dropoff_pct": None,
        "coverage_pct": 0,
        "status": "unavailable",
        "error": None,
    }
    creds = _load_supabase_creds()
    if not creds:
        out["error"] = "supabase creds ausentes"
        return out
    sb_url, sb_key = creds

    end = datetime.strptime(end_date_str, "%Y-%m-%d")
    start = end - timedelta(days=days - 1)
    start_iso = start.strftime("%Y-%m-%dT00:00:00")
    end_iso = (end + timedelta(days=1)).strftime("%Y-%m-%dT00:00:00")

    # Tabela: public.orders (multi-platform). Coluna: logistic_type (sem 's').
    # GAP CONHECIDO: sync-shopee-orders.py atualmente NÃO popula logistic_type pra
    # pedidos Shopee — 100% vêm com null. Backfill pendente. Enquanto isso, este
    # bloco sai com status='unavailable' e nota explícita.
    try:
        params = (
            f"select=logistic_type"
            f"&platform=eq.shopee"
            f"&shop_id=eq.{shop_id}"
            f"&order_date=gte.{start_iso}"
            f"&order_date=lt.{end_iso}"
            f"&limit=10000"
        )
        headers = {
            "apikey": sb_key,
            "Authorization": f"Bearer {sb_key}",
        }
        url = f"{sb_url}/rest/v1/orders?{params}"
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
        rows = json.loads(resp.read())
    except Exception as e:
        out["error"] = f"supabase fetch: {e}"
        return out

    counts = {"full": 0, "sls": 0, "dropoff": 0}
    total = len(rows)
    populated = 0
    for r in rows:
        lt = r.get("logistic_type")
        if not lt:
            continue
        populated += 1
        bucket = _shopee_bucket(lt)
        if bucket in counts:
            counts[bucket] += 1

    if total == 0:
        out["error"] = f"sem pedidos em {days}d"
        return out
    if populated == 0:
        out["error"] = f"logistic_type=null em 100% dos {total} pedidos (sync-shopee-orders pendente de backfill)"
        return out
    # Calcula em cima dos populated, registra cobertura real.
    for k in counts:
        out[f"{k}_pct"] = round(counts[k] * 100 / populated, 1)
    out["coverage_pct"] = round(populated * 100 / total, 1)
    out["status"] = "ok"
    log.info(
        f"  → {days}d: Full {out['full_pct']}% / SLS {out['sls_pct']}% / "
        f"Drop-off {out['dropoff_pct']}% (cobertura {out['coverage_pct']}% de {total} pedidos)"
    )
    return out


# ─── Bloco 6 — Shopee Ads ─────────────────────────────────────────────────────


def build_ads_block(shop_id, access_token, date_str):
    """
    Coleta resumo de Shopee Ads do dia anterior.
    Endpoints variam por versão e podem requerer escopos extras.
    Tenta /api/v2/ads/get_total_balance + /api/v2/ads/get_all_cpc_ads_daily_performance.
    """
    log.info("Buscando resumo Shopee Ads...")
    out = {
        "campaigns_total_count": None,
        "campaigns_active_count": None,
        "spend_yesterday_brl": None,
        "revenue_ads_yesterday_brl": None,
        "avg_acos_pct": None,
        "status": "unavailable",
        "error": None,
    }

    # Tentativa primária: /api/v2/ads/get_all_cpc_ads_daily_performance
    # Aceita start_date / end_date em YYYY-MM-DD.
    resp = shopee_get(
        "/api/v2/ads/get_all_cpc_ads_daily_performance",
        {"start_date": date_str, "end_date": date_str},
        shop_id,
        access_token,
    )
    if resp.get("error"):
        out["error"] = f"ads_daily: {resp.get('error')} — {resp.get('message','')}"
        return out

    body = resp.get("response", {}) or {}
    rows = body.get("campaign_list") or body.get("daily_performance_list") or []
    if not rows:
        out["status"] = "ok"
        return out

    total = 0
    active = 0
    spend = 0.0
    revenue = 0.0
    acos_sum = 0.0
    acos_count = 0
    for r in rows:
        total += 1
        if r.get("status") in ("ongoing", "active", 1, True):
            active += 1
        spend += _as_float(r.get("expense")) or _as_float(r.get("spend")) or 0
        revenue += _as_float(r.get("gmv")) or _as_float(r.get("revenue")) or 0
        acos = _as_float(r.get("acos"))
        if acos is not None:
            acos_sum += acos
            acos_count += 1

    out["campaigns_total_count"] = total
    out["campaigns_active_count"] = active
    out["spend_yesterday_brl"] = round(spend, 2)
    out["revenue_ads_yesterday_brl"] = round(revenue, 2)
    if acos_count > 0:
        out["avg_acos_pct"] = round(acos_sum / acos_count, 2)
    elif spend > 0:
        out["avg_acos_pct"] = round(spend * 100 / revenue, 2) if revenue else None
    out["status"] = "ok"
    log.info(f"  → Shopee Ads: spend=R${spend:.2f} revenue=R${revenue:.2f} acos~{out['avg_acos_pct']}%")
    return out


# ─── Bloco 7 — Affiliate (gap conhecido — sai unavailable sempre) ─────────────


def build_affiliate_block():
    """Programa de Afiliados Shopee NÃO é exposto na Open API."""
    return {
        "revenue_affiliate_yesterday_brl": None,
        "commission_paid_yesterday_brl": None,
        "active_affiliates_count": None,
        "status": "unavailable",
        "error": "Programa de Afiliados Shopee não exposto via Open API (somente Seller Center). Esperado pela L01.",
    }


# ─── Bloco 8 — Coins Cashback (gap conhecido — sai unavailable sempre) ────────


def build_coins_block():
    """Cashback em Moedas Shopee NÃO é exposto na Open API."""
    return {
        "coins_pct_active_avg": None,
        "revenue_with_coins_yesterday_brl": None,
        "status": "unavailable",
        "error": "Cashback em Moedas Shopee não exposto via Open API (somente Seller Center). Esperado pela L01.",
    }


# ─── Supabase credenciais ─────────────────────────────────────────────────────


def _load_supabase_creds():
    """Lê SUPABASE_URL + SERVICE_ROLE_KEY do ambiente ou do .env do sync."""
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_SERVICE_KEY")
    if url and key:
        return url, key
    # Fallback: lê do sync-shopee-orders.py (mesmo padrão das outras integrações)
    sync_path = "/root/.openclaw/workspace/scripts/sync-shopee-orders.py"
    if not Path(sync_path).exists():
        return None
    try:
        text = open(sync_path).read()
        url_line = next((l for l in text.splitlines() if l.startswith("SUPABASE_URL = ")), "")
        key_line = next((l for l in text.splitlines() if l.startswith("SUPABASE_SERVICE_KEY = ")), "")
        url = url_line.split("=", 1)[1].strip().strip('"').strip("'")
        key = key_line.split("=", 1)[1].strip().strip('"').strip("'")
        return url, key
    except Exception:
        return None


# ─── Persistência ─────────────────────────────────────────────────────────────


def persist_account_snapshot_to_supabase(date_str, shop_id, shop_name, shop_perf, programs, overview, ads, raw_snapshot):
    """Insere/atualiza linha em public.shopee_account_snapshots."""
    creds = _load_supabase_creds()
    if not creds:
        log.warning("Supabase creds ausentes — pulando persistência.")
        return False
    sb_url, sb_key = creds

    payload = {
        "shop_id": shop_id,
        "shop_name": shop_name,
        "snapshot_date": date_str,
        "fetched_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),

        "penalty_points": shop_perf.get("penalty_points"),
        "late_shipment_rate_pct": shop_perf.get("late_shipment_rate_pct"),
        "non_fulfillment_rate_pct": shop_perf.get("non_fulfillment_rate_pct"),
        "response_rate_pct": shop_perf.get("response_rate_pct"),
        "preparation_time_days": shop_perf.get("preparation_time_days"),
        "shop_rating": shop_perf.get("shop_rating"),
        "cancellation_rate_seller_pct": shop_perf.get("cancellation_rate_seller_pct"),

        "is_preferred_seller": programs.get("is_preferred_seller"),
        "preferred_seller_eligibility": programs.get("preferred_seller_eligibility_status"),
        "is_star_seller": programs.get("is_star_seller"),
        "is_star_plus": programs.get("is_star_plus"),
        "mall_status": programs.get("mall_status"),
        "next_preferred_seller_review": programs.get("next_preferred_seller_review_date"),

        "items_active": overview.get("totals", {}).get("active"),
        "items_paused": overview.get("totals", {}).get("paused"),
        "items_unlisted": overview.get("totals", {}).get("unlisted"),
        "items_banned": overview.get("totals", {}).get("banned"),

        "active_mall_pct": overview.get("active_analysis", {}).get("mall_pct"),
        "active_fsp_pct": overview.get("active_analysis", {}).get("fsp_pct"),
        "active_coupon_pct": overview.get("active_analysis", {}).get("coupon_active_pct"),
        "active_coins_active_avg_pct": overview.get("active_analysis", {}).get("coins_active_avg_pct"),

        "ads_campaigns_total": ads.get("campaigns_total_count"),
        "ads_campaigns_active": ads.get("campaigns_active_count"),
        "ads_spend_yesterday_brl": ads.get("spend_yesterday_brl"),
        "ads_revenue_yesterday_brl": ads.get("revenue_ads_yesterday_brl"),
        "ads_avg_acos_pct": ads.get("avg_acos_pct"),

        "raw_payload": raw_snapshot,
    }

    url = f"{sb_url}/rest/v1/shopee_account_snapshots"
    headers = {
        "apikey": sb_key,
        "Authorization": f"Bearer {sb_key}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers=headers,
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=HTTP_TIMEOUT)
        log.info(f"  → shopee_account_snapshots upserted ({shop_name} {date_str})")
        return True
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:500]
        log.error(f"Upsert falhou: HTTP {e.code} — {body}")
        return False
    except Exception as e:
        log.error(f"Upsert falhou: {e}")
        return False


# ─── Top products loader ──────────────────────────────────────────────────────


def read_top_products(package_path, slug):
    """Lê top_products do package parcial. Filtra pelo slug do shop."""
    try:
        with open(package_path) as f:
            pkg = json.load(f)
    except Exception as e:
        log.warning(f"Não consegui ler {package_path}: {e}")
        return []
    platform_key = f"shopee-{slug}"
    platform = pkg.get("platforms", {}).get(platform_key, {})
    top = platform.get("top_products") or []
    log.info(f"Top products lidos ({platform_key}): {len(top)}")
    return top


# ─── Cache ────────────────────────────────────────────────────────────────────


def cache_path(cache_dir, shop_id, date_str):
    return Path(cache_dir) / f"shopee-snapshot-{shop_id}-{date_str}.json"


def save_to_cache(cache_dir, shop_id, date_str, snapshot):
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    path = cache_path(cache_dir, shop_id, date_str)
    with open(path, "w") as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)
    log.info(f"Cache salvo: {path}")


def load_last_valid_cache(cache_dir, shop_id, date_str):
    """Procura cache válido nos últimos 7 dias antes de date_str."""
    base = datetime.strptime(date_str, "%Y-%m-%d")
    for delta in range(1, 8):
        prev = (base - timedelta(days=delta)).strftime("%Y-%m-%d")
        path = cache_path(cache_dir, shop_id, prev)
        if path.exists():
            try:
                with open(path) as f:
                    return json.load(f), prev
            except Exception:
                continue
    return None, None


# ─── Orchestrator ─────────────────────────────────────────────────────────────


def overall_status(*blocks):
    """Se TUDO falhar, status é 'unavailable'; caso contrário, 'ok'."""
    statuses = [b.get("status") for b in blocks if b]
    return "ok" if any(s == "ok" for s in statuses) else "unavailable"


def build_snapshot(shop_id, date_str, top_items_from):
    if shop_id not in SHOP_ID_TO_SLUG:
        raise SystemExit(f"shop_id desconhecido: {shop_id}. Esperados: {list(SHOP_ID_TO_SLUG)}")
    slug = SHOP_ID_TO_SLUG[shop_id]

    log.info(f"Refresh token check para {slug}...")
    tokens = ensure_valid_token(slug, shop_id)
    access = tokens["access_token"]

    top = read_top_products(top_items_from, slug) if top_items_from else []

    shop_perf = build_shop_performance_block(shop_id, access)
    programs = build_programs_block(shop_id, access)
    top_items = build_top_items_block(shop_id, access, top)
    overview = build_account_overview_block(shop_id, access)
    fulfillment_30d = build_fulfillment_mix_window_block(shop_id, date_str, 30)
    fulfillment_7d = build_fulfillment_mix_window_block(shop_id, date_str, 7)
    ads = build_ads_block(shop_id, access, date_str)
    affiliate = build_affiliate_block()
    coins = build_coins_block()

    # Mix yesterday top10 (a partir dos top_items resolvidos)
    fulfillment_yesterday_top10 = _compute_yesterday_top10_mix(top_items.get("items", []), top)

    overall = {
        "shop_id": shop_id,
        "shop_name": slug,
        "snapshot_date": date_str,
        "fetched_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "shop_performance": shop_perf,
        "programs": programs,
        "top_items_details": top_items,
        "account_overview": overview,
        "fulfillment_mix_30d": fulfillment_30d,
        "fulfillment_mix_7d": fulfillment_7d,
        "fulfillment_mix_yesterday_top10": fulfillment_yesterday_top10,
        "ads_summary": ads,
        "affiliate_summary": affiliate,
        "coins_summary": coins,
        "status": overall_status(shop_perf, programs, top_items, overview, fulfillment_30d, ads),
    }
    return overall


def _compute_yesterday_top10_mix(items_resolved, top_products):
    """Pondera mix de Full/SLS/Drop-off por nº de pedidos dos top do dia."""
    counts = {"full": 0, "sls": 0, "dropoff": 0}
    covered = 0
    total = 0
    pedidos_by_id = {}
    for p in top_products[:10]:
        pid = p.get("platform_item_id") or p.get("item_id")
        try:
            pedidos_by_id[int(pid)] = int(p.get("pedidos") or p.get("orders") or 0)
        except (TypeError, ValueError):
            continue
    for it in items_resolved:
        pid = it.get("platform_item_id")
        pedidos = pedidos_by_id.get(pid, 0)
        total += pedidos
        bucket = it.get("logistics_bucket")
        if bucket in counts:
            counts[bucket] += pedidos
            covered += pedidos
    out = {
        "full_pct": None,
        "sls_pct": None,
        "dropoff_pct": None,
        "coverage_pct": 0,
        "status": "ok" if total > 0 else "unavailable",
    }
    if total > 0:
        for k in counts:
            out[f"{k}_pct"] = round(counts[k] * 100 / total, 1)
        out["coverage_pct"] = round(covered * 100 / total, 1)
    return out


# ─── Main ─────────────────────────────────────────────────────────────────────


def main():
    p = argparse.ArgumentParser(description="Snapshot diário Shopee por shop_id")
    p.add_argument("--shop-id", required=True, type=int)
    p.add_argument("--date", required=True, help="YYYY-MM-DD (BRT)")
    p.add_argument("--top-items-from", default="", help="Path do package parcial com top_products")
    p.add_argument("--output", required=True, help="Path do JSON de saída")
    p.add_argument("--cache-dir", default="/root/.openclaw/shopee-snapshot-cache")
    p.add_argument("--no-persist", action="store_true", help="Pula upsert no Supabase")
    args = p.parse_args()

    try:
        snap = build_snapshot(args.shop_id, args.date, args.top_items_from)
    except Exception as e:
        log.error(f"Build falhou catastroficamente: {e}")
        cached, cached_date = load_last_valid_cache(args.cache_dir, args.shop_id, args.date)
        if cached:
            log.warning(f"Usando cache de {cached_date}")
            snap = cached
            snap["status"] = "stale"
            snap["stale_from"] = cached_date
        else:
            raise

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(snap, f, indent=2, ensure_ascii=False)
    log.info(f"✓ Snapshot escrito: {args.output} (status={snap.get('status')})")

    save_to_cache(args.cache_dir, args.shop_id, args.date, snap)

    if not args.no_persist:
        slug = SHOP_ID_TO_SLUG[args.shop_id]
        persist_account_snapshot_to_supabase(
            args.date,
            args.shop_id,
            slug,
            snap.get("shop_performance", {}),
            snap.get("programs", {}),
            snap.get("account_overview", {}),
            snap.get("ads_summary", {}),
            snap,
        )


if __name__ == "__main__":
    main()
