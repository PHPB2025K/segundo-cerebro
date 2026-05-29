---
title: "Estoque GB — Fase 2 mapeamento de SKUs (resolver + camadas)"
created: 2026-05-28
type: project-memory
status: implementado-camada-dados-pendente-codigo
project: estoque-gb-movimentacoes
tags:
  - estoque
  - gb-importadora
  - budamix-central
  - sku-mapping
  - phase-2
---

# Estoque GB — Fase 2 mapeamento de SKUs

## Decisão executada — 2026-05-28 (sessão Claude Code direto, não Kobe)

Pedro pediu para implementar o plano completo de mapeamento de SKUs do
motor de estoque Budamix Central (`/var/www/estoque-budamix`). Implementação
foi feita **fora do Kobe**, direto via Claude Code + Supabase MCP.

## O que está em produção

### Tabelas populadas (Supabase project Budamix Central)

- `public.sku_aliases` — **25 aliases** com confidence ≥ 0.85, todos `source='auto_phase2_classify'`.
  Exemplos: `CK4742_BB → CK4742_B`, `914C → 914C_B`, vários `54171X → 54171X_B`.
- `public.kit_bom` — **16 kits homogêneos** decomponíveis.
  Exemplos: `KIT2YW1520RC_T → 2× YW1520RC`, `KIT4YW800SQ_T → 4× YW800SQ_T`.

### Tabelas auxiliares (cache da análise)

- `public._catalog_estoque` (93 SKUs) — snapshot da aba ESTOQUE em 28/05 ~15:30 BRT,
  via service account Google Sheets do app.
- `public._sku_analise` (940 SKUs únicos divergentes) — classificação automática.

### Postgres function

- `public.resolver_sku(p_sku_raw text)` — resolvedor único, ordem:
  1. catálogo direto
  2. sku_aliases ativo (ordenado por confidence)
  3. kit_bom ativo (verifica se cada componente está no catálogo)
  4. desconhecido

### Views

- `public.vw_resolver_dashboard` — JOIN de stock_movements × resolver para observabilidade.
- `public.vw_decisoes_pendentes_familias` — agrupamento por família para decisão humana.

### Documentação

- `/var/www/estoque-budamix/docs/stock-movements-phase2-resolver.md` — handoff para o Kobe.

## Cobertura atual

| Bucket | Movimentos | % | SKUs únicos |
|---|---|---|---|
| Aplicaria auto (direto + alias + kit_bom) | 170 | **8%** | 52 |
| Bloqueado (desconhecido + kit_sem_bom) | 1.949 | 92% | 888 |

92% bloqueado **não é falha do resolver** — reflete o pivot 100% vidro de 25/05:
a aba ESTOQUE tem apenas 93 SKUs, mas as planilhas FULL ainda contêm giro
de famílias legadas (CK/Clink jarras, FYTR001 panos, PUMP, AD, BR, BF, IN0,
MANT, BAT, BACIA, BARBECUE FORK, etc).

## O que NÃO foi feito

1. ~~**Integração com o motor TypeScript** (Etapa 5 do plano, parte de código).~~
   **✅ FEITO em 2026-05-28 ~15:50 BRT** — 3 arquivos refatorados:
   - `src/lib/stock-movements.ts` ganhou `resolveSku()` + tipos `SkuResolution`
   - `src/app/api/stock-movements/ingest-safe-outbound/route.ts` chama o resolver,
     expande kits em N movimentos com external_event_id derivado por componente
   - `src/app/api/sheets/update/route.ts` idem
   - `npx tsc --noEmit` passou
   - `/api/stock-movements/ingest-envios-full` não precisou mudar — só faz upload
     do XLSX e dispatcha pra ingest-safe-outbound, que já tem o resolver
   - **Build/PM2 restart NÃO foi feito** — código vivo no disco aguarda decisão.

2. **Etapas 8-9 do plano** (modo sombra 2-3 dias + liberação gradual) — exigem
   o motor TS plugado no resolver e dias reais de operação.

3. **Limpeza dos 2.119 movimentos `divergente` atuais** — não foi feita.
   Ficam de baseline pra comparação futura.

## Decisões humanas pendentes (top 8 famílias)

| Família | SKUs | Mov | Qty | Decisão típica |
|---|---|---|---|---|
| kits_diversos | 197 | 469 | 5.020 | Maioria sem BOM no catálogo — cadastrar componente OU descontinuar |
| outros | 237 | 379 | 4.888 | Inspeção caso a caso |
| familia_CK_jarra_clink | 150 | 332 | 3.581 | Clink fora do pivot 100% vidro — descontinuar? |
| codigos_numericos | 167 | 236 | 2.481 | Provavelmente lixo / SKUs de teste |
| familia_FYTR001 | 13 | 130 | 5.540 | Panos — cadastrar família? Família alta-frequência |
| familia_BR | 28 | 64 | 592 | Avaliar |
| familia_BF_bf_bling | 14 | 53 | 673 | Pedidos Bling — cadastrar? |
| familia_PUMP | 22 | 53 | 530 | Dosadores — descontinuar? |

## Próximo passo natural

