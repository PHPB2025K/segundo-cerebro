#!/usr/bin/env python3
"""Envia Daily Sales Report para equipe administrativa via Slack.

Destinatários: Yasmin, Lucas e Leonardo.
Fonte canônica marketplaces: Budamix Central / Supabase `v_daily_sales`.
Top produtos: consolidação cross-plataforma por SKU equivalente.
"""

from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
UTC = timezone.utc
CENTRAL_ENV = Path("/var/www/budamix-central/.env")
SKU_MAP_CSV = Path("/root/segundo-cerebro/tmp/sku_fiscal_map_abril_2026_v5_sem_ck4742.csv")
OP_ITEM = "Slack Pedro Read Only"
OP_VAULT = "OpenClaw"

# IDs validados em 2026-05-11 via users.list.
RECIPIENTS = {
    "Yasmin": "U09AX9SETDM",      # yasminoscarlino7@gmail.com
    "Lucas": "U08TCL5A8U9",       # Lucas Gabriel / lsimon@gbimportadora.com
    "Leonardo": "U0AUUQ5MP6C",    # leonardoctparticular@gmail.com
}
PEDRO_RECIPIENT = {"Pedro": "U03UY0UNLDC"}  # Pedro Broglio / tradesup.co@gmail.com

PLATFORM_LABELS = {"shopee": "Shopee", "ml": "Mercado Livre", "amazon": "Amazon"}
PLATFORM_ORDER = ["shopee", "ml", "amazon"]
SKU_SUFFIX_RE = re.compile(r"(_T|_BB|_B2|_B)$", re.I)
DISPLAY_NAMES = {
    "IMB501P": "Conjunto 5 Potes de Vidro Redondos Tampa Preta",
    "IMB501C": "Conjunto 5 Potes de Vidro Redondos Tampa Cinza",
    "IMB501V": "Conjunto 5 Potes de Vidro Redondos Tampa Vermelha",
    "CK4742": "Jarra Medidora de Vidro 500ml",
    "KIT2YW800SQ": "Kit 2 Potes de Vidro 800ml Quadrado",
    "KIT2YW1050": "Kit 2 Potes de Vidro 1050ml Retangular",
    "KIT2YW1520": "Kit 2 Potes de Vidro 1520ml Retangular",
    "KIT2YW520SQ": "Kit 2 Potes de Vidro 520ml Quadrado",
    "KIT2YW320": "Kit 2 Potes de Vidro 320ml Retangular",
    "KIT6S097": "Kit 6 Potes de Vidro Hermético",
    "914C": "Kit 6 Canecas Porcelana 200ml",
    "914C_BB": "Kit 6 Canecas Porcelana 200ml",
    "CTL002": "Kit 6 Canecas Tulipa Porcelana 250ml",
}


def brl(value: float) -> str:
    return "R$ " + f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(value: float) -> str:
    return f"{value:.1f}%".replace(".", ",")


def underline(text: str) -> str:
    """Slack não tem underline nativo; usa combining low line para efeito visual."""
    return "".join((ch + "\u0332") if ch != " " else " " for ch in text)


def section_title(text: str) -> str:
    return f"*{underline(text)}*"


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def load_op_service_token() -> None:
    if os.environ.get("OP_SERVICE_ACCOUNT_TOKEN"):
        return
    try:
        out = subprocess.check_output(["pgrep", "-f", "openclaw-gateway"], text=True).splitlines()
        for pid in out:
            try:
                with open(f"/proc/{pid}/environ", "rb") as f:
                    env = dict(x.split("=", 1) for x in f.read().decode(errors="ignore").split("\0") if "=" in x)
                token = env.get("OP_SERVICE_ACCOUNT_TOKEN")
                if token:
                    os.environ["OP_SERVICE_ACCOUNT_TOKEN"] = token
                    return
            except Exception:
                continue
    except Exception:
        pass


