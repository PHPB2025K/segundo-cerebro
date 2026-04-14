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
**Deploy:** Vercel (budamix-ecommerce.vercel.app)
**Domínio:** https://budamix.com.br (DNS pendente → A record 76.76.21.21)
**Supabase:** projeto `ioujfkrqvporfbvdqyus` (org GB Importadora, sa-east-1)
**Vercel Project:** prj_wMl99f4aixldKCwBiJv9xDedL7AR

## O que é

E-commerce próprio da Budamix. Catálogo de produtos (vidro, MDF, porcelana), carrinho com guest checkout, painel admin, rastreamento de pedidos. Checkout integrado com Mercado Pago (Payment Brick).

## Stack detalhada

- **Frontend:** React 18.3.1, Vite 5.4.19, @mercadopago/sdk-react, react-router-dom 6
- **Backend:** Supabase (PostgreSQL 17 + RLS + Edge Functions + Auth)
- **Pagamento:** Mercado Pago Checkout Bricks (Pix + Cartão até 12x)
- **Hospedagem:** Vercel (deploy via CLI: `vercel --prod`)
- **DNS:** Registro.br (pendente migração para Vercel)

## Schema Supabase (13 tabelas)

products, product_variants, product_images, product_videos, collections, carts, cart_items, orders, order_items, addresses, profiles, user_roles, site_settings

## Edge Functions (deployed)

- `create-mp-payment` — Cria order + chama MP /v1/payments
- `mp-webhook` — IPN Mercado Pago (HMAC-SHA256 via Web Crypto API)
- `get-order-by-token` — Busca pedido por ID + email

## Admin

- **Login:** pehpbroglio@gmail.com / Admin@Budamix2026
- **URL:** /admin/login
- **User ID:** d6bfbcbe-0765-4ec5-8f5c-23d0e03c42ec

## Dados migrados

- 3 collections, 23 products, 113 images, 23 variants, 16 videos
- Storage: 101 imagens + 16 vídeos migrados (URLs atualizadas)
- 3 produtos placeholder (inativos no Supabase antigo, sem service role key)

## Decisões-chave

- [2026-04-14] Migração Stripe → Mercado Pago (9 commits). Stripe nunca foi funcional.
- [2026-04-14] Payment Brick (não Checkout Pro) — controle total da UX.
- [2026-04-14] Migração Lovable → Vercel + Supabase próprio (org GB Importadora).
- [2026-04-14] Credenciais MP e Supabase no 1Password vault OpenClaw.

## Pendências

- [ ] Configurar DNS: A record budamix.com.br → 76.76.21.21 (Registro.br)
- [ ] Configurar DNS: A record www.budamix.com.br → 76.76.21.21
- [ ] Testar pagamento sandbox (Pix + Cartão) — produtos agora têm estoque
- [ ] Trocar credenciais MP para produção
- [ ] Configurar webhook URL no painel MP Developers
- [ ] 3 produtos placeholder precisam de dados reais (nomes, descrições, imagens)

## 1Password (vault OpenClaw)

- Supabase - Budamix Ecommerce - Anon Key
- Supabase - Budamix Ecommerce - Service Role
- Supabase - Budamix Ecommerce - DB Password
- Mercado Pago - Budamix Ecommerce - Access Token
- Mercado Pago - Budamix Ecommerce - Public Key
- Mercado Pago - Budamix Ecommerce - Test Access Token
- Mercado Pago - Budamix Ecommerce - Test Public Key

## Como deployar

```bash
cd ~/Documents/05-Projetos-Codigo/budamix-ecommerce
vercel --prod
```

## Como acessar Supabase

```bash
SUPABASE_ACCESS_TOKEN="$(op item get 'Supabase Access Token - CLI' --vault OpenClaw --fields credential --reveal)" \
  supabase link --project-ref ioujfkrqvporfbvdqyus
```

## Notas relacionadas

- [[memory/context/decisoes/2026-04|Decisões Abril 2026]]
