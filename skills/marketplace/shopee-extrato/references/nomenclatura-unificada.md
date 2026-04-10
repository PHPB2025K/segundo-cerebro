# Nomenclatura Unificada — Mercado Livre ↔ Shopee

Mapeamento de termos entre as APIs do Mercado Livre e Shopee para padronização dos extratos financeiros da GB Importadora.

| Termo Unificado | Mercado Livre | Shopee | Descrição |
|---|---|---|---|
| Valor Bruto | transaction_amount | cost_of_goods_sold | Valor total do produto antes de taxas |
| Valor Líquido | net_received_amount | escrow_amount | Valor efetivamente recebido pelo vendedor |
| Comissão Marketplace | marketplace_fee (charges_details) | commission_fee | Comissão cobrada pela plataforma |
| Taxa de Serviço | — | service_fee | Taxa adicional de serviço (Shopee) |
| Taxa de Transação | — | transaction_fee / credit_card_transaction_fee | Taxa sobre método de pagamento |
| Frete Comprador | shipping_fee | buyer_paid_shipping_fee | Valor de frete pago pelo comprador |
| Frete Real | — | actual_shipping_fee | Custo real do frete (Shopee subsidia diferença) |
| Frete Líquido | — | final_shipping_fee | Diferença entre frete pago e custo real |
| Voucher Vendedor | — | seller_voucher | Desconto concedido pelo vendedor |
| Voucher Plataforma | coupon_amount | shopee_voucher + coins | Desconto bancado pela plataforma |
| Taxa Campanha | — | campaign_fee | Taxa por participar de campanhas |
| Taxa FBS | — | fbs_fee | Taxa de fulfillment (FBS) |
| ID Pedido | order.id | order_sn | Identificador único do pedido |
| ID Pagamento | payment.id | (não existe separado) | ID do pagamento |
| Método Pagamento | payment_method_id | buyer_payment_method | Pix, Cartão, etc. |
| Status | status + status_detail | order_status | Status do pedido |

## Diferenças Estruturais

### Shopee tem que o ML não tem:
- **service_fee**: taxa separada da comissão
- **transaction_fee / credit_card_transaction_fee**: taxa específica do método de pagamento
- **campaign_fee**: taxa por participar de promoções/campanhas
- **fbs_fee**: taxa de fulfillment (quando usa armazém Shopee)
- **final_shipping_fee**: saldo de frete (subsidio da Shopee)
- **coins**: moedas Shopee usadas como desconto

### ML tem que Shopee não tem:
- **pack_id**: agrupamento de pedidos no mesmo carrinho
- **payment_id separado**: na Shopee, order_sn é a referência única
- **charges_details com breakdown**: no ML as taxas vêm em charges_details; na Shopee cada fee é um campo separado

## Fórmula de Equivalência

```
ML: valor_liquido = transaction_amount - marketplace_fee - outras_taxas
Shopee: escrow_amount = cost_of_goods_sold + all_fees + vouchers + shipping_adjustments
```

Na Shopee, escrow_amount já é o valor final considerando todas as deduções.