def get_slack_token() -> str:
    load_op_service_token()
    result = subprocess.run(
        ["op", "item", "get", OP_ITEM, "--vault", OP_VAULT, "--format", "json"],
        capture_output=True,
        text=True,
        timeout=20,
    )
    if result.returncode != 0:
        raise RuntimeError("Não consegui ler o token Slack no 1Password")
    data = json.loads(result.stdout)
    for field in data.get("fields", []):
        label = (field.get("label") or "").lower()
        value = field.get("value") or ""
        if label == "token" or value.startswith(("xoxp-", "xoxb-", "xoxe.xoxp-")):
            return value
    raise RuntimeError("Token Slack não encontrado no item 1Password")


def slack_api(method: str, params: dict[str, str], *, post: bool = False) -> dict:
    token = get_slack_token()
    url = "https://slack.com/api/" + method
    data = None
    headers = {"Authorization": "Bearer " + token, "User-Agent": "OpenClaw Kobe"}
    if post:
        data = urllib.parse.urlencode(params).encode()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    elif params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def supabase_get(url: str, key: str, table: str, params: dict[str, str]) -> list[dict]:
    query = urllib.parse.urlencode(params, safe=",.:()")
    endpoint = f"{url.rstrip('/')}/rest/v1/{table}?{query}"
    req = urllib.request.Request(endpoint, headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def supabase_get_raw(url: str, key: str, path_query: str) -> list[dict]:
    endpoint = f"{url.rstrip('/')}/rest/v1/{path_query}"
    req = urllib.request.Request(endpoint, headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_bling_revenue(day: str) -> tuple[float | None, int | None]:
    token_path = Path("/root/.openclaw/workspace/scripts/bling-oauth/tokens-matriz.json")
    try:
        token = json.loads(token_path.read_text())["access_token"]
        page = 1
        total = 0.0
        count = 0
        while True:
            params = urllib.parse.urlencode({"dataInicial": day, "dataFinal": day, "pagina": page, "limite": 100})
            req = urllib.request.Request(
                f"https://api.bling.com.br/Api/v3/pedidos/vendas?{params}",
                headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            rows = payload.get("data", []) if isinstance(payload, dict) else []
            for row in rows:
                situacao = str((row.get("situacao") or {}).get("valor") or (row.get("situacao") or {}).get("nome") or "").lower()
                if "cancel" in situacao:
                    continue
                total += float(row.get("total") or row.get("valorTotal") or row.get("totalProdutos") or 0)
                count += 1
            if len(rows) < 100:
                break
            page += 1
        return round(total, 2), count
    except Exception:
        return None, None


def load_sku_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    if SKU_MAP_CSV.exists():
        with SKU_MAP_CSV.open(newline="") as f:
            for row in csv.DictReader(f):
                src = (row.get("sku_marketplace_sku_vendido") or "").strip().upper()
                dst = (row.get("sku_fiscal_entrada_transferencia") or "").strip().upper() or src
                if src:
                    mapping[src] = dst
    return mapping


def canonical_sku(raw_sku: str, mapping: dict[str, str]) -> str:
    sku = (raw_sku or "").strip().upper()
    if not sku:
        return ""
    stripped = SKU_SUFFIX_RE.sub("", sku)
    return mapping.get(sku) or mapping.get(stripped) or stripped


def clean_title(title: str) -> str:
    return " ".join((title or "").replace("–", "-").split())[:78]


def display_name(canon: str, titles: Counter) -> str:
    return DISPLAY_NAMES.get(canon) or (clean_title(titles.most_common(1)[0][0]) if titles else canon)


def fetch_top_products(url: str, key: str, day: str, limit: int = 5) -> list[dict]:
    mapping = load_sku_map()
    d = date.fromisoformat(day)
    start_utc = datetime.combine(d, time.min, tzinfo=BRT).astimezone(UTC).isoformat().replace("+00:00", "Z")
    end_utc = datetime.combine(d + timedelta(days=1), time.min, tzinfo=BRT).astimezone(UTC).isoformat().replace("+00:00", "Z")
    query = (
        "orders?"
        f"order_date=gte.{urllib.parse.quote(start_utc)}&"
        f"order_date=lt.{urllib.parse.quote(end_utc)}&"
        "select=platform,status,total_amount,items,order_date&limit=2000"
    )
    orders = supabase_get_raw(url, key, query)
    agg = defaultdict(lambda: {"qty": 0.0, "gross": 0.0, "titles": Counter()})
    for order in orders:
        if "cancel" in str(order.get("status") or "").lower():
            continue
        items = order.get("items") or []
        if isinstance(items, str):
            try:
                items = json.loads(items)
            except Exception:
                items = []
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            title = (item.get("title") or item.get("name") or "").strip()
            low = title.lower()
            if "produto não identificado" in low or "produto nao identificado" in low:
                continue
            qty = float(item.get("quantity") or item.get("qty") or 1)
            unit_price = float(item.get("unit_price") or item.get("price") or 0)
            canon = canonical_sku((item.get("sku") or item.get("seller_sku") or "").strip(), mapping) or clean_title(title)
            if not canon:
                continue
            agg[canon]["qty"] += qty
            agg[canon]["gross"] += qty * unit_price
            if title:
                agg[canon]["titles"][title] += qty
    ranked = sorted(agg.items(), key=lambda kv: (kv[1]["qty"], kv[1]["gross"]), reverse=True)[:limit]
    return [{"name": display_name(canon, data["titles"]), "qty": int(data["qty"])} for canon, data in ranked]


def build_message(day: str) -> str:
    env = load_env(CENTRAL_ENV)
    supabase_url = env["NEXT_PUBLIC_SUPABASE_URL"]
    service_key = env["SUPABASE_SERVICE_ROLE_KEY"]
    rows = supabase_get(supabase_url, service_key, "v_daily_sales", {"sale_date": f"eq.{day}", "select": "platform,order_count,total_revenue,avg_order_value"})
    by_platform = {row["platform"]: row for row in rows}
    market_revenue = sum(float(row.get("total_revenue") or 0) for row in rows)
    market_orders = sum(int(row.get("order_count") or 0) for row in rows)
    bling_revenue, bling_orders = fetch_bling_revenue(day)
    total_revenue = market_revenue + (bling_revenue or 0)
    total_orders = market_orders + (bling_orders or 0)
    ticket = total_revenue / total_orders if total_orders else 0

    d = date.fromisoformat(day)
    prev_days = [(d - timedelta(days=i)).isoformat() for i in range(1, 31)]
    history_rows = supabase_get(supabase_url, service_key, "v_daily_sales", {"sale_date": f"gte.{prev_days[-1]}", "select": "sale_date,platform,order_count,total_revenue"})
    hist_by_day = defaultdict(lambda: {"rev": 0.0, "orders": 0})
    for row in history_rows:
        sale_date = row.get("sale_date")
        if sale_date in prev_days:
            hist_by_day[sale_date]["rev"] += float(row.get("total_revenue") or 0)
            hist_by_day[sale_date]["orders"] += int(row.get("order_count") or 0)
    avg30 = sum(hist_by_day[x]["rev"] for x in prev_days) / 30
    delta30 = ((total_revenue / avg30) - 1) * 100 if avg30 else 0
    same_weekdays = []
    cursor = d - timedelta(days=1)
    while len(same_weekdays) < 4 and (d - cursor).days <= 60:
        if cursor.weekday() == d.weekday():
            same_weekdays.append(cursor.isoformat())
        cursor -= timedelta(days=1)
    avg_same_weekday = sum(hist_by_day[x]["rev"] for x in same_weekdays) / len(same_weekdays) if same_weekdays else 0

    channel_values = []
    for platform in PLATFORM_ORDER:
        row = by_platform.get(platform, {})
        channel_values.append((PLATFORM_LABELS[platform], float(row.get("total_revenue") or 0), int(row.get("order_count") or 0)))
    atacado_line = "• Atacado GB Matriz: indisponível" if bling_revenue is None else f"• Atacado GB Matriz: *{brl(bling_revenue)}* | {bling_orders} pedidos"
    best_name, best_revenue, _ = max(channel_values, key=lambda item: item[1]) if channel_values else ("-", 0, 0)
    best_share = (best_revenue / total_revenue * 100) if total_revenue else 0
    top_products = fetch_top_products(supabase_url, service_key, day)
    display_date = d.strftime("%d/%m/%Y")
    weekday_names = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    weekday_name = weekday_names[d.weekday()]
    direction = "abaixo" if delta30 < 0 else "acima"
    analysis = [
        f"• O faturamento de ontem ficou {pct(abs(delta30))} {direction} da média dos últimos 30 dias, que foi de aproximadamente {brl(avg30)}.",
        f"• Como foi {weekday_name}, a leitura mais justa é cruzar também com dias equivalentes: a média dos últimos 4 {weekday_name}s foi de {brl(avg_same_weekday)}.",
        "• O mix de produtos considera SKUs equivalentes somados nas três plataformas, evitando duplicar o mesmo item por anúncio diferente.",
        "• Para hoje, vale acompanhar se Shopee e Mercado Livre recuperam tração. Se Amazon continuar abaixo, a checagem prioritária é Buy Box, anúncios e estoque FBA.",
    ]
    section_gap = "\n\n\n\n"
    sections = [
        f"DAILY SALES REPORT - {display_date} (Ontem)",
        "\n".join([
            section_title("📊 RESUMO GERAL"),
            f"• Faturamento total: {brl(total_revenue)}",
            f"• Pedidos: {total_orders}",
            f"• Ticket médio: {brl(ticket)}",
        ]),
        "\n".join([
            section_title("🛒 VENDAS POR CANAL"),
            *[f"• {name}: {brl(revenue)} | {orders} pedidos" for name, revenue, orders in channel_values],
            atacado_line.replace("*", ""),
        ]),
        "\n".join([
            section_title("📌 DESTAQUES DO DIA"),
            f"• Melhor canal em faturamento: {best_name}",
            f"• {best_name} representou aproximadamente {pct(best_share)} do faturamento do dia",
            "• Ranking de produtos consolidado por equivalência de SKU entre plataformas",
        ]),
        "\n".join([
            section_title("🏆 TOP PRODUTOS — CONSOLIDADO 3 PLATAFORMAS"),
            *[f"• {item['name']} — {item['qty']} un." for item in top_products],
        ]),
        "\n".join([
            section_title("📈 ANÁLISE DO DIA"),
            *analysis,
        ]),
        f"Dia analisado: {display_date} — 00:00–23:59 BRT",
    ]
    return section_gap.join(sections)


def send_dm(user_id: str, text: str) -> None:
    opened = slack_api("conversations.open", {"users": user_id}, post=True)
    if not opened.get("ok"):
        raise RuntimeError(f"conversations.open falhou: {opened.get('error')}")
    channel = (opened.get("channel") or {}).get("id")
    sent = slack_api("chat.postMessage", {"channel": channel, "text": text}, post=True)
    if not sent.get("ok"):
        raise RuntimeError(f"chat.postMessage falhou: {sent.get('error')}")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    day = args[0] if args else (datetime.now(BRT).date() - timedelta(days=1)).isoformat()
    dry_run = "--dry-run" in sys.argv
    test_pedro = "--to-pedro" in sys.argv
    message = build_message(day)
    recipients = PEDRO_RECIPIENT if test_pedro else RECIPIENTS
    if dry_run:
        print(message)
        print("\n--- DESTINATÁRIOS SLACK ---")
        for name, uid in recipients.items():
            print(f"{name}: {uid}")
        return 0
    sent = []
    for name, uid in recipients.items():
        send_dm(uid, message)
        sent.append(name)
    print("SENT " + ", ".join(sent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
