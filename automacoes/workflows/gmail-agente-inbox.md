---
title: "Workflow N8N — Agente de Inbox Gmail"
type: workflow
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - automacao
  - workflow
  - n8n
  - gmail
---

# Workflow N8N — Agente de Inbox Gmail

| Campo | Valor |
|-------|-------|
| **ID** | `VbmG1A62aighLsxL` |
| **URL** | https://trottingtuna-n8n.cloudfy.live/workflow/VbmG1A62aighLsxL |
| **Trigger** | Gmail polling (1 minuto) |
| **Nodes** | 22 |
| **Modelo AI** | Claude Sonnet 4.6 |
| **Status** | ✅ Ativo |

## O que faz

Categoriza automaticamente emails recebidos em 9 categorias usando Claude AI como classificador. Aplica labels do Gmail, envia alertas no Slack para emails urgentes e financeiros, e gera rascunhos de resposta automáticos via LLM Chain.

## Categorias

1. Urgente
2. Contabilidade
3. Financeiro
4. Importação
5. Logística Nacional
6. Marketplaces
7. Pessoal
8. Trabalho/Operacional
9. Promoções

## Credenciais

| Credencial | ID |
|------------|-----|
| Gmail OAuth2 | `OZ2LN81GgKHXsf6c` |
| Anthropic API | `EF7hcx5rtf0veSNH` |

## Resiliência

- Todos os nodes "Modify Labels" têm `continueOnFail: true`
- Notificações Slack para Urgente + Financeiro

## Workflow Relacionado

- **Inbox Zero Automatizado** — ID: `9CDYtQ5fOCONxhpY` — Status: INATIVO

## Notas relacionadas

- [[projects/gmail-organizer]] — ficha do projeto
- [[projects/n8n-builder]] — infraestrutura N8N
