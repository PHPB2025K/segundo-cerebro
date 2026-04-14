---
title: "m08 paginacao"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 8 — Paginação e Expand

## Paginação (cursor-based)

- `limit`: 1-100 (default 10)
- `starting_after`: ID do último objeto da página anterior
- `ending_before`: inverso
- `has_more`: true/false na resposta
- Ordem: cronológica reversa

```bash
# Primeira página
curl -G https://api.stripe.com/v1/customers \
  -u "$STRIPE_SECRET_KEY:" -d limit=100

# Próxima
curl -G https://api.stripe.com/v1/customers \
  -u "$STRIPE_SECRET_KEY:" -d limit=100 \
  -d starting_after=cus_ultimoID
```

Para buscar TODOS: iterar `starting_after` até `has_more=false`.

## Expandable objects

Muitos campos retornam só IDs. Expandir com `expand[]` (até 4 níveis):

```bash
curl https://api.stripe.com/v1/payment_intents/pi_xxx \
  -u "$STRIPE_SECRET_KEY:" \
  -d "expand[]=customer" \
  -d "expand[]=latest_charge.balance_transaction"
```

Em listas: prefixar com `data.`:
```bash
-d "expand[]=data.customer"
```