Pedro/Kobe definir por família: cadastrar, aliasar ou descontinuar. Cada decisão
é UM INSERT em `sku_aliases`, `kit_bom`, `_catalog_estoque` (este último seria
uma atualização da planilha ESTOQUE real, depois re-snapshot). Após cada lote
de decisões, re-rodar `vw_resolver_dashboard` pra ver a cobertura subir.

## Primeira baixa real aplicada — 29/05/2026 ~09:50 BRT

**Contexto:** Pedro recebeu dos analistas a lista de envios FULL criados em 28/05 e autorizou aplicar baixa real.

**Envios processados (5):**
- ML590 (Yasmin / FULL ML)
- AM328B (Leonardo / FBA AMAZON)
- SH45 (Lucas / FULL SHOPEE 1)
- SH41 (Lucas / FULL SHOPEE 2)
- SH41 (Lucas / FULL SHOPEE 3)

**Eventos: 13/13 aplicado em 20.7s. Total: 671 unidades baixadas.**

| Canal | Movimentos | Qty baixada |
|---|---|---|
| fba_amazon | 1 | 10 |
| full_ml | 1 (kit expandido) | 120 |
| full_shopee_1 | 2 | 160 |
| full_shopee_2 | 2 | 107 |
| full_shopee_3 | 7 | 274 |

**Decisões/aprendizados desta rodada:**
- `gog drive download` (conta gb.ai.agent@gbimportadora.com) é o caminho oficial pra baixar XLSX do Drive na VPS. SA dedicada do estoque-budamix não precisa Drive API.
- Parser TS `lib/envios-full.ts` — **TODOS bugs corrigidos em 29/05 ~10:30 BRT:**
  - ✅ Abas inexistentes removidas (AMAZON FULL, FULL MAGALU)
  - ✅ `SAFE_STATUSES` estendido: `coletado, entregue, preparando, aguardando coleta, nf gerado, nf não gerado`
  - ✅ `BLOCKED_STATUSES` estendido com `devolvido`
  - ✅ `columnsForSheet` agora retorna por aba: FBA AMAZON `(1,2,3,6)`, FULL ML `(1,2,3,4)`, FULL SHOPEE `(2,3,4,null)` (sem coluna status confiável)
  - ✅ Novo `isShipmentHeader` (regex `/^(AM|ML|SH|MALU)\w*\d/i`) + `isItemRow` baseado em SKU em coluna correta (não mais `row[0] > 0`)
  - ✅ `SKU_LABEL_BLOCKLIST` rejeita labels (SKU/PRODUTO/GTIN/SEM GTIN/ASIN/etc.)
  - ✅ Date em coluna status é ignorado (Shopee tem datas em col 5)
  - **Validação:** 3.196 eventos extraídos do XLSX oficial em isolamento, 43 skipped (32 corretos por CANCELADO, 5 typo "ENREGUE", 3 status "ENVIADO" não-mapeado).
- **Skipped pendentes pra decisão Pedro:**
  - ✅ `ENVIADO` (3 casos) — Pedro confirmou 29/05: significa "saiu do galpão pra transportadora". Adicionado em SAFE_STATUSES. PM2 restartado pid 2891417.
  - `ENREGUE` (5 casos) — typo de "Entregue" na planilha. Localizado em **FULL ML, linhas 1317-1321, todos no envio ML143** (Yasmin). Pedir Yasmin corrigir.
- Novo kit cadastrado: `KIT6YW640 → 6× YW640RC` (descoberto via envio ML590 do Yasmin).

**Estado pós-aplicação:**
- `kit_bom` agora tem 17 entries (16 + KIT6YW640)
- `stock_movements` tem 13 novos rows com status='aplicado' e correspondentes baixas na planilha ESTOQUE do Drive
- Saldos planilha decrementados em 671 unidades em 11 SKUs distintos

## Riscos abertos (não tratados nesta sessão)

- RLS continua **desabilitado** em `stock_movements`, `stock_movement_evidences`,
  `sku_aliases`, `kit_bom` (e mais 9 tabelas). Advisor crítico do Supabase ativo.
- Repo VPS sem commits (git mostra "No commits yet").

## Deploy 2026-05-28 ~16:09 BRT

- Build webpack: 12.5s compile + 2.2min TS + 13 páginas OK
- PM2 restart: pid 2428590, restart #6, Ready in 215ms
- Smoke HTTP `apply:false` em ingest-safe-outbound: 5/5 cenários comportaram correto
  (sku_direto, alias, kit_bom expandido, Clink bloqueado, desconhecido)
- BUILD_ID: 2026-05-28 19:09:16 UTC

## Limpeza Clink — decisão Pedro 2026-05-28

Pedro confirmou: Budamix não trabalha mais com Clink. Aplicado em produção:
- 1 SKU removido de `_catalog_estoque` (`CK4742_B`)
- 2 aliases marcados `active=false` (`CK4742_BB`, `CK4742`)
- 1 kit marcado `active=false` (`KIT2CK4742_B`)
- Família `familia_CK_jarra_clink` (150 SKUs / 332 movimentos divergentes)
  passou a contar como descontinuada — não cadastrar.
