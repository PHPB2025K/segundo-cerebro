#!/usr/bin/env bash
# safe-write.sh — protocolo Git seguro para o segundo-cerebro
#
# Coordena escritas no vault entre Claude Code local e o Kobe na VPS,
# evitando corrida e rebase em base velha.
#
# Uso:
#   safe-write.sh sync                 # só pull --rebase (antes de escrever)
#   safe-write.sh commit "<mensagem>"  # add+commit+pull+push (depois de escrever)
#
# Lockfile: /tmp/segundo-cerebro-local.lock.d (mkdir atômico, timeout 30s)
# Em conflito: aborta rebase, sai com erro 2 e mensagem clara.

set -euo pipefail

VAULT="${VAULT:-$HOME/segundo-cerebro}"
LOCK_DIR="/tmp/segundo-cerebro-local.lock.d"
LOCK_TIMEOUT_SEC=30

usage() {
  echo "Uso: $0 {sync|commit '<msg>'}"
  exit 64
}

[ $# -ge 1 ] || usage
ACTION="$1"

cd "$VAULT"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
  echo "ERROR: $VAULT não é repositório git" >&2
  exit 1
}

acquire_lock() {
  local waited=0
  while ! mkdir "$LOCK_DIR" 2>/dev/null; do
    if [ "$waited" -ge "$LOCK_TIMEOUT_SEC" ]; then
      echo "ERROR: outro safe-write em andamento (${LOCK_DIR} preso há >${LOCK_TIMEOUT_SEC}s)" >&2
      echo "Se tiver certeza que não há outra escrita, remova: rmdir $LOCK_DIR" >&2
      exit 3
    fi
    sleep 1
    waited=$((waited + 1))
  done
  echo "$$" > "$LOCK_DIR/pid"
  trap 'rm -rf "$LOCK_DIR"' EXIT INT TERM
}

acquire_lock

do_pull() {
  if ! git pull --rebase origin main; then
    echo "ERROR: pull --rebase falhou — conflito" >&2
    git rebase --abort >/dev/null 2>&1 || true
    echo "Rebase abortado. Resolva manualmente antes de tentar de novo." >&2
    exit 2
  fi
}

case "$ACTION" in
  sync)
    do_pull
    echo "✓ vault em $(git rev-parse --short HEAD) (sincronizado)"
    ;;

  commit)
    [ $# -ge 2 ] || { echo "ERROR: falta mensagem de commit" >&2; usage; }
    MSG="$2"

    if [ -z "$(git status --porcelain)" ]; then
      echo "✓ nada local para commitar"
      do_pull
      exit 0
    fi

    git add -A
    git -c user.email=pehpbroglio@gmail.com -c user.name="Pedro Broglio" \
      commit -m "$MSG"

    do_pull

    if ! git push origin main; then
      echo "ERROR: push falhou — verificar conexão/credenciais" >&2
      exit 4
    fi

    echo "✓ commit + push OK ($(git rev-parse --short HEAD))"
    ;;

  *)
    usage
    ;;
esac
