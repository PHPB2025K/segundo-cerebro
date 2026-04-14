---
title: "m04 assinaturas"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 4 — Assinaturas Recorrentes

## Status do ciclo de vida

| Status | Descrição |
|---|---|
| `incomplete` | Pagamento inicial falhou; expira em 23h → `incomplete_expired` |
| `trialing` | Período de teste gratuito |
| `active` | Corrente e paga |
| `past_due` | Última fatura falhou; retentando |
| `canceled` | Cancelada. Terminal. |
| `unpaid` | Todas as tentativas esgotadas |
| `paused` | Trial terminou sem método de pagamento |

## Endpoints

| Operação | Método | Endpoint |
|---|---|---|
| Criar | POST | /v1/subscriptions |
| Recuperar | GET | /v1/subscriptions/:id |
| Atualizar | POST | /v1/subscriptions/:id |
| Cancelar | DELETE | /v1/subscriptions/:id |
| Listar | GET | /v1/subscriptions |
| Buscar | GET | /v1/subscriptions/search |

## Exemplos

```bash
# Criar assinatura
curl https://api.stripe.com/v1/subscriptions \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d customer=cus_xxx \
  -d "items[0][price]=price_xxx" \
  -d default_payment_method=pm_xxx

# Com trial
curl https://api.stripe.com/v1/subscriptions \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d customer=cus_xxx \
  -d "items[0][price]=price_xxx" \
  -d trial_period_days=14

# Cancelar no fim do período (graceful)
curl https://api.stripe.com/v1/subscriptions/sub_xxx \
  -u "$STRIPE_SECRET_KEY:" \
  -d cancel_at_period_end=true

# Cancelar imediatamente (⚠️ CONFIRMAR ANTES)
curl -X DELETE https://api.stripe.com/v1/subscriptions/sub_xxx \
  -u "$STRIPE_SECRET_KEY:"

# Listar ativas
curl -G https://api.stripe.com/v1/subscriptions \
  -u "$STRIPE_SECRET_KEY:" -d status=active -d limit=25

# Upgrade/downgrade (trocar price)
curl https://api.stripe.com/v1/subscriptions/sub_xxx \
  -u "$STRIPE_SECRET_KEY:" \
  -d "items[0][id]=si_xxx" \
  -d "items[0][price]=price_novo" \
  -d proration_behavior=create_prorations
```
