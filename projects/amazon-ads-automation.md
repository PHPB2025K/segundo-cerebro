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
**Último commit (local):** 22/04/2026 — `ce5b218` docs(financeiro): snapshot 21/04 + plano maio. **22 commits local-only**, não pushed.
**Skill operacional:** `ANALISE_SEMANAL_SKILL.md` **v4.2** (BidSpark-3 consolidado — 3 campanhas, sem Defesa salvo edge Jarra-ASIN real)
**Migração BidSpark-3: FILA FECHADA** (9/10 grupos ativos; Abraçadeiras+Redinha pausados 15/04). Sessão conjunta 20-22/04 executou os 5 restantes: Canequinhas, Potes Redondos, Kits Microfibra, Canelada, Jarra Medidora. Total 50 EXECUTED + 24 DEFERRED = 74 entries em `actions_log`.
**Próxima revisão:** D+7 em **27/04/2026** conjunta dos 5 executados.
**Knowledge file:** [[knowledge/concepts/amazon-ads-bidspark-3]] (consolidado 13 seções).

## O que é

Sistema de automação de publicidade Amazon Ads para a GB Importadora. Coleta métricas diárias via Amazon SP-API e alimenta análise manual via Claude Code com skill BidSpark-3. Backend FastAPI hospedado no Railway, dados no Supabase, orquestração N8N.

Inclui também o cron de Amazon Request Review (review requests pós-venda).

**Modelo operacional atualizado (19/04):** N8N é usado APENAS para coletas diárias (campaigns, keywords, search_terms, snapshots, compute-results). Análise e otimização de campanhas são feitas manualmente via Claude Code com `ANALISE_SEMANAL_SKILL.md`. Modelo original "N8N → Claude API automática → ações" foi abandonado em favor de supervisão humana.

## Decisões-chave

- [13/04] Amazon Request Review migrado de GPT-5.4 para Opus 4.6 exclusivo (sem fallback GPT)
- [13/04] Campo `delivered_at` adicionado à tabela `orders` — filtra por data de entrega real
- [13/04] Timeout aumentado de 420s para 600s, batch size 35 orders/run
- [13/04] Backfill de ~4866 pedidos executado
- [16/04] BidSpark-4 → BidSpark-3 — Defesa removida como role; 3 campanhas (Descoberta/Alcance/Performance)
- [19/04] Budget split nominal 15/30/55 obrigatório em migração; multiplicadores ×1.5/×1.2/×0.72
- [19/04] N8N apenas para coletas (análise é manual); compute-results fix com `continueOnFail` no WhatsApp Alert
- [19/04] Grupos antigos (pré-01/03/2026) têm legado destrutivo Fev/Mar — inspeção de NEG_PHRASE obrigatória na análise
- [20/04] Health check N8N revelou fix 19/04 incompleto — paliativo aplicado em `Send Rolling WhatsApp`. Ticket 1 elevado para ALTA.
- [22/04] **Defesa-ASIN real é excepção** (só Jarra Medidora tem Defesa produtiva — 2 ped/R$47/30d via ASIN concorrente). Não pausar em futuros scripts desse grupo.
- [22/04] **G1 evoluído em 3 dimensões** (tokenizado, match_type, contexto de ação). Candidato a template skill v4.3.
- [22/04] **Leonardo = focal point Amazon** para investigações Seller Central (Tickets 7/10/11).
- [22/04] **Plano maio** orientado a cortar waste: 274→249/dia (−9,3%). Escalar só Jarra (+20%).

## Pendências

- [ ] **Push dos 22 commits local-only** em `main` (cresceu de 4→22 na sessão 20-22/04). Pedro decide quando.
- [ ] **Revisão D+7 em 27/04** dos 5 grupos executados. Com ressalva do Ticket 12 (blind spots compute-results).
- [ ] **Tickets novos abertos** (22/04):
  - Ticket 7 — Canequinhas listing Performance → Leonardo
  - Ticket 9 — `TargetsV3` helper para bid reduction Auto → código
  - Ticket 10 — Potes Redondos bootstrap → Leonardo (ALTA)
  - Ticket 11 — Kits Microfibra anomalia 7d=0 → Leonardo
  - Ticket 12 — compute-results blind spots → código
- [ ] Tampa Bambu investigation residual — confirmar com Pedro se já foi feita antes de re-delegar a Leonardo
- [ ] Revisitar Tulipa ~03/05 (14d pós-Bloco 3)
- [ ] Jarra Medidora ciclo 2 — se `copo medidor` bid R$0,65 converter ≥2 vendas em D+14, subir para R$0,85
- [ ] Abraçadeiras + Redinha: status real deveria ser `active=false` em `product_groups` (dívida mapping)
- [ ] SKUs duplicados IMB501*_T — investigação antiga, segue em aberto

## Notas relacionadas

- [[projects/ml-ads-automation]]
- [[projects/bidspark-multiagente-completo]]
- [[openclaw/agents/spark/IDENTITY]]
- [[openclaw/agents/trader/IDENTITY]]
- [[business/marketplaces/_index]]
- [[meta/mocs/MOC - Superpowers Pipeline]]
- [[meta/mocs/MOC - Taxas e Precificacao]]
