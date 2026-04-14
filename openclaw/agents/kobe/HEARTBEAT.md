---
title: "HEARTBEAT"
created: 2026-04-14
type: heartbeat
agent: kobe
status: active
tags:
  - agent/kobe
---

# HEARTBEAT — Checklist Proativo do Kobe

_Atualizado: 2026-03-23_

## Horários de Silêncio (NUNCA notificar)
- **22:00–06:45 SP** — madrugada
- **Sáb 13:00–Dom 23:59** — descanso do Pedro
- **07:00–10:00 seg-sex** — bloco de foco (só urgências reais)
- Urgência real = dinheiro sendo perdido, sistema fora do ar, prazo vencendo HOJE

## Verificações a cada heartbeat

### 1. Emails urgentes
- Checar inbox pehpbroglio@gmail.com por emails com Label_8 (Urgente)
- Se encontrar → avisar Pedro com resumo
- Se não → silêncio

### 2. Agenda próximas 48h
- Puxar eventos do calendar pehpbroglio@gmail.com (próximas 48h)
- Se houver evento nas próximas 4h que Pedro pode não ter visto → avisar
- Se nada relevante → silêncio

### 3. Tokens e integrações
- ML tokens: verificar se access_token não está expirado (6h TTL)
- Shopee tokens: verificar os 3 (budamix-store, budamix-store2, budamix-shop). Se algum expirou → avisar Pedro pra reautorizar
- Meta Ads token: verificar validade (60 dias, expira ~2026-05-18)
- Google OAuth (gog): verificar se está funcional
- Se algum quebrado → avisar + tentar refresh automático

### 4. WhatsApp
- Verificar conexão: `openclaw channels status --probe`
- Se WhatsApp desconectado → avisar Pedro (precisa re-escanear QR code)
- Se conectado → silêncio

### 5. Agentes (Trader, Spark, Builder)
- Verificar se os agentes estão operacionais
- Se algum com erro → diagnosticar e reportar
- Se todos ok → silêncio

### 6. Pendências estagnadas
- Ler memory/pending.md
- Itens há >7 dias sem resolução → incluir no próximo briefing
- NÃO notificar no heartbeat, apenas marcar pro briefing

### 7. Saúde do sistema
- Espaço em disco (df -h / | awk '{print $5}')
- Se >85% → avisar
- Verificar se últimos crons rodaram ok (cron runs dos últimos 3 jobs)
- Se algum falhou → avisar

### 8. Tabela orders (Supabase) — CRÍTICO
- Verificar count da tabela orders no Supabase
- Se orders < 1000 registros → ALERTA URGENTE ao Pedro (tabela foi esvaziada)
- Se orders < 10000 → ALERTA: dados incompletos, verificar sync
- Esperado: >40.000 registros (180 dias de histórico)
- Se vazia → rodar imediatamente: `python3 /root/.openclaw/workspace/scripts/sync-ml-orders.py --days 180` + shopee + amazon
- Causa resolvida: pg_cron jobs no Supabase foram removidos (eram redundantes e conflitavam com scripts VPS)

### 9. Tarefas pendentes (tasks-pending.md)
- Ler memory/tasks-pending.md
- Se há tarefas não concluídas (sem ✅) → reportar status ao Pedro no próximo briefing
- Se há tarefas com mais de 24h sem progresso → incluir como alerta

### 10. MEMORY.md e arquivos core
- Última atualização: checar data nos arquivos
- Se MEMORY.md >7 dias → atualizar silenciosamente
- Se SOUL.md, AGENTS.md ou IDENTITY.md >14 dias sem modificação e houve mudanças relevantes → avisar no briefing

## Regra de ouro
- **Encontrou algo urgente** → avisa Pedro
- **Encontrou algo importante mas não urgente** → anota pro briefing
- **Nada de novo** → HEARTBEAT_OK (silêncio total)
- **Trabalho de organização** → faz sozinho, sem avisar
