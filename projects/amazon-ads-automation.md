---
title: "Amazon Ads Automation"
created: 2026-04-14
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/amazon-ads-automation/"
tags:
  - project
  - dev
  - amazon
  - ads
---

# Amazon Ads Automation

**Path:** `~/Documents/05-Projetos-Codigo/amazon-ads-automation/`
**Branch:** main
**Stack:** Python (FastAPI) + Docker
**Deploy:** Docker (Railway)
**CLAUDE.md:** sim
**Último commit:** 4 days ago — fix: add missing start_negative_snapshot function

## O que é

Sistema de automação de publicidade Amazon Ads para a GB Importadora. Coleta métricas diárias via Amazon SP-API, analisa performance com IA (Claude), e envia recomendações via WhatsApp. Backend FastAPI hospedado no Railway, dados no Supabase.

Inclui também o cron de Amazon Request Review (review requests pós-venda).

## Decisões-chave

- [13/04] Amazon Request Review migrado de GPT-5.4 para Opus 4.6 exclusivo (sem fallback GPT)
- [13/04] Campo `delivered_at` adicionado à tabela `orders` — filtra por data de entrega real
- [13/04] Timeout aumentado de 420s para 600s, batch size 35 orders/run
- [13/04] Backfill de ~4866 pedidos executado

## Pendências

- [ ] Monitorar taxa de sucesso Request Review até 20/04 (meta >70%)
- [ ] SKUs duplicados: IMB501*_T e IMB501T-{cor} apontam para mesmos ASINs — investigar

## Notas relacionadas

- [[projects/ml-ads-automation]]
- [[projects/bidspark-multiagente-completo]]
- [[openclaw/agents/spark/IDENTITY]]
- [[openclaw/agents/trader/IDENTITY]]
- [[business/marketplaces/_index]]
- [[meta/mocs/MOC - Superpowers Pipeline]]
- [[meta/mocs/MOC - Taxas e Precificacao]]
