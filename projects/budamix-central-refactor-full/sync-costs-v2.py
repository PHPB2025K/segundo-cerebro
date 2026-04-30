#!/usr/bin/env python3
"""
Sync cost prices from Google Sheets → Supabase fulfillment_inventory.cost_price.

Tabs & layout (after 2026-04-30 mapping refactor):

  ESTOQUE: SKU BASE col B (idx 1), CUSTO col D (idx 3), data starts row 8
  MELI:    SKU BASE col B (idx 1), SKU ANUNCIO col D (idx 3), data starts row 2
  SHOPEE:  SKU BASE col B (idx 1), SKU ANUNCIO col D (idx 3), data starts row 2
  AMAZON:  SKU BASE col B (idx 1), SKU ANUNCIO col D (idx 3), data starts row 2

Logic:
  1. Load cost_map from ESTOQUE: { SKU_BASE: CUSTO }
  2. Load mapping from each marketplace tab: { SKU_ANUNCIO: SKU_BASE }
  3. For each fulfillment_inventory row:
     - direct: if sku is itself a SKU_BASE in ESTOQUE → cost_map[sku]
     - via mapping: if sku is SKU_ANUNCIO in marketplace tab → cost_map[mapping[sku]]
     - else: skip (stays zero)
  4. Apply updates to Supabase (skip dry-run)

Cost is per product (SKU_BASE), not per platform/listing.

Usage: python3 sync-costs.py [--dry-run]
"""

import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

SPREADSHEET_ID = "1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU"
SUPABASE_URL = "https://sqbkoprcmnznmzbwdrmf.supabase.co"
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNxYmtvcHJjbW56bm16Yndkcm1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NDM4MDQxNCwiZXhwIjoyMDg5OTU2NDE0fQ.-sTaIitEplNoBbW8U5nBHIjAlsIe20ImZ3SkLs17i6A")

DRY_RUN = "--dry-run" in sys.argv

ESTOQUE_RANGE = "ESTOQUE!A8:K500"
ESTOQUE_BASE_IDX = 1
ESTOQUE_COST_IDX = 3

MARKETPLACE_TABS = [
    ("MELI", "ml", "MELI!A2:H300"),
    ("SHOPEE", "shopee", "SHOPEE!A2:H300"),
    ("AMAZON", "amazon", "AMAZON!A2:H300"),
]
MARKETPLACE_BASE_IDX = 1
MARKETPLACE_ANUNCIO_IDX = 3


def parse_cost(value):
    if value is None:
        return None
    s = str(value).strip()
    if not s:
        return None
    if s.startswith("#"):
        return None
    s = s.replace("R$", "").strip()
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        v = float(s)
    except ValueError:
        return None
    if v <= 0:
        return None
    return v


def read_sheet_range(range_str):
    result = subprocess.run(
        ["gog", "sheets", "get", SPREADSHEET_ID, range_str, "--json", "--results-only"],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"  ⚠️ gog error for {range_str}: {result.stderr.strip()}")
        return []
    try:
        data = json.loads(result.stdout)
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "values" in data:
            return data["values"]
        return []
    except json.JSONDecodeError:
        print(f"  ⚠️ JSON parse error for {range_str}")
        return []


def load_cost_map_from_estoque():
    rows = read_sheet_range(ESTOQUE_RANGE)
    cost_map = {}
    rows_read = len(rows)
    skus_seen = 0
    for row in rows:
        if not isinstance(row, list):
            continue
        if len(row) <= ESTOQUE_BASE_IDX:
            continue
        sku = str(row[ESTOQUE_BASE_IDX]).strip()
        if not sku:
            continue
        skus_seen += 1
        cost = parse_cost(row[ESTOQUE_COST_IDX]) if len(row) > ESTOQUE_COST_IDX else None
        if cost is None:
            continue
        if sku not in cost_map:
            cost_map[sku] = cost
    print(f"  ESTOQUE: {rows_read} rows, {skus_seen} SKUs base, {len(cost_map)} com custo")
    return cost_map


def load_mapping_from_marketplace(tab_name, range_str):
    rows = read_sheet_range(range_str)
    mapping = {}
    rows_read = len(rows)
    anuncios_seen = 0
    via_base = 0
    for row in rows:
        if not isinstance(row, list):
            continue
        base = ""
        if len(row) > MARKETPLACE_BASE_IDX and row[MARKETPLACE_BASE_IDX]:
            base = str(row[MARKETPLACE_BASE_IDX]).strip()
        anuncio = ""
        if len(row) > MARKETPLACE_ANUNCIO_IDX and row[MARKETPLACE_ANUNCIO_IDX]:
            anuncio = str(row[MARKETPLACE_ANUNCIO_IDX]).strip()
        if not anuncio:
            continue
        anuncios_seen += 1
        # Se base vazio, anuncio é o próprio base (caso comum: KIT2YW1520 listado direto)
        target = base if base else anuncio
        if base:
            via_base += 1
        if anuncio not in mapping:
            mapping[anuncio] = target
    print(f"  {tab_name}: {rows_read} rows, {anuncios_seen} anúncios, {via_base} com SKU base preenchido")
    return mapping


def resolve_cost(sku, platform, cost_map, mappings_by_platform):
    """Returns (cost, source) or (None, None)."""
    # Tenta direto (SKU base na ESTOQUE)
    if sku in cost_map:
        return cost_map[sku], "direct"
    # Tenta via mapping anuncio→base
    mapping = mappings_by_platform.get(platform, {})
    base = mapping.get(sku)
    if base and base in cost_map:
        return cost_map[base], f"via {base}"
    return None, None


