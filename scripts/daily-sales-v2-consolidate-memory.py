#!/usr/bin/env python3
"""Daily Sales Report v2 — consolidação semanal/mensal da memória do Trader.

Fase 6A: gera consolidações em dry-run/preview a partir das análises diárias.
Fase 6B: o mesmo script pode atualizar weekly.md/monthly.md com --write.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
BASE = WORKSPACE / "shared" / "trader" / "memory" / "projects" / "daily-sales-report"
ACCOUNTS_DIR = BASE / "accounts"
REPORTS_DIR = WORKSPACE / "reports" / "daily-sales-report-v2" / "phase6"


SKU_SUFFIX_RE = re.compile(r"(_T|_BB|_B2|_B|_BAP)$", re.I)
DISPLAY_NAMES = {
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
    "XCP002": "Xícara Porcelana com Pires",
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

def display_name(raw_sku: str) -> str:
    sku = (raw_sku or "").strip().upper()
    if sku in DISPLAY_NAMES:
        return DISPLAY_NAMES[sku]
    canon = SKU_SUFFIX_RE.sub("", sku)
    if canon in DISPLAY_NAMES:
        return DISPLAY_NAMES[canon]
    if "IMB501T-CINZA" in sku:
        return "Conjunto 5 Potes de Vidro Redondos Tampa Cinza"
    if "IMB501T-PRETO" in sku:
        return "Conjunto 5 Potes de Vidro Redondos Tampa Preta"
    return raw_sku

ACCOUNT_LABELS = {
    "shopee-budamix-store": "Shopee — Budamix Store",
    "shopee-budamix-oficial-2": "Shopee — Budamix Oficial / Conta 2",
    "shopee-budamix-shop-3": "Shopee — Budamix Shop / Conta 3",
    "mercado-livre": "Mercado Livre",
    "amazon": "Amazon",
}


@dataclass
class DailyAnalysis:
    account: str
    path: Path
    day: date
    weekday: str
    orders: int
    cancellations: int
    gmv: float
    ticket: float
    items: int
    top_skus: list[tuple[str, int]]
    concentration_top3: float | None
    comparisons: dict[str, dict[str, str]]
    hypotheses: list[str]
    risks: list[str]
    actions: list[str]
    watch: list[str]


def brl(v: float) -> str:
    return "R$ " + f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(v: float) -> str:
    return f"{v:.1f}%".replace(".", ",")


def parse_money(s: str) -> float:
    return float(s.replace("R$", "").replace(",", "").strip())


def parse_day(md: str, path: Path, account: str) -> DailyAnalysis:
    m = re.search(r"\*\*Data:\*\* (\d{4}-\d{2}-\d{2}) \(([^)]+)\)", md)
    if not m:
        raise ValueError(f"Data não encontrada em {path}")
    day = date.fromisoformat(m.group(1))
    weekday = m.group(2)

    def metric_int(label: str) -> int:
        mm = re.search(rf"\| {re.escape(label)} \| ([\d,.]+) \|", md)
        return int(float(mm.group(1).replace(",", ""))) if mm else 0

    def metric_money(label: str) -> float:
        mm = re.search(rf"\| {re.escape(label)} \| R\$ ([\d,.]+) \|", md)
        return parse_money(mm.group(1)) if mm else 0.0

    orders = metric_int("Pedidos válidos")
    cancellations = metric_int("Cancelamentos")
    gmv = metric_money("Faturamento/GMV")
    ticket = metric_money("Ticket médio")
    items = metric_int("Itens vendidos")

    top_skus: list[tuple[str, int]] = []
    for mm in re.finditer(r"\| \d+ \| ([^|]+) \| (\d+) \|", md):
        top_skus.append((mm.group(1).strip(), int(mm.group(2))))

    conc = None
    mm = re.search(r"Concentração top 3:\*\* ([\d.,]+)%", md)
    if mm:
        conc = float(mm.group(1).replace(",", "."))

    comparisons: dict[str, dict[str, str]] = {}
    for mm in re.finditer(
        r"\| (30 dias|60 dias|Mesmo dia semana \(4x\)) \| ([\d.]+) \| R\$ ([\d,.]+) \| R\$ ([\d,.]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|",
        md,
    ):
        key = "30d" if mm.group(1) == "30 dias" else ("60d" if mm.group(1) == "60 dias" else "same_weekday")
        comparisons[key] = {
            "orders_avg": mm.group(2).strip(),
            "gmv_avg": mm.group(3).strip(),
            "ticket_avg": mm.group(4).strip(),
            "var_orders": mm.group(5).strip(),
            "var_gmv": mm.group(6).strip(),
            "var_ticket": mm.group(7).strip(),
        }

    def collect(section: str) -> list[str]:
        out: list[str] = []
        in_sec = False
        for line in md.splitlines():
            if line.strip() == f"## {section}":
                in_sec = True
                continue
            if in_sec and line.startswith("## "):
                break
            if in_sec and line.strip().startswith("- "):
                out.append(line.strip()[2:])
        return out

    return DailyAnalysis(
        account=account,
        path=path,
        day=day,
        weekday=weekday,
        orders=orders,
        cancellations=cancellations,
        gmv=gmv,
        ticket=ticket,
        items=items,
        top_skus=top_skus,
        concentration_top3=conc,
        comparisons=comparisons,
        hypotheses=collect("Hipóteses e Insights"),
        risks=collect("Riscos"),
        actions=collect("Ação Recomendada"),
        watch=collect("O Que Observar Amanhã"),
    )


def load_daily(account: str, until: date, days: int) -> list[DailyAnalysis]:
    daily_dir = ACCOUNTS_DIR / account / "daily"
    if not daily_dir.exists():
        return []
    start = until - timedelta(days=days - 1)
    rows: list[DailyAnalysis] = []
    for path in sorted(daily_dir.glob("*.md")):
        try:
            d = date.fromisoformat(path.stem)
        except ValueError:
            continue
        if start <= d <= until:
            rows.append(parse_day(path.read_text(encoding="utf-8"), path, account))
    return rows


def summarize_week(account: str, rows: list[DailyAnalysis], until: date) -> str:
    label = ACCOUNT_LABELS.get(account, account)
    start = until - timedelta(days=6)
    if not rows:
        return f"# Consolidação Semanal — {label} — {start} a {until}\n\n_Nenhuma análise diária disponível para o período._\n"
    total_orders = sum(r.orders for r in rows)
    total_gmv = sum(r.gmv for r in rows)
    total_cancels = sum(r.cancellations for r in rows)
    ticket = total_gmv / total_orders if total_orders else 0
    sku_counter: Counter[str] = Counter()
    risks = Counter()
    hypotheses = Counter()
    watch = []
    for r in rows:
        for sku, qty in r.top_skus[:5]:
            sku_counter[display_name(sku)] += qty
        risks.update(r.risks)
        hypotheses.update(r.hypotheses)
        watch.extend(r.watch)
    conc_values = [r.concentration_top3 for r in rows if r.concentration_top3 is not None]
    avg_conc = sum(conc_values) / len(conc_values) if conc_values else None
    best_day = max(rows, key=lambda r: r.gmv)
    weak_day = min(rows, key=lambda r: r.gmv)
    cancel_rate = total_cancels / (total_orders + total_cancels) * 100 if (total_orders + total_cancels) else 0

    lines = [
        f"# Consolidação Semanal — {label} — Semana até {until}",
        "",
        "## Metadados",
        f"- **Semana analisada:** {start} a {until}",
        f"- **Conta:** {label}",
        f"- **Dias analisados:** {len(rows)} de 7 ({', '.join(r.day.isoformat() for r in rows)})",
        "",
        "## Leitura da Semana",
        f"- A conta somou {total_orders} pedidos e {brl(total_gmv)} em GMV granular nos dias disponíveis, com ticket médio de {brl(ticket)}.",
        f"- Melhor dia granular: {best_day.day.isoformat()} ({best_day.weekday}) com {brl(best_day.gmv)}; dia mais fraco: {weak_day.day.isoformat()} ({weak_day.weekday}) com {brl(weak_day.gmv)}.",
        f"- Cancelamentos no período: {total_cancels} ({pct(cancel_rate)}).",
    ]
    if avg_conc is not None:
        lines.append(f"- Concentração média do top 3: {pct(avg_conc)}; usar como sinal de dependência de mix nas próximas leituras.")

    lines += ["", "## Produtos em Observação"]
    if sku_counter:
        for sku, qty in sku_counter.most_common(8):
            lines.append(f"- {sku}: {qty} un. acumuladas nos rankings diários.")
    else:
        lines.append("- Sem dados suficientes de SKU.")

    lines += ["", "## Padrões e Riscos Recorrentes"]
    if risks or hypotheses:
        for text, count in (risks + hypotheses).most_common(8):
            lines.append(f"- ({count}x) {text}")
    else:
        lines.append("- Nenhum padrão recorrente suficiente ainda; manter observação.")

    lines += ["", "## O que Carregar para Próxima Semana"]
    if watch:
        for item, count in Counter(watch).most_common(6):
            lines.append(f"- ({count}x) {item}")
    else:
        lines.append("- Continuar acumulando análises diárias até formar padrões semanais robustos.")
    lines.append("")
    return "\n".join(lines)


def summarize_month(account: str, rows: list[DailyAnalysis], until: date) -> str:
    label = ACCOUNT_LABELS.get(account, account)
    month = until.strftime("%Y-%m")
    if not rows:
        return f"# Tese Mensal — {label} — {month}\n\n_Nenhuma análise diária disponível para o período._\n"
    total_orders = sum(r.orders for r in rows)
    total_gmv = sum(r.gmv for r in rows)
    total_cancels = sum(r.cancellations for r in rows)
    ticket = total_gmv / total_orders if total_orders else 0
    cancel_rate = total_cancels / (total_orders + total_cancels) * 100 if (total_orders + total_cancels) else 0
    sku_counter: Counter[str] = Counter()
    for r in rows:
        for sku, qty in r.top_skus[:5]:
            sku_counter[display_name(sku)] += qty
    trend = "em observação" if len(rows) < 7 else "a consolidar"

    lines = [
        f"# Tese Mensal — {label} — {month}",
        "",
        "## Metadados",
        f"- **Mês:** {month}",
        f"- **Conta:** {label}",
        f"- **Dias analisados:** {len(rows)}",
        "",
        "## Tese Atual da Conta",
        f"Com {len(rows)} dia(s) analisado(s), a tese mensal ainda está em formação. O acumulado granular disponível mostra {total_orders} pedidos, {brl(total_gmv)} de GMV e ticket médio de {brl(ticket)}.",
        "A prioridade do ciclo mensal é separar sinais pontuais de padrões recorrentes, usando as consolidações semanais como filtro antes de promover regras permanentes.",
        "",
        "## Saúde da Conta",
        f"- **Tendência geral:** {trend}",
        f"- **GMV analisado:** {brl(total_gmv)}",
        f"- **Pedidos analisados:** {total_orders}",
        f"- **Ticket médio:** {brl(ticket)}",
        f"- **Cancelamentos:** {pct(cancel_rate)}",
        "",
        "## Dependências e Riscos",
    ]
    if sku_counter:
        top = sku_counter.most_common(3)
        lines.append("- Principais produtos a monitorar no mês: " + "; ".join(f"{sku} ({qty} un.)" for sku, qty in top) + ".")
    else:
        lines.append("- Ainda sem volume suficiente de SKU para tese de dependência.")
    lines += [
        "",
        "## Hipóteses Estratégicas para Próximo Mês",
        "- Manter acúmulo diário e promover para regra permanente apenas padrões repetidos em múltiplas semanas.",
        "- Usar semanal.md como camada intermediária para evitar overfitting em um único dia forte/fraco.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Consolida memória semanal/mensal do Daily Sales Report v2")
    parser.add_argument("--until", default=None, help="Data final YYYY-MM-DD. Se omitido em monthly no dia 1, usa ontem para fechar o mês anterior.")
    parser.add_argument("--period", choices=["weekly", "monthly", "all"], default="all")
    parser.add_argument("--accounts", default="all", help="Lista separada por vírgula ou all")
    parser.add_argument("--write", action="store_true", help="Atualiza weekly.md/monthly.md; sem isso salva apenas preview")
    args = parser.parse_args()

    today = date.today()
    if args.until:
        until = date.fromisoformat(args.until)
    elif args.period == "monthly" and today.day == 1:
        until = today - timedelta(days=1)
    else:
        until = today
    accounts = list(ACCOUNT_LABELS) if args.accounts == "all" else [a.strip() for a in args.accounts.split(",") if a.strip()]
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    for account in accounts:
        if account not in ACCOUNT_LABELS:
            raise SystemExit(f"Conta desconhecida: {account}")
        account_dir = ACCOUNTS_DIR / account
        weekly_text = summarize_week(account, load_daily(account, until, 7), until)
        monthly_text = summarize_month(account, load_daily(account, until, 30), until)

        if args.period in ("weekly", "all"):
            target = account_dir / "weekly.md" if args.write else REPORTS_DIR / f"preview-weekly-{account}-{until}.md"
            target.write_text(weekly_text, encoding="utf-8")
            print(f"weekly OK: {account} -> {target.relative_to(WORKSPACE)}")
        if args.period in ("monthly", "all"):
            target = account_dir / "monthly.md" if args.write else REPORTS_DIR / f"preview-monthly-{account}-{until.strftime('%Y-%m')}.md"
            target.write_text(monthly_text, encoding="utf-8")
            print(f"monthly OK: {account} -> {target.relative_to(WORKSPACE)}")

    print("CONSOLIDATION_OK" if args.write else "CONSOLIDATION_DRY_RUN_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
