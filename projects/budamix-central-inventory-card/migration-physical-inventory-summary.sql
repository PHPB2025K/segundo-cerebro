-- Migration: physical_inventory_summary
-- Snapshot do estoque físico (galpão Pedreira-SP) populado pelo cron sync-physical-inventory.py
-- Single-row pattern (id=1 forçado) — sempre 1 registro com snapshot atual.

CREATE TABLE IF NOT EXISTS physical_inventory_summary (
  id INTEGER PRIMARY KEY DEFAULT 1 CHECK (id = 1),
  total_qty INTEGER NOT NULL DEFAULT 0,
  total_cost NUMERIC(12,2) NOT NULL DEFAULT 0,
  sku_count INTEGER NOT NULL DEFAULT 0,
  last_synced TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO physical_inventory_summary (id, total_qty, total_cost, sku_count)
VALUES (1, 0, 0, 0)
ON CONFLICT (id) DO NOTHING;

-- Habilita Realtime para que o frontend receba updates automáticos quando o cron rodar
ALTER PUBLICATION supabase_realtime ADD TABLE physical_inventory_summary;
