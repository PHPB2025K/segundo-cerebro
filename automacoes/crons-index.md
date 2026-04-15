---
title: "Índice de Crons e Automações — OpenClaw"
type: index
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - automacoes
  - crons
  - openclaw
  - index
---

# Índice de Crons e Automações — OpenClaw

> Todos os crons e automações do sistema OpenClaw documentados.
> Rodam na VPS 187.77.237.231 via OpenClaw Gateway (daemon).
> Config: `/root/.openclaw/openclaw.json`

---

## Crons Ativos

### Kobe (Orquestrador)

| # | Nome | Frequência | O que faz | Modelo | Timeout | Status |
|:-:|------|-----------|-----------|--------|:-------:|:------:|
| 1 | **Segundo Cérebro Sync** | Diário 06:45 BRT | Git pull GitHub → rsync skills + agents → lê pendencias.md e sessions | — | — | ✅ |
| 2 | **Briefing Matinal** | Diário ~07:00 BRT | Emails, calendar 48h, tokens, WhatsApp, saúde agentes, disco (>85%), orders Supabase | GPT 5.4 | — | ✅ |
| 3 | **Consolidação Diária** | Diário 23:30 SP | Extrai lessons→context, decisions→context, limpa pending (>14d), commit+push GitHub | GPT 5.4 | — | ✅ 🔒 |
| 4 | **Consolidação Profunda** | 1º e 15º do mês 04:00 SP | Segunda passagem em sessões, promove lições recorrentes a ESTRATÉGICA, expira táticas velhas | GPT 5.4 | — | ✅ 🔒 |
| 5 | **Contingency Guard** | A cada 5 min | Monitora rate limit (429, 503). Se detectado, fallback chain auto-engaja | GPT 5.4 | 30s ⚠️ | ✅ |
| 6 | **Job Monitor** | Polling contínuo ~30s | Monitora status de jobs do Builder (completed/failed/timeout) | GPT 5.4 | 30s ⚠️ | ✅ |
| 7 | **Organização Noturna** | Noturno (~22-23h) | Arquiva logs antigos, remove orphans, limpa backups (mantém 30d), health check | GPT 5.4 | 180s ⚠️ | ✅ |
| 8 | **GitHub Backup** | Diário (noturno) | Commit workspace state + push config + memory + sessions | GPT 5.4 | 120s ⚠️ | ✅ |

🔒 = INVIOLÁVEL — nunca fazer downgrade de modelo

### Trader (Marketplaces)

| # | Nome | Frequência | O que faz | Modelo | Timeout | Status |
|:-:|------|-----------|-----------|--------|:-------:|:------:|
| 9 | **Amazon Request Review** | Diário 20:30 BRT | Processa review requests, filtra por delivered_at, batch 35 orders | Opus 4.6 | 600s | ✅ |

### RH (Recursos Humanos)

| # | Nome | Frequência | O que faz | Modelo | Timeout | Status |
|:-:|------|-----------|-----------|--------|:-------:|:------:|
| 10 | **Monitor Ponto Semanal** | Segunda 10:00 BRT | Analisa registros semana anterior, envia WhatsApp consolidado por funcionário, report Telegram thread 10 | GPT 5.4 | 300s | ✅ |
| 11 | **Compliance Check Diário** | Seg-Sáb 19:00 BRT | Auditoria silenciosa CLT (intervalos, jornada 10h, faltas, banco horas). Só notifica Pedro se violação grave | GPT 5.4 | 120s | ✅ |
| 12 | **Ponto Certo QR Refresh** | Diário 03:00 BRT | Manutenção técnica — refresh QR codes, health check | GPT 5.4 | 120s | ✅ |

---

## Crons Planejados (Não Criados)

| Nome | Frequência | O que faz | Agente | Bloqueio |
|------|-----------|-----------|--------|----------|
| **Relatório Mensal Contador** | 1º do mês 09:00 BRT | Gera relatório ponto para contador (FOUR/Suellen) | RH | Aguardando formato da contadora |
| **Banco de Horas Semanal** | Segunda 08:00 BRT | Calcula saldo semanal, verifica teto 40h / piso -10h | RH | Skill pronta, cron não criado |

---

## Problemas de Timeout

| Cron | Atual | Necessário | Impacto |
|------|:-----:|:----------:|---------|
| Job Monitor | 30s | 60-90s | Checks insuficientes para jobs longos |
| Contingency Guard | 30s | 60s | Detecção de rate limit atrasada |
| Organização Noturna | 180s | 300-600s | Operações de limpeza interrompidas |
| GitHub Backup | 120s | 300s | Push falha em repos grandes |

---

## Fallback Chain

```
GPT 5.4 (primário) → GPT 5.1-mini → Claude Haiku 4.5
```

Todos os agentes usam esta cadeia. Amazon Request Review é exceção: usa Opus 4.6 exclusivo (sem fallback GPT).

---

## Automações N8N

| Workflow | O que faz | Onde roda |
|----------|-----------|-----------|
| PDF Parser Estoque | Parseia planilha de entrada de estoque | N8N trottingtuna |
| Gmail Organizer | Categoriza emails em 6 pastas | N8N trottingtuna |
| Running Coach | Coaching de corrida personalizado | N8N trottingtuna |
| Ana/Giovana Atendimento | Fluxo WhatsApp SDR (Evolution API → Supabase → resposta) | N8N trottingtuna |

---

## Monitoramento

- **Telegram**: Canal principal para alertas e reports (Kobe Hub, 11 tópicos)
- **Debounce**: 8s de silêncio antes de processar (exceto `!` no final)
- **Reações**: ⏳ = aguardando mais mensagens, 🧠 = processando
- **HEARTBEAT_OK**: Condição silenciosa (sem issues encontrados)

---

## Notas Relacionadas

- [[openclaw/agents/kobe/IDENTITY]] — orquestrador
- [[openclaw/agents/kobe/HEARTBEAT]] — checklist briefing
- [[openclaw/agents/rh/IDENTITY]] — agente RH
- [[memory/context/pendencias]] — pendências com timeout
- [[knowledge/concepts/stack-tecnico]] — infraestrutura
