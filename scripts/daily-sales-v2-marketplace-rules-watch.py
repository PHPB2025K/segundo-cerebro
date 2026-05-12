#!/usr/bin/env python3
"""Daily Sales Report v2 — Fase 8: Marketplace Rules Watch.

Atualiza o arquivo consumido pelo Trader/Daily Sales com estado das regras,
taxas e políticas monitoradas por plataforma. Não tenta fazer web scraping pesado;
os crons semanais por plataforma fazem a revisão profunda das skills. Este script
consolida o que está documentado e destaca revisões vencidas/impacto operacional.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
RULES_WATCH = WORKSPACE / "openclaw" / "agents" / "kobe" / "shared" / "trader" / "memory" / "projects" / "daily-sales-report" / "marketplace-rules-watch.md"
SKILLS = {
    "Mercado Livre": WORKSPACE / "skills" / "marketplace" / "ml-fees-rules" / "SKILL.md",
    "Shopee": WORKSPACE / "skills" / "marketplace" / "shopee-fees-rules" / "SKILL.md",
    "Amazon": WORKSPACE / "skills" / "marketplace" / "amazon-fees-rules" / "SKILL.md",
}

BRT = timezone(timedelta(hours=-3))


@dataclass
class PlatformRules:
    platform: str
    skill_path: Path
    last_updated: str
    next_review: str
    cron: str
    summary: str
    impact: list[str]
    status: str


def extract_quoted(text: str, key: str) -> str:
    m = re.search(rf'{key}:\s*["\']([^"\']+)["\']', text)
    return m.group(1).strip() if m else "não informado"


def extract_header_summary(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("> ⚠️"):
            return line.lstrip("> ").strip()
    return "Resumo não encontrado no cabeçalho da skill."


def status_for(next_review: str, today: date) -> str:
    try:
        nr = date.fromisoformat(next_review)
    except Exception:
        return "⚠️ revisão sem data"
    if nr < today:
        return f"⚠️ revisão vencida desde {nr.isoformat()}"
    if (nr - today).days <= 3:
        return f"🟡 revisão próxima ({nr.isoformat()})"
    return f"✅ revisão vigente até {nr.isoformat()}"


def platform_impact(platform: str, text: str) -> list[str]:
    blob = text.lower()
    out: list[str] = []
    if platform == "Shopee":
        out.append("Taxas Shopee impactam diretamente margem, preço mínimo, viabilidade de cupons, frete grátis e leitura de conversão nas 3 contas.")
        if "taxa fixa" in blob:
            out.append("Monitorar armadilhas de faixa/taxa fixa, especialmente produtos entre R$ 8 e R$ 99,99.")
        if "subsídio pix" in blob or "subsidio pix" in blob:
            out.append("Subsídio PIX/cupons pode alterar ticket e conversão sem necessariamente indicar mudança orgânica de demanda.")
    elif platform == "Mercado Livre":
        out.append("Custos ML impactam margem, decisão Clássico/Premium, frete grátis, Full e competitividade de preço.")
        if "frete" in blob:
            out.append("Mudanças em frete/reputação podem explicar queda de conversão mesmo com demanda estável.")
        if "premium" in blob:
            out.append("Diferença Clássico vs Premium deve ser considerada quando exposição/parcelamento mudar performance.")
    elif platform == "Amazon":
        out.append("Regras Amazon impactam FBA, Buy Box, comissão, parcelamento e leitura de cancelamentos/indisponibilidade.")
        if "fba" in blob:
            out.append("FBA/Buy Box devem ser checados antes de escalar ADS quando houver cancelamento ou ruptura.")
        if "parcelamento" in blob:
            out.append("Taxa de parcelamento pode afetar margem e pricing em faixas específicas.")
    return out


def load_platform(platform: str, path: Path, today: date) -> PlatformRules:
    text = path.read_text(encoding="utf-8")
    last_updated = extract_quoted(text, "last_updated")
    next_review = extract_quoted(text, "next_review")
    cron = extract_quoted(text, "cron")
    summary = extract_header_summary(text)
    return PlatformRules(
        platform=platform,
        skill_path=path,
        last_updated=last_updated,
        next_review=next_review,
        cron=cron,
        summary=summary,
        impact=platform_impact(platform, text),
        status=status_for(next_review, today),
    )


def render(platforms: list[PlatformRules]) -> str:
    now = datetime.now(BRT)
    lines = [
        "# Monitoramento de Regras dos Marketplaces",
        "",
        "Registro operacional de mudanças/revisões de regras, políticas e taxas que podem impactar vendas, margem, exposição, frete, campanhas ou interpretação do Daily Sales Report v2.",
        "",
        f"_Atualizado automaticamente em {now.strftime('%Y-%m-%d %H:%M BRT')} por `daily-sales-v2-marketplace-rules-watch.py`._",
        "",
        "## Como usar no Daily Sales Report v2",
        "- Usar como contexto causal/hipótese, não como explicação automática.",
        "- Só mencionar no report se a regra/taxa/política puder explicar o dia analisado ou mudar uma prioridade prática.",
        "- Se houver revisão vencida, tratar como alerta interno de qualidade de contexto, não como mudança confirmada.",
        "- Fonte de verdade das regras detalhadas continua sendo a skill específica de cada plataforma.",
        "",
    ]
    for p in platforms:
        lines.extend([
            f"## {p.platform}",
            f"- **Status:** {p.status}",
            f"- **Última atualização da skill:** {p.last_updated}",
            f"- **Próxima revisão prevista:** {p.next_review}",
            f"- **Cron/revisão profunda:** {p.cron}",
            f"- **Skill fonte:** `{p.skill_path.relative_to(WORKSPACE)}`",
            f"- **Resumo vigente:** {p.summary}",
            "- **Impacto operacional para reports:**",
        ])
        for item in p.impact:
            lines.append(f"  - {item}")
        lines.append("")
    lines.extend([
        "---",
        "",
        "## Checklist de escalonamento",
        "Escalar para Kobe/Pedro quando:",
        "- houver mudança confirmada que afete margem/preço/frete/comissão;",
        "- revisão vencida coincidir com anomalia forte no Daily Sales;",
        "- mudança exigir decisão de preço, campanha, estoque, Full/FBA ou Himmel;",
        "- regra afetar múltiplas contas/canais ao mesmo tempo.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    today = datetime.now(BRT).date()
    platforms = [load_platform(platform, path, today) for platform, path in SKILLS.items()]
    RULES_WATCH.parent.mkdir(parents=True, exist_ok=True)
    RULES_WATCH.write_text(render(platforms), encoding="utf-8")
    for p in platforms:
        print(f"{p.platform}: {p.status}")
    print("MARKETPLACE_RULES_WATCH_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
