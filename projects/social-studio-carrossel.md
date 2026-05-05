---
title: "Social Studio · Módulo de Carrossel"
created: 2026-05-03
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/budamix-ecommerce/"
spec: "docs/social-studio-carrossel-spec.md"
tags:
  - project
  - dev
  - ecommerce
  - social-studio
  - carrossel
related:
  - "[[projects/budamix-ecommerce]]"
  - "[[business/marketing/marca/templates-carrossel-paper]]"
---

# Social Studio · Módulo de Carrossel

**Path:** `~/Documents/05-Projetos-Codigo/budamix-ecommerce/`
**Spec canônica:** [`docs/social-studio-carrossel-spec.md`](https://github.com/PHPB2025K/budamix-ecommerce/blob/main/docs/social-studio-carrossel-spec.md) (commit `7670f2a`, 03/05)
**Subset de:** [[projects/budamix-ecommerce|Budamix E-commerce]] / Social Studio

## O que é

Módulo de geração assistida por IA de carrosséis para Instagram dentro do Social Studio. Substitui o fluxo "criar carrossel slot por slot" por caminho guiado:

1. Usuário escolhe **1 dos 5 templates oficiais** × **1 das 3 paletas cromáticas** = grid 15 cartões
2. Briefing curto: tema + propósito (+ direção fina opcional por card)
3. IA preenche copy (Claude Sonnet 4.6) + gera imagens (Gemini Nano Banana)
4. Preview = editor completo: edição inline, regerar imagem, reordenar, +/- cards, trocar paleta, trocar template
5. Saída: export PNG/PDF/JPG **ou** publicação direta no `@budamixoficial` via Meta Graph API

## Templates oficiais (Paper.design `01KQMVPNGXW4ZWQPVE1KDPMBN3`)

| Slug | Slides | Função |
|---|---|---|
| `lancamento` | 6 | Apresentar produto/coleção novo |
| `lista` | 7 | "X motivos / X dicas / X erros" |
| `tutorial` | 7 | "Como fazer X" sequência didática |
| `storytelling` | 6 | Antes/depois, transformação |
| `credibilidade` | 6 | Social proof, autoridade, depoimentos |

3 versões cromáticas (CLARA Areia / NORMAL Teal / ESCURA Grafite). Acentos fixos: dourado `#C7A35A` na palavra-chave, terracota `#C56A4A` no CTA.

Documentação dos templates: [[business/marketing/marca/templates-carrossel-paper]]

## Decisões tomadas (03/05/2026)

| ID | Decisão | Razão |
|---|---|---|
| D1 | Descartar wizard Kobe atual (commits `a66e319` + `7df4c1b` na VPS) e começar fresh | Wizard atual é "criar slot a slot livremente"; módulo novo é "template+briefing → IA gera". Produto diferente, adaptar custa mais que reescrever |
| D2 | Capturar 96 baselines via Paper MCP (não 45) | Cobertura completa elimina ambiguidade no QA visual; tempo extra via batch é marginal |
| D3 | Usar app Meta existente da Budamix | Evita criar app novo, rota mais rápida pra publicação IG |
| D4 | Telemetria via Supabase nativo (não PostHog) | Admin interno com 1 usuário primário; 5 queries SQL cobrem tudo; PostHog é overkill |
| D5 | Implementação paralela CC + Kobe | Mesmo padrão Blog Pipeline v2 (funcionou bem); reduz timeline de 5–6 sem pra ~4 sem |
| D6 | Templates como dados em jsonb (`social_templates.structure`) | Mesmo padrão `blog_pillars`; mudar template não exige deploy |
| D7 | Trocar template descarta copy (com confirmação dupla) | Mapeamento entre templates é não-trivial; gerar do zero é rápido |
| D8 | Quota mensal $50 (não por carrossel) | Exploração visual é parte do valor; alinha com unidade real de orçamento |
| D9 | Trocar paleta preserva copy (só re-render) | Operação barata (~$0.007 × N slides), reversível |
| D10 | Adicionar/remover cards livre (range 1–20) | Lista de 2 ou 15 itens muda vibe — usuário decide |

## Plano de implementação

### Fase 0 · Pré-trabalho (3 dias) — em andamento

- [ ] **Capturar 96 baselines do Paper via MCP** — `/test/visual-baselines/{T1-T5}/{clara,normal,escura}/slide-{N}.png` ⏸ aguardando reinício de sessão pra carregar Paper MCP
- [ ] **Setup Meta Graph API + long-lived token IG no Vault** — Pedro identifica app Meta existente + gera token + Kobe coloca em Supabase Vault
- [ ] **Draft do system prompt da IA copy** — `docs/social-studio-carrossel-prompt-copy.md` no repo (CC drafta, Pedro aprova)
- [x] Decisão sobre wizard Kobe — descartar (D1)

### Fase 1 · Fundação (1–2 semanas)

Caminho feliz mínimo: escolher template+paleta → briefing → IA gera → preview renderizado (sem edição).

**Backend (Kobe):**
- Migrations: `social_templates`, `social_palettes`, alters em `social_carousels`/`social_carousel_slides`
- Seed: 5 templates × structure JSON + 3 paletas
- Edge Functions: `social-generate-copy`, `social-generate-image`
- Endpoints: `/templates`, `/palettes`, `/template-grid`, CRUD `/carousels`, `/generate`

**Frontend (CC):**
- Tela 1: grid 15 cartões com renders cacheados
- Tela 2: briefing form (tema + propósito + direção fina collapsed)
- Tela 3: preview básico read-only com Realtime
- 8 componentes React de render: `_layout`, `cover`, `cover-numeric`, `item`, `tutorial-step`, `before-after`, `credibility-card`, `testimonial`, `cta`
- Adaptação do render engine (parte de `9e6af3d`)

### Fase 2 · Editor completo (1 semana)
Edição inline, regerar imagem, reordenar (drag-drop), +/- cards, trocar paleta, trocar template.

### Fase 3 · Saída (1 semana)
Caption (60/30/10) + hashtags (4 camadas) + export PNG/PDF/JPG + listagem rascunhos + duplicar.

### Fase 4 · Publicação IG (1 semana)
Meta Graph API + cron refresh token + UI status + reconexão self-serve em `/admin/social/instagram-config`.

### Fase 5 · Hardening (1 semana)
QA visual diff em CI (3% tolerância) + rate limiting + quota mensal $50 + audit log + tradução erros Meta + telemetria + E2E Playwright.

**Total: 5–6 semanas para MVP publicável.**

## Stack técnica

- **Frontend:** React 18 + Vite + TypeScript + Tailwind + shadcn/ui (mesmo do budamix-ecommerce)
- **Backend:** Supabase (Postgres + Edge Functions + Storage + Realtime + Vault)
- **IA copy:** Claude Sonnet 4.6 (Anthropic API, padrão Blog Pipeline v2)
- **IA imagem:** Gemini Nano Banana / `imagen-4` (padrão Blog Pipeline v2)
- **Render PNG:** Puppeteer + componentes React server-side (HTML/CSS)
- **Publicação:** Meta Graph API (Instagram Business Account `@budamixoficial`)
- **Drag-and-drop:** `@dnd-kit/sortable`

## Custo estimado

- Por carrossel publicado (sem regen): ~$0.31
- Com 3 regens médias: ~$0.43
- 16 carrosséis/mês ≈ **$7/mês em IA**
- Limite duro mensal: $50/workspace

## Estado atual (04/05/2026)

✅ **FASE 1 FECHADA E EM PRODUÇÃO** — pipeline E2E funcionando:

| Etapa | Owner | Commit | Métrica chave |
|---|---|---|---|
| A · Schema v3 | Kobe | `ff79ee5` | 5 templates · 3 paletas · 5 views · RLS OK |
| B · IA Copy | Kobe | `4ff9f0a` | $0.045/carrossel · gancho 11 palavras · 3 caveats |
| C · IA Imagem | Kobe | `ae7ff43` | $0.04/img · 7.7s p50 · Nano Banana |
| D · Render Puppeteer | Kobe | `071a277` | hot 1.31s · cold 18.6s (backlog F5) |
| E · Export PNG/PDF | Kobe | `8ab45da` | 2.1s ZIP · 2.4s PDF · JPG 400 controlado |
| Frontend (CC) | CC | `0670608`+iters | 3 telas + 9 componentes render + rota Puppeteer |

**Custo real validado:** ~$0.31 por carrossel completo (alinhado com spec).
**Tempo total briefing→pronto:** ~28-35s (cold) / ~10s (hot cache).

### Iterações de polish após Fase 1 fechada (04/05/2026 tarde-noite)

8 iterações de smoke E2E e ajustes visuais com Pedro:

- iter 1: `getCarouselFull` refatorado em 4 queries (PostgREST embedding multi-nível bug) — `c32929c`
- iter 2: signed URLs batch pra imagens privadas do bucket `social-assets` — `46a7ee0`
- iter 3: auto-shrink fontSize quando texto excede confortável + R10 prompt + max_chars 42 (Kobe `60fdb00`) — `fa9e40a`
- iter 4: logos PNG `/public/logos/*.png` (eram 404) — `558a3ef`
- iter 5: SwipeIndicator implementado e iterado (cápsula → seta+barra → removido completo) — `97848e3`
- iter 6: brand header (cover/cta) + footer URL + fontes Variable correção crítica — `65d7ed2`
- iter 7: header em todos slides + remove logo + seta discreta — `0f21c90`
- iter 8: trocar lados URL e seta — `433bc7f`

### Decisões adicionais (04/05/2026)

| ID | Decisão | Razão |
|---|---|---|
| D11 | Trocar key Anthropic legacy `sk-ant-...` por `sk-ant-api03-...` | API antiga revogada — 401 invalid x-api-key |
| D12 | Billing Google AI Studio ativado no projeto SOCIAL STUDIO | Sem billing, Imagen/Nano Banana não disponíveis |
| D13 | render-bot user dedicado pra Puppeteer (uuid `585f0ac3-...`) | Service_role no client é inseguro; magic JWT user-scoped + role admin é o caminho |
| D14 | Cold start Puppeteer 18.6s aceito como Fase 1 | Cache hot 1.31s cobre 90% casos. Refactor pra container warm = backlog F5 |
| D15 | JPG bundle FORMAT_UNAVAILABLE controlado | Encoder JPG em Edge Function instável; PNG ZIP + PDF cobrem uso real |
| D16 | Imagem AI ocupa 60% top + gradient fade pra paleta | Visual mais limpo que full-bleed; texto não compete com imagem |
| D17 | Auto-shrink fontSize + R10 prompt | Defesa em profundidade: IA respeita max_chars + frontend protege overflow |
| D18 | Header brand `BUDAMIX | OUTONO · NN / TT` em todos slides | Identidade institucional sutil; usa palette.eyebrow ou highlight |
| D19 | Logo PNG removido, substituído por seta `→` discreta canto inferior esquerdo | Pedro pediu — minimalismo + indicador de swipe |
| D20 | URL `BUDAMIX.COM.BR` canto inferior direito | Reforça canal sem ser CTA agressivo |
| D21 | Fontes Variable obrigatórias (`'Bricolage Grotesque Variable'`, etc) | Sem isso, Puppeteer caía em fallback Helvetica genérica — quebrava fidelidade visual |

### O que foi pulado (não vai virar Fase 2)

- **Editor inline** (Fase 2 original): Pedro decidiu pular — confia que IA gera bem com R10 + max_chars apertados + auto-shrink. Reavaliar se precisar editar fora do refresh
- **Template panorama** (Fase 6): descartado por agora — complexidade alta sem caso de uso comprovado

### Próximas decisões pendentes

- Fase 4 publish IG (1 sem) OU Fase 5 hardening (1 sem) — Pedro decide ordem
- Backlog F5 priorizado: cold start render → container warm; JPG encoder; QA visual diff CI; rate limiting + audit log

## PR2 · Cor por elemento + Histórico de imagens (05/05/2026)

✅ **PR2 ~95% — C1 a C6 entregues, validado visualmente**. Implementado entre 05/05 manhã e noite.

| Commit | Owner | Entrega |
|---|---|---|
| C1+C1.5 migrations | CC | `element_styles jsonb` + `image_versions jsonb` + backfill 21 slides sintéticos |
| C2 helpers | CC | `lib/element-style-tokens.ts` com 7 tokens · `resolveSlotColor` · `colorOverrideForSlot` (conservador) · `updateSlideElementStyle` |
| C3 ColorTokenPicker | CC | Swatches inline 3-estados (custom/default/limpar) · botão × · `cta_terracotta` exclusivo de `cta_button` |
| C4 templates | CC | 11 templates + Eyebrow shared usando `colorOverrideForSlot(slot, ...) ?? palette.X` — visual 100% preservado quando sem custom |
| C5 edge function | CC | `social-generate-image` v10 com append em `image_versions` + truncate `slice(-5)` · entries: id, image_asset_id, prompt, reference_image_url=null, cost, created_at |
| C6 popover | CC | `ImageVersionsPopover.tsx` (213 linhas) · badge `vN/total` clicável · thumbs com signed URLs sob demanda · restore zero-custo · regenerar inline com guard de quota >80% |

### Decisões PR2

| ID | Decisão | Razão |
|---|---|---|
| D22 | Token semântico em `element_styles` (não RGB literal) | Ajustar paleta no futuro propaga em elementos customizados |
| D23 | Manter blobs no bucket ao rotacionar versões (5 max) | Storage barato; cleanup futuro >90d como PR independente |
| D24 | Padrão conservador `colorOverrideForSlot` no C4 (não `resolveSlotColor` completo) | `SLOT_DEFAULT_TOKEN` diverge do render real em alguns slots — preservar visual quando sem custom |
| D25 | Edge function `generate-social-copy` reescrita com 2 queries em vez de embedded join `palette:social_palettes(*)` | Migration `palette_key_decouple` dropou FK; PostgREST não resolve embed sem FK → 404 enganoso |
| D26 | `image_versions[].prompt = imageBrief` (não prompt completo enviado ao Gemini) | Coerência com `slide.image_prompt` e backfill C1.5; `aiKeywords` + RESTRICTIONS são uniformes |
| D27 | Restore zero-custo · não bumpa `image_version` numérico · não toca `image_versions` array | Restore aponta de volta, não cria entry; "versão ativa" deriva do índice da entry com `image_asset_id == slide.image_asset_id` |
| D28 | Geração individual em slide vazio fica para PR3 | C6 = "regenerar/restaurar versão" (slide já tem imagem); PR3 = "criar imagem sob demanda" (módulo coeso) |
| D29 | Bug visual `cover-numeric` levantado mas NÃO corrigido na sessão | Pedro decide entre 3 opções de fix (mínimo / +tech debt / outro) na próxima sessão |

### Falta apenas no PR2

- [ ] **Bug cover-numeric**: `SlideRenderer.tsx:143` instancia `<CoverNumeric>` sem `imageUrl={img}`. Imagem é gerada (~$0.04) mas template nunca renderiza trans inferior 480px. Inconsistência colateral em `Editor.tsx:777` (`'cover-numeric'` em `noImage` do `needsImage`). Fix mínimo: 2 linhas.
- [ ] **Tech debt lateral (não-bloqueante)**: edge function gera imagem pra slides item posições 2/6 do `lista` que nunca renderizam (~$0.08/carousel desperdiçado). Solução: edge function aceitar lista de slide_ids do frontend.

## Como retomar (próxima sessão)

1. `/cerebro` no terminal
2. Pedro decide entre 3 opções de fix do bug cover-numeric (mínimo / +tech debt / outro) → fechar PR2 100%
3. Depois: PR3 (modo manual default + ImageGenerationDialog + geração individual em slide vazio + foto de referência)
4. Eventualmente Fase 4 (publish IG) ou Fase 5 (hardening)

## Referências cruzadas

- [[projects/budamix-ecommerce]] — projeto pai
- [[business/marketing/marca/templates-carrossel-paper]] — documentação dos 5 templates Paper
- [[business/marketing/marca/recomendacao-carrosseis]] — SIMON 7 formatos
- [[business/marketing/marca/recomendacao-legendas]] — fórmula 60/30/10
- [[business/marketing/marca/manual-hashtags]] — 4 camadas, 8–10 tags
- [[business/marketing/marca/design-system]] — Design System v1.2
- [[memory/context/decisoes/2026-04#[29/04 noite] Blog Budamix Pipeline v2]] — padrão IA aplicável
