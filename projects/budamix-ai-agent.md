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

## Pendências

- [ ] Fase 4 cleanup: remover campos antigos (marketplace_links, available_kits, price_marketplace)
- [ ] ~14 Session Extractors desabilitados (timeout 120s insuficiente, precisam 300s+)

## Notas relacionadas

- [[automacoes/atendimento/system-prompt-atendimento]]
- [[automacoes/atendimento/prompt-pre-vendas]]
- [[projects/budamix-agent-architecture]]
- [[projects/budamix-agent-changelog-ana]]
- [[openclaw/agents/kobe/IDENTITY]]
- [[skills/whatsapp-ultimate/SKILL]]
- [[business/marketplaces/_index]]