---
title: "m09 erros"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 9 — Tratamento de Erros

## Códigos HTTP

| Código | Significado | Ação |
|---|---|---|
| 200 | Sucesso | — |
| 400 | Parâmetro inválido | Corrigir e retentar |
| 401 | Chave API inválida | Verificar STRIPE_SECRET_KEY |
| 402 | Falhou (ex: cartão recusado) | Informar usuário |
| 403 | Sem permissão | Verificar permissões da chave |
| 404 | Não encontrado | Verificar ID |
| 409 | Conflito idempotência | Nova Idempotency-Key |
| 429 | Rate limit | Backoff exponencial com jitter |
| 500/502/503 | Erro Stripe | Retentar com backoff |

## Tipos de erro (`error.type`)

- `card_error`: Cartão não pode ser cobrado — `message` seguro pra exibir ao usuário
- `invalid_request_error`: Parâmetros inválidos ou recurso inexistente
- `api_error`: Problema temporário no Stripe
- `idempotency_error`: Chave reutilizada com parâmetros diferentes

## Códigos frequentes

**Cartão:** `card_declined`, `expired_card`, `incorrect_cvc`, `insufficient_funds`, `authentication_required`
**Request:** `parameter_missing`, `resource_missing`, `resource_already_exists`
**PaymentIntent:** `payment_intent_unexpected_state`, `payment_intent_authentication_failure`

## Estratégia obrigatória

- **4xx:** Corrigir parâmetros + nova Idempotency-Key
- **429:** Backoff exponencial + verificar `Stripe-Should-Retry`
- **5xx:** Retentar com backoff + webhooks pra reconciliação posterior
- **Sempre:** Parsear `error.type`, `error.code`, `error.message` e apresentar de forma clara
