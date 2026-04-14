---
title: "m02 clientes"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
---

# Módulo 2 — Gestão de Clientes

IDs: `cus_`. Stripe não impõe unicidade de email.

## Endpoints

| Operação | Método | Endpoint |
|---|---|---|
| Criar | POST | /v1/customers |
| Recuperar | GET | /v1/customers/:id |
| Atualizar | POST | /v1/customers/:id |
| Deletar | DELETE | /v1/customers/:id |
| Listar | GET | /v1/customers |
| Buscar | GET | /v1/customers/search |

⚠️ **DELETE cancela TODAS as assinaturas ativas. Sempre confirmar.**

## Campos
`name` (max 256), `email` (max 512), `phone` (max 20), `description`, `address` (line1, city, state, postal_code, country), `metadata` (até 50 chaves, chave max 40, valor max 500), `balance` (centavos, negativo = crédito), `invoice_settings.default_payment_method`, `tax_exempt`

## Exemplos

```bash
# Criar completo
curl https://api.stripe.com/v1/customers \
  -u "$STRIPE_SECRET_KEY:" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d name="João Silva" \
  --data-urlencode email="joao@exemplo.com" \
  -d phone="+5511999998888" \
  -d description="Cliente B2B" \
  -d "address[line1]=Av Paulista 1000" \
  -d "address[city]=São Paulo" -d "address[state]=SP" \
  -d "address[postal_code]=01311000" -d "address[country]=BR" \
  -d "metadata[plano]=premium" -d "metadata[origem]=website"

# Buscar por email
curl -G https://api.stripe.com/v1/customers \
  -u "$STRIPE_SECRET_KEY:" --data-urlencode email="joao@exemplo.com"

# Search API (indexação ~1 min)
curl -G https://api.stripe.com/v1/customers/search \
  -u "$STRIPE_SECRET_KEY:" --data-urlencode query="email:'joao@exemplo.com'"

# Atualizar
curl https://api.stripe.com/v1/customers/cus_xxx \
  -u "$STRIPE_SECRET_KEY:" -d "metadata[plano]=enterprise"
```

## Metadata — operações especiais
```bash
-d "metadata[chave]=valor"   # Definir (preserva demais)
-d "metadata[chave]="        # Remover chave
-d "metadata="               # Limpar tudo
```

## Prioridade de payment method
`subscription.default_payment_method` > `customer.invoice_settings.default_payment_method` > `customer.default_source` (legado)
