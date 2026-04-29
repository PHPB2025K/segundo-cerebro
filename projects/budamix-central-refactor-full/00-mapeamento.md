---
title: "Budamix Central Refactor Full — 00 Mapeamento"
created: 2026-04-29
type: reference
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - mapeamento
---

# Budamix Central Refactor Full — 00 Mapeamento

Mapeamento read-only do módulo **Estoque Full** para orientar a Etapa 1 (auditoria das 3 Shopees) e Etapa 2 (KPI **Valor Custo** no header).

Escopo respeitado: leitura de código, logs e `SELECT`/REST read-only no Supabase. Não houve build, restart de PM2, alteração de código, `.env`, `.next`, nem escrita no banco.

---

## A — Estrutura do módulo Full (rotas e componentes)

### Rota principal

- Rota do app: `src/app/(dashboard)/estoque/page.tsx:153`
- URL funcional esperada: `/estoque`
- Sidebar aponta para essa rota: `src/components/layout/sidebar.tsx:47`
- A página é client component e carrega dados via `useInventory()`: `src/app/(dashboard)/estoque/page.tsx:48` e `src/app/(dashboard)/estoque/page.tsx:50`

### Hierarquia confirmada

Top-level tabs no header da página:

- **Visão Geral**: `src/app/(dashboard)/estoque/page.tsx:23`
- **Reposição**: `src/app/(dashboard)/estoque/page.tsx:25`
- **Histórico**: `src/app/(dashboard)/estoque/page.tsx:26`

Renderização das tabs:

- `overview` renderiza `InventoryOverview`: `src/app/(dashboard)/estoque/page.tsx:133`
- `restock` renderiza `RestockTab`: `src/app/(dashboard)/estoque/page.tsx:141`
- `history` renderiza `SalesHistoryTab`: `src/app/(dashboard)/estoque/page.tsx:143`

Dentro da **Visão Geral**, há filtros por marketplace:

- Todas / ML Full / Shopee Full / Amazon FBA: `src/components/inventory/inventory-overview.tsx:12`
- Subtabs Shopee aparecem só quando `platform === "shopee"`: `src/components/inventory/inventory-overview.tsx:149`
- Subtabs Shopee atuais: `Shopee 1`, `Shopee 2`, `Shopee 3`: `src/components/inventory/inventory-overview.tsx:19`
- IDs atuais das subtabs: `448649947`, `860803675`, `442066454`: `src/components/inventory/inventory-overview.tsx:21`

Existe também componente reutilizável de filtro com os mesmos shop_ids:

- `src/components/inventory/platform-filter.tsx:9`
- Helper de filtro por marketplace/shop: `src/components/inventory/platform-filter.tsx:124`
- Helper de contagem por marketplace/shop: `src/components/inventory/platform-filter.tsx:140`

### Cabeçalho e KPIs

Há dois “headers” relevantes:

1. **Header visual da página** — título `Estoque Full`, tabs e última sync:
   - Container: `src/app/(dashboard)/estoque/page.tsx:74`
   - Título: `src/app/(dashboard)/estoque/page.tsx:87`
   - Última sync: `src/app/(dashboard)/estoque/page.tsx:90`
   - Tabs top-level: `src/app/(dashboard)/estoque/page.tsx:105`

2. **Header/KPI cards da Visão Geral** — onde aparece **Valor Custo**:
   - `InventoryOverview` injeta KPI cards: `src/components/inventory/inventory-overview.tsx:93`
   - Componente dos cards: `src/components/inventory/inventory-kpis.tsx:117`
   - Card **Valor Custo**: `src/components/inventory/inventory-kpis.tsx:160`

### Árvore de arquivos do módulo

