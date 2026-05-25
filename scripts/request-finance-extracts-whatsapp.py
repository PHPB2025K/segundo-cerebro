#!/usr/bin/env python3
"""Solicita extratos de movimentação no grupo Financeiro - GB Importadora via Evolution API.

Uso:
  python3 scripts/request-finance-extracts-whatsapp.py 01-10
  python3 scripts/request-finance-extracts-whatsapp.py 11-20
  python3 scripts/request-finance-extracts-whatsapp.py 21-fim
  python3 scripts/request-finance-extracts-whatsapp.py 01-10 --dry-run
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone

BASE_URL = "https://trottingtuna-evolution.cloudfy.live"
OP_ITEM = "Evolution API Cloudfy - WhatsApp Kobe"
OP_VAULT = "OpenClaw"
INSTANCE_FALLBACK = "WHATSAPP PRÓPRIO KOBE"
GROUP_JID = "120363428248073679@g.us"  # Financeiro - GB Importadora
BRT = timezone(timedelta(hours=-3))

PERIOD_LABELS = {
    "01-10": "01 a 10",
    "11-20": "11 a 20",
    "21-fim": "21 ao último dia do mês anterior",
}


def load_credentials() -> tuple[str, str]:
    raw = subprocess.check_output(
        ["op", "item", "get", OP_ITEM, "--vault", OP_VAULT, "--format", "json"],
        text=True,
        timeout=15,
    )
    item = json.loads(raw)
    fields = {field.get("label"): field.get("value") for field in item.get("fields", [])}
    api_key = fields.get("API Key")
    instance = fields.get("Instance Name") or INSTANCE_FALLBACK
    if not api_key:
        raise RuntimeError("API Key do WhatsApp Kobe não encontrada no 1Password")
    return instance, api_key


def build_message(period_key: str) -> str:
    period = PERIOD_LABELS[period_key]
    return (
        "Bom dia, Simone! Pode enviar aqui, por favor, os extratos de movimentação "
        f"das contas da GB referentes ao período de {period}? Obrigado."
    )


def send_message(instance: str, api_key: str, text: str) -> dict:
    url = f"{BASE_URL}/message/sendText/{urllib.parse.quote(instance)}"
    payload = json.dumps({
        "number": GROUP_JID,
        "text": text,
        "linkPreview": False,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "apikey": api_key,
            "User-Agent": "OpenClaw/finance-extract-request",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", "replace")
            return {"ok": True, "status": resp.status, "body": body[:500]}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:500]
        return {"ok": False, "status": exc.code, "body": body}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("period", choices=sorted(PERIOD_LABELS))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    text = build_message(args.period)
    if args.dry_run:
        print(text)
        return 0

    instance, api_key = load_credentials()
    result = send_message(instance, api_key, text)
    if result["ok"]:
        print(json.dumps({
            "ok": True,
            "sent_at_brt": datetime.now(BRT).strftime("%Y-%m-%d %H:%M:%S BRT"),
            "period": args.period,
            "group": "Financeiro - GB Importadora",
        }, ensure_ascii=False))
        return 0

    print(json.dumps(result, ensure_ascii=False), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
