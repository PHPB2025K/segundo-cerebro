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

- [2026-04-23 noite] **Push dos 111 commits represados + SoonBadge + 4 rotas stub** — sessão longa em 3 blocos. Bloco 1: 5 fases (backup branch, 6 commits lógicos do WIP, `git merge -s ours origin/main` dos 2 "behind" redundantes, push direto `135570e..9ab138a` em 4s, descoberta de que webhook GitHub→Vercel NÃO EXISTE → deploy `vercel --prod --yes` manual `dpl_3Gaz38ULNsddwhawDsZCQvEKypov` em 32s). Bloco 2: remover slide 2 "potes-vidro" do HeroBanner (`a2c525b`, asset preservado). Bloco 3: SoonBadge + ComingSoon + 4 rotas stub `/faq` `/contato` `/trocas-e-devolucoes` `/termos` (`5a1837b`, deploy `dpl_HH6A5NtEbcWLwkke4KDNs2NwT6V3`). Estratégia `merge -s ours` validada para cenário "remoto é snapshot antigo preservado por cherry-pick". HEAD válido é suficiente para Vercel Hobby — `111/118` commits com author `.local` passaram. Bundle 708.21 kB (gzip 206.70). 3 deploys bem-sucedidos mesmo dia. Backup `backup-pre-push-20260423-200452` preservada. → [[memory/context/decisoes/2026-04|decisões]]
- [2026-04-20 noite] **HeroBanner virou carousel real com 2 slides** — refactor em `src/components/home/HeroBanner.tsx`: array `SLIDES`, dots com ARIA e foco por teclado, auto-advance 7s (pausa em mouseenter, respeita `prefers-reduced-motion`). Slide 2: fundo Graphite `#132525`, imagem 3:2 (`w-[560px] h-[374px]`), título "Conservação que dura mais", CTA mantida. Imagem `/images/hero-potes-vidro.png` (1536×1024) veio do ChatGPT do Pedro com fundo graphite já embutido — Nano Banana descartado porque Gemini não gera PNG com alpha real (→ [[knowledge/concepts/nano-banana-no-alpha-channel]]). WIP em `main` local (não committed).
- [2026-04-20 noite] **Admin ganhou drag-and-drop de imagens** — `@dnd-kit/core` + `@dnd-kit/sortable` + `@dnd-kit/utilities`. Novo `SortableImageItem` envolve thumb em `DndContext` + `SortableContext`. `handleImagesDragEnd` usa `arrayMove` + reatribuição de `sort_order`. Persistência já existia (`uploadProductMedia` fazia UPDATE). Acessível via pointer/touch/keyboard. Função legacy `moveImage` (setinhas) removida.
- [2026-04-20 noite] **Admin — botão "Ver na loja"** na listagem: ícone `ExternalLink` abre `/produto/{slug}` em nova aba. + **fix ordering `product_images` no embed** da listagem (`.order('sort_order', { foreignTable: 'product_images' })`) — mesmo bug de 19/04 (`4ad4937`), agora resolvido também no admin.
- [2026-04-20 tarde] **Migration `differentials_image_url` aplicada direto em prod** via Supabase Management API (`POST /v1/projects/{ref}/database/query` com `ALTER TABLE ADD COLUMN IF NOT EXISTS`). Admin voltou a salvar imagem de diferenciais. Migration local untracked `supabase/migrations/20260418_product_differentials_image.sql` fica redundante (idempotente, será no-op quando pushada).
- [2026-04-20 tarde] **Reescrita editorial das 3 descrições MDF** — 2 rodadas de UPDATE: primeira seguiu padrão `CARACTERÍSTICAS\n----------\n`; depois descobri que a PDP renderiza texto puro (não markdown) e o bloco aparecia literal — 2ª rodada de UPDATE removeu `CARACTERÍSTICAS`/traços. Padrão Budamix final: título + pitch + bullets `•` direto. PCM 778 chars, DPM001 607, DPM002 677. Verbos: "Proteja" (PCM), "Organize" (DPMs). `Material: MDF` puro sem adjetivos.
- [2026-04-20 manhã] **Hotfix PDP branco em prod deployed** — React error #310 (Rules of Hooks — 3 `useEffect` após early returns). Cherry-pick do commit `62aa9e1` (17/04) sobre branch saindo de `origin/main`, PR #1 mergeado, rebaseado para `1dd78cb`. Vercel Hobby bloqueou por author `*.local`: resolvido com `git config --global user.email "pehpbroglio@gmail.com"` + empty commit `135570e` + `vercel --prod --yes`. Prod live 14:04 UTC. 3/3 PDPs renderizando 0 errors. → [[knowledge/concepts/vercel-hobby-commit-author-block]]
- [2026-04-20 manhã] **Cadastrados 3 produtos MDF via API ML** — porta-copos (PCM001, R$19,90, 9 fotos), descanso redondo (DPM001, R$39,88, 8 fotos), descanso quadrado (DPM002, R$39,88, 7 fotos). Collection `Linha MDF`. IDs: `a826b449-3dc9-42e1-b34a-9acfc2d61783`, `bdb644fc-cae6-4c15-a156-4092121350f4`, `cd9b8493-e99c-484a-827d-743741b12f8f`. Dados 100% puxados do ML (titles/price/pics -O/descrição/SKU do SELLER_SKU). Stock=0 (cron VPS popula via SKU). `materials=null` alinhado com padrão dos 20 produtos existentes. Doc: `docs/products-2026-04-20-mdf-batch.md`. Commit `10861d6` em main local.
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
- [x] ~~Push dos commits locais para `origin/main`~~ → ✅ **23/04 noite** — 113 commits totais em prod na sessão (111 do push inicial `9ab138a` + 2 ajustes `a2c525b` e `5a1837b`). Estratégia `merge -s ours` para os 2 "behind" redundantes; deploy manual obrigatório (webhook GitHub→Vercel inexiste)
- [ ] Instalar Apps Script na planilha ESTOQUE — Pedro manual, setup em `docs/SETUP-STOCK-SYNC.md`
- [ ] Testes manuais de pagamento MP real (suite completa em `AUDITORIA-CHECKOUT-MP.md` §5)
- [ ] Migrar `ProductDetail.tsx` para usar `<QuantitySelector />` novo (Cart.tsx já usa)
- [x] ~~Criar rotas `/loja`, `/sobre`, `/blog`~~ → ✅ 17/04 (commit `13f99ca`)
- [x] ~~Criar rotas faltantes: `/faq`, `/contato`, `/trocas-e-devolucoes`, `/termos`~~ → ✅ **23/04 noite** — stubs `<ComingSoon>` com `noindex,nofollow` (`5a1837b`). Conteúdo real segue pendente (🟡 bloqueia Meta Ads)
- [ ] **Escrever conteúdo real das 4 páginas stub** e migrar cada uma para página dedicada (remover `setNoIndex()`)
- [ ] Integração GitHub→Vercel — hoje deploy é `vercel --prod --yes` manual. Conectar via Vercel Dashboard → Settings → Git (~15 min OAuth)
- [ ] Newsletter form não persiste email — hoje é `console.log` + toast fake em `NewsletterSection.tsx`. Hook para supabase/Resend/ConvertKit pendente
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