- `src/app/(dashboard)/estoque/page.tsx` — rota `/estoque`, header visual, 3 tabs top-level e wiring inicial do `useInventory`.
- `src/components/inventory/inventory-overview.tsx` — tab Visão Geral, filtros de marketplace/status/busca, subtabs Shopee e tabela.
- `src/components/inventory/inventory-kpis.tsx` — cards de KPIs, incluindo **Valor Venda** e **Valor Custo**.
- `src/components/inventory/inventory-table.tsx` — tabela de SKUs/estoque/cobertura.
- `src/components/inventory/platform-filter.tsx` — filtro reutilizável por marketplace e loja Shopee, usado em reposição/planejamento.
- `src/components/inventory/restock-tab.tsx` — tab Reposição com subtabs Recomendações, Planejados, Enviados, Recebidos.
- `src/components/inventory/restock-recommendations.tsx` — recomendações de reposição e filtros.
- `src/components/inventory/shipment-planner.tsx` — planejamentos de envio.
- `src/components/inventory/in-transit-list.tsx` — enviados/em trânsito.
- `src/components/inventory/shipment-history.tsx` — recebidos/histórico de envios.
- `src/components/inventory/restock-config-modal.tsx` — configuração de lead time/target.
- `src/components/inventory/sales-history.tsx` — tab Histórico.
- `src/hooks/use-inventory.ts` — query client-side `/api/inventory`, cache React Query e Realtime.
- `src/app/api/inventory/route.ts` — API server-side que lê `fulfillment_inventory`, calcula média de vendas e KPIs.
- `src/data/types-inventory.ts` — tipos do módulo.
- `src/data/mock-inventory.ts` — fallback/mock e função `computeInventoryKPIs`.

---

## B — Schema Supabase relevante

### `fulfillment_inventory`

Schema local versionado em migration:

- Criação da tabela: `supabase/migrations/003_inventory_module.sql:7`
- Índices: `supabase/migrations/003_inventory_module.sql:52`
- Constraint única: `supabase/migrations/003_inventory_module.sql:20`

Colunas versionadas:

| Coluna | Tipo | Observação |
|---|---:|---|
| `id` | `UUID` | PK, default `gen_random_uuid()` |
| `sku` | `TEXT` | obrigatório |
| `platform` | `TEXT` | check `ml`, `shopee`, `amazon` |
| `shop_id` | `TEXT` | loja/seller/marketplace id |
| `title` | `TEXT` | título do anúncio/produto |
| `available_qty` | `INTEGER` | default 0 |
| `reserved_qty` | `INTEGER` | default 0 |
| `inbound_qty` | `INTEGER` | default 0 |
| `unit_price` | `NUMERIC(10,2)` | preço de venda |
| `cost_price` | `NUMERIC` | existe no banco real e é usado no app; não aparece na migration 003 original, mas é lido em `src/app/api/inventory/route.ts:228` e sincronizado por `sync-costs.py` |
| `last_synced` | `TIMESTAMPTZ` | default `now()` |
| `created_at` | `TIMESTAMPTZ` | default `now()` |
| `updated_at` | `TIMESTAMPTZ` | default `now()` |

Índices/versionamento local:

- `idx_fulfillment_inventory_sku` em `sku`: `supabase/migrations/003_inventory_module.sql:52`
- `idx_fulfillment_inventory_platform` em `platform`: `supabase/migrations/003_inventory_module.sql:53`
- Unique por `sku, platform, COALESCE(shop_id, '')`: `supabase/migrations/003_inventory_module.sql:20`

FKs: nenhuma FK declarada nas migrations locais para `fulfillment_inventory`.

### Counts Supabase

```sql
SELECT count(*) FROM fulfillment_inventory;
-- Resultado: 195 registros.
```

```sql
SELECT platform, count(*)
FROM fulfillment_inventory
GROUP BY platform
ORDER BY platform;
-- Resultado: amazon=69, ml=30, shopee=96.
```

### Samples — 3 registros por marketplace

```sql
SELECT sku, platform, shop_id, title, available_qty, reserved_qty, inbound_qty, unit_price, cost_price, last_synced
FROM fulfillment_inventory
WHERE platform = 'ml'
ORDER BY sku
LIMIT 3;
-- Resultado resumido:
-- 914C_B | ml | 532562281 | available=51 | unit_price=44.90 | cost_price=18.48 | last_synced=2026-04-29T13:15:04Z
-- 914C_BA | ml | 532562281 | available=27 | unit_price=20.90 | cost_price=7.70 | last_synced=2026-04-29T13:15:02Z
-- CK4742_B | ml | 532562281 | available=52 | unit_price=26.90 | cost_price=6.61 | last_synced=2026-04-29T13:15:04Z
```

