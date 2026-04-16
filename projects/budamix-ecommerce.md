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
**Deploy:** Vercel (`vercel --prod`)
**Domínio:** https://budamix.com.br (DNS ativo, Vercel GRU)
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

## Design System

### Atualização 16/04 — spec + mockups Paper

- **Fontes:** Bricolage Grotesque 800 (headings), Plus Jakarta Sans 400/500/600 via `@fontsource-variable/plus-jakarta-sans` (body — trocou Satoshi), JetBrains Mono 700 (preços)
- **Paleta:** Teal #004D4D, Terracotta #C56A4A, Gold #C7A35A, Sage #7EADAD, Areia #F7F4EF, Grafite #132525, Porcelain #D9E6E6, Muted #EDE8E0, Border #C2D1D1, Card #FFFFFF
- **Mockup referência:** Paper Design file `01KP8R1XYH6D1PQV14R4RJ04BT` (10 artboards: Homepage/PDP/Carrinho/Checkout em Desktop + Mobile)
- **Fonte de verdade:** `src/design/DESIGN-TOKENS.md` (v1.1) + `src/index.css` tokens HSL

### Componentes reescritos (16/04) — 8 commits

| Componente | Arquivo | Nota |
|---|---|---|
| AnnouncementBar | `src/components/layout/AnnouncementBar.tsx` | Terracotta h-8/h-9, texto responsivo, dismiss via useState |
| Header (desktop) | `src/components/layout/Header.tsx` | Teal 64px, logo PNG branco, NavLinks LOJA/COLEÇÕES/SOBRE/BLOG, busca+conta+SACOLA(N) |
| HeaderMobile | `src/components/layout/HeaderMobile.tsx` (novo) | Teal 56px, hamburger+logo+SACOLA |
| MobileMenu | `src/components/layout/MobileMenu.tsx` (novo) | Sheet slide L→R, Radix Dialog (Escape, backdrop, scroll lock) |
| Footer (desktop) | `src/components/layout/Footer.tsx` | Grafite bg, 4 colunas, marketplaces row, bottom bar |
| FooterMobile | `src/components/layout/FooterMobile.tsx` (novo) | Logo+tagline+social center, 3 accordions Radix |
| ProductCard | `src/components/products/ProductCard.tsx` | Radius 12, img 1:1 bg muted, title uppercase, mono prices, hover scale |
| ProductBadge | `src/components/products/ProductBadge.tsx` (novo) | 4 variantes: discount/bestseller/new/sold_out |
| NavArrow | `src/components/shared/NavArrow.tsx` (novo) | Circle teal, chevron branca, desktop-only |
| QuantitySelector | `src/components/shared/QuantitySelector.tsx` (novo) | 2 variantes: default pill (PDP) + cart circular teal |
| Layout | `src/components/layout/Layout.tsx` | Compõe AnnouncementBar + HeaderMobile + Header + FooterMobile + Footer |

### Rotas referenciadas mas inexistentes (404 até criar)
- `/loja`, `/sobre`, `/blog`, `/faq`, `/contato`, `/trocas-e-devolucoes`, `/termos`

### Componentes antigos ainda não migrados
- [ ] `src/pages/ProductDetail.tsx` — usa quantity inline, migrar para `<QuantitySelector variant="default" />`
- [ ] `src/pages/Cart.tsx` — usa quantity inline, migrar para `<QuantitySelector variant="cart" />`

### Infra 15/04 mantida
- **Referências visuais:** Granado + Great Jones
- **Multi-agent pipeline:** `.claude/agents/` com 5 agentes reutilizáveis

## Decisões-chave

- [2026-04-16] Design system alinhado com spec + mockups Paper Design. Plus Jakarta Sans trocou Satoshi (@fontsource local). Paper MCP como fonte visual. 8 componentes reescritos. → [[memory/context/decisoes/2026-04|decisões]]
- [2026-04-15] Redesign completo com identidade Budamix (Granado + Great Jones). 5 agentes multi-agent. → [[memory/context/decisoes/2026-04|decisões]]
- [2026-04-14] Migração Stripe → Mercado Pago (9 commits). Stripe nunca foi funcional.
- [2026-04-14] Payment Brick (não Checkout Pro) — controle total da UX.
- [2026-04-14] Migração Lovable → Vercel + Supabase próprio (org GB Importadora).
- [2026-04-14] Credenciais MP e Supabase no 1Password vault OpenClaw.

## Pendências

- [x] ~~Configurar DNS~~ → ✅ Ativo (76.76.21.21)
- [x] ~~Trocar credenciais MP para produção~~ → ✅ Ativo
- [ ] Configurar webhook URL no painel MP Developers — **Pedro manualmente**
- [ ] Testar pagamento Pix real (valor baixo) para validar QR code + webhook
- [ ] 3 produtos placeholder precisam de dados reais
- [ ] Testar redesign no mobile real (StickyAddToCart, fontes, AnnouncementBar)
- [ ] Code-splitting: chunk JS 895KB (considerar dynamic import)
- [ ] Push dos 8 commits locais de 16/04 para `origin/main` (aguardando validação visual)
- [ ] Migrar `ProductDetail.tsx` e `Cart.tsx` para usar `<QuantitySelector />` novo
- [ ] Criar rotas futuras: `/loja`, `/sobre`, `/blog`, `/faq`, `/contato`, `/trocas-e-devolucoes`, `/termos`

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
