---
title: "Running Coach AI"
created: 2026-04-14
updated: 2026-04-15
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/running-coach-ai/"
tags:
  - project
  - dev
  - corrida
  - n8n
  - pessoal
---

# Running Coach AI

**Path:** `~/Documents/05-Projetos-Codigo/running-coach-ai/`
**Branch:** N/A (não é git repo)
**Stack:** N8N workflows + Supabase + Strava API + Claude Sonnet 4.5 + Evolution API (WhatsApp) + Google Sheets
**Deploy:** N8N Cloud (trottingtuna-n8n.cloudfy.live)
**Supabase:** `xxbsjbgipmtzojhtsrve`
**CLAUDE.md:** sim

## O que é

Sistema de coaching de corrida automatizado com memória persistente. A coach **"Antonieta"** analisa cada atividade do Strava usando Claude AI, aprende a cada treino, atualiza uma planilha Google Sheets e envia a análise via WhatsApp. Projeto pessoal do Pedro.

## Workflows N8N

### 1. Nova Atividade v2 (ID: `NsREYJCSrE0OYP2p`)
- **Status:** ATIVO
- **Trigger:** Webhook POST /webhook/strava-events (subscription 334482)
- **24 nodes:** Strava webhook → filtrar → buscar detalhes → salvar Supabase → buscar histórico + memória + plano → Claude análise → Claude memória → atualizar planilha → WhatsApp
- **AI:** Claude Sonnet 4.5 (análise 2000 tokens + memória 500 tokens)
- **Coach persona:** Antonieta v4 — profissional, acolhedora, metodologia 5 eixos, contexto médico (Venvanse/FC, TRT, canelite)

### 2. Resumo Semanal (ID: `a7PRuJs6bmoy7x5G`)
- **Status:** ATIVO
- **Trigger:** Schedule (domingo 0h UTC)
- **9 nodes:** activities → calc → profile → save summary → prompt → Claude → WhatsApp

## Banco de Dados (Supabase)

| Tabela | Uso |
|--------|-----|
| activities | Atividades Strava + análise AI |
| runner_profile | Perfil atleta (JSON) |
| weekly_summaries | Resumos semanais |
| coach_memory | **50 notas** — memória persistente (5 categorias: athlete_profile, injury_watch, biomechanics, coaching_notes, progress_milestones) |

## Integrações

| Serviço | Detalhes |
|---------|----------|
| Strava API | OAuth2, client_id=210371, athlete_id=29493389 |
| Google Sheets | ID: 12tnvIhydtvg3qwsc54H3IV5vwyZOsQ75rlUDf5Li780 (Plano_Unificado_Pedro_2026) |
| Evolution API | WhatsApp 5519993040768 |
| Claude API | Sonnet 4.5 |

## Dados Importados

- 12 atividades (11 históricas + 1 Strava) — importado 11/Mar/2026
- 50 notas de coach_memory (33 do briefing antigo coach + 17 do histórico)
- Runner profile completo (altura, peso, medicação, zonas de pace, cadência)

## Notas relacionadas

- [[projects/n8n-builder]] — infraestrutura N8N
- [[knowledge/pessoal/perfil-pedro-broglio]] — Pedro pratica corrida