---
tipo: referencia
projeto: Canggu
status: ativo
tags:
  - canggu
  - supabase
  - pgvector
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Supabase Canggu

## Identidade

| Campo | Valor |
|---|---|
| Project ref | `jpacmloqsfiebvagfomt` |
| Nome oficial | `budamix-ai-agent` |
| Região | sa-east-1 |
| Postgres | 17.6 on aarch64 |
| Pooler | `aws-1-sa-east-1.pooler.supabase.com:5432` |

## Totais (snapshot 2026-04-22)

| Categoria | Total |
|---|---:|
| Schemas não-sistema | 6 |
| Tabelas totais | 63 (public: 11) |
| Functions | 234 (public: 7) |
| Triggers | 21 |
| RLS policies | 26 |
| Indexes | 148 |
| **Foreign Keys** | **11** (integridade referencial intencional — ponto forte) |
| Types/enums | 89 |
| Sequences | 3 |
| Edge functions | 14 deployed (1 ghost — ver [[edge-functions]]) |
| Storage buckets | 0 (áudio não é persistido) |
| Cron jobs | 0 (pg_cron instalado mas não usado) |
| DB webhooks | 0 |
| Realtime tables | ≥1 |
| Custom roles | 1 (`cli_login_postgres`) |

## Tabelas por domínio

### Chat
- `conversations` (64 rows) — estado, category, sentiment, assigned_to (agent | human_agent)
- `messages` (396 rows) — sender, content, tokens_used, whatsapp_message_id ⚠️ SEM UNIQUE

