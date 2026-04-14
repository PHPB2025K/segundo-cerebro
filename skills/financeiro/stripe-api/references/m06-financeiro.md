---
title: "m06 financeiro"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 6 — Relatórios Financeiros

## Balance API

```bash
curl https://api.stripe.com/v1/balance -u "$STRIPE_SECRET_KEY:"
```
Retorna: `available[]` (disponível), `pending[]` (não liberados). Cada: `amount`, `currency`, `source_types`.

## Balance Transactions — reconciliação

Cada movimentação: `amount` (bruto), `fee` (taxa), `net` (líquido), `type`, `source`, `status` (available|pending).

```bash
# Listar
curl -G https://api.stripe.com/v1/balance_transactions \
  -u "$STRIPE_SECRET_KEY:" -d limit=25 -d type=charge

# Por payout (reconciliação)
curl -G https://api.stripe.com/v1/balance_transactions \
  -u "$STRIPE_SECRET_KEY:" -d payout=po_xxx

# Por data
curl -G https://api.stripe.com/v1/balance_transactions \
  -u "$STRIPE_SECRET_KEY:" \
  -d "created[gte]=1700000000" -d "created[lt]=1700604800"
```

Tipos: `charge`, `refund`, `payout`, `payment`, `payment_refund`, `transfer`, `adjustment`, `stripe_fee`

## Payouts API — saques

```bash
# Criar payout manual (⚠️ CONFIRMAR ANTES)
curl https://api.stripe.com/v1/payouts \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d amount=50000 -d currency=brl \
  -d description="Saque semanal" -d method=standard

# Listar
curl -G https://api.stripe.com/v1/payouts \
  -u "$STRIPE_SECRET_KEY:" -d status=paid -d limit=10

# Cancelar pendente
curl -X POST https://api.stripe.com/v1/payouts/po_xxx/cancel \
  -u "$STRIPE_SECRET_KEY:"
```

Statuses: `pending → in_transit → paid | failed | canceled`

## Refunds API

```bash
# Total
curl https://api.stripe.com/v1/refunds \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d payment_intent=pi_xxx

# Parcial
curl https://api.stripe.com/v1/refunds \
  -u "$STRIPE_SECRET_KEY:" \
  -d payment_intent=pi_xxx -d amount=1500 \
  -d reason=requested_by_customer

# Listar
curl -G https://api.stripe.com/v1/refunds \
  -u "$STRIPE_SECRET_KEY:" -d payment_intent=pi_xxx
```

⚠️ `reason=fraudulent` adiciona cartão e email a blocklists. Usar APENAS quando confirmado.
Reasons: `duplicate`, `fraudulent`, `requested_by_customer`

## Disputes API

```bash
# Listar
curl -G https://api.stripe.com/v1/disputes \
  -u "$STRIPE_SECRET_KEY:" -d limit=10

# Submeter evidências
curl https://api.stripe.com/v1/disputes/dp_xxx \
  -u "$STRIPE_SECRET_KEY:" \
  -d "evidence[customer_name]=João Silva" \
  -d "evidence[customer_email_address]=joao@exemplo.com" \
  -d "evidence[product_description]=Descrição" \
  -d "evidence[shipping_tracking_number]=BR123456789"

# Aceitar (⚠️ IRREVERSÍVEL — CONFIRMAR ANTES)
curl -X POST https://api.stripe.com/v1/disputes/dp_xxx/close \
  -u "$STRIPE_SECRET_KEY:"
```

Statuses: `needs_response → under_review → won | lost`
