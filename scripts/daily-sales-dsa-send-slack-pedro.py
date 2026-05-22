#!/usr/bin/env python3
"""Send Daily Sales Analyst outputs to Pedro's personal Slack DM only.

This is the production delivery bridge for the temporary rollout state approved
on 2026-05-15: full DSA LLM pipeline for Lucas/Yasmin/Leonardo, but delivery to
Pedro Broglio's Slack DM only — never to employee DMs.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRT = timezone(timedelta(hours=-3))
WORKSPACE = Path(__file__).resolve().parent.parent
RUNS_DIR = WORKSPACE / "shared" / "daily-sales-analyst" / "runs"
OP_ITEM = "Slack Pedro Read Only"
OP_VAULT = "OpenClaw"
PEDRO_SLACK_USER_ID = "U03UY0UNLDC"
EXPECTED_RECIPIENTS = ["lucas", "yasmin", "leonardo"]
DISPLAY_NAMES = {
    "lucas": "Lucas / Shopee",
    "yasmin": "Yasmin / Mercado Livre",
    "leonardo": "Leonardo / Amazon",
}


def default_day() -> str:
    return (datetime.now(BRT).date() - timedelta(days=1)).isoformat()


def load_op_service_token() -> None:
    if os.environ.get("OP_SERVICE_ACCOUNT_TOKEN"):
        return
    try:
        out = subprocess.check_output(["pgrep", "-f", "openclaw-gateway"], text=True).splitlines()
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
        raise RuntimeError("Não consegui ler o token Slack no 1Password")
    data = json.loads(result.stdout)
    for field in data.get("fields", []):
        label = (field.get("label") or "").lower()
        value = field.get("value") or ""
        if label == "token" or value.startswith(("xoxp-", "xoxb-", "xoxe.xoxp-")):
            return value
    raise RuntimeError("Token Slack não encontrado no item 1Password")


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


def text_to_blocks(text: str) -> list[dict]:
    # Keep formatting conservative: Slack mrkdwn section chunks.
    chunks: list[str] = []
    remaining = text
    while remaining:
        chunks.append(remaining[:2900])
        remaining = remaining[2900:]
    return [{"type": "section", "text": {"type": "mrkdwn", "text": chunk}} for chunk in chunks]


def send_dm_to_pedro(text: str, *, dry_run: bool) -> None:
    if dry_run:
        print(text)
        return
    opened = slack_api("conversations.open", {"users": PEDRO_SLACK_USER_ID}, post=True)
    if not opened.get("ok"):
        raise RuntimeError(f"conversations.open falhou: {opened.get('error')}")
    channel = (opened.get("channel") or {}).get("id")
    sent = slack_api(
        "chat.postMessage",
        {
            "channel": channel,
            "text": text,
            "blocks": json.dumps(text_to_blocks(text), ensure_ascii=False),
        },
        post=True,
    )
    if not sent.get("ok"):
        raise RuntimeError(f"chat.postMessage falhou: {sent.get('error')}")


def recipient_is_full_llm(recipient: dict) -> bool:
    details = recipient.get("llm_layers_detail") or {}
    if not recipient.get("llm_used") or not details:
        return False
    return all(layer.get("llm_used") is True and layer.get("fallback") is False for layer in details.values())


def load_qa_gate(recipient: dict) -> dict:
    qa_path = ((recipient.get("layers") or {}).get("layer7_qa_gate") or "").strip()
    if not qa_path:
        raise RuntimeError("Recipient sem artefato QA Gate")
    path = Path(qa_path)
    if not path.exists():
        raise RuntimeError(f"Artefato QA Gate não encontrado: {path}")
    return json.loads(path.read_text())


def qa_gate_allows_send(recipient: dict) -> bool:
    qa = load_qa_gate(recipient)
    verdict = str(qa.get("resultado_qa") or qa.get("verdict") or "").upper()
    if "BLOQUEADO" in verdict or verdict == "BLOCKED":
        return False
    if qa.get("send_allowed") is False:
        return False
    if qa.get("fallback") is True or qa.get("llm_used") is not True:
        return False
    return True


def validate_manifest(manifest: dict, target_recipients: list[str]) -> None:
    """Valida o manifest apenas para os recipients alvo (permite execução por plataforma)."""
    recipients = manifest.get("recipients") or {}
    missing = [name for name in target_recipients if name not in recipients]
    if missing:
        raise RuntimeError(f"Manifest sem recipients obrigatórios: {', '.join(missing)}")
    not_llm = [name for name in target_recipients if not recipient_is_full_llm(recipients[name])]
    if not_llm:
        raise RuntimeError(f"Recipients não estão 100% LLM: {', '.join(not_llm)}")
    blocked = [name for name in target_recipients if recipients[name].get("status") == "BLOCKED"]
    if blocked:
        raise RuntimeError(f"Recipients bloqueados: {', '.join(blocked)}")
    qa_blocked = [name for name in target_recipients if not qa_gate_allows_send(recipients[name])]
    if qa_blocked:
        raise RuntimeError(f"QA Gate não permite envio: {', '.join(qa_blocked)}")


def load_manifest(day: str) -> dict:
    path = RUNS_DIR / day / "manifest.json"
    if not path.exists():
        raise RuntimeError("Manifest do DSA não encontrado para a data analisada")
    return json.loads(path.read_text())


def extract_slack_message(raw: str) -> str:
    """Extrai apenas o bloco da mensagem Slack do artefato L06.

    O arquivo 06-slack-preview.md tem três blocos por design:
      ### Mensagem Slack       (vai pro Slack — dentro de ```...```)
      ### Respeito de bloqueios (log auditável pra L07 QA Gate)
      ### Decisões de formatação (log auditável pra L07 QA Gate)

    Só o primeiro deve ser enviado. A extração pega o conteúdo entre
    a primeira e a segunda ocorrência de ``` no arquivo.
    """
    first = raw.find("```")
    if first == -1:
        return raw.strip()
    second = raw.find("```", first + 3)
    if second == -1:
        return raw.strip()
    body = raw[first + 3:second]
    if body.startswith("\n"):
        body = body[1:]
    return body.strip()


