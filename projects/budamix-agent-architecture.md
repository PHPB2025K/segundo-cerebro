---
title: "budamix agent architecture"
created: 2026-04-14
type: project
status: active
tags:
  - project
---

# Architecture — Budamix AI Agent

## Pipeline de Mensagem (fluxo completo)

```
Cliente envia msg WhatsApp
  → Evolution API v2 (BUDAMIX AI AGENT instance)
    → Webhook POST para Supabase Edge Function
      → webhook-whatsapp/index.ts
        1. parseWebhookPayload() — normaliza evento, extrai phone/name/content
        2. Upsert customer (cria se novo)
        3. Upsert conversation (cria ou reutiliza ativa)
        4. Salva mensagem no DB
        5. Debounce check (8s buffer para msgs consecutivas)
        6. Fire-and-forget → process-message
      → process-message/index.ts
        1. Verifica conversation.assigned_to === 'agent'
        2. Carrega config (getConfig com cache 5min)
        3. Busca customer phone
        4. Check working hours → away message se fora
        5. Typing indicator (setPresence)
        6. buildContext() — 6 queries paralelas:
           - Últimas 20 msgs do histórico
           - Dados do customer
           - Políticas ativas
           - FAQs relevantes (keyword overlap)
           - Produtos (busca semântica pgvector)
           - Message count (para escalação)
        7. classifyIntent() — Claude Haiku
        8. checkEscalation() — 4 regras
        9. generateResponse() — Claude Sonnet
       10. validateResponse() — chunks, duplicatas, formatação
       11. Salva resposta no DB
       12. sendText() via Evolution API
       13. Atualiza conversation (category, sentiment)
```

## Edge Functions (deployadas)

| Function | Rota | JWT | Descrição |
|----------|------|-----|-----------|
| webhook-whatsapp | POST /functions/v1/webhook-whatsapp | no-verify | Entrada de msgs WhatsApp (legado, N8N substitui) |
| process-message | POST /functions/v1/process-message | no-verify | Pipeline IA completo (consulta correções desde 17/04) |
| send-whatsapp | POST /functions/v1/send-whatsapp | no-verify | Envio via Evolution API (legado) |
| send-human-message | POST /functions/v1/send-human-message | no-verify | Msgs do dashboard Canggu |
| escalate | POST /functions/v1/escalate | no-verify | Escalação para humano |
| sync-product-embedding | POST /functions/v1/sync-product-embedding | no-verify | Re-embedding de `products` (legado, disparado por trigger) |
| sync-base-product-embedding | POST /functions/v1/sync-base-product-embedding | no-verify | Re-embedding de `base_products` — aceita `{baseProductId}` targeted (desde 17/04) OU batch `embedding IS NULL` |
| process-correction-embedding | POST /functions/v1/process-correction-embedding | no-verify | Gera embedding para `response_corrections` após insert |
| process-ml-question | POST /functions/v1/process-ml-question | no-verify | Pipeline IA p/ perguntas ML (consulta correções) |

## Shared Modules (12 arquivos em _shared/)

| Arquivo | Linhas | Função |
|---------|--------|--------|
| types.ts | 457 | Tipos TypeScript |
| evolution-api.ts | 201 | Evolution API (send, parse, presence) |
| response-generator.ts | 178 | Gera resposta Claude Sonnet |
| response-validator.ts | 162 | Valida chunks/formato |
| embeddings.ts | 159 | OpenAI embeddings + pgvector search |
| context-builder.ts | 153 | Monta contexto (6 queries paralelas) |
| intent-classifier.ts | 144 | Classificação Claude Haiku |
| config.ts | 122 | Config loader com cache 5min |
| groq-transcription.ts | 64 | Transcrição áudio Groq/Whisper |
| anthropic.ts | 59 | Wrapper API Anthropic |
| cors.ts | 32 | CORS headers |
| supabase-client.ts | 16 | Cliente Supabase service role |

## Frontend (src/)

### Stack
- React 19 + TypeScript 5.7 + Vite 6
- TailwindCSS 4 + Shadcn/UI (Radix)
- Zustand 5 (state) + React Router 7
- Recharts (gráficos) + date-fns
- Supabase Realtime (WebSocket)

### Páginas (13)
- /login — Autenticação Supabase Auth
- /dashboard — KPIs, gráficos, alertas
- /conversations — Lista + ChatView
- /conversations/:id — Detalhe conversa
- /products — Catálogo CRUD
- /products/:id — Edição produto
- /customers — Lista clientes
- /customers/:id — Perfil cliente
- /policies — Editor políticas + FAQ
- /escalations — Fila de escalonamentos
- /analytics — Métricas detalhadas
- /settings — Configuração do agente

### Componentes (39), Hooks (8), Stores (4)

## Database (9 tabelas)