```sql
SELECT sku, platform, shop_id, title, available_qty, reserved_qty, inbound_qty, unit_price, cost_price, last_synced
FROM fulfillment_inventory
WHERE platform = 'shopee'
ORDER BY sku
LIMIT 3;
-- Resultado resumido:
-- 099 | shopee | 442066454 | available=8 | unit_price=64.90 | cost_price=25.33 | last_synced=2026-04-01T15:22:41Z
-- 1888M | shopee | 860803675 | available=1 | unit_price=34.90 | cost_price=41.11 | last_synced=2026-04-18T22:18:19Z
-- 1888M | shopee | 442066454 | available=1 | unit_price=48.90 | cost_price=41.11 | last_synced=2026-04-01T15:25:02Z
```

```sql
SELECT sku, platform, shop_id, title, available_qty, reserved_qty, inbound_qty, unit_price, cost_price, last_synced
FROM fulfillment_inventory
WHERE platform = 'amazon'
ORDER BY sku
LIMIT 3;
-- Resultado resumido:
-- 001 | amazon | A2Q3Y263D00KWC | available=10 | unit_price=89.90 | cost_price=36.54 | last_synced=2026-04-29T13:20:55Z
-- 002 | amazon | A2Q3Y263D00KWC | available=0 | reserved=1 | unit_price=89.90 | cost_price=45.21 | last_synced=2026-04-15T14:04:51Z
-- 003 | amazon | A2Q3Y263D00KWC | available=10 | unit_price=189.90 | cost_price=87.12 | last_synced=2026-04-29T13:20:54Z
```

### Relação com `base_products`, `products`, `product_listings`

No estado atual do repo/banco:

- `products` existe e é tabela do schema inicial: `supabase/migrations/001_initial_schema.sql:55`
- `products` não possui FK para `fulfillment_inventory`; relação é conceitual por `platform`, `sku`, `shop_id` e/ou `platform_item_id`.
- `fulfillment_inventory` não aponta para `products` por FK.
- `base_products` não existe no PostgREST/banco consultado e não aparece nas migrations locais.
- `product_listings` não existe no PostgREST/banco consultado e não aparece nas migrations locais.

```sql
SELECT count(*) FROM products;
-- Resultado: 1043 registros.
```

```sql
SELECT * FROM base_products LIMIT 1;
-- Resultado: tabela não encontrada/inacessível via PostgREST (404).
```

```sql
SELECT * FROM product_listings LIMIT 1;
-- Resultado: tabela não encontrada/inacessível via PostgREST (404).
```

### Outras tabelas Full-related

Existem:

- `restock_config` — configuração de lead time/cobertura: `supabase/migrations/003_inventory_module.sql:24`
- `restock_log` — envios/reposição: `supabase/migrations/003_inventory_module.sql:41`
- `sku_mapping` — mapeamento SKU filho/pai: `supabase/migrations/005_sku_mapping.sql:1`

Não existem/inacessíveis via PostgREST:

- `fulfillment_movements`
- `fulfillment_history`
- `fulfillment_sync_log`

```sql
SELECT * FROM fulfillment_movements LIMIT 1;
-- Resultado: tabela não encontrada/inacessível via PostgREST (404).
```

```sql
SELECT * FROM fulfillment_history LIMIT 1;
-- Resultado: tabela não encontrada/inacessível via PostgREST (404).
```

```sql
SELECT * FROM fulfillment_sync_log LIMIT 1;
-- Resultado: tabela não encontrada/inacessível via PostgREST (404).
```

Counts relacionados:

```sql
SELECT count(*) FROM restock_log;
-- Resultado: 3 registros.
```

```sql
SELECT count(*) FROM restock_config;
-- Resultado: 4 registros.
```

```sql
SELECT count(*) FROM sku_mapping;
-- Resultado: 68 registros.
```

---

## C — Integração das 3 contas Shopee

### Accounts / shop_ids

O inventário Shopee é sincronizado por script Python, não pelo frontend.

Config hardcoded no script:

