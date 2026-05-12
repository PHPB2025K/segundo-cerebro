#!/usr/bin/env python3
"""Daily Sales Report v2 — Fase 4.1: Geração de mensagens Slack individuais.

Gera 3 mensagens Slack individuais para Lucas (Shopee), Yasmin (Mercado Livre)
e Leonardo (Amazon), usando v_daily_sales como fonte oficial e análises
internas salvas pela Fase 3.

Fase 4.1: correção de qualidade — diagnósticos profundos, nomes de produto
(nunca SKU cru), prioridades acionáveis e formatação visual aprovada.

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
# SKU → Nome Comercial (importado do script canônico)
# ---------------------------------------------------------------------------

SKU_SUFFIX_RE = re.compile(r"(_T|_BB|_B2|_B|_BAP)$", re.I)

DISPLAY_NAMES: dict[str, str] = {
    "IMB501P": "Conjunto 5 Potes de Vidro Redondos Tampa Preta",
    "IMB501C": "Conjunto 5 Potes de Vidro Redondos Tampa Cinza",
    "IMB501V": "Conjunto 5 Potes de Vidro Redondos Tampa Vermelha",
    "IMB501PT": "Conjunto 5 Potes de Vidro Redondos Tampa Preta",
    "IMB501T-PRETO": "Conjunto 5 Potes de Vidro Redondos Tampa Preta",
    "IMB501T-CINZA": "Conjunto 5 Potes de Vidro Redondos Tampa Cinza",
    "CK4742": "Jarra Medidora de Vidro 500ml",
    "KIT2YW800SQ": "Kit 2 Potes de Vidro 800ml Quadrado",
    "KIT4YW800SQ": "Kit 4 Potes de Vidro 800ml Quadrado",
    "KIT2YW1050": "Kit 2 Potes de Vidro 1050ml Retangular",
    "KIT4YW1050": "Kit 4 Potes de Vidro 1050ml Retangular",
    "KIT2YW1520": "Kit 2 Potes de Vidro 1520ml Retangular",
    "KIT2YW520SQ": "Kit 2 Potes de Vidro 520ml Quadrado",
    "KIT2YW320": "Kit 2 Potes de Vidro 320ml Retangular",
    "KIT6S097": "Kit 6 Potes de Vidro Hermético",
    "914C": "Kit 6 Canecas Porcelana 200ml",
    "CTL002": "Kit 6 Canecas Tulipa Porcelana 250ml",
    "CLR002": "Kit 6 Canecas Lisas Redondas Porcelana",
    "KIT6CAR200": "Kit 6 Canecas Altas Retas Porcelana 200ml",
    "KIT3S099": "Kit 3 Potes de Vidro Hermético",
    "K6CAN250": "Kit 6 Canecas 250ml",
    "XCP002": "Xicara Porcelana com Pires",
    "SPC002": "Suporte Porta-Copos",
    "PCM001": "Porta-Copos MDF",
    "TL250": "Tigela de Vidro 250ml",
    "TL250B": "Tigela de Vidro 250ml",
    "TL250P": "Tigela de Vidro 250ml",
    "TL6250": "Kit 6 Tigelas de Vidro 250ml",
    "098": "Pote de Vidro Hermético 800ml",
    "097": "Pote de Vidro Hermético 600ml",
    "008": "Pote de Vidro Hermético Pequeno",
}

# Padrões de SKU cru proibidos no texto visível
RAW_SKU_PATTERNS = re.compile(
    r"\b("
    r"IMB501[PCV]?_[A-Z0-9]+"
    r"|CTL\d{3}"
    r"|CK\d{4}(_[A-Z0-9]+)?"
    r"|914C(_[A-Z0-9]+)?"
    r"|SPC\d{3}"
    r"|TL\d{3,4}[A-Z]?"
    r"|KIT\d[A-Z0-9_]+"
    r"|XCP\d{3}"
    r"|CLR\d{3}"
    r"|PCM\d{3}"
    r"|K6CAN\d+"
    r"|KIT6CAR\d+"
    r"|KIT3S\d+"
    r"|IMB501PT"
    r"|IMB501T-[a-z]+"
    r")\b",
    re.I,
)


def canonical_sku(raw_sku: str) -> str:
    """Normaliza SKU removendo sufixos de variante."""
    sku = (raw_sku or "").strip().upper()
    if not sku:
        return ""
    return SKU_SUFFIX_RE.sub("", sku)


def display_name_from_sku(raw_sku: str) -> str:
    """Converte SKU em nome comercial legível. Nunca retorna SKU cru."""
    canon = canonical_sku(raw_sku)
    if not canon:
        return "Produto não identificado"
    # Tentar lookup direto com SKU original (upper)
    upper = raw_sku.strip().upper()
    if upper in DISPLAY_NAMES:
        return DISPLAY_NAMES[upper]
    # Tentar com canônico
    if canon in DISPLAY_NAMES:
        return DISPLAY_NAMES[canon]
    # Fallback: humanizar o código
    return _humanize_sku(canon)


def _humanize_sku(canon: str) -> str:
    """Fallback para SKUs sem mapeamento — gera nome legível genérico."""
    # Melhor um nome genérico do que mostrar SKU cru
    if canon.startswith("KIT"):
        return f"Kit de Produtos ({canon})"
    return f"Produto Budamix ({canon})"


def qa_check_raw_skus(text: str) -> list[str]:
    """Verifica se há SKUs crus no texto visível. Retorna lista de violações."""
    violations = []
    for line in text.splitlines():
        # Ignorar linhas que são claramente metadados/debug
        if line.strip().startswith("##") or line.strip().startswith("---"):
            continue
        matches = RAW_SKU_PATTERNS.findall(line)
        for m in matches:
            sku = m if isinstance(m, str) else m[0]
            violations.append(f"SKU cru encontrado: '{sku}' na linha: {line.strip()[:80]}")
    return violations


# ---------------------------------------------------------------------------
# Utilitários
# ---------------------------------------------------------------------------


def brl(value: float) -> str:
    return "R$ " + f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(value: float) -> str:
    return f"{value:.1f}%".replace(".", ",")


def var_direction(var_str: str) -> str:
    """Interpreta string de variação como 'acima'/'abaixo'."""
    try:
        val = float(var_str.rstrip("%").replace(",", "."))
        return "acima" if val >= 0 else "abaixo"
    except (ValueError, AttributeError):
        return ""


def var_abs(var_str: str) -> str:
    """Retorna valor absoluto formatado da variação."""
    try:
        val = float(var_str.rstrip("%").replace(",", "."))
        return pct(abs(val))
    except (ValueError, AttributeError):
        return var_str


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
        "watch_tomorrow": [],
    }

    def parse_number(s: str) -> float:
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

    # Hypotheses, Risks, Actions, Watch
    in_hyp = False
    in_risks = False
    in_actions = False
    in_watch = False
    for line in md.splitlines():
        stripped = line.strip()
        if "## Hipóteses e Insights" in line:
            in_hyp, in_risks, in_actions, in_watch = True, False, False, False
            continue
        if "## Riscos" in line:
            in_hyp, in_risks, in_actions, in_watch = False, True, False, False
            continue
        if "## Ação Recomendada" in line:
            in_hyp, in_risks, in_actions, in_watch = False, False, True, False
            continue
        if "## O Que Observar Amanhã" in line:
            in_hyp, in_risks, in_actions, in_watch = False, False, False, True
            continue
        if stripped.startswith("## "):
            in_hyp = in_risks = in_actions = in_watch = False
            continue
        if in_hyp and stripped.startswith("- "):
            result["hypotheses"].append(stripped[2:])
        if in_risks and stripped.startswith("- "):
            result["risks"].append(stripped[2:])
        if in_actions and stripped.startswith("- "):
            result["actions"].append(stripped[2:])
        if in_watch and stripped.startswith("- "):
            result["watch_tomorrow"].append(stripped[2:])

    # Comparisons — 30d, 60d, same weekday
    for m in re.finditer(
        r"\| (30 dias|60 dias|Mesmo dia semana[^|]*) \| ([\d.]+) \| R\$ ([\d.,]+) \| R\$ ([\d.,]+) \| ([^\|]+) \| ([^\|]+) \| ([^\|]+) \|",
        md,
    ):
        label = m.group(1).strip()
        key = "30d" if "30" in label else ("60d" if "60" in label else "same_weekday")
        result["comparisons"][key] = {
            "avg_orders": float(m.group(2)),
            "avg_gmv": m.group(3).strip(),
            "avg_ticket": m.group(4).strip(),
            "var_orders": m.group(5).strip(),
            "var_gmv": m.group(6).strip(),
            "var_ticket": m.group(7).strip(),
        }

    # Fulfillment
    m = re.search(r"(Shopee Full|FBA): (\d+/\d+)", md)
    if m:
        result["fulfillment"] = f"{m.group(1)}: {m.group(2)} pedidos"

    # FBM
    m2 = re.search(r"FBM: (\d+/\d+)", md)
    if m2:
        result["fulfillment_fbm"] = f"FBM: {m2.group(1)} pedidos"

    return result


# ---------------------------------------------------------------------------
# Helpers de formatação de diagnóstico profundo
# ---------------------------------------------------------------------------


def _top_products_text(top_skus: list[tuple[str, int]], limit: int = 5) -> list[str]:
    """Converte top SKUs em linhas com nome comercial."""
    lines = []
    for sku, qty in top_skus[:limit]:
        name = display_name_from_sku(sku)
        lines.append(f"  - {name}: {qty} un.")
    return lines


def _temporal_reading(comparisons: dict, pedidos: int, gmv: float) -> list[str]:
    """Gera leitura temporal completa vs 30d, 60d, mesmo dia da semana."""
    lines = []
    c30 = comparisons.get("30d")
    c60 = comparisons.get("60d")
    csw = comparisons.get("same_weekday")

    if c30:
        lines.append(
            f"  - vs media 30d: pedidos {c30['var_orders']} | GMV {c30['var_gmv']} | ticket {c30['var_ticket']}"
        )
    if c60:
        lines.append(
            f"  - vs media 60d: pedidos {c60['var_orders']} | GMV {c60['var_gmv']}"
        )
    if csw:
        lines.append(
            f"  - vs mesmo dia da semana (4 semanas): pedidos {csw['var_orders']} | GMV {csw['var_gmv']}"
        )
    return lines


def _cancel_analysis(cancelamentos: int, pedidos: int) -> tuple[float, str]:
    """Retorna taxa e texto de cancelamento."""
    if cancelamentos <= 0 or pedidos <= 0:
        return 0.0, ""
    total = pedidos + cancelamentos
    rate = cancelamentos / total * 100
    return rate, pct(rate)


def _concentration_reading(conc: float) -> str:
    """Interpreta concentração."""
    if conc > 90:
        return "muito alta — risco critico de dependencia"
    if conc > 75:
        return "alta — risco de dependencia"
    if conc > 50:
        return "moderada"
    return "saudavel — boa diversificacao"


# ---------------------------------------------------------------------------
# Geração de mensagens Slack
# ---------------------------------------------------------------------------


def build_general_summary(canonical: dict[str, dict], day: str) -> list[str]:
    """Gera o bloco fixo de Resumo Geral (igual para os 3 destinatários)."""
    total_rev = sum(float(r.get("total_revenue") or 0) for r in canonical.values())
    total_orders = sum(int(r.get("order_count") or 0) for r in canonical.values())
    ticket = total_rev / total_orders if total_orders else 0

    return [
        f"• Faturamento total: {brl(total_rev)}",
        f"• Pedidos: {total_orders}",
        f"• Ticket medio: {brl(ticket)}",
    ]


def build_sales_by_channel(canonical: dict[str, dict]) -> list[str]:
    """Gera o bloco fixo de Vendas por Canal (igual para os 3 destinatários)."""
    lines = []
    for pk in PLATFORM_ORDER:
        row = canonical.get(pk, {})
        rev = float(row.get("total_revenue") or 0)
        orders = int(row.get("order_count") or 0)
        label = PLATFORM_LABELS[pk]
        lines.append(f"• {label}: {brl(rev)} | {orders} pedidos")
    return lines


def build_lucas_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Lucas — Shopee com diagnostico profundo."""
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
    sections.append("📊 *RESUMO GERAL*\n" + "\n".join(summary_lines))

    channel_lines = build_sales_by_channel(canonical)
    sections.append("🛒 *VENDAS POR CANAL*\n" + "\n".join(channel_lines))

    # Visao Shopee oficial
    shopee_row = canonical.get("shopee", {})
    shopee_rev = float(shopee_row.get("total_revenue") or 0)
    shopee_orders = int(shopee_row.get("order_count") or 0)
    shopee_ticket = shopee_rev / shopee_orders if shopee_orders else 0

    shopee_lines = []
    shopee_lines.append(f"• Faturamento oficial Shopee: {brl(shopee_rev)}")
    shopee_lines.append(f"• Pedidos Shopee: {shopee_orders}")
    shopee_lines.append(f"• Ticket medio Shopee: {brl(shopee_ticket)}")
    sections.append("🛒 *VISAO SHOPEE*\n" + "\n".join(shopee_lines))

    # Diagnostico profundo por conta
    account_slugs = [
        ("shopee-budamix-store", "Budamix Store"),
        ("shopee-budamix-oficial-2", "Budamix Oficial / Conta 2"),
        ("shopee-budamix-shop-3", "Budamix Shop / Conta 3"),
    ]
    diag_lines = []
    for slug, label in account_slugs:
        a = analyses.get(slug)
        if not a:
            diag_lines.append(f"\n• {label}: analise nao disponivel")
            continue

        diag_lines.append(f"\n• {label}: {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")

        # Leitura temporal completa
        diag_lines.extend(_temporal_reading(a["comparisons"], a["pedidos"], a["gmv"]))

        # Top produtos por nome
        if a["top_skus"]:
            top_name = display_name_from_sku(a["top_skus"][0][0])
            top_qty = a["top_skus"][0][1]
            diag_lines.append(f"  - Produto principal: {top_name} ({top_qty} un.)")

        # Concentracao com leitura
        if a["concentration_top3"] > 0:
            reading = _concentration_reading(a["concentration_top3"])
            diag_lines.append(f"  - Concentracao top 3: {pct(a['concentration_top3'])} ({reading})")

        # Cancelamentos
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if cancel_rate > 5:
            diag_lines.append(f"  - Taxa de cancelamento: {cancel_text} ({a['cancelamentos']} pedidos)")

        # Interpretacao e hipotese por conta
        c30 = a["comparisons"].get("30d")
        c60 = a["comparisons"].get("60d")
        csw = a["comparisons"].get("same_weekday")

        if slug == "shopee-budamix-store":
            # Budamix Store — conta principal, queda significativa
            if c30:
                var_o = float(c30["var_orders"].rstrip("%"))
                var_g = float(c30["var_gmv"].rstrip("%"))
                var_t = float(c30["var_ticket"].rstrip("%"))
                if var_o < -10:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Queda de {var_abs(c30['var_orders'])} em pedidos e "
                        f"{var_abs(c30['var_gmv'])} em GMV vs 30d, com ticket {c30['var_ticket']}. "
                        f"Isso sugere perda de tracao/exposicao, nao mudanca de mix. "
                        f"Como {pct(a['concentration_top3'])} das unidades estao em 3 produtos, "
                        f"qualquer queda nesses anuncios derruba a conta inteira."
                    )
                    diag_lines.append(
                        f"  - ACAO: Checar posicao/visibilidade dos anuncios de "
                        f"{display_name_from_sku(a['top_skus'][0][0])} e "
                        f"{display_name_from_sku(a['top_skus'][1][0]) if len(a['top_skus']) > 1 else 'segundo produto'}. "
                        f"Comparar trafego de ontem com media. Alinhar com Himmel se queda repetir hoje."
                    )
                elif abs(var_o) <= 10:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Conta principal dentro da faixa normal vs 30d. "
                        f"Monitorar tendencia nos proximos dias."
                    )

        elif slug == "shopee-budamix-oficial-2":
            # Conta 2 — pedidos acima de 30d mas GMV abaixo
            if c30:
                var_o = float(c30["var_orders"].rstrip("%"))
                var_g = float(c30["var_gmv"].rstrip("%"))
                var_t = float(c30["var_ticket"].rstrip("%"))
                if var_o > 0 and var_g < 0:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Pedidos {c30['var_orders']} vs 30d, mas GMV {c30['var_gmv']} e "
                        f"ticket {c30['var_ticket']}. Mais pedidos com ticket menor indica mudanca de mix "
                        f"para produtos de menor valor ou acao promocional. Verificar se houve alteracao de preco "
                        f"em {display_name_from_sku(a['top_skus'][0][0])}."
                    )
                elif var_o > 5:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Conta crescendo em volume ({c30['var_orders']} vs 30d). "
                        f"Manter momentum e monitorar ticket."
                    )
                elif var_o < -10:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Queda relevante de {var_abs(c30['var_orders'])} em pedidos. "
                        f"Verificar exposicao dos anuncios principais."
                    )
                else:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Operacao dentro dos parametros normais."
                    )

        elif slug == "shopee-budamix-shop-3":
            # Conta 3 — ticket alto, pedidos variáveis
            if c30:
                var_o = float(c30["var_orders"].rstrip("%"))
                var_g = float(c30["var_gmv"].rstrip("%"))
                var_t = float(c30["var_ticket"].rstrip("%"))
                if var_o < -5 and var_g >= -2:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Menos pedidos ({c30['var_orders']} vs 30d) mas GMV estavel "
                        f"({c30['var_gmv']}). Ticket subiu {c30['var_ticket']}, compensando volume. "
                        f"Conta sustentada por {display_name_from_sku(a['top_skus'][0][0])} com "
                        f"{a['top_skus'][0][1]} un. Se ticket cair sem recuperar volume, GMV despenca."
                    )
                elif var_o < -10:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Volume em queda significativa ({c30['var_orders']}). "
                        f"Verificar exposicao e concorrencia nos anuncios principais."
                    )
                else:
                    diag_lines.append(
                        f"  - INTERPRETACAO: Operacao estavel. Monitorar tendencia."
                    )

    sections.append("🔎 *DIAGNOSTICO POR CONTA*" + "\n".join(diag_lines))

    # Prioridades profundas
    prio_lines = []

    # Lucas — prioridades operacionais
    prio_lines.append("\n• Lucas (Operacional Shopee):")

    store_a = analyses.get("shopee-budamix-store")
    if store_a:
        c30 = store_a["comparisons"].get("30d")
        if c30 and float(c30["var_orders"].rstrip("%")) < -10:
            prio_lines.append(
                f"  - Checar posicao e visibilidade dos anuncios de "
                f"{display_name_from_sku(store_a['top_skus'][0][0])} e "
                f"{display_name_from_sku(store_a['top_skus'][1][0]) if len(store_a['top_skus']) > 1 else 'segundo produto'} "
                f"na Budamix Store, porque a conta caiu {var_abs(c30['var_orders'])} em pedidos com ticket estavel. "
                f"Se hoje ate 12h seguir abaixo da media horaria, escalar para Himmel revisar trafego/campanha."
            )
        cancel_rate, _ = _cancel_analysis(store_a["cancelamentos"], store_a["pedidos"])
        if cancel_rate > 7:
            prio_lines.append(
                f"  - Investigar cancelamentos na Budamix Store ({store_a['cancelamentos']} cancelados, "
                f"taxa {pct(cancel_rate)}): verificar se sao por ruptura de estoque, prazo ou reclamacao. "
                f"Se padrao se repetir, reportar ao Pedro."
            )

    conta2_a = analyses.get("shopee-budamix-oficial-2")
    if conta2_a:
        c30 = conta2_a["comparisons"].get("30d")
        if c30 and float(c30["var_ticket"].rstrip("%")) < -10:
            prio_lines.append(
                f"  - Conta 2: ticket caiu {var_abs(c30['var_ticket'])} vs 30d. "
                f"Verificar se houve alteracao de preco/cupom em "
                f"{display_name_from_sku(conta2_a['top_skus'][0][0])} ou mudanca de mix. "
                f"Se GMV continuar caindo com pedidos estaveis, o problema e precificacao."
            )

    conta3_a = analyses.get("shopee-budamix-shop-3")
    if conta3_a and conta3_a["concentration_top3"] > 75:
        prio_lines.append(
            f"  - Conta 3: mix muito concentrado ({pct(conta3_a['concentration_top3'])} em 3 produtos). "
            f"Avaliar se ha espaco para impulsionar anuncios secundarios e reduzir dependencia de "
            f"{display_name_from_sku(conta3_a['top_skus'][0][0])}."
        )

    # Se nenhuma prioridade especifica para Lucas
    if len(prio_lines) == 1:
        prio_lines.append("  - Operacao Shopee dentro dos parametros. Monitorar tendencias e confirmar expedição.")

    # Himmel — prioridades ADS
    prio_lines.append("\n• Himmel (ADS Shopee):")
    any_traffic_signal = False
    for slug, label in account_slugs:
        a = analyses.get(slug)
        if not a:
            continue
        c30 = a["comparisons"].get("30d")
        if c30 and float(c30["var_orders"].rstrip("%")) < -10:
            any_traffic_signal = True
            prio_lines.append(
                f"  - {label}: queda de {var_abs(c30['var_orders'])} em pedidos vs 30d com ticket "
                f"{c30['var_ticket']}. Verificar se campanhas/anuncios patrocinados perderam impressao ou "
                f"posicao. Checar se concorrente entrou com preco agressivo nos "
                f"{display_name_from_sku(a['top_skus'][0][0])}."
            )
    if not any_traffic_signal:
        prio_lines.append("  - Sem sinal critico de queda de trafego. Manter campanhas atuais e monitorar.")

    sections.append("🎯 *PRIORIDADES DO DIA*" + "\n".join(prio_lines))

    return "\n\n".join(sections)


