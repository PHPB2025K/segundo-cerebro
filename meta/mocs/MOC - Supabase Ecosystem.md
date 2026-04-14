---
title: "MOC   Supabase Ecosystem"
created: 2026-04-14
type: moc
status: active
tags:
  - moc
---

# MOC — Supabase Ecosystem

> Mapa de todos os projetos Supabase e quais agentes/sistemas usam cada um.

---

## Projetos Supabase

| Projeto | ID | Usado por | Proposito |
|---------|-----|----------|----------|
| GB Import Hub | `ocxvwwaaqqxecmzhfxhb` | [[openclaw/agents/kobe/IDENTITY|Kobe]] | Controle de importacoes, containers, tracking |
| Budamix Central (Canggu) | — | [[openclaw/agents/builder/IDENTITY|Builder]], Ana | Dashboard interno, produtos, atendimento |
| Ponto Certo | — | [[openclaw/agents/rh/IDENTITY|RH]], [[openclaw/agents/builder/IDENTITY|Builder]] | Ponto eletronico, banco de horas |
| Spark Ads | `wzhmrpskiscassbixurr` | [[openclaw/agents/spark/IDENTITY|Spark]] | Cache de dados Meta/Google Ads |

## Uso por agente

| Agente | Como usa Supabase |
|--------|------------------|
| [[openclaw/agents/kobe/IDENTITY|Kobe]] | GB Import Hub (containers, docs, finance), orders cache marketplace |
| [[openclaw/agents/trader/IDENTITY|Trader]] | Cache de dados marketplace, marketplace_tokens (dual-sync OAuth) |
| [[openclaw/agents/spark/IDENTITY|Spark]] | Edge Function sync-ads, cache de campanhas |
| [[openclaw/agents/builder/IDENTITY|Builder]] | Stack padrao (PostgreSQL + Auth + Storage + Realtime + Edge Functions) |
| [[openclaw/agents/fisco/IDENTITY|Fisco]] | marketplace_tokens table para dual-sync de tokens OAuth Bling |
| [[openclaw/agents/rh/IDENTITY|RH]] | Ponto Certo (punches, banco de horas, perfis, atrasos, faltas) |
| Ana (AI) | Embeddings pgvector em base_products para busca semantica |

## Features Supabase em uso

| Feature | Projetos |
|---------|---------|
| PostgreSQL | Todos |
| Auth (RLS) | Budamix Central, Ponto Certo, GB Import Hub |
| Storage | GB Import Hub (documentos), Budamix Central (product-images) |
| Realtime | GB Import Hub (finance_pagamentos) |
| Edge Functions | GB Import Hub (17), Ponto Certo, Spark Ads (sync-ads) |
| pgvector | Budamix Central (embeddings de produtos) |

## Licoes compartilhadas

- Upsert on_conflict: condicional por tabela — products sim, price_history nao
- Row limit 1000: sempre paginar queries grandes
- service_role key: hardcoded nos scripts (divida tecnica documentada)

## Skills relacionadas

- [[skills/gb-import-hub/SKILL|gb-import-hub]] — acesso ao Import Hub
- [[skills/dev/fullstack-dev/references/database|fullstack-dev/database]] — PostgreSQL avancado + Drizzle
- [[skills/dev/fullstack-dev/references/auth-security|fullstack-dev/auth-security]] — Auth + RLS patterns

---

*Criado: 10/04/2026 — Auditoria de conexoes*
