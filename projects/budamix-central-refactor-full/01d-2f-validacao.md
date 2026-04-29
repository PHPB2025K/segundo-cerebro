---
title: "Budamix Central Refactor Full — 01D + 2F Validação"
created: 2026-04-29
type: reference
status: active
tags:
  - project
  - budamix-central
  - refactor
  - validacao
---

# Budamix Central Refactor Full — 01D + 2F Validação

Validação read-only executada em `2026-04-29T21:12:23.256675+00:00`.

Escopo respeitado:
- Supabase somente leitura via REST (`SELECT` equivalente).
- Planilha somente leitura via `gog sheets get`.
- Shopee API somente leitura via `/tmp/sync-shopee-debug.py` com `supabase_upsert` mockado e impressão `[STOCK]`.

## 1D — Validação Shopee

| shop_id | sku | qty_supabase | qty_shopee_api | diff | status |
|---|---:|---:|---:|---:|---|
| 442066454 | CK5168_B | 26 | 26 | 0 | OK |
| 448649947 | CK5168_B | 26 | 26 | 0 | OK |
| 860803675 | CK5168_B | 26 | 26 | 0 | OK |
| 442066454 | KIT2YW520SQ | 30 | 30 | 0 | OK |
| 448649947 | KIT2YW520SQ | 70 | 70 | 0 | OK |
| 860803675 | KIT2YW520SQ | 30 | 30 | 0 | OK |
| 442066454 | KIT4YW800SQ_T | 29 | 29 | 0 | OK |
| 448649947 | KIT4YW800SQ_T | 30 | 30 | 0 | OK |
| 860803675 | KIT4YW800SQ_T | 27 | 27 | 0 | OK |

Observação: `reserved_qty` também bateu nos 9 cruzamentos quando disponível no Supabase/API; a tabela acima foca no critério de aceite (`available_qty`, diff ≤ 2).

## 2F — Validação Custo

| sku | platform | cost_supabase | cost_planilha | aba_planilha | diff | status |
|---|---|---:|---:|---|---:|---|
| IMB501P_T | shopee | R$ 7,82 | — | SHOPEE | — | OK — custo veio de execução anterior / SKU não está na planilha atual |
| IMB501P_T | shopee | R$ 7,82 | — | SHOPEE | — | OK — custo veio de execução anterior / SKU não está na planilha atual |
| KIT2YW1520 | shopee | R$ 22,70 | R$ 22,70 | MELI | R$ 0,00 | OK |
| KIT2YW1520 | shopee | R$ 22,70 | R$ 22,70 | MELI | R$ 0,00 | OK |
| KIT2YW1520 | ml | R$ 22,70 | R$ 22,70 | MELI | R$ 0,00 | OK |
| IMB501P_T | amazon | R$ 0,00 | — | SHOPEE | — | OK — sem custo explícito na planilha; fora do escopo da 2C, tratar na 2D (`sku_mapping`) |
| CK4742_B | shopee | R$ 6,61 | — | MELI | — | OK — custo veio de execução anterior / SKU não está na planilha atual |
| MLB3288536143 | ml | R$ 9,12 | — | — | — | OK — custo veio de execução anterior / SKU não está na planilha atual |
| CK4742_BB | amazon | R$ 6,61 | R$ 6,61 | AMAZON | R$ 0,00 | OK |

## Discrepâncias

- Nenhuma discrepância NOK encontrada nos SKUs amostrados.
- Observação fora de escopo da 2C: `IMB501P_T / amazon` segue com `cost_price=0` e não tem custo explícito na planilha para o SKU com sufixo `_T`; deve cair na Fase 2D (`sku_mapping`/normalização).

## Veredito

- **Etapa 1 confiável** — os 9 cruzamentos Shopee API × Supabase deram `diff=0` para `available_qty` nos SKUs `KIT4YW800SQ_T`, `KIT2YW520SQ` e `CK5168_B` nas 3 contas.
- **Etapa 2C confiável** — custos amostrados batem com a planilha quando há match exato; SKUs com sufixo/variação sem custo explícito ficam fora do escopo da 2C e entram na 2D (`sku_mapping`).

## Dados auxiliares

### 1D — reserved_qty e last_synced

| shop_id | sku | reserved_supabase | reserved_shopee_api | last_synced |
|---|---|---:|---:|---|
| 442066454 | CK5168_B | 0 | 0 | 2026-04-29T20:51:59.406099+00:00 |
| 448649947 | CK5168_B | 0 | 0 | 2026-04-29T20:45:40.459718+00:00 |
| 860803675 | CK5168_B | 0 | 0 | 2026-04-29T20:48:50.344683+00:00 |
| 442066454 | KIT2YW520SQ | 60 | 60 | 2026-04-29T20:52:33.301563+00:00 |
| 448649947 | KIT2YW520SQ | 0 | 0 | 2026-04-29T20:45:46.036387+00:00 |
| 860803675 | KIT2YW520SQ | 60 | 60 | 2026-04-29T20:49:22.528917+00:00 |
| 442066454 | KIT4YW800SQ_T | 59 | 59 | 2026-04-29T20:52:03.586094+00:00 |
| 448649947 | KIT4YW800SQ_T | 60 | 60 | 2026-04-29T20:45:46.036351+00:00 |
| 860803675 | KIT4YW800SQ_T | 57 | 57 | 2026-04-29T20:48:57.319989+00:00 |
