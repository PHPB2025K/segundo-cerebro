---
title: "HEARTBEAT"
created: 2026-04-14
type: heartbeat
agent: spark
status: active
tags:
  - agent/spark
---

# HEARTBEAT.md — Spark

_Verificações periódicas quando ativado em modo heartbeat._

---

## Verificações

### 1. Token Meta Ads
- Token válido? Testar via `GET /me`
- Expira nos próximos 7 dias? → Alertar Kobe para renovação
- Se expirado → 🔴 Alerta imediato (monitoramento cego)

### 2. Campanhas Ativas
- Alguma campanha ativa? (status != PAUSED/ARCHIVED)
- Se ativa: CPA vs meta (10x ROAS)? Spend vs budget? Anomalias?
- Se todas pausadas: HEARTBEAT_OK (nada a monitorar)

### 3. Anomalias (se campanhas ativas)
- CPA > 1.5x meta? → 🟡 Atenção
- CPA > 2x meta? → 🔴 Alerta
- Budget burn > 120% antes das 15h? → 🟡 Atenção
- Conversões zeraram com spend > 0? → 🔴 Alerta (tracking?)

### 4. Pendências Estagnadas
- Ler `memory/pending.md`
- Itens 🔴 há > 2 dias → sinalizar ao Kobe
- Itens 🟡 há > 7 dias → reavaliar prioridade

### 5. Creative Lifecycle (se campanhas ativas)
- Algum creative com > 14 dias sem refresh? → 🟡 Verificar CTR
- CTR caindo > 20% em 7 dias? → Alertar creative fatigue

## Regra

- **Encontrou algo urgente** → alerta ao Kobe
- **Encontrou algo importante** → anota em `pending.md`
- **Nada de novo / campanhas pausadas** → HEARTBEAT_OK