| Tabela | RLS | Realtime | Descrição |
|--------|-----|----------|-----------|
| customers | ✓ | ✓ | Clientes (phone, name, tags) |
| conversations | ✓ | ✓ | Conversas (status, category, sentiment) |
| messages | ✓ | ✓ | Mensagens (sender, content, tokens) |
| escalations | ✓ | ✓ | Escalonamentos (reason, urgency) |
| products | ✓ | ✗ | Catálogo (10 produtos, com embeddings) |
| policies | ✓ | ✗ | Políticas (troca, frete, garantia) |
| faq | ✓ | ✗ | Perguntas frequentes |
| agent_config | ✓ | ✗ | 15 configs (prompt, modelo, limites) |
| analytics_daily | ✓ | ✗ | Métricas diárias agregadas |

### Extensões
- pgvector 0.8.0 (busca semântica)
- pg_net (HTTP calls from triggers)
- Colunas extras em products/base_products/response_corrections: `embedding` (vector 1536)
- Funções SQL:
  - `match_products(query_embedding, match_threshold, match_count)` — busca em `products`
  - `search_products_semantic(query_embedding, match_threshold, match_count)` — busca em `base_products` (Fase 5)
  - `search_corrections(query_embedding, match_threshold, match_count)` — busca em `response_corrections` (criada 17/04 via migration `20260417120100`)
- Triggers pg_net:
  - `trg_product_embedding_sync` — `products` UPDATE dispara `sync-product-embedding`
  - `trg_base_product_embedding_sync` — `base_products` UPDATE dispara `sync-base-product-embedding` com `{baseProductId}` (criado 17/04 via migration `20260417120000`)

## Deployment

```bash
# Deploy single function
SUPABASE_ACCESS_TOKEN=sbp_ea6e04da6df4f425df7e642e16bb7dec7f0609fe \
  npx supabase functions deploy <nome> --no-verify-jwt \
  --project-ref jpacmloqsfiebvagfomt

# Deploy all functions
for fn in webhook-whatsapp process-message send-whatsapp send-human-message escalate sync-product-embedding; do
  SUPABASE_ACCESS_TOKEN=sbp_ea6e04da6df4f425df7e642e16bb7dec7f0609fe \
    npx supabase functions deploy $fn --no-verify-jwt \
    --project-ref jpacmloqsfiebvagfomt
done

# DB query
curl -s -X POST "https://api.supabase.com/v1/projects/jpacmloqsfiebvagfomt/database/query" \
  -H "Authorization: Bearer sbp_ea6e04da6df4f425df7e642e16bb7dec7f0609fe" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT ..."}'
```

## Evolution API
- URL: configurada via secret `WHATSAPP_API_URL`
- Instance: `BUDAMIX AI AGENT` (spaces — URL encoded em evolution-api.ts)
- API Key: secret `WHATSAPP_API_KEY`
- Webhook event: `MESSAGES_UPSERT` (uppercase — normalizado para case-insensitive)
- Suporta: @s.whatsapp.net, @g.us, @lid (WhatsApp moderno)

## N8N Workflows

| Workflow | ID | Status | Descrição |
|----------|----|--------|-----------|
| Budamix WhatsApp Agent (Principal) | `KE7YVXayl5ntjwQk` | active | Pipeline WhatsApp. 17 nodes (pós-refactor 17/04). Credential `Budamix Supabase (Ana)` no HTTP node `Process Message (AI)`. Setup Credentials + guard clauses nos 7 Code nodes. |
| Budamix WhatsApp Health Check (15min) | `DEjLkJcllQEmrcLF` | active | 4 checks reais desde 17/04 (Supabase auth, Ana responsividade, Evolution state, erros <30min). Alerta WhatsApp para 5519993040768 (pessoal). |
| Budamix ML Questions (Polling 2min) | `g4JxNpC2sP9K8c71` | active | Restaurado em 17/04 após fix de placeholders. |
| Budamix ML Messages (Polling 1min) | `sg2yU46R9EQq3a2v` | active | Fonte canônica de credenciais OAuth ML (client_id, client_secret). |
| Budamix Relatório Diário | `g7HBVeBRGPA29goW` | inactive | Cron 21h (desativado). |

### Padrão "Setup Credentials" (desde 17/04)
Primeiro Code node do workflow (`Setup Credentials`) exporta constantes via `$json`:
```js
const SUPABASE_URL = 'https://jpacmloqsfiebvagfomt.supabase.co';
const SRK          = '<service_role_key>';
const EVO_URL      = 'https://trottingtuna-evolution.cloudfy.live';
const EVO_KEY      = '<evolution_api_key>';
const INSTANCE     = 'BUDAMIX AI AGENT';
return [{ json: { ...$input.first().json, SUPABASE_URL, SRK, EVO_URL, EVO_KEY, INSTANCE } }];
```

Downstream Code nodes consomem via `$('Setup Credentials').item.json.*` com guard clause obrigatório:
```js
const cfg = $('Setup Credentials').item.json;
const serviceKey = cfg.SRK;
if (!serviceKey || /PLACEHOLDER|YOUR_|FAKE/i.test(serviceKey)) {
  throw new Error('[GUARD] SRK inválida — verificar Setup Credentials');
}
```

**Motivação:** evitar nova cascata como os 8 dias de downtime 09-17/04 onde placeholders re-importados derrubaram todo o workflow silenciosamente.

## Notas relacionadas

- [[projects/budamix-ai-agent]]
