# Módulo 7 — Webhooks

## Criar endpoint

```bash
curl https://api.stripe.com/v1/webhook_endpoints \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  --data-urlencode url="https://seusite.com/stripe/webhook" \
  -d "enabled_events[]=payment_intent.succeeded" \
  -d "enabled_events[]=payment_intent.payment_failed" \
  -d "enabled_events[]=customer.subscription.created" \
  -d "enabled_events[]=customer.subscription.updated" \
  -d "enabled_events[]=customer.subscription.deleted" \
  -d "enabled_events[]=invoice.paid" \
  -d "enabled_events[]=invoice.payment_failed" \
  -d "enabled_events[]=charge.dispute.created" \
  -d "enabled_events[]=charge.refunded"
```

⚠️ O `secret` (`whsec_*`) é retornado APENAS na criação — armazenar imediatamente.
Limite: máximo 16 endpoints. `enabled_events[]=*` para todos.

## Eventos importantes

- **Pagamentos:** `payment_intent.succeeded`, `.payment_failed`, `.canceled`
- **Cobranças:** `charge.succeeded`, `.failed`, `.refunded`, `.dispute.created`, `.dispute.closed`
- **Clientes:** `customer.created`, `.updated`, `.deleted`
- **Assinaturas:** `customer.subscription.created`, `.updated`, `.deleted`, `.trial_will_end` (3 dias antes)
- **Faturas:** `invoice.created`, `.finalized`, `.paid`, `.payment_failed`, `.upcoming`
- **Payouts:** `payout.paid`, `.failed`

## Verificação de assinatura

HMAC-SHA256 com `whsec_*`. Header `Stripe-Signature`: `t=timestamp,v1=assinatura`

1. Extrair `t` e `v1`
2. `signed_payload = {timestamp}.{corpo_raw}`
3. `HMAC-SHA256(key=whsec_secret, message=signed_payload)`
4. Comparar com `v1` em tempo constante
5. Timestamp dentro de 5 minutos

**Usar corpo RAW, não JSON parseado.**
