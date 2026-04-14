---
title: "nomenclatura unificada"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
---

# Nomenclatura Unificada — Mercado Livre ↔ Shopee ↔ Amazon

Mapeamento de termos entre as APIs do Mercado Livre, Shopee e Amazon para padronização dos extratos financeiros da GB Importadora.

| Termo Unificado | Mercado Livre | Shopee | Amazon (SP-API) | Descrição |
|---|---|---|---|---|
| Valor Bruto | transaction_amount | cost_of_goods_sold | soma ItemChargeList | Valor total antes de taxas |
| Valor Líquido | net_received_amount | escrow_amount | charges + fees + promos | Valor efetivamente recebido |
| Comissão Marketplace | marketplace_fee | commission_fee | Commission (ItemFeeList) | Comissão da plataforma |
| Taxa de Serviço | — | service_fee | — | Taxa adicional (Shopee only) |
| Taxa de Transação | — | transaction_fee | — | Taxa de pagamento (Shopee only) |
| Taxa FBA por Unidade | — | — | FBAPerUnitFulfillmentFee | Taxa FBA unitária |
| Taxa FBA por Pedido | — | — | FBAPerOrderFulfillmentFee | Taxa FBA por pedido |
| Taxa FBA por Peso | — | — | FBAWeightBasedFee | Taxa FBA baseada em peso |
| Taxa FBA Armazenagem | — | — | FBAStorageFee (ServiceFee) | Armazenagem mensal FBA |
| Frete Comprador | shipping_fee | buyer_paid_shipping_fee | ShippingCharge (ItemChargeList) | Frete pago pelo comprador |
| Frete Real | — | actual_shipping_fee | ShippingChargeback (ItemFeeList) | Custo real do frete |
| Frete Líquido | — | final_shipping_fee | — | Diferença frete pago/custo |
| Voucher Vendedor | — | seller_voucher | PromotionList | Desconto do vendedor |
| Voucher Plataforma | coupon_amount | shopee_voucher + coins | PromotionList | Desconto da plataforma |
| Taxa Campanha | — | campaign_fee | — | Taxa de campanha (Shopee) |
| Taxa FBS | — | fbs_fee | — | Fulfillment Shopee |
| Taxa Fechamento | — | — | VariableClosingFee / FixedClosingFee | Taxa de fechamento Amazon |
| ID Pedido | order.id | order_sn | AmazonOrderId | Identificador do pedido |
| ID Pagamento | payment.id | — | — | ID do pagamento |
| ID Envio | shipment_id | tracking_number | ShipmentId | Identificador do envio |
| Método Pagamento | payment_method_id | buyer_payment_method | — (não exposto) | Pix, Cartão, etc |
| Status | status + status_detail | order_status | ProcessingStatus | Status do pedido |
| Modo Envio | me2 | shipping_carrier | FulfillmentChannel (FBA/MFN) | Canal de fulfillment |

## Diferenças Estruturais

### Amazon tem que ML e Shopee não têm:
- **FBA fees detalhadas**: por unidade, por pedido, por peso — breakdown granular
- **AdjustmentEventList**: ajustes automáticos (WAREHOUSE_DAMAGE, REVERSAL)
- **ServiceFeeEventList**: taxas avulsas não vinculadas a pedidos (Storage, Disposal)
- **GuaranteeClaimEventList**: disputas A-to-Z como evento financeiro separado
- **ShipmentId**: ID único por envio (não existe no ML/Shopee)

### ML tem que Amazon não tem:
- **pack_id**: agrupamento de pedidos no mesmo carrinho
- **payment_id separado**: pagamento como entidade independente
- **charges_details com breakdown**: taxas detalhadas em charges_details
- **Método de pagamento do comprador**: visa, mastercard, pix, etc.

### Shopee tem que Amazon não tem:
- **service_fee / transaction_fee**: taxas separadas por tipo
- **campaign_fee**: taxa por participar de campanhas
- **coins**: moedas Shopee como desconto
- **final_shipping_fee**: subsídio de frete Shopee

## Fórmula de Equivalência

```
ML:     valor_liquido = transaction_amount - marketplace_fee - outras_taxas
Shopee: escrow_amount = cost_of_goods_sold + all_fees + vouchers + shipping_adjustments
Amazon: valor_liquido = soma(ItemChargeList) + soma(ItemFeeList) + soma(PromotionList)
```

Na Amazon, fees são negativas e charges positivas. O valor líquido é a soma de tudo.
