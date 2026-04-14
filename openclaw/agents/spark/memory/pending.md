---
title: "pending"
created: 2026-04-14
type: agent
agent: spark
status: active
tags:
  - agent/spark
---

# Pendências — Spark

_Atualizado: 2026-04-06_

## 🔴 Prioridade Alta

### Google Ads — Integração
- [ ] **Pedro solicitar Developer Token** — sem isso, nenhuma operação Google Ads via API
- [ ] Configurar OAuth 2.0 (Client ID, Secret, Refresh Token)
- [ ] Armazenar credenciais no 1Password (vault OpenClaw)

### Meta Ads — Token
- [ ] **Renovar token antes de ~2026-05-18** — cron agendado, verificar se está funcional

## 🟡 Prioridade Média

### Meta Ads — Mapeamento
- [ ] Mapear campanhas das contas Budamix, Broglio Brinquedos e Trades Up
- [ ] Documentar histórico de performance quando disponível
- [ ] Identificar quais campanhas podem ser reativadas primeiro

### Bidspark — Webapp
- [ ] Pedro aprovar plano do webapp (Supabase + GitHub + Next.js)
- [ ] Pedro criar projeto Supabase "spark-ads"

## 🟢 Backlog

### Quando campanhas reativarem
- [ ] Configurar monitoramento contínuo (anomaly detection)
- [ ] Implementar regras de escala automática (budget optimizer)
- [ ] Estabelecer benchmarks de CPA/ROAS por produto/categoria
- [ ] Criar dashboard de performance (demanda para Builder via Kobe)
- [ ] Análise cross-platform quando Google Ads estiver integrado