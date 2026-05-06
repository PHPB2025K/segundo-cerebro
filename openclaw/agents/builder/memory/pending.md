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

_Atualizado: 2026-05-05_

## 🔴 Prioridade Alta

### Estoque Budamix
- [ ] Retomar deploy em produção: VPS sem credencial GitHub, `git fetch` falhou 403. Recomendação: Deploy Key SSH read-only; depois reset/build/restart/smoke com backup e hash `.env`.
- [ ] Fechar PR1+PR2+PR3a em produção e validar visualmente: radio cards, default Venda/Compra, Devolução em entrada, autocomplete `914`/`KIT4YW800SQ_T`.
- [ ] Depois do deploy/cadastro: desenhar PR4 kits/BOM, pois 75% dos erros reais recentes são “Estoque insuficiente”.

### Social Studio
- [ ] Corrigir bug `cover-numeric`: `SlideRenderer` não passa `imageUrl` para `CoverNumeric` e `needsImage()` diverge no Editor.
- [ ] PR3 Social Studio: modo manual default + ImageGenerationDialog + prompt editável + foto de referência + geração individual em slide vazio.
- [ ] Fase 5 cold start/render: se Pedro priorizar hardening, desenhar container warm/render service para reduzir cold start Puppeteer de 18,6s.

### Canggu
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
