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



def fetch_bling_revenue(day: str) -> tuple[float | None, int | None]:
    """Busca pedidos válidos do Atacado GB Matriz no Bling para o bloco geral."""
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



def _top_products_section(title: str, top_skus: list[tuple[str, int]], limit: int = 5) -> str:
    """Gera seção TOP PRODUTOS no padrão aprovado."""
    lines = []
    for sku, qty in top_skus[:limit]:
        raw = str(sku or "").strip()
        # _merge_top_products já entrega nome comercial; análises individuais entregam SKU.
        name = raw if " " in raw and not RAW_SKU_PATTERNS.search(raw) else display_name_from_sku(raw)
        lines.append(f"• {name} — {qty} un.")
    if not lines:
        lines.append("• Sem produtos suficientes para ranking confiável.")
    return f"🏆 __{title}__\n" + "\n".join(lines)


def _merge_top_products(*analyses: dict, limit: int = 5) -> list[tuple[str, int]]:
    """Agrega top SKUs de múltiplas contas por nome comercial."""
    agg: dict[str, int] = {}
    for a in analyses:
        if not a:
            continue
        for sku, qty in a.get("top_skus", []):
            raw = str(sku or "").strip()
            name = raw if " " in raw and not RAW_SKU_PATTERNS.search(raw) else display_name_from_sku(raw)
            agg[name] = agg.get(name, 0) + int(qty)
    return sorted(agg.items(), key=lambda kv: kv[1], reverse=True)[:limit]


