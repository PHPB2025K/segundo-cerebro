---
title: "DRE Abril 2026 — U15 e U44 v4"
created: 2026-05-06
type: financeiro
status: fechado
tags:
  - financeiro/dre
  - gb-importadora
  - date/2026-05
---

# DRE Abril 2026 — U15 e U44 v4

_Fechado em 2026-05-06 19:39 BRT._

## U15 — Descontos Concedidos

Critério: desconto explícito financiado pelo seller em pedido válido de abril/2026. Excluir preço riscado/promocional, voucher/subsídio da plataforma, moedas Shopee e promoção de frete.

| Marketplace | Valor U15 | Base validada | % da base | Observação |
|---|---:|---:|---:|---|
| Mercado Livre | R$ 5.061,14 | R$ 120.764,44 | 4,19% | Critério já revalidado e aceito: desconto explícito do seller em pedidos válidos. |
| Shopee | R$ 0,00 | R$ 257.064,42 | 0,00% | `seller_voucher=0`; `shopee_voucher=0`; `coins=R$ 582,87` excluído por ser voucher/plataforma/moedas, não desconto seller. |
| Amazon | R$ 0,00 | R$ 28.010,79 | 0,00% | Promoções financeiras de abril batem como promoção de frete: shipment promo R$ 1.102,80 e refund reversal R$ 83,88, líquido R$ 1.018,92; item-promotion seller = R$ 0,00. |
| **Consolidado** | **R$ 5.061,14** | **R$ 405.839,65** | **1,25%** | Número final para U15 no DRE. |

## U44 v4 — Quebra limpa das taxas de marketplace

Critério v4: U44 limpa deve conter comissão + taxa fixa/service/transaction/FBA + frete líquido seller quando aplicável. Outras taxas ficam em linha separada abaixo da U44 para não contaminar leitura operacional.

### U44 limpa

| Marketplace | U44 limpa |
|---|---:|
| Mercado Livre | R$ 41.539,31 |
| Shopee | R$ 60.132,34 |
| Amazon | R$ 7.565,05 |
| **Total U44 limpa** | **R$ 109.236,70** |

### Outras Taxas Marketplace

| Marketplace | Outras Taxas | Composição |
|---|---:|---|
| Mercado Livre | R$ 6.156,26 | Disputas/cancelamentos R$ 3.769,11 + taxas de reembolso/devolução R$ 2.387,15 |
| Amazon | R$ 138,72 | Ajustes/taxas vinculadas a refund/reembolso |
| Shopee | R$ 0,00 | Sem reclassificação para outras taxas nesta v4 |
| **Total Outras Taxas Marketplace** | **R$ 6.294,98** |  |

## Reconciliação obrigatória

- U44 limpa: **R$ 109.236,70**
- Outras Taxas Marketplace: **R$ 6.294,98**
- Total reconciliado: **R$ 115.531,68**
- Total DRE corrigido anterior: **R$ 115.531,68**
- Diferença: **R$ 0,00**

Conclusão: a v4 reorganiza a leitura gerencial sem alterar EBITDA/LL gerencial.
