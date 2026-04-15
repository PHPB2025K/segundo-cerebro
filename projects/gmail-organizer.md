---
title: "Gmail Organizer"
created: 2026-04-14
updated: 2026-04-15
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/GMAIL-ORGANIZER/"
tags:
  - project
  - dev
  - automacao
  - n8n
---

# Gmail Organizer

**Path:** `~/Documents/05-Projetos-Codigo/GMAIL-ORGANIZER/`
**Branch:** N/A (não é git repo)
**Stack:** N8N workflow + Google Apps Script + Gmail Filters XML
**Deploy:** N8N Cloud (trottingtuna-n8n.cloudfy.live)
**CLAUDE.md:** sim

## O que é

Sistema de organização automática do Gmail com 3 componentes complementares:

### 1. Google Apps Script (`OrganizarGmail.gs`)
- Categorização de emails via regex (6 categorias)
- Processamento em lote (200 emails/execução)
- Log automático em Google Sheets

### 2. Filtros Gmail nativos (`filtros-gmail.xml`)
- 34 filtros XML complementares ao script

### 3. Workflow N8N — Agente de Inbox
- **ID:** `VbmG1A62aighLsxL`
- **URL:** https://trottingtuna-n8n.cloudfy.live/workflow/VbmG1A62aighLsxL
- **Arquitetura:** Nate Herk — 22 nodes
- **Trigger:** Gmail (polls INBOX a cada minuto)
- **Classificador:** Claude Sonnet 4.6 — 9 categorias (Urgente, Contabilidade, Financeiro, Importação, Logística, Marketplaces, Pessoal, Trabalho, Promoções)
- **Resiliência:** todos os nodes "Modify Labels" têm `continueOnFail: true`
- **Notificações:** Slack (Urgente + Financeiro), Draft automático (LLM Chain)

### 4. Workflow relacionado: Inbox Zero Automatizado
- **ID:** `9CDYtQ5fOCONxhpY`
- **Status:** INATIVO

## Notas relacionadas

- [[projects/n8n-builder]] — infraestrutura N8N
- [[skills/n8n/n8n-mcp-tools-expert]] — MCP tools