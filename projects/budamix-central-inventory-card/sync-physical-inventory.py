#!/usr/bin/env python3
"""
Sync physical inventory snapshot from Google Sheets (aba ESTOQUE) → Supabase.

Reads aba ESTOQUE da PLANILHA DE ESTOQUE / PRECIFICAÇÃO (1u74a...):
  Col A = qty no galpão
  Col B = SKU base
  Col D = custo unitário
  Col H = custo total da linha (=A*D, mas pode ter #ERROR! ou vazio)

Soma:
  total_qty   = Σ col A (qty no galpão)
  total_cost  = Σ (col A × col D) — recalcula no Python para evitar #ERROR! da col H
  sku_count   = SKUs base únicos com qty > 0

Upsert single-row em physical_inventory_summary (id=1).

Cron: 0,30 * * * * via /root/scripts/sync-physical-inventory-cron.sh
"""

import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

SPREADSHEET_ID = "1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI"
SHEET_RANGE = "ESTOQUE!A4:H500"
SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_SERVICE_KEY = os.environ.get(
    "SUPABASE_SERVICE_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNxYmtvcHJjbW56bm16Yndkcm1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDM4MDQxNCwiZXhwIjoyMDg5OTU2NDE0fQ.-sTaIitEplNoBbW8U5nBHIjAlsIe20ImZ3SkLs17i6A",
)


def parse_number(value):
    """Parse cell value to float. Handles R$, BR/US decimals, errors, blanks. Returns None if invalid."""
    if value is None:
        return None
    s = str(value).strip()
    if not s or s.startswith("#"):
        return None
    s = s.replace("R$", "").strip()
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def parse_int(value):
    n = parse_number(value)
    if n is None:
        return None
    return int(n)


def read_sheet():
    result = subprocess.run(
        ["gog", "sheets", "get", SPREADSHEET_ID, SHEET_RANGE, "--json", "--results-only"],
        capture_output=True, text=True, timeout=30,
    )
    if result.returncode != 0:
        print(f"  ⚠️ gog error: {result.stderr.strip()}")
        return []
    try:
        data = json.loads(result.stdout)
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "values" in data:
            return data["values"]
        return []
    except json.JSONDecodeError:
        print("  ⚠️ JSON parse error")
        return []


def upsert_summary(total_qty, total_cost, sku_count):
    url = f"{SUPABASE_URL}/rest/v1/physical_inventory_summary?on_conflict=id"
    headers = {
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "apikey": SUPABASE_SERVICE_KEY,
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    }
    payload = [{
        "id": 1,
        "total_qty": total_qty,
        "total_cost": round(total_cost, 2),
        "sku_count": sku_count,
        "last_synced": datetime.now(timezone.utc).isoformat(),
    }]
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
    try:
        urllib.request.urlopen(req, timeout=20)
        return True
    except Exception as e:
        print(f"  ❌ Supabase upsert error: {e}")
        return False


def main():
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] Physical inventory sync starting")
    print(f"  Spreadsheet: {SPREADSHEET_ID}")
    print(f"  Range: {SHEET_RANGE}")

    rows = read_sheet()
    if not rows:
        print("  ⚠️ Nenhuma linha lida. Abortando.")
        sys.exit(1)

    total_qty = 0
    total_cost = 0.0
    skus = set()
    rows_with_sku = 0
    rows_with_cost = 0

    for row in rows:
        if not isinstance(row, list) or len(row) < 2:
            continue
        sku = str(row[1]).strip() if len(row) > 1 and row[1] else ""
        qty = parse_int(row[0]) if len(row) > 0 else None
        unit_cost = parse_number(row[3]) if len(row) > 3 else None

        if not sku:
            continue
        rows_with_sku += 1

        if qty is None:
            qty = 0
        if unit_cost is None:
            unit_cost = 0.0
        else:
            rows_with_cost += 1

        line_cost = qty * unit_cost

        total_qty += qty
        total_cost += line_cost
        if qty > 0:
            skus.add(sku)

    sku_count = len(skus)
    print(f"  Rows lidas: {len(rows)}, com SKU: {rows_with_sku}, com custo: {rows_with_cost}")
    print(f"  Total qty: {total_qty}")
    print(f"  Total cost: R$ {total_cost:,.2f}")
    print(f"  SKUs únicos com qty>0: {sku_count}")

    if upsert_summary(total_qty, total_cost, sku_count):
        print(f"✅ Snapshot atualizado em physical_inventory_summary")
    else:
        print(f"❌ Falha no upsert")
        sys.exit(2)

    print(f"[{datetime.now(timezone.utc).isoformat()}] Physical inventory sync done")


if __name__ == "__main__":
    main()
