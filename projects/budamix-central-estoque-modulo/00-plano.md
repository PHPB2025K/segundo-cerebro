---
title: "Módulo Estoque Dedicado — Plano"
created: 2026-04-30
type: plan
status: active
tags:
  - project
  - budamix-central
  - estoque
  - dashboard
  - plano
---

# Módulo Estoque Dedicado — Budamix Central

## Visão geral

Transformar `/estoque` num hub com 3 sub-rotas, abrir caminho para gestão de movimentações (entrada/saída) substituindo gradualmente o preenchimento manual da planilha pelos analistas.

```
/estoque                       ← HUB (tabs no topo)
  ├ /estoque/full              ← módulo atual (Visão Geral / Reposição / Histórico) — MOVIDO
  ├ /estoque/fisico            ← NOVO: galpão Pedreira-SP, tabela de SKUs + movimentações
  └ /estoque/consolidado       ← NOVO: 3 cards FULL/FÍSICO/TOTAL (movidos da home) + gráficos
```

**Cards da home:** removidos. Movem para `/estoque/consolidado`.

**Movimentações:** estrutura preparada desde o início. Implementação real em fases.

## Princípios

1. **Não tocar no Full atual** — só mover de path. Lógica/componentes intactos.
2. **Planilha continua fonte de verdade do CADASTRO** (SKU base, custo unitário).
3. **Supabase passa a ser fonte de verdade da QUANTIDADE em galpão** — movimentações pelo app.
4. **Sync de mão dupla com planilha** — quando movimentação é registrada no app, opcional escrever na planilha via gspread.
5. **Cada fase é independente** — pode parar em qualquer ponto.

## Faseamento

| Fase | O que entrega | Tempo | Dependência |
|------|--------------|-------|-------------|
| **1** | Refactor rotas + tabela items + páginas read-only + remove cards home | ~2h | — |
| **2** | Form manual de movimentação + tabela movements + sync app→planilha | ~3h | Fase 1 |
| **3** | Import via planilha template CSV/XLSX (batch movimentações) | ~3-4h | Fase 2 |
| **4** | Import via PDF com Claude Vision (OCR/extraction) | ~5-7h | Fase 3 |

Hoje: planejamos as 4 fases, executamos **só a Fase 1** (depois Pedro decide quando avançar).

---

## FASE 1 — Refactor + Páginas Read-Only

### 1.1 Schema Supabase

Migration nova `00X_physical_inventory_items.sql`:

```sql
-- Tabela SKU-level do estoque físico (galpão)
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

-- Habilita Realtime
ALTER PUBLICATION supabase_realtime ADD TABLE physical_inventory_items;
```

> Mantém `physical_inventory_summary` (snapshot agregado já existente). Items é granular.

### 1.2 Sync expandido

Patch em `/root/.openclaw/workspace/scripts/sync-physical-inventory.py`:
- Continua populando `physical_inventory_summary` (sem mudança)
- ADICIONA: para cada linha da planilha com SKU base, upsert em `physical_inventory_items`:
  - `sku` ← col B
  - `description` ← col C
  - `qty` ← col A (parse_int corrigido)
  - `unit_cost` ← col D
  - `ean` ← col E
  - `ncm` ← col F
  - `brand` ← col G
  - `last_synced` ← agora

> Defesas (cross-check col H + sanity bound) já aplicadas continuam funcionando.

### 1.3 Refactor de rotas

**Antes:**
```
src/app/(dashboard)/estoque/page.tsx  ← módulo Full
```

**Depois:**
```
src/app/(dashboard)/estoque/
  layout.tsx            ← header com tabs (Full / Físico / Consolidado)
  page.tsx              ← redirect pra /estoque/full
  full/page.tsx         ← MOVE arquivo atual
  fisico/page.tsx       ← NOVO: lista SKU-level read-only
  consolidado/page.tsx  ← NOVO: 3 cards + métricas
```

`layout.tsx`:
- Header com nome "Estoque" + 3 tabs (link visual ativa por pathname)
- `<Outlet>`/`{children}` renderiza a sub-rota
- Estilo consistente com módulo Live Sales (tabs no topo)

`page.tsx`:
- `redirect("/estoque/full")` — mantém URL antiga funcional

`full/page.tsx`:
- Conteúdo atual de `/estoque/page.tsx` (todos os imports preservados, sem mudança lógica)

