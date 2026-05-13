#!/usr/bin/env python3
"""
Daily Sales Report v2 — Fase 3: Motor de Análise Profunda por Conta

Lê dados reais do Supabase (Budamix Central), separa por unidade operacional,
calcula métricas, comparações e gera hipóteses determinísticas.

Uso:
    python3 scripts/daily-sales-v2-analyzer.py 2026-05-11 --dry-run
    python3 scripts/daily-sales-v2-analyzer.py 2026-05-11 --write-memory
    python3 scripts/daily-sales-v2-analyzer.py 2026-05-11 --accounts shopee-budamix-store,amazon --dry-run
"""

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from supabase import create_client

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

BRT = timezone(timedelta(hours=-3))
WORKSPACE = Path(__file__).resolve().parent.parent
MEMORY_BASE = WORKSPACE / "shared" / "trader" / "memory" / "projects" / "daily-sales-report"
ACCOUNTS_DIR = MEMORY_BASE / "accounts"

ACCOUNTS = {
    "shopee-budamix-store": {
        "name": "Shopee — Budamix Store",
        "platform": "shopee",
        "filter": {"shop_id": "448649947"},
        "responsavel": "Lucas",
        "ads": "Himmel",
    },
    "shopee-budamix-oficial-2": {
        "name": "Shopee — Budamix Oficial / Conta 2",
        "platform": "shopee",
        "filter": {"shop_id": "860803675"},
        "responsavel": "Lucas",
        "ads": "Himmel",
    },
    "shopee-budamix-shop-3": {
        "name": "Shopee — Budamix Shop / Conta 3",
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

PLATFORM_LABELS = {
    "shopee": "Shopee",
    "ml": "Mercado Livre",
    "amazon": "Amazon",
}

# O report externo usa agregação direta de orders em BRT como fonte canônica.
# A análise granular por conta usa orders porque v_daily_sales não separa shop_id
# e historicamente truncava o dia em UTC. Por isso o script não depende da view.
RECONCILIATION_ORDER_TOLERANCE = 0
RECONCILIATION_REVENUE_TOLERANCE = 1.00

# ---------------------------------------------------------------------------
# Supabase client
# ---------------------------------------------------------------------------

def load_env(path="/var/www/budamix-central/.env"):
    """Carrega variáveis do .env sem dependência de python-dotenv."""
    env = {}
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
    env = load_env()
    url = env.get("NEXT_PUBLIC_SUPABASE_URL") or os.environ.get("NEXT_PUBLIC_SUPABASE_URL")
    key = env.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        print("ERRO: Credenciais Supabase não encontradas.", file=sys.stderr)
        sys.exit(1)
    return create_client(url, key)


# ---------------------------------------------------------------------------
# Reconciliação canônica
# ---------------------------------------------------------------------------

def fetch_v_daily_sales(sb, date_str: str):
    """Busca a fonte canônica do resumo geral por plataforma.

    Regra crítica: o dia de negócio da GB é BRT, não UTC. A view
    v_daily_sales já foi corrigida no repo do Budamix Central, mas este
    analyzer não deve depender cegamente da view: ele agrega diretamente a
    tabela orders na janela BRT e usa essa agregação para reconciliação.
    """
    start, end = brt_window(date_str)
    all_orders = []
    offset = 0
    page_size = 1000
    while True:
        resp = (
            sb.table("orders")
            .select("platform,status,total_amount")
            .gte("order_date", start)
            .lt("order_date", end)
            .range(offset, offset + page_size - 1)
            .execute()
        )
        data = resp.data or []
        all_orders.extend(data)
        if len(data) < page_size:
            break
        offset += page_size

    grouped = {}
    for row in all_orders:
        if "cancel" in (row.get("status") or "").lower():
            continue
        platform = row.get("platform")
        if not platform:
            continue
        bucket = grouped.setdefault(platform, {"platform": platform, "order_count": 0, "total_revenue": 0.0, "avg_order_value": 0.0})
        bucket["order_count"] += 1
        bucket["total_revenue"] += float(row.get("total_amount") or 0)

    for bucket in grouped.values():
        bucket["total_revenue"] = round(bucket["total_revenue"], 2)
        bucket["avg_order_value"] = round(bucket["total_revenue"] / bucket["order_count"], 2) if bucket["order_count"] else 0
    return grouped


def reconciliation_for_platform(canonical_by_platform, platform, orders_count, gmv):
    """Compara orders granular da conta contra orders canônico BRT da plataforma."""
    row = canonical_by_platform.get(platform) or {}
    canonical_orders = int(row.get("order_count") or 0)
    canonical_revenue = round(float(row.get("total_revenue") or 0), 2)
    order_delta = orders_count - canonical_orders
    revenue_delta = round(gmv - canonical_revenue, 2)
    ok = (
        abs(order_delta) <= RECONCILIATION_ORDER_TOLERANCE
        and abs(revenue_delta) <= RECONCILIATION_REVENUE_TOLERANCE
    )
    return {
        "platform": platform,
        "canonical_orders": canonical_orders,
        "canonical_revenue": canonical_revenue,
        "orders_count": orders_count,
        "orders_revenue": round(gmv, 2),
        "order_delta": order_delta,
        "revenue_delta": revenue_delta,
        "ok": ok,
    }


def format_brl(value):
    return f"R$ {value:,.2f}"


# ---------------------------------------------------------------------------
# Consultas
# ---------------------------------------------------------------------------

def brt_window(date_str: str):
    """Retorna (start_utc, end_utc) para o dia BRT informado."""
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=BRT)
    start = dt.astimezone(timezone.utc)
    end = (dt + timedelta(days=1)).astimezone(timezone.utc)
    return start.isoformat(), end.isoformat()


def fetch_orders(sb, date_str: str, account_slug: str):
    """Busca pedidos do dia para uma conta, excluindo cancelados."""
    acct = ACCOUNTS[account_slug]
    start, end = brt_window(date_str)

    q = sb.table("orders").select("*").gte("order_date", start).lt("order_date", end)

    if "shop_id" in acct["filter"]:
        q = q.eq("shop_id", acct["filter"]["shop_id"])
    else:
        q = q.eq("platform", acct["filter"]["platform"])

    # Paginate to get all orders (Supabase default limit is 1000)
    all_orders = []
    offset = 0
    page_size = 1000
    while True:
        resp = q.range(offset, offset + page_size - 1).execute()
        all_orders.extend(resp.data)
        if len(resp.data) < page_size:
            break
        offset += page_size

    # Separate cancelled
    valid = [o for o in all_orders if "cancelled" not in (o.get("status") or "").lower()]
    cancelled = [o for o in all_orders if "cancelled" in (o.get("status") or "").lower()]
    return valid, cancelled


def fetch_historical_orders(sb, date_str: str, days: int, account_slug: str):
    """Busca pedidos dos últimos N dias (excluindo o dia em questão)."""
    acct = ACCOUNTS[account_slug]
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=BRT)
    start_dt = dt - timedelta(days=days)
    start = start_dt.astimezone(timezone.utc).isoformat()
    end = dt.astimezone(timezone.utc).isoformat()

    q = sb.table("orders").select("id, order_date, total_amount, items, status")
    q = q.gte("order_date", start).lt("order_date", end)

    if "shop_id" in acct["filter"]:
        q = q.eq("shop_id", acct["filter"]["shop_id"])
    else:
        q = q.eq("platform", acct["filter"]["platform"])

    all_orders = []
    offset = 0
    page_size = 1000
    while True:
        resp = q.range(offset, offset + page_size - 1).execute()
        all_orders.extend(resp.data)
        if len(resp.data) < page_size:
            break
        offset += page_size

    valid = [o for o in all_orders if "cancelled" not in (o.get("status") or "").lower()]
    return valid


