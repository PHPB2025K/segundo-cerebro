#!/usr/bin/env python3
"""Daily memory ingest — Mercado Livre.

Lê o `05-condensadora.json` do dia analisado e anexa a `memoria_para_amanha`
no `weekly.md` da conta `mercado-livre`. Isso garante que a próxima execução
do pipeline DSA (L01-L03) tenha contexto temporal acumulado, pois o runner
já injeta `weekly.md` no input das camadas analíticas (ver `daily-sales-runner-ml.py`).

Estrutura criada no `weekly.md`:
  - Seção "## Memória diária acumulada" — N blocos diários mais recentes
  - Cada bloco: classificação (fato/hipótese), confiança, itens da memoria_para_amanha
  - Rotação: mantém apenas os últimos N blocos (default 14)
  - A seção "## Histórico semanal" (depois do marker) é preservada — destino futuro
    da consolidação semanal

Uso:
  daily-memory-ingest-ml.py [YYYY-MM-DD]
Default: ontem em BRT (igual ao cron oficial do pipeline).

Idempotente: re-ingerir o mesmo dia substitui o bloco antigo (não duplica).
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
RUNS_DIR = Path("/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/runs")
MEMORY_DIR = Path("/root/segundo-cerebro/shared/daily-sales-analyst/memory/accounts/mercado-livre")
WEEKLY_FILE = MEMORY_DIR / "weekly.md"
RECIPIENT = "yasmin"
MAX_DAILY_ENTRIES = 14

ACCUMULATED_HEADER = "## Memória diária acumulada"
SEMANAL_MARKER = "*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*"


def default_day() -> str:
    return (datetime.now(BRT).date() - timedelta(days=1)).isoformat()


def build_block(target_date: str, cond: dict) -> str:
    """Monta o bloco diário a partir do JSON da L05."""
    memoria = cond.get("memoria_para_amanha") or []
    alertas = cond.get("alertas_de_confianca") or {}
    analise = cond.get("analise_final_condensada") or []
    prioridades = cond.get("prioridades_condensadas") or []

    confianca = alertas.get("nivel", "n/a")
    classifications = [str(i.get("classificacao", "")).lower() for i in analise]
    n_fato = sum(1 for c in classifications if "fato" in c)
    n_hip = sum(1 for c in classifications if "hip" in c or "risco" in c)

    ingested_at = datetime.now(BRT).isoformat(timespec="seconds")

    lines = [
        f"### Dia analisado: {target_date}",
        f"_ingestido em {ingested_at} BRT | confiança L05: {confianca} | "
        f"insights L05: {len(analise)} ({n_fato} fato, {n_hip} hipótese/risco latente) | "
        f"prioridades L05: {len(prioridades)}_",
        "",
        "**Memória para o próximo ciclo (da L05):**",
    ]
    for item in memoria:
        lines.append(f"- {item}")
    lines.append("")
    return "\n".join(lines)


def remove_existing_block(content: str, target_date: str) -> str:
    """Remove bloco diário existente da mesma data (idempotência)."""
    pattern = re.compile(
        rf"^### Dia analisado: {re.escape(target_date)}.*?(?=^### Dia analisado:|^## |^---\s*$)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub("", content)


def rotate_blocks(content: str, max_entries: int) -> str:
    """Mantém apenas N blocos diários mais recentes (no topo)."""
    pattern = re.compile(r"^### Dia analisado: ", re.MULTILINE)
    matches = list(pattern.finditer(content))
    if len(matches) <= max_entries:
        return content
    cutoff = matches[max_entries].start()
    end_section = content.find("---", cutoff)
    if end_section == -1:
        return content[:cutoff].rstrip() + "\n\n"
    return content[:cutoff].rstrip() + "\n\n" + content[end_section:]


def ensure_accumulated_section(content: str) -> str:
    """Cria seção '## Memória diária acumulada' se não existir."""
    if ACCUMULATED_HEADER in content:
        return content
    if SEMANAL_MARKER in content:
        return content.replace(
            SEMANAL_MARKER,
            f"{ACCUMULATED_HEADER}\n\n_Blocos diários abaixo. Job `daily-memory-ingest-ml.py` adiciona um bloco por dia. "
            f"Rotação automática mantém os últimos {MAX_DAILY_ENTRIES} dias._\n\n---\n\n{SEMANAL_MARKER}",
        )
    return content.rstrip() + (
        f"\n\n{ACCUMULATED_HEADER}\n\n"
        f"_Blocos diários abaixo. Job `daily-memory-ingest-ml.py` adiciona um bloco por dia. "
        f"Rotação automática mantém os últimos {MAX_DAILY_ENTRIES} dias._\n\n"
    )


def insert_block(content: str, block: str) -> str:
    """Insere o bloco logo após o cabeçalho da seção acumulada."""
    marker = re.compile(
        rf"({re.escape(ACCUMULATED_HEADER)}\n\n_[^_]+_\n\n)",
        re.DOTALL,
    )
    m = marker.search(content)
    if m:
        idx = m.end()
        return content[:idx] + block + "\n" + content[idx:]
    idx = content.find(ACCUMULATED_HEADER)
    if idx == -1:
        return content + "\n" + block + "\n"
    return content[: idx + len(ACCUMULATED_HEADER)] + "\n\n" + block + "\n" + content[idx + len(ACCUMULATED_HEADER):]


def main() -> int:
    target_date = sys.argv[1] if len(sys.argv) > 1 else default_day()

    cond_path = RUNS_DIR / target_date / RECIPIENT / "05-condensadora.json"
    if not cond_path.exists():
        print(f"SKIP: condensadora não encontrada em {cond_path}", file=sys.stderr)
        return 0

    with cond_path.open() as f:
        cond = json.load(f)

    memoria = cond.get("memoria_para_amanha") or []
    if not memoria:
        print(f"SKIP: memoria_para_amanha vazia para {target_date}", file=sys.stderr)
        return 0

    block = build_block(target_date, cond)

    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    existing = WEEKLY_FILE.read_text() if WEEKLY_FILE.exists() else ""

    cleaned = remove_existing_block(existing, target_date)
    cleaned = ensure_accumulated_section(cleaned)
    new_content = insert_block(cleaned, block)
    new_content = rotate_blocks(new_content, MAX_DAILY_ENTRIES)

    WEEKLY_FILE.write_text(new_content)
    print(f"OK: ingestido bloco de {target_date} em {WEEKLY_FILE} ({len(memoria)} itens)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
