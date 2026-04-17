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

### Rotas referenciadas mas inexistentes
- ✅ `/loja` (Shop.tsx — grid 2/3/4 cols de produtos ativos)
- ✅ `/sobre` (About.tsx — institucional com CTA → /loja)
- ✅ `/blog` (Blog.tsx — placeholder "em breve" com CTA → /loja)
- ❌ `/faq`, `/contato`, `/trocas-e-devolucoes`, `/termos` — ainda 404

### Componentes antigos ainda não migrados
- [ ] `src/pages/ProductDetail.tsx` — usa quantity inline, migrar para `<QuantitySelector variant="default" />`
- [ ] `src/pages/Cart.tsx` — usa quantity inline, migrar para `<QuantitySelector variant="cart" />`

### Infra 15/04 mantida
- **Referências visuais:** Granado + Great Jones
- **Multi-agent pipeline:** `.claude/agents/` com 5 agentes reutilizáveis

## Decisões-chave

- [2026-04-17] **Checkout + MP hardening #MP01-04** em prod: validação de estoque (400 com details), decremento idempotente via RPC `decrement_stock`, validação server-side de frete (lê `site_settings.free_shipping_threshold`), HMAC do webhook mandatório. Edge Functions `create-mp-payment` v5 + `mp-webhook` v6 (com `--no-verify-jwt` — MP não envia JWT). Secrets do MP confirmados.
- [2026-04-17] **SKU remapping em prod** — 19 variants renomeadas (ex: `CONJUNTO_DE_5_POTES_` → `IMB501V_T`, `POTE_HERMETICO_QUADR` → `YW320SQ`). Tulipa splitada em 6 cores (TL250V/P/Z/R/A/B). 3 produtos "Migrado" deletados. Estado final: 25 variants / 25 SKUs únicos / 0 truncados. Doc: `docs/sku-remapping-2026-04-17.md`.
- [2026-04-17] **Stock sync em prod** — 19 UPDATEs aplicando `product_variants.stock` a partir da coluna Quantidade da planilha ESTOQUE. Estado: 8 unidades totais (6 Tulipa=1, CK4742_B=1, YW1520RC=2, resto 0).
- [2026-04-17] **Apps Script real-time Sheets → Supabase** — `onEdit` trigger em `scripts/google-apps-script-stock-sync.js`. Pedro instala manualmente. → [[knowledge/concepts/apps-script-onedit-supabase-sync]]
- [2026-04-17] **Confetes canvas-confetti** ao atingir frete grátis no drawer/cart/checkout. Paleta Budamix, 3 explosões em cascata, origem calculada do `getBoundingClientRect()` de elemento-alvo. Guard `prefers-reduced-motion`.
- [2026-04-17] **Frete grátis server-side automático** — quando `subtotal >= 19900`, `create-mp-payment` força `shipping_cents=0`; Checkout + Cart mostram banner + "Grátis" Teal; `canPay` libera checkout sem CEP.
- [2026-04-17] `verify_jwt=false` obrigatório para Edge Functions chamadas por webhook externo (MP não envia JWT). Proteção vira responsabilidade do HMAC no código. → [[knowledge/concepts/supabase-edge-function-verify-jwt-webhooks]]
- [2026-04-17] Fix PDP branco — Rules of Hooks violation (useEffect após early return). Móvidos os 3 effects pra antes dos returns, guards no callback. → [[knowledge/concepts/react-hooks-order-early-return]]
- [2026-04-17] Criadas páginas `/loja`, `/sobre`, `/blog` (placeholder) com React.lazy. Faltam `/faq`, `/contato`, `/trocas-e-devolucoes`, `/termos`.
- [2026-04-17] MarqueeStrip texto focado em conversão: FRETE GRÁTIS ★ 6X SEM JUROS ★ RASTREIE SEU PEDIDO ★ COMPRA SEGURA ★ ENVIO EM 24H ★ (substituiu branding genérico).
- [2026-04-17] Favicon casinha Budamix — PNG oficial multi-size via sips + npx png-to-ico (16/32/48/64 .ico + 32/64 PNG + 180px apple-touch).
- [2026-04-17] CategoryBar usa 3 coleções reais (Vidro, MDF, Porcelana) em vez de categorias fictícias.
- [2026-04-16] PDP + Cart + Checkout reescritos, code-splitting aplicado, sitemap dinâmico, site_settings populado. Detalhes na sessão 5 do dia.
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
- [x] ~~Code-splitting: chunk JS 895KB~~ → ✅ 16/04 React.lazy em 12 rotas, 255KB→195KB gzip, commit `ebfebc1`
- [ ] Push dos commits locais para `origin/main` — **~75 commits acumulados** (16/04 + 17/04 manhã + 17/04 noite), aguardando validação visual e confirmação do Pedro para disparar Vercel deploy
- [ ] Instalar Apps Script na planilha ESTOQUE — Pedro manual, setup em `docs/SETUP-STOCK-SYNC.md`
- [ ] Testes manuais de pagamento MP real (suite completa em `AUDITORIA-CHECKOUT-MP.md` §5)
- [ ] Migrar `ProductDetail.tsx` para usar `<QuantitySelector />` novo (Cart.tsx já usa)
- [x] ~~Criar rotas `/loja`, `/sobre`, `/blog`~~ → ✅ 17/04 (commit `13f99ca`)
- [ ] Criar rotas faltantes: `/faq`, `/contato`, `/trocas-e-devolucoes`, `/termos`
- [ ] Corrigir warning pré-existente `fetchPriority` vs `fetchpriority` no img do HeroBanner (cosmético)
- [ ] Gerar sitemap em build pipeline (hoje é manual via `npm run generate:sitemap`)

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
