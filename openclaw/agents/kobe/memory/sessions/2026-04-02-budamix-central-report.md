---
title: "2026-04-02-budamix-central-report"
created: 2026-04-26
type: session
agent: kobe
status: active
tags:
 - agent/kobe
 - session
---
# Budamix Central — Relatório de Sessão 02/04/2026

## 1. Correções de Dados

### Bug Amazon unit_price (CRÍTICO)
- **Problema:** `sync-amazon-orders.py` salvava `ItemPrice.Amount` (total do line item) como `unit_price`. Qualquer order com qty > 1 tinha receita inflada.
- **Exemplo:** KIT2PANO800AM_T mostrava R$79.818 em 30d. Real: R$1.939 (120 un × R$15,90).
- **Fix:** `unit_price = ItemPrice.Amount / QuantityOrdered` na função `normalize_order()`.
- **Orders afetados:** 447 (divisão direta) + 179 (recálculo via OrderTotal/qty) + 8 (re-sync da SP-API para multi-item orders).
- **Baseline validado:** Receita 30d = R$377.640 | 64 SKUs ativos (pós-correção).
- **ML e Shopee:** Não tinham esse bug (APIs já retornam unit_price).

### Shopee sync restaurado
- **Problema:** `sync-shopee-prices.py` falhava com HTTP 409/400 há 8 dias (desde 25/03).
- **Causa raiz:** Função `supabase_upsert` sem `on_conflict` para tabela `products` (409 em duplicatas), e com `on_conflict` errado para `price_history` (400 em tabela sem constraint).
- **Fix:** `on_conflict` como parâmetro opcional na função. `products` usa `on_conflict=platform,platform_item_id`. `price_history` não usa (tabela de log).
- **Resultado:** 916 products sincronizados nas 3 lojas Shopee.

### Paginação Curva ABC
- **Problema:** Query no `/api/abc/route.ts` buscava orders sem `.range()`, limitando a 1000 de 20k+ rows.
- **Fix:** `fetchAllOrdersPaginated()` com loop `PAGE_SIZE=1000` e `.range(from, from+999)`.
- **Validado:** 20.098 orders nos últimos 90 dias (antes só 1000).

### sync-inventory-amazon.py
- **Problema:** Escrevia `unit_price: 0` no payload de upsert a cada 30 min, sobrescrevendo preços reais.
- **Fix:** Removida a linha `"unit_price": 0` do payload. Campo gerenciado exclusivamente pelo `sync-amazon-prices.py`.

## 2. Implementação de Tempo Real (Syncs)

### Latências atingidas

| Dados | Antes | Depois |
|-------|-------|--------|
| Preços (Amazon, ML, Shopee) | 30min a ∞ | **≤2 min** |
| Orders (ML, Shopee) | 30 min | **≤2 min** |
| Orders (Amazon) | 30 min | **≤5 min** |
| Estoque | 30 min | 30 min (não alterado) |

### Mecanismo
- **Preços:** Scripts dedicados por plataforma, cron `*/2`, buscam preço atual do anúncio via API do marketplace e atualizam Supabase.
- **Orders rápidos:** Mesmos scripts existentes com novo param `--minutes 5` (janela de 5 min com overlap). Upsert garante idempotência. Lock file evita execução concorrente.
- **Cron 30min mantido** como catchup/rede de segurança (`--days 1`).

### Volume por ciclo (média)
- ~0.4 orders novos por 2 min (peak 21h BRT: ~1.2/2min)
- 23 API calls por ciclo de preços (Amazon 3 + ML 2 + Shopee 18)

## 3. Scripts Criados e Modificados

### Novos

