---
title: "budamix agent changelog ana"
created: 2026-04-14
type: project
status: active
tags:
  - project
---

# CHANGELOG — Agente Ana (WhatsApp)

## 2026-04-12 — Sprint Auditoria 7d (5 correções sistêmicas)

**Contexto:** Auditoria de 113 mensagens (06-09/abr) revelou taxa de erro de 61%.
3 problemas CRÍTICOS + 4 ALTOS + 2 MÉDIOS + 1 BAIXO.

### Problemas corrigidos: 10/10 da auditoria

| # | Problema | Severidade | Status |
|---|---------|-----------|--------|
| 1 | Loop perguntas repetitivas (Ellen Joyce) | CRITICO | CORRIGIDO |
| 2 | Vazamento "Nenhum produto foi carregado" | CRITICO | CORRIGIDO |
| 3 | Promessas indevidas (Edneuda — troca/reembolso) | CRITICO | CORRIGIDO |
| 4 | Reclamação sem escalação real | ALTO | CORRIGIDO |
| 5 | Loop mensagem vazia (7 tentativas) | ALTO | CORRIGIDO |
| 6 | Áudio não transcrito | ALTO | CORRIGIDO |
| 7 | Cupom BEMVINDO10 para cliente existente | MEDIO | CORRIGIDO |
| 8 | Resposta duplicada (debounce) | MEDIO | CORRIGIDO |
| 9 | "Fita" não abordada (produto fora catálogo) | BAIXO | CORRIGIDO |
| 10 | Produtos nunca carregados (pipeline) | ALTO | CORRIGIDO |

### Arquivos modificados

| Arquivo | Tipo de mudança |
|---------|----------------|
| `supabase/functions/_shared/context-builder.ts` | Carry-over 0.2, regex expandido, fallback legacy |
| `supabase/functions/_shared/response-generator.ts` | Instrução no-products, regra reativa anti-loop |
| `supabase/functions/_shared/response-validator.ts` | 6 novos patterns anti-vazamento |
| `supabase/functions/process-message/index.ts` | Anti-loop, post-response escalation, áudio fallback |
| `n8n/workflow-principal.json` | Debounce 8s → 12s |
| `CLAUDE.md` | Seção 31 documentando todas as correções |
| `agent_config (Supabase DB)` | Regras 16-18 no prompt, debounce 12s |

### Deploy — EXECUTADO 2026-04-13 01:02 UTC

| Componente | Status | Timestamp |
|-----------|--------|-----------|
| `process-message` (Edge Function) | ACTIVE | 2026-04-13 01:02:14 UTC |
| N8N Workflow Principal (KE7YVXayl5ntjwQk) | ACTIVE, debounce=12s | 2026-04-13 01:03:12 UTC |
| `agent_config` (DB) | Regras 16-18 + debounce 12s | 2026-04-12 (sessão anterior) |

### Smoke Tests — 4/4 PASSED

| # | Teste | Resultado |
|---|-------|----------|
| 1 | Busca "potes herméticos" | Resposta com "potes de vidro hermético", sem vazamento |
| 2 | Carry-over "Sim, quero ver os kits" | Ana reconheceu contexto de potes/kits |
| 3 | Anti-vazamento "Ambos" | 3 produtos reais com preços (Kit 5 Potes R$24,90), ZERO debug |
| 4 | Escalação "tampa com borracha diferente" | Ana respondeu sem promessas proibidas, `escalated=true`, registro criado em `escalations` |

### Monitoramento pós-deploy

- Verificar busca semântica: "potes herméticos" deve retornar 5+ produtos
- Verificar escalação: reclamação com nro pedido → `escalations` deve ter registro
- Verificar anti-loop: 2+ "[Mensagem sem texto]" → auto-escalação
- Verificar áudio: arquivo .ogg deve ser transcrito via Groq
- **Próxima auditoria: 19/abr/2026** — meta: taxa de erro < 20%

## 2026-04-17 — Incident Response (8 dias downtime) + Feedback Loop + Credentials Refactor

### Sintoma
Ana não respondia no WhatsApp desde **09/04 19:31 BRT** (última mensagem bem-sucedida — customer "Sim" + agent resposta 15s depois). **8 dias, 0 respostas.** Evolution Cloudfly com `state=open` (falso positivo do health check antigo).

### Causa raiz
Deploy de 12/04 22:03 BRT (Sprint Auditoria 7d) re-importou o workflow `KE7YVXayl5ntjwQk` com **placeholders literais** em 8 de 16 Code nodes: 7x `SUPABASE_SERVICE_ROLE_KEY_PLACEHOLDER` + 2x `WHATSAPP_API_KEY_PLACEHOLDER`. Primeiro node na cadeia (`Upsert Customer`) fazia `axios.get(/rest/v1/customers, {apikey: 'SUPABASE_SERVICE_ROLE_KEY_PLACEHOLDER'})` → PostgREST 401 → execução morria antes de Save Message. 20+ execuções visíveis na API do N8N com `status=error` em `Upsert Customer`.

