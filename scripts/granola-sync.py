#!/usr/bin/env python3
"""Sync Granola meeting notes into Kobe/Trader/Spark memory.

- Uses Granola public API via API key stored in 1Password item "Granola" notes/password.
- Stores only structured summaries/context, not full transcripts.
- Idempotent via memory/integrations/granola-sync-state.json.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

ROOT = Path('/root/segundo-cerebro')
STATE_PATH = ROOT / 'memory/integrations/granola-sync-state.json'
TRADER_HIMMEL = ROOT / 'openclaw/agents/kobe/shared/trader/memory/projects/daily-sales-report/himmel-context.md'
SPARK_HIMMEL = ROOT / 'openclaw/agents/kobe/shared/spark/memory/context/himmel-ads-context.md'
KOBE_SESSION = ROOT / f"memory/sessions/{datetime.now(timezone.utc).date().isoformat()}.md"
API_BASE = 'https://public-api.granola.ai/v1'

ADS_KEYWORDS = [
    'himmel', 'ads', 'tacos', 'acos', 'roas', 'campanha', 'campanhas', 'budget', 'verba',
    'shopee', 'mercado livre', 'meli', 'anúncio', 'anuncio', 'afiliado', 'up-sell', 'upsell',
]
SHOPEE_KEYWORDS = ['shopee', 'budamix store', 'budamix shop', 'underline store', 'afiliado', 'cupons']
ML_KEYWORDS = ['mercado livre', 'meli', 'ml ads', 'product ads']
AMAZON_KEYWORDS = ['amazon ads', 'amazon']


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL).strip()


def get_api_key() -> str:
    env_key = os.environ.get('GRANOLA_API_KEY', '').strip()
    if env_key:
        return env_key
    # Pedro saved it in notes; some future item may use password/api_key.
    candidates: list[str] = []
    for field in ('notesPlain', 'password', 'api_key', 'credential'):
        try:
            candidates.append(run(['op', 'item', 'get', 'Granola', '--vault', 'OpenClaw', '--fields', field]))
        except Exception:
            pass
    blob = '\n'.join(candidates)
    m = re.search(r'grn_[A-Za-z0-9_.\-]+', blob)
    if not m:
        raise RuntimeError('Granola API key not found in 1Password item Granola')
    return m.group(0)


def api_get(path: str, key: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    url = API_BASE + path
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {key}'})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'ignore')[:500]
        raise RuntimeError(f'Granola API HTTP {e.code}: {body}') from e


def load_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {'processed_note_ids': [], 'last_run_at': None}


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix('.tmp')
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    tmp.replace(STATE_PATH)


def list_notes(key: str, created_after: str) -> list[dict[str, Any]]:
    notes: list[dict[str, Any]] = []
    cursor = None
    while True:
        params = {'created_after': created_after, 'limit': '50'}
        if cursor:
            params['cursor'] = cursor
        data = api_get('/notes', key, params)
        notes.extend(data.get('notes') or [])
        if not data.get('hasMore'):
            break
        cursor = data.get('cursor')
        if not cursor:
            break
    return notes


def get_note_detail(key: str, note_id: str) -> dict[str, Any]:
    return api_get(f'/notes/{note_id}', key, {'include': 'transcript'})


def text_blob(note: dict[str, Any]) -> str:
    parts = [note.get('title') or '', note.get('summary_text') or '', note.get('summary_markdown') or '']
    for a in note.get('attendees') or []:
        parts.append((a.get('name') or '') + ' ' + (a.get('email') or ''))
    ev = note.get('calendar_event') or {}
    parts.append(ev.get('event_title') or '')
    return '\n'.join(parts).lower()


def classify(note: dict[str, Any]) -> dict[str, Any]:
    blob = text_blob(note)
    platforms = []
    if any(k in blob for k in SHOPEE_KEYWORDS):
        platforms.append('Shopee')
    if any(k in blob for k in ML_KEYWORDS):
        platforms.append('Mercado Livre')
    if any(k in blob for k in AMAZON_KEYWORDS):
        platforms.append('Amazon')
    domain = 'ADS/Marketplace' if any(k in blob for k in ADS_KEYWORDS) else 'Geral'
    agents = []
    if domain == 'ADS/Marketplace':
        agents = ['Trader', 'Spark']
    else:
        agents = ['Kobe']
    return {'domain': domain, 'platforms': platforms or ['Não identificado'], 'agents': agents}


def attendees(note: dict[str, Any]) -> str:
    vals = []
    for a in note.get('attendees') or []:
        name = a.get('name') or ''
        email = a.get('email') or ''
        vals.append(f"{name} <{email}>" if name and email else name or email)
    return ', '.join(v for v in vals if v) or 'Não informado'


def extract_actions(summary: str) -> list[str]:
    lines = [re.sub(r'^[-*#\s]+', '', l).strip() for l in summary.splitlines()]
    keep = []
    triggers = ['próximo', 'proximo', 'responsável', 'responsavel', 'enviar', 'compartilhar', 'teste', 'análise', 'analise', 'reestruturação', 'reestruturacao', 'pendente']
    for l in lines:
        if l and any(t in l.lower() for t in triggers):
            keep.append(l)
    return keep[:12]


def meeting_date(note: dict[str, Any]) -> str:
    ev = note.get('calendar_event') or {}
    dt = ev.get('scheduled_start_time') or note.get('created_at') or note.get('updated_at') or ''
    if dt:
        return dt[:10]
    return datetime.now(timezone.utc).date().isoformat()


def build_entry(note: dict[str, Any], cls: dict[str, Any]) -> str:
    title = note.get('title') or '(sem título)'
    summary = note.get('summary_markdown') or note.get('summary_text') or '(sem resumo gerado)'
    actions = extract_actions(summary)
    web_url = note.get('web_url') or ''
    ev = note.get('calendar_event') or {}
    start = ev.get('scheduled_start_time') or note.get('created_at') or ''
    end = ev.get('scheduled_end_time') or ''
    transcript_len = len(note.get('transcript') or [])
    action_block = '\n'.join(f'- {a}' for a in actions) if actions else '- Nenhuma ação explícita extraída do resumo.'
    return f"""

