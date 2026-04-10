# Módulo 3 — Produtos e Preços

## Products API

Obrigatório: `name`

```bash
# Criar
curl https://api.stripe.com/v1/products \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d name="Plano Premium" -d description="Assinatura mensal" \
  -d "metadata[tier]=premium"

# Listar ativos
curl -G https://api.stripe.com/v1/products \
  -u "$STRIPE_SECRET_KEY:" -d active=true -d limit=25

# Atualizar
curl https://api.stripe.com/v1/products/prod_xxx \
  -u "$STRIPE_SECRET_KEY:" -d name="Plano Platina"

# Deletar (apenas sem preços associados)
curl -X DELETE https://api.stripe.com/v1/products/prod_xxx \
  -u "$STRIPE_SECRET_KEY:"
```

## Prices API

⚠️ Após criação, `unit_amount`, `currency`, `product` e `recurring` NÃO podem ser alterados — criar novo price.

Intervalos: `day`, `week`, `month`, `year`. `interval_count` = multiplicador. Máximo ~3 anos.

```bash
# Recorrente mensal
curl https://api.stripe.com/v1/prices \
  -u "$STRIPE_SECRET_KEY:" -H "Idempotency-Key: $(uuidgen)" \
  -d currency=brl -d unit_amount=4990 \
  -d "recurring[interval]=month" -d product=prod_xxx

# One-time
curl https://api.stripe.com/v1/prices \
  -u "$STRIPE_SECRET_KEY:" \
  -d currency=brl -d unit_amount=9900 -d product=prod_xxx

# Anual
curl https://api.stripe.com/v1/prices \
  -u "$STRIPE_SECRET_KEY:" \
  -d currency=brl -d unit_amount=49900 \
  -d "recurring[interval]=year" -d product=prod_xxx

# Com produto inline
curl https://api.stripe.com/v1/prices \
  -u "$STRIPE_SECRET_KEY:" \
  -d currency=brl -d unit_amount=2990 \
  -d "recurring[interval]=month" \
  -d "product_data[name]=Plano Básico"

# Listar preços de um produto
curl -G https://api.stripe.com/v1/prices \
  -u "$STRIPE_SECRET_KEY:" -d product=prod_xxx -d active=true
```
