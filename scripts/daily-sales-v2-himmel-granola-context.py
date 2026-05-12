#!/usr/bin/env python3
"""Daily Sales Report v2 — Fase 7: contexto Himmel/Granola.

- Opcionalmente roda scripts/granola-sync.py para trazer resumos Granola.
- Lê o contexto global `himmel-context.md`.
- Classifica entradas relevantes por conta/plataforma.
- Gera um `himmel-context.md` enxuto em cada conta para ser carregado pelo analyzer.

Nunca copia transcrição integral. Usa apenas resumo/contexto já persistido.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
BASE = WORKSPACE / "openclaw" / "agents" / "kobe" / "shared" / "trader" / "memory" / "projects" / "daily-sales-report"
ACCOUNTS_DIR = BASE / "accounts"
GLOBAL_HIMMEL = BASE / "himmel-context.md"
REPORTS_DIR = WORKSPACE / "reports" / "daily-sales-report-v2" / "phase7"
GRANOLA_SYNC = WORKSPACE / "scripts" / "granola-sync.py"

ACCOUNT_LABELS = {
    "shopee-budamix-store": "Shopee — Budamix Store",
    "shopee-budamix-oficial-2": "Shopee — Budamix Oficial / Conta 2",
    "shopee-budamix-shop-3": "Shopee — Budamix Shop / Conta 3",
    "mercado-livre": "Mercado Livre",
}

ACCOUNT_KEYWORDS = {
    "shopee-budamix-store": ["budamix store", "shopee", "448649947", "loja 1", "store"],
    "shopee-budamix-oficial-2": ["budamix oficial", "conta 2", "860803675", "shopee"],
    "shopee-budamix-shop-3": ["budamix shop", "conta 3", "442066454", "shopee"],
    "mercado-livre": ["mercado livre", "meli", "ml ads", "product ads", "yasmin"],
}

ADS_TERMS = [
    "himmel", "ads", "campanha", "campanhas", "budget", "verba", "roas", "acos", "tacos",
    "bid", "lance", "exposição", "exposicao", "tráfego", "trafego", "afiliado", "cupom", "cupons",
]


@dataclass
class Entry:
    title: str
    body: str
    date: str


def split_entries(text: str) -> list[Entry]:
    parts = re.split(r"\n---\n", text)
    entries: list[Entry] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Account files should receive concrete meeting/context entries, not the
        # static global operating rules at the top of himmel-context.md.
        title_match = re.search(r"^## \[([^\]]+)\] (.+)$", part, re.M)
        if not title_match:
            continue
        date = title_match.group(1).strip()
        title = title_match.group(2).strip()
        entries.append(Entry(title=title, body=part, date=date))
    return entries


def classify(entry: Entry) -> set[str]:
    blob = f"{entry.title}\n{entry.body}".lower()
    matched: set[str] = set()
    is_ads = any(term in blob for term in ADS_TERMS)
    if not is_ads:
        return matched

    # Regra Pedro 2026-05-12: reuniões Shopee/Himmel costumam ser consolidadas.
    # Quando uma nota fala de Shopee, considerar as 3 contas abordadas por padrão.
    # O relatório de cada conta deve usar esse contexto global e separar particularidades
    # explicitamente citadas ou hipóteses específicas cruzando com dados reais.
    if "shopee" in blob:
        matched.update(a for a in ACCOUNT_LABELS if a.startswith("shopee-"))

    for account, keys in ACCOUNT_KEYWORDS.items():
        if any(k in blob for k in keys):
            matched.add(account)

    # Contexto Himmel sem plataforma explícita vale para Shopee + ML, exceto Amazon.
    if "himmel" in blob and not matched:
        matched.update(ACCOUNT_LABELS)
    return matched



def account_interpretation(account: str, entry: Entry) -> list[str]:
    """Extrai pontos operacionais cabíveis para a conta, sem depender de transcrição integral."""
    blob = f"{entry.title}\n{entry.body}".lower()
    points: list[str] = []

    if account == "shopee-budamix-store":
        if "queda de 11%" in blob or "budamix store principal" in blob:
            points.append("Budamix Store principal teve queda citada de 11% em abril, mas com leitura positiva de eficiência: faturamento relevante com investimento baixo e TACOS melhorando. Nos reports, queda de venda aqui deve ser cruzada com redução deliberada de investimento/exposição antes de tratar como problema operacional.")
        if "tacos" in blob:
            points.append("TACOS da conta principal foi citado como muito melhor, saindo de 5,60% para 2,05%; usar como hipótese de eficiência de mídia, mas validar se o ganho não veio à custa de perda de volume.")
    elif account == "shopee-budamix-oficial-2":
        if "underline store" in blob or "72,7k" in blob:
            points.append("Conta 2/Underline Store foi citada com faturamento de R$ 72,7k e melhora de TACOS de 6,78% para 4,67%; tratar como conta em melhora de eficiência, mas ainda dentro do risco de canibalização entre lojas.")
        if "reestruturação semanal" in blob or "contas menores" in blob:
            points.append("Himmel propôs reestruturação semanal de campanhas nas contas menores; qualquer oscilação futura nessa conta deve ser lida junto dessa intervenção, não como ruído isolado.")
    elif account == "shopee-budamix-shop-3":
        if "budamix shop" in blob or "75k" in blob:
            points.append("Budamix Shop foi citado com cerca de R$ 75k de faturamento e TACOS melhorando de 5,69% para 4,36%; usar como sinal de eficiência crescente, mas monitorar dependência de produtos iguais às outras lojas.")
        if "reestruturação semanal" in blob or "contas menores" in blob:
            points.append("Conta menor incluída na proposta de reestruturação semanal de campanhas; nos próximos reports, separar efeito de campanha de efeito de estoque/mix.")

    if account.startswith("shopee-"):
        if "canibalização" in blob or "competem entre si" in blob:
            points.append("Risco estrutural confirmado pela reunião: as 3 lojas Shopee competem entre si com produtos/fotos semelhantes. Análises devem olhar performance consolidada Shopee e, depois, separar se uma conta cresceu às custas da outra.")
        if "154 skus" in blob or "produtos sem vendas" in blob:
            points.append("Há 154 SKUs com impressões sem conversão. Quando aparecer tráfego sem venda ou produto parado, priorizar hipótese de conversão/listing/oferta antes de aumentar verba cegamente.")
        if "jarra medidora" in blob or "1520ml" in blob or "rupturas" in blob:
            points.append("Ruptura de produtos âncora foi citada: jarra medidora e pote 1520ml. Queda nesses produtos não deve ser interpretada como demanda fraca sem checar estoque/Full.")
        if "kits pequenos" in blob or "320ml" in blob or "520ml" in blob or "640ml" in blob:
            points.append("Himmel/Rafaela sugeriu foco em kits pequenos herméticos e kits maiores para marmitas; acompanhar se esses produtos ganham força nos Top Produtos e se substituem parte da queda dos itens em ruptura.")
        if "mdf" in blob:
            points.append("Produtos MDF foram sugeridos como alternativa com estoque controlável; se aparecerem em venda/ADS, tratar como teste estratégico para reduzir dependência de importados com reposição lenta.")
        if "afiliados" in blob or "roi atual: 26" in blob:
            points.append("Afiliados foram apontados como canal saudável e subutilizado, com ROI de 26%; bons candidatos são SKUs parados, desde que o report valide conversão e estoque.")
        if "cupons" in blob:
            points.append("Teste de cupons fixos/mais chamativos foi sugerido; se houver variação de ticket ou conversão nos próximos 7 dias, considerar efeito de cupom antes de concluir mudança orgânica de demanda.")
        if "lucas" in blob and "produtos prioritários" in blob:
            points.append("Pendência operacional: Lucas deve compartilhar produtos prioritários para maio; enquanto isso não estiver fechado, recomendações de ADS Shopee ficam parcialmente dependentes dessa definição.")

    if account == "mercado-livre":
        points.append("Nenhum ponto específico de Mercado Livre identificado nesta reunião; não usar este contexto para explicar variações de ML.")

    # Deduplicate preserving order
    seen = set()
    out = []
    for pt in points:
        if pt not in seen:
            seen.add(pt); out.append(pt)
    return out

def compact_body(entry: Entry, max_chars: int = 2200) -> str:
    body = entry.body.strip()
    # Remove transcript metadata noise but keep source/summary/actions.
    body = re.sub(r"\n\*\*Transcrição:\*\*.*", "", body)
    if len(body) <= max_chars:
        return body
    return body[:max_chars].rstrip() + "\n\n_[trecho truncado para manter contexto enxuto]_"


def build_account_context(account: str, entries: list[Entry], generated_at: str) -> str:
    label = ACCOUNT_LABELS[account]
    relevant = [e for e in entries if account in classify(e)]
    relevant = sorted(relevant, key=lambda e: e.date, reverse=True)[:12]

    lines = [
        f"# Contexto Himmel/Granola — {label}",
        "",
        f"_Gerado em: {generated_at} UTC._",
        "",
        "## Como usar",
        "- Usar como contexto causal/hipótese nas análises diárias, nunca como fato isolado.",
        "- Cruzar qualquer fala/decisão de ADS com venda real, exposição, mix, cancelamentos e estoque.",
        "- Não culpar Himmel sem evidência quantitativa; formular como hipótese e ponto de checagem.",
        "- Amazon não entra nesta camada: Amazon Ads é gerido pelo Pedro.",
        "- Regra Pedro 2026-05-12: reunião Shopee consolidada vale para as 3 contas Shopee; separar particularidades por conta quando o resumo/transcrição permitir.",
        "",
        "## Contextos relevantes recentes",
    ]
    if not relevant:
        lines.append("- Nenhum contexto Himmel/Granola específico encontrado para esta conta ainda.")
    else:
        for e in relevant:
            lines.extend(["", f"### {e.date} — {e.title}"])
            interp = account_interpretation(account, e)
            if interp:
                lines.append("#### Pontos cabíveis para esta conta")
                for pt in interp:
                    lines.append(f"- {pt}")
            lines.extend(["", "#### Resumo-fonte Granola", compact_body(e)])
    lines.append("")
    return "\n".join(lines)


def run_granola_sync(days: int) -> str:
    if not GRANOLA_SYNC.exists():
        return "GRANOLA_SYNC_MISSING"
    proc = subprocess.run(
        ["python3", str(GRANOLA_SYNC), "--days", str(days)],
        cwd=str(WORKSPACE),
        text=True,
        capture_output=True,
        timeout=120,
    )
    if proc.returncode != 0:
        msg = (proc.stderr or proc.stdout or "erro desconhecido").strip()[:500]
        return f"GRANOLA_SYNC_FAILED: {msg}"
    return proc.stdout.strip() or "GRANOLA_SYNC_OK"


def main() -> int:
    ap = argparse.ArgumentParser(description="Classifica contexto Himmel/Granola por conta do Daily Sales Report v2")
    ap.add_argument("--days", type=int, default=14)
    ap.add_argument("--sync-granola", action="store_true", help="Roda scripts/granola-sync.py antes de gerar contexto")
    ap.add_argument("--write", action="store_true", help="Atualiza accounts/*/himmel-context.md; sem isso escreve previews")
    args = ap.parse_args()

    sync_status = "GRANOLA_SYNC_SKIPPED"
    if args.sync_granola:
        sync_status = run_granola_sync(args.days)

    text = GLOBAL_HIMMEL.read_text(encoding="utf-8") if GLOBAL_HIMMEL.exists() else ""
    entries = split_entries(text)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    for account in ACCOUNT_LABELS:
        content = build_account_context(account, entries, generated_at)
        if args.write:
            target = ACCOUNTS_DIR / account / "himmel-context.md"
        else:
            target = REPORTS_DIR / f"preview-himmel-context-{account}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        print(f"context OK: {account} -> {target.relative_to(WORKSPACE)}")

    print(sync_status)
    print("HIMMEL_CONTEXT_OK" if args.write else "HIMMEL_CONTEXT_DRY_RUN_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
