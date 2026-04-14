---
title: "classificacoes"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Classificações de Transação — Extrato Amazon BR

## Mapeamento Evento → Classificação

| Lista de Eventos (SP-API) | Tipo Técnico | Classificação (PT-BR) | Cor no Resumo |
|---|---|---|---|
| ShipmentEventList | SETTLEMENT | Venda Concluída | 🟢 Verde |
| RefundEventList | REFUND | Devolução / Reembolso | 🔴 Vermelho |
| GuaranteeClaimEventList | DISPUTE | Disputa A-to-Z | 🔴 Vermelho |
| ServiceFeeEventList | SERVICE_FEE | Taxa de Serviço | 🔴 Vermelho |
| AdjustmentEventList | ADJUSTMENT | Ajuste | 🟡 Amarelo |

## Equivalência com ML e Shopee

| Amazon | Mercado Livre | Shopee | Notas |
|---|---|---|---|
| SETTLEMENT | SETTLEMENT | SETTLEMENT | Venda paga e processada |
| REFUND | REFUND | REFUND | Valor devolvido ao comprador |
| DISPUTE | DISPUTE | DISPUTE (IN_CANCEL) | Reclamação/garantia em andamento |
| SERVICE_FEE | — | — | Taxas avulsas (FBA Storage, etc.) |
| ADJUSTMENT | — | — | Ajustes: WAREHOUSE_DAMAGE, REVERSAL, etc. |
| — | SETTLEMENT_SHIPPING | — | Amazon não separa frete como evento |
| — | REFUND_SHIPPING | — | Amazon não separa estorno de frete |

## Regras de Classificação

1. **SETTLEMENT (Venda Concluída)**: Evento em `ShipmentEventList`. Pedido enviado e fees cobradas. O settlement será creditado ao vendedor no próximo ciclo de pagamento.

2. **REFUND (Devolução / Reembolso)**: Evento em `RefundEventList`. Valores de charges são negativos (dinheiro devolvido ao comprador). Fees são parcialmente revertidas (valores positivos).

3. **DISPUTE (Disputa A-to-Z)**: Evento em `GuaranteeClaimEventList`. Garantia A-to-Z acionada pelo comprador. Mesma estrutura de ShipmentEvent.

4. **SERVICE_FEE (Taxa de Serviço)**: Evento em `ServiceFeeEventList`. Taxas avulsas como FBAStorageFee, FBADisposalFee, etc. Não vinculadas a pedidos específicos.

5. **ADJUSTMENT (Ajuste)**: Evento em `AdjustmentEventList`. Tipos incluem:
   - `WAREHOUSE_DAMAGE`: Reembolso por dano no armazém FBA
   - `REVERSAL`: Reversão de transação anterior
   - `FREE_REPLACEMENT_REFUND_ITEMS`: Substituição gratuita

## Status de Liquidação

| Condição | Status | Significado |
|---|---|---|
| ProcessingStatus == "Closed" | Recebido | Settlement já creditado |
| ProcessingStatus == "Open" | Pendente | Aguardando próximo ciclo |

## Cores do Resumo

| Cor | Hex | Uso |
|---|---|---|
| 🟢 Verde | #E8F5E9 | Entradas positivas (vendas, recebido) |
| 🔴 Vermelho | #FFEBEE | Saídas (devoluções, disputas, taxas) |
| 🟡 Amarelo | #FFF8E1 | Neutro/parcial (ajustes, cupons) |
| 🔵 Azul | #E3F2FD | Saldo líquido final |
