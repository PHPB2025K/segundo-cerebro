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

_Atualizado: 2026-06-08_

## 🔴 Prioridade Alta

### Estoque Budamix
- [ ] Retomar deploy em produção: VPS sem credencial GitHub, `git fetch` falhou 403. Recomendação: Deploy Key SSH read-only; depois reset/build/restart/smoke com backup e hash `.env`.
- [ ] Fechar PR1+PR2+PR3a em produção e validar visualmente: radio cards, default Venda/Compra, Devolução em entrada, autocomplete `914`/`KIT4YW800SQ_T`.
- [ ] Após autorização, aplicar aliases seguros do mapeamento retroativo de 07/06 e reprocessar só esses movimentos: `CK4742_B2` → `CK4742_B`, `914C_B2` → `914C_B`, `KITIMB501P_T` → `IMB501P_T`.
- [ ] Validar antes de qualquer automapeamento: `XCP004` → possível `COLORS170_B`; `KFJ003` sem canônico seguro.
- [ ] Depois do deploy/cadastro: desenhar PR4 kits/BOM, pois a maioria dos erros reais recentes é “Estoque insuficiente”.
- [ ] Auditoria Full: validar build/restart/smoke em produção da nova aba padrão de Estoque > Full antes de considerar entregue em produção.
- [ ] Auditoria Full: confirmar que o sync externo da planilha ENVIOS FULL está ativo e populando envios recentes; sem isso, recomendações podem sair subestimadas.
- [ ] Auditoria Full: monitorar filtro de vendas Full por logistic type no ML para evitar média inflada com vendas não-Full quando o campo vier vazio.
- [ ] Auditoria Full: revisar SKUs marcados sem match no inventário Full antes de qualquer correção automática de planilha/cadastro.
- [ ] Preencher alocação de receita por componente no fechamento de estoque; CMV seller de 03/06 foi corrigido, mas receita da camada de componentes ainda está nula.
- [ ] Tratar fila residual de divergências por saldo real insuficiente/entrada física não registrada: `YW1520RC`, `YW1050RC`, `CAC250P`, `CAC250AZ`, `TL250P`, `CAR200B`, `CAR200R`; não baixar negativo sem prova operacional.

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
- [ ] Validar em produção a página dedicada Daily Sales Shopee antes de ativar cron: overview das 3 contas, drill-down de camadas e API própria.
- [ ] Implementar 11 módulos restantes: Tasks, Agents detail, Logs, Terminal, Git, Workflows, Search, Analytics, Settings, Calendar e About/Actions.
- [ ] Implementar n8n usage tracking em `/costs` com saveDataSuccessExecution, coletor 15min e pricing real.

### Infra OpenClaw / Agentes
- [ ] Fisco/OpenClaw — diagnosticar bloqueio de `sessions_spawn` com `agentId=fisco` retornando `allowed: none`.

### Budamix Facebook Page / Meta Graph
- [ ] Rotacionar App Secret do Meta exposto em chat/contexto operacional e atualizar os runtimes que dependem do app compartilhado.
- [ ] Ajustar website público da Página Budamix para HTTPS, preencher descrição longa e tentar configurar vanity URL `/budamix` manualmente via Meta Business Suite.

## 🟡 Prioridade Média

### Atlas Finance
- [ ] Relatório de fluxo de caixa, DRE e balanço quebrados — retomar quando Pedro priorizar.

### SimulImport
- [ ] Testes extensivos, melhorias de UX e production ready.

### Daily Sales Shopee
- [ ] Manter Fase 1 em standby até lapidação: aplicar regra de densidade nas camadas tática/operacional/forense, rodar smokes nas contas 2 e 3, resolver gaps de fetcher e só então avaliar cron 07:00 BRT.

## 🟢 Backlog

- [ ] Revisar repos “a classificar” quando virar frente.
