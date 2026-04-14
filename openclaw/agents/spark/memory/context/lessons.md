---
title: "lessons"
created: 2026-04-14
type: agent
agent: spark
status: active
tags:
  - agent/spark
---

# Lições — Spark

_Erros e aprendizados. [ESTRATÉGICA] = permanente, [TÁTICA] = expira 30 dias._

### 2026-03-19 — Meta Ads: todas as 16 campanhas estão pausadas [TÁTICA]
**Contexto:** Test drive do Spark — mapeou 16 campanhas na conta GB Distribuição.
**Achado:** Todas pausadas. Nenhuma campanha ativa para monitorar ou otimizar.
**Implicação:** Spark está em modo standby para Meta Ads até campanhas serem reativadas.
**Expira:** 2026-04-19

### 2026-03-19 — Meta Ads token expira ~18/Maio/2026 [TÁTICA]
**Contexto:** Token long-lived do System User tem TTL de ~60 dias.
**Lição:** Cron de renovação agendado. Se falhar, monitoramento fica cego.
**Ação:** Verificar no heartbeat. Renovar 7 dias antes da expiração.
**Expira:** 2026-05-18

### 2026-03-19 — Gasto histórico Meta é baixo (R$27k total) [ESTRATÉGICA]
**Contexto:** GB Distribuição gastou R$27.432,69 total em Meta Ads ao longo do tempo.
**Lição:** Pouco dado histórico para benchmarks robustos. Quando campanhas retomarem, começar conservador com budget e learning phase antes de escalar.
