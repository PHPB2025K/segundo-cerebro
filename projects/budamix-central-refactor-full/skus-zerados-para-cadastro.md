---
title: "SKUs Zerados — Para Cadastro/Atualização na Planilha de Precificação"
created: 2026-04-29
type: reference
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - skus-zerados
  - planilha
---

# SKUs Zerados — Para Cadastro/Atualização na Planilha de Precificação

> Lista de 51 registros do fulfillment_inventory com cost_price=0 ou NULL em 29/04/2026.
>
> Fonte de verdade: planilha `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU`
> Mapeamento das contas Shopee:
> - 448649947 = Budamix Store (aba SHOPEE 1)
> - 860803675 = Budamix Oficial (aba SHOPEE 2)
> - 442066454 = Budamix Shop (aba SHOPEE 3)

## Resumo

- Total: **51 registros zerados**
- Por marketplace: Amazon=15, ML=4, Shopee=32
- Valor de venda potencial sem custo: **R$ 53.136,52**
- SKUs com `sku_mapping`: **8** — candidatos a fallback automático na Fase 2D, não precisa cadastrar na planilha
- SKUs sem `sku_mapping`: **43** — precisa cadastrar/atualizar na planilha

## SHOPEE (aba SHOPEE) — para o analista da Shopee

| SKU | Conta | Qty | Valor Venda Potencial | Tem mapping? | Mapping para |
|---|---|---:|---:|---|---|
| `098` | Budamix Shop | 40 | R$ 5.138,80 | Sim | KIT9S098 × 1 |
| `KIT4YW800SQ_T` | Budamix Store | 30 | R$ 2.139,60 | Não | — |
| `KIT4YW800SQ_T` | Budamix Shop | 29 | R$ 2.068,57 | Não | — |
| `CK5168_B` | Budamix Shop | 26 | R$ 1.999,40 | Não | — |
| `CK5168_B` | Budamix Oficial | 26 | R$ 1.999,40 | Não | — |
| `CK5168_B` | Budamix Store | 26 | R$ 1.999,40 | Não | — |
| `KIT4YW800SQ_T` | Budamix Oficial | 27 | R$ 1.925,91 | Não | — |
| `098` | Budamix Oficial | 12 | R$ 1.541,64 | Sim | KIT9S098 × 1 |
| `DPM002` | Budamix Shop | 50 | R$ 1.525,50 | Não | — |
| `096` | Budamix Shop | 31 | R$ 1.483,66 | Sim | KIT3S096 × 1 |
| `KIT2YW800SQ_T` | Budamix Shop | 29 | R$ 1.210,17 | Não | — |
| `KIT2YW800SQ_T` | Budamix Oficial | 29 | R$ 1.210,17 | Não | — |
| `18928M` | Budamix Shop | 14 | R$ 1.048,60 | Não | — |
| `18928M` | Budamix Store | 14 | R$ 1.048,60 | Não | — |
| `18928M` | Budamix Oficial | 14 | R$ 1.048,60 | Não | — |
| `CTL002` | Budamix Oficial | 16 | R$ 1.006,40 | Sim | TL6250 × 1 |
| `KIT2WX11975` | Budamix Oficial | 25 | R$ 997,50 | Não | — |
| `KIT2WX11975` | Budamix Shop | 25 | R$ 997,50 | Não | — |
| `DPM002` | Budamix Oficial | 20 | R$ 610,20 | Não | — |
| `DPM002` | Budamix Store | 20 | R$ 610,20 | Não | — |
| `KIT2YW800SQ_T` | Budamix Store | 13 | R$ 542,49 | Não | — |
| `1920_T` | Budamix Oficial | 11 | R$ 119,90 | Não | — |
| `1920_T` | Budamix Shop | 11 | R$ 119,90 | Não | — |
| `1920_T` | Budamix Store | 11 | R$ 119,90 | Não | — |
| `KIT2405_B` | Budamix Oficial | 4 | R$ 115,60 | Não | — |
| `KIT2405_B` | Budamix Shop | 4 | R$ 115,60 | Não | — |
| `KIT2405_B` | Budamix Store | 4 | R$ 115,60 | Não | — |
| `PUMPB5_T` | Budamix Store | 6 | R$ 71,40 | Não | — |
| `BR20P1000P_T` | Budamix Store | 1 | R$ 54,90 | Não | — |
| `ER2806_T` | Budamix Shop | 1 | R$ 22,90 | Não | — |
| `ER2806_T` | Budamix Store | 1 | R$ 16,90 | Não | — |
| `ER2806_T` | Budamix Oficial | 1 | R$ 16,90 | Não | — |

