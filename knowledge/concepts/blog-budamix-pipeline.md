---
title: "Pipeline do Blog Budamix — arquitetura e workflows N8N"
created: 2026-06-09
type: knowledge
status: active
tags:
  - knowledge/blog
  - knowledge/n8n
  - knowledge/budamix-ecommerce
---

# Pipeline do Blog Budamix

## Visão geral

Pipeline editorial em 5 etapas, executado em N8N + Supabase + frontend admin (Vercel). Existe em dois modos:

- **Modo radar** (full): WF0 Perplexity gera pauta → admin escolhe → WF4 orquestra → WF2 escreve → WF3 (DESLIGADO desde 06/06) gera imagens. Pauta vem rica em research.
- **Modo tema livre** (novo, 06/06): admin escreve tema → frontend cria pauta sintetizada → WF4 orquestra → WF2 escreve (com self-enrichment interno) → imagens ficam vazias pro admin subir manual.

## Workflows N8N (live em `trottingtuna-n8n.cloudfy.live`)

| Workflow | ID | Função | Status |
|----------|-----|--------|--------|
| **WF0 — Radar de Pautas** | `QBVA6TZ5O6O3tzCP` | Perplexity pesquisa tópicos atuais e gera pautas com `raw_research`, `freshness_notes`, `target_keyword`, `search_intent` | ativo |
| **WF2 — Article Generator** | `IG9KBmrEGts3CDp8` | Claude Sonnet 4.6 escreve artigo + cria slots de imagem com prompts | ativo |
| **WF3 — Image Generator (Gemini)** | `OkaGMhd7iXarsikl` | Geraria imagens via Gemini 3 Pro Preview | **DESCONECTADO em 06/06** (créditos esgotados, pivot pra upload manual) |
| **WF4 — Orchestrator** | `jyJ0d79yZgPqcGeT` | Encadeia WF2 (texto) + WF3 (imagens, agora pulado) + final_validation | ativo (short-circuit) |

## API key e acesso

- API key (`X-N8N-API-KEY`): `~/Documents/05-Projetos-Codigo/N8N-BUILDER/.mcp.json` (env do server `n8n` no MCP)
- Backups dos workflows: `~/Documents/05-Projetos-Codigo/budamix-ecommerce/n8n-workflows/` (5 JSONs versionados no repo)

## Fluxo do tema livre (modo 06/06+)

1. User digita tema no admin `/admin/blog` aba **Pautas** → card "Tema personalizado"
2. `generateArticleFromCustomTopic` em `BlogAdmin.tsx`:
   - Cria row em `blog_ideas` com `status='utilizada'`, `source='admin-blog-custom-topic'` (pauta dummy pra não quebrar orchestrator)
   - Cria row em `blog_posts` com `status='gerando'`, `pauta_origem` = id da pauta criada
   - Chama webhook do **WF4 orchestrator** com `{ post_id, idea_id, run_id }`
3. **WF4**:
   - "Normalizar input WF4" valida payload
   - "Marcar geração rodando" → "Marcar etapa artigo"
   - "Chamar WF2 — Gerar artigo" via HTTP
   - "Extrair post do WF2" → emite `body` com `status='em_edicao'` direto pra "Marcar artigo em edição" (short-circuit pula 8 nós da pipeline de imagem)
4. **WF2**:
   - "Preparar busca do artigo" (tolera `idea_id=null`, usa UUID dummy)
   - "Buscar pauta no Supabase" (`alwaysOutputData=true` propaga mesmo com array vazio)
   - "Buscar post no Supabase"
   - "Combinar pauta e post" (sintetiza idea a partir de blog_posts quando ausente)
   - "Buscar post anterior do pilar" + "Buscar capa anterior" (referência negativa)
   - "Preparar prompt editorial" monta `userPrompt` com `currentPauta`, `RAW RESEARCH SUMMARY`, `REFERÊNCIA NEGATIVA`
   - "Gerar artigo com IA" — Claude Sonnet 4.6 via `lmChatAnthropic` (sem tools, sem web_search)
   - "Validar artigo gerado" — strict pra estrutura, lenient pra image-prompt content
   - "Atualizar post para edição" PATCH em `blog_posts`
   - "Preparar slots de imagem" → "Salvar slots de imagem" (POST batch em `blog_post_images` com `image_status='pending'`)
   - "Responder OK" devolve `{ post_id, slug, ... }` pro WF4
