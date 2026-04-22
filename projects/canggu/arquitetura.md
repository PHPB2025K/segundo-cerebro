---
tipo: referencia
projeto: Canggu
status: ativo
tags:
  - canggu
  - arquitetura
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Arquitetura

> Diagrama de pipeline + 5 fluxos end-to-end derivados da auditoria forense 2026-04-22.
> Evidência completa: `~/audit-canggu-forensics/RAW/C_analysis/24_call_graph.md`.

## Diagrama

```
                       ┌──────────────────────┐
                       │  Cliente WhatsApp    │
                       │  (texto, áudio,      │
                       │   imagens)           │
                       └──────────┬───────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │ Evolution API (Cloudfly)  │  ← trottingtuna-evolution.cloudfy.live
                    │ instance "BUDAMIX AI..."  │
                    └────────┬────────┬─────────┘
                             │        │
               ⚠️ REDUNDÂNCIA (resolvida em ADR-007)
                             │        │
           ┌─────────────────┘        └──────────────┐
           ▼                                         ▼
    ┌──────────────┐                       ┌──────────────────┐
    │ N8N workflow │                       │ edge function    │
    │ "Principal"  │  [em depreciação]     │ webhook-whatsapp │  ← canônico (ADR-007)
    │ (KE7YV...)   │                       │  (490 LOC)       │
    │ 17 nodes live│                       │                  │
    └──────┬───────┘                       └─────┬────────────┘
           │                                     │
           └────────────────┬────────────────────┘
                            ▼
             ┌────────────────────────────────┐
             │ edge function process-message  │  ← 630 LOC (+237 no dirty)
             │                                │
             │  1. classifyIntent — Haiku     │  ← Anthropic
             │  2. buildContext (paralelo):   │
             │     ├─ semantic search (vec)   │  ← OpenAI emb + pgvector
             │     ├─ history messages        │
             │     └─ policies/faqs           │
             │  3. checkEscalation            │
             │  4. [se não escala]            │
             │     generateResponse — Sonnet  │  ← Anthropic
             │  5. INSERT message sender=agent│
             └──────────────┬─────────────────┘
                            │
                            ▼
             ┌────────────────────────────────┐
             │ edge function send-whatsapp    │
             │  → Evolution API sendText      │
             └─────────────┬──────────────────┘
                           │
                           ▼
                   Cliente WhatsApp

    ════════════════ FLUXO SECUNDÁRIO (ML) ════════════════
    ML ─webhook─▶ ml-webhook ─▶ process-ml-question
                  (CORS*)    (Sonnet; searchProducts LEGACY — ver ADR-006)

    ═════════════ FLUXO ESCALONAMENTO (humano) ═════════════
    Dashboard ─fetch─▶ send-human-message ─▶ Evolution sendText
    (atendente)     (retorna success mesmo se envio falhou — achado #14)

    ═══════════════ TRIGGERS AUTOMÁTICOS ═══════════════════
    INSERT/UPDATE products       ─trigger─▶ notify_product_embedding
                                              (service_role HARDCODED — ADR-001)
                                              ─pg_net POST─▶
                                              sync-product-embedding
                                              ─OpenAI embed─▶ UPDATE embedding

    INSERT/UPDATE base_products  ─trigger─▶ notify_base_product_embedding
```

## Fluxo 24a — Cliente envia mensagem WhatsApp (texto)

Legenda: `[svc]` = usa service_role | `[noJWT]` = verify_jwt=false | `[CORS*]` = CORS wildcard | `[silencio]` = erro silenciado sem alerta.

**Pós-ADR-007** (edge function canônica, N8N depreciado):

