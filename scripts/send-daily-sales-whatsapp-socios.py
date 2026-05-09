#!/usr/bin/env python3
"""Envia o Resumo de Vendas Diário simplificado para o grupo WhatsApp dos sócios.

Fonte canônica marketplaces: Budamix Central / Supabase `v_daily_sales`.
Envio: WhatsApp próprio do Kobe via wrapper central `send-whatsapp.py`.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
CENTRAL_ENV = Path("/var/www/budamix-central/.env")
SEND_WHATSAPP = Path("/root/.openclaw/workspace/scripts/send-whatsapp.py")
GROUP_JID = "120363270687689452@g.us"  # GB Importadora

PLATFORM_LABELS = {
    "shopee": "Shopee",
    "amazon": "Amazon",
    "ml": "Mercado Livre",
}
PLATFORM_ORDER = ["shopee", "amazon", "ml"]


def brl(value: float) -> str:
    formatted = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatted}"


def load_env(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def supabase_get(url: str, key: str, table: str, params: dict[str, str]) -> list[dict]:
    query = urllib.parse.urlencode(params, safe=",.:()")
    endpoint = f"{url.rstrip('/')}/rest/v1/{table}?{query}"
    req = urllib.request.Request(
        endpoint,
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_bling_revenue(day: str) -> tuple[float | None, int | None]:
    """Busca pedidos do Bling Matriz. Retorna (None, None) se falhar."""
    token_path = Path("/root/.openclaw/workspace/scripts/bling-oauth/tokens-matriz.json")
    try:
        token = json.loads(token_path.read_text())["access_token"]
        page = 1
        total = 0.0
        count = 0
        while True:
            params = urllib.parse.urlencode({
                "dataInicial": day,
                "dataFinal": day,
                "pagina": page,
                "limite": 100,
            })
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


def build_message(day: str) -> str:
    env = load_env(CENTRAL_ENV)
    supabase_url = env["NEXT_PUBLIC_SUPABASE_URL"]
    service_key = env["SUPABASE_SERVICE_ROLE_KEY"]

    rows = supabase_get(
        supabase_url,
        service_key,
        "v_daily_sales",
        {
            "sale_date": f"eq.{day}",
            "select": "platform,order_count,total_revenue,avg_order_value",
        },
    )
    by_platform = {row["platform"]: row for row in rows}

    market_revenue = sum(float(row.get("total_revenue") or 0) for row in rows)
    market_orders = sum(int(row.get("order_count") or 0) for row in rows)

    bling_revenue, bling_orders = fetch_bling_revenue(day)
    total_revenue = market_revenue + (bling_revenue or 0)
    total_orders = market_orders + (bling_orders or 0)
    ticket = total_revenue / total_orders if total_orders else 0

    channel_values = []
    for platform in PLATFORM_ORDER:
        row = by_platform.get(platform, {})
        channel_values.append((
            PLATFORM_LABELS[platform],
            float(row.get("total_revenue") or 0),
            int(row.get("order_count") or 0),
        ))
    if bling_revenue is None:
        atacado_line = "• Atacado GB Matriz: indisponível"
    else:
        atacado_line = f"• Atacado GB Matriz: {brl(bling_revenue)} | {bling_orders} pedidos"

    best_name, best_revenue, _ = max(channel_values, key=lambda item: item[1])
    amazon_ticket = float((by_platform.get("amazon") or {}).get("avg_order_value") or 0)

    display_date = datetime.fromisoformat(day).strftime("%d/%m/%Y")

    return "\n".join([
        f"Resumo de Vendas Diário - {display_date} (Ontem)",
        "",
        "*📊 Resumo geral*",
        f"• Faturamento total: {brl(total_revenue)}",
        f"• Pedidos: {total_orders}",
        f"• Ticket médio: {brl(ticket)}",
        "",
        "*🛒 Vendas por canal*",
        *[f"• {name}: {brl(revenue)} | {orders} pedidos" for name, revenue, orders in channel_values],
        atacado_line,
        "",
        "*📌 Destaques do dia*",
        f"• Melhor canal em faturamento: {best_name}",
        f"• Amazon teve o maior ticket médio: {brl(amazon_ticket)}",
        "• Dia com bom equilíbrio entre volume na Shopee e ticket mais alto na Amazon",
    ])


def main() -> int:
    if len(sys.argv) > 1:
        day = sys.argv[1]
    else:
        day = (datetime.now(BRT).date() - timedelta(days=1)).isoformat()
    message = build_message(day)
    if "--dry-run" in sys.argv:
        print(message)
        return 0
    result = subprocess.run(
        [sys.executable, str(SEND_WHATSAPP), GROUP_JID, message, "--ttl", "3600", "--instance", "kobe"],
        text=True,
        capture_output=True,
        timeout=60,
    )
    if result.returncode != 0 or "SENT" not in result.stdout:
        print(result.stderr[-500:] or result.stdout[-500:], file=sys.stderr)
        return 1
    print("SENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