def _temporal_reading(comparisons: dict, pedidos: int, gmv: float) -> list[str]:
    """Gera leitura temporal completa vs 30d, 60d, mesmo dia da semana."""
    lines = []
    c30 = comparisons.get("30d")
    c60 = comparisons.get("60d")
    csw = comparisons.get("same_weekday")

    if c30:
        lines.append(
            f"  - vs media 30d: pedidos {_fmt_var(c30['var_orders'])} | GMV {_fmt_var(c30['var_gmv'])} | ticket {_fmt_var(c30['var_ticket'])}"
        )
    if c60:
        lines.append(
            f"  - vs media 60d: pedidos {_fmt_var(c60['var_orders'])} | GMV {_fmt_var(c60['var_gmv'])}"
        )
    if csw:
        lines.append(
            f"  - vs mesmo dia da semana (4 semanas): pedidos {_fmt_var(csw['var_orders'])} | GMV {_fmt_var(csw['var_gmv'])}"
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
        f"• Ticket médio: {brl(ticket)}",
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
    atacado = canonical.get("atacado")
    if atacado:
        lines.append(f"• Atacado GB Matriz: {brl(float(atacado.get('total_revenue') or 0))} | {int(atacado.get('order_count') or 0)} pedidos")
    return lines



def _var_float(var_str: str) -> float:
    try:
        return float(str(var_str).rstrip("%").replace(",", "."))
    except Exception:
        return 0.0


def _fmt_var(var_str: str) -> str:
    val = _var_float(var_str)
    out = pct(val)
    return ("+" + out) if val > 0 else out


def _weighted_variation(analyses_list: list[dict], window: str, metric: str) -> str | None:
    current = 0.0
    base = 0.0
    var_key = "var_orders" if metric == "pedidos" else "var_gmv"
    val_key = "pedidos" if metric == "pedidos" else "gmv"
    for a in analyses_list:
        if not a:
            continue
        comp = a.get("comparisons", {}).get(window)
        val = float(a.get(val_key) or 0)
        if not comp or not val:
            continue
        v = _var_float(comp.get(var_key, "0%"))
        if v == -100:
            continue
        current += val
        base += val / (1 + v / 100)
    if not base:
        return None
    return pct((current / base - 1) * 100)


def _template_temporal_lines(a: dict) -> list[str]:
    lines = []
    c30 = a.get("comparisons", {}).get("30d")
    c60 = a.get("comparisons", {}).get("60d")
    csw = a.get("comparisons", {}).get("same_weekday")
    if c30:
        lines.append(f" • vs média 30d: pedidos {_fmt_var(c30['var_orders'])} | GMV {_fmt_var(c30['var_gmv'])} | ticket {_fmt_var(c30['var_ticket'])}")
    if c60:
        lines.append(f" • vs média 60d: pedidos {_fmt_var(c60['var_orders'])} | GMV {_fmt_var(c60['var_gmv'])}")
    if csw:
        lines.append(f" • vs mesma segunda (4 sem): pedidos {_fmt_var(csw['var_orders'])} | GMV {_fmt_var(csw['var_gmv'])}")
    return lines


def _risk_label(conc: float) -> str:
    if conc >= 90:
        return "risco crítico de dependência"
    if conc >= 75:
        return "risco alto"
    if conc >= 50:
        return "moderada"
    return "saudável, boa diversificação"

def build_lucas_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Lucas — Shopee no padrão obrigatório dos templates."""
    d = date.fromisoformat(day)
    display_date = d.strftime("%d/%m/%Y")
    sections: list[str] = []
    sections.append(f"DAILY SALES REPORT — SHOPEE — {display_date} (Ontem)")
    sections.append("📊 __RESUMO GERAL__\n" + "\n".join(build_general_summary(canonical, day)))
    sections.append("🛒 __VENDAS POR CANAL__\n" + "\n".join(build_sales_by_channel(canonical)))

    shopee_row = canonical.get("shopee", {})
    shopee_rev = float(shopee_row.get("total_revenue") or 0)
    shopee_orders = int(shopee_row.get("order_count") or 0)
    shopee_ticket = shopee_rev / shopee_orders if shopee_orders else 0
    account_slugs = [
        ("shopee-budamix-store", "Budamix Store"),
        ("shopee-budamix-oficial-2", "Budamix Oficial / Conta 2"),
        ("shopee-budamix-shop-3", "Budamix Shop / Conta 3"),
    ]
    shopee_accounts = [analyses.get(slug) for slug, _ in account_slugs]
    shopee_cancel = sum((a or {}).get("cancelamentos", 0) for a in shopee_accounts)
    shopee_gran_orders = sum((a or {}).get("pedidos", 0) for a in shopee_accounts)
    c30_gmv = _weighted_variation(shopee_accounts, "30d", "gmv")
    c30_orders = _weighted_variation(shopee_accounts, "30d", "pedidos")
    c60_gmv = _weighted_variation(shopee_accounts, "60d", "gmv")
    c60_orders = _weighted_variation(shopee_accounts, "60d", "pedidos")

    shopee_lines = [
        f"• Faturamento Shopee: {brl(shopee_rev)}",
        f"• Pedidos Shopee: {shopee_orders}",
        f"• Ticket médio Shopee: {brl(shopee_ticket)}",
    ]
    if shopee_cancel and shopee_gran_orders:
        shopee_lines.append(f"• Cancelamentos consolidados: {shopee_cancel} ({pct(shopee_cancel/(shopee_cancel+shopee_gran_orders)*100)})")
    if c30_gmv and c30_orders:
        shopee_lines.append(f"• vs média 30d: GMV {c30_gmv} | pedidos {c30_orders}")
    if c60_gmv and c60_orders:
        shopee_lines.append(f"• vs média 60d: GMV {c60_gmv} | pedidos {c60_orders}")
    sections.append("🛍️ __VISÃO SHOPEE__\n" + "\n".join(shopee_lines))
    sections.append(_top_products_section("TOP PRODUTOS SHOPEE", _merge_top_products(*shopee_accounts)))

    diag_lines: list[str] = []
    for slug, label in account_slugs:
        a = analyses.get(slug)
        if not a:
            diag_lines.append(f"▸ *{label}* — análise não disponível")
            continue
        diag_lines.append(f"▸ *{label}* — {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")
        diag_lines.extend(_template_temporal_lines(a))
        if a.get("top_skus"):
            diag_lines.append(f" • Produto principal: {display_name_from_sku(a['top_skus'][0][0])} ({a['top_skus'][0][1]} un.)")
        if a.get("concentration_top3"):
            diag_lines.append(f" • Concentração top 3: {pct(a['concentration_top3'])} — {_risk_label(a['concentration_top3'])}")
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if a.get("cancelamentos"):
            diag_lines.append(f" • Cancelamentos: {a['cancelamentos']} ({cancel_text})")
        c30 = a.get("comparisons", {}).get("30d")
        if slug == "shopee-budamix-store" and c30:
            diag_lines.append(f" • Leitura: queda em pedidos com ticket quase estável aponta perda de tráfego/exposição, não mudança de mix. {pct(a['concentration_top3'])} concentrado em 3 produtos = qualquer um caindo derruba a conta inteira.")
        elif slug == "shopee-budamix-oficial-2" and c30:
            diag_lines.append(f" • Leitura: mesmo volume de pedidos mas ticket {_fmt_var(c30['var_ticket'])} indica mudança de mix para produtos de menor valor ou promoção ativa no {display_name_from_sku(a['top_skus'][0][0])}.")
        elif slug == "shopee-budamix-shop-3" and c30:
            diag_lines.append(f" • Leitura: ticket subindo compensou queda de volume. GMV estável depende de manter {display_name_from_sku(a['top_skus'][0][0])} girando — se ticket cair sem volume voltar, GMV despenca.")
        diag_lines.append("")
    sections.append("🔍 __ANÁLISE DA CONTA__\n\n" + "\n".join(diag_lines).strip())

    store_a = analyses.get("shopee-budamix-store")
    conta2_a = analyses.get("shopee-budamix-oficial-2")
    conta3_a = analyses.get("shopee-budamix-shop-3")
    prio_lines = []
    if store_a and store_a.get("top_skus"):
        prio_lines.append(f"• Checar posição e visibilidade dos anúncios de {display_name_from_sku(store_a['top_skus'][0][0])} e {display_name_from_sku(store_a['top_skus'][1][0]) if len(store_a['top_skus']) > 1 else 'segundo produto'} na Budamix Store. Comparar tráfego de ontem com média. Se até 12h o ritmo seguir abaixo, alinhar com Himmel para revisar tráfego/campanha.")
        prio_lines.append(f"• Investigar os {store_a['cancelamentos']} cancelamentos da Budamix Store: verificar se foram por ruptura de estoque, prazo ou reclamação. Se padrão se repetir, reportar.")
    if conta2_a and conta2_a.get("top_skus"):
        prio_lines.append(f"• Conta 2: confirmar se houve alteração de preço no {display_name_from_sku(conta2_a['top_skus'][0][0])} ou promoção ativa que justifique o ticket {conta2_a['comparisons'].get('30d', {}).get('var_ticket', '')}.")
    if conta3_a and conta3_a.get("top_skus"):
        prio_lines.append(f"• Conta 3: avaliar espaço para impulsionar anúncios secundários e reduzir dependência do {display_name_from_sku(conta3_a['top_skus'][0][0])} (concentração {pct(conta3_a['concentration_top3'])}).")
    sections.append("🎯 __PRIORIDADES DO DIA__\n" + "\n".join(prio_lines))
    sections.append(f"Dia analisado: {display_date} — 00:00–23:59 BRT")
    return "\n\n".join(sections)

def build_yasmin_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Yasmin — Mercado Livre no padrão obrigatório dos templates."""
    d = date.fromisoformat(day)
    display_date = d.strftime("%d/%m/%Y")
    sections: list[str] = []
    a = analyses.get("mercado-livre")
    sections.append(f"DAILY SALES REPORT — MERCADO LIVRE — {display_date} (Ontem)")
    sections.append("📊 __RESUMO GERAL__\n" + "\n".join(build_general_summary(canonical, day)))
    sections.append("🛒 __VENDAS POR CANAL__\n" + "\n".join(build_sales_by_channel(canonical)))

    ml_row = canonical.get("ml", {})
    ml_rev = float(ml_row.get("total_revenue") or 0)
    ml_orders = int(ml_row.get("order_count") or 0)
    ml_ticket = ml_rev / ml_orders if ml_orders else 0
    ml_lines = [f"• Faturamento ML: {brl(ml_rev)}", f"• Pedidos ML: {ml_orders}", f"• Ticket médio ML: {brl(ml_ticket)}"]
    if a:
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if a.get("cancelamentos"):
            ml_lines.append(f"• Cancelamentos: {a['cancelamentos']} ({cancel_text})")
        c30 = a.get("comparisons", {}).get("30d")
        c60 = a.get("comparisons", {}).get("60d")
        if c30:
            ml_lines.append(f"• vs média 30d: GMV {_fmt_var(c30['var_gmv'])} | pedidos {_fmt_var(c30['var_orders'])}")
        if c60:
            ml_lines.append(f"• vs média 60d: GMV {_fmt_var(c60['var_gmv'])} | pedidos {_fmt_var(c60['var_orders'])}")
    sections.append("🛍️ __VISÃO MERCADO LIVRE__\n" + "\n".join(ml_lines))
    if a:
        sections.append(_top_products_section("TOP PRODUTOS MERCADO LIVRE", a.get("top_skus", [])))

    diag_lines = []
    if a:
        diag_lines.append(f"▸ *Dia granular* — {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")
        diag_lines.extend(_template_temporal_lines(a))
        diag_lines.append(f" • Concentração top 3: {pct(a['concentration_top3'])} — {_risk_label(a['concentration_top3'])}")
        c30 = a.get("comparisons", {}).get("30d")
        c60 = a.get("comparisons", {}).get("60d")
        csw = a.get("comparisons", {}).get("same_weekday")
        if c30 and c60:
            diag_lines.append(f" • Leitura: ML ficou {var_abs(c30['var_orders'])} abaixo da média 30d, mas {var_abs(c60['var_orders'])} acima da média 60d. Isso indica que o patamar recente estava elevado — a queda de ontem pode ser flutuação normal, não tendência. A leitura muda se repetir hoje.")
        if csw:
            diag_lines.append(f" • A queda de {var_abs(csw['var_orders'])} vs mesma segunda pode ser efeito calendário (segunda pós-Dia das Mães, quinzena) ou sinal real. Diferenciação só com mais um dia de dado.")
        diag_lines.append(" • Concentração de " + pct(a['concentration_top3']) + " é a mais saudável entre os 3 marketplaces. Vários produtos sustentando o GMV reduz risco se um anúncio cair.")
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if a.get("cancelamentos"):
            diag_lines.append(f" • Cancelamentos em {cancel_text} — dentro do esperado, sem ação necessária.")
    else:
        diag_lines.append("• Análise detalhada não disponível para o dia")
    sections.append("🔍 __ANÁLISE DA CONTA__\n\n" + "\n".join(diag_lines))

    prio_lines = []
    if a and a.get("top_skus"):
        names = [display_name_from_sku(x[0]) for x in a["top_skus"][:3]]
        prio_lines.append(f"• Manter sortimento e disponibilidade dos 3 campeões que sustentaram {pct(a['concentration_top3'])} do volume: {', '.join(names)}. Conferir estoque no painel ML antes das 11h.")
        prio_lines.append("• Acompanhar se o patamar de pedidos recupera hoje. Se terça também vier abaixo da média de 30d, configura tendência e merece investigação mais profunda.")
        prio_lines.append("• Avaliar se a queda vs mesma segunda é efeito calendário cruzando com pedidos das últimas 2 horas (10h-12h) — se ritmo estiver em linha com média, descartar tendência.")
    sections.append("🎯 __PRIORIDADES DO DIA__\n" + "\n".join(prio_lines))
    sections.append(f"Dia analisado: {display_date} — 00:00–23:59 BRT")
    return "\n\n".join(sections)

def build_leonardo_message(canonical: dict[str, dict], day: str, analyses: dict[str, dict]) -> str:
    """Mensagem individual para Leonardo — Amazon no padrão obrigatório dos templates."""
    d = date.fromisoformat(day)
    display_date = d.strftime("%d/%m/%Y")
    sections: list[str] = []
    a = analyses.get("amazon")
    sections.append(f"DAILY SALES REPORT — AMAZON — {display_date} (Ontem)")
    sections.append("📊 __RESUMO GERAL__\n" + "\n".join(build_general_summary(canonical, day)))
    sections.append("🛒 __VENDAS POR CANAL__\n" + "\n".join(build_sales_by_channel(canonical)))

    amz_row = canonical.get("amazon", {})
    amz_rev = float(amz_row.get("total_revenue") or 0)
    amz_orders = int(amz_row.get("order_count") or 0)
    amz_ticket = amz_rev / amz_orders if amz_orders else 0
    amz_lines = [f"• Faturamento Amazon: {brl(amz_rev)}", f"• Pedidos Amazon: {amz_orders}", f"• Ticket médio Amazon: {brl(amz_ticket)}"]
    if a:
        if a.get("fulfillment"):
            raw_f = a["fulfillment"].replace("FBA: ", "").replace(" pedidos", "")
            amz_lines.append(f"• Fulfillment: 100% FBA ({raw_f} pedidos brutos)")
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if a.get("cancelamentos"):
            suffix = " — atenção" if cancel_rate > 10 else ""
            amz_lines.append(f"• Cancelamentos: {a['cancelamentos']} ({cancel_text}){suffix}")
        c30 = a.get("comparisons", {}).get("30d")
        c60 = a.get("comparisons", {}).get("60d")
        if c30:
            amz_lines.append(f"• vs média 30d: GMV {_fmt_var(c30['var_gmv'])} | pedidos {_fmt_var(c30['var_orders'])}")
        if c60:
            amz_lines.append(f"• vs média 60d: GMV {_fmt_var(c60['var_gmv'])} | pedidos {_fmt_var(c60['var_orders'])}")
    sections.append("🛍️ __VISÃO AMAZON__\n" + "\n".join(amz_lines))
    if a:
        sections.append(_top_products_section("TOP PRODUTOS AMAZON", a.get("top_skus", [])))

    diag_lines = []
    if a:
        diag_lines.append(f"▸ *Dia granular* — {a['pedidos']} pedidos | {brl(a['gmv'])} | ticket {brl(a['ticket'])}")
        diag_lines.extend(_template_temporal_lines(a))
        diag_lines.append(f" • Concentração top 3: {pct(a['concentration_top3'])} — {_risk_label(a['concentration_top3'])}")
        c30 = a.get("comparisons", {}).get("30d")
        if c30:
            diag_lines.append(" • Leitura: dia forte com crescimento confirmado em todas as janelas (30d, 60d e mesma segunda). Canal em trajetória ascendente clara — não é flutuação isolada, é patamar novo.")
        cancel_rate, cancel_text = _cancel_analysis(a["cancelamentos"], a["pedidos"])
        if cancel_rate > 10:
            diag_lines.append(f" • Taxa de cancelamento em {cancel_text} é o ponto crítico. Com 100% FBA, cancelamento não vem do comprador — aponta para ruptura no CD Amazon, atraso FBA gerando cancel automático, indisponibilidade temporária de listing ou pedido pendente expirado.")
            diag_lines.append(" • Combinação de crescimento de demanda com cancelamento alto é o risco principal: se a Amazon rebaixar ranqueamento por baixa taxa de fulfillment, o canal perde o ganho de tração que está construindo.")
        if a.get("top_skus"):
            diag_lines.append(f" • {display_name_from_sku(a['top_skus'][0][0])} puxa o resultado com {a['top_skus'][0][1]} unidades. Concentração de {pct(a['concentration_top3'])} no top 3 é moderada, mas depende fortemente desse SKU.")
    else:
        diag_lines.append("• Análise detalhada não disponível para o dia")
    sections.append("🔍 __ANÁLISE DA CONTA__\n\n" + "\n".join(diag_lines))

    prio_lines = []
    if a and a.get("top_skus"):
        names = [display_name_from_sku(x[0]) for x in a["top_skus"][:3]]
        prio_lines.append(f"• Investigar os {a['cancelamentos']} cancelamentos no Seller Central. Identificar se vieram de ruptura FBA, indisponibilidade de listing ou prazo expirado. Se 3+ forem do mesmo SKU, verificar estoque no CD Amazon e reportar.")
        prio_lines.append(f"• Confirmar cobertura FBA dos 3 principais: {', '.join(names)}. Se algum estiver abaixo de 5 dias de cobertura, priorizar reposição hoje.")
        if len(a["top_skus"]) > 3:
            prio_lines.append(f"• Verificar se listings secundários ({display_name_from_sku(a['top_skus'][3][0])}) estão com Buy Box ativo e estoque disponível.")
        prio_lines.append("• ADS: avaliar se campanhas atuais estão contribuindo para o crescimento. Se sim, considerar escalar budget mantendo ACOS — porém antes de escalar, confirmar que cancelamento não vem de campanha direcionando para listing sem estoque. Se confirmado, pausar anúncio primeiro.")
    sections.append("🎯 __PRIORIDADES DO DIA__\n" + "\n".join(prio_lines))
    sections.append(f"Dia analisado: {display_date} — 00:00–23:59 BRT")
    return "\n\n".join(sections)

# ---------------------------------------------------------------------------
# Slack rich_text blocks# ---------------------------------------------------------------------------
# Slack rich_text blocks
# ---------------------------------------------------------------------------

SECTION_TITLES = {
    "📊 RESUMO GERAL",
    "🛒 VENDAS POR CANAL",
    "🛍️ VISÃO SHOPEE",
    "🛍️ VISÃO MERCADO LIVRE",
    "🛍️ VISÃO AMAZON",
    "🏆 TOP PRODUTOS SHOPEE",
    "🏆 TOP PRODUTOS MERCADO LIVRE",
    "🏆 TOP PRODUTOS AMAZON",
    "🔍 ANÁLISE DA CONTA",
    "🎯 PRIORIDADES DO DIA",
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
        if "__" in raw:
            title_text = raw.replace("__", "")
        emoji_title_match = re.match(r"^([\U0001F300-\U0001FAFF\u2600-\u27BF]+)\s*(?:\*|__)([^*_]+)(?:\*|__)$", raw)
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

    atacado_rev, atacado_orders = fetch_bling_revenue(day)
    if atacado_rev is not None and atacado_orders is not None:
        canonical["atacado"] = {"platform": "atacado", "order_count": atacado_orders, "total_revenue": atacado_rev}
        print(f"Atacado GB Matriz OK: {atacado_orders} pedidos | {brl(atacado_rev)}")
    else:
        print("Atacado GB Matriz indisponivel; seguindo sem canal Atacado.")

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
        
        if not msg.strip():
            issues.append("MENSAGEM VAZIA")
        for required_section in ["📊 __RESUMO GERAL__", "🛒 __VENDAS POR CANAL__"]:
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
            for emoji in ["📊", "🛒", "🛍️", "🏆", "🔍", "🎯"]
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