- Lista de contas: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:27`
- Partner API base: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:22`
- Token dir: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:25`

Contas mapeadas:

| Nome interno | shop_id | token file |
|---|---:|---|
| `budamix-store` | `448649947` | `/root/.openclaw/workspace/integrations/shopee/.shopee-tokens-budamix-store.json` |
| `budamix-store2` | `860803675` | `/root/.openclaw/workspace/integrations/shopee/.shopee-tokens-budamix-store2.json` |
| `budamix-shop` | `442066454` | `/root/.openclaw/workspace/integrations/shopee/.shopee-tokens-budamix-shop.json` |

Observação: não foi copiado token real para o vault. Arquivos sensíveis foram identificados apenas por caminho.

Formato esperado dos token files, pelo código:

```json
{
  "access_token": "<REDACTED>",
  "refresh_token": "<REDACTED>"
}
```

### Onde chama API Shopee de inventory/stock

Fluxo por conta:

1. Loop nas 3 contas: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:325`
2. Token por conta e refresh automático se arquivo tem mais de ~3,3h: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:72`
3. Lista itens ativos (`get_item_list`): `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:107`
4. Endpoint Shopee `/api/v2/product/get_item_list`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:112`
5. Detalhes em batches de 50 (`get_item_base_info`): `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:127`
6. Endpoint Shopee `/api/v2/product/get_item_base_info`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:133`
7. Se tem variações, busca modelos (`get_model_list`): `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:176`
8. Endpoint Shopee `/api/v2/product/get_model_list`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:178`
9. Extrai `stock_info_v2.shopee_stock`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:185`
10. Para modelos, cria row com `platform='shopee'` e `shop_id`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:271`
11. Para itens sem variação, cria row com `platform='shopee'` e `shop_id`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:302`
12. Upsert no Supabase em `fulfillment_inventory`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:145`
13. Conflict target `sku,platform,shop_id`: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:159`

### Job/cron e frequência

Crontab VPS:

```cron
15,45 * * * * /root/scripts/sync-inventory-cron.sh
```

Referência: `/var/spool/cron/crontabs/root:2`.

Wrapper:

- `/root/scripts/sync-inventory-cron.sh:1`
- ML inventory: `/root/scripts/sync-inventory-cron.sh:15`
- Shopee inventory: `/root/scripts/sync-inventory-cron.sh:20`
- Amazon inventory: `/root/scripts/sync-inventory-cron.sh:25`

Frequência efetiva: a cada 30 minutos, nos minutos `:15` e `:45` de cada hora.

Log do dia mostra Shopee rodando e saindo `exit=0` até a execução `13:15` UTC:

```sql
SELECT shop_id, max(last_synced)
FROM fulfillment_inventory
WHERE platform = 'shopee'
GROUP BY shop_id
ORDER BY shop_id;
-- Resultado:
-- 448649947 => 2026-04-29T13:18:13Z
-- 860803675 => 2026-04-18T22:18:43Z
-- 442066454 => 2026-04-01T15:26:01Z
```

Leitura: o cron roda, mas os dados por conta estão muito assimétricos. A conta `448649947` está atualizada hoje; `860803675` está parada desde 18/04; `442066454` está parada desde 01/04. Isso é ponto central da Etapa 1.

### Fluxo conta → API → DB

```text
crontab (:15/:45)
  → /root/scripts/sync-inventory-cron.sh
    → /root/.openclaw/workspace/scripts/sync-inventory-shopee.py
      → ACCOUNTS[3]
        → get_shopee_token / refresh_shopee_token
        → /api/v2/product/get_item_list
        → /api/v2/product/get_item_base_info
        → /api/v2/product/get_model_list quando há variações
        → extract_shopee_stock(stock_info_v2.shopee_stock)
        → rows { sku, platform='shopee', shop_id, title, available_qty, reserved_qty, inbound_qty, unit_price, last_synced }
        → POST Supabase REST /fulfillment_inventory?on_conflict=sku,platform,shop_id
