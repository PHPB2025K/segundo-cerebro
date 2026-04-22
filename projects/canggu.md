---
title: "Canggu"
created: 2026-04-22
updated: 2026-04-22
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/budamix-ai-agent/"
tags:
  - project
  - dev
  - microsaas
  - whatsapp
  - atendimento
  - canggu
---

# Canggu

Agente de IA para atendimento ao cliente via WhatsApp, com módulo específico para marketplaces (ML, Shopee, Amazon). MicroSaaS que pode ser personalizado para qualquer empresa — a IA responde perguntas e chats conforme os cadastros e informações alimentadas no sistema.

## Identidade

| | |
|---|---|
| **Produto** | Canggu (MicroSaaS) |
| **Instância atual** | "Ana" — operando no WhatsApp da Budamix como primeiro cliente/validação |
| **Status comercial** | Em teste interno na GB; ainda não aberto para test users externos |
| **Último rename** | "Giovana" → "Ana" em 2026-04-02 |

Ana é a identidade visível ao cliente final; o sistema por trás é o Canggu.

## Stack & Infra

- **Frontend:** Vite (React 19 + TypeScript 5.7 + TailwindCSS 4 + Shadcn/UI)
- **State:** Zustand 5, React Router 7, Recharts, Supabase Realtime
- **Backend:** Supabase Edge Functions (Deno) + N8N
- **Supabase:** `jpacmloqsfiebvagfomt` (nome oficial: `budamix-ai-agent`)
- **Deploy frontend:** Vercel
- **WhatsApp:** Evolution API v2, instance `BUDAMIX AI AGENT`
- **LLMs:** Claude Haiku (classificação), Claude Sonnet (resposta), OpenAI text-embedding-3-small (pgvector 1536d), Groq/Whisper (áudio)
- **Path local:** `~/Documents/05-Projetos-Codigo/budamix-ai-agent/`
- **Branch ativa:** `feat/fase4-ai-agent`

## Arquitetura — Pipeline de Mensagem

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

## Edge Functions (9 deployadas)

| Function | Rota | JWT | Descrição |
|---|---|---|---|
| webhook-whatsapp | POST /functions/v1/webhook-whatsapp | no-verify | Entrada de msgs WhatsApp (legado, N8N substitui) |
| process-message | POST /functions/v1/process-message | no-verify | Pipeline IA completo (consulta correções desde 17/04) |
| send-whatsapp | POST /functions/v1/send-whatsapp | no-verify | Envio via Evolution API (legado) |
| send-human-message | POST /functions/v1/send-human-message | no-verify | Msgs do dashboard Budamix Central |
| escalate | POST /functions/v1/escalate | no-verify | Escalação para humano |
| sync-product-embedding | POST /functions/v1/sync-product-embedding | no-verify | Re-embedding de `products` (legado, disparado por trigger) |
| sync-base-product-embedding | POST /functions/v1/sync-base-product-embedding | no-verify | Re-embedding de `base_products` — aceita `{baseProductId}` targeted (desde 17/04) OU batch `embedding IS NULL` |
| process-correction-embedding | POST /functions/v1/process-correction-embedding | no-verify | Gera embedding para `response_corrections` após insert |
| process-ml-question | POST /functions/v1/process-ml-question | no-verify | Pipeline IA p/ perguntas ML (consulta correções) |

## Shared Modules (12 arquivos em `_shared/`)

| Arquivo | Linhas | Função |
|---|---:|---|
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

## Database (9 tabelas)

| Tabela | RLS | Realtime | Descrição |
|---|:---:|:---:|---|
| customers | ✓ | ✓ | Clientes (phone, name, tags) |
| conversations | ✓ | ✓ | Conversas (status, category, sentiment) |
| messages | ✓ | ✓ | Mensagens (sender, content, tokens) |
| escalations | ✓ | ✓ | Escalonamentos (reason, urgency) |
| products | ✓ | ✗ | Catálogo (10 produtos, com embeddings) |
| policies | ✓ | ✗ | Políticas (troca, frete, garantia) |
| faq | ✓ | ✗ | Perguntas frequentes |
| agent_config | ✓ | ✗ | 15 configs (prompt, modelo, limites) |
| analytics_daily | ✓ | ✗ | Métricas diárias agregadas |

### Extensões e funções

- **pgvector 0.8.0** (busca semântica)
- **pg_net** (HTTP calls from triggers)
- Colunas `embedding` (vector 1536) em `products`, `base_products`, `response_corrections`
- **Funções SQL:**
  - `match_products(query_embedding, match_threshold, match_count)` — busca em `products`
  - `search_products_semantic(query_embedding, match_threshold, match_count)` — busca em `base_products` (Fase 5)
  - `search_corrections(query_embedding, match_threshold, match_count)` — busca em `response_corrections` (migration `20260417120100`)
- **Triggers pg_net:**
  - `trg_product_embedding_sync` — `products` UPDATE dispara `sync-product-embedding`
  - `trg_base_product_embedding_sync` — `base_products` UPDATE dispara `sync-base-product-embedding` com `{baseProductId}` (migration `20260417120000`)

## Frontend — Admin UI

### Páginas (13)

