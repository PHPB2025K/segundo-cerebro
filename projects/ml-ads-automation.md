---
title: "ML Ads Automation"
created: 2026-04-14
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/ml-ads-automation/"
tags:
  - project
  - dev
  - mercado-livre
  - ads
---

# ML Ads Automation

**Path:** `~/Documents/05-Projetos-Codigo/ml-ads-automation/`
**Branch:** main
**Stack:** Python (FastAPI)
**Deploy:** Railway
**CLAUDE.md:** sim
**Último commit:** 6 weeks ago — feat: add authenticated /dashboard/* endpoints with CORS for BudaAds integration

## O que é

Sistema de automação de publicidade Mercado Livre Product Ads para a GB Importadora. Mesma arquitetura do Amazon Ads Automation: coleta métricas diárias, análise com IA, recomendações via WhatsApp. Inclui endpoints autenticados para dashboard BudaAds.

4 tabelas Supabase: ml_tokens, ml_campaigns_daily, ml_ads_daily, ml_optimization_reports. Endpoints: refresh, status, collect/campaigns, collect/ads, analyze, notify.

## Status

⚠️ **Inativo há 6 semanas.** Sistema pronto para deployment — necessita apenas cron N8N configurado. Considerar reativação.

## Notas relacionadas

- [[projects/amazon-ads-automation]]
- [[projects/ml-ads-next-steps]]
- [[openclaw/agents/spark/IDENTITY]]
- [[openclaw/agents/trader/IDENTITY]]
- [[business/marketplaces/_index]]
- [[meta/mocs/MOC - Taxas e Precificacao]]
- [[meta/mocs/MOC - Listing Pipeline]]