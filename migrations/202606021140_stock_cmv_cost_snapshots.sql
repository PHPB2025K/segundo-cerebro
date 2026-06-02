-- Fase CMV-1 — snapshots de custo para CMV oficial por período
-- Seguro por desenho: cria estrutura financeira auditável; não recalcula histórico e não altera saldos.

create extension if not exists pgcrypto;

create table if not exists public.stock_cost_layers (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),

  sku text not null,
  product_name text,

  source_type text not null check (source_type in (
    'opening_balance',
    'spreadsheet_cost',
    'import_hub',
    'purchase_invoice',
    'manual_adjustment',
    'recalculation',
    'unknown'
  )),
  source_ref text,
  source_date date,

  quantity_original numeric(14,3),
  quantity_remaining numeric(14,3),
  unit_cost_brl numeric(14,6) not null check (unit_cost_brl >= 0),
  total_cost_brl numeric(14,2),

  costing_method text not null default 'weighted_average' check (costing_method in (
    'weighted_average',
    'fifo_layer',
    'manual_fixed',
    'unknown'
  )),

  status text not null default 'active' check (status in ('active', 'superseded', 'exhausted', 'rejected')),
  validated_by text,
  validated_at timestamptz,
  notes text,

  raw_payload jsonb not null default '{}'::jsonb
);

comment on table public.stock_cost_layers is
  'Camadas/fontes de custo por SKU. Base para custo médio ponderado agora e FIFO por lote/container no futuro.';
comment on column public.stock_cost_layers.unit_cost_brl is
  'Custo unitário em reais validado para o SKU na fonte indicada. Deve representar custo landed quando disponível.';

create index if not exists ix_stock_cost_layers_sku_status
  on public.stock_cost_layers (sku, status, source_date desc nulls last, created_at desc);
create index if not exists ix_stock_cost_layers_source
  on public.stock_cost_layers (source_type, source_ref);

create table if not exists public.stock_movement_cost_snapshots (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),

  movement_id uuid not null references public.stock_movements(id) on delete restrict,
  cost_layer_id uuid references public.stock_cost_layers(id) on delete restrict,

  movement_business_date date not null,
  sku text not null,
  quantity numeric(14,3) not null check (quantity > 0),

  unit_cost_brl numeric(14,6) not null check (unit_cost_brl >= 0),
  total_cost_brl numeric(14,2) not null check (total_cost_brl >= 0),

  costing_method text not null check (costing_method in (
    'weighted_average',
    'fifo_layer',
    'manual_fixed',
    'unknown'
  )),
  cost_source_type text not null check (cost_source_type in (
    'stock_cost_layers',
    'spreadsheet_cost',
    'import_hub',
    'purchase_invoice',
    'manual_adjustment',
    'opening_balance',
    'unknown'
  )),
  cost_source_ref text,

  cmv_category text not null check (cmv_category in (
    'venda_marketplace',
    'venda_atacado',
    'perda_avaria',
    'ajuste_negativo',
    'devolucao_reversa',
    'nao_cmv_transferencia'
  )),

  marketplace text check (marketplace in ('mercado_livre', 'shopee', 'amazon', 'atacado', 'outro') or marketplace is null),
  order_id text,
  order_item_id text,

  gross_revenue_brl numeric(14,2),
  revenue_source_ref text,

  is_official boolean not null default true,
  correction_of_snapshot_id uuid references public.stock_movement_cost_snapshots(id) on delete restrict,
  notes text,
  raw_payload jsonb not null default '{}'::jsonb,

  constraint stock_movement_cost_snapshots_total_matches
    check (abs(total_cost_brl - round((quantity * unit_cost_brl)::numeric, 2)) <= 0.02),
  constraint stock_movement_cost_snapshots_correction_requires_notes
    check (correction_of_snapshot_id is null or notes is not null)
);

comment on table public.stock_movement_cost_snapshots is
  'Snapshot imutável de custo gerado quando movimento aplicado consome ou reverte estoque. Fonte oficial para CMV por período.';
comment on column public.stock_movement_cost_snapshots.movement_business_date is
  'Data de competência do CMV: pedido aprovado/faturado, perda validada ou ajuste aplicado. Não usar created_at técnico como única referência.';
