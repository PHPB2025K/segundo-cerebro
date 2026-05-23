#!/usr/bin/env python3
"""Consolidação semanal — Mercado Livre.

Lê os 7 blocos diários da `## Memória diária acumulada` no `weekly.md`,
chama Opus 4.7 via `claude -p` com o prompt 08-weekly-consolidator,
e insere o bloco `### Semana: DD/MM a DD/MM/AAAA` resultante na seção
de Histórico Semanal (depois do marker `*Histórico semanal abaixo...*`).

Cron sugerido: toda segunda às 09:00 BRT (12:00 UTC na VPS).
Crontab: `0 12 * * 1 ...`

Uso:
  daily-sales-weekly-consolidator-ml.py [--week-end YYYY-MM-DD]
Default `--week-end`: domingo passado em BRT.

Idempotente: re-rodar a mesma semana substitui o bloco existente.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import urllib.request
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
MEMORY_DIR = Path("/root/segundo-cerebro/shared/daily-sales-analyst/memory/accounts/mercado-livre")
WEEKLY_FILE = MEMORY_DIR / "weekly.md"
PROMPT_PATH = Path(
    "/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/"
    "prompts/versions/v4.0/mercado-livre/08-weekly-consolidator.md"
)
HISTORY_MARKER = "*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*"
ACCUMULATED_HEADER = "## Memória diária acumulada"
LLM_MODEL = "claude-opus-4-7"
LLM_TIMEOUT = 900

SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_ENV_FILE = Path("/root/.openclaw/credentials/supabase.env")


def default_week_end() -> str:
    today = datetime.now(BRT).date()
    last_sunday = today - timedelta(days=(today.weekday() + 1) % 7 or 7)
    return last_sunday.isoformat()


def parse_daily_blocks(content: str) -> list[dict]:
    """Extrai blocos `### Dia analisado: YYYY-MM-DD` da seção acumulada."""
    if ACCUMULATED_HEADER not in content:
        return []
    section_start = content.index(ACCUMULATED_HEADER) + len(ACCUMULATED_HEADER)
    section_end = content.find("---", section_start)
    if section_end == -1:
        section_end = len(content)
    section = content[section_start:section_end]

    blocks = []
    pattern = re.compile(r"^### Dia analisado: (\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
    starts = [(m.group(1), m.start()) for m in pattern.finditer(section)]
    for idx, (date_iso, pos) in enumerate(starts):
        end = starts[idx + 1][1] if idx + 1 < len(starts) else len(section)
        body = section[pos:end].strip()
        blocks.append({"date": date_iso, "body": body})
    return blocks


def filter_week_blocks(blocks: list[dict], week_start: str, week_end: str) -> list[dict]:
    """Filtra blocos cuja data está dentro do intervalo [week_start, week_end]."""
    out = []
    for b in blocks:
        if week_start <= b["date"] <= week_end:
            out.append(b)
    out.sort(key=lambda x: x["date"])
    return out


def load_supabase_creds():
    if not SUPABASE_ENV_FILE.exists():
        return None
    creds = {}
    for line in SUPABASE_ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        creds[k.strip()] = v.strip().strip('"').strip("'")
    return creds.get("SUPABASE_SERVICE_ROLE_KEY")


def fetch_current_mercadolider_snapshot():
    """Lê o snapshot ml_account_snapshots mais recente do Supabase."""
    key = load_supabase_creds()
    if not key:
        return None
    url = (
        f"{SUPABASE_URL}/rest/v1/ml_account_snapshots"
        "?select=snapshot_date,power_seller_status,sales_60d_revenue_brl,"
        "platinum_revenue_gap_brl,platinum_progress_pct,claims_rate,"
        "cancellations_rate,delayed_handling_rate"
        "&order=snapshot_date.desc&limit=1"
    )
    req = urllib.request.Request(url, headers={"apikey": key, "Authorization": f"Bearer {key}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
            return data[0] if data else None
    except Exception:
        return None


def build_llm_input(blocks: list[dict], week_label: str, snapshot: dict | None) -> str:
    prompt = PROMPT_PATH.read_text()
    sections = [
        prompt,
        "\n---\n",
        f"# Contexto de execução — Consolidação Semanal Mercado Livre\n",
        f"Período da semana: {week_label}\n",
        f"Blocos diários disponíveis: {len(blocks)} de 7\n",
    ]
    if snapshot:
        sections.append("\n## Snapshot MercadoLíder mais recente\n")
        sections.append(f"```json\n{json.dumps(snapshot, indent=2, ensure_ascii=False)}\n```\n")
    sections.append("\n## Blocos diários da semana\n")
    if not blocks:
        sections.append("_Nenhum bloco diário disponível para a semana._\n")
    for b in blocks:
        sections.append(f"\n{b['body']}\n")
    return "\n".join(sections)


def call_opus(prompt_text: str) -> tuple[str | None, str | None]:
    try:
        result = subprocess.run(
            ["claude", "-p", "--model", LLM_MODEL, "--allowedTools", ""],
            input=prompt_text,
            capture_output=True,
            text=True,
            timeout=LLM_TIMEOUT,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip(), None
        return None, (result.stderr or "").strip() or f"returncode={result.returncode}"
    except subprocess.TimeoutExpired:
        return None, f"timeout ({LLM_TIMEOUT}s)"
    except Exception as e:
        return None, str(e)


def remove_existing_weekly_block(content: str, week_label: str) -> str:
    pattern = re.compile(
        rf"^### Semana: {re.escape(week_label)}.*?(?=^### Semana:|^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub("", content)


def insert_weekly_block(content: str, block: str) -> str:
    if HISTORY_MARKER not in content:
        return content.rstrip() + "\n\n" + block.rstrip() + "\n"
    idx = content.index(HISTORY_MARKER) + len(HISTORY_MARKER)
    return content[:idx] + "\n\n" + block.rstrip() + "\n" + content[idx:]


def format_week_label(week_start: str, week_end: str) -> str:
    start_dt = datetime.strptime(week_start, "%Y-%m-%d")
    end_dt = datetime.strptime(week_end, "%Y-%m-%d")
    return f"{start_dt.strftime('%d/%m')} a {end_dt.strftime('%d/%m/%Y')}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Consolidação semanal Mercado Livre — Opus 4.7")
    parser.add_argument("--week-end", default=default_week_end(),
                        help="Data fim da semana (domingo) YYYY-MM-DD; default = último domingo BRT")
    parser.add_argument("--min-days", type=int, default=7,
                        help="Mínimo de blocos diários pra rodar a consolidação. Default 7.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Imprime o output sem gravar no weekly.md")
    args = parser.parse_args()

    week_end_dt = datetime.strptime(args.week_end, "%Y-%m-%d").date()
    week_start_dt = week_end_dt - timedelta(days=6)
    week_start = week_start_dt.isoformat()
    week_end = week_end_dt.isoformat()
    week_label = format_week_label(week_start, week_end)

    if not WEEKLY_FILE.exists():
        print(f"SKIP: weekly.md não encontrado em {WEEKLY_FILE}", file=sys.stderr)
        return 0

    content = WEEKLY_FILE.read_text()
    all_blocks = parse_daily_blocks(content)
    blocks = filter_week_blocks(all_blocks, week_start, week_end)

    if len(blocks) < args.min_days:
        print(
            f"SKIP: apenas {len(blocks)} de 7 blocos diários disponíveis para "
            f"{week_label} (mínimo: {args.min_days}). Consolidação não gerada.",
            file=sys.stderr,
        )
        return 0

    snapshot = fetch_current_mercadolider_snapshot()
    llm_input = build_llm_input(blocks, week_label, snapshot)
    print(f"Consolidando semana {week_label} com {len(blocks)} blocos via {LLM_MODEL}...")
    output, err = call_opus(llm_input)
    if not output:
        print(f"ERRO Opus: {err}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(output)
        return 0

    cleaned = remove_existing_weekly_block(content, week_label)
    new_content = insert_weekly_block(cleaned, output)
    WEEKLY_FILE.write_text(new_content)
    print(f"OK: bloco semanal {week_label} gravado em {WEEKLY_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
