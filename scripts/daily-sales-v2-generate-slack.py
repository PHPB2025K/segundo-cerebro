#!/usr/bin/env python3
"""Daily Sales Report v2 — Fase 4: Geração de mensagens Slack individuais.

Gera 3 mensagens Slack individuais para Lucas (Shopee), Yasmin (Mercado Livre)
e Leonardo (Amazon), usando v_daily_sales como fonte oficial e análises
internas salvas pela Fase 3.

Uso:
    python3 scripts/daily-sales-v2-generate-slack.py 2026-05-11 --dry-run
    python3 scripts/daily-sales-v2-generate-slack.py 2026-05-11 --write-preview
    python3 scripts/daily-sales-v2-generate-slack.py 2026-05-11 --to-pedro
    python3 scripts/daily-sales-v2-generate-slack.py 2026-05-11 --send-real
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------

BRT = timezone(timedelta(hours=-3))
UTC = timezone.utc
CENTRAL_ENV = Path("/var/www/budamix-central/.env")
WORKSPACE = Path(__file__).resolve().parent.parent
MEMORY_BASE = (
    WORKSPACE
    / "openclaw"
    / "agents"
    / "kobe"
    / "shared"
    / "trader"
    / "memory"
    / "projects"
    / "daily-sales-report"
)
ACCOUNTS_DIR = MEMORY_BASE / "accounts"
REPORTS_DIR = WORKSPACE / "reports" / "daily-sales-report-v2" / "phase4"

OP_ITEM = "Slack Pedro Read Only"
OP_VAULT = "OpenClaw"

RECIPIENTS = {
    "Lucas": "U08TCL5A8U9",
    "Yasmin": "U09AX9SETDM",
    "Leonardo": "U0AUUQ5MP6C",
}
PEDRO_RECIPIENT = {"Pedro": "U03UY0UNLDC"}

PLATFORM_LABELS = {"shopee": "Shopee", "ml": "Mercado Livre", "amazon": "Amazon"}
PLATFORM_ORDER = ["shopee", "ml", "amazon"]

# Mapeamento de contas por responsável
RECIPIENT_ACCOUNTS = {
    "Lucas": {
        "platform_label": "Shopee",
        "platform_key": "shopee",
        "accounts": [
            {"slug": "shopee-budamix-store", "label": "Budamix Store"},
            {"slug": "shopee-budamix-oficial-2", "label": "Budamix Oficial / Conta 2"},
            {"slug": "shopee-budamix-shop-3", "label": "Budamix Shop / Conta 3"},
        ],
    },
    "Yasmin": {
        "platform_label": "Mercado Livre",
        "platform_key": "ml",
        "accounts": [
            {"slug": "mercado-livre", "label": "Mercado Livre"},
        ],
    },
    "Leonardo": {
        "platform_label": "Amazon",
        "platform_key": "amazon",
        "accounts": [
            {"slug": "amazon", "label": "Amazon"},
        ],
    },
}

# ADS responsável por plataforma
ADS_OWNER = {
    "shopee": "Himmel",
    "ml": "Himmel",
    "amazon": "Pedro",
}


# ---------------------------------------------------------------------------
# Utilitários
# ---------------------------------------------------------------------------


def brl(value: float) -> str:
    return "R$ " + f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(value: float) -> str:
    return f"{value:.1f}%".replace(".", ",")


# ---------------------------------------------------------------------------
# Supabase
# ---------------------------------------------------------------------------


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


def fetch_v_daily_sales(day: str) -> dict[str, dict]:
    """Busca v_daily_sales canônica. Retorna dict por plataforma."""
    env = load_env(CENTRAL_ENV)
    url = env["NEXT_PUBLIC_SUPABASE_URL"]
    key = env["SUPABASE_SERVICE_ROLE_KEY"]
    rows = supabase_get(
        url,
        key,
        "v_daily_sales",
        {
            "sale_date": f"eq.{day}",
            "select": "platform,order_count,total_revenue,avg_order_value",
        },
    )
    return {row["platform"]: row for row in rows}


def fetch_v_daily_sales_history(day: str, days: int = 30) -> dict[str, dict]:
    """Busca histórico de v_daily_sales para comparação."""
    env = load_env(CENTRAL_ENV)
    url = env["NEXT_PUBLIC_SUPABASE_URL"]
    key = env["SUPABASE_SERVICE_ROLE_KEY"]
    d = date.fromisoformat(day)
    start = (d - timedelta(days=days)).isoformat()
    rows = supabase_get(
        url,
        key,
        "v_daily_sales",
        {
            "sale_date": f"gte.{start}",
            "sale_date": f"lt.{day}",
            "select": "sale_date,platform,order_count,total_revenue",
        },
    )
    from collections import defaultdict

    by_day: dict[str, dict] = defaultdict(lambda: {"rev": 0.0, "orders": 0})
    for row in rows:
        sd = row.get("sale_date")
        by_day[sd]["rev"] += float(row.get("total_revenue") or 0)
        by_day[sd]["orders"] += int(row.get("order_count") or 0)
    return dict(by_day)


# ---------------------------------------------------------------------------
# Leitura de análises da Fase 3
# ---------------------------------------------------------------------------


def read_daily_analysis(account_slug: str, day: str) -> str | None:
    """Lê a análise diária da Fase 3 para uma conta."""
    path = ACCOUNTS_DIR / account_slug / "daily" / f"{day}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def parse_analysis(md: str) -> dict:
    """Extrai dados-chave da análise markdown da Fase 3."""
    result: dict = {
        "pedidos": 0,
        "cancelamentos": 0,
        "gmv": 0.0,
        "ticket": 0.0,
        "itens": 0,
        "top_skus": [],
        "concentration_top3": 0.0,
        "hypotheses": [],
        "risks": [],
        "actions": [],
        "comparisons": {},
        "fulfillment": "",
        "canonical_orders": 0,
        "canonical_revenue": 0.0,
    }

    def parse_number(s: str) -> float:
        """Parse number from markdown: '2,896.47' (US format with comma thousands)."""
        return float(s.replace(",", ""))

    # Métricas
    m = re.search(r"Pedidos válidos \| (\d+)", md)
    if m:
        result["pedidos"] = int(m.group(1))
    m = re.search(r"Cancelamentos \| (\d+)", md)
    if m:
        result["cancelamentos"] = int(m.group(1))
    m = re.search(r"Faturamento/GMV \| R\$ ([\d.,]+)", md)
    if m:
        result["gmv"] = parse_number(m.group(1))
    m = re.search(r"Ticket médio \| R\$ ([\d.,]+)", md)
    if m:
        result["ticket"] = parse_number(m.group(1))
    m = re.search(r"Itens vendidos \| (\d+)", md)
    if m:
        result["itens"] = int(m.group(1))

    # Canonical from reconciliation
    m = re.search(r"v_daily_sales \([^)]+\):\*\* (\d+) pedidos \| R\$ ([\d.,]+)", md)
    if m:
        result["canonical_orders"] = int(m.group(1))
        result["canonical_revenue"] = parse_number(m.group(2))

    # Top SKUs
    for m in re.finditer(r"\| \d+ \| ([^\|]+) \| (\d+) \|", md):
        sku = m.group(1).strip()
        qty = int(m.group(2))
        result["top_skus"].append((sku, qty))

    # Concentration
    m = re.search(r"Concentração top 3:\*\* ([\d.,]+)%", md)
    if m:
        result["concentration_top3"] = float(m.group(1).replace(",", "."))

    # Hypotheses
    in_hyp = False
    in_risks = False
    in_actions = False
    for line in md.splitlines():
        stripped = line.strip()
        if "## Hipóteses e Insights" in line:
            in_hyp = True
            in_risks = False
            in_actions = False
            continue
        if "## Riscos" in line:
            in_hyp = False
            in_risks = True
            in_actions = False
            continue
        if "## Ação Recomendada" in line:
            in_hyp = False
            in_risks = False
            in_actions = True
            continue
        if stripped.startswith("## "):
            in_hyp = False
            in_risks = False
            in_actions = False
            continue
        if in_hyp and stripped.startswith("- "):
            result["hypotheses"].append(stripped[2:])
        if in_risks and stripped.startswith("- "):
            result["risks"].append(stripped[2:])
        if in_actions and stripped.startswith("- "):
            result["actions"].append(stripped[2:])

    # Comparisons (30d)
    m = re.search(
        r"\| 30 dias \| ([\d.]+) \| R\$ ([\d.,]+) \| R\$ ([\d.,]+) \| ([^\|]+) \| ([^\|]+) \| ([^\|]+) \|",
        md,
    )
    if m:
        result["comparisons"]["30d"] = {
            "avg_orders": float(m.group(1)),
            "avg_gmv": m.group(2).strip(),
            "avg_ticket": m.group(3).strip(),
            "var_orders": m.group(4).strip(),
            "var_gmv": m.group(5).strip(),
            "var_ticket": m.group(6).strip(),
        }

    # Fulfillment
    m = re.search(r"(Shopee Full|FBA): (\d+/\d+)", md)
    if m:
        result["fulfillment"] = f"{m.group(1)}: {m.group(2)} pedidos"

    return result


# ---------------------------------------------------------------------------
# Geração de mensagens Slack
# ---------------------------------------------------------------------------


def build_general_summary(canonical: dict[str, dict], day: str) -> list[str]:
    """Gera o bloco de Resumo Geral (igual para os 3 destinatários)."""
    total_rev = sum(float(r.get("total_revenue") or 0) for r in canonical.values())
    total_orders = sum(int(r.get("order_count") or 0) for r in canonical.values())
    ticket = total_rev / total_orders if total_orders else 0

    lines = []
    lines.append(f"• Faturamento total marketplaces: {brl(total_rev)}")
    lines.append(f"• Pedidos totais: {total_orders}")
    lines.append(f"• Ticket medio: {brl(ticket)}")

    for pk in PLATFORM_ORDER:
        row = canonical.get(pk, {})
        rev = float(row.get("total_revenue") or 0)
        orders = int(row.get("order_count") or 0)
        label = PLATFORM_LABELS[pk]
        lines.append(f"• {label}: {brl(rev)} | {orders} pedidos")

    return lines


def build_lucas_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Lucas — Shopee."""
    d = date.fromisoformat(day)
    display_date = d.strftime("%d/%m/%Y")
    weekday_names = [
        "segunda-feira", "terca-feira", "quarta-feira",
        "quinta-feira", "sexta-feira", "sabado", "domingo",
    ]
    weekday = weekday_names[d.weekday()]

    sections = []

    # Titulo
    sections.append(f"DAILY SALES REPORT — SHOPEE\n{display_date} ({weekday}) — 00:00-23:59 BRT")

    # Resumo geral
    summary_lines = build_general_summary(canonical, day)
    sections.append("*RESUMO GERAL DA OPERACAO*\n" + "\n".join(summary_lines))

    # Visao Shopee oficial
    shopee_row = canonical.get("shopee", {})
    shopee_rev = float(shopee_row.get("total_revenue") or 0)
    shopee_orders = int(shopee_row.get("order_count") or 0)
    shopee_ticket = shopee_rev / shopee_orders if shopee_orders else 0

    shopee_lines = []
    shopee_lines.append(f"• Faturamento oficial Shopee: {brl(shopee_rev)}")
    shopee_lines.append(f"• Pedidos Shopee: {shopee_orders}")
    shopee_lines.append(f"• Ticket medio Shopee: {brl(shopee_ticket)}")
    sections.append("*VISAO SHOPEE*\n" + "\n".join(shopee_lines))

    # Diagnostico por conta
    account_slugs = [
        ("shopee-budamix-store", "Budamix Store"),
        ("shopee-budamix-oficial-2", "Budamix Oficial / Conta 2"),
        ("shopee-budamix-shop-3", "Budamix Shop / Conta 3"),
    ]
    diag_lines = []
    for slug, label in account_slugs:
        a = analyses.get(slug)
        if not a:
            diag_lines.append(f"• {label}: analise nao disponivel")
            continue

        diag_lines.append(f"• {label}: {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")

        # Top SKU
        if a["top_skus"]:
            top = a["top_skus"][0]
            diag_lines.append(f"  - SKU principal: {top[0]} ({top[1]} un.)")

        # Concentracao
        if a["concentration_top3"] > 60:
            diag_lines.append(f"  - Concentracao top 3 SKUs: {pct(a['concentration_top3'])} (alta)")

        # Comparacao 30d
        comp = a["comparisons"].get("30d")
        if comp:
            diag_lines.append(f"  - Variacao vs media 30d: pedidos {comp['var_orders']} | GMV {comp['var_gmv']}")

        # Cancelamentos relevantes
        if a["cancelamentos"] > 0 and a["pedidos"] > 0:
            cancel_rate = a["cancelamentos"] / (a["pedidos"] + a["cancelamentos"]) * 100
            if cancel_rate > 5:
                diag_lines.append(f"  - Taxa de cancelamento: {pct(cancel_rate)}")

        # Hipoteses relevantes
        for h in a["hypotheses"]:
            if "trafego" in h.lower() or "ads" in h.lower() or "exposicao" in h.lower():
                diag_lines.append(f"  - Ponto para alinhar com Himmel: sinal de queda de trafego/exposicao")
                break

    sections.append("*DIAGNOSTICO POR CONTA*\n" + "\n".join(diag_lines))

    # Prioridades
    prio_lines = []
    for slug, label in account_slugs:
        a = analyses.get(slug)
        if not a:
            continue
        comp = a["comparisons"].get("30d")
        if comp and comp["var_orders"].startswith("-") and float(comp["var_orders"].rstrip("%")) < -10:
            prio_lines.append(f"• {label}: acompanhar se volume de pedidos recupera; verificar anuncios e exposicao")
        elif a["concentration_top3"] > 80:
            prio_lines.append(f"• {label}: mix muito concentrado — vale avaliar diversificacao de anuncios")

    if not prio_lines:
        prio_lines.append("• Monitorar operacao normal. Sem acoes urgentes identificadas")

    # ADS
    any_traffic_signal = any(
        any("trafego" in h.lower() or "ads" in h.lower() for h in analyses.get(s, {}).get("hypotheses", []))
        for s, _ in account_slugs
    )
    if any_traffic_signal:
        prio_lines.append("• Ponto para Himmel: verificar performance de campanhas Shopee")

    sections.append("*PRIORIDADES DO DIA*\n" + "\n".join(prio_lines))

    return "\n\n".join(sections)


