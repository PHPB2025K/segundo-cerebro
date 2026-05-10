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

_Atualizado: 2026-05-09_

## 🔴 Prioridade Alta

### Estoque Budamix
- [ ] Retomar deploy em produção: VPS sem credencial GitHub, `git fetch` falhou 403. Recomendação: Deploy Key SSH read-only; depois reset/build/restart/smoke com backup e hash `.env`.
- [ ] Fechar PR1+PR2+PR3a em produção e validar visualmente: radio cards, default Venda/Compra, Devolução em entrada, autocomplete `914`/`KIT4YW800SQ_T`.
- [ ] Depois do deploy/cadastro: desenhar PR4 kits/BOM, pois 75% dos erros reais recentes são “Estoque insuficiente”.

### Social Studio
- [ ] Social Studio Reborn Fase C C2: página `/admin/social/conta` (status conta, botão OAuth, callback handler).
- [ ] Social Studio Reborn C3: aguardar/guia Pedro nos pré-requisitos Meta Developers + `META_APP_ID`/`META_APP_SECRET` antes de implementar callback real.
- [ ] Social Studio Reborn C4-C8: publicação Meta real com trava `TESTE INTERNO`, UI pós-publicação, refresh token, smoke final e PR.
- [ ] Social Studio Reborn Fase D: métricas/dashboard após Fase C.

### Canggu
- [ ] Corrigir type TS pré-existente em `_shared/evolution-api.ts` (`EvolutionMessageContent` vs `EvolutionMessageData`).
- [ ] Atualizar GitHub Actions Node 20 → 24 antes de 16/09/2026.
- [ ] Estender ajuste de tom para `process-message`/WhatsApp se Pedro quiser equalizar a Ana fora do ML.

### Bidspark — Segurança
- [ ] Remover credenciais do CLAUDE.md — Client ID + Secret em plain text no Amazon Ads.
- [ ] Trocar ambiente para produção — `AMAZON_ADS_ENVIRONMENT=production` antes de otimizações reais.
- [ ] Suite mínima de testes nos caminhos que mexem com dinheiro.

### Infra OpenClaw / Agentes
- [ ] Fisco/OpenClaw — diagnosticar bloqueio de `sessions_spawn` com `agentId=fisco` retornando `allowed: none`.

## 🟡 Prioridade Média

### Atlas Finance
- [ ] Relatório de fluxo de caixa, DRE e balanço quebrados — retomar quando Pedro priorizar.

### SimulImport
- [ ] Testes extensivos, melhorias de UX e production ready.

## 🟢 Backlog

- [ ] Revisar repos “a classificar” quando virar frente.
