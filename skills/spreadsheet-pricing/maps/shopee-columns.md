---
title: "shopee columns"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
  - pricing
---

# Mapeamento de Colunas — ABA SHOPEE

> Headers: row 6 | Dados: row 7+
> INPUT: A, D, E, F, G, I, L, O, P, Q, W
> FORMULA (NUNCA TOCAR): B, C, H, J, K, M, N, R, X, Y, Z
> ATENCAO ESPECIAL: S, T, U, V — copiar formula da row anterior ao inserir

| Col | Campo | Tipo | Formula |
|-----|-------|------|---------|
| A | ESTOQUE | INPUT | Quantidade. ArrayFormula pode existir |
| B | ICONE | FORMULA | Icone de status |
| C | STATUS | FORMULA | `=IF(A=0,"SEM ESTOQUE",IF(A>=100,"OK",IF(A>=15,"REPOR ESTOQUE","ESTOQUE MINIMO")))` |
| D | SKU | INPUT | Codigo interno Budamix |
| E | PRODUTO | INPUT | Titulo resumido |
| F | PRECO DE CUSTO | INPUT | Valor numerico. ArrayFormula pode existir |
| G | PRECO DE VENDA | INPUT | Valor numerico |
| H | COMISSAO | FORMULA | `=G*IF(G<=79.99,20%,14%)` |
| I | TAXA TRANSACAO | INPUT | Valor fixo (ex: 0.48). NAO e formula |
| J | TAXA FIXA | FORMULA | `=IF(G<=79.99,4,IF(G<=99.99,16,IF(G<=199.99,20,IF(G<=499.99,26,26))))` |
| K | IMPOSTO | FORMULA | `=G*0.07` |
| L | FRETE | INPUT | Valor fixo. NAO e formula |
| M | DEVOLUCOES | FORMULA | `=G*0.04` |
| N | ADS | FORMULA | `=G*0.05` |
| O | CAIXA | INPUT | Custo da caixa |
| P | EMBALAGEM | INPUT | Custo de embalagem |
| Q | BILHETE | INPUT | Valor do bilhete (ex: 0.05) |
| R | COMISSAO AFILIADO | FORMULA | `=G*0.1` |
| S | MARGEM | COPIAR FORMULA | Pode ser estatico em rows antigas. Ao inserir nova row, copiar formula da row anterior |
| T | LUCRO LIQ | COPIAR FORMULA | Idem S |
| U | MARGEM VENDA AFILIADO | COPIAR FORMULA | Idem S |
| V | LUCRO LIQ VENDA AFILIADO | COPIAR FORMULA | Idem S |
| W | EAN | INPUT | Codigo de barras (texto) |
| X | NCM | FORMULA | VLOOKUP do EAN na aba ESTOQUE |
| Y | PESO | FORMULA | VLOOKUP do EAN na aba ESTOQUE |
| Z | MARCA | FORMULA | VLOOKUP do EAN na aba ESTOQUE |
