#!/bin/bash
# Wrapper cron para sync-physical-inventory.py
# Cron: 0,30 * * * * /root/scripts/sync-physical-inventory-cron.sh

set -uo pipefail

export GOG_KEYRING_PASSWORD=$(cat /root/.openclaw/.gog-keyring-pass)
export GOG_ACCOUNT=gb.ai.agent@gbimportadora.com

LOG_DIR=/var/log/budamix-sync
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/physical-inventory-$(date +%Y%m%d).log"
SCRIPT=/root/.openclaw/workspace/scripts/sync-physical-inventory.py

echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting physical inventory sync" >> "$LOG_FILE"
timeout 60 python3 -u "$SCRIPT" >> "$LOG_FILE" 2>&1
EXIT=$?
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Physical inventory exit=$EXIT" >> "$LOG_FILE"
exit $EXIT
