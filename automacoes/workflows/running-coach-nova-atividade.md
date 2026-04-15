---
title: "Workflow N8N — Running Coach Nova Atividade v2"
type: workflow
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - automacao
  - workflow
  - n8n
  - corrida
  - pessoal
---

# Workflow N8N — Running Coach Nova Atividade v2

| Campo | Valor |
|-------|-------|
| **ID** | `NsREYJCSrE0OYP2p` |
| **URL** | https://trottingtuna-n8n.cloudfy.live/workflow/NsREYJCSrE0OYP2p |
| **Trigger** | Webhook POST /webhook/strava-events (subscription 334482) |
| **Nodes** | 24 |
| **Modelo AI** | Claude Sonnet 4.5 (análise 2000 tokens + memória 500 tokens) |
| **Status** | ✅ Ativo |

## O que faz

Coach de corrida AI "Antonieta" analisa cada atividade do Strava. Pipeline: recebe webhook → filtra corridas → busca histórico + memória + plano → gera análise personalizada → atualiza memória persistente → registra em Google Sheets → envia via WhatsApp.

## Pipeline (24 nodes)

1. Strava Webhook (POST)
2. Filtrar Evento (object_type=activity, aspect_type=create)
3. Buscar Detalhes Strava (OAuth2)
4. Filtrar Corrida (sport_type contains "Run")
5. Formatar Dados (cadência ×2)
6. Salvar no Supabase (activities)
7. Buscar Histórico (últimas 7 atividades)
8. Buscar Perfil (runner_profile)
9. Buscar Memória Coach (últimas 50 notas)
10. Consolidar (1 item — fix rate limit)
11. Ler Plano Semana (Google Sheets A5:J30)
12. Montar Prompt (Antonieta persona v4)
13. Claude API — Análise
14. Atualizar Análise no Supabase
15. Preparar Prompt Memória
16. Claude API — Memória (gera notas JSON)
17. Parsear Notas Memória
18. Salvar Notas Memória (coach_memory)
19. Preparar Registro (15 colunas)
20. Atualizar Registro Treinos (Sheets API append)
21. Preparar Evolução (8 colunas cadência)
22. Atualizar Evolução (Sheets API append)
23. Enviar WhatsApp (Evolution API)
24. Sticky Note

## Integrações

| Serviço | Detalhes |
|---------|----------|
| Strava API | OAuth2, client_id=210371, athlete_id=29493389 |
| Supabase | `xxbsjbgipmtzojhtsrve` — activities, runner_profile, coach_memory |
| Google Sheets | ID: 12tnvIhydtvg3qwsc54H3IV5vwyZOsQ75rlUDf5Li780 |
| Evolution API | WhatsApp 5519993040768 |
| Claude API | Sonnet 4.5 |

## Workflow Relacionado

- **Resumo Semanal** — ID: `a7PRuJs6bmoy7x5G` — Trigger: domingo 0h UTC — 9 nodes

## Notas relacionadas

- [[projects/running-coach-ai]] — ficha do projeto
- [[projects/n8n-builder]] — infraestrutura N8N