def build_yasmin_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Yasmin — Mercado Livre."""
    d = date.fromisoformat(day)
    display_date = d.strftime("%d/%m/%Y")
    weekday_names = [
        "segunda-feira", "terca-feira", "quarta-feira",
        "quinta-feira", "sexta-feira", "sabado", "domingo",
    ]
    weekday = weekday_names[d.weekday()]

    sections = []

    # Titulo
    sections.append(f"DAILY SALES REPORT — MERCADO LIVRE\n{display_date} ({weekday}) — 00:00-23:59 BRT")

    # Resumo geral
    summary_lines = build_general_summary(canonical, day)
    sections.append("*RESUMO GERAL DA OPERACAO*\n" + "\n".join(summary_lines))

    # Visao ML oficial
    ml_row = canonical.get("ml", {})
    ml_rev = float(ml_row.get("total_revenue") or 0)
    ml_orders = int(ml_row.get("order_count") or 0)
    ml_ticket = ml_rev / ml_orders if ml_orders else 0

    ml_lines = []
    ml_lines.append(f"• Faturamento oficial Mercado Livre: {brl(ml_rev)}")
    ml_lines.append(f"• Pedidos Mercado Livre: {ml_orders}")
    ml_lines.append(f"• Ticket medio Mercado Livre: {brl(ml_ticket)}")
    sections.append("*VISAO MERCADO LIVRE*\n" + "\n".join(ml_lines))

    # Diagnostico ML
    a = analyses.get("mercado-livre")
    diag_lines = []
    if a:
        # Top SKUs
        diag_lines.append("• Produtos que mais venderam:")
        for sku, qty in a["top_skus"][:5]:
            diag_lines.append(f"  - {sku}: {qty} un.")

        # Concentracao
        diag_lines.append(f"• Concentracao top 3 SKUs: {pct(a['concentration_top3'])}")

        # Comparacao 30d
        comp = a["comparisons"].get("30d")
        if comp:
            diag_lines.append(f"• Variacao vs media 30d: pedidos {comp['var_orders']} | GMV {comp['var_gmv']}")

        # Cancelamentos
        if a["cancelamentos"] > 0 and a["pedidos"] > 0:
            cancel_rate = a["cancelamentos"] / (a["pedidos"] + a["cancelamentos"]) * 100
            if cancel_rate > 5:
                diag_lines.append(f"• Taxa de cancelamento: {pct(cancel_rate)}")

        # Hipoteses
        for h in a["hypotheses"]:
            if "normal" in h.lower() or "parametros" in h.lower():
                diag_lines.append("• Dia dentro dos parametros normais. Sem anomalias detectadas")
            elif "trafego" in h.lower() or "ads" in h.lower():
                diag_lines.append("• Ponto para alinhar com Himmel: sinal de possivel queda de trafego/exposicao")
            elif "concentracao" in h.lower():
                diag_lines.append(f"• {h.lstrip('⚠️ ').lstrip('HIPÓTESE: ')}")
    else:
        diag_lines.append("• Analise detalhada nao disponivel para o dia")

    sections.append("*DIAGNOSTICO MERCADO LIVRE*\n" + "\n".join(diag_lines))

    # Prioridades
    prio_lines = []
    if a:
        comp = a["comparisons"].get("30d")
        if comp and comp["var_orders"].startswith("-") and float(comp["var_orders"].rstrip("%")) < -10:
            prio_lines.append("• Acompanhar volume de pedidos; verificar exposicao dos anuncios principais")
        if any("trafego" in h.lower() or "ads" in h.lower() for h in a.get("hypotheses", [])):
            prio_lines.append("• Ponto para Himmel: checar performance de campanhas ML")

    if not prio_lines:
        prio_lines.append("• Monitorar operacao normal. Sem acoes urgentes identificadas")

    sections.append("*PRIORIDADES DO DIA*\n" + "\n".join(prio_lines))

    return "\n\n".join(sections)


def build_leonardo_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Leonardo — Amazon."""
    d = date.fromisoformat(day)
    display_date = d.strftime("%d/%m/%Y")
    weekday_names = [
        "segunda-feira", "terca-feira", "quarta-feira",
        "quinta-feira", "sexta-feira", "sabado", "domingo",
    ]
    weekday = weekday_names[d.weekday()]

    sections = []

    # Titulo
    sections.append(f"DAILY SALES REPORT — AMAZON\n{display_date} ({weekday}) — 00:00-23:59 BRT")

    # Resumo geral
    summary_lines = build_general_summary(canonical, day)
    sections.append("*RESUMO GERAL DA OPERACAO*\n" + "\n".join(summary_lines))

    # Visao Amazon oficial
    amz_row = canonical.get("amazon", {})
    amz_rev = float(amz_row.get("total_revenue") or 0)
    amz_orders = int(amz_row.get("order_count") or 0)
    amz_ticket = amz_rev / amz_orders if amz_orders else 0

    amz_lines = []
    amz_lines.append(f"• Faturamento oficial Amazon: {brl(amz_rev)}")
    amz_lines.append(f"• Pedidos Amazon: {amz_orders}")
    amz_lines.append(f"• Ticket medio Amazon: {brl(amz_ticket)}")
    sections.append("*VISAO AMAZON*\n" + "\n".join(amz_lines))

    # Diagnostico Amazon
    a = analyses.get("amazon")
    diag_lines = []
    if a:
        # Fulfillment
        if a["fulfillment"]:
            diag_lines.append(f"• Fulfillment: {a['fulfillment']}")

        # Top SKUs
        diag_lines.append("• Produtos que mais venderam:")
        for sku, qty in a["top_skus"][:5]:
            diag_lines.append(f"  - {sku}: {qty} un.")

        # Concentracao
        diag_lines.append(f"• Concentracao top 3 SKUs: {pct(a['concentration_top3'])}")

        # Comparacao 30d
        comp = a["comparisons"].get("30d")
        if comp:
            diag_lines.append(f"• Variacao vs media 30d: pedidos {comp['var_orders']} | GMV {comp['var_gmv']}")

        # Cancelamentos
        if a["cancelamentos"] > 0 and a["pedidos"] > 0:
            cancel_rate = a["cancelamentos"] / (a["pedidos"] + a["cancelamentos"]) * 100
            if cancel_rate > 5:
                diag_lines.append(f"• Taxa de cancelamento: {pct(cancel_rate)} — verificar motivo dos cancelamentos")

        # Hipoteses
        for h in a["hypotheses"]:
            if "buy box" in h.lower() or "fba" in h.lower() or "listing" in h.lower():
                diag_lines.append(f"• Operacional Leonardo: verificar Buy Box, FBA e listings")
            elif "concentracao" in h.lower():
                diag_lines.append(f"• Alta concentracao nos top SKUs — avaliar diversificacao de catalogo")
    else:
        diag_lines.append("• Analise detalhada nao disponivel para o dia")

    sections.append("*DIAGNOSTICO AMAZON*\n" + "\n".join(diag_lines))

    # Prioridades — separar operacional Leonardo vs ADS Pedro
    prio_lines = []
    if a:
        comp = a["comparisons"].get("30d")

        # Operacional Leonardo
        if a["fulfillment"] and "FBA" in a["fulfillment"]:
            prio_lines.append("• Operacional: confirmar estoque FBA e status de envio")
        if a["concentration_top3"] > 70:
            prio_lines.append("• Operacional: acompanhar listings dos SKUs principais no catalogo")

        # Cancelamentos altos
        if a["cancelamentos"] > 0 and a["pedidos"] > 0:
            cancel_rate = a["cancelamentos"] / (a["pedidos"] + a["cancelamentos"]) * 100
            if cancel_rate > 10:
                prio_lines.append("• Operacional: investigar causa dos cancelamentos (estoque, prazo, FBA)")

        # ADS Pedro
        if comp and comp["var_orders"].startswith("-") and float(comp["var_orders"].rstrip("%")) < -10:
            prio_lines.append("• Gestao/ADS (Pedro): acompanhar se queda de volume persiste; avaliar campanhas")

    if not prio_lines:
        prio_lines.append("• Monitorar operacao normal. Sem acoes urgentes identificadas")

    sections.append("*PRIORIDADES DO DIA*\n" + "\n".join(prio_lines))

    return "\n\n".join(sections)


