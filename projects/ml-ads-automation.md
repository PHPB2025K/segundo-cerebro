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
**Advertiser ID configurado:** 172453 (conta GAMMAOFICIAL, user_id 532562281, site MLB)

## O que é

Sistema de automação de publicidade Mercado Livre Product Ads para a GB Importadora. Mesma arquitetura do Amazon Ads Automation: coleta métricas diárias, análise com IA, recomendações via WhatsApp. Inclui endpoints autenticados para dashboard BudaAds.

4 tabelas Supabase: ml_tokens, ml_campaigns_daily, ml_ads_daily, ml_optimization_reports. Endpoints: refresh, status, collect/campaigns, collect/ads, analyze, notify.

## Status

🟡 **Semi-vivo (08/05/2026)**: refresh diário de token rodando às 10:30 BRT (último em 07/05 → expires 08/05 19:01 UTC). OAuth completo, advertiser_id preenchido, refresh_token vivo (válido 6 meses). **Falta:** cron de coleta diária (`/ml/collect/campaigns` + `/ml/collect/ads`) — Supabase tem só linha de tokens, sem `ml_campaigns_daily` ou `ml_ads_daily` populadas. Por isso histórico de métricas se limita ao que a API expõe ao vivo: **últimos 90 dias**.

**Pra ativar coleta acumulativa:** subir workflow N8N descrito em [[projects/ml-ads-next-steps]] § 4 (cron 10:30 BRT → refresh → collect campaigns → collect ads → analyze → notify).

## Notas relacionadas

- [[projects/amazon-ads-automation]]
- [[projects/ml-ads-next-steps]]
- [[openclaw/agents/spark/IDENTITY]]
- [[openclaw/agents/trader/IDENTITY]]
- [[business/marketplaces/_index]]
- [[meta/mocs/MOC - Taxas e Precificacao]]
- [[meta/mocs/MOC - Listing Pipeline]]