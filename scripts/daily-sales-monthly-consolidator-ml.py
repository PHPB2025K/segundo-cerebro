#!/usr/bin/env python3
"""Consolidação mensal — Mercado Livre.

Lê 4-5 blocos semanais (`### Semana: ...`) do mês anterior no `weekly.md`,
chama Opus 4.7 via `claude -p` com o prompt 09-monthly-consolidator, e
insere o bloco `### Mês: MM/AAAA` resultante no `monthly.md`.

Cron sugerido: dia 1 do mês às 09:00 BRT (12:00 UTC na VPS).
Crontab: `0 12 1 * * ...`

Uso:
  daily-sales-monthly-consolidator-ml.py [--month YYYY-MM]
Default `--month`: mês anterior em BRT.

Idempotente: re-rodar o mesmo mês substitui o bloco existente.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
MEMORY_DIR = Path("/root/segundo-cerebro/shared/daily-sales-analyst/memory/accounts/mercado-livre")
WEEKLY_FILE = MEMORY_DIR / "weekly.md"
MONTHLY_FILE = MEMORY_DIR / "monthly.md"
PROMPT_PATH = Path(
    "/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/"
    "prompts/versions/v4.0/mercado-livre/09-monthly-consolidator.md"
)
HISTORY_MARKER_MONTHLY = "*Histórico mensal abaixo. Não sobrescrever — adicionar nova entrada acima.*"
LLM_MODEL = "claude-opus-4-7"
LLM_TIMEOUT = 1200

SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_ENV_FILE = Path("/root/.openclaw/credentials/supabase.env")


def default_month() -> str:
    today = datetime.now(BRT).date()
    first_of_this_month = today.replace(day=1)
    last_of_prev_month = first_of_this_month - timedelta(days=1)
    return last_of_prev_month.strftime("%Y-%m")


def parse_weekly_blocks(content: str) -> list[dict]:
    """Extrai blocos `### Semana: DD/MM a DD/MM/AAAA` do weekly.md."""
    pattern = re.compile(
        r"^### Semana: (\d{2})/(\d{2}) a (\d{2})/(\d{2})/(\d{4})\s*$",
        re.MULTILINE,
    )
    starts = []
    for m in pattern.finditer(content):
        start_dd, start_mm, end_dd, end_mm, year = m.groups()
        starts.append({
            "match": m,
            "label": m.group(0).replace("### Semana: ", ""),
            "start_date": f"{year}-{start_mm}-{start_dd}",
            "end_date": f"{year}-{end_mm}-{end_dd}",
            "pos": m.start(),
        })

    blocks = []
    for idx, info in enumerate(starts):
        next_start = starts[idx + 1]["pos"] if idx + 1 < len(starts) else len(content)
        body = content[info["pos"]:next_start].strip()
        blocks.append({"label": info["label"], "start_date": info["start_date"],
                       "end_date": info["end_date"], "body": body})
    return blocks


def filter_month_blocks(blocks: list[dict], month: str) -> list[dict]:
    """Filtra blocos cuja end_date está dentro do mês YYYY-MM."""
    out = []
    for b in blocks:
        if b["end_date"].startswith(month):
            out.append(b)
    out.sort(key=lambda x: x["end_date"])
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


def get_previous_month_thesis(month: str) -> str | None:
    """Pega o bloco do mês anterior em monthly.md, se existir."""
    if not MONTHLY_FILE.exists():
        return None
    dt = datetime.strptime(month, "%Y-%m")
    first_of_month = dt.replace(day=1)
    prev_last = first_of_month - timedelta(days=1)
    prev_month = prev_last.strftime("%m/%Y")
    content = MONTHLY_FILE.read_text()
    pattern = re.compile(
        rf"^### Mês: {re.escape(prev_month)}\s*$.*?(?=^### Mês:|^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(content)
    return m.group(0).strip() if m else None


def build_llm_input(weekly_blocks: list[dict], month_label: str, snapshot, prev_thesis) -> str:
    prompt = PROMPT_PATH.read_text()
    sections = [
        prompt,
        "\n---\n",
        f"# Contexto de execução — Consolidação Mensal Mercado Livre\n",
        f"Mês de referência: {month_label}\n",
        f"Blocos semanais disponíveis: {len(weekly_blocks)}\n",
    ]
    if snapshot:
        sections.append("\n## Snapshot MercadoLíder mais recente\n")
        sections.append(f"```json\n{json.dumps(snapshot, indent=2, ensure_ascii=False)}\n```\n")
    if prev_thesis:
        sections.append("\n## Tese do mês anterior (referência)\n")
        sections.append(prev_thesis + "\n")
    else:
        sections.append("\n## Tese do mês anterior\n_Não existe — primeira consolidação mensal._\n")
    sections.append("\n## Blocos semanais do mês\n")
    if not weekly_blocks:
        sections.append("_Nenhum bloco semanal disponível para o mês._\n")
    for b in weekly_blocks:
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


def remove_existing_monthly_block(content: str, month_label: str) -> str:
    pattern = re.compile(
        rf"^### Mês: {re.escape(month_label)}.*?(?=^### Mês:|^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    return pattern.sub("", content)


def insert_monthly_block(content: str, block: str) -> str:
    if HISTORY_MARKER_MONTHLY not in content:
        return content.rstrip() + "\n\n" + block.rstrip() + "\n"
    idx = content.index(HISTORY_MARKER_MONTHLY) + len(HISTORY_MARKER_MONTHLY)
    return content[:idx] + "\n\n" + block.rstrip() + "\n" + content[idx:]


def main() -> int:
    parser = argparse.ArgumentParser(description="Consolidação mensal Mercado Livre — Opus 4.7")
    parser.add_argument("--month", default=default_month(),
                        help="Mês YYYY-MM; default = mês anterior em BRT")
    parser.add_argument("--min-weeks", type=int, default=2,
                        help="Mínimo de blocos semanais pra rodar a consolidação. Default 2.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Imprime o output sem gravar no monthly.md")
    args = parser.parse_args()

    month = args.month
    dt = datetime.strptime(month, "%Y-%m")
    month_label = dt.strftime("%m/%Y")

    if not WEEKLY_FILE.exists():
        print(f"SKIP: weekly.md não encontrado em {WEEKLY_FILE}", file=sys.stderr)
        return 0

    all_weekly = parse_weekly_blocks(WEEKLY_FILE.read_text())
    weekly_blocks = filter_month_blocks(all_weekly, month)

    if len(weekly_blocks) < args.min_weeks:
        print(
            f"SKIP: apenas {len(weekly_blocks)} blocos semanais disponíveis para "
            f"{month_label} (mínimo: {args.min_weeks}). Consolidação mensal não gerada.",
            file=sys.stderr,
        )
        return 0

    snapshot = fetch_current_mercadolider_snapshot()
    prev_thesis = get_previous_month_thesis(month)
    llm_input = build_llm_input(weekly_blocks, month_label, snapshot, prev_thesis)
    print(f"Consolidando mês {month_label} com {len(weekly_blocks)} blocos semanais via {LLM_MODEL}...")
    output, err = call_opus(llm_input)
    if not output:
        print(f"ERRO Opus: {err}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(output)
        return 0

    MONTHLY_FILE.parent.mkdir(parents=True, exist_ok=True)
    content = MONTHLY_FILE.read_text() if MONTHLY_FILE.exists() else ""
    cleaned = remove_existing_monthly_block(content, month_label)
    new_content = insert_monthly_block(cleaned, output)
    MONTHLY_FILE.write_text(new_content)
    print(f"OK: bloco mensal {month_label} gravado em {MONTHLY_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