# ---------------------------------------------------------------------------
# Slack rich_text blocks
# ---------------------------------------------------------------------------

SECTION_TITLES = {
    "RESUMO GERAL DA OPERACAO",
    "VISAO SHOPEE",
    "VISAO MERCADO LIVRE",
    "VISAO AMAZON",
    "DIAGNOSTICO POR CONTA",
    "DIAGNOSTICO MERCADO LIVRE",
    "DIAGNOSTICO AMAZON",
    "PRIORIDADES DO DIA",
}


def message_to_rich_text_blocks(text: str) -> list[dict]:
    elements: list[dict] = []
    lines = text.split("\n")
    for idx, line in enumerate(lines):
        raw = line.strip()
        is_title = raw.startswith("*") and raw.endswith("*") and raw[1:-1] in SECTION_TITLES
        if is_title:
            elements.append(
                {"type": "text", "text": raw[1:-1], "style": {"bold": True, "underline": True}}
            )
        elif line:
            elements.append({"type": "text", "text": line})
        if idx < len(lines) - 1:
            elements.append({"type": "text", "text": "\n"})
    return [
        {
            "type": "rich_text",
            "elements": [{"type": "rich_text_section", "elements": elements}],
        }
    ]


# ---------------------------------------------------------------------------
# Slack API
# ---------------------------------------------------------------------------