---

## [{meeting_date(note)}] Granola — {title}

**Granola note ID:** `{note.get('id')}`  
**Link:** {web_url or 'não disponível'}  
**Horário:** {start or 'não informado'}{(' → ' + end) if end else ''}  
**Participantes:** {attendees(note)}  
**Classificação:** {cls['domain']}  
**Plataformas/contas:** {', '.join(cls['platforms'])}  
**Agentes impactados:** {', '.join(cls['agents'])}  
**Transcrição:** disponível via Granola API ({transcript_len} trechos), não copiada integralmente para memória.

### Resumo Granola
{summary.strip()}

### Ações / pendências extraídas
{action_block}

### Como usar nos reports
- Usar como contexto causal/hipótese, não como fato isolado.
- Cruzar com vendas reais, TACOS/ROAS/ACOS, exposição, estoque e campanhas nos próximos Daily Sales Reports.
- Status inicial: **aberto**.
"""


def append_once(path: Path, note_id: str, entry: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    current = path.read_text() if path.exists() else ''
    if note_id in current:
        return False
    with path.open('a', encoding='utf-8') as f:
        f.write(entry)
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--days', type=int, default=7)
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()

    key = get_api_key()
    state = load_state()
    processed = set(state.get('processed_note_ids') or [])
    created_after = (datetime.now(timezone.utc) - timedelta(days=args.days)).strftime('%Y-%m-%dT%H:%M:%SZ')
    notes = list_notes(key, created_after)
    new_count = 0
    ingested = []

    for note in sorted(notes, key=lambda n: n.get('created_at') or ''):
        nid = note.get('id')
        if not nid:
            continue
        if nid in processed and not args.force:
            continue
        detail = get_note_detail(key, nid)
        cls = classify(detail)
        entry = build_entry(detail, cls)
        # Only route ADS/Marketplace automatically to Trader/Spark memory. General goes to Kobe session note.
        if 'Trader' in cls['agents']:
            append_once(TRADER_HIMMEL, nid, entry)
        if 'Spark' in cls['agents']:
            append_once(SPARK_HIMMEL, nid, entry)
        if cls['agents'] == ['Kobe']:
            append_once(KOBE_SESSION, nid, entry)
        processed.add(nid)
        new_count += 1
        ingested.append({'id': nid, 'title': detail.get('title'), 'agents': cls['agents'], 'platforms': cls['platforms']})

    state['processed_note_ids'] = sorted(processed)
    state['last_run_at'] = datetime.now(timezone.utc).isoformat()
    state['last_created_after'] = created_after
    state['last_ingested'] = ingested[-20:]
    save_state(state)

    print(json.dumps({'ok': True, 'seen': len(notes), 'new': new_count, 'ingested': ingested}, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