## AMAZON (aba AMAZON)

| SKU | Conta | Qty | Valor Venda Potencial | Tem mapping? | Mapping para |
|---|---|---:|---:|---|---|
| `IMB501T-cinza` | FBA | 144 | R$ 4.305,60 | Sim | IMB501C_T × 1 |
| `IMB501T-vermelho` | FBA | 163 | R$ 4.221,70 | Sim | IMB501V_T × 1 |
| `IMB501T-preto` | FBA | 135 | R$ 3.496,50 | Sim | IMB501P_T × 1 |
| `DPM002` | FBA | 50 | R$ 1.745,00 | Não | — |
| `KIT2YW1520AZ` | FBA | 0 | R$ 0,00 | Sim | KIT2YW1520 × 1 |
| `PRA03P` | FBA | 1 | R$ 0,00 | Não | — |
| `SPC003` | FBA | 0 | R$ 0,00 | Não | — |
| `IMB501P_T` | FBA | 0 | R$ 0,00 | Não | — |
| `KIT12AL011__` | FBA | 1 | R$ 0,00 | Não | — |
| `KIT24FIT100M` | FBA | 0 | R$ 0,00 | Não | — |
| `1201602800019` | FBA | 1 | R$ 0,00 | Não | — |
| `213_BB` | FBA | 1 | R$ 0,00 | Não | — |
| `0063_` | FBA | 29 | R$ 0,00 | Não | — |
| `CK4818V_B` | FBA | 1 | R$ 0,00 | Não | — |
| `403_B` | FBA | 2 | R$ 0,00 | Não | — |

## ML (aba MELI)

| SKU | Conta | Qty | Valor Venda Potencial | Tem mapping? | Mapping para |
|---|---|---:|---:|---|---|
| `KIT2YW800SQ_T` | ML Full | 100 | R$ 4.190,00 | Não | — |
| `CLR002` | ML Full | 30 | R$ 1.947,00 | Não | — |
| `MLB6293133822` | ML Full | 2 | R$ 133,38 | Não | — |
| `MLB4597683007` | ML Full | 1 | R$ 55,53 | Não | — |

## SKUs com mapping (não precisa cadastrar — Fase 2D resolve)

Estes casos **não devem ser duplicados na planilha**. A Fase 2D deve usar `sku_mapping` para herdar custo do SKU pai com `quantity_multiplier`.

| SKU zerado | Marketplace | Conta | Qty | Valor Venda Potencial | Mapping para |
|---|---|---|---:|---:|---|
| `098` | Shopee | Budamix Shop | 40 | R$ 5.138,80 | `KIT9S098 × 1` |
| `IMB501T-cinza` | Amazon | FBA | 144 | R$ 4.305,60 | `IMB501C_T × 1` |
| `IMB501T-vermelho` | Amazon | FBA | 163 | R$ 4.221,70 | `IMB501V_T × 1` |
| `IMB501T-preto` | Amazon | FBA | 135 | R$ 3.496,50 | `IMB501P_T × 1` |
| `098` | Shopee | Budamix Oficial | 12 | R$ 1.541,64 | `KIT9S098 × 1` |
| `096` | Shopee | Budamix Shop | 31 | R$ 1.483,66 | `KIT3S096 × 1` |
| `CTL002` | Shopee | Budamix Oficial | 16 | R$ 1.006,40 | `TL6250 × 1` |
| `KIT2YW1520AZ` | Amazon | FBA | 0 | R$ 0,00 | `KIT2YW1520 × 1` |

## SKUs sem mapping (precisa cadastrar/atualizar na planilha)

