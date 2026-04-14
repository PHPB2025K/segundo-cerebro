---
title: "m05 faturas"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 5 — Faturas

## Ciclo de vida
`draft → open → paid | void | uncollectible`

Assinaturas criam faturas automaticamente. Faturas manuais: draft → adicionar itens → finalizar → cobrar.

## Endpoints

| Operação | Método | Endpoint |
|---|---|---|
| Criar | POST | /v1/invoices |
| Recuperar | GET | /v1/invoices/:id |
| Atualizar | POST | /v1/invoices/:id |
| Finalizar | POST | /v1/invoices/:id/finalize |
| Enviar email | POST | /v1/invoices/:id/send |
| Pagar | POST | /v1/invoices/:id/pay |
| Anular | POST | /v1/invoices/:id/void |
| Listar | GET | /v1/invoices |
| Preview | GET | /v1/invoices/upcoming |

## Exemplos

```bash
# Criar fatura manual
curl https://api.stripe.com/v1/invoices \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d customer=cus_xxx -d auto_advance=false

# Adicionar item
curl https://api.stripe.com/v1/invoiceitems \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d customer=cus_xxx -d "pricing[price]=price_xxx" \
  -d invoice=in_xxx -d quantity=2

# Finalizar
curl -X POST https://api.stripe.com/v1/invoices/in_xxx/finalize \
  -u "$STRIPE_SECRET_KEY:"

# Enviar por email
curl -X POST https://api.stripe.com/v1/invoices/in_xxx/send \
  -u "$STRIPE_SECRET_KEY:"

# Pagar
curl -X POST https://api.stripe.com/v1/invoices/in_xxx/pay \
  -u "$STRIPE_SECRET_KEY:"

# Anular
curl -X POST https://api.stripe.com/v1/invoices/in_xxx/void \
  -u "$STRIPE_SECRET_KEY:"

# Listar do cliente
curl -G https://api.stripe.com/v1/invoices \
  -u "$STRIPE_SECRET_KEY:" -d customer=cus_xxx -d status=open

# Preview próxima fatura
curl -G https://api.stripe.com/v1/invoices/upcoming \
  -u "$STRIPE_SECRET_KEY:" -d customer=cus_xxx
```