```

---

## D — Cálculo do KPI CUSTO no cabeçalho

### Componente do cabeçalho/KPI

- Página passa `kpis` para `InventoryOverview`: `src/app/(dashboard)/estoque/page.tsx:134`
- `InventoryOverview` renderiza `InventoryKPICards`: `src/components/inventory/inventory-overview.tsx:100`
- `InventoryKPICards` monta card **Valor Custo**: `src/components/inventory/inventory-kpis.tsx:160`

Trecho exato do card:

```tsx
{
  title: "Valor Custo",
  value: kpis.estimated_cost,
  format: "currency",
  icon: DollarSign,
  accent: "bg-[var(--accent)]/15 text-[var(--accent)]",
  gradient: "--gradient-hero",
  glowShadow: "hover:shadow-[var(--shadow-glow-accent)]",
}
```

Referência: `src/components/inventory/inventory-kpis.tsx:160`.

### Query/hook que busca o número

Fluxo real:

1. `useInventory()` usa React Query: `src/hooks/use-inventory.ts:67`
2. `fetchInventory()` chama `/api/inventory`: `src/hooks/use-inventory.ts:12`
3. `fetchInventory()` só envia parâmetros se o hook receber filtros: `src/hooks/use-inventory.ts:17`
4. Na página, `useInventory()` é chamado **sem argumentos**: `src/app/(dashboard)/estoque/page.tsx:50`
5. API route lê `platform`, `status`, `search` da querystring: `src/app/api/inventory/route.ts:154`
6. API route consulta `fulfillment_inventory`: `src/app/api/inventory/route.ts:162`
7. Se `platform` vier na query, aplica `.eq("platform", platform)`: `src/app/api/inventory/route.ts:167`
8. Retorna `kpis: computeInventoryKPIs(items)`: `src/app/api/inventory/route.ts:251`

Trecho da query real no app:

```ts
let query = supabase
  .from("fulfillment_inventory")
  .select("*")
  .order("sku", { ascending: true });

if (platform) {
  query = query.eq("platform", platform);
}

const { data: rows, error } = await query;
```

Referência: `src/app/api/inventory/route.ts:162`.

### Fórmula exata do cálculo

A fórmula do KPI **Valor Custo** está em `computeInventoryKPIs`:

```ts
estimated_cost: items.reduce(
  (s, i) => s + i.available_qty * (i.cost_price ?? 0),
  0,
),
```

Referência: `src/data/mock-inventory.ts:94`.

O `cost_price` chega do Supabase aqui:

```ts
cost_price: row.cost_price ? parseFloat(row.cost_price) : undefined,
```

Referência: `src/app/api/inventory/route.ts:228`.

### Filtros aplicados

No backend `/api/inventory`:

- Fonte: `fulfillment_inventory`, sem join com `products`.
- Ordenação: `order("sku", ascending)`.
- Filtro backend por platform somente se `?platform=` for passado: `src/app/api/inventory/route.ts:167`.
- Filtro backend por status ocorre depois do cálculo de cobertura, antes do KPI: `src/app/api/inventory/route.ts:240`.
- Filtro backend por search idem: `src/app/api/inventory/route.ts:242`.
- Não há filtro `active=true`.
- Não exclui `available_qty=0`; zero entra e contribui zero no custo.
- Não exclui `cost_price` nulo; nulo vira 0 na fórmula.

Na tela atual da **Visão Geral**, os filtros visuais são client-side sobre `items`, mas **não recalculam `kpis`**:

- Estado local `platform`: `src/components/inventory/inventory-overview.tsx:64`
- Filtragem local da tabela: `src/components/inventory/inventory-overview.tsx:76`
- KPI recebe o objeto original `kpis`: `src/components/inventory/inventory-overview.tsx:100`

Conclusão cirúrgica: **o número do KPI não muda quando o usuário troca o filtro de marketplace na Visão Geral**, porque o filtro atual só filtra a tabela (`filtered`) e o KPI continua usando `kpis` do payload inicial de `useInventory()` sem argumentos.

Quando seleciona Shopee, o KPI continua agregado geral dos 3 marketplaces, não agregado Shopee. As subtabs Shopee só filtram a tabela por `shop_id`; não recalculam KPI por conta.

### Validação SQL/read-only do KPI

```sql
SELECT
  count(*) AS rows,
  count(DISTINCT sku) AS total_skus,
  sum(available_qty) AS total_units,
  sum(available_qty * unit_price) AS estimated_value,
  sum(available_qty * coalesce(cost_price, 0)) AS estimated_cost
