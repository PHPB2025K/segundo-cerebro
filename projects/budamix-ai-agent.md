---
title: "Budamix AI Agent (Ana)"
created: 2026-04-14
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/budamix-ai-agent/"
tags:
  - project
  - dev
  - whatsapp
  - atendimento
---

# Budamix AI Agent (Ana)

**Path:** `~/Documents/05-Projetos-Codigo/budamix-ai-agent/`
**Branch:** feat/fase4-ai-agent
**Stack:** Vite (React + Tailwind)
**Deploy:** Vercel
**CLAUDE.md:** sim
**Último commit:** 2 days ago — fix: PROIBIDO compartilhar WhatsApp/contatos externos no Mercado Livre

## O que é

Agente de atendimento ao cliente via WhatsApp (estilo SDR) para a marca Budamix. Assistente virtual "Ana" (renomeada de Giovana em 2026-04-02). Frontend em React para configuração e monitoramento. Arquitetura híbrida: N8N + Supabase Edge Functions (4 workflows, 4 Edge Functions, 9 tabelas).

## Decisões-chave

- [06/04] Pipeline vetorial: embedding pergunta → busca vetorial (pgvector) → SQL → contexto enriquecido
- [06/04] Bug envio WhatsApp humano→cliente CORRIGIDO
- [17/04] Ana restaurada após 8 dias de downtime — placeholders hardcoded (`SUPABASE_SERVICE_ROLE_KEY_PLACEHOLDER`, `WHATSAPP_API_KEY_PLACEHOLDER`) em 8 Code nodes do workflow `KE7YVXayl5ntjwQk` substituídos por chaves reais. Deploy de 12-13/04 reintroduziu o problema via import de workflow stub.
- [17/04] ML Questions workflow `g4JxNpC2sP9K8c71` destravado — 8 placeholders `YOUR_*` substituídos. Refresh OAuth ML automático via `marketplace_tokens` intacto.
- [17/04] Feedback loop ativo no WhatsApp — `search_corrections` RPC criada no Supabase, `process-message` integrado com as correções via `searchCorrections()` (threshold 0.85, bloco "CORREÇÕES APRENDIDAS" no prompt).
- [17/04] Trigger pg_net `trg_base_product_embedding_sync` criado — re-embedding automático de `base_products` para qualquer origem de UPDATE (não só Canggu UI).
- [17/04] Health Check refatorado com 4 checks reais (Supabase auth, Ana responsividade, Evolution state, erros do principal <30min). Alerta via WhatsApp para 5519993040768 (pessoal, não o da Ana).
- [17/04] N8N Credentials Opção A no workflow principal — `Process Message (AI)` usa credential httpHeaderAuth; 7 Code nodes + Send WhatsApp Response leem chaves de um único `Setup Credentials` node com guard clauses. SRK 9→1 ocorrências, WAK 2→1 no JSON.
- [17/04] `linkPreview: false` no Send WhatsApp Response — elimina bolha de loading que aparecia em msgs com URL.

## Pendências

- [ ] Fase 4 cleanup: remover campos antigos (marketplace_links, available_kits, price_marketplace)
- [ ] ~14 Session Extractors desabilitados (timeout 120s insuficiente, precisam 300s+)
- [ ] Opção B das Credentials: extrair os 7 Code nodes para uma Edge Function `ana-pipeline-step` que usa `Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')`. Elimina chave 100% do JSON do workflow. ~4-6h de refactor.

## Notas relacionadas

- [[automacoes/atendimento/system-prompt-atendimento]]
- [[automacoes/atendimento/prompt-pre-vendas]]
- [[projects/budamix-agent-architecture]]
- [[projects/budamix-agent-changelog-ana]]
- [[openclaw/agents/kobe/IDENTITY]]
- [[skills/whatsapp-ultimate/SKILL]]
- [[business/marketplaces/_index]]