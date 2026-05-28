-- Fase 1 — Livro auditável de movimentações de estoque GB
-- Seguro por desenho: estas tabelas NÃO atualizam a aba ESTOQUE nem qualquer saldo automaticamente.
-- Aplicar no Supabase SQL Editor ou via CLI: supabase db push / psql, conforme o ambiente.

create extension if not exists pgcrypto;

create table if not exists public.stock_movements (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),

  source_type text not null check (source_type in (
    'marketplace',
    'atacado_whatsapp',
    'full_sheet',
    'whatsapp_estoque',
    'whatsapp_devolucoes',
    'import_hub',
    'manual_audit',
    'manual_app',
    'unknown'
  )),
  source_channel text,
  source_message_id text,
  external_event_id text,

  movement_type text not null check (movement_type in ('entrada', 'saida', 'transferencia', 'ajuste')),
  status text not null default 'recebido' check (status in (
    'recebido',
    'pendente_interpretacao',
    'pendente_validacao',
    'validado',
    'aplicado',
    'rejeitado',
    'duplicado',
    'divergente',
    'erro'
  )),

  sku_raw text not null,
  sku_resolved text,
  product_name_raw text,
  quantity numeric(14,3) not null check (quantity > 0),
  unit text not null default 'un',

  location_from text,
  location_to text,
  responsible_name text,
  validator_name text,
  validated_at timestamptz,
  applied_at timestamptz,
  error_reason text,
  notes text,

  raw_payload jsonb not null default '{}'::jsonb,
  normalized_payload jsonb not null default '{}'::jsonb,

  constraint stock_movements_validated_requires_validator
    check (validated_at is null or validator_name is not null),
  constraint stock_movements_applied_requires_validated
    check (applied_at is null or status = 'aplicado')
);

comment on table public.stock_movements is
  'Fase 1: ledger auditável de movimentações. Não aplica saldo nem escreve na planilha ESTOQUE automaticamente.';
comment on column public.stock_movements.external_event_id is
  'Chave de idempotência por fonte. Use junto com source_type para evitar duplicidade de evento externo.';
comment on column public.stock_movements.applied_at is
  'Reservado para fases futuras. Fase 1 não deve popular automaticamente.';

create unique index if not exists ux_stock_movements_source_event
  on public.stock_movements (source_type, external_event_id)
  where external_event_id is not null;

create index if not exists ix_stock_movements_created_at
  on public.stock_movements (created_at desc);
create index if not exists ix_stock_movements_status
  on public.stock_movements (status, created_at desc);
create index if not exists ix_stock_movements_sku_resolved
  on public.stock_movements (sku_resolved);
create index if not exists ix_stock_movements_sku_raw
  on public.stock_movements (sku_raw);

create table if not exists public.stock_movement_evidences (
  id uuid primary key default gen_random_uuid(),
  movement_id uuid not null references public.stock_movements(id) on delete cascade,
  created_at timestamptz not null default now(),
  media_type text not null check (media_type in ('foto', 'pdf', 'audio', 'texto', 'planilha', 'link', 'outro')),
  url_or_storage_key text,
  ocr_text text,
  parsed_payload jsonb not null default '{}'::jsonb,
  notes text
);

create index if not exists ix_stock_movement_evidences_movement
  on public.stock_movement_evidences (movement_id, created_at desc);

create table if not exists public.sku_aliases (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  alias_raw text not null,
  sku text not null,
  confidence numeric(5,4) not null default 0.5 check (confidence >= 0 and confidence <= 1),
  source text not null default 'manual',
  active boolean not null default true,
  notes text
);

create unique index if not exists ux_sku_aliases_alias_active
  on public.sku_aliases (lower(alias_raw))
  where active = true;
create index if not exists ix_sku_aliases_sku
  on public.sku_aliases (sku);

create table if not exists public.kit_bom (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  kit_sku text not null,
  component_sku text not null,
  component_qty numeric(14,3) not null check (component_qty > 0),
  active boolean not null default true,
  valid_from date not null default current_date,
  valid_to date,
  notes text,
  constraint kit_bom_valid_range check (valid_to is null or valid_to >= valid_from)
);

create unique index if not exists ux_kit_bom_active_component
  on public.kit_bom (kit_sku, component_sku)
  where active = true;
create index if not exists ix_kit_bom_component
  on public.kit_bom (component_sku);

-- stock_balances fica deliberadamente fora da Fase 1.
-- Motivo: a aba ESTOQUE segue como saldo final operacional, e o novo ledger ainda não aplica movimentos.
-- Criar stock_balances na Fase 2, junto com regras explícitas de aplicação/conciliação e sync controlado.
