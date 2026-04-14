#!/bin/bash
# brain-boot.sh — Executado pelo SessionStart hook do Claude Code
# Sincroniza o repositório do segundo cérebro antes de cada sessão.

set -e

if [ -z "$SECOND_BRAIN_PATH" ]; then
  echo "⚠️  SECOND_BRAIN_PATH não configurado."
  exit 1
fi

if [ ! -d "$SECOND_BRAIN_PATH" ]; then
  echo "⚠️  Diretório não encontrado: $SECOND_BRAIN_PATH"
  exit 1
fi

if [ ! -d "$SECOND_BRAIN_PATH/.git" ]; then
  echo "⚠️  $SECOND_BRAIN_PATH não é um repositório git."
  exit 1
fi

cd "$SECOND_BRAIN_PATH"

BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
REMOTE=$(git remote 2>/dev/null | head -1)

echo "=== SEGUNDO CÉREBRO — $(date '+%d/%m/%Y %H:%M') ==="
echo "Repo: $SECOND_BRAIN_PATH"

if [ -n "$REMOTE" ]; then
  OUTPUT=$(git pull --rebase "$REMOTE" "$BRANCH" 2>&1)
  echo "Git:  $OUTPUT"
else
  echo "Git:  Repositório local (sem remote configurado)"
fi

PENDENCIAS="$SECOND_BRAIN_PATH/memory/context/pendencias.md"
if [ -f "$PENDENCIAS" ]; then
  echo ""
  echo "--- PENDÊNCIAS ---"
  cat "$PENDENCIAS"
fi

SESSIONS_DIR="$SECOND_BRAIN_PATH/memory/sessions"
if [ -d "$SESSIONS_DIR" ]; then
  LAST_SESSION=$(ls "$SESSIONS_DIR"/*.md 2>/dev/null | sort | tail -1)
  if [ -n "$LAST_SESSION" ]; then
    SESSION_DATE=$(basename "$LAST_SESSION" .md)
    echo ""
    echo "--- ÚLTIMA SESSÃO ($SESSION_DATE) ---"
    cat "$LAST_SESSION"
  fi
fi
