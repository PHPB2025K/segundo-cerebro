# Patch v3 — adicionar upsert em physical_inventory_items

Mantém TODA a lógica do v2 (parser corrigido + defesas cross-check + sanity bound).
ADICIONA: além de gravar em `physical_inventory_summary`, grava também em
`physical_inventory_items` (1 row por SKU). Sem remover nada.

## Onde patchar

Em `/root/.openclaw/workspace/scripts/sync-physical-inventory.py`:

### Adicionar nova função `upsert_items` antes de `def main()`

```python
def upsert_items(items):
    """Upsert lista de SKUs em physical_inventory_items."""
    if not items:
        return 0
    url = f"{SUPABASE_URL}/rest/v1/physical_inventory_items?on_conflict=sku"
    headers = {
        "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
        "apikey": SUPABASE_SERVICE_KEY,
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    }
    # Lote em chunks de 100 para não passar de tamanho de payload
    sent = 0
    BATCH = 100
    for i in range(0, len(items), BATCH):
        chunk = items[i:i+BATCH]
        req = urllib.request.Request(url, data=json.dumps(chunk).encode(), headers=headers, method="POST")
        try:
            urllib.request.urlopen(req, timeout=30)
            sent += len(chunk)
        except Exception as e:
            print(f"  ❌ Items upsert error (chunk {i}): {e}")
            return sent
    return sent
```

### No loop principal, coletar items e chamar upsert_items

Encontrar o bloco que monta os totais e adicionar coleta de items por SKU:

```python
# Antes (já existe):
total_qty = 0
total_cost = 0.0
col_h_total = 0.0
skus = set()
rows_with_sku = 0
rows_with_cost = 0

# ADICIONAR:
items_payload = []  # lista de dicts pra upsert em physical_inventory_items
items_seen = set()  # evitar duplicatas se planilha tiver SKU repetido

# No loop, dentro do `for row in rows:`, depois de calcular qty/cost:
description = str(row[2]).strip() if len(row) > 2 and row[2] else None
ean = str(row[4]).strip() if len(row) > 4 and row[4] else None
ncm = str(row[5]).strip() if len(row) > 5 and row[5] else None
brand = str(row[6]).strip() if len(row) > 6 and row[6] else None

if sku not in items_seen:
    items_seen.add(sku)
    items_payload.append({
        "sku": sku,
        "description": description,
        "qty": qty,
        "unit_cost": round(unit_cost, 2),
        "ean": ean,
        "ncm": ncm,
        "brand": brand,
        "last_synced": datetime.now(timezone.utc).isoformat(),
    })
```

### Antes do upsert do summary, chamar upsert dos items

```python
# Atual:
if upsert_summary(total_qty, total_cost, sku_count):
    print(f"✅ Snapshot atualizado em physical_inventory_summary")

# Mudar para:
items_sent = upsert_items(items_payload)
print(f"  Items upserted: {items_sent}/{len(items_payload)}")

if upsert_summary(total_qty, total_cost, sku_count):
    print(f"✅ Snapshot atualizado em physical_inventory_summary")
```

## Validação pós-patch

```sql
SELECT count(*) FROM physical_inventory_items;
-- Esperado: ~113 (todos SKUs base com algo na planilha)

SELECT sum(total_cost) FROM physical_inventory_items WHERE qty > 0;
-- Esperado: ~R$ 552.191 (mesmo do summary)

SELECT * FROM physical_inventory_items
ORDER BY total_cost DESC LIMIT 10;
-- Top SKUs de capital imobilizado
```