def fetch_same_weekday_orders(sb, date_str: str, account_slug: str, count=4):
    """Busca pedidos dos últimos 4 mesmos dias da semana."""
    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=BRT)
    daily_counts = []

    for i in range(1, count + 1):
        target = dt - timedelta(weeks=i)
        target_str = target.strftime("%Y-%m-%d")
        orders, _ = fetch_orders(sb, target_str, account_slug)
        gmv = sum(float(o.get("total_amount") or 0) for o in orders)
        items = sum(sum(it.get("quantity", 1) for it in (o.get("items") or [])) for o in orders)
        daily_counts.append({
            "date": target_str,
            "orders": len(orders),
            "gmv": gmv,
            "items": items,
        })

    return daily_counts


# ---------------------------------------------------------------------------
# Métricas
# ---------------------------------------------------------------------------

def compute_metrics(orders, cancelled):
    """Calcula métricas do dia para uma lista de pedidos válidos."""
    n = len(orders)
    gmv = sum(float(o.get("total_amount") or 0) for o in orders)
    ticket = gmv / n if n else 0

    # Items
    total_items = 0
    sku_counter = Counter()
    product_meta = {}
    for o in orders:
        for item in (o.get("items") or []):
            qty = item.get("quantity", 1)
            total_items += qty
            sku = item.get("sku") or item.get("title", "unknown")
            sku_counter[sku] += qty

            # Keep the real marketplace identity attached to the counted SKU.
            # This is critical for Amazon: a SKU nickname can be wrong/stale, but
            # ASIN + title come from the orderItems payload for the actual order.
            if sku not in product_meta:
                product_meta[sku] = {
                    "sku": sku,
                    "platform_item_id": item.get("platform_item_id") or item.get("asin") or "",
                    "title": item.get("title") or item.get("name") or "",
                }

    # Top SKUs
    top_skus = sku_counter.most_common(10)
    top_products = [
        {**product_meta.get(sku, {"sku": sku, "platform_item_id": "", "title": ""}), "quantity": qty}
        for sku, qty in top_skus
    ]
    total_sku_qty = sum(sku_counter.values()) or 1
    top3_concentration = sum(c for _, c in top_skus[:3]) / total_sku_qty * 100 if top_skus else 0

    # Distribuição por hora BRT
    hour_dist = Counter()
    for o in orders:
        od = o.get("order_date")
        if od:
            try:
                dt = datetime.fromisoformat(od)
                brt_dt = dt.astimezone(BRT)
                hour_dist[brt_dt.hour] += 1
            except Exception:
                pass

    # Fulfillment
    fulfillment = {"shopee_full": 0, "amazon_fba": 0, "amazon_fbm": 0, "total": n}
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
        "top_skus": top_skus,
        "top_products": top_products,
        "top3_concentration": round(top3_concentration, 1),
        "hour_distribution": dict(sorted(hour_dist.items())),
        "fulfillment": fulfillment,
    }


