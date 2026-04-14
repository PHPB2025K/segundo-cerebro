---
title: "classificacoes"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Classificações de Transação — Extrato Shopee

## Mapeamento Status → Classificação

| order_status (Shopee) | Tipo Técnico | Classificação (PT-BR) | Cor no Resumo |
|---|---|---|---|
| COMPLETED | SETTLEMENT | Venda Concluída | 🟢 Verde |
| CANCELLED | REFUND | Devolução/Cancelamento | 🔴 Vermelho |
| IN_CANCEL | DISPUTE | Em Cancelamento/Disputa | 🔴 Vermelho |
| SHIPPED | PENDING | Em Trânsito | 🟡 Amarelo |
| READY_TO_SHIP | PENDING | Aguardando Envio | 🟡 Amarelo |
| PROCESSED | PENDING | Processando | 🟡 Amarelo |
| UNPAID | PENDING | Aguardando Pagamento | 🟡 Amarelo |
| INVOICE_PENDING | PENDING | Aguardando NF | 🟡 Amarelo |

## Equivalência com ML

| Shopee | Mercado Livre | Notas |
|---|---|---|
| SETTLEMENT | SETTLEMENT | Venda paga e liberada |
| REFUND | REFUND | Valor devolvido ao comprador |
| DISPUTE | DISPUTE | Reclamação em andamento |
| PENDING | — | ML não lista pedidos pendentes no extrato financeiro |

## Regras de Classificação

1. **SETTLEMENT (Venda Concluída)**: Pedido com `order_status == COMPLETED`. O comprador confirmou recebimento ou o prazo de garantia expirou. O escrow foi (ou será) liberado ao vendedor.

2. **REFUND (Devolução/Cancelamento)**: Pedido com `order_status == CANCELLED`. Pode ser cancelamento pelo comprador, pelo vendedor, ou automático. O valor não será creditado ao vendedor.

3. **DISPUTE (Em Cancelamento/Disputa)**: Pedido com `order_status == IN_CANCEL`. Processo de cancelamento/devolução em andamento. Resultado ainda indefinido.

4. **PENDING**: Pedidos em status intermediário (SHIPPED, READY_TO_SHIP, PROCESSED, UNPAID, INVOICE_PENDING). Ainda não houve liberação financeira. Incluídos no extrato para visibilidade, mas não contabilizados como receita confirmada.

## Status de Liquidação

| Condição | Status | Significado |
|---|---|---|
| escrow_release_time preenchido | Recebido | Valor já creditado na conta Shopee |
| order_status == CANCELLED | Cancelado | Não será liquidado |
| Qualquer outro caso | Pendente | Aguardando conclusão do pedido |

## Cores do Resumo

| Cor | Hex | Uso |
|---|---|---|
| 🟢 Verde | #E8F5E9 | Entradas positivas (vendas, total bruto, recebido) |
| 🔴 Vermelho | #FFEBEE | Saídas (devoluções, disputas, taxas) |
| 🟡 Amarelo | #FFF8E1 | Neutro/parcial (frete, pendente, cupons) |
| 🔵 Azul | #E3F2FD | Saldo líquido final |