def build_yasmin_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Yasmin — Mercado Livre com diagnostico profundo."""
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
    sections.append("📊 *RESUMO GERAL*\n" + "\n".join(summary_lines))

    channel_lines = build_sales_by_channel(canonical)
    sections.append("🛒 *VENDAS POR CANAL*\n" + "\n".join(channel_lines))

    # Visao ML oficial
    ml_row = canonical.get("ml", {})
    ml_rev = float(ml_row.get("total_revenue") or 0)
    ml_orders = int(ml_row.get("order_count") or 0)
    ml_ticket = ml_rev / ml_orders if ml_orders else 0

    ml_lines = []
    ml_lines.append(f"• Faturamento oficial Mercado Livre: {brl(ml_rev)}")
    ml_lines.append(f"• Pedidos Mercado Livre: {ml_orders}")
    ml_lines.append(f"• Ticket medio Mercado Livre: {brl(ml_ticket)}")
    sections.append("🛒 *VISAO MERCADO LIVRE*\n" + "\n".join(ml_lines))

    # Diagnostico profundo ML
    a = analyses.get("mercado-livre")
    diag_lines = []
    if a:
        # Metricas do dia (granular)
        diag_lines.append(f"• Dia granular: {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")

        # Leitura temporal completa
        diag_lines.extend(_temporal_reading(a["comparisons"], a["pedidos"], a["gmv"]))

        # Interpretacao cruzada 30d vs 60d
        c30 = a["comparisons"].get("30d")
        c60 = a["comparisons"].get("60d")
        csw = a["comparisons"].get("same_weekday")

        if c30 and c60:
            var30_o = float(c30["var_orders"].rstrip("%"))
            var60_o = float(c60["var_orders"].rstrip("%"))
            if var30_o < 0 and var60_o > 0:
                diag_lines.append(
                    f"• INTERPRETACAO: ML ficou {var_abs(c30['var_orders'])} abaixo da media 30d, "
                    f"mas {var_abs(c60['var_orders'])} acima da media 60d. Isso indica que o patamar recente "
                    f"(30d) estava mais alto — a queda de ontem pode ser flutuacao normal, nao tendencia. "
                    f"A leitura muda se repetir hoje."
                )
            elif var30_o < -15:
                diag_lines.append(
                    f"• INTERPRETACAO: Queda expressiva de {var_abs(c30['var_orders'])} vs 30d. "
                    f"Verificar se houve mudanca de exposicao ou concorrencia nos anuncios principais."
                )
            elif abs(var30_o) <= 10:
                diag_lines.append(
                    f"• INTERPRETACAO: Dia dentro da faixa normal vs 30d ({c30['var_orders']}). "
                    f"Sem anomalia detectada."
                )
            else:
                diag_lines.append(
                    f"• INTERPRETACAO: Dia {c30['var_orders']} vs 30d. Monitorar continuidade."
                )

        # Efeito dia da semana
        if csw:
            var_sw = float(csw["var_orders"].rstrip("%"))
            if abs(var_sw) > 8:
                direction = "abaixo" if var_sw < 0 else "acima"
                diag_lines.append(
                    f"• vs mesmo dia semana: {var_abs(csw['var_orders'])} {direction}. "
                    f"Verificar se e efeito calendario (feriado proximo, quinzena) ou sinal real."
                )

        # Top produtos por nome
        diag_lines.append("• Produtos que mais venderam:")
        diag_lines.extend(_top_products_text(a["top_skus"], 5))

        # Concentracao com interpretacao
        reading = _concentration_reading(a["concentration_top3"])
        diag_lines.append(f"• Concentracao top 3: {pct(a['concentration_top3'])} ({reading})")

        if a["concentration_top3"] < 55:
            diag_lines.append(
                "  - Distribuicao mais saudavel que Shopee. Risco de dependencia menor — "
                "varios produtos contribuem para o GMV."
            )

        # Cancelamentos
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if cancel_rate > 3:
            diag_lines.append(f"• Cancelamentos: {a['cancelamentos']} ({cancel_text})")
        elif a["cancelamentos"] > 0:
            diag_lines.append(f"• Cancelamentos: {a['cancelamentos']} (dentro do normal)")

    else:
        diag_lines.append("• Analise detalhada nao disponivel para o dia")

    sections.append("🔎 *DIAGNOSTICO MERCADO LIVRE*\n" + "\n".join(diag_lines))

    # Prioridades profundas
    prio_lines = []

    prio_lines.append("\n• Yasmin (Operacional ML):")
    if a:
        c30 = a["comparisons"].get("30d")
        csw = a["comparisons"].get("same_weekday")

        if c30 and float(c30["var_orders"].rstrip("%")) < -10:
            prio_lines.append(
                f"  - Verificar exposicao dos 3 anuncios principais ({display_name_from_sku(a['top_skus'][0][0])}, "
                f"{display_name_from_sku(a['top_skus'][1][0]) if len(a['top_skus']) > 1 else 'segundo produto'}, "
                f"{display_name_from_sku(a['top_skus'][2][0]) if len(a['top_skus']) > 2 else 'terceiro produto'}) "
                f"— pedidos cairam {var_abs(c30['var_orders'])} vs 30d. Se hoje ate 14h o ritmo seguir abaixo, "
                f"alinhar com Himmel sobre campanhas."
            )
        else:
            # Prioridade de manutencao
            if a["top_skus"]:
                prio_lines.append(
                    f"  - Manter sortimento e disponibilidade dos anuncios principais: "
                    f"{display_name_from_sku(a['top_skus'][0][0])}"
                    f"{', ' + display_name_from_sku(a['top_skus'][1][0]) if len(a['top_skus']) > 1 else ''}"
                    f"{', ' + display_name_from_sku(a['top_skus'][2][0]) if len(a['top_skus']) > 2 else ''}. "
                    f"Esses 3 sustentaram {pct(a['concentration_top3'])} do volume."
                )

            if csw and abs(float(csw["var_orders"].rstrip("%"))) > 8:
                prio_lines.append(
                    f"  - Queda de {var_abs(csw['var_orders'])} vs {weekday} anterior. "
                    f"Verificar se e apenas efeito de calendario (segunda pos-Dia das Maes, por ex.) "
                    f"ou se ha sinal de perda de tracao. Criterio: se terça tambem vier abaixo, investigar."
                )

        # Cancelamentos
        cancel_rate, _ = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if cancel_rate > 5:
            prio_lines.append(
                f"  - Cancelamentos acima do normal ({pct(cancel_rate)}). Verificar motivos: "
                f"ruptura de estoque, problema com envio, ou cliente desistiu. Se padrao persistir, escalar."
            )

    if len(prio_lines) == 1:
        prio_lines.append("  - Operacao ML dentro dos parametros. Manter acompanhamento padrao.")

    # Himmel
    prio_lines.append("\n• Himmel (ADS ML):")
    if a:
        c30 = a["comparisons"].get("30d")
        if c30 and float(c30["var_orders"].rstrip("%")) < -10:
            prio_lines.append(
                f"  - ML caiu {var_abs(c30['var_orders'])} em pedidos vs 30d. "
                f"Checar performance de campanhas, impressoes e posicao dos anuncios patrocinados. "
                f"Prioridade nos {display_name_from_sku(a['top_skus'][0][0])} que representam o maior volume."
            )
        else:
            prio_lines.append(
                "  - Sem sinal critico de queda. Manter campanhas atuais e monitorar tendencia semanal."
            )

    sections.append("🎯 *PRIORIDADES DO DIA*" + "\n".join(prio_lines))

    return "\n\n".join(sections)


def build_leonardo_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Leonardo — Amazon com diagnostico profundo."""
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
    sections.append("📊 *RESUMO GERAL*\n" + "\n".join(summary_lines))

    channel_lines = build_sales_by_channel(canonical)
    sections.append("🛒 *VENDAS POR CANAL*\n" + "\n".join(channel_lines))

    # Visao Amazon oficial
    amz_row = canonical.get("amazon", {})
    amz_rev = float(amz_row.get("total_revenue") or 0)
    amz_orders = int(amz_row.get("order_count") or 0)
    amz_ticket = amz_rev / amz_orders if amz_orders else 0

    amz_lines = []
    amz_lines.append(f"• Faturamento oficial Amazon: {brl(amz_rev)}")
    amz_lines.append(f"• Pedidos Amazon: {amz_orders}")
    amz_lines.append(f"• Ticket medio Amazon: {brl(amz_ticket)}")
    sections.append("🛒 *VISAO AMAZON*\n" + "\n".join(amz_lines))

    # Diagnostico profundo Amazon
    a = analyses.get("amazon")
    diag_lines = []
    if a:
        # Metricas granulares
        diag_lines.append(f"• Dia granular: {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")

        # Fulfillment detalhado
        if a["fulfillment"]:
            diag_lines.append(f"• Fulfillment: {a['fulfillment']}")
            if "32/32" in a["fulfillment"] or "FBA:" in a["fulfillment"]:
                diag_lines.append(
                    "  - 100% FBA: bom para Buy Box. Porem, se houver cancelamento, "
                    "pode ser ruptura no CD Amazon ou indisponibilidade temporaria."
                )

        # Leitura temporal completa
        diag_lines.extend(_temporal_reading(a["comparisons"], a["pedidos"], a["gmv"]))

        # Interpretacao temporal
        c30 = a["comparisons"].get("30d")
        c60 = a["comparisons"].get("60d")
        csw = a["comparisons"].get("same_weekday")

        if c30:
            var30_o = float(c30["var_orders"].rstrip("%"))
            var30_g = float(c30["var_gmv"].rstrip("%"))
            if var30_o > 10:
                diag_lines.append(
                    f"• INTERPRETACAO: Dia forte — {c30['var_orders']} acima da media 30d em pedidos "
                    f"e {c30['var_gmv']} em GMV. "
                )
                if c60:
                    var60_o = float(c60["var_orders"].rstrip("%"))
                    if var60_o > 15:
                        diag_lines[-1] += (
                            f"Tendencia confirmada tambem vs 60d ({c60['var_orders']}). "
                            f"Amazon em trajetoria ascendente."
                        )
                    else:
                        diag_lines[-1] += "Verificar se e pico pontual ou tendencia sustentada."
            elif var30_o < -10:
                diag_lines.append(
                    f"• INTERPRETACAO: Queda de {var_abs(c30['var_orders'])} vs 30d. "
                    f"Investigar Buy Box, exposicao e status FBA."
                )

        # Cancelamentos com profundidade
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if cancel_rate > 10:
            diag_lines.append(
                f"• ALERTA — Taxa de cancelamento: {cancel_text} ({a['cancelamentos']} de "
                f"{a['pedidos'] + a['cancelamentos']} pedidos totais)"
            )
            diag_lines.append(
                "  - Com 100% FBA, cancelamentos altos podem indicar: "
                "(a) ruptura de estoque no CD Amazon; "
                "(b) atraso FBA gerando cancelamento automatico; "
                "(c) indisponibilidade temporaria de listing; "
                "(d) pedido pendente que expirou. "
                "Leonardo deve verificar no Seller Central o motivo de cada cancelamento."
            )
        elif cancel_rate > 5:
            diag_lines.append(
                f"• Cancelamentos: {cancel_text} — acima do ideal mas nao critico. Monitorar."
            )

        # Top produtos por nome
        diag_lines.append("• Produtos que mais venderam:")
        diag_lines.extend(_top_products_text(a["top_skus"], 5))

        # Concentracao
        reading = _concentration_reading(a["concentration_top3"])
        diag_lines.append(f"• Concentracao top 3: {pct(a['concentration_top3'])} ({reading})")

    else:
        diag_lines.append("• Analise detalhada nao disponivel para o dia")

    sections.append("🔎 *DIAGNOSTICO AMAZON*\n" + "\n".join(diag_lines))

    # Prioridades profundas — separar operacional Leonardo vs ADS Pedro
    prio_lines = []

    prio_lines.append("\n• Leonardo (Operacional Amazon):")
    if a:
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])

        if cancel_rate > 10:
            prio_lines.append(
                f"  - URGENTE: Investigar os {a['cancelamentos']} cancelamentos no Seller Central. "
                f"Identificar se vieram de ruptura FBA, indisponibilidade de listing ou prazo expirado. "
                f"Se mais de 3 forem do mesmo produto, verificar estoque desse item no CD Amazon."
            )

        if a["fulfillment"] and "FBA" in a["fulfillment"]:
            prio_lines.append(
                f"  - Confirmar estoque FBA para os 3 principais produtos: "
                f"{display_name_from_sku(a['top_skus'][0][0])}"
                f"{', ' + display_name_from_sku(a['top_skus'][1][0]) if len(a['top_skus']) > 1 else ''}"
                f"{', ' + display_name_from_sku(a['top_skus'][2][0]) if len(a['top_skus']) > 2 else ''}. "
                f"Se algum estiver abaixo de 5 dias de cobertura, priorizar reposicao."
            )

        if a["concentration_top3"] > 70:
            prio_lines.append(
                f"  - Concentracao alta ({pct(a['concentration_top3'])}). Verificar se listings "
                f"secundarios ({display_name_from_sku(a['top_skus'][3][0]) if len(a['top_skus']) > 3 else 'demais produtos'}) "
                f"estao com Buy Box ativo e estoque disponivel."
            )

    if len(prio_lines) == 1:
        prio_lines.append("  - Operacao Amazon estavel. Confirmar expedicao FBA e monitorar Buy Box.")

    prio_lines.append("\n• Pedro (ADS Amazon):")
    if a:
        c30 = a["comparisons"].get("30d")
        cancel_rate, _ = _cancel_analysis(a["cancelamentos"], a["pedidos"])

        if c30 and float(c30["var_orders"].rstrip("%")) < -10:
            prio_lines.append(
                f"  - Volume caiu {var_abs(c30['var_orders'])} vs 30d. Revisar campanhas Sponsored Products "
                f"e verificar se ACOS subiu ou impressoes cairam. Foco em "
                f"{display_name_from_sku(a['top_skus'][0][0])}."
            )
        elif c30 and float(c30["var_orders"].rstrip("%")) > 10:
            prio_lines.append(
                f"  - Dia forte ({c30['var_orders']} vs 30d). Avaliar se campanhas atuais estao "
                f"contribuindo para o crescimento. Se sim, considerar escalar budget mantendo ACOS."
            )
        else:
            prio_lines.append(
                "  - Volume dentro da faixa normal. Manter campanhas atuais e monitorar ACOS."
            )

        if cancel_rate > 10:
            prio_lines.append(
                f"  - Cancelamentos altos ({pct(cancel_rate)}). Verificar se alguma campanha "
                f"esta direcionando trafego para listing sem estoque. Se confirmado, pausar anuncio."
            )

    sections.append("🎯 *PRIORIDADES DO DIA*" + "\n".join(prio_lines))

    return "\n\n".join(sections)


