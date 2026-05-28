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

1. **Integração com o motor TypeScript** (Etapa 5 do plano, parte de código).
   O resolver vive no Postgres. As rotas `/api/sheets/update`,
   `/api/stock-movements/ingest-safe-outbound` e `/api/stock-movements/ingest-envios-full`
   continuam fazendo match direto contra a planilha — precisam ser refatoradas
   para chamar `supabase.rpc('resolver_sku', { p_sku_raw })`. **Esse trabalho é do Kobe.**

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

## Riscos abertos (não tratados nesta sessão)

- RLS continua **desabilitado** em `stock_movements`, `stock_movement_evidences`,
  `sku_aliases`, `kit_bom` (e mais 9 tabelas). Advisor crítico do Supabase ativo.
- PM2 do `estoque-budamix` continua rodando build de 20/05 — código da Fase 2
  do Kobe não está em produção.
- Repo VPS sem commits (git mostra "No commits yet").