5. **WF4 final**: "Marcar artigo em edição" PATCH `status='em_edicao'`, `generation_step='completed'`, `generation_progress=100`
6. **Admin** mostra post em "Em geração" → aparece em "Rascunhos" quando WF4 termina
7. Admin abre post → vê 4 slots vazios (cover + 2 support + 1 pinterest) com prompts prontos
8. Admin **sobe imagens manualmente** ou clica "Gerar com IA" (vazio enquanto Gemini sem crédito)

## Self-Enrichment do Claude (system prompt do WF2)

Bloco "SELF-ENRICHMENT — entrada tema livre vs. pauta refinada" detecta entrada crua (sinais: `raw_research_summary.source='custom-topic-fallback'` OU `target_keyword` vazio OU `freshness_notes` vazio OU `pillar='Tema livre — '`). Quando detecta, obriga Claude a autoderivar mentalmente ANTES de escrever:

1. Título refinado (mantendo essência, SEO + voz Budamix)
2. Ângulo: público-alvo concreto + gancho + 3-4 sub-blocos + diferencial
3. Pillar editorial classificado (cozinha funcional, conservação, organização, marmita, decoração, limpeza, etc.)
4. Target keyword principal + 2 secundárias
5. Search intent (informational/comparative/transactional/inspirational)
6. Contexto sazonal quando aplicável
7. **Antiviés**: lista 2-3 ângulos manjados que NÃO vai seguir (técnica via negativa pra forçar criatividade)

Pautas que JÁ vieram do radar (raw_research populado pela Perplexity) seguem o caminho normal sem este bloco.

## Viés pró-potes herméticos de vidro (system prompt do WF2)

3 linhas adicionadas:
- "Leve viés editorial pró-potes herméticos de vidro QUANDO tema toca em armazenamento, conservação de alimentos, marmita, meal prep, organização de despensa/geladeira/freezer ou rotina de cozinha"
- Destaca vantagens reais e verificáveis: não absorvem cheiros/manchas, suportam freezer→micro→lavadora, vedação confiável, conteúdo visível, durabilidade longa, livre de BPA — de forma natural e consultiva, NUNCA panfletária
- Em temas fora desse universo (limpeza pesada, decoração estética, finanças, lavanderia, banheiro), segue NEUTRO
- Citar marca "Budamix" é opcional; o ganho é o leitor enxergar pote hermético de vidro como escolha funcional padrão

## Recuperação automática de posts em "falhou"

`pg_cron` job `reconcile_blog_generation` roda a cada 2 minutos:
```sql
WHERE status = 'falhou'
  AND generation_error_stage = 'final_validation'
  AND content > 300 chars
  AND seo_title NOT NULL
  AND seo_description NOT NULL
  AND generation_started_at > NOW() - INTERVAL '24 hours'
```
Verifica se 1 cover + 2+ support + 1+ pinterest têm `image_status='generated'` e `image_url`. Se sim → reabilita pra `em_edicao`. Migration: `20260604120000_blog_reconcile_falhou_posts.sql`.

## RLS fixes (06/06)

- `blog_post_images` — policy "Public can read images for published blog posts" filtrava `status='published'` (inglês); corrigido pra `'publicado'` (português). Migration: `20260604140000_fix_blog_post_images_public_read_status.sql`.
- Storage `blog-images` — bucket public:true mas sem policies INSERT/UPDATE/DELETE pra `authenticated`. Adicionadas 3 policies usando `is_admin()`. Migration: `20260604130000_blog_images_storage_policies.sql`.

## Tabelas Supabase

- `blog_posts` — campos chave: `status`, `generation_status`, `generation_step`, `generation_progress`, `generation_error_stage`, `generation_run_id`, `pauta_origem`, `pilar_editorial`, `source`, `cover_image_url`, `content`, `seo_title`, `seo_description`
- `blog_post_images` — slots de imagem: `slot_key` (cover/support_1/support_2/support_3/pinterest_1/pinterest_2/pinterest_3), `slot_label`, `placement_index`, `image_prompt`, `image_alt`, `image_url`, `image_status` (pending/generating/generated/failed), `aspect_ratio` (16:9 ou 2:3), `image_model`
- `blog_ideas` — pautas (radar ou tema livre): `theme`, `title_suggestion`, `angle`, `target_keyword`, `freshness_notes`, `search_intent`, `seasonal_context`, `related_products`, `raw_research` (jsonb), `priority`, `status` (nova/utilizada/rejeitada), `source` (n8n-radar / perplexity-radar / admin-blog-custom-topic)
- `blog_pillars` — pilares editoriais

## Ver também

- [[projects/budamix-ecommerce]] — projeto onde tudo vive
- [[memory/context/decisoes/2026-06]] — decisões que originaram a refatoração
