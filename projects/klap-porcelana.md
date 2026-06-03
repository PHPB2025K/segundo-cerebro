---
title: "Klap Porcelana"
created: 2026-06-03
type: project
status: active
path: "/tmp/klap-migration/klap-ecommerce/"
tags:
  - project
  - dev
  - ecommerce
---

# Klap Porcelana

**Path local:** `/tmp/klap-migration/klap-ecommerce/` (volátil — /tmp limpa em reboot; reclone via `gh repo clone PHPB2025K/klap-ecommerce`)
**Repo:** https://github.com/PHPB2025K/klap-ecommerce (privado)
**Branch:** main
**Stack:** React 18 + Vite 5 + TypeScript + Tailwind + shadcn/ui + Supabase + Mercado Pago
**Deploy:** Vercel auto-deploy a partir de push em `main` (sem GHA)
**Domínio:** https://klapporcelana.com.br
**Supabase:** projeto `lzjfswnvqzpqsrjjrwjn`
**Vercel Project:** prj_BicAvuN5LrczA1PRexhz9H3xq8sI

## O que é

Marca de canecas e xícaras de porcelana sob CNPJ GB Importadora — pivot 2026 do mix Budamix saindo de Yiwu (Pedreira-SP). Clone arquitetural do Budamix-ecommerce com identidade visual própria (Azul Klap + Coral + Porcelana cream).

## Paleta oficial

| Cor | HEX | Função |
|-----|-----|--------|
| Azul Klap | `#2440C9` | Primary — botões, links, headers |
| Coral Klap | `#FF6B4A` | Accent — badges, dots (NUNCA dominante) |
| Porcelana | `#F6F2EA` | Background |
| Grafite | `#14162A` | Texto |
| Névoa | `#D2D4DC` | Bordas/apoio |

## Tipografia

- **Montserrat Variable** — títulos, hero, logo (font-heading/font-display)
- **Inter Variable** — corpo, UI, descrições (font-sans/font-body)
- Self-hosted via Fontsource.

## Catálogo

28 produtos ativos em 4 coleções, cada uma com 7 cores (Amarelo, Azul, Branco, Coloridas, Preto, Rosa, Verde):

| Coleção | Slug | Produto base |
|---------|------|--------------|
| Tulipa | `tulipa` | Kit 6 canecas porcelana 250ml |
| Paris | `paris` | Kit 6 xícaras porcelana 170ml |
| Reta | `reta` | Kit 6 canecas porcelana 200ml |
| Canelada | `canelada` | Kit 6 canecas porcelana 250ml |

## Padrão de descrição (PDP)

Toda descrição segue o template `template-descricao-produto-ecommerce.md` (em `/Users/pedrobroglio/Documents/05-Projetos-Codigo/planejamento-importacao-2026/`):

- **Intro** — 1 parágrafo storytelling, 3 movimentos (gancho → cena → fecho); ZERO dado técnico.
- **4 accordions fixos** — Material e acabamento / Dimensões e capacidade / Cuidados e uso / Entrega e devoluções.
- **2 accordions opcionais** — Avaliações de clientes / FAQ.

## Reviews (junho/2026)

- Schema: `product_reviews` + `review_photos`
- Volume: 82 reviews + 77 fotos populadas a partir de 4 docx (Tulipa/Paris/Reta/Canelada) com reviews reais do ML/Shopee
- Rating médio: 4.94/5 · 26 dos 28 produtos com avaliação (Reta Verde + Reta Colorida sem dados)
- Fotos hospedadas em `product-media/reviews/{família}/{review_id}/{idx}.png`
- Componentes consumidores: `TestimonialsSection` (home — só reviews com foto, embaralha) + `ProductReviews` (PDP — todas do produto)

## Marcos recentes

| Data | Marco |
|------|-------|
| 28/05/2026 | Supabase criado, 9/25 migrations aplicadas (checkpoint em /tmp) |
| 29/05/2026 | DNS Registro.br + SSL Vercel ativos |
| 01/06/2026 | Padrão de descrição (intro + 4 accordions) aplicado nos 28 produtos |
| 02/06/2026 | Banner único "Leve mais, pague menos" (desktop + mobile) substitui carrossel |
| 02/06/2026 | 82 reviews + 77 fotos populadas no Supabase |
| 03/06/2026 | Dedup product_images: 424 → 169 (255 duplicatas Amazon CDN removidas) |

## Pendências

- Texto real de "Entrega e devoluções" — ainda usando texto temporário em `ENTREGA_DEVOLUCOES_TEXT` (ProductInfo.tsx)
- Dimensões físicas em `[PREENCHER]` para Paris (7), Reta (7), Canelada (7) — coletar via SP-API/Shopee/ML
- Reta Verde + Reta Colorida sem reviews (sem dados nos docx)