`fisico/page.tsx`:
- KPIs no topo: qty total · valor total · SKUs com estoque · última atualização
- Tabela com colunas: SKU | Descrição | Qty | Custo Unit. | Custo Total | Marca | Última sync
- Filtros: marca (dropdown), busca por SKU/descrição, "só com estoque" toggle
- Sort por qualquer coluna
- Paginação client-side (113 SKUs, ok sem server-side)
- Botão `Registrar movimentação` (disabled na Fase 1, ativa na Fase 2)
- Botão `Importar planilha` (disabled na Fase 1, ativa na Fase 3)

`consolidado/page.tsx`:
- 3 cards `InventoryValueCards` (movidos da home)
- Gráfico: distribuição % FULL vs FÍSICO (donut)
- Gráfico: top 10 SKUs por valor de estoque (FULL + FÍSICO somados)
- Card: "Capital total imobilizado" com tendência se houver histórico

### 1.4 API routes

**Nova:** `src/app/api/inventory-physical/route.ts`
```ts
GET → retorna lista de physical_inventory_items
- query params opcionais: ?brand=GB&search=KIT&minQty=1
- requireAuth
- ordenação default: qty DESC
```

**Existente:** `src/app/api/inventory-summary/route.ts` — sem mudança (já alimenta os cards).

### 1.5 Hooks

**Novo:** `src/hooks/use-physical-inventory.ts`
- `useQuery(["physical-inventory"], fetchItems)`
- Realtime: `physical_inventory_items` channel postgres_changes
- `refetchInterval: 60_000`, `staleTime: 30_000`
- Padrão idêntico ao `use-inventory.ts`

### 1.6 Componentes

- `src/components/inventory/physical-inventory-table.tsx` — tabela com filtros + sort
- `src/components/inventory/physical-inventory-kpis.tsx` — 4 KPIs no topo da página
- `src/components/inventory/inventory-tabs.tsx` — header com tabs (usado no layout)
- `src/components/inventory/consolidated-overview.tsx` — composição da página /consolidado

### 1.7 Remover cards da home

`src/app/(dashboard)/page.tsx`:
- Remove `<InventoryValueCards />` do `DashboardData`
- Remove import
- O componente em si NÃO é deletado — vai ser reutilizado em `/estoque/consolidado`

### 1.8 Critério de aceite Fase 1

| Validação | Como medir |
|-----------|-----------|
| `/estoque` redireciona pra `/estoque/full` | curl segue 307→200 |
| Full intacto | KPI Valor Custo continua R$ 157.723, filtros funcionam |
| `/estoque/fisico` lista 97+ SKUs | tabela popula |
| Total custo físico bate | Σ tabela = R$ 552.191 (igual snapshot) |
| `/estoque/consolidado` mostra 3 cards | igual home anterior |
| Home não tem mais cards inventário | layout limpo |
| Sem erro JS no console | F12 limpo |

---

## FASE 2 — Movimentações manuais (estrutura + UX)

### 2.1 Schema

```sql
CREATE TABLE IF NOT EXISTS physical_movements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  sku TEXT NOT NULL REFERENCES physical_inventory_items(sku),
  type TEXT NOT NULL CHECK (type IN ('entrada', 'saida', 'ajuste')),
  qty INTEGER NOT NULL,                  -- positivo sempre; type define direção
  reason TEXT,                           -- "Recebimento container GB25012", "Envio FBA Amazon", etc
  reference TEXT,                        -- ID externo (container, NF, etc)
  user_id UUID REFERENCES auth.users(id),
  user_email TEXT,
  source TEXT NOT NULL DEFAULT 'manual', -- 'manual' | 'csv_import' | 'pdf_import'
  applied_to_sheet BOOLEAN DEFAULT FALSE,-- se foi escrito na planilha
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_movements_sku ON physical_movements(sku);
CREATE INDEX IF NOT EXISTS idx_movements_created ON physical_movements(created_at DESC);

-- Trigger: atualizar qty em physical_inventory_items quando inserir movimento
CREATE OR REPLACE FUNCTION apply_physical_movement()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.type = 'entrada' THEN
    UPDATE physical_inventory_items SET qty = qty + NEW.qty, last_synced = NOW() WHERE sku = NEW.sku;
  ELSIF NEW.type = 'saida' THEN
    UPDATE physical_inventory_items SET qty = qty - NEW.qty, last_synced = NOW() WHERE sku = NEW.sku;
  ELSIF NEW.type = 'ajuste' THEN
    UPDATE physical_inventory_items SET qty = NEW.qty, last_synced = NOW() WHERE sku = NEW.sku;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER on_physical_movement AFTER INSERT ON physical_movements
  FOR EACH ROW EXECUTE FUNCTION apply_physical_movement();
```

### 2.2 UX