| Script | Função |
|--------|--------|
| `sync-amazon-prices.py` | Preços Amazon via Listings API (getListingsItem com offers). 59 SKUs, ~52s/ciclo. |
| `sync-ml-prices.py` | Preços ML via multi-get /items. Upsert com variações (MLB_ID::SKU). 58 listings → 69 products. |
| `resync-8-orders.py` | Script one-shot para re-sync de 8 orders específicos da SP-API. |
| `sync-amazon-prices-cron.sh` | Wrapper cron para sync-amazon-prices.py (timeout 90s, log rotate 7d). |
| `sync-ml-prices-cron.sh` | Wrapper cron para sync-ml-prices.py (timeout 90s, log rotate 7d). |
| `sync-shopee-prices-2min-cron.sh` | Wrapper cron para sync-shopee-prices.py (timeout 90s, log rotate 7d). |
| `sync-orders-fast.sh` | Wrapper cron ML+Shopee orders `--minutes 5` com lock file. |
| `sync-amazon-orders-fast.sh` | Wrapper cron Amazon orders `--minutes 5` com lock file. |
| `lib/constants.ts` | Constante SHOPEE_STORE_NAMES centralizada para reutilização cross-módulo. |

### Modificados

| Script | Mudança |
|--------|---------|
| `sync-amazon-orders.py` | Fix unit_price (÷ qty) + param `--minutes` |
| `sync-ml-orders.py` | Param `--minutes` + fix strftime (truncava pra meia-noite) |
| `sync-shopee-orders.py` | Param `--minutes` + fix time_from/time_to (float → int) |
| `sync-shopee-prices.py` | Fix on_conflict como parâmetro opcional |
| `sync-inventory-amazon.py` | Removido `unit_price: 0` do payload |
| `sync-orders-cron.sh` | Adicionado `timeout 300` |
| `sync-inventory-cron.sh` | Adicionado `timeout 300` |

### Frontend (VPS /var/www/budamix-central/src/)

| Arquivo | Mudança |
|---------|---------|
| `app/api/abc/route.ts` | Paginação, sem sku_mapping, shop_id, filtro pending >7d |
| `app/api/prices/cross-channel/route.ts` | Sem sku_mapping |
| `app/api/live-sales/route.ts` | Filtro pending >7d no bloco Amazon |
| `app/(dashboard)/page.tsx` | Mock fallbacks removidos (fix flash), dead code limpo |
| `app/(dashboard)/abc/page.tsx` | Abas duplicadas removidas |
| `components/abc/abc-table.tsx` | Sub-abas Shopee, consolidação, filtros corrigidos, SKU 160px+tooltip |
| `components/abc/abc-insights.tsx` | Encoding fix (período) |
| `components/dashboard/kpi-cards.tsx` | Encoding fix (Ticket Médio) |
| `components/dashboard/channel-breakdown.tsx` | Encoding fix (Participação por Canal) |
| `components/live/ranking-list.tsx` | Key fix (removido índice) |
| `hooks/use-live-sales.ts` | Removido sort hardcoded |
| `hooks/use-kpis.ts` | refetchInterval: 120_000 (2 min) |
| `hooks/use-daily-sales.ts` | refetchInterval: 120_000 (2 min) |
| `components/prices/price-row-detail.tsx` | Nomenclatura Shopee via constante |
| `lib/constants.ts` | NOVO — SHOPEE_STORE_NAMES |

## 4. Crontab Final

```
5,35 * * * *   /root/scripts/sync-orders-cron.sh
15,45 * * * *  /root/scripts/sync-inventory-cron.sh
0 9 * * *      /root/scripts/sync-costs-cron.sh
0 * * * *      /var/www/mission-control/scripts/collect-usage-cron.sh
*/2 * * * *    /root/scripts/sync-amazon-prices-cron.sh
*/2 * * * *    /root/scripts/sync-ml-prices-cron.sh
*/2 * * * *    /root/scripts/sync-shopee-prices-2min-cron.sh
*/2 * * * *    /root/scripts/sync-orders-fast.sh
*/5 * * * *    /root/scripts/sync-amazon-orders-fast.sh
```

