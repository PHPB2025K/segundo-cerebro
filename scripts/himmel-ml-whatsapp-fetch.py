#!/usr/bin/env python3
"""Fetch readable messages from the Himmel ML WhatsApp group via Evolution API.

This script intentionally only reads messages. It never sends WhatsApp messages.
Credentials are read from 1Password item "Evolution API Cloudfy - WhatsApp Kobe".
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
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
GROUP_JID = "120363400937784728@g.us"
GROUP_NAME = "💎 [HML*] BUDAMIX"
STATE_PATH = Path("/root/segundo-cerebro/shared/trader/memory/projects/daily-sales-report/.himmel-ml-whatsapp-state.json")


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
        raise RuntimeError("API Key not found in 1Password item")
    return instance, api_key


def request_json(method: str, path: str, api_key: str, payload: dict[str, Any] | None = None) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL + path,
        data=data,
        headers={
            "apikey": api_key,
            "Content-Type": "application/json",
            "User-Agent": "OpenClaw/1.0",
        },
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:2000]
        raise RuntimeError(f"Evolution API HTTP {exc.code}: {body}") from exc


def extract_text(record: dict[str, Any]) -> str | None:
    message = record.get("message") or {}
    if message.get("conversation"):
        return message["conversation"]
    extended = message.get("extendedTextMessage") or {}
    if extended.get("text"):
        return extended["text"]
    image = message.get("imageMessage") or {}
    if image.get("caption"):
        return image["caption"]
    video = message.get("videoMessage") or {}
    if video.get("caption"):
        return video["caption"]
    document = message.get("documentMessage") or {}
    if document.get("caption"):
        return document["caption"]
    return None


def ts_to_iso(timestamp: Any) -> str | None:
    if timestamp is None:
        return None
    try:
        return dt.datetime.fromtimestamp(int(timestamp), dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=-3))).isoformat()
    except Exception:
        return None


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text())
    except Exception:
        return {}


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Himmel ML WhatsApp group messages")
    parser.add_argument("--since-state", action="store_true", help="only return messages newer than saved state")
    parser.add_argument("--update-state", action="store_true", help="advance saved state to newest fetched message")
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    instance, api_key = load_credentials()
    inst = urllib.parse.quote(instance, safe="")

    # Validate group membership/name without exposing participants in output.
    info = request_json("GET", f"/group/findGroupInfos/{inst}?groupJid={urllib.parse.quote(GROUP_JID, safe='')}", api_key)
    if info.get("id") != GROUP_JID:
        raise RuntimeError("Unexpected group info response")

    payload = {"where": {"key": {"remoteJid": GROUP_JID}}, "limit": max(args.limit, 1)}
    data = request_json("POST", f"/chat/findMessages/{inst}", api_key, payload)
    records = data.get("messages", {}).get("records", [])

    state = load_state()
    since_ts = int(state.get("last_message_ts") or 0) if args.since_state else 0
    messages: list[dict[str, Any]] = []
    newest_ts = since_ts

    for rec in records:
        text = extract_text(rec)
        if not text:
            continue
        ts = int(rec.get("messageTimestamp") or 0)
        if since_ts and ts <= since_ts:
            continue
        newest_ts = max(newest_ts, ts)
        key = rec.get("key") or {}
        messages.append(
            {
                "group": GROUP_NAME,
                "group_jid": GROUP_JID,
                "id": key.get("id") or rec.get("id"),
                "timestamp": ts,
                "timestamp_brt": ts_to_iso(ts),
                "from_me": bool(key.get("fromMe")),
                "sender": rec.get("pushName") or key.get("participantPn") or key.get("participant"),
                "participant": key.get("participantPn") or key.get("participant"),
                "message_type": rec.get("messageType"),
                "text": text,
            }
        )

    messages.sort(key=lambda m: (m.get("timestamp") or 0, m.get("id") or ""))

    if args.update_state and newest_ts:
        save_state({"last_message_ts": newest_ts, "last_checked_at_brt": dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).isoformat()})

    print(json.dumps({"ok": True, "group": GROUP_NAME, "group_jid": GROUP_JID, "count": len(messages), "messages": messages}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1)