# ---------------------------------------------------------------------------
# Slack rich_text blocks
# ---------------------------------------------------------------------------

SECTION_TITLES = {
    "📊 RESUMO GERAL",
    "🛒 VENDAS POR CANAL",
    "🛒 VISAO SHOPEE",
    "🛒 VISAO MERCADO LIVRE",
    "🛒 VISAO AMAZON",
    "🔎 DIAGNOSTICO POR CONTA",
    "🔎 DIAGNOSTICO MERCADO LIVRE",
    "🔎 DIAGNOSTICO AMAZON",
    "🎯 PRIORIDADES DO DIA",
    "📦 PRODUTOS EM DESTAQUE",
}


def message_to_rich_text_blocks(text: str) -> list[dict]:
    elements: list[dict] = []
    lines = text.split("\n")
    for idx, line in enumerate(lines):
        raw = line.strip()
        # Check for emoji + *TITLE* pattern
        is_title = False
        title_text = raw
        if raw.startswith("*") and raw.endswith("*"):
            title_text = raw[1:-1]
        # Also check for "EMOJI *TITLE*" pattern
        emoji_title_match = re.match(r"^([\U0001F300-\U0001FAFF\u2600-\u27BF]+)\s*\*([^*]+)\*$", raw)
        if emoji_title_match:
            title_text = emoji_title_match.group(1) + " " + emoji_title_match.group(2)
            is_title = title_text in SECTION_TITLES
        elif title_text in SECTION_TITLES:
            is_title = True

        if is_title:
            elements.append(
                {"type": "text", "text": title_text, "style": {"bold": True, "underline": True}}
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
    parser = argparse.ArgumentParser(description="Daily Sales v2 — Slack Message Generator (Fase 4.1)")
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
    print(f"\n--- Daily Sales v2 — Slack Generator (Fase 4.1) ---")
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
    print(f"\nGerando mensagens individuais (Fase 4.1 — diagnostico profundo)...")
    messages = {
        "Lucas": build_lucas_message(canonical, day, analyses),
        "Yasmin": build_yasmin_message(canonical, day, analyses),
        "Leonardo": build_leonardo_message(canonical, day, analyses),
    }

    # 4. Validacoes QA
    print(f"\n--- QA ---")
    qa_passed = True
    for name, msg in messages.items():
        issues = []
        if "atacado" in msg.lower() or "bling" in msg.lower():
            issues.append("CONTEM ATACADO/BLING")
        if not msg.strip():
            issues.append("MENSAGEM VAZIA")
        for required_section in ["📊 *RESUMO GERAL*", "🛒 *VENDAS POR CANAL*"]:
            if required_section not in msg:
                issues.append(f"SECAO FIXA AUSENTE: {required_section}")

        # QA: SKU cru no texto visivel
        sku_violations = qa_check_raw_skus(msg)
        if sku_violations:
            issues.append(f"SKU CRU DETECTADO ({len(sku_violations)} ocorrencias)")
            for v in sku_violations[:3]:
                print(f"    ⚠ {v}")

        # QA: Titulos com emoji + uppercase
        has_emoji_titles = any(
            emoji in msg
            for emoji in ["📊", "🛒", "🔎", "🎯"]
        )
        if not has_emoji_titles:
            issues.append("FALTAM TITULOS COM EMOJI")

        status = "PASS" if not issues else "FAIL: " + ", ".join(issues)
        if issues:
            qa_passed = False
        print(f"  {name}: {status}")

    if not qa_passed:
        print("\n⚠ QA encontrou problemas. Verifique as mensagens.")

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