- `/login` — Supabase Auth
- `/dashboard` — KPIs, gráficos, alertas
- `/conversations` — Lista + ChatView
- `/conversations/:id` — Detalhe
- `/products` — Catálogo CRUD
- `/products/:id` — Edição
- `/customers` — Lista
- `/customers/:id` — Perfil
- `/policies` — Editor políticas + FAQ
- `/escalations` — Fila
- `/analytics` — Métricas
- `/settings` — Configuração do agente

Componentes: 39 | Hooks: 8 | Stores: 4

## Integração N8N

| Workflow | ID | Status | Descrição |
|---|---|---|---|
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

## Evolution API

- **URL:** configurada via secret `WHATSAPP_API_URL`
- **Instance:** `BUDAMIX AI AGENT` (spaces — URL encoded em evolution-api.ts)
- **API Key:** secret `WHATSAPP_API_KEY`
- **Webhook event:** `MESSAGES_UPSERT` (uppercase — normalizado para case-insensitive)
- **Suporta:** @s.whatsapp.net, @g.us, @lid

## Deployment

```bash
# Deploy single function
SUPABASE_ACCESS_TOKEN=<token> \
  npx supabase functions deploy <nome> --no-verify-jwt \
  --project-ref jpacmloqsfiebvagfomt

# Deploy all functions
for fn in webhook-whatsapp process-message send-whatsapp send-human-message escalate sync-product-embedding; do
  SUPABASE_ACCESS_TOKEN=<token> \
    npx supabase functions deploy $fn --no-verify-jwt \
    --project-ref jpacmloqsfiebvagfomt
done

# DB query via Management API
curl -s -X POST "https://api.supabase.com/v1/projects/jpacmloqsfiebvagfomt/database/query" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT ..."}'
```

## Decisões-chave

- [06/04] Pipeline vetorial: embedding pergunta → busca vetorial (pgvector) → SQL → contexto enriquecido
- [06/04] Bug envio WhatsApp humano→cliente CORRIGIDO (feature do dashboard Budamix Central)
- [17/04] Ana restaurada após 8 dias de downtime — placeholders hardcoded (`SUPABASE_SERVICE_ROLE_KEY_PLACEHOLDER`, `WHATSAPP_API_KEY_PLACEHOLDER`) em 8 Code nodes do workflow `KE7YVXayl5ntjwQk` substituídos por chaves reais. Deploy de 12-13/04 reintroduziu o problema via import de workflow stub.
- [17/04] ML Questions workflow `g4JxNpC2sP9K8c71` destravado — 8 placeholders `YOUR_*` substituídos. Refresh OAuth ML automático via `marketplace_tokens` intacto.
- [17/04] Feedback loop ativo no WhatsApp — `search_corrections` RPC criada no Supabase, `process-message` integrado com as correções via `searchCorrections()` (threshold 0.85, bloco "CORREÇÕES APRENDIDAS" no prompt).
- [17/04] Trigger pg_net `trg_base_product_embedding_sync` criado — re-embedding automático de `base_products` para qualquer origem de UPDATE (não só UI do Budamix Central).
- [17/04] Health Check refatorado com 4 checks reais (Supabase auth, Ana responsividade, Evolution state, erros do principal <30min). Alerta via WhatsApp para 5519993040768 (pessoal, não o da Ana).
- [17/04] N8N Credentials Opção A no workflow principal — `Process Message (AI)` usa credential httpHeaderAuth; 7 Code nodes + Send WhatsApp Response leem chaves de um único `Setup Credentials` node com guard clauses. SRK 9→1 ocorrências, WAK 2→1 no JSON.
- [17/04] `linkPreview: false` no Send WhatsApp Response — elimina bolha de loading que aparecia em msgs com URL.
- [17/04] Auditoria 48 threads / 151 respostas concluída — 60% ✅ / 18% ⚠️ / 18% ❌ / 4% 🔄. 4/5 padrões top já corrigidos pelos fixes de 04/04 + 12/04. Único residual: loop de qualificação de canal (Rec 4.1). Artefato: `auditoria-ana-whatsapp-abril2026.md` na raiz do projeto.

## Pendências

- [ ] Fase 4 cleanup (lado Budamix Central): remover campos antigos (marketplace_links, available_kits, price_marketplace)
- [ ] ~14 Session Extractors desabilitados (timeout 120s insuficiente, precisam 300s+)
- [ ] Opção B das Credentials: extrair os 7 Code nodes para uma Edge Function `ana-pipeline-step` que usa `Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')`. Elimina chave 100% do JSON do workflow. ~4-6h de refactor.
- [ ] Aplicar **Rec 4.1** da auditoria — regra ANTI-LOOP DE CANAL no Passo 4a do BLOCO 4 do `system_prompt` (bloqueia repetir pergunta "site/ML/Shopee?" quando cliente já respondeu).
- [ ] Próxima auditoria programada (meta erro <20%).
- [ ] Validação externa — abrir para test users após estabilidade confirmada na GB.

## Notas relacionadas

- [[projects/budamix-agent-changelog-ana]]
- [[projects/whatsapp-api]]
- [[openclaw/agents/kobe/IDENTITY]]
- [[skills/whatsapp-ultimate/SKILL]]
- [[business/marketplaces/_index]]
- [[projects/budamix-central]] — dashboard interno que compartilha camada de produtos e pgvector
