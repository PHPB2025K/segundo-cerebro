---
title: "Budamix E-commerce"
created: 2026-04-14
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/budamix-ecommerce/"
tags:
  - project
  - dev
  - ecommerce
---

# Budamix E-commerce

**Path:** `~/Documents/05-Projetos-Codigo/budamix-ecommerce/`
**Repo:** https://github.com/PHPB2025K/budamix-ecommerce
**Branch:** main
**Stack:** React 18 + Vite 5 + TypeScript + Tailwind + shadcn/ui + Supabase
**Deploy:** Lovable (cloud build, não roda local)
**Domínio:** https://budamix.com.br
**Supabase:** projeto `jtczupudieeogzspdqae`

## O que é

E-commerce próprio da Budamix. Catálogo de produtos (vidro, MDF, porcelana), carrinho com guest checkout, painel admin, rastreamento de pedidos. Checkout integrado com Mercado Pago (Payment Brick).

## Stack detalhada

- **Frontend:** React 18.3.1, Vite 5.4.19, @mercadopago/sdk-react, react-router-dom 6
- **Backend:** Supabase (PostgreSQL + RLS + Edge Functions + Auth)
- **Pagamento:** Mercado Pago Checkout Bricks (Pix + Cartão até 12x)
- **Hospedagem:** Lovable (deploy automático via GitHub)
- **CDN:** Cloudflare

## Schema Supabase (13 tabelas)

products, product_variants, product_images, product_videos, collections, carts, cart_items, orders, order_items, addresses, profiles, user_roles, site_settings

## Edge Functions

- `create-mp-payment` — Cria order + chama MP /v1/payments
- `mp-webhook` — IPN Mercado Pago (HMAC-SHA256)
- `get-order-by-token` — Busca pedido por ID + email

## Decisões-chave

- [2026-04-14] Migração Stripe → Mercado Pago (9 commits). Stripe nunca foi funcional (sem credenciais). MP é o gateway definitivo.
- [2026-04-14] Payment Brick (não Checkout Pro) — controle total da UX, sem redirect externo.
- [2026-04-14] Credenciais MP no 1Password vault OpenClaw (4 itens: Access Token, Public Key, Test Access Token, Test Public Key).

## Pendências

- [ ] Rodar migration SQL no Supabase (rename stripe → mp columns)
- [ ] Deploy Edge Functions (create-mp-payment, mp-webhook)
- [ ] Configurar secret MP_ACCESS_TOKEN no Supabase
- [ ] Testar pagamento sandbox (Pix + Cartão)
- [ ] Trocar credenciais para produção
- [ ] Configurar webhook URL no painel MP Developers
- [ ] Produtos com estoque zerado — adicionar estoque para testes

## Notas relacionadas

- [[memory/context/decisoes/2026-04|Decisões Abril 2026]]
- [[skills/marketplace/ml-fees-rules/SKILL|ML Fees Rules]]
