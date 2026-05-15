#!/usr/bin/env python3
"""Orquestra o Daily Sales Report v2 individual para Slack dos funcionários.

Fluxo diário:
1. Determina o dia anterior em BRT quando --date não é informado.
2. Executa a análise profunda por conta e salva memória do Trader.
3. Gera/envia as mensagens individuais no padrão aprovado em 2026-05-12.

Uso:
    python3 scripts/send-daily-sales-v2-slack-funcionarios.py --dry-run
    python3 scripts/send-daily-sales-v2-slack-funcionarios.py --to-pedro
    python3 scripts/send-daily-sales-v2-slack-funcionarios.py --send-real
    python3 scripts/send-daily-sales-v2-slack-funcionarios.py --date 2026-05-11 --send-real
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
LAYERED_PREVIEW = WORKSPACE / "scripts" / "daily-sales-v2-layered-preview.py"
SHOPEE_CONSOLIDATOR = WORKSPACE / "scripts" / "daily-sales-v2-shopee-consolidator-runner.py"
GENERATOR = WORKSPACE / "scripts" / "daily-sales-v2-generate-slack.py"


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
        analyzer_mode = "--write-memory"
        generator_mode = "--send-real"
        final = "SENT"
    else:
        analyzer_mode = "--write-memory"
        generator_mode = "--write-preview"
        final = "PREVIEW_WRITTEN"

    print(f"Daily Sales Report v2 — Slack Funcionários | Data: {day}")
    run_step([sys.executable, str(ANALYZER), day, analyzer_mode], "Análise profunda por conta")
    run_step([sys.executable, str(BUILD_PACKAGE), day, "--write"], "Pacote validado / Data readiness")
    run_step([sys.executable, str(LAYERED_PREVIEW), day], "Ciclo em 7 camadas / QA shadow")
    run_step([sys.executable, str(SHOPEE_CONSOLIDATOR), day], "Consolidadora Shopee / síntese consolidada")
    run_step([sys.executable, str(GENERATOR), day, generator_mode], "Geração/Envio Slack")
    print(final)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
