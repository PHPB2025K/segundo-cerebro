-- Migration: physical_inventory_items
-- Tabela SKU-level do estoque físico (galpão). Complementa physical_inventory_summary
-- (que é o snapshot agregado, mantido pra retrocompatibilidade dos cards).
--
-- Populada pelo cron sync-physical-inventory.py (a cada 30min) lendo a aba ESTOQUE da
-- planilha de precificação. Quando Fase 2 entrar (movimentações), qty passa a ser
-- atualizada por triggers de physical_movements.

CREATE TABLE IF NOT EXISTS physical_inventory_items (
  sku TEXT PRIMARY KEY,
  description TEXT,
  qty INTEGER NOT NULL DEFAULT 0,
  unit_cost NUMERIC(10,2) NOT NULL DEFAULT 0,
  total_cost NUMERIC(12,2) GENERATED ALWAYS AS (qty * unit_cost) STORED,
  ean TEXT,
  ncm TEXT,
  brand TEXT,
  last_synced TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_physical_inventory_items_brand ON physical_inventory_items(brand);
CREATE INDEX IF NOT EXISTS idx_physical_inventory_items_qty ON physical_inventory_items(qty) WHERE qty > 0;

-- Habilita Realtime para que o frontend receba updates em tempo real
-- (quando cron rodar 30min ou movimentação for registrada na Fase 2)
ALTER PUBLICATION supabase_realtime ADD TABLE physical_inventory_items;