FROM fulfillment_inventory;
-- Resultado: rows=195, total_skus=119, total_units=10146, estimated_value=408433.61, estimated_cost=118475.60.
```

```sql
SELECT
  platform,
  count(*) AS rows,
  count(DISTINCT sku) AS total_skus,
  sum(available_qty) AS total_units,
  sum(available_qty * unit_price) AS estimated_value,
  sum(available_qty * coalesce(cost_price, 0)) AS estimated_cost
FROM fulfillment_inventory
GROUP BY platform
ORDER BY platform;
-- Resultado:
-- amazon: rows=69, total_skus=69, total_units=2537, estimated_value=103340.13, estimated_cost=23362.96
-- ml: rows=30, total_skus=30, total_units=1714, estimated_value=63553.11, estimated_cost=17782.16
-- shopee: rows=96, total_skus=49, total_units=5895, estimated_value=241540.37, estimated_cost=77330.48
```

```sql
SELECT
  shop_id,
  count(*) AS rows,
  count(DISTINCT sku) AS total_skus,
  sum(available_qty) AS total_units,
  sum(available_qty * unit_price) AS estimated_value,
  sum(available_qty * coalesce(cost_price, 0)) AS estimated_cost,
  max(last_synced) AS last_synced_max
FROM fulfillment_inventory
WHERE platform = 'shopee'
GROUP BY shop_id
ORDER BY shop_id;
-- Resultado:
-- 442066454: rows=24, total_skus=24, total_units=1264, estimated_value=58014.63, estimated_cost=22969.92, last_synced_max=2026-04-01T15:26:01Z
-- 448649947: rows=43, total_skus=43, total_units=3414, estimated_value=134833.90, estimated_cost=39246.98, last_synced_max=2026-04-29T13:18:13Z
-- 860803675: rows=29, total_skus=29, total_units=1217, estimated_value=48691.84, estimated_cost=15113.58, last_synced_max=2026-04-18T22:18:43Z
```

### Views/RPC SQL

Não há RPC/view dedicada para cálculo do KPI **Valor Custo** no código localizado. O cálculo é TypeScript em `computeInventoryKPIs`, depois de trazer rows de `fulfillment_inventory`.

Busca no repo encontrou uso de `fulfillment_inventory` em:

- `src/app/api/inventory/route.ts:163`
- `src/app/api/inventory/recommendations/route.ts:19`
- `src/app/api/prices/cross-channel/route.ts:143`
- `src/app/api/live-sales/route.ts:302`
- scripts externos de sync (`sync-inventory-*`, `sync-costs.py`)

---

## E — Marketplaces ML Full + Amazon FBA

### ML Full

Arquivo de integração:

- `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:1`

Fluxo:

1. Lê/renova token ML: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:26`
2. Busca itens ativos do seller: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:137`
3. Multiget de detalhes em batches de 20: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:153`
4. Filtra apenas `shipping.logistic_type === "fulfillment"` ou tag fulfillment: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:164`
5. Resolve SKU por `seller_custom_field`, variação, atributo `SELLER_SKU` ou fallback item id: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:167`
6. Monta row com `platform='ml'`, `shop_id=ML_SELLER_ID`: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:187`
7. Upsert em `fulfillment_inventory` por `sku,platform,shop_id`: `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:90` e `/root/.openclaw/workspace/scripts/sync-inventory-ml.py:112`

Cron:

```cron
15,45 * * * * /root/scripts/sync-inventory-cron.sh
```

Wrapper chama ML em `/root/scripts/sync-inventory-cron.sh:15`.

Último log visto:

- `2026-04-29T13:15:01Z` iniciou ML inventory.
- `2026-04-29T13:15:04Z` terminou com exit 0.
- Script reportou `Total active items: 59`, `Fulfillment items found: 19`, `Upserted 14 items`.

### Amazon FBA

Arquivo de integração:

- `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:1`

Fluxo:

1. Lê credenciais SP-API: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:26`
2. Gera token LWA: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:31`
3. Chama SP-API FBA Inventory Summaries: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:135`
4. Endpoint: `/fba/inventory/v1/summaries`: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:135`
5. Extrai `fulfillableQuantity`, `inboundReceivingQuantity`, `inboundWorkingQuantity`, `inboundShippedQuantity`, `reservedQuantity`: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:147`
6. Filtra itens sem estoque/reserva/inbound: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:159`
7. Monta row com `platform='amazon'`, `shop_id=MARKETPLACE_ID`: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:166`
8. Upsert em `fulfillment_inventory` por `sku,platform,shop_id`: `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:84` e `/root/.openclaw/workspace/scripts/sync-inventory-amazon.py:98`

