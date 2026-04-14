---
title: "estoque columns"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
  - pricing
---

# Mapeamento de Colunas — ABA ESTOQUE

> Headers: row 8 | Dados: row 9+
> INPUT: A, C, E, F, G, H, I
> FORMULA (NUNCA TOCAR): D, J, K
> ESTA ABA E A FONTE DE VERDADE — preencher SEMPRE PRIMEIRO

| Col | Campo | Tipo | Formula |
|-----|-------|------|---------|
| A | ESTOQUE | INPUT | Quantidade em estoque |
| B | — | — | Vazio |
| C | SKU | INPUT | Codigo interno Budamix |
| D | STATUS | FORMULA | `=IF(A=0,"SEM ESTOQUE",IF(A>=100,"OK",IF(A>=15,"REPOR ESTOQUE","ESTOQUE MINIMO")))` |
| E | PRODUTO | INPUT | Titulo resumido |
| F | PRECO DE CUSTO | INPUT | Valor numerico |
| G | EAN | INPUT | Codigo de barras (texto). Chave para VLOOKUP de MELI e SHOPEE |
| H | NCM | INPUT | Codigo fiscal (ex: 4411.12.10) |
| I | MARCA | INPUT | Nome da marca (ex: BUDAMIX) |
| J | VALOR ESTOQUE | FORMULA | `=A*F` (estoque x custo) |
| K | (calc auxiliar) | FORMULA | `=IF(L="","",L*F)` |

## Importancia da aba ESTOQUE

Esta aba alimenta via VLOOKUP:
- MELI cols Y (NCM), Z (PESO), AA (MARCA) — lookup por EAN (col G)
- SHOPEE cols X (NCM), Y (PESO), Z (MARCA) — lookup por EAN (col G)
- AMAZON cols T (NCM), U (PESO), V (MARCA) — lookup por SKU (col C)

**Se o produto nao estiver na aba ESTOQUE, os VLOOKUPs das abas de marketplace vao retornar #N/A.**