1. Cliente WhatsApp envia texto
2. → Evolution Cloudfly
3. → `webhook-whatsapp/index.ts` (490 LOC) [CORS*] [noJWT hoje; ADR-B1 muda]
4. → parseWebhookPayload (extrai phone/content/messageType)
5. → Upsert customer + get_or_create conversation (janela 24h)
6. → INSERT messages sender=customer
7. → debounce 12s (aguarda bursts)
8. → checkBuffer (se chegou msg mais nova, descarta esta iteração)
9. → consolidateMessages (agrega pending)
10. → chama `/functions/v1/process-message` [svc]
11. → `process-message:142` classifyIntent() via Claude Haiku
12. → `process-message:181` buildContext() → embeddings.ts → searchProductsEnriched → OpenAI + RPC search_products_semantic em `base_products`
13. → `process-message:248` checkEscalation
14. → [se não escala] generateResponse() via Claude Sonnet [silencio — sem catch interno]
15. → INSERT messages sender=agent [svc]
16. → send-whatsapp → Evolution sendText
17. → Cliente

**Hoje** (antes de ADR-007 executado): existe branch paralelo em N8N workflow `KE7YVXayl5ntjwQk` (17 nodes live) que implementa o mesmo fluxo. Ver [[n8n-workflows]].

## Fluxo 24b — Cliente envia áudio

1. Cliente envia áudio OGG/Opus
2. → Evolution Cloudfly
3. → `webhook-whatsapp:49` parseWebhookPayload detecta `messageType='audio'`
4. → `webhook-whatsapp:83` handleAudioTranscription()
5. → evolution-api.ts getMediaBase64 [svc]
6. → groq-transcription.ts transcribeAudio(base64, mimetype) [silencio — catch em `:338` substitui por placeholder]
7. → Groq API `/audio/transcriptions` (whisper-large-v3, pt)
8. → retorna transcription text (ou placeholder `[Áudio recebido — transcrição indisponível...]` se falhou)
9. → fluxo continua como 24a a partir do passo 5

**Fragilidade:** se Groq cai, cliente recebe placeholder, operador não é avisado. Endereçado em [[debitos-tecnicos#B2]] achado #15.

## Fluxo 24c/24d — Auto-embedding de produtos

1. INSERT/UPDATE em `products` (ou `base_products`)
2. → trigger `trg_product_embedding_sync` (ou `trg_base_product_embedding_sync`)
3. → `notify_product_embedding()` (ou `notify_base_product_embedding()`) — SECURITY DEFINER
4. → `pg_net.http_post` [svc HARDCODED — ADR-001] [noJWT] → `/functions/v1/sync-product-embedding` (ou `-base-product-embedding`)
5. → sync-*-embedding recebe `{productId}` (ou `{baseProductId}`)
6. → SELECT produto [svc]
7. → OpenAI `text-embedding-3-small`
8. → UPDATE embedding [svc]

**Divergência detectada:** `buildSearchText` está duplicado — `sync-product-embedding` usa versão de `_shared/embeddings.ts`; `sync-base-product-embedding` redefine localmente com campos diferentes (color, capacity, tags, line). Risco de drift. Ver [[debitos-tecnicos]] achado #13.

## Fluxo 24e — Atendente humano responde via frontend

1. Frontend `ConversationDetailPage` — atendente digita
2. → `fetch POST /functions/v1/send-human-message` (JWT do usuário) [CORS*]
3. → send-human-message `:52` SELECT conversation + customers [svc]
4. → `:71` verifica assigned_to !== 'agent' (403 se ainda no bot)
5. → INSERT messages sender=human_agent [svc]
6. → Evolution setPresence (typing)
7. → Evolution sendText [silencio parcial em `:105`]
8. → Cliente

**Bug:** catch em `:105` loga erro mas retorna `{success: true, sent: false}` — frontend pensa que enviou. Achado #14, endereçado em [[debitos-tecnicos#B3]].

## Evidência completa

Arquivos RAW da auditoria forense:
- `~/audit-canggu-forensics/RAW/C_analysis/24_call_graph.md` — 5 call graphs detalhados
- `~/audit-canggu-forensics/RAW/C_analysis/26_breakpoints.md` — SPOFs por componente
- `~/audit-canggu-forensics/AUDIT_REPORT.md` §3 (arquitetura) e §5 (achados)
