---
title: "Budamix Central Refactor Full — 02 Plano KPI Custo"
created: 2026-04-29
type: plan
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - custo
  - plano
---

# Etapa 2 — Validar e Corrigir KPI "Valor Custo" no Cabeçalho

## Contexto

Mapeamento ([[projects/budamix-central-refactor-full/00-mapeamento|00-mapeamento.md]]) revelou:

**Estado atual do KPI:**
```
Total agregado (3 marketplaces, 195 registros):
  estimated_cost = R$ 118.475,60
```

**Fórmula em si está correta:**
```ts
estimated_cost: items.reduce(
  (s, i) => s + i.available_qty * (i.cost_price ?? 0),
  0,
)
```
Referência: [src/data/mock-inventory.ts:94](src/data/mock-inventory.ts#L94)

**Os 3 problemas reais:**

### Problema 1 — Match de cost_price fraco (CRÍTICO, afeta o número)

`sync-costs.py` última execução (29/04 09:00):
- 195 registros em `fulfillment_inventory`
- 128 SKUs com custo na planilha de precificação
- **Apenas 40 matches** ← 155 registros podem ter `cost_price` NULL ou desatualizado

Como a fórmula faz `coalesce(cost_price, 0)`, registros sem match contribuem **R$ 0,00 silenciosamente**. O R$ 118k pode estar subestimado em ~R$ 50k+ se 155 registros tiverem custo zerado.

### Problema 2 — KPI não recalcula com filtro (UX)

Filtros visuais da Visão Geral filtram tabela mas mantêm KPI global.

Referência: [src/components/inventory/inventory-overview.tsx:100](src/components/inventory/inventory-overview.tsx#L100)

```tsx
// kpis vem do payload inicial e não é recalculado
<InventoryKPICards kpis={kpis} ... />
```

Filtrar Shopee mostra tabela só de Shopee, mas KPI continua somando ML + Shopee + Amazon.

### Problema 3 — Schema drift (defensivo)

`cost_price` existe no banco e é lido no código, mas não está na migration `003_inventory_module.sql`. Recriar ambiente do zero quebra. Documentação está mentindo.

## Objetivos

1. **Saber o número CORRETO** do custo total do estoque Full hoje
2. **Garantir que o número exibido bate com o número correto**
3. **Filtros funcionarem** (KPI segue filtro de marketplace/status)
4. **Migration consistente** com banco real

Sem fazer redesign de UX, sem mudar schema de tabelas, sem reescrever sync-costs. Apenas auditar + patch cirúrgico onde necessário.

## Fases

### 2A — Diagnóstico do match cost_price (read-only, Kobe)

Quantificar o tamanho do problema antes de propor correção.

**Output esperado:** arquivo `02a-diagnostico-custo.md` no vault com:
- SKUs sem `cost_price` (NULL) ou com `cost_price = 0`
- SKUs presentes em `fulfillment_inventory` mas ausentes na planilha de precificação
- SKUs presentes na planilha mas com formato divergente (ex: "001" vs "001A", case, prefixo)
- Uso de `sku_mapping` (68 registros) — ele resolve algum caso?
- Estimativa de custo "real" se todos os SKUs tivessem custo correto
- Recomendação: planilha precisa cobrir mais SKUs? script precisa ser mais flexível?

**SQLs principais (read-only, Kobe roda no Supabase):**

```sql
-- Quantos sem custo
SELECT
  count(*) AS total,
  count(*) FILTER (WHERE cost_price IS NULL) AS null_cost,
  count(*) FILTER (WHERE cost_price = 0) AS zero_cost,
  count(*) FILTER (WHERE cost_price > 0) AS valid_cost
FROM fulfillment_inventory;

-- Por marketplace, qual o impacto?
SELECT
  platform,
  count(*) AS rows,
  count(*) FILTER (WHERE cost_price IS NULL OR cost_price = 0) AS sem_custo,
  sum(available_qty) FILTER (WHERE cost_price IS NULL OR cost_price = 0) AS units_sem_custo,
  sum(available_qty * unit_price) FILTER (WHERE cost_price IS NULL OR cost_price = 0) AS valor_venda_sem_custo
FROM fulfillment_inventory
GROUP BY platform
ORDER BY platform;

-- Top 20 registros sem custo, ordenados por valor potencial perdido
SELECT sku, platform, shop_id, available_qty, unit_price,
       available_qty * unit_price AS valor_venda_potencial
FROM fulfillment_inventory
WHERE (cost_price IS NULL OR cost_price = 0)
  AND available_qty > 0
ORDER BY valor_venda_potencial DESC
LIMIT 20;

-- sku_mapping cobre algum caso?
SELECT count(DISTINCT fi.sku) AS skus_inventory_com_mapping
FROM fulfillment_inventory fi
JOIN sku_mapping sm ON sm.child_sku = fi.sku OR sm.parent_sku = fi.sku;
```

**Análise da planilha:** invocar skill `planilha-precificacao` pra ler estrutura da planilha de precificação, listar SKUs presentes, comparar com inventário.

### 2B — Auditoria do bug UX (CC local + Kobe)

Confirmar comportamento e mapear todos os KPIs afetados.

**Tarefas:**
- Listar todas as KPI cards do componente `InventoryKPICards` ([src/components/inventory/inventory-kpis.tsx:117](src/components/inventory/inventory-kpis.tsx#L117))
- Para cada uma: confirmar se respeita filtro ou não
- Definir comportamento esperado: KPI segue filtros visuais (marketplace + status + busca) sempre, ou mantém global com toggle?

**Decisão proposta:** KPI segue filtros sempre (comportamento esperado pelo usuário). Sem toggle. Simplicidade > flexibilidade.

### 2C — Plano de correção (CC local)

Documento separado com patches específicos depois das 2A e 2B. Esboço:

**Fix Problema 1 (match cost_price):**
- (a) Pedro adiciona SKUs faltantes na planilha de precificação (esforço operacional)
- (b) `sync-costs.py` usa `sku_mapping` como fallback (busca pelo parent_sku se child não tem custo)
- (c) UI marca SKUs sem custo (badge ou cor) — quebra a invisibilidade do `coalesce(0)`

**Fix Problema 2 (UX KPI):**
- Recalcular `kpis` no client a partir de `filtered` (resolve no front, sem precisar mudar API)
- Ou: API aceita os mesmos filtros e retorna `kpis` filtrados (mais correto, mas mais código)

**Fix Problema 3 (schema drift):**
- Criar migration `006_add_cost_price.sql` declarando `cost_price NUMERIC` em `fulfillment_inventory`
- Marcar como "schema reconciliation" no commit

### 2D — Execução (Kobe)

Aplicar patches da 2C. Mesmo padrão da Fase 1C: snapshot tar antes, validação progressiva, rollback definido.

### 2E — Validação cruzada (Pedro)

- Abrir `/estoque` em produção
- Conferir que filtro Shopee mostra KPI Shopee (não global)
- Conferir SKU campeão: comparar `qty × custo` no Supabase com Pedro fazendo conta manual via planilha de precificação
- Marcar 3 SKUs com discrepância significativa pra revisão futura

## Dependências

- ✅ Fase 0 concluída
- ✅ Fase 1C concluída
- Skill `planilha-precificacao` instalada e operacional
- Acesso de leitura à planilha de precificação Google Sheets (Kobe via service account ou Pedro via export)

## Riscos

- **Planilha de precificação fora do nosso controle de versão:** se Pedro editar enquanto rodamos diagnóstico, números mudam. Snapshotar valores no início da Fase 2A.
- **Mudar fórmula do KPI pode regredir outros lugares:** `computeInventoryKPIs` é usado em mock também. Tem que validar que mudar comportamento de filtro não quebra restock-tab, history, etc.
- **`sku_mapping` pode introduzir custos errados:** se parent e child têm custos diferentes, fallback silencioso é perigoso. Tem que ser explícito.

## Próximo passo

Mensagem pro Kobe executar Fase 2A (diagnóstico do match cost_price).