def get_inventory():
    url = f"{SUPABASE_URL}/rest/v1/fulfillment_inventory?select=sku,platform,shop_id,cost_price,available_qty,unit_price"
    headers = {
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "apikey": SUPABASE_SERVICE_KEY,
    }
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=30)
    return json.loads(resp.read())


def build_updates(cost_map, mappings_by_platform, inventory):
    updates = []
    direct_count = 0
    via_mapping_count = 0
    for row in inventory:
        sku = row["sku"]
        platform = row["platform"]
        current_cost = row.get("cost_price") or 0
        new_cost, source = resolve_cost(sku, platform, cost_map, mappings_by_platform)
        if new_cost is None:
            continue
        if source == "direct":
            direct_count += 1
        else:
            via_mapping_count += 1
        if abs(new_cost - float(current_cost)) > 0.001:
            updates.append({
                "sku": sku,
                "platform": platform,
                "shop_id": row["shop_id"],
                "cost_price": new_cost,
                "_source": source,
            })
    return updates, direct_count, via_mapping_count


def apply_updates(updates):
    if not updates:
        print("")
        print("  Nenhum custo pra atualizar — tudo já tá correto.")
        return 0
    if DRY_RUN:
        print("")
        print(f"  [DRY RUN] {len(updates)} SKUs seriam atualizados:")
        for u in updates[:20]:
            src = u.get("_source", "")
            print(f"    {u['sku']} ({u['platform']}/{u['shop_id']}): → R$ {u['cost_price']:.2f}  [{src}]")
        if len(updates) > 20:
            print(f"    ... e mais {len(updates) - 20}")
        return len(updates)
    # Strip _source antes de enviar pro Supabase
    payload = [{k: v for k, v in u.items() if not k.startswith("_")} for u in updates]
    url = f"{SUPABASE_URL}/rest/v1/fulfillment_inventory?on_conflict=sku,platform,shop_id"
    headers = {
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "apikey": SUPABASE_SERVICE_KEY,
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        urllib.request.urlopen(req, timeout=30)
        return len(updates)
    except Exception as e:
        print(f"  ❌ Supabase upsert error: {e}")
        return 0


def print_coverage(inventory, updates):
    update_key = {(u["sku"], u["platform"], u.get("shop_id")): u["cost_price"] for u in updates}
    inv_unmatched = []
    for inv_row in inventory:
        sku = inv_row.get("sku")
        platform = inv_row.get("platform")
        shop_id = inv_row.get("shop_id")
        current_cost = inv_row.get("cost_price") or 0
        effective_cost = update_key.get((sku, platform, shop_id), float(current_cost))
        if not effective_cost or effective_cost <= 0:
            inv_unmatched.append({
                "sku": sku,
                "platform": platform,
                "shop_id": shop_id,
                "available_qty": inv_row.get("available_qty") or 0,
                "unit_price": inv_row.get("unit_price") or 0,
            })
    for u in inv_unmatched:
        u["potential_value"] = u["available_qty"] * u["unit_price"]
    inv_unmatched.sort(key=lambda x: x["potential_value"], reverse=True)
    total_inventory = len(inventory)
    with_cost = total_inventory - len(inv_unmatched)
    without_cost = len(inv_unmatched)
    total_potential = sum(u["potential_value"] for u in inv_unmatched)
    print("")
    print(f"[COVERAGE] {total_inventory} registros no inventario, {with_cost} com custo, {without_cost} sem custo")
    print(f"[COVERAGE] Valor venda potencial sem custo: R$ {total_potential:.2f}")
    print("[COVERAGE] Top 20 SKUs sem custo por valor potencial:")
    for u in inv_unmatched[:20]:
        sku = u["sku"]
        plat = u["platform"]
        shop = u["shop_id"]
        qty = u["available_qty"]
        val = u["potential_value"]
        print(f" {sku:25s} {plat:8s} {str(shop):12s} qty={qty:5d} R$ {val:10.2f}")


def main():
    ts = datetime.now(timezone.utc).isoformat()
    print(f"[{ts}] Sync costs starting {'(DRY RUN)' if DRY_RUN else ''}")
    print(f"  Spreadsheet: {SPREADSHEET_ID}")
    print("  Logic: ESTOQUE = cost_map (SKU_BASE → CUSTO); marketplaces = mapping (SKU_ANUNCIO → SKU_BASE)")
    print("")

    cost_map = load_cost_map_from_estoque()
    if not cost_map:
        print("  ⚠️ Nenhum custo encontrado em ESTOQUE. Abortando.")
        return

    mappings_by_platform = {}
    for tab_name, platform, range_str in MARKETPLACE_TABS:
        mapping = load_mapping_from_marketplace(tab_name, range_str)
        mappings_by_platform[platform] = mapping

    print("")
    print(f"  Cost map: {len(cost_map)} SKUs base com custo (ESTOQUE)")
    print(f"  Mappings: ml={len(mappings_by_platform.get('ml', {}))} shopee={len(mappings_by_platform.get('shopee', {}))} amazon={len(mappings_by_platform.get('amazon', {}))}")

    print("")
    print("  Buscando inventário no Supabase...")
    inventory = get_inventory()
    print(f"  {len(inventory)} registros no fulfillment_inventory")

    updates, direct_count, via_mapping_count = build_updates(cost_map, mappings_by_platform, inventory)
    total_resolved = direct_count + via_mapping_count
    print(f"  Resolvidos: {total_resolved} (direct={direct_count}, via_mapping={via_mapping_count})")

    updated = apply_updates(updates)
    print("")
    print(f"✅ {updated} registros atualizados com custo")

    print_coverage(inventory, updates)
    print("")
    print(f"[{datetime.now(timezone.utc).isoformat()}] Sync costs done")


if __name__ == "__main__":
    main()
