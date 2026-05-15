#!/usr/bin/env python3
"""Orquestrador legado do Daily Sales Report v2 individual para funcionários.

LOCK DE OWNERSHIP (2026-05-15): este wrapper não executa mais Slack Writer,
QA Gate, Consolidadora Shopee nem envio por scripts paralelos. O caminho oficial
é Trader → Daily Sales Analyst (DSA) → Trader → Kobe.

Este arquivo permanece apenas como compatibilidade para crons/wrappers antigos:
1. determina o dia anterior em BRT quando --date não é informado;
2. executa análise/memória do Trader e pacote validado;
3. delega a execução das camadas ao runner oficial do DSA em modo preview/shadow.

Envio real por este wrapper fica bloqueado até promoção explícita do Pedro.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
WORKSPACE = Path(__file__).resolve().parent.parent
ANALYZER = WORKSPACE / "scripts" / "daily-sales-v2-analyzer.py"
BUILD_PACKAGE = WORKSPACE / "scripts" / "daily-sales-v2-build-package.py"
DSA_RUNNER = WORKSPACE / "scripts" / "daily-sales-analyst-runner.py"


def default_day() -> str:
    return (datetime.now(BRT).date() - timedelta(days=1)).isoformat()


def run_step(cmd: list[str], label: str) -> None:
    print(f"\n--- {label} ---")
    result = subprocess.run(cmd, cwd=WORKSPACE, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(description="Daily Sales Report v2 — Slack funcionários")
    parser.add_argument("--date", default=default_day(), help="Data analisada YYYY-MM-DD; default ontem em BRT")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--dry-run", action="store_true", help="Roda análise sem salvar e gera preview sem enviar")
    group.add_argument("--write-preview", action="store_true", help="Salva análise/memória e previews, sem enviar")
    group.add_argument("--to-pedro", action="store_true", help="Envia previews para Pedro, não para equipe")
    group.add_argument("--send-real", action="store_true", help="Envia real para Lucas/Yasmin/Leonardo")
    args = parser.parse_args()

    day = args.date
    try:
        datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        print("ERRO: use data YYYY-MM-DD", file=sys.stderr)
        return 1

    if args.dry_run:
        analyzer_mode = "--dry-run"
        generator_mode = "--dry-run"
        final = "DRY_RUN_OK"
    elif args.to_pedro:
        analyzer_mode = "--write-memory"
        generator_mode = "--to-pedro"
        final = "PREVIEW_SENT_TO_PEDRO"
    elif args.send_real:
        print("BLOQUEADO: envio real por wrapper legado desativado. Use cadeia Trader → DSA → Trader após aprovação do Pedro.", file=sys.stderr)
        return 2
    else:
        analyzer_mode = "--write-memory"
        generator_mode = "--write-preview"
        final = "PREVIEW_WRITTEN"

    print(f"Daily Sales Report v2 — Slack Funcionários | Data: {day}")
    run_step([sys.executable, str(ANALYZER), day, analyzer_mode], "Análise profunda por conta")
    run_step([sys.executable, str(BUILD_PACKAGE), day, "--write"], "Pacote validado / Data readiness")
    dsa_mode = "--dry-run" if args.dry_run else "--preview-to-kobe"
    run_step([sys.executable, str(DSA_RUNNER), day, dsa_mode, "--llm"], "Daily Sales Analyst oficial — camadas LLM + QA shadow")
    print(final)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