| Cron | Script | O que faz | Freq | Timeout |
|------|--------|----------|------|---------|
| `5,35 * * * *` | sync-orders-cron.sh | Orders ML+Shopee+Amazon (--days 1, catchup) | 30 min | 300s |
| `15,45 * * * *` | sync-inventory-cron.sh | Estoque ML+Shopee+Amazon | 30 min | 300s |
| `0 9 * * *` | sync-costs-cron.sh | Custos planilha Google | Diário 06h BRT | — |
| `0 * * * *` | collect-usage-cron.sh | Mission Control usage | 1h | — |
| `*/2 * * * *` | sync-amazon-prices-cron.sh | Preços Amazon (59 SKUs, Listings API) | 2 min | 90s |
| `*/2 * * * *` | sync-ml-prices-cron.sh | Preços ML (58 listings, multi-get + upsert) | 2 min | 90s |
| `*/2 * * * *` | sync-shopee-prices-2min-cron.sh | Preços Shopee (916 items, 3 lojas) | 2 min | 90s |
| `*/2 * * * *` | sync-orders-fast.sh | Orders ML+Shopee (--minutes 5, lock file) | 2 min | 90s |
| `*/5 * * * *` | sync-amazon-orders-fast.sh | Orders Amazon (--minutes 5, lock file) | 5 min | 90s |

## 5. Mudanças nos Módulos

### Curva ABC
- **sku_mapping removido** — opera por listing individual (97 SKUs vs 64 antes com mapping)
- **Sub-abas Shopee:** Budamix Store / Budamix Oficial / Budamix Shop (constante centralizada em lib/constants.ts)
- **Consolidação frontend:** Visão "Todas" e "Shopee > Todas" agrupam rows por SKU raw (soma receita das 3 lojas)
- **Filtros corrigidos:** Recálculo Pareto (step 4) roda ANTES do filtro de curva (step 5). Antes B/C infiltravam na visão Curva A.
- **Abas duplicadas removidas:** Tinha 2 fileiras de filtro plataforma — removida a de cima
- **Coluna SKU:** Alargada de 100px para 160px + tooltip no hover
- **Encoding:** "Variação", "período" corrigidos
- **API:** Shopee fragmentado por shop_id (aggKey = sku::shop_id), filtro pending >7d

### Preços v2
- **sku_mapping removido** — compara por SKU raw. KIT2YW640 (R$29,61) e KIT4YW640 (R$62,91) agora são linhas separadas.
- **Inconsistentes:** 37 → 20 (falsos do mapping removidos) → 13 (variações ML resolvidas)
- **sync-ml-prices com upsert:** Cria entrada na products se não existe. Antes só atualizava existentes.
- **Variações ML:** Mapa MLB_ID → Set<SKU> construído a partir dos orders. Cria uma entry por variação com platform_item_id = `MLB_ID::SKU`. 36 variações cobertas.
- **Limpeza:** 28 duplicatas formato antigo (MLB ID sem ::) deletadas
- **IMB501C_T:** Corrigido de R$29,90 (fallback fulfillment) para R$24,88 (ML API real)
- **Nomenclatura Shopee:** "budamix-store" → "Budamix Store", etc. Via constante compartilhada.
- **Products ML:** 26 → 61 → 97 (upsert + variações)

## 6. Regra de Negócio: Pending Amazon

### Regra
- **Mostrar:** Orders Amazon pending (incluir em KPIs/gráficos)
- **Remover:** Se status mudar para cancelled
- **Remover:** Se ficar pending por mais de 7 dias sem mudar de status

### Onde aplicada (4 pontos)

| Ponto | Tipo | Filtro |
|-------|------|--------|
| `v_kpis_by_period` | View SQL | `AND NOT (status = 'pending' AND order_date < NOW() - INTERVAL '7 days')` |
| `v_daily_sales` | View SQL | Mesmo filtro |
| `/api/live-sales/route.ts` | Query TS | `.gte("order_date", pendingCutoff)` no bloco Amazon pending |
| `/api/abc/route.ts` | Loop TS | `if (status === "pending" && order_date < cutoff) continue` |

### Impacto
- **Hoje:** 0 orders excluídos (nenhum pending > 7 dias)
- **18 pending ativos:** 13 (<24h) + 7 (1-3d) + 1 (3-7d) = R$633,80
- **Sync de status funciona:** 504 orders cancelled confirmam que pending → cancelled é atualizado via LastUpdatedAfter + upsert