def compute_historical_avg(historical_orders, days):
    """Calcula média diária de pedidos/GMV/itens em N dias."""
    if not historical_orders:
        return {"avg_orders": 0, "avg_gmv": 0, "avg_ticket": 0, "avg_items": 0}

    # Group by date
    by_date = defaultdict(list)
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
    total_items = 0
    for o in historical_orders:
        for item in (o.get("items") or []):
            total_items += item.get("quantity", 1)

    avg_orders = total_orders / num_days
    avg_gmv = total_gmv / num_days
    avg_ticket = total_gmv / total_orders if total_orders else 0
    avg_items = total_items / num_days

    return {
        "avg_orders": round(avg_orders, 1),
        "avg_gmv": round(avg_gmv, 2),
        "avg_ticket": round(avg_ticket, 2),
        "avg_items": round(avg_items, 1),
        "days_with_data": num_days,
    }


def pct_change(current, baseline):
    if baseline == 0:
        return "N/A"
    return f"{((current - baseline) / baseline) * 100:+.1f}%"


# ---------------------------------------------------------------------------
# Hipóteses determinísticas
# ---------------------------------------------------------------------------

def generate_hypotheses(metrics, avg30, avg60, avg_weekday, account_slug):
    acct = ACCOUNTS[account_slug]
    hyps = []
    m = metrics

    orders_today = m["pedidos_validos"]
    gmv_today = m["gmv"]
    ticket_today = m["ticket_medio"]

    # Comparação com média 30d
    if avg30["avg_orders"] > 0:
        orders_ratio = orders_today / avg30["avg_orders"]
        ticket_ratio = ticket_today / avg30["avg_ticket"] if avg30["avg_ticket"] else 1

        if orders_ratio < 0.7 and ticket_ratio > 0.9:
            hyps.append("⚠️ HIPÓTESE: Queda de pedidos com ticket preservado → possível problema de tráfego/exposição/ADS.")
        elif ticket_ratio < 0.8 and orders_ratio > 0.9:
            hyps.append("⚠️ HIPÓTESE: Queda de ticket médio com pedidos preservados → possível mudança no mix de produtos.")
        elif orders_ratio < 0.7 and ticket_ratio < 0.8:
            hyps.append("⚠️ HIPÓTESE: Queda simultânea de pedidos e ticket → possível problema de tráfego/plataforma.")

        if orders_ratio > 1.3:
            hyps.append("✅ Dia acima da média: pedidos +30% vs média 30d.")

    if m["top3_concentration"] > 60:
        hyps.append(f"⚠️ HIPÓTESE: Alta concentração nos top 3 SKUs ({m['top3_concentration']}%) → risco de dependência.")

    if acct["platform"] == "amazon" and orders_today < 5:
        hyps.append("⚠️ HIPÓTESE: Amazon com poucos pedidos → checar Buy Box, FBA, ADS e listings.")

    if acct["platform"] in ("shopee", "ml") and avg30["avg_orders"] > 0:
        if orders_today / avg30["avg_orders"] < 0.7:
            hyps.append(f"💡 Ponto para {acct['ads']}: sinal de queda de tráfego em {acct['name']}.")

    if not hyps:
        hyps.append("✅ Dia dentro dos parâmetros normais. Sem anomalias detectadas.")

    return hyps


