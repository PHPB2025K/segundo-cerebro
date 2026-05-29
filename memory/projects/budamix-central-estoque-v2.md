---
title: "Budamix Central — Módulo Estoque v2 (sem UI manual, físico tempo real)"
created: 2026-05-29
type: project-status
status: producao
project: budamix-central
tags:
  - budamix-central
  - estoque
  - producao
---

# Budamix Central — Módulo Estoque v2

> Decisão Pedro 29/05/2026: estoque vira 100% automatizado, sem UI de baixa manual.

## Mudanças aplicadas em 29/05/2026 14:20 BRT

### 1. Renomeação
- Sidebar: `"Estoque Full"` → **`"Estoque"`**
- Redirect index: `/estoque` agora vai pra `/estoque/fisico` (era `/estoque/full`)
- `/estoque/full` (Visão Geral / Reposição / Histórico) continua acessível como subpágina legada — não está mais no link default

### 2. Sync acelerado
- Cron `/root/scripts/sync-physical-inventory-cron.sh` agora roda **a cada 3 minutos** (era 0,30 = 30min)
- Script Python: `/root/.openclaw/workspace/scripts/sync-physical-inventory.py`
- Alvo: tabelas `physical_inventory_items` + `physical_inventory_summary`
- Latência aceitável: ≤ 3 min do save na planilha ESTOQUE até aparecer no painel

### 3. Botões manuais removidos
- "+ Registrar movimentação" e "Importar planilha" sumiram da `/estoque/fisico` (eram disabled na v1; agora deletados de vez)
- Subtítulo da página agora: "Galpão Pedreira-SP · sync automático a cada 3min"

### 4. Nova seção Movimentações (na mesma página /estoque/fisico)
- Componente `InventoryMovementsSection` em `/var/www/budamix-central/src/components/inventory/`
- Hook `useInventoryMovements` (React Query, refetch a cada 30s)
- Fonte: tabela `stock_movements` no Supabase Budamix Central
- KPIs do período: total, aplicados, divergentes, unidades aplicadas
- Filtros:
  - **Período**: Hoje / 7 dias / 30 dias / Sempre
  - **Status**: Todos / Aplicado / Divergente / Validado / Erro
  - **Origem**: ENVIOS FULL / Marketplace / WhatsApp Estoque / WhatsApp Devoluções / Atacado WhatsApp / Manual UI / Auditoria
  - **Busca SKU** (livre)
- Paginação 50 por página
- Tabela mostra: timestamp, SKU resolvido + SKU original se diferente, produto, tipo (↑↓↔⚙), qty, origem + canal, status badge + erro inline

### 5. API criada
- Rota: `GET /api/inventory-movements` (Budamix Central)
- Auth obrigatório via `requireAuth`
- Query params: `from`, `to`, `status`, `sourceType`, `channel`, `sku`, `limit`, `offset`
- Retorno: `{ items, pagination, kpis }`

## Arquitetura final do módulo

```
/estoque (redirect)
  └── /fisico  ← NOVO DEFAULT
       ├── Header: "Estoque Físico" + subtítulo sync
       ├── PhysicalInventoryKpis (qty total, valor, SKUs com estoque)
       ├── Card de filtros (busca, marca, "só com estoque")
       ├── PhysicalInventoryTable (saldo SKU a SKU)
       └── InventoryMovementsSection (NOVO)
            ├── KPIs do período
            ├── Filtros (período, status, origem, busca SKU)
            ├── Tabela paginada
            └── Refresh automático 30s
  ├── /full (legado, acessível mas não default)
  └── /consolidado (legado)
```

## Roadmap

- ✅ **Opção A (curto prazo)** — sync planilha→Supabase 3min (FEITO)
- ⏳ **Opção C (longo prazo)** — Supabase vira fonte de verdade do saldo (não planilha). Motor escreve no Supabase, planilha vira reflexo. Reduz latência pra zero e elimina dependência de Google Sheets.

## Próximas frentes pendentes

1. **WhatsApp Estoque parser** (b): ENTRADA/BAIXA via comando no grupo
2. **Cron marketplaces tempo real** (c): vendas pagas → baixa automática

## Validação live

- Build: OK (warnings TS em legados não relacionados)
- PM2 `budamix-central` restart pid 2920737, online
- `GET /api/inventory-movements` retorna 401 sem auth (rota existe) ✅
- Cron `*/3 * * * *` confirmado em crontab
- Smoke do sync rodou: `Items upserted: 94/94`

## Arquivos modificados/criados

| Arquivo | Mudança |
|---|---|
| `src/components/layout/sidebar.tsx` | Label "Estoque Full" → "Estoque" |
| `src/app/(dashboard)/estoque/page.tsx` | Redirect para `/fisico` em vez de `/full` |
| `src/app/(dashboard)/estoque/fisico/page.tsx` | Botões manuais removidos + `<InventoryMovementsSection />` adicionado |
| `src/app/api/inventory-movements/route.ts` | **NOVO** — GET com filtros |
| `src/hooks/use-inventory-movements.ts` | **NOVO** |
| `src/components/inventory/inventory-movements-section.tsx` | **NOVO** |
| `/etc/crontab` (root) | `0,30 * * * *` → `*/3 * * * *` |
