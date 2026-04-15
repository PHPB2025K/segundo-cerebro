---
title: "Workflow N8N — Estoque PDF Parser"
type: workflow
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - automacao
  - workflow
  - n8n
  - estoque
---

# Workflow N8N — Estoque PDF Parser

| Campo | Valor |
|-------|-------|
| **ID** | `WyxKDxwIkuuL8BdH` |
| **URL** | https://trottingtuna-n8n.cloudfy.live/workflow/WyxKDxwIkuuL8BdH |
| **Trigger** | Webhook POST /estoque-upload |
| **Nodes** | 4 |
| **Status** | ✅ Ativo |

## O que faz

Parseia PDFs de notas fiscais de entrada de mercadoria. Extrai dados do fornecedor, número/data da nota, códigos de produto, quantidades e preços unitários. Converte formato numérico brasileiro (1.234,56 → 1234.56) e insere no Supabase.

## Pipeline (4 nodes)

1. **Webhook** — recebe upload do PDF
2. **Extract text** — extrai texto do PDF
3. **Code** — regex parsing, conversão de formato numérico BR, validação
4. **Supabase** — insert na tabela de estoque

## Integrações

| Serviço | Detalhes |
|---------|----------|
| Supabase | `sqbkoprcmnznmzbwdrmf` — tabela de estoque |
| File extraction | PDF → texto via N8N built-in |

## Notas relacionadas

- [[projects/estoque-budamix]] — ficha do projeto
- [[projects/n8n-builder]] — infraestrutura N8N
