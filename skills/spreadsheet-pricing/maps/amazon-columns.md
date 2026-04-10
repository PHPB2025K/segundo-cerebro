# Mapeamento de Colunas — ABA AMAZON

> Headers: row 6 | Dados: row 7+
> NOTA: Rows 7-9 tem dados quebrados na col F. Usar row 10+ como referencia.
> INPUT: D, E, F, G, I, K, L, M, S
> FORMULA (NUNCA TOCAR): C, H, J, N, O, Q, R, T, U, V
> ATENCAO: Col A pode ser INPUT ou FORMULA — verificar antes de escrever

| Col | Campo | Tipo | Formula |
|-----|-------|------|---------|
| A | ESTOQUE | INPUT/FORMULA | Algumas rows tem `=MIN(ESTOQUE!ref)`, outras sao input direto. VERIFICAR antes de escrever |
| B | — | — | Vazio na maioria |
| C | STATUS | FORMULA | `=IF(A=0,"SEM ESTOQUE",IF(A>=100,"OK",IF(A>=15,"REPOR ESTOQUE","ESTOQUE MINIMO")))` |
| D | SKU | INPUT | Codigo interno Budamix |
| E | PRODUTO | INPUT | Titulo resumido |
| F | PRECO DE CUSTO | INPUT | Valor numerico |
| G | PRECO DE VENDA | INPUT | Valor numerico |
| H | COMISSAO AMZ | FORMULA | `=G*0.12` |
| I | TARIFA FBA | INPUT | Valor fixo (ex: 5.00). NAO e formula |
| J | IMPOSTO | FORMULA | `=G*7%` |
| K | CAIXA | INPUT | Custo da caixa |
| L | EMBALAGEM | INPUT | Custo de embalagem |
| M | FRETE | INPUT | Custo de frete (pode ser 0) |
| N | ADS | FORMULA | `=G*0.089` |
| O | DEVOLUCOES | FORMULA | `=G*0.04` |
| P | — | — | Vazio |
| Q | MARGEM | FORMULA | `=(R*100)/G/100` |
| R | LUCRO LIQ | FORMULA | `=G-F-H-I-J-L-M-O-P-N-K` |
| S | EAN | INPUT | Codigo de barras (texto) |
| T | NCM | FORMULA | VLOOKUP do SKU na aba ESTOQUE |
| U | PESO | FORMULA | VLOOKUP do SKU na aba ESTOQUE |
| V | MARCA | FORMULA | VLOOKUP do SKU na aba ESTOQUE |
