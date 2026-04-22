---
tipo: referencia
projeto: Canggu
status: ativo
tags:
  - canggu
  - edge-functions
  - supabase
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Edge Functions

> 14 functions deployed no Supabase (project `jpacmloqsfiebvagfomt`) vs 13 no repo.
> Deficit de 1 = `test-search` ghost (deploy sem código versionado).

## Tabela de referência

| Function | Estado | LOC | Invocada por | verify_jwt (hoje) | ADR/Achado |
|---|---|---:|---|:-:|---|
| `webhook-whatsapp` | ⏳ Em depreciação após ADR-007 | 490 | Evolution Cloudfly (ou N8N — ver [[arquitetura]]) | false | [[decisoes#ADR-007]] |
| `process-message` | ✅ Ativa (core) | 630 | N8N + webhook-whatsapp | false | — |
| `send-whatsapp` | ✅ Ativa (interna) | 139 | process-message, escalate | false | — |
| `send-human-message` | ✅ Ativa | 126 | Frontend `src/lib/api.ts:238` via fetch | false | [[debitos-tecnicos]] #14 |
| `escalate` | ✅ Ativa (interna) | 278 | process-message (via classifier) | false | — |
| `ml-webhook` | ✅ Ativa (externa) | 502 | Mercado Livre webhook | false | — |
| `ml-oauth` | ✅ Ativa (externa) | 276 | OAuth callback ML | false | — |
| `process-ml-question` | ✅ Ativa | 328 | ml-webhook; N8N `workflow-ml-questions` | false | [[decisoes#ADR-006]] (pendente) |
| `process-ml-message` | ✅ Ativa | 325 | N8N `workflow-ml-messages` | false | — |
| `sync-product-embedding` | ✅ Ativa (trigger) | 175 | trigger `trg_product_embedding_sync` via pg_net | false | [[decisoes#ADR-001]] |
| `sync-base-product-embedding` | ✅ Ativa (trigger) | 114 | trigger `trg_base_product_embedding_sync` via pg_net | false | [[decisoes#ADR-001]] |
| `process-correction-embedding` | ✅ Ativa (trigger) | 65 | trigger em response_corrections (inferido) | false | — |
| `test-semantic-search` | 🔒 Manter com JWT | 28 | — (debug manual) | false → **true após B6** | [[decisoes#ADR-003]] |
| `test-search` | 🗑️ **GHOST — deletar em B1** | ? | — (sem chamador) | false | [[auditorias/2026-04-22-forense#Achado-2]] |

## Classificação por público-alvo

### Externas (manter `verify_jwt=false`)
- `webhook-whatsapp` (Evolution webhook — se for o canônico pós-ADR-007)
- `ml-webhook` (ML webhook)
- `ml-oauth` (OAuth callback)

### Internas (habilitar `verify_jwt=true` em B1)
- `process-message` (chamada pelo N8N via service_role) ou por webhook-whatsapp interno
- `send-human-message` (chamada pelo frontend autenticado com user JWT)
- `send-whatsapp` (chamada por process-message/escalate — passagem de service_role)
- `escalate` (chamada interna)
- `sync-product-embedding`, `sync-base-product-embedding` (chamadas por triggers pg_net com service_role)
- `process-correction-embedding` (idem)
- `process-ml-question`, `process-ml-message` (chamadas por N8N ou ml-webhook com service_role)

### Debug (proteger com JWT)
- `test-semantic-search` (ADR-003 mantém com `verify_jwt=true` + README)

### Deletar
- `test-search` (ADR-003 + B1 passo 2)

## Módulos compartilhados (`_shared/`)

| Arquivo | LOC | Responsabilidade |
|---|---:|---|
| `types.ts` | 457 | Tipos TypeScript compartilhados |
| `evolution-api.ts` | 201 | Evolution API client (sendText, setPresence, getMediaBase64) |
| `response-generator.ts` | 178 | Claude Sonnet para geração de resposta |
| `response-validator.ts` | 162 | Validação chunks/formato |
| `embeddings.ts` | 159 | OpenAI embeddings + pgvector search |
| `context-builder.ts` | 153 | Monta contexto (6 queries paralelas) |
| `intent-classifier.ts` | 144 | Claude Haiku para classify |
| `config.ts` | 122 | Config loader com cache 5min |
| `groq-transcription.ts` | 64 | Groq Whisper wrapper |
| `anthropic.ts` | 59 | Anthropic API wrapper |
| `cors.ts` | 32 | CORS headers — `*` global (achado #16) |
| `supabase-client.ts` | 16 | Cliente Supabase com service_role (via env — seguro) |

## Secrets em uso

Declarados: 14 (via `supabase secrets list`). Usados ativamente: 13. Órfão: 1 (`LOVABLE_API_KEY` — [[decisoes#ADR-002]]).

```
ANTHROPIC_API_KEY          → _shared/anthropic.ts (intent-classifier, response-generator)
OPENAI_API_KEY             → _shared/embeddings.ts
GROQ_API_KEY               → _shared/groq-transcription.ts
SUPABASE_SERVICE_ROLE_KEY  → _shared/supabase-client.ts, ml-webhook, webhook-whatsapp (todos via Deno.env.get — seguro)
SUPABASE_URL               → _shared/supabase-client.ts
SUPABASE_ANON_KEY          → não usado em edge fn (frontend usa)
WHATSAPP_API_KEY           → _shared/evolution-api.ts
WHATSAPP_API_URL           → _shared/evolution-api.ts
WHATSAPP_INSTANCE_NAME     → _shared/evolution-api.ts
ML_APP_ID                  → _shared/ml-api-client.ts
ML_CLIENT_SECRET           → _shared/ml-api-client.ts
ML_REDIRECT_URI            → ml-oauth
LOVABLE_API_KEY            → 🗑️ zero refs ([[decisoes#ADR-002]])
```

## Deploy

Script atual: `scripts/deploy-functions.sh` cobre apenas **5 de 13 functions** (webhook-whatsapp, process-message, send-whatsapp, escalate, send-human-message) — todas com `--no-verify-jwt`. Restantes (ml-*, sync-*-embedding, process-correction-embedding, test-*) foram deployadas manualmente sem atualizar o script. Endereçado em [[debitos-tecnicos#B5]] achado #8.

## Observação global de segurança

**14/14 edge functions hoje têm `verify_jwt=false`.** Comentário no script: "for simplicity during development". O plano de remediação está em [[debitos-tecnicos#B1]] (passo 13): split explícito em INTERNAL (verify_jwt=true) vs EXTERNAL (verify_jwt=false).

## Evidência completa

- Lista deployed via Management API: `~/audit-canggu-forensics/RAW/A_supabase/24_edge_functions.json`
- Análise B2 do monorepo: `~/audit-canggu-forensics/RAW/B_monorepo/01_summary.md`
- Análise do ghost `test-search`: `~/audit-canggu-forensics/RAW/C_analysis/22_test_search_trace.md`
- Source baixado do ghost: `~/audit-canggu-forensics/RAW/C_analysis/test-search_source.ts`
