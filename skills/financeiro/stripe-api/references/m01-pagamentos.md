---
title: "m01 pagamentos"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 1 — Cobranças e Pagamentos

## PaymentIntents API

Usar SEMPRE PaymentIntents — nunca Charges API legada.

### Máquina de estados
`requires_payment_method → requires_confirmation → requires_action → processing → requires_capture → succeeded`

### Endpoints

| Operação | Método | Endpoint |
|---|---|---|
| Criar | POST | /v1/payment_intents |
| Recuperar | GET | /v1/payment_intents/:id |
| Atualizar | POST | /v1/payment_intents/:id |
| Confirmar | POST | /v1/payment_intents/:id/confirm |
| Capturar | POST | /v1/payment_intents/:id/capture |
| Cancelar | POST | /v1/payment_intents/:id/cancel |
| Listar | GET | /v1/payment_intents |
| Buscar | GET | /v1/payment_intents/search |

### Parâmetros de criação
- **Obrigatórios:** `amount` (centavos), `currency`
- **Importantes:** `customer`, `payment_method`, `payment_method_types[]`, `automatic_payment_methods[enabled]=true`, `confirm`, `capture_method` (automatic_async|manual), `description`, `metadata`, `receipt_email`, `setup_future_usage` (on_session|off_session), `statement_descriptor`, `statement_descriptor_suffix`

### Exemplos

```bash
# Pagamento simples cartão
curl -X POST https://api.stripe.com/v1/payment_intents \
  -u "$STRIPE_SECRET_KEY:" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d amount=5000 -d currency=brl \
  -d "payment_method_types[]=card" \
  -d description="Pedido #1234" \
  -d "metadata[order_id]=1234"

# Pix
curl -X POST https://api.stripe.com/v1/payment_intents \
  -u "$STRIPE_SECRET_KEY:" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d amount=2000 -d currency=brl \
  -d "payment_method_types[]=pix" \
  -d "payment_method_options[pix][expires_after_seconds]=86400"

# Boleto (requer CPF/CNPJ)
curl -X POST https://api.stripe.com/v1/payment_intents \
  -u "$STRIPE_SECRET_KEY:" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d amount=2000 -d currency=brl \
  -d "payment_method_types[]=boleto" \
  -d "payment_method_options[boleto][expires_after_days]=7" \
  -d "payment_method_data[type]=boleto" \
  -d "payment_method_data[boleto][tax_id]=00000000000" \
  -d "payment_method_data[billing_details][name]=Nome Cliente" \
  -d "payment_method_data[billing_details][email]=email@exemplo.com" \
  -d "payment_method_data[billing_details][address][country]=BR" \
  -d confirm=true

# Captura manual (hold)
curl -X POST https://api.stripe.com/v1/payment_intents \
  -u "$STRIPE_SECRET_KEY:" \
  -d amount=10000 -d currency=brl \
  -d capture_method=manual \
  -d "payment_method_types[]=card"

# Capturar (parcial ou total) — sem captura em 7 dias = cancelamento
curl -X POST https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
  -u "$STRIPE_SECRET_KEY:" \
  -d amount_to_capture=7500

# Cancelar
curl -X POST https://api.stripe.com/v1/payment_intents/pi_xxx/cancel \
  -u "$STRIPE_SECRET_KEY:" \
  -d cancellation_reason=requested_by_customer

# Listar com filtros
curl -G https://api.stripe.com/v1/payment_intents \
  -u "$STRIPE_SECRET_KEY:" \
  -d customer=cus_xxx -d limit=25 \
  -d "created[gte]=1700000000"
```

## Payment Methods API

| Operação | Método | Endpoint |
|---|---|---|
| Criar | POST | /v1/payment_methods |
| Recuperar | GET | /v1/payment_methods/:id |
| Listar do cliente | GET | /v1/customers/:id/payment_methods |
| Anexar ao cliente | POST | /v1/payment_methods/:id/attach |
| Desanexar | POST | /v1/payment_methods/:id/detach |

```bash
# Anexar
curl -X POST https://api.stripe.com/v1/payment_methods/pm_xxx/attach \
  -u "$STRIPE_SECRET_KEY:" -d customer=cus_xxx

# Listar
curl -G https://api.stripe.com/v1/customers/cus_xxx/payment_methods \
  -u "$STRIPE_SECRET_KEY:" -d type=card

# Desanexar
curl -X POST https://api.stripe.com/v1/payment_methods/pm_xxx/detach \
  -u "$STRIPE_SECRET_KEY:"
```
