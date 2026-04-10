# Referência de Colunas — Extrato ML

## Colunas do extrato (23 colunas)

| # | Coluna | Tipo | Fonte API | Descrição |
|---|---|---|---|---|
| 1 | Ref. Externa | texto | order.id ou payment.id | Referência externa (ID do pedido ML) |
| 2 | ID Origem | número | payment.id | ID único do pagamento no Mercado Pago |
| 3 | ID Usuário | número | collector_id | ID do vendedor (532562281) |
| 4 | Tipo Pagamento | texto | payment_type_id | Tipo: credit_card, debit_card, account_money, available_money |
| 5 | Método | texto | payment_method_id | Método específico: visa, mastercard, pix, elo, etc |
| 6 | Site | texto | fixo | Sempre "MLB" (Mercado Livre Brasil) |
| 7 | Tipo (técnico) | texto | calculado | Classificação técnica: SETTLEMENT, REFUND, DISPUTE, etc |
| 8 | Classificação | texto | calculado | Classificação em português: Venda Concluída, Devolução, etc |
| 9 | Valor (R$) | decimal | transaction_amount | Valor bruto da transação |
| 10 | Moeda | texto | currency_id | Moeda (BRL) |
| 11 | Data Transação | datetime | date_created | Data/hora da criação do pagamento |
| 12 | Taxas (R$) | decimal | calculado | Diferença entre bruto e líquido (valor negativo = cobrança) |
| 13 | Valor Líquido (R$) | decimal | transaction_details.net_received_amount | Valor efetivamente recebido pelo vendedor |
| 14 | Moeda Liq. | texto | currency_id | Moeda da liquidação (BRL) |
| 15 | Data Liquidação | datetime | date_approved | Data/hora da aprovação/liquidação |
| 16 | Status Liquidação | texto | calculado | Recebido / Pendente / Cancelado |
| 17 | Valor Real (R$) | decimal | net_received_amount | Igual ao Valor Líquido (compatibilidade com modelo anterior) |
| 18 | Cupom (R$) | decimal | coupon_amount | Valor de cupom/desconto aplicado |
| 19 | Metadata | JSON | charges_details | Detalhes das cobranças (comissões, frete, taxas) |
| 20 | ID Pedido | texto | order.id | ID do pedido no Mercado Livre |
| 21 | ID Envio | texto | charges_details.metadata.shipment_id | ID do envio/remessa |
| 22 | Modo Envio | texto | fixo | Modo de envio (me2 = Mercado Envios 2) |
| 23 | ID Pack | texto | pack_id | ID do pack (compras múltiplas no mesmo carrinho) |

## Lógica de classificação

```
SE status == 'refunded' OU amount < 0:
    SE descrição contém 'shipment': REFUND_SHIPPING
    SENÃO: REFUND
SE descrição contém 'shipment': SETTLEMENT_SHIPPING
SE status in ('rejected','cancelled') OU status_detail in ('bpp_refunded','mediation','chargeback'): DISPUTE
SENÃO: SETTLEMENT
```

## Lógica de status de liquidação

```
SE date_approved preenchido: Recebido
SE status in ('rejected','cancelled','refunded'): Cancelado
SENÃO: Pendente
```

## Cálculo de taxas

```
taxas = -(valor_bruto - valor_liquido)  # Negativo = cobrança do ML
```

Quando taxas = 0 e valor_bruto = valor_liquido, não houve cobrança (ex: repasse de frete).
