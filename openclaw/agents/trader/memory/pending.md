---
title: "pending"
created: 2026-04-14
type: agent
agent: trader
status: active
tags:
  - agent/trader
---

# Pendências — Trader

_Atualizado: 2026-04-06_

## 🔴 Prioridade Alta

### Consolidado Financeiro — Gaps
- [ ] **Margem por produto** — cruzar curva ABC com preço de custo (planilha estoque Google Sheets)
- [ ] **Fluxo de caixa** — timeline de liquidação real por plataforma
- [ ] **Alertas automáticos** — margem < 15% → 🔴, taxa acima da média → ⚠️
- [ ] **Ads no breakdown** — puxar gasto de ads (ML Ads API + Amazon Ads) como linha de custo

### Relatório de Performance — Connectors Faltantes
- [ ] Connector Amazon (SP-API: orders, items, seller metrics)
- [ ] Connector Shopee (3 contas: orders, items, shop metrics)
- [ ] Todas as 9 seções cobrindo 3 plataformas
- [ ] HTML no mesmo design system do financeiro

### Base Ana — Links de Marketplace
- [ ] Amazon segue como prioridade #1 na base Ana — ML avançou para 25/61 e Shopee para 51/61, mas Amazon ainda está sem cobertura confirmada
- [ ] Casos manuais restantes do ML e Shopee — revisar quando o tema voltar

## 🟡 Prioridade Média

### Shopee
- [ ] budamix-store: atualizar SKUs via API (token estava expirado em 21/03)
- [ ] Estratégia de pricing Shopee (margens muito menores que ML)

### Análise de Concorrência
- [ ] Completar análise concorrência ML (case pote 1520ml kit 2 — parcial, 1 termo)
- [ ] Expandir para 5+ termos conforme metodologia da skill

## 🟢 Backlog

- [ ] Monitoramento automático de taxas ML (cron semanal ativo)
- [ ] Monitoramento automático de taxas Shopee (cron semanal ativo)
- [ ] Tendência mês a mês no consolidado (a partir de abril — precisa de 2+ meses)