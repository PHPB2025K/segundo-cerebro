---
title: "FinanceFlow"
created: 2026-04-15
type: project
status: building
path: "VPS 187.77.237.231 (OpenClaw/Fisco)"
tags:
  - project
  - dev
  - fiscal
  - bling
---

# FinanceFlow

**Branch:** — (integrado ao OpenClaw)
**Stack:** OpenClaw (multi-agent) + Bling API v3 (OAuth, plano Mercúrio)
**Deploy:** VPS Hostinger (187.77.237.231)
**Agente:** [[openclaw/agents/fisco/IDENTITY|Fisco]]

## O que é

Automação fiscal para 6 CNPJs da GB Importadora. Gerencia distribuição de estoque, emissão de NF-e (transferência e interna), conciliação fiscal e monitoramento do Simples Nacional. Opera como parte do agente Fisco dentro do OpenClaw.

## Módulos Arquitetados

| Módulo | Nome | Status | Descrição |
|:------:|------|:------:|-----------|
| A | Motor de Distribuição | 🔴 Não iniciado | Distribui estoque entre CNPJs conforme regras fiscais |
| B | NF Transferência | 🔴 Não iniciado | Emissão de NFs de transferência entre filiais |
| C | NF Interna | 🔴 Não iniciado | Emissão de NFs internas (draft mode) |
| D | Conciliação | 🔴 Não iniciado | Conciliação fiscal entre Bling e realidade |
| E | Monitor Simples Nacional | 🔴 Não iniciado | Monitoramento de limites e compliance SN |

## Integração Bling

| Item | Valor |
|------|-------|
| API | Bling v3 (OAuth) |
| Plano | Mercúrio |
| Matriz | 58.151.616/0001-43 |
| Filial | 58.151.616/0002-24 |
| Contadora | FOUR (Suellen) |
| Credenciais | 1Password → "Bling API - Matriz" e "Bling API - Filial" |

## Status Atual

🔨 **Fase 1 — Fundação**: Setup do agente Fisco pronto (IDENTITY, SOUL, skills). Integração Bling API v3 configurada (OAuth tokens). Estrutura dos 5 módulos arquitetada. **Bloqueio**: Módulos A-E não iniciados.

## Decisões-chave

- [06/04] Agente Fisco criado dentro do OpenClaw, subordinado ao Kobe
- [06/04] Nível L1 (Observer) — todo output revisado pelo Kobe antes de executar
- Dois ciclos independentes: logístico (containers) vs financeiro (3 pagamentos)

## Pendências

- [ ] Implementar Motor de Distribuição (Módulo A)
- [ ] Emissão de NFs em draft (Módulos B e C)
- [ ] Conciliação + Monitor + crons (Módulos D e E)
- [ ] Integração API Bling v3 completa (OAuth flow validado)

## Notas relacionadas

- [[openclaw/agents/fisco/IDENTITY]] — agente Fisco
- [[business/financeiro/_index]] — índice financeiro
- [[knowledge/concepts/credenciais-map]] — credenciais Bling