`/estoque/fisico` ganha:
- Botão `+ Registrar movimentação` no header da tabela
- Modal com form: SKU (autocomplete) | Tipo (entrada/saída/ajuste) | Qty | Motivo | Referência opcional
- Validação: qty > 0; saída não pode passar qty atual
- Sub-tab `Histórico` na própria página: lista de `physical_movements` recentes (últimos 50)
- Cada movimento mostra: data/hora · usuário · tipo · qty · SKU · motivo · status (✓ aplicado / ⚠ pendente sync planilha)

### 2.3 Sync app → planilha (opcional, defaultativado)

- Quando movimento é inserido, função SQL aplica em `physical_inventory_items` (já garante coerência interna)
- Job assíncrono (cron 5min) lê movements com `applied_to_sheet=false` e atualiza col A da planilha via `gspread`
- Marca `applied_to_sheet=true`
- Se falhar, fica pendente e tenta de novo na próxima rodada
- Sanity check: o sync-physical-inventory continua rodando 30min e fazendo cross-check

### 2.4 Permissões

- `admin`: pode registrar/excluir movimentações
- `viewer`: só visualiza tabela e histórico

### 2.5 Critério de aceite Fase 2

- Form abre, valida, persiste movimento
- qty em `physical_inventory_items` reflete movimento imediatamente
- Histórico mostra movimento na sub-tab
- Após cron de 5min, planilha tem qty atualizada (col A)
- Sanity check do sync 30min continua [OK]

---

## FASE 3 — Import via planilha template

### 3.1 Template padrão

Definir CSV/XLSX simples:
```csv
sku,type,qty,reason,reference
KIT2YW1520,entrada,500,Recebimento GB25012,GB25012
KIT4YW800SQ,saida,30,Envio FBA Amazon,SHIP-2026-04-30-A
```

Disponibilizar download do template na própria página `/estoque/fisico`.

### 3.2 Fluxo de import

1. Usuário clica `Importar planilha`
2. Modal: drag-and-drop CSV/XLSX
3. Backend valida cada linha:
   - SKU existe em `physical_inventory_items`?
   - Type é válido?
   - Qty > 0?
   - Saída não passa qty atual?
4. Preview com erros destacados (linhas inválidas em vermelho)
5. Botão "Confirmar import" → cria N movimentações em batch (source='csv_import')
6. Trigger atualiza qty automaticamente

### 3.3 Tech

- Parse: `papaparse` (CSV) ou `xlsx` (Excel)
- Server side validation completa antes de aplicar
- Transação: ou aplica tudo, ou nada (BEGIN/COMMIT/ROLLBACK)

### 3.4 Critério de aceite Fase 3

- Download template funciona
- Upload de arquivo válido aplica todas as linhas
- Upload de arquivo inválido mostra erros antes de aplicar (sem persistir nada)
- 100 linhas em batch leva < 3s

---

## FASE 4 — Import via PDF (futuro)

### 4.1 Conceito

PDF com formato padrão (template Budamix):
- Cabeçalho: data, tipo (entrada/saída), referência (container, NF, etc)
- Tabela: SKU · Qty
- (Opcional) descrição

Backend usa Claude Vision API (Anthropic) para extrair tabela do PDF como structured JSON, depois mesma pipeline da Fase 3 (validação + batch).

### 4.2 Tech

- `anthropic` SDK Python ou JS
- `claude-sonnet-4-7` com vision
- Prompt estruturado: "Extraia SKUs e quantidades desta nota de movimentação"
- Fallback manual se IA falhar (mostrar PDF + form pre-populado pra revisão)

### 4.3 Custo estimado

- ~R$ 0,02-0,05 por PDF processado (ordem de grandeza Claude API)
- Volume estimado: 5-15 PDFs/semana → < R$ 1/mês

### 4.4 Quando implementar

Depois das Fases 1-3 estabilizadas e analista validar fluxo manual. Sem urgência.

---

## Decisões finais (30/04 noite)

1. **Role `operator`** — criar role intermediária entre `viewer` e `admin`. Lucas/Yasmin/Leonardo permanecem `viewer` por enquanto; quando começarem a registrar movimentação no app, Pedro promove pra `operator`. Permissões:
   - `viewer`: só lê
   - `operator`: lê + registra movimentações
   - `admin`: tudo + estornar movimentações + gerenciar usuários
2. **Sem DELETE de movimento** — admin estorna criando contramovimento (preserva histórico). Schema NÃO tem policy de DELETE em `physical_movements`.
3. **Cron sync app→planilha: 2 minutos** (não 5). Mais responsivo. Job lê movimentos com `applied_to_sheet=false` e atualiza col A da planilha via `gspread`.

## Próximo passo

Mensagem pro Kobe executar Fase 1 (auditoria + implementação completa).