def load_message(recipient: dict) -> str:
    layer_path = ((recipient.get("layers") or {}).get("layer6_slack_writer") or "").strip()
    if not layer_path:
        raise RuntimeError("Recipient sem artefato Slack Writer")
    path = Path(layer_path)
    if not path.exists():
        raise RuntimeError("Artefato Slack Writer não encontrado")
    raw = path.read_text().strip()
    if not raw:
        raise RuntimeError("Artefato Slack Writer vazio")
    message = extract_slack_message(raw)
    if not message:
        raise RuntimeError("Bloco de mensagem Slack vazio após extração")
    if message.lstrip().startswith("### Respeito") or message.lstrip().startswith("### Decisões"):
        raise RuntimeError(
            "Extração quebrou: bloco extraído começa com log auditável. "
            "Verificar formato do L06 antes de reenviar."
        )
    return message


def persist_sent_message(date_iso: str, recipient_key: str, text: str, *, dry_run: bool) -> None:
    """Persist the exact text sent to Slack (after sender transformations).

    Single source of truth for what reached the user — used by Mission Control
    to render the Sender stage INPUT/OUTPUT. Saved in both dry-run and real send,
    overwritten on each invocation so the file always reflects the latest send.
    """
    run_dir = RUNS_DIR / date_iso / recipient_key
    if not run_dir.exists():
        return
    out_path = run_dir / "08-slack-sent.txt"
    timestamp = datetime.now(BRT).isoformat(timespec="seconds")
    mode = "dry-run" if dry_run else "real"
    header_comment = (
        f"<!-- sender_mode={mode} sent_at_brt={timestamp} recipient={recipient_key} -->\n"
    )
    out_path.write_text(header_comment + text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Enviar outputs DSA para Slack pessoal do Pedro")
    parser.add_argument("--date", default=default_day(), help="Data analisada YYYY-MM-DD; default ontem BRT")
    parser.add_argument(
        "--recipients",
        default=",".join(EXPECTED_RECIPIENTS),
        help="Lista comma-separated de recipients (lucas,yasmin,leonardo). "
             "Default: todos. Use pra rodar pipeline por plataforma.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Não envia; imprime destino e validações")
    args = parser.parse_args()

    target_recipients = [r.strip().lower() for r in args.recipients.split(",") if r.strip()]
    unknown = [r for r in target_recipients if r not in EXPECTED_RECIPIENTS]
    if unknown:
        raise SystemExit(f"Recipients desconhecidos: {', '.join(unknown)}. "
                         f"Válidos: {', '.join(EXPECTED_RECIPIENTS)}")

    manifest = load_manifest(args.date)
    validate_manifest(manifest, target_recipients)
    recipients = manifest["recipients"]

    sent = []
    for key in target_recipients:
        header = f"*Daily Sales Report — {DISPLAY_NAMES[key]}*\n_Entrega temporária: enviado só para Pedro._\n\n"
        final_text = header + load_message(recipients[key])
        persist_sent_message(args.date, key, final_text, dry_run=args.dry_run)
        send_dm_to_pedro(final_text, dry_run=args.dry_run)
        sent.append(DISPLAY_NAMES[key])

    print("SENT_TO_PEDRO_SLACK " + ", ".join(sent))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