### Clientes
- `customers` (49 rows) — phone, name, tags
- `marketplace_chats`, `marketplace_chat_messages` — ⚠️ **criadas sem migration** (ver [[perguntas-abertas#ADR-004]])

### Produtos (restruturação de phase1)
- `base_products` — base do catálogo com embeddings (vector 1536)
- `products` (87 rows, 3.2 MB) — produtos com FK para base_products, coluna `embedding`
- `kit_compositions` (52 rows) — composição de kits com `embedding`
- `product_listings` (57 rows) — multi-plataforma
- `products_backup_20260404` — 🗑️ órfã (sem migration criadora, 4 MB desperdiçados — ver [[debitos-tecnicos]] achado #17)

### Analytics
- `analytics_daily` — tokens, custos, contagens diárias
- `analytics_monthly`, `analytics_hourly` — agregados

### Marketplace
- `ml_accounts`, `marketplace_tokens` — OAuth
- `marketplace_product_mapping` — product-to-listing
- `marketplace_questions`, `marketplace_answers` — perguntas ML

### Health
- `whatsapp_health_checks` (1.620 rows, 640 kB — maior tabela) — populada pelo workflow `DEjLkJcllQEmrcLF`

### Correções semânticas (feature em andamento)
- `response_corrections` — feedback loop para aprendizado (migration untracked `20260407000000`)
- `responses` — relacionada; uso incerto (verificar em B6)

### Misc
- `policies`, `faq`, `agent_config`, `escalations`, `sync_log`

## Extensões (8)

| Extensão | Versão | Uso |
|---|---|---|
| **vector** (pgvector) | 0.8.0 | Embeddings 1536d em 5 tabelas (ponto forte) |
| **pg_net** | 0.20.0 | HTTP calls a partir de triggers (auto-embedding) |
| pg_graphql | 1.5.11 | GraphQL layer (não usado ativamente) |
| pg_stat_statements | 1.11 | Observabilidade de queries |
| pgcrypto | 1.3 | Cripto básica |
| uuid-ossp | 1.1 | UUID generation |
| supabase_vault | 0.3.1 | Key management (não usado) |
| plpgsql | 1.0 | — |

## Triggers críticos

| Trigger | Tabela | Disparado em | Ação |
|---|---|---|---|
| `trg_product_embedding_sync` | `products` | AFTER INSERT/UPDATE | pg_net → `/functions/v1/sync-product-embedding` |
| `trg_base_product_embedding_sync` | `base_products` | AFTER INSERT/UPDATE | pg_net → `/functions/v1/sync-base-product-embedding` |

**Alerta de segurança:** ambas as trigger functions (`notify_product_embedding`, `notify_base_product_embedding`) contêm **service_role JWT hardcoded** como fallback de `current_setting('app.settings.service_role_key')` — e `ALTER DATABASE SET` nunca foi executado, então o fallback está **sempre ativo**. Ver [[decisoes#ADR-001]] para plano de mitigação.

**Alerta de observabilidade:** pg_net.http_post é fire-and-forget. Se 401/timeout, falha silenciosa. Coluna `embedding` fica NULL invisível. Monitoria em [[debitos-tecnicos#B2]] (cron diário de `embedding IS NULL` count).

## Functions PL/pgSQL críticas (schema public, 7 total)

- `match_products(query_embedding, match_threshold, match_count)` — RPC de busca semântica legacy (tabela products)
- `search_products_semantic(query_embedding, match_threshold, match_count)` — RPC nova (tabela base_products, phase1)
- `search_corrections(query_embedding, ...)` — RPC do feedback loop (migration untracked `20260417120100`)
- `notify_product_embedding()` — trigger func, contém service_role hardcoded
- `notify_base_product_embedding()` — idem
- `update_customer_stats()` — trigger util
- `update_updated_at()` — trigger util

## Colunas AI/embedding

| Tabela | Coluna | Tipo |
|---|---|---|
| `products` | embedding | vector(1536) |
| `base_products` | embedding | vector(1536) |
| `kit_compositions` | embedding | vector(1536) |
| `response_corrections` | embedding | vector(1536) |
| `responses` | embedding | vector(1536) |
| `messages` | tokens_used | integer |
| `analytics_{daily,monthly,hourly}` | total_tokens_used | integer |

## Edge secrets (14)

Ver [[edge-functions#secrets]] e [[decisoes#ADR-002]].

Críticos: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GROQ_API_KEY`, `SUPABASE_SERVICE_ROLE_KEY`.
ML: `ML_APP_ID`, `ML_CLIENT_SECRET`, `ML_REDIRECT_URI`.
WhatsApp: `WHATSAPP_API_KEY`, `WHATSAPP_API_URL`, `WHATSAPP_INSTANCE_NAME`.
Supabase: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`.
🗑️ Órfão: `LOVABLE_API_KEY` (ADR-002).

## Migrations (13 tracked + 2 untracked no working copy)

Evolução coerente em `supabase/migrations/`:

1. `20260227000000_initial_schema` — schema base (customers, conversations, messages, products, ...)
2. `20260228000000_add_message_buffer` — debounce buffer
3. `20260228100000_add_product_embeddings` — pgvector em products
4. `20260306000000_auto_embed_trigger` — **contém service_role hardcoded :42**
5. `20260307000000_add_marketplace_integration` — ml_accounts, marketplace_product_mapping
6. `20260307100000_marketplace_kit_support` — kits
7. `20260307200000_product_listings` — product_listings multi-plataforma
8. `20260404000000_whatsapp_health_checks` — health_checks table
9. `20260404100000_catalog_migration_schema` — ALTER products +17 cols CSV
10. `20260406000000_product_restructure_phase1` — base_products, kit_compositions
11. `20260407000000_response_corrections` — feedback loop table
12. ⚠️ `20260417120000_auto_embed_trigger_base_products` — **UNTRACKED, já aplicada** (contém service_role hardcoded :40)
13. ⚠️ `20260417120100_search_corrections_function` — **UNTRACKED, já aplicada** (search_corrections RPC)

Ver [[debitos-tecnicos]] achado #21 (commit do dirty).

## Auth

- 2 auth users ativos
- raw_user_meta_data keys: apenas `name, email_verified` (sem WhatsApp metadata)
- raw_app_meta_data keys: `role, provider, providers`

## Evidência completa

- Inventário estruturado: `~/audit-canggu-forensics/RAW/A_supabase/` (29 JSONs)
- Análise de drift migrations vs banco: `~/audit-canggu-forensics/RAW/C_analysis/23_migrations_vs_state.md`
- Extensão das evidências sobre triggers: `~/audit-canggu-forensics/RAW/C_analysis/_triggers_expanded.json`
