---
title: "Social Studio · Reborn (Publicador + Métricas Instagram)"
created: 2026-05-06
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/budamix-ecommerce/"
tags:
  - project
  - dev
  - ecommerce
  - social-studio
  - reborn
related:
  - "[[projects/budamix-ecommerce]]"
  - "[[projects/social-studio-carrossel]]"
---

# Social Studio · Reborn

**Path:** `~/Documents/05-Projetos-Codigo/budamix-ecommerce/`
**Subset de:** [[projects/budamix-ecommerce|Budamix E-commerce]] / Social Studio
**Sucessor de:** [[projects/social-studio-carrossel]] (descontinuado em 06/05/2026 após 2 pivots)

## O que é

Painel de controle de redes sociais Budamix. Recebe assets prontos (imagens de carrossel ou single post) + caption + hashtags do usuário (que produz tudo fora — Canva, etc), agenda data/hora de publicação, publica no Instagram via Meta Graph API, e coleta métricas pós-publicação pra dashboard de performance.

**Não toca em criação.** Sem IA. Sem editor de copy. Sem editor visual. Sem biblioteca de hashtags. Todas essas decisões ficam fora do produto.

## Por que existe (jornada de pivots)

1. **Original (PR1 + PR2):** editor visual completo dentro do Social Studio com 5 templates × 3 paletas, geração IA de copy + imagens, render Puppeteer, edição inline. Funcional mas custoso de manter.
2. **Pivot 1 (descartado em 06/05):** `feature/social-studio-pivot-copy-only`. Gerador de copy IA + upload manual de PNGs editados no Canva Pro. Validado E2E mas Pedro decidiu que copy IA também não agrega — usuário prefere escrever caption + hashtags ele mesmo.
3. **Pivot 2 (este, Reborn):** publicador puro + métricas. Sem nenhuma IA.

Branches preservadas no GitHub remoto por 30 dias como referência: `feature/social-studio-pr2`, `feature/social-studio-pivot-copy-only`.

## Schema de dados (Fase A aplicada em prod 06/05)

| Tabela | Status | Função |
|---|---|---|
| `social_posts` | ALTER (17 rows preservados) | Posts unificados (carousel/single). Status: draft/scheduled/publishing/published/failed |
| `social_accounts` | NOVA | Multi-plataforma-ready (CHECK platform IN ('instagram')). vault_secret_id aponta pra vault.secrets pro token Meta |
| `social_post_metrics` | NOVA | Snapshots append-only de Meta Graph /insights. engagement_rate é GENERATED STORED |
| `social_archive_*_pre_reborn_2026_05_06` | DEFENSIVO (RLS admin-read) | Snapshot de posts/carousels/slides legacy antes do drop |

Todas tabelas legacy (templates, palettes, carousels, slides, jobs, telemetry, publish_logs) **dropped** + 5 views analíticas **dropped**.

Indices críticos:
- `social_posts (status, scheduled_at) WHERE status IN ('scheduled', 'publishing')` — partial, hot path do worker
- `social_post_metrics (post_id, collected_at DESC)` — dashboard busca métrica mais recente

## Stack

- **Frontend:** React 18 + Vite + TS + Tailwind + shadcn/ui (mesmo do budamix-ecommerce)
- **Backend:** Supabase (Postgres + Edge Functions + Storage + Realtime + Vault)
- **Cron:** Supabase Cron Jobs (pg_cron + pg_net) — `cron.schedule()` chamando edge functions
- **Publicação:** Meta Graph API (Instagram Business Account `@budamix.br`)
- **Métricas:** Meta Graph `/{post_id}/insights`
- **Storage:** bucket `social-assets` mantido com convenção `posts/{post_id}/asset-{N}.{ext}`

## Roadmap em 4 fases

### Fase A · Limpeza total + schema novo (1 dia) ✅ CONCLUÍDA 06/05

PR #3: https://github.com/PHPB2025K/budamix-ecommerce/pull/3 (aguardando merge)

Branch: `feature/social-studio-reborn` — 7 commits.

- A1 (`0df815c`): hide nav + remove routes
- A2 (`a2ba134`): delete frontend legacy (25+ arquivos)
- A3 (`8cc81bc`): delete edge functions local
- A4 (`3dbf57c`): migration archive defensivo (17/17/48 rows)
- A5 (`086a40c`): drop legacy schema (CASCADE)
- A6 (`ca0c5b6`): create reborn schema (accounts, post_metrics, posts ALTER)
- ops (`d6e76d5`): delete 5 edges em prod via REST API com PAT do MCP — sem ação manual

Side-effect prod resolvido: 5 edges legacy DELETADAS via `DELETE /v1/projects/{ref}/functions/{slug}` da Supabase Management API. Validado via `mcp list_edge_functions` — só restam 3 edges não-Social-Studio (MP + orders).

### Fase B · Composer + Agendador (~2 dias) ⏳ PRÓXIMA

- Tela `/admin/social/posts` (lista + calendário)
- Tela `/admin/social/posts/novo` (composer)
- Tela `/admin/social/posts/[id]` (editor)
- Validações (carousel 2-10, single 1, caption ≤2200, scheduled futuro)
- Upload de assets pro bucket `social-assets/posts/{post_id}/`
- pg_cron criado mas mock (marca publishing → published sem chamar Meta)
- Reaproveitar: `useSocialJobsChannel` (renomeado), `STATUS_LABEL/DOT` (adaptados), `SlideImageUploader` (refatorado pra `PostAssetUploader`)

### Fase C · Publicação Instagram real (~2-3 dias)

- Tela `/admin/social/conta` — Meta OAuth pra vincular @budamix.br
- Edge `publish-instagram-post` (carousel = 2-step containers + agrupamento; single = 1-step)
- pg_cron real disparando edge
- Refresh automático de token long-lived (cron mensal)

### Fase D · Métricas e Dashboard (~2-3 dias)

- Edge `collect-instagram-metrics` (cron diário 03:00, posts published <90d)
- Tela `/admin/social/dashboard` (KPIs + tabela ordenável + gráfico recharts + export CSV)
- Cards de post na lista ganham métricas resumidas

## Decisões fundadoras

| ID | Decisão | Data |
|---|---|---|
| R1 | Sem IA no produto | 06/05 |
| R2 | Carousel + single no MVP, story/reel pendentes | 06/05 |
| R3 | Single conta (@budamix.br); schema preparado pra multi | 06/05 |
| R4 | pg_cron+pg_net (Cron Jobs Supabase) vs Scheduler puro | 06/05 |
| R5 | Bucket social-assets mantido; convenção `posts/{post_id}/asset-{N}` | 06/05 |
| R6 | media_type text+CHECK (não enum) — evolução fácil | 06/05 |
| R7 | engagement_rate GENERATED STORED — single source of truth | 06/05 |
| R8 | Vault pro token Meta (vault_secret_id sem FK cross-schema) | 06/05 |
| R9 | Archive defensivo antes de drop legacy | 06/05 |
| R10 | Conta Instagram Business com Facebook Page já vinculada | 06/05 |

## Referências

- Briefing original (anexo da sessão): `~/Documents/05-Projetos-Codigo/budamix-ecommerce/social-studio-reborn-briefing.md` (se Pedro salvou)
- PR Fase A: https://github.com/PHPB2025K/budamix-ecommerce/pull/3
- PR2 backup: https://github.com/PHPB2025K/budamix-ecommerce/tree/feature/social-studio-pr2
- Pivot 1 backup: https://github.com/PHPB2025K/budamix-ecommerce/tree/feature/social-studio-pivot-copy-only
