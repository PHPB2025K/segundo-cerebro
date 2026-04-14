---
title: "meli columns"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
  - pricing
---

# Mapeamento de Colunas — ABA MELI

> Headers: row 6 | Dados: row 7+
> INPUT: A, B, D, E, F, G, H, M, N, P, X
> FORMULA (NUNCA TOCAR): C, I, J, K, L, O, Q, R, S, T, U, V, W, Y, Z, AA

| Col | Campo | Tipo | Formula |
|-----|-------|------|---------|
| A | ESTOQUE | INPUT | Quantidade. ArrayFormula pode existir — se sim, manter |
| B | SKU REFERENCIA | INPUT | Texto livre — SKU de referencia, nao icone |
| C | STATUS | FORMULA | `=IF(A=0,"SEM ESTOQUE",IF(A>=100,"OK",IF(A>=15,"REPOR ESTOQUE","ESTOQUE MINIMO")))` |
| D | SKU | INPUT | Codigo interno Budamix |
| E | PRODUTO | INPUT | Titulo resumido |
| F | PRECO DE CUSTO | INPUT | Valor numerico (ex: 1.04). ArrayFormula pode existir |
| G | PRECO DE VENDA | INPUT | Valor numerico (ex: 19.90) |
| H | ANUNCIO | INPUT | "Classico" ou "Premium" (sem acento OK) |
| I | FRETE CHEIO | FORMULA | `=G*0.28` |
| J | COMISSAO ML | FORMULA | `=IF(H="Classico",G*12.5%,IF(H="Premium",G*17.5%,0))` |
| K | CUSTO FIXA | FORMULA | `=IF(G<12.5,G*50%,0)` |
| L | IMPOSTO | FORMULA | `=G*7%` |
| M | CAIXA | INPUT | Custo da caixa (ex: 0.97) |
| N | FULL | INPUT | Custo armazenagem Full (opcional, pode ser vazio) |
| O | DEVOLUCOES | FORMULA | `=G*0.04` |
| P | EMBALAGEM | INPUT | Custo de embalagem (ex: 0.50) |
| Q | ADS | FORMULA | `=G*0.06` |
| R | FRETE | FORMULA | `=IF(G<79.9,0,IF(OR(H="Classico",H="Classico"),I*50%,IF(H="Premium",I*70%,0)))` |
| S | COMISSAO AFILIADO | FORMULA | `=G*0.1` |
| T | MARGEM | FORMULA | `=(U*100)/G/100` |
| U | LUCRO LIQ | FORMULA | `=G-F-J-K-L-M-P-R-Q-O` |
| V | MARGEM VENDA AFILIADO | FORMULA | `=(W*100)/G/100` |
| W | LUCRO LIQ VENDA AFILIADO | FORMULA | `=G-F-J-K-L-M-P-R-Q-S-O` |
| X | EAN | INPUT | Codigo de barras (texto) |
| Y | NCM | FORMULA | VLOOKUP do EAN na aba ESTOQUE |
| Z | PESO | FORMULA | VLOOKUP do EAN na aba ESTOQUE |
| AA | MARCA | FORMULA | VLOOKUP do EAN na aba ESTOQUE |