### 7 fixes executados em sequência

| # | Fix | Arquivos/componentes | Timestamp |
|---|-----|----------------------|-----------|
| 1 | **Ana placeholders substituídos** | 8 Code nodes do `KE7YVXayl5ntjwQk` via `PUT /api/v1/workflows/:id` | 17/04 09:48 UTC |
| 2 | **ML Questions placeholders** | 4 nodes do `g4JxNpC2sP9K8c71` (`YOUR_SUPABASE_SERVICE_ROLE_KEY` x4, `YOUR_ML_APP_ID` x2, `YOUR_ML_CLIENT_SECRET` x2) | 17/04 10:00 UTC |
| 3 | **`linkPreview: false`** | Send WhatsApp Response — 2 `axios.post('/message/sendText/')` | 17/04 10:22 UTC |
| 4 | **Health Check refatorado** | `DEjLkJcllQEmrcLF` reescrito: 11 nodes → 2. 4 checks reais (Supabase auth, Ana 2h+ sem responder, Evolution state, erros principal <30min). Alerta via WhatsApp **5519993040768 (pessoal do Pedro, não a Ana)**. Dedup 30min. | 17/04 10:12 UTC |
| 5 | **RPC `search_corrections`** | Migration `20260417120100_search_corrections_function.sql` — função `search_corrections(vector(1536), float, int)` | 17/04 10:35 UTC |
| 6 | **Feedback loop no WhatsApp** | `_shared/embeddings.ts` novo `searchCorrections()`; `_shared/context-builder.ts` chama threshold 0.85; `_shared/response-generator.ts` injeta bloco "CORREÇÕES APRENDIDAS"; `ContextBundle.relevantCorrections` em `_shared/types.ts`; deploy de `process-message` | 17/04 10:45 UTC |
| 7 | **Trigger re-embedding `base_products`** | Migration `20260417120000_auto_embed_trigger_base_products.sql` — `trg_base_product_embedding_sync` via pg_net. Edge Function `sync-base-product-embedding` estendida: aceita `{baseProductId}` targeted (além do batch `embedding IS NULL`) | 17/04 10:40 UTC |
| 8 | **N8N Credentials Opção A** | `KE7YVXayl5ntjwQk` refatorado: credential `Budamix Supabase (Ana)` (id `Yc25vX9mtZ8oM018`, httpHeaderAuth) no `Process Message (AI)` HTTP node; novo node `Setup Credentials` centraliza as 5 chaves; 7 Code nodes + Send WhatsApp Response leem via `$('Setup Credentials').item.json.*` + guard `[GUARD]`. SRK 9→1 ocorrências, WAK 2→1. | 17/04 11:39 UTC |

### Validações
- Ana restaurada: execução 93145 success, Ana respondeu "potes herméticos de vidro borossilicato" em 9.2s / 12.586 tokens.
- ML Questions: execução 93166 success.
- Health Check: happy path `alert_sent=false`; failure simulada (SRK=FAKE) → `alert_sent=true`, mensagem chegou no 5519993040768.
- Feedback loop: "Voces tem o pote 1050ml na cor branca?" → Ana responde "disponível apenas na tampa azul-petróleo — não temos a versão branca" (conteúdo literal da correção cadastrada).
- Re-embedding: UPDATE em `description_short` do YW640 muda embedding hash em 3s.
- Credentials: 9 guard clauses ativas, SRK=1 ocorrência no JSON, smoke test da pipeline toda OK (400 final era destinatário fictício, não credential).

### Backups criados
- `~/budamix-wf-backup-20260417-0647.json` (workflow pré-fix Ana)
- `~/budamix-ml-questions-backup-20260417-0700.json` (pré-fix ML Questions)
- `~/budamix-wf-pre-linkpreview-20260417-0722.json` (pré-linkPreview)
- `~/budamix-healthcheck-backup-20260417-0705.json` (pré-refactor health check)
- `~/budamix-wf-pre-credentials-20260417-0837.json` (pré-Opção A credentials)

### Pendências pós-incident
- **Opção B das Credentials**: extrair os 7 Code nodes do workflow principal para uma Edge Function `ana-pipeline-step` que usa `Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')`. Tira 100% a chave do JSON do workflow. ~4-6h. Pendência registrada em [[memory/context/pendencias|pendencias]].
- Monitorar Health Check por 7 dias — confirmar que `alert_sent=false` permanece com pipeline saudável e que as 4 checks disparam adequadamente em falhas reais.

## Notas relacionadas

- [[projects/budamix-ai-agent]]