| SKU | Marketplace | Conta | Qty | Valor Venda Potencial | Aba sugerida |
|---|---|---|---:|---:|---|
| `KIT2YW800SQ_T` | ML | ML Full | 100 | R$ 4.190,00 | MELI |
| `KIT4YW800SQ_T` | Shopee | Budamix Store | 30 | R$ 2.139,60 | SHOPEE |
| `KIT4YW800SQ_T` | Shopee | Budamix Shop | 29 | R$ 2.068,57 | SHOPEE |
| `CK5168_B` | Shopee | Budamix Shop | 26 | R$ 1.999,40 | SHOPEE |
| `CK5168_B` | Shopee | Budamix Oficial | 26 | R$ 1.999,40 | SHOPEE |
| `CK5168_B` | Shopee | Budamix Store | 26 | R$ 1.999,40 | SHOPEE |
| `CLR002` | ML | ML Full | 30 | R$ 1.947,00 | MELI |
| `KIT4YW800SQ_T` | Shopee | Budamix Oficial | 27 | R$ 1.925,91 | SHOPEE |
| `DPM002` | Amazon | FBA | 50 | R$ 1.745,00 | AMAZON |
| `DPM002` | Shopee | Budamix Shop | 50 | R$ 1.525,50 | SHOPEE |
| `KIT2YW800SQ_T` | Shopee | Budamix Shop | 29 | R$ 1.210,17 | SHOPEE |
| `KIT2YW800SQ_T` | Shopee | Budamix Oficial | 29 | R$ 1.210,17 | SHOPEE |
| `18928M` | Shopee | Budamix Shop | 14 | R$ 1.048,60 | SHOPEE |
| `18928M` | Shopee | Budamix Store | 14 | R$ 1.048,60 | SHOPEE |
| `18928M` | Shopee | Budamix Oficial | 14 | R$ 1.048,60 | SHOPEE |
| `KIT2WX11975` | Shopee | Budamix Oficial | 25 | R$ 997,50 | SHOPEE |
| `KIT2WX11975` | Shopee | Budamix Shop | 25 | R$ 997,50 | SHOPEE |
| `DPM002` | Shopee | Budamix Oficial | 20 | R$ 610,20 | SHOPEE |
| `DPM002` | Shopee | Budamix Store | 20 | R$ 610,20 | SHOPEE |
| `KIT2YW800SQ_T` | Shopee | Budamix Store | 13 | R$ 542,49 | SHOPEE |
| `MLB6293133822` | ML | ML Full | 2 | R$ 133,38 | MELI |
| `1920_T` | Shopee | Budamix Oficial | 11 | R$ 119,90 | SHOPEE |
| `1920_T` | Shopee | Budamix Shop | 11 | R$ 119,90 | SHOPEE |
| `1920_T` | Shopee | Budamix Store | 11 | R$ 119,90 | SHOPEE |
| `KIT2405_B` | Shopee | Budamix Oficial | 4 | R$ 115,60 | SHOPEE |
| `KIT2405_B` | Shopee | Budamix Shop | 4 | R$ 115,60 | SHOPEE |
| `KIT2405_B` | Shopee | Budamix Store | 4 | R$ 115,60 | SHOPEE |
| `PUMPB5_T` | Shopee | Budamix Store | 6 | R$ 71,40 | SHOPEE |
| `MLB4597683007` | ML | ML Full | 1 | R$ 55,53 | MELI |
| `BR20P1000P_T` | Shopee | Budamix Store | 1 | R$ 54,90 | SHOPEE |
| `ER2806_T` | Shopee | Budamix Shop | 1 | R$ 22,90 | SHOPEE |
| `ER2806_T` | Shopee | Budamix Store | 1 | R$ 16,90 | SHOPEE |
| `ER2806_T` | Shopee | Budamix Oficial | 1 | R$ 16,90 | SHOPEE |
| `PRA03P` | Amazon | FBA | 1 | R$ 0,00 | AMAZON |
| `SPC003` | Amazon | FBA | 0 | R$ 0,00 | AMAZON |
| `IMB501P_T` | Amazon | FBA | 0 | R$ 0,00 | AMAZON |
| `KIT12AL011__` | Amazon | FBA | 1 | R$ 0,00 | AMAZON |
| `KIT24FIT100M` | Amazon | FBA | 0 | R$ 0,00 | AMAZON |
| `1201602800019` | Amazon | FBA | 1 | R$ 0,00 | AMAZON |
| `213_BB` | Amazon | FBA | 1 | R$ 0,00 | AMAZON |
| `0063_` | Amazon | FBA | 29 | R$ 0,00 | AMAZON |
| `CK4818V_B` | Amazon | FBA | 1 | R$ 0,00 | AMAZON |
| `403_B` | Amazon | FBA | 2 | R$ 0,00 | AMAZON |

## Observações operacionais

- Ordenação por marketplace e valor de venda potencial, para o analista atacar primeiro o que mais distorce o KPI **Valor Custo**.
- Para Shopee, a coluna **Conta** já traduz `shop_id` para a conta operacional.
- Casos com `sku_mapping` devem ser tratados pelo fallback automático da Fase 2D; não cadastrar duplicado na planilha sem revisar.
- Consulta executada em modo read-only no Supabase; nenhum dado foi alterado.
