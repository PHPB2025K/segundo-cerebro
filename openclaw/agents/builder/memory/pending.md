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

_Atualizado: 2026-05-28_

## 🔴 Prioridade Alta

### Estoque Budamix
- [ ] Retomar deploy em produção: VPS sem credencial GitHub, `git fetch` falhou 403. Recomendação: Deploy Key SSH read-only; depois reset/build/restart/smoke com backup e hash `.env`.
- [ ] Fechar PR1+PR2+PR3a em produção e validar visualmente: radio cards, default Venda/Compra, Devolução em entrada, autocomplete `914`/`KIT4YW800SQ_T`.
- [ ] Depois do deploy/cadastro: desenhar PR4 kits/BOM, pois 75% dos erros reais recentes são “Estoque insuficiente”.

### Social Studio Reborn
- [ ] Fase C C2: construir `/admin/social/conta` com status de conta, OAuth e callback handler.
- [ ] Fase C C3-C8: publicação real via Meta Graph após Pedro configurar App Meta e secrets.
- [ ] Fase D: métricas Instagram + dashboard + export CSV.
- [ ] Preservar branches antigas até 05/06/2026 antes de avaliar delete.

### Canggu
- [ ] Corrigir fire-and-forget do `webhook-whatsapp` com `EdgeRuntime.waitUntil()` ou fila persistente para evitar cancelamento silencioso do `process-message`.
- [ ] Manter acesso ao repo canônico `PHPB2025K/canguu` após Pedro voltar privacidade do repo; garantir que VPS/token consegue patch/commit/deploy quando necessário.
- [ ] Auditar rotas Supabase que postam no Mercado Livre para garantir guard determinístico contra frases proibidas em todas.
- [ ] Atualizar GitHub Actions Node 20 → 24 antes de 16/09/2026.
- [ ] Estender ajuste de tom para `process-message`/WhatsApp se Pedro quiser equalizar a Ana fora do ML.

### Bidspark — Segurança
- [ ] Remover credenciais do CLAUDE.md — Client ID + Secret em plain text no Amazon Ads.
- [ ] Trocar ambiente para produção — `AMAZON_ADS_ENVIRONMENT=production` antes de otimizações reais.
- [ ] Suite mínima de testes nos caminhos que mexem com dinheiro.

### Mission Control
- [ ] Ativar Daily Sales Pipeline Panel em produção com restart controlado e smoke test da página/APIs.
- [ ] Implementar 11 módulos restantes: Tasks, Agents detail, Logs, Terminal, Git, Workflows, Search, Analytics, Settings, Calendar e About/Actions.
- [ ] Implementar n8n usage tracking em `/costs` com saveDataSuccessExecution, coletor 15min e pricing real.

### Infra OpenClaw / Agentes
- [ ] Fisco/OpenClaw — diagnosticar bloqueio de `sessions_spawn` com `agentId=fisco` retornando `allowed: none`.

## 🟡 Prioridade Média

### Atlas Finance
- [ ] Relatório de fluxo de caixa, DRE e balanço quebrados — retomar quando Pedro priorizar.

### SimulImport
- [ ] Testes extensivos, melhorias de UX e production ready.

## 🟢 Backlog

- [ ] Revisar repos “a classificar” quando virar frente.
