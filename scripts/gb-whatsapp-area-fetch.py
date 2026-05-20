#!/usr/bin/env python3
"""Read-only fetcher for GB internal WhatsApp area groups via local Evolution API.

Never sends WhatsApp messages. It resolves a group by exact subject, fetches readable
messages since the saved state, and optionally advances state.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE_URL = "https://trottingtuna-evolution.cloudfy.live"
OP_ITEM = "Evolution API Cloudfy - WhatsApp Kobe"
OP_VAULT = "OpenClaw"
INSTANCE_FALLBACK = "WHATSAPP PRÓPRIO KOBE"
STATE_DIR = Path("/root/segundo-cerebro/memory/projects/gb-whatsapp-areas/.state")
BRT = dt.timezone(dt.timedelta(hours=-3))

AREAS: dict[str, dict[str, str]] = {
    "financeiro": {"group": "Financeiro - GB Importadora", "topic": "7", "label": "Financeiro"},
    "compras": {"group": "Compras - GB Importadora", "topic": "11", "label": "Compras"},
    "contas-a-receber": {"group": "Contas a Receber - GB Importadora", "topic": "7", "label": "Contas a Receber"},
    "contas-a-pagar": {"group": "Contas a Pagar - GB Importadora", "topic": "7", "label": "Contas a Pagar"},
    "vendas-atacado": {"group": "Vendas atacado - GB Importadora", "topic": "6", "label": "Vendas Atacado"},
    "expedicao": {"group": "Expedição - GB Importadora", "topic": "10911", "label": "Expedição"},
    "socios": {"group": "Sócios - GB Importadora", "topic": "10912", "label": "Sócios"},
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


def request_json(method: str, path: str, api_key: str, payload: dict[str, Any] | None = None, timeout: int = 45) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL + path,
        data=data,
        headers={"apikey": api_key, "Content-Type": "application/json", "User-Agent": "OpenClaw/gb-area-whatsapp"},
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", "replace")
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:1000]
        raise RuntimeError(f"Evolution API HTTP {exc.code}: {body}") from exc


def extract_text(record: dict[str, Any]) -> str | None:
    msg = record.get("message") or {}
    if msg.get("conversation"):
        return msg["conversation"]
    extended = msg.get("extendedTextMessage") or {}
    if extended.get("text"):
        return extended["text"]
    for key in ("imageMessage", "videoMessage", "documentMessage", "audioMessage"):
        node = msg.get(key) or {}
        caption = node.get("caption")
        if caption:
            return caption
    reaction = msg.get("reactionMessage") or {}
    if reaction.get("text"):
        return f"[reação: {reaction['text']}]"
    return None


def ts_to_brt(timestamp: int) -> str:
    return dt.datetime.fromtimestamp(timestamp, dt.timezone.utc).astimezone(BRT).strftime("%Y-%m-%d %H:%M:%S BRT")


def state_path(area: str) -> Path:
    return STATE_DIR / f"{area}.json"


def load_state(area: str) -> dict[str, Any]:
    p = state_path(area)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except Exception:
        return {}


def save_state(area: str, state: dict[str, Any]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_path(area).write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def normalize(s: str) -> str:
    return " ".join(s.casefold().strip().split())


def resolve_group(api_key: str, instance: str, group_name: str) -> tuple[str, str]:
    inst = urllib.parse.quote(instance, safe="")
    data = request_json("GET", f"/group/fetchAllGroups/{inst}?getParticipants=false", api_key, timeout=60)
    groups = data if isinstance(data, list) else (data or {}).get("groups") or (data or {}).get("data") or []
    wanted = normalize(group_name)
    for g in groups:
        subject = g.get("subject") or g.get("name") or g.get("groupSubject") or ""
        jid = g.get("id") or g.get("jid") or g.get("remoteJid")
        if jid and normalize(subject) == wanted:
            return jid, subject
    close = []
    for g in groups:
        subject = g.get("subject") or g.get("name") or g.get("groupSubject") or ""
        if "gb" in normalize(subject) or "importadora" in normalize(subject):
            close.append(subject)
    raise RuntimeError(f"Grupo não encontrado: {group_name}. Candidatos GB: {close[:20]}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--area", choices=sorted(AREAS), required=True)
    parser.add_argument("--since-state", action="store_true")
    parser.add_argument("--update-state", action="store_true")
    parser.add_argument("--limit", type=int, default=300)
    args = parser.parse_args()

    cfg = AREAS[args.area]
    instance, api_key = load_credentials()
    jid, subject = resolve_group(api_key, instance, cfg["group"])
    inst = urllib.parse.quote(instance, safe="")
    payload = {"where": {"key": {"remoteJid": jid}}, "limit": max(args.limit, 1)}
    data = request_json("POST", f"/chat/findMessages/{inst}", api_key, payload, timeout=60)
    records = (data or {}).get("messages", {}).get("records", [])

    state = load_state(args.area)
    since_ts = int(state.get("last_message_ts") or 0) if args.since_state else 0
    messages: list[dict[str, Any]] = []
    newest_ts = since_ts
    for rec in records:
        ts = int(rec.get("messageTimestamp") or 0)
        if since_ts and ts <= since_ts:
            continue
        text = extract_text(rec)
        if not text:
            continue
        newest_ts = max(newest_ts, ts)
        key = rec.get("key") or {}
        messages.append({
            "id": key.get("id") or rec.get("id"),
            "timestamp": ts,
            "timestamp_brt": ts_to_brt(ts),
            "sender": rec.get("pushName") or key.get("participantPn") or key.get("participant") or rec.get("participant"),
            "from_me": bool(key.get("fromMe")),
            "message_type": rec.get("messageType"),
            "text": text,
        })
    messages.sort(key=lambda m: (m.get("timestamp") or 0, m.get("id") or ""))

    if args.update_state and newest_ts:
        save_state(args.area, {
            "last_message_ts": newest_ts,
            "last_checked_at_brt": dt.datetime.now(BRT).strftime("%Y-%m-%d %H:%M:%S BRT"),
            "group_jid": jid,
            "group_name": subject,
        })

    print(json.dumps({
        "ok": True,
        "area": args.area,
        "label": cfg["label"],
        "group_name": subject,
        "group_jid": jid,
        "telegram_topic": cfg["topic"],
        "count": len(messages),
        "messages": messages,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1)