Cron:

```cron
15,45 * * * * /root/scripts/sync-inventory-cron.sh
```

Wrapper chama Amazon em `/root/scripts/sync-inventory-cron.sh:25`.

Últimos sinais:

- Última execução completa em log: `2026-04-29T12:54:05Z`, `Total FBA items: 59`, `Upserted 59 items`.
- Dados no Supabase tinham `last_synced` Amazon até `2026-04-29T13:23:02Z` no momento da consulta read-only.

### Paralelo entre Shopee, ML e Amazon

Lógica homogênea no destino, heterogênea na origem:

- Todos populam a mesma tabela: `fulfillment_inventory`.
- Todos fazem upsert com conflict target `sku,platform,shop_id`.
- Todos gravam `available_qty`, `reserved_qty`, `inbound_qty`, `unit_price` quando disponível e `last_synced`.
- `cost_price` não vem dos marketplaces; é aplicado depois por `/root/.openclaw/workspace/scripts/sync-costs.py`.

Diferenças principais:

- **Shopee**: multi-conta explícita; estoque Full vem de `stock_info_v2.shopee_stock`; problema atual é assimetria forte de `last_synced` por `shop_id`.
- **ML Full**: filtra anúncios fulfillment por `shipping.logistic_type`/tag; ML não expõe reservado/inbound separadamente nesse script.
- **Amazon FBA**: usa FBA Inventory Summaries; tem reserved e inbound detalhados, mas o sync é mais longo/paginado.

### Custo — sync separado

O custo do KPI vem de `cost_price`, sincronizado por:

- `/root/.openclaw/workspace/scripts/sync-costs.py:1`
- Cron diário: `/root/scripts/sync-costs-cron.sh:1`
- Crontab: `0 9 * * * /root/scripts/sync-costs-cron.sh`

Fonte: Google Sheets com prioridade:

- `ESTOQUE > MELI > SHOPEE > AMAZON`: `/root/.openclaw/workspace/scripts/sync-costs.py:11`
- Atualiza `fulfillment_inventory.cost_price`: `/root/.openclaw/workspace/scripts/sync-costs.py:111`
- Upsert em `fulfillment_inventory`: `/root/.openclaw/workspace/scripts/sync-costs.py:140`

Último log de custo visto:

- `2026-04-29T09:00:04Z` iniciou.
- 128 SKUs com custo mapeado.
- 195 registros no `fulfillment_inventory`.
- 40 registros com SKU encontrado na planilha.
- 0 atualizações necessárias.

---

## Pontos de atenção para a Etapa 1/2

1. **Bug de UX/KPI:** filtros da Visão Geral não recalculam KPIs. Hoje o KPI **Valor Custo** permanece global mesmo quando o usuário filtra ML/Shopee/Amazon ou uma loja Shopee.
2. **Shopee assimétrico:** `448649947` está atualizada hoje; `860803675` e `442066454` estão defasadas. A Etapa 1 deve começar por logs/resultado por account dentro do `sync-inventory-shopee.py`.
3. **Schema drift:** `cost_price` existe no banco e no código, mas não aparece na migration `003_inventory_module.sql` lida. Vale consolidar migration/schema antes do refactor.
4. **Sem base catalog:** `base_products` e `product_listings` não existem no estado atual consultado. Qualquer plano que dependa dessas tabelas precisa criar/migrar explicitamente ou adaptar ao `products`/`sku_mapping` atuais.
5. **CUSTO depende de SKU match exato:** `sync-costs.py` aplica custo por `sku` exato; o log mostra muitos SKUs da planilha sem match no inventário. Isso pode distorcer o KPI quando `cost_price` fica nulo/zero.
