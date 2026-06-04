---
title: "Índice de Fichas de Projeto"
created: 2026-04-14
type: index
status: active
tags:
  - project
  - index
---

# Fichas de Projeto

> Cada ficha descreve um projeto de código com path, stack, deploy e links.
> Código-fonte em `~/Documents/05-Projetos-Codigo/`.

## Marketplaces e Ads

- [[projects/amazon-ads-automation]] — Automação Amazon Ads (Python/FastAPI)
- [[projects/ml-ads-automation]] — Automação ML Ads (Python/FastAPI) — 🟡 semi-vivo (refresh diário OK, cron de coleta inativo). Advertiser 172453 (GAMMAOFICIAL). Briefing baseline gerado 08/05/2026.
- [[projects/ml-ads-next-steps]] — Próximos passos ML Ads
- [[projects/analise-semanal-skill-amazon]] — Skill de análise semanal Amazon
- [[projects/bidspark-multiagente-completo]] — Bidspark multi-agente (spec)
- [[projects/daily-sales-shopee]] — Daily Sales Report Shopee multi-conta (Store/Oficial/Shop). 🟡 **Fase 1 validada (04/06) — em standby por decisão do Pedro pra lapidação futura.** 9 prompts v4.0/shopee (3.708 linhas) + snapshot fetcher + runner adaptado do ML + Mission Control `/reports/daily-sales-shopee` com 3 cards. Smoke 03/06 APROVADO (13 gates, 0 críticos). Regra de densidade de 4 elementos pra risco silencioso por gap aplicada.

## Atendimento e WhatsApp

- [[projects/canggu/canggu|Canggu]] — MicroSaaS atendimento WhatsApp (agente "Ana"). Stack: Vite + React 19 + Supabase Edge Functions + N8N + Evolution API + Anthropic/OpenAI/Groq. Auditoria forense 2026-04-22, roadmap de refatoração em 6 blocos. Subpasta com 12 notas (MOC + arquitetura + edge functions + N8N + frontend + débitos + ADRs + histórico).
- [[projects/budamix-agent-changelog-ana]] — Changelog da Ana (pré-auditoria 22/04)
- [[projects/whatsapp-api]] — Config WhatsApp API (Baileys + Evolution)

## Dashboards e Sistemas Internos

- [[projects/budamix-central]] — Budamix Central (dashboard interno, Live Sales, pgvector)
- [[projects/gb-import-hub]] — GB Import Hub (gestão importações, containers, tracking)
- [[projects/ponto-certo]] — Ponto Certo (ponto eletrônico funcionários, GPS, QR Code, banco de horas)
- [[projects/atlas-finance]] — Atlas Finance (contas a pagar/receber, DFC — pausado)

## E-commerce

- [[projects/budamix-ecommerce]] — E-commerce Budamix (React + Supabase + Mercado Pago). 20/05 ganhou feature de variações estruturadas (atributos JSONB + galeria por variante)
- [[projects/klap-porcelana]] — E-commerce Klap Porcelana (canecas/xícaras CNPJ GB). 28 SKUs em 4 coleções, 82 reviews populadas, banner único, dedup product_images concluído 03/06
- [[projects/banner-triplo-budamix]] — Banner triplo Instagram 2000×2500 (HTML+Puppeteer) — entregue 20/05/2026
- [[projects/social-studio-reborn]] — **Social Studio Reborn** (publicador + métricas Instagram, sem IA) — Fase A concluída 06/05, PR #3 aguardando merge. Próxima: Fase B (Composer + Agendador).
- [[projects/social-studio-carrossel]] — ⚠️ DESCONTINUADO 06/05/2026 (módulo IA original, substituído pelo Reborn). Mantido como referência histórica.

## Fiscal e Financeiro

- [[projects/financeflow]] — FinanceFlow (automação fiscal 6 CNPJs, agente Fisco)

## Estratégia e Planejamento

- [[projects/planejamento-importacao-2026]] — Dimensionamento da cadência de importação (tese do flywheel, lotes de 4 × GB25011), 4 fases, método essencialista

## Operação e Estoque

- [[projects/estoque-budamix]] — Estoque Budamix (Next.js + Supabase)
- [[projects/simulimpor]] — SimulaImport (MicroSaaS importação)
- [[projects/carousel-factory]] — Carousel Factory (paused)

## Infraestrutura e N8N

- [[projects/mission-control]] — Mission Control (painel visual OpenClaw, fork TenacitOS + design system Budamix Central) — 🟢 frontend 100% + Dashboard PRD fechado 12/05
- [[projects/openclaw-vps]] — OpenClaw VPS (deploy/config)
- [[projects/openclaw-config]] — OpenClaw Config (briefings)
- [[projects/n8n-builder]] — N8N Builder (workflow architect)
- [[projects/gmail-organizer]] — Gmail Organizer (N8N)
- [[projects/running-coach-ai]] — Running Coach AI (N8N)