def load_op_service_token() -> None:
    if os.environ.get("OP_SERVICE_ACCOUNT_TOKEN"):
        return
    try:
        out = subprocess.check_output(
            ["pgrep", "-f", "openclaw-gateway"], text=True
        ).splitlines()
        for pid in out:
            try:
                with open(f"/proc/{pid}/environ", "rb") as f:
                    env = dict(
                        x.split("=", 1)
                        for x in f.read().decode(errors="ignore").split("\0")
                        if "=" in x
                    )
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
        raise RuntimeError("Nao consegui ler o token Slack no 1Password")
    data = json.loads(result.stdout)
    for field in data.get("fields", []):
        label = (field.get("label") or "").lower()
        value = field.get("value") or ""
        if label == "token" or value.startswith(("xoxp-", "xoxb-", "xoxe.xoxp-")):
            return value
    raise RuntimeError("Token Slack nao encontrado no item 1Password")


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


def send_dm(user_id: str, text: str) -> None:
    opened = slack_api("conversations.open", {"users": user_id}, post=True)
    if not opened.get("ok"):
        raise RuntimeError(f"conversations.open falhou: {opened.get('error')}")
    channel = (opened.get("channel") or {}).get("id")
    sent = slack_api(
        "chat.postMessage",
        {
            "channel": channel,
            "text": text.replace("*", ""),
            "blocks": json.dumps(message_to_rich_text_blocks(text), ensure_ascii=False),
        },
        post=True,
    )
    if not sent.get("ok"):
        raise RuntimeError(f"chat.postMessage falhou: {sent.get('error')}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description="Daily Sales v2 — Slack Message Generator (Fase 4)")
    parser.add_argument("date", help="Data no formato YYYY-MM-DD")
    parser.add_argument("--dry-run", action="store_true", help="Imprime preview sem enviar")
    parser.add_argument("--write-preview", action="store_true", help="Salva previews em markdown/JSON")
    parser.add_argument("--to-pedro", action="store_true", help="Envia teste para Pedro (nao real)")
    parser.add_argument(
        "--send-real",
        action="store_true",
        help="Envia real para Yasmin/Lucas/Leonardo (default OFF)",
    )
    args = parser.parse_args()

    day = args.date
    try:
        datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        print("ERRO: Data invalida. Use YYYY-MM-DD.", file=sys.stderr)
        return 1

    # 1. Buscar v_daily_sales canonica
    print(f"\n--- Daily Sales v2 — Slack Generator (Fase 4) ---")
    print(f"Data: {day}")
    print(f"Buscando v_daily_sales...")

    canonical = fetch_v_daily_sales(day)
    if not canonical:
        print("ERRO: v_daily_sales sem dados para a data.", file=sys.stderr)
        return 1

    total_rev = sum(float(r.get("total_revenue") or 0) for r in canonical.values())
    total_orders = sum(int(r.get("order_count") or 0) for r in canonical.values())
    print(f"v_daily_sales OK: {total_orders} pedidos | {brl(total_rev)}")

    for pk in PLATFORM_ORDER:
        row = canonical.get(pk, {})
        rev = float(row.get("total_revenue") or 0)
        orders = int(row.get("order_count") or 0)
        print(f"  {PLATFORM_LABELS[pk]}: {orders} pedidos | {brl(rev)}")

    # 2. Ler analises da Fase 3
    print(f"\nLendo analises da Fase 3...")
    all_slugs = [
        "shopee-budamix-store",
        "shopee-budamix-oficial-2",
        "shopee-budamix-shop-3",
        "mercado-livre",
        "amazon",
    ]
    analyses: dict[str, dict] = {}
    for slug in all_slugs:
        md = read_daily_analysis(slug, day)
        if md:
            analyses[slug] = parse_analysis(md)
            print(f"  {slug}: OK ({analyses[slug]['pedidos']} pedidos)")
        else:
            print(f"  {slug}: NAO ENCONTRADA")

    # 3. Gerar mensagens
    print(f"\nGerando mensagens individuais...")
    messages = {
        "Lucas": build_lucas_message(canonical, day, analyses),
        "Yasmin": build_yasmin_message(canonical, day, analyses),
        "Leonardo": build_leonardo_message(canonical, day, analyses),
    }

    # 4. Validacoes QA
    print(f"\n--- QA ---")
    for name, msg in messages.items():
        issues = []
        if "atacado" in msg.lower() or "bling" in msg.lower():
            issues.append("CONTEM ATACADO/BLING")
        if "destaque" in msg.lower():
            issues.append("CONTEM DESTAQUES")
        if not msg.strip():
            issues.append("MENSAGEM VAZIA")
        status = "PASS" if not issues else "FAIL: " + ", ".join(issues)
        print(f"  {name}: {status}")

    # 5. Output conforme modo
    if args.dry_run or (not args.write_preview and not args.to_pedro and not args.send_real):
        print(f"\n{'='*60}")
        for name, msg in messages.items():
            print(f"\n--- PREVIEW: {name} ---")
            print(msg)
            print(f"--- FIM {name} ---\n")
        print(f"{'='*60}")
        print("Modo dry-run: nenhuma acao tomada.")
        return 0

    if args.write_preview:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        filemap = {
            "Lucas": f"preview-lucas-shopee-{day}.md",
            "Yasmin": f"preview-yasmin-ml-{day}.md",
            "Leonardo": f"preview-leonardo-amazon-{day}.md",
        }
        for name, msg in messages.items():
            path = REPORTS_DIR / filemap[name]
            path.write_text(msg, encoding="utf-8")
            print(f"  Salvo: {path.relative_to(WORKSPACE)}")

        # JSON payloads
        payloads = {}
        for name, msg in messages.items():
            payloads[name] = {
                "recipient": RECIPIENTS[name],
                "text_fallback": msg.replace("*", ""),
                "blocks": message_to_rich_text_blocks(msg),
            }
        json_path = REPORTS_DIR / f"slack-payloads-{day}.json"
        json_path.write_text(json.dumps(payloads, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Salvo: {json_path.relative_to(WORKSPACE)}")
        print("Previews salvos com sucesso.")
        return 0

    if args.to_pedro:
        print("\nEnviando preview para Pedro...")
        for name, msg in messages.items():
            header = f"[PREVIEW - Mensagem para {name}]\n\n"
            send_dm(PEDRO_RECIPIENT["Pedro"], header + msg)
            print(f"  Enviado preview de {name} para Pedro")
        print("Teste enviado para Pedro.")
        return 0

    if args.send_real:
        print("\n⚠ ENVIO REAL para Yasmin, Lucas e Leonardo!")
        print("Confirme que Kobe autorizou este envio.")
        for name, msg in messages.items():
            uid = RECIPIENTS[name]
            send_dm(uid, msg)
            print(f"  ENVIADO: {name} ({uid})")
        print("Envio real concluido.")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
