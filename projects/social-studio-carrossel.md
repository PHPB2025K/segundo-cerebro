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

## Estado atual (03/05/2026 noite)

⏸ **Pausado em Fase 0**, aguardando ações:

1. **Pedro reiniciar sessão Claude Code** — Paper MCP está adicionado globalmente (`claude mcp list` confirma `paper: ✓ Connected`) mas a sessão atual não carregou as tools `mcp__paper__*`. Reiniciar resolve.
2. Após reinício: CC retoma com `/cerebro` → lê esta ficha → continua Fase 0 (capturar baselines + draft system prompt).

## Como retomar (próxima sessão)

1. `/cerebro` no terminal
2. Ler esta ficha: `cat ~/segundo-cerebro/projects/social-studio-carrossel.md`
3. Verificar Paper MCP carregado: `ToolSearch query "paper write_html"` deve achar tools
4. Se OK: capturar 96 baselines → batch via Paper MCP `get_basic_info` + `get_screenshot`
5. Em paralelo: draftar `docs/social-studio-carrossel-prompt-copy.md`
6. Pedro identifica app Meta existente em paralelo

## Referências cruzadas

- [[projects/budamix-ecommerce]] — projeto pai
- [[business/marketing/marca/templates-carrossel-paper]] — documentação dos 5 templates Paper
- [[business/marketing/marca/recomendacao-carrosseis]] — SIMON 7 formatos
- [[business/marketing/marca/recomendacao-legendas]] — fórmula 60/30/10
- [[business/marketing/marca/manual-hashtags]] — 4 camadas, 8–10 tags
- [[business/marketing/marca/design-system]] — Design System v1.2
- [[memory/context/decisoes/2026-04#[29/04 noite] Blog Budamix Pipeline v2]] — padrão IA aplicável
