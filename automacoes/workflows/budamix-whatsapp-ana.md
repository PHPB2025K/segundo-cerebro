---
title: "Workflow N8N — Budamix AI Agent (Ana)"
type: workflow
created: 2026-04-15
updated: 2026-04-15
status: development
tags:
  - automacao
  - workflow
  - n8n
  - whatsapp
  - atendimento
---

# Workflow N8N — Budamix AI Agent (Ana)

| Campo | Valor |
|-------|-------|
| **ID** | Em desenvolvimento (workflow-principal.json) |
| **URL** | — (não deployado no N8N ainda) |
| **Trigger** | Webhook POST /budamix-whatsapp |
| **Nodes** | 16 |
| **Modelo AI** | Claude AI |
| **Status** | 🟡 Desenvolvimento |

## O que faz

Agente de atendimento WhatsApp "Ana" para a marca Budamix. Recebe mensagens via Evolution API v2, gerencia perfil do cliente (upsert), cria/recupera conversas (janela 24h), salva histórico, e responde via Claude AI ou rota para atendimento humano.

## Pipeline (16 nodes)

1. Webhook recebe mensagem (Evolution API v2)
2. Parse message (extrai texto, mídia, sender)
3. Upsert customer (Supabase — customers)
4. Get/create conversation (janela 24h)
5. Save incoming message (messages)
6. Route: AI ou humano?
7. Build context (histórico + produto + FAQ)
8. Claude API — gerar resposta
9. Save AI response (messages)
10. Send via Evolution API (WhatsApp)
11-16. Error handling, logging, notifications

## Integrações

| Serviço | Detalhes |
|---------|----------|
| Evolution API v2 | WhatsApp envio/recebimento |
| Supabase | `jpacmloqsfiebvagfomt` — customers, conversations, messages |
| Claude AI | Resposta conversacional |

## Workflows Auxiliares

| Workflow | Trigger | O que faz |
|----------|---------|-----------|
| ML messages polling | 1 min | Busca mensagens do Mercado Livre |
| ML questions polling | 2 min | Busca perguntas do ML |
| Health check | 15 min | Verifica status das integrações |
| Daily report | Diário | Gera relatório de conversas do dia |

## Notas relacionadas

- [[projects/budamix-ai-agent]] — ficha do projeto
- [[projects/whatsapp-api]] — infraestrutura WhatsApp