# ---------------------------------------------------------------------------
# Memória: leitura de contexto
# ---------------------------------------------------------------------------

def read_account_memory(account_slug: str):
    """Lê memória existente da conta para contexto."""
    acct_dir = ACCOUNTS_DIR / account_slug
    context = {}

    for fname in ["weekly.md", "monthly.md", "rules.md", "himmel-context.md"]:
        fpath = acct_dir / fname
        if fpath.exists():
            key = fname if fname != "himmel-context.md" else "account-himmel-context.md"
            context[key] = fpath.read_text(encoding="utf-8")

    for fname in ["himmel-context.md", "marketplace-rules-watch.md", "OPERATING-RULES.md"]:
        fpath = MEMORY_BASE / fname
        if fpath.exists():
            key = fname if fname != "himmel-context.md" else "global-himmel-context.md"
            context[key] = fpath.read_text(encoding="utf-8")

    # Última análise diária
    daily_dir = acct_dir / "daily"
    if daily_dir.exists():
        dailies = sorted(daily_dir.glob("*.md"), reverse=True)
        if dailies:
            context["last_daily"] = dailies[0].read_text(encoding="utf-8")
            context["last_daily_file"] = dailies[0].name

    return context


# ---------------------------------------------------------------------------
# Geração de análise (Markdown)
# ---------------------------------------------------------------------------