**Nota Kobe/VPS (28/04/2026):** por enquanto Pedro faz o deploy pelo Mac até Kobe rodar 1–2 ciclos sem incidente. Quando Kobe precisar deployar pela VPS, ler o token da Vercel do item 1Password `Vercel Token - Budamix Ecommerce` em `notesPlain`; o campo `password` fica vazio. Nunca hardcodar token.

```bash
cd ~/Documents/05-Projetos-Codigo/budamix-ecommerce
VERCEL_TOKEN=$(op item get "Vercel Token - Budamix Ecommerce" --vault OpenClaw --field notesPlain --reveal | grep -oE 'vercel_[A-Za-z0-9]+' | head -1)
[ -z "$VERCEL_TOKEN" ] && VERCEL_TOKEN=$(op item get "Vercel Token - Budamix Ecommerce" --vault OpenClaw --field notesPlain --reveal | grep -oE '[A-Za-z0-9]{24,}' | head -1)
vercel --prod --yes --token "$VERCEL_TOKEN"
```

## Como acessar Supabase

```bash
SUPABASE_ACCESS_TOKEN="$(op item get 'Supabase Access Token - CLI' --vault OpenClaw --fields credential --reveal)" \
  supabase link --project-ref ioujfkrqvporfbvdqyus
```

## Notas relacionadas

- [[memory/context/decisoes/2026-04|Decisões Abril 2026]]