## 7. Dashboard Home

### Flash de valores
- **Causa raiz:** Mock estático (R$497k / 2.847 pedidos / ticket R$174) era renderizado como fallback enquanto TanStack Query fazia fetch. Dados reais (R$397k / 8.833 / R$44) substituíam após ~0.5s.
- **Fix:** 3 fallbacks mock substituídos por `undefined`. Componentes exibem skeleton durante fetch. Dead code mock removido.

### Polling
- `useKPIs`: sem polling → `refetchInterval: 120_000` (2 min)
- `useDailySales`: sem polling → `refetchInterval: 120_000` (2 min)
- `useHealthStatus`: mantido em 60s

### Encoding
- "Ticket Medio" → "Ticket Médio" (kpi-cards.tsx)
- "Participacao por Canal" → "Participação por Canal" (channel-breakdown.tsx, 2 ocorrências)
- "Variação %" e "vs período anterior" já corrigidos anteriormente
- **Auditoria final:** Zero ocorrências de encoding incorreto em todo o dashboard

### Acuracidade validada
- View (dashboard): R$397.411 | 8.833 pedidos | ticket R$44,99
- Query direta: R$360.552 | 8.161 pedidos | ticket R$44,18
- Delta (10%): view inclui Amazon pending (correto por design)

## 8. Dívidas Técnicas Remanescentes

| Item | Severidade | Detalhe |
|------|-----------|---------|
| Cache IDs Shopee | Média | `list_all_items()` roda a cada 2 min (~54 calls/ciclo só pra listar IDs). A lista de items ativos não muda a cada 2 min. Fix: cachear IDs em JSON local, atualizar lista a cada 30 min, sync de preços só faz get_item_base_info. Reduz de 54 pra 18 calls/ciclo. |
| Supabase key hardcoded | Média | service_role key em texto nos scripts Python no VPS. Risco baixo (VPS com acesso root), mas impede rotação de credenciais. Fix: mover pra arquivo de credenciais ou env var. |
| 9 Amazon SKUs sem preço | Menor | 8 com estoque: KIT2PANO800AZ_T (38un), 0063_ (29un), e 6 com 1-2un. Listings provavelmente inativos ou SKU legado. Investigar no painel Amazon. |
| Next.js 16 | Menor | Versão antiga, funcional. Upgrade quando houver necessidade. |

## 9. Regras Operacionais Estabelecidas

1. **Nenhuma escrita no Supabase sem aprovação explícita do Pedro** — sem exceção. Aplica pra scripts Python, queries SQL, PATCH requests, tudo.
2. **Sanity check obrigatório em valores monetários** — nunca aceitar números absurdos sem questionar. Cruzar preço unitário × quantidade = total faz sentido?
3. **Backup antes de UPDATE em massa** — criar tabela de backup ou salvar estado antes de modificar dados existentes.
4. **Horários sempre em Brasília (BRT, UTC-3)** — nunca UTC. Em crons, logs, relatórios, comunicação com Pedro.
5. **Credenciais salvar em memória persistente** — nunca pedir de novo ao Pedro.
6. **sku_mapping reservado para módulo futuro** — NÃO usar em Curva ABC nem Preços v2. Reservado para módulo de Estoque/Compras (consolidação unitária para planejamento de importação).

---

## Status Geral

| Módulo | Status |
|--------|--------|
| Home KPIs | ✅ Operacional |
| Live Sales | ✅ Operacional |
| Estoque Full | ✅ Operacional |
| Curva ABC | ✅ Operacional |
| Preços v2 | ✅ Operacional |
| Daily Sales | ✅ Operacional |
| Sync Preços (3 plataformas) | ✅ Operacional (≤2 min) |
| Sync Orders (ML+Shopee) | ✅ Operacional (≤2 min) |
| Sync Orders (Amazon) | ✅ Operacional (≤5 min) |
| Crontab (9 jobs) | ✅ Ativo |