def format_analysis(date_str, account_slug, metrics, avg30, avg60, avg_weekday, hypotheses, memory_context, reconciliation=None):
    acct = ACCOUNTS[account_slug]
    m = metrics
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    weekday_pt = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"][dt.weekday()]

    lines = []
    lines.append(f"# Análise Diária — {acct['name']}")
    lines.append(f"**Data:** {date_str} ({weekday_pt})")
    lines.append(f"**Responsável:** {acct['responsavel']} | **ADS:** {acct['ads']}")
    lines.append(f"**Gerado por:** daily-sales-v2-analyzer.py (Fase 3)")
    lines.append("")

    # Métricas
    lines.append("## Métricas do Dia")
    lines.append(f"| Métrica | Valor |")
    lines.append(f"|---|---|")
    lines.append(f"| Pedidos válidos | {m['pedidos_validos']} |")
    lines.append(f"| Cancelamentos | {m['cancelamentos']} |")
    lines.append(f"| Faturamento/GMV | R$ {m['gmv']:,.2f} |")
    lines.append(f"| Ticket médio | R$ {m['ticket_medio']:,.2f} |")
    lines.append(f"| Itens vendidos | {m['itens_vendidos']} |")
    lines.append("")

    if reconciliation:
        lines.append("## Reconciliação com Fonte Canônica")
        status = "OK" if reconciliation["ok"] else "DIVERGÊNCIA — NÃO usar soma de orders como total oficial"
        lines.append(f"- **Status:** {status}")
        lines.append(f"- **orders BRT canônico ({PLATFORM_LABELS.get(reconciliation['platform'], reconciliation['platform'])}):** {reconciliation['canonical_orders']} pedidos | {format_brl(reconciliation['canonical_revenue'])}")
        lines.append(f"- **orders granular usado nesta análise:** {reconciliation['orders_count']} pedidos | {format_brl(reconciliation['orders_revenue'])}")
        lines.append(f"- **Diferença:** {reconciliation['order_delta']:+d} pedidos | {format_brl(reconciliation['revenue_delta'])}")
        lines.append("- **Regra:** o Slack/Resumo Geral permanece ancorado em `orders` agregado em BRT; o diagnóstico usa a mesma fonte por conta/SKU/horário.")
        lines.append("")

    # Top products with real marketplace identity.
    # Keep SKU for internal traceability, but also persist ASIN/platform id and
    # title so downstream Slack generation never has to guess product names from
    # a stale hardcoded SKU map.
    lines.append("## Top Produtos")
    lines.append("| # | SKU | ASIN/Item | Produto no pedido | Qtd |")
    lines.append("|---|---|---|---|---|")
    for i, product in enumerate(m.get("top_products", [])[:10], 1):
        sku = str(product.get("sku") or "").replace("|", "-")
        platform_item_id = str(product.get("platform_item_id") or "").replace("|", "-")
        title = str(product.get("title") or "").replace("|", "-")
        qty = int(product.get("quantity") or 0)
        lines.append(f"| {i} | {sku} | {platform_item_id} | {title} | {qty} |")
    lines.append(f"\n**Concentração top 3:** {m['top3_concentration']}%")
    lines.append("")

    # Distribuição por hora
    lines.append("## Distribuição por Hora (BRT)")
    if m["hour_distribution"]:
        max_h = max(m["hour_distribution"].values()) if m["hour_distribution"] else 1
        for h in range(24):
            cnt = m["hour_distribution"].get(h, 0)
            bar = "█" * int(cnt / max(max_h, 1) * 20) if cnt else ""
            if cnt > 0:
                lines.append(f"  {h:02d}h: {bar} {cnt}")
    lines.append("")

    # Fulfillment
    ff = m["fulfillment"]
    if acct["platform"] == "shopee":
        lines.append(f"## Fulfillment")
        lines.append(f"- Shopee Full: {ff['shopee_full']}/{ff['total']} pedidos")
        lines.append("")
    elif acct["platform"] == "amazon":
        lines.append(f"## Fulfillment")
        lines.append(f"- FBA: {ff['amazon_fba']}/{ff['total']} pedidos")
        lines.append(f"- FBM: {ff['amazon_fbm']}/{ff['total']} pedidos")
        lines.append("")

    # Comparações
    lines.append("## Comparações")
    lines.append("| Base | Pedidos (média) | GMV (média) | Ticket (média) | Var. Pedidos | Var. GMV | Var. Ticket |")
    lines.append("|---|---|---|---|---|---|---|")

    for label, avg in [("30 dias", avg30), ("60 dias", avg60)]:
        lines.append(
            f"| {label} | {avg['avg_orders']} | R$ {avg['avg_gmv']:,.2f} | R$ {avg['avg_ticket']:,.2f} "
            f"| {pct_change(m['pedidos_validos'], avg['avg_orders'])} "
            f"| {pct_change(m['gmv'], avg['avg_gmv'])} "
            f"| {pct_change(m['ticket_medio'], avg['avg_ticket'])} |"
        )

    if avg_weekday:
        wd_orders = sum(d["orders"] for d in avg_weekday) / len(avg_weekday) if avg_weekday else 0
        wd_gmv = sum(d["gmv"] for d in avg_weekday) / len(avg_weekday) if avg_weekday else 0
        wd_ticket = wd_gmv / wd_orders if wd_orders else 0
        lines.append(
            f"| Mesmo dia semana (4x) | {wd_orders:.1f} | R$ {wd_gmv:,.2f} | R$ {wd_ticket:,.2f} "
            f"| {pct_change(m['pedidos_validos'], wd_orders)} "
            f"| {pct_change(m['gmv'], wd_gmv)} "
            f"| {pct_change(m['ticket_medio'], wd_ticket)} |"
        )
    lines.append("")

    # Contexto ADS
    lines.append("## Contexto ADS")
    lines.append(f"Responsável ADS: {acct['ads']}")
    lines.append("_Dados de ADS não disponíveis no banco. Hipóteses marcadas como tal._")
    lines.append("")

    # Memória lida
    lines.append("## Contexto de Memória")
    if memory_context:
        for k, v in memory_context.items():
            if k == "last_daily_file":
                continue
            label = k.replace(".md", "").replace("_", " ").title()
            if k == "last_daily":
                label = f"Última análise ({memory_context.get('last_daily_file', '?')})"
            lines.append(f"- **{label}:** carregado ✓")
    else:
        lines.append("_Nenhuma memória anterior encontrada para esta conta._")
    lines.append("")

    # Hipóteses
    lines.append("## Hipóteses e Insights")
    for h in hypotheses:
        lines.append(f"- {h}")
    lines.append("")

    # Riscos
    lines.append("## Riscos")
    risks = []
    if m["top3_concentration"] > 50:
        risks.append(f"Concentração de {m['top3_concentration']}% nos top 3 SKUs.")
    if m["cancelamentos"] > 0 and m["pedidos_validos"] > 0:
        cancel_rate = m["cancelamentos"] / (m["pedidos_validos"] + m["cancelamentos"]) * 100
        if cancel_rate > 5:
            risks.append(f"Taxa de cancelamento de {cancel_rate:.1f}%.")
    if not risks:
        risks.append("Nenhum risco significativo detectado.")
    for r in risks:
        lines.append(f"- {r}")
    lines.append("")

    # Ação recomendada
    lines.append("## Ação Recomendada")
    if any("queda" in h.lower() for h in hypotheses):
        lines.append(f"- Revisar campanhas ADS com {acct['ads']}.")
        lines.append(f"- Verificar exposição e tráfego na plataforma.")
    else:
        lines.append("- Manter operação atual. Monitorar tendências.")
    lines.append("")

    # O que observar amanhã
    lines.append("## O Que Observar Amanhã")
    lines.append(f"- Tendência de pedidos: hoje {m['pedidos_validos']} vs média 30d {avg30['avg_orders']}.")
    lines.append(f"- Ticket médio: hoje R$ {m['ticket_medio']:.2f} vs média 30d R$ {avg30['avg_ticket']:.2f}.")
    if acct["platform"] == "amazon":
        lines.append("- Verificar Buy Box e status FBA.")
    lines.append("")

    # Observações para Kobe/Pedro
    lines.append("## Observações para Kobe/Pedro")
    lines.append(f"- Conta: {acct['name']}")
    lines.append(f"- Dia analisado: {date_str} ({weekday_pt})")
    lines.append(f"- GMV: R$ {m['gmv']:,.2f} | Pedidos: {m['pedidos_validos']} | Ticket: R$ {m['ticket_medio']:,.2f}")
    if any("⚠️" in h for h in hypotheses):
        lines.append("- **Atenção:** hipóteses de anomalia detectadas — ver seção acima.")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def analyze_account(sb, date_str: str, account_slug: str, dry_run: bool, canonical_by_platform=None):
    acct = ACCOUNTS[account_slug]
    print(f"\n{'='*60}")
    print(f"  Analisando: {acct['name']} ({account_slug})")
    print(f"  Data: {date_str}")
    print(f"{'='*60}")

    # 1. Fetch orders
    print("  → Buscando pedidos do dia...")
    valid, cancelled = fetch_orders(sb, date_str, account_slug)
    print(f"    Pedidos válidos: {len(valid)} | Cancelados: {len(cancelled)}")

    # 2. Metrics
    metrics = compute_metrics(valid, cancelled)

    # 3. Historical
    print("  → Buscando histórico 30 dias...")
    hist30 = fetch_historical_orders(sb, date_str, 30, account_slug)
    avg30 = compute_historical_avg(hist30, 30)

    print("  → Buscando histórico 60 dias...")
    hist60 = fetch_historical_orders(sb, date_str, 60, account_slug)
    avg60 = compute_historical_avg(hist60, 60)

    print("  → Buscando mesmo dia da semana (4x)...")
    avg_weekday = fetch_same_weekday_orders(sb, date_str, account_slug, 4)

    # 4. Memory context
    memory_ctx = read_account_memory(account_slug)

    # 5. Hypotheses
    hypotheses = generate_hypotheses(metrics, avg30, avg60, avg_weekday, account_slug)

    # 6. Reconcile with canonical platform summary
    reconciliation = None
    if canonical_by_platform is not None:
        reconciliation = reconciliation_for_platform(canonical_by_platform, acct["platform"], metrics["pedidos_validos"], metrics["gmv"])
        if not reconciliation["ok"]:
            print(
                "    ⚠ Divergência vs total canônico BRT da plataforma: "
                    f"{reconciliation['order_delta']:+d} pedidos | {format_brl(reconciliation['revenue_delta'])}"
                )

    # 7. Generate analysis
    analysis = format_analysis(date_str, account_slug, metrics, avg30, avg60, avg_weekday, hypotheses, memory_ctx, reconciliation)

    # 7. Output
    if dry_run:
        print("\n--- PREVIEW (dry-run) ---")
        print(analysis[:2000])
        if len(analysis) > 2000:
            print(f"  ... (truncado, {len(analysis)} chars total)")
        print("--- FIM PREVIEW ---\n")
    else:
        out_dir = ACCOUNTS_DIR / account_slug / "daily"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{date_str}.md"

        if out_path.exists():
            backup = out_path.with_suffix(f".md.bak")
            print(f"  ⚠ Arquivo já existe! Criando backup: {backup.name}")
            out_path.rename(backup)

        out_path.write_text(analysis, encoding="utf-8")
        print(f"  ✅ Salvo: {out_path.relative_to(WORKSPACE)}")

    return {
        "slug": account_slug,
        "name": acct["name"],
        "metrics": metrics,
        "avg30": avg30,
        "avg60": avg60,
        "analysis_len": len(analysis),
        "reconciliation": reconciliation,
    }