comment on column public.stock_movement_cost_snapshots.cmv_category is
  'Separa venda de perda/avaria e impede tratar transferência Full como CMV comercial.';
comment on column public.stock_movement_cost_snapshots.is_official is
  'Somente snapshots oficiais entram nos relatórios finais; snapshots de teste/reprocessamento podem ficar false.';

create unique index if not exists ux_stock_movement_cost_snapshot_official_component
  on public.stock_movement_cost_snapshots (movement_id, sku, cmv_category)
  where is_official = true and correction_of_snapshot_id is null;

create index if not exists ix_stock_movement_cost_snapshots_period
  on public.stock_movement_cost_snapshots (movement_business_date, cmv_category, marketplace);
create index if not exists ix_stock_movement_cost_snapshots_sku_period
  on public.stock_movement_cost_snapshots (sku, movement_business_date);
create index if not exists ix_stock_movement_cost_snapshots_order
  on public.stock_movement_cost_snapshots (marketplace, order_id, order_item_id);

create or replace view public.v_stock_cmv_official_lines as
select
  s.id as snapshot_id,
  s.created_at as snapshot_created_at,
  s.movement_id,
  m.source_type,
  m.source_channel,
  m.external_event_id,
  m.movement_type,
  m.status as movement_status,
  m.applied_at,
  s.movement_business_date,
  s.cmv_category,
  s.marketplace,
  s.order_id,
  s.order_item_id,
  s.sku,
  s.quantity,
  s.unit_cost_brl,
  s.total_cost_brl,
  s.costing_method,
  s.cost_source_type,
  s.cost_source_ref,
  s.gross_revenue_brl,
  case
    when s.gross_revenue_brl is null then null
    else round((s.gross_revenue_brl - s.total_cost_brl)::numeric, 2)
  end as gross_margin_brl,
  case
    when s.gross_revenue_brl is null or s.gross_revenue_brl = 0 then null
    else round(((s.gross_revenue_brl - s.total_cost_brl) / s.gross_revenue_brl * 100)::numeric, 2)
  end as gross_margin_pct,
  s.is_official
from public.stock_movement_cost_snapshots s
join public.stock_movements m on m.id = s.movement_id
where s.is_official = true
  and s.correction_of_snapshot_id is null;

comment on view public.v_stock_cmv_official_lines is
  'Linhas oficiais de CMV para filtros por período, marketplace, SKU e pedido.';

create or replace view public.v_stock_cmv_daily_summary as
select
  movement_business_date,
  cmv_category,
  marketplace,
  sku,
  count(distinct movement_id) as movement_count,
  count(distinct order_id) filter (where order_id is not null) as order_count,
  sum(quantity) as quantity,
  round(sum(total_cost_brl)::numeric, 2) as cmv_brl,
  round(sum(gross_revenue_brl)::numeric, 2) as gross_revenue_brl,
  case
    when sum(gross_revenue_brl) is null then null
    else round((sum(gross_revenue_brl) - sum(total_cost_brl))::numeric, 2)
  end as gross_margin_brl,
  case
    when sum(gross_revenue_brl) is null or sum(gross_revenue_brl) = 0 then null
    else round(((sum(gross_revenue_brl) - sum(total_cost_brl)) / sum(gross_revenue_brl) * 100)::numeric, 2)
  end as gross_margin_pct
from public.v_stock_cmv_official_lines
group by movement_business_date, cmv_category, marketplace, sku;

comment on view public.v_stock_cmv_daily_summary is
  'Resumo diário base. Semana/mês são filtros/agregações sobre esta view.';

create table if not exists public.stock_cmv_pending_costs (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  resolved_at timestamptz,
  movement_id uuid not null references public.stock_movements(id) on delete restrict,
  sku text not null,
  quantity numeric(14,3) not null check (quantity > 0),
  reason text not null,
  status text not null default 'open' check (status in ('open', 'resolved', 'ignored')),
  notes text
);

create unique index if not exists ux_stock_cmv_pending_costs_open
  on public.stock_cmv_pending_costs (movement_id, sku)
  where status = 'open';

comment on table public.stock_cmv_pending_costs is
  'Pendências financeiras: movimentos que consomem estoque mas ainda não têm custo confiável para CMV oficial.';
