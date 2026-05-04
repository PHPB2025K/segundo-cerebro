---
title: "pending"
created: 2026-04-14
type: agent
agent: builder
status: active
tags:
  - agent/builder
---

# Pendências — Builder

_Atualizado: 2026-05-03_

## 🔴 Prioridade Alta

### Bidspark — Segurança
- [ ] **Remover credenciais do CLAUDE.md** — Client ID + Secret em plain text no Amazon Ads. Pedro precisa remover urgente
- [ ] **Trocar ambiente para produção** — `AMAZON_ADS_ENVIRONMENT=production` no `.env` antes de ativar otimizações reais

### Bidspark — Testes
- [ ] **Suite mínima de testes** — zero testes atualmente. Implementar testes nos caminhos que mexem com dinheiro (bids, budgets, guardrails)


### Infra OpenClaw / Agentes
- [ ] Fisco/OpenClaw — diagnosticar bloqueio de sessions_spawn com `agentId=fisco` retornando `allowed: none`; validar policy/runtime/gateway e restaurar roteamento direto.

## 🟡 Prioridade Média

### Atlas Finance — Relatórios
- [ ] Relatório de fluxo de caixa — quebrado, Pedro precisa
- [ ] DRE (Demonstração de Resultado) — quebrado
- [ ] Balanço — quebrado
- [ ] Retomar quando Pedro priorizar

### SimulImport
- [ ] Testes extensivos
- [ ] Melhorias de UX
- [ ] Production ready para primeiros test users

### Infra
- [ ] Nginx — instalar quando necessário para reverse proxy no VPS

### Execução técnica
- [ ] Em automações longas via gateway, usar scripts curtos gravados por arquivo. Evitar heredocs grandes que disparam `obfuscation-detected`

## 🟢 Backlog

### Bidspark — Evolução
- [ ] Validar eficácia com dados reais (Amazon Ads) antes de abrir pra test users
- [ ] ML Ads automation — completar desenvolvimento

### Canguu
- [ ] Retomar desenvolvimento quando Pedro abrir janela
- [ ] Definir stack do módulo de atendimento

### Sistemas Internos
- [ ] Revisar repos "a classificar" (gb-link-hub, leadflow-crm-sync, morning-brief, etc.)
