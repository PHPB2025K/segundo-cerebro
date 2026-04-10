# Referência de Colunas — Extrato Amazon BR

## Colunas do extrato (23 colunas)

| # | Coluna | Tipo | Fonte API (SP-API Finances) | Descrição |
|---|---|---|---|---|
| 1 | Ref. Externa | texto | AmazonOrderId | ID do pedido Amazon |
| 2 | ID Origem | texto | AmazonOrderId | Mesmo que Ref. Externa (Amazon não tem payment_id separado) |
| 3 | ID Usuário | texto | Seller ID (fixo) | Identificação do vendedor |
| 4 | Tipo Pagamento | texto | — | Amazon não expõe método de pagamento do comprador |
| 5 | Método | texto | fixo | Sempre "Amazon Pay" |
| 6 | Site | texto | fixo | Sempre "AMAZON_BR" |
| 7 | Tipo (técnico) | texto | calculado | SETTLEMENT, REFUND, DISPUTE, SERVICE_FEE, ADJUSTMENT |
| 8 | Classificação | texto | calculado | Venda Concluída, Devolução, Disputa A-to-Z, Taxa de Serviço, Ajuste |
| 9 | Valor (R$) | decimal | soma ItemChargeList/ItemChargeAdjustmentList | Valor bruto (Principal + Tax + ShippingCharge + ShippingTax) |
| 10 | Moeda | texto | CurrencyCode | Sempre "BRL" para marketplace BR |
| 11 | Data Transação | datetime | PostedDate | Data de postagem do evento financeiro |
| 12 | Taxas (R$) | decimal | soma ItemFeeList/ItemFeeAdjustmentList | Commission + FBA fees (valores negativos) |
| 13 | Valor Líquido (R$) | decimal | charges + fees + promotions | Valor efetivamente recebido/debitado |
| 14 | Moeda Liq. | texto | fixo | Sempre "BRL" |
| 15 | Data Liquidação | datetime | PostedDate | Mesma que Data Transação (Amazon liquida no settlement) |
| 16 | Status Liquidação | texto | FinancialEventGroup.ProcessingStatus | Recebido / Pendente |
| 17 | Valor Real (R$) | decimal | = Valor Líquido | Igual ao Valor Líquido (compatibilidade) |
| 18 | Cupom (R$) | decimal | soma PromotionList/PromotionAdjustmentList | Promoções aplicadas (valores negativos) |
| 19 | Metadata | JSON | compilado | Breakdown completo: SKU, qty, charges, fees, promotions |
| 20 | ID Pedido | texto | AmazonOrderId | ID do pedido Amazon |
| 21 | ID Envio | texto | ShipmentId | ID do envio/remessa |
| 22 | Modo Envio | texto | FulfillmentChannel / ShipmentId | FBA ou MFN |
| 23 | ID Pack | texto | — | Não aplicável na Amazon (vazio) |

## Tipos de Charge (ItemChargeList)

| ChargeType | Descrição |
|---|---|
| Principal | Preço do produto |
| Tax | Imposto sobre produto |
| ShippingCharge | Frete cobrado do comprador |
| ShippingTax | Imposto sobre frete |
| GiftWrap | Embrulho para presente |
| GiftWrapTax | Imposto sobre embrulho |

## Tipos de Fee (ItemFeeList)

| FeeType | Descrição | Sinal |
|---|---|---|
| Commission | Comissão da Amazon (%) | Negativo |
| FBAPerUnitFulfillmentFee | Taxa FBA por unidade | Negativo |
| FBAPerOrderFulfillmentFee | Taxa FBA por pedido | Negativo |
| FBAWeightBasedFee | Taxa FBA por peso | Negativo |
| VariableClosingFee | Taxa de fechamento variável | Negativo |
| FixedClosingFee | Taxa de fechamento fixa | Negativo |
| ShippingChargeback | Estorno de frete | Negativo |

## Cálculos

```
valor_bruto = soma(ItemChargeList) → Principal + Tax + ShippingCharge + ShippingTax
taxas = soma(ItemFeeList) → Commission + FBA fees (todos negativos)
cupom = soma(PromotionList) → promoções (negativos)
valor_liquido = valor_bruto + taxas + cupom
```

## Refunds

Refunds usam campos com sufixo `Adjustment`:
- `ShipmentItemAdjustmentList` em vez de `ShipmentItemList`
- `ItemChargeAdjustmentList` em vez de `ItemChargeList`
- `ItemFeeAdjustmentList` em vez de `ItemFeeList`
- `PromotionAdjustmentList` em vez de `PromotionList`

Os valores de charges em refunds são **negativos** (dinheiro devolvido).
Os valores de fees em refunds são **positivos** (fees revertidas).
