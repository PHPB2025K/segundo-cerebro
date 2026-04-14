---
title: "colunas"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Referência de Colunas — Extrato Shopee

## Colunas do extrato (23 colunas)

| # | Coluna | Tipo | Fonte API Shopee | Descrição |
|---|---|---|---|---|
| 1 | Ref. Externa | texto | order_sn | Número do pedido Shopee |
| 2 | ID Origem | texto | order_sn | Mesmo que Ref. Externa (Shopee não tem payment_id separado) |
| 3 | ID Usuário | número | shop_id | ID da loja (448649947) |
| 4 | Tipo Pagamento | texto | buyer_payment_info.buyer_payment_method | Tipo: credit_card, wallet, etc. |
| 5 | Método | texto | buyer_payment_info.buyer_payment_method | Método específico: Pix, Cartão, etc. |
| 6 | Site | texto | fixo | Sempre "SHOPEE_BR" |
| 7 | Tipo (técnico) | texto | calculado | Classificação técnica: SETTLEMENT, REFUND, DISPUTE, PENDING |
| 8 | Classificação | texto | calculado | Em português: Venda Concluída, Devolução, etc. |
| 9 | Valor (R$) | decimal | order_income.cost_of_goods_sold | Valor bruto dos produtos |
| 10 | Moeda | texto | fixo | Sempre "BRL" |
| 11 | Data Transação | datetime | create_time | Data de criação do pedido |
| 12 | Taxas (R$) | decimal | calculado | Soma: commission + service + transaction + campaign + fbs fees |
| 13 | Valor Líquido (R$) | decimal | order_income.escrow_amount | Valor efetivamente recebido pelo vendedor |
| 14 | Moeda Liq. | texto | fixo | Sempre "BRL" |
| 15 | Data Liquidação | datetime | escrow_release_time | Data de liberação do pagamento |
| 16 | Status Liquidação | texto | calculado | Recebido / Pendente / Cancelado |
| 17 | Valor Real (R$) | decimal | order_income.escrow_amount | Igual ao Valor Líquido (compatibilidade) |
| 18 | Cupom (R$) | decimal | calculado | seller_voucher + shopee_voucher + coins |
| 19 | Metadata | JSON | compilado | Breakdown completo de fees em JSON |
| 20 | ID Pedido | texto | order_sn | ID do pedido Shopee |
| 21 | ID Envio | texto | tracking_number | Código de rastreio |
| 22 | Modo Envio | texto | shipping_carrier | Transportadora (SLS = Shopee Logistics Service) |
| 23 | ID Pack | texto | — | Não aplicável na Shopee (vazio) |

## Cálculo de Taxas

```
total_taxas = commission_fee + service_fee + max(|transaction_fee|, |credit_card_transaction_fee|) + campaign_fee + fbs_fee
```

Todos os valores de taxa são negativos na API Shopee.

## Cálculo de Cupons

```
total_cupom = seller_voucher + shopee_voucher + coins
```

## Status de Liquidação

```
SE escrow_release_time preenchido → Recebido
SE order_status == CANCELLED → Cancelado
SENÃO → Pendente
```