def main():
    parser = argparse.ArgumentParser(description="Daily Sales v2 — Analyzer (Fase 3)")
    parser.add_argument("date", help="Data no formato YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true", help="Apenas exibe, não salva")
    parser.add_argument("--write-memory", action="store_true", help="Salva análise em memória")
    parser.add_argument("--accounts", default="all", help="Contas separadas por vírgula ou 'all'")
    args = parser.parse_args()

    # Validate date
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print("ERRO: Data inválida. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)

    # Determine mode
    dry_run = args.dry_run or not args.write_memory

    # Select accounts
    if args.accounts == "all":
        slugs = list(ACCOUNTS.keys())
    else:
        slugs = [s.strip() for s in args.accounts.split(",")]
        for s in slugs:
            if s not in ACCOUNTS:
                print(f"ERRO: Conta desconhecida '{s}'. Opções: {', '.join(ACCOUNTS.keys())}", file=sys.stderr)
                sys.exit(1)

    mode_label = "DRY-RUN" if dry_run else "WRITE-MEMORY"
    print(f"\n🔍 Daily Sales v2 Analyzer — Fase 3")
    print(f"   Data: {args.date} | Modo: {mode_label} | Contas: {len(slugs)}")

    sb = get_supabase()
    canonical_by_platform = fetch_v_daily_sales(sb, args.date)
    selected_platforms = {ACCOUNTS[slug]["platform"] for slug in slugs}
    if not canonical_by_platform:
        print("  ⚠ orders BRT sem dados para a data. A análise será marcada como não reconciliada.")
    else:
        selected_rows = [row for platform, row in canonical_by_platform.items() if platform in selected_platforms]
        canonical_orders = sum(int(row.get("order_count") or 0) for row in selected_rows)
        canonical_revenue = sum(float(row.get("total_revenue") or 0) for row in selected_rows)
        print(f"   Fonte canônica orders BRT (escopo selecionado): {canonical_orders} pedidos | {format_brl(canonical_revenue)}")

    results = []

    for slug in slugs:
        try:
            r = analyze_account(sb, args.date, slug, dry_run, canonical_by_platform)
            results.append(r)
        except Exception as e:
            print(f"  ❌ ERRO ao analisar {slug}: {e}")
            import traceback
            traceback.print_exc()

    # Summary
    print(f"\n{'='*60}")
    print(f"  RESUMO — {args.date} ({mode_label})")
    print(f"{'='*60}")
    for r in results:
        m = r["metrics"]
        print(f"  {r['name']:<40} Ped: {m['pedidos_validos']:>4} | GMV: R$ {m['gmv']:>10,.2f} | Ticket: R$ {m['ticket_medio']:>7,.2f}")

    total_ped = sum(r["metrics"]["pedidos_validos"] for r in results)
    total_gmv = sum(r["metrics"]["gmv"] for r in results)
    print(f"  {'TOTAL orders granular':<40} Ped: {total_ped:>4} | GMV: R$ {total_gmv:>10,.2f}")

    if canonical_by_platform:
        selected_rows = [row for platform, row in canonical_by_platform.items() if platform in {ACCOUNTS[r['slug']]['platform'] for r in results}]
        canonical_orders = sum(int(row.get("order_count") or 0) for row in selected_rows)
        canonical_revenue = sum(float(row.get("total_revenue") or 0) for row in selected_rows)
        print(f"  {'TOTAL orders BRT (oficial)':<40} Ped: {canonical_orders:>4} | GMV: R$ {canonical_revenue:>10,.2f}")

    divergences = [r for r in results if r.get("reconciliation") and not r["reconciliation"]["ok"]]
    if divergences:
        print("\n  ⚠ Reconciliação: há divergência entre conta granular e total da plataforma.")
        print("  Regra aplicada: orders BRT é oficial para resumo/Slack e diagnóstico granular.")
    print()

    return results


if __name__ == "__main__":
    main()
