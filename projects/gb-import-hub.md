---
title: "GB Import Hub"
created: 2026-04-15
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/gb-import-hub/"
tags:
  - project
  - dev
  - importacao
---

# GB Import Hub

**URL:** https://import.budamix.com.br
**Branch:** main
**Stack:** Next.js + React + Supabase + Edge Functions (Deno) + Terminal49 + Mapbox
**Deploy:** VPS 187.77.237.231 (Nginx + Traefik + SSL Let's Encrypt)
**Supabase:** `ocxvwwaaqqxecmzhfxhb`
**Repo:** `PHPB2025K/gb-import-hub`

## O que é

Sistema de gestão de importações da GB Importadora. Controla containers, documentos, tracking marítimo, pagamentos (numerário + 70% balanço), e conferências de custos. Central de controle para todas as operações de importação.

## Schema (12 tabelas)

| Tabela | O que guarda |
|--------|-------------|
| containers | Dados centrais do container (ID, status logístico/financeiro) |
| documents | Documentos de importação (PDF, storage) |
| finance_pagamentos | Pagamentos (numerário, 70% balanço) |
| finance_numerario_itens | Itens individuais por pagamento |
| conferencias_numerario | Conferências de numerário |
| conferencias_comunicacoes | Comunicações de conferência |
| referencias_mercado | Referências de mercado para precificação |
| referencias_ncm | Referências NCM/tributárias |
| vessel_tracking | Tracking de embarcações (Terminal49) |
| vessel_position_history | Histórico de posições |
| tracking_alerts | Alertas de tracking |
| container_milestones | Marcos/eventos do container |

## Edge Functions (17 deployadas)

Inclui: `extract-import-document`, `calculate-tax-references`, `fetch-vessel-position`, `get-mapbox-token`, entre outras.

## Containers Ativos

| Container | Status Logístico | Status Financeiro |
|-----------|:----------------:|:-----------------:|
| GB25007 | finished | A PREENCHER |
| GB25009 | finished | 🔴 70% R$72.232 vence 16/04 |
| GB25011 | em trânsito | Numerário pago, 70% R$71.419 vence 24/05 |
| GB26001 | A PREENCHER | A PREENCHER |
| GB26002 | A PREENCHER | A PREENCHER |

## Decisões-chave

- [08/04] Migração completa de Lovable Cloud para Supabase externo: 12 tabelas, 4.530 rows, 17 Edge Functions, 27 docs, SSL
- [08/04] Dual cycle model: status logístico (production→maritime→customs→road→finished) ≠ status financeiro (pending/paid/overdue)
- [08/04] Supabase REST API: ANON_KEY para reads, SERVICE_ROLE_KEY para writes

## Pendências

- [ ] Frontend Lovable ainda aponta pro Supabase antigo — atualizar env vars OU usar somente deploy VPS
- [ ] MarineTraffic API key não configurada (tracking funciona via Terminal49)
- [ ] Módulo Conferências (validação custos importação) — em construção
- [ ] Skill gb-import-hub v2 validada (14/15 testes OK, terminal49-fetch-shipment com bug HTTP 500)

## Notas relacionadas

- [[business/importacao/_index]] — índice importação
- [[automacoes/sops/atualizar-pagamento-importacao]] — SOP pagamentos
- [[knowledge/concepts/credenciais-map]] — credenciais (7 items GB Import Hub)
- [[memory/context/deadlines]] — prazos financeiros
