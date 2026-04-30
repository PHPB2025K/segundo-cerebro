# Pendências — Builder

_Atualizado: 2026-04-29_

## 🔴 Prioridade Alta

### Budamix E-commerce / Blog / Social Studio
- [ ] Social Studio — QA autenticado do preview completo até Fase 5: criar ideia, gerar copy IA, editar carrossel, adicionar/reordenar slides, renderizar PNG e abrir asset final.
- [ ] Social Studio — decidir merge/deploy produção da branch/estado atual após QA.
- [ ] Social Studio — executar refactor wizard step-by-step (`/admin/social`, `/admin/social/new`, `/admin/social/:postId?step=...`) conforme briefing consolidado.
- [ ] Blog Budamix — inspeção visual manual do post de teste `35873e72-a3ff-4ad9-9ea4-1216c05ecec0` e cleanup após aprovação.
- [ ] Blog WF0 — polir payload de resposta (`pillar_focus` aparece null no response, embora o fluxo funcione internamente).
- [ ] Vercel Preview — configurar envs públicas de Preview no dashboard ou padronizar deploy CLI com envs explícitas.
- [ ] Vercel Token Budamix E-commerce — completar item 1Password para Kobe ter deploy autônomo.

### Budamix Central
- [ ] Full — Etapa 2D `sku_mapping` fallback para 8 SKUs já mapeados, com atenção ao `quantity_multiplier`.
- [ ] Full — Etapa 1E monitoramento Shopee: alerta se alguma conta passar de 6h sem sync.
- [ ] Full — validação cruzada ML Full e Amazon FBA equivalente à Shopee 1D.
- [ ] Full — após analistas cadastrarem SKUs zerados, rodar `sync-costs.py` e validar `zero_cost < 25`, custo real ≥ R$145k.

### Bidspark — Segurança/Testes
- [ ] Remover credenciais do CLAUDE.md — Client ID + Secret em plain text no Amazon Ads.
- [ ] Trocar ambiente para produção — `AMAZON_ADS_ENVIRONMENT=production` no `.env` antes de ativar otimizações reais.
- [ ] Suite mínima de testes — zero testes atualmente. Implementar testes nos caminhos que mexem com dinheiro (bids, budgets, guardrails).

## 🟡 Prioridade Média

### Atlas Finance
- [ ] Relatório de fluxo de caixa — quebrado, Pedro precisa.
- [ ] DRE — quebrado.
- [ ] Balanço — quebrado.
- [ ] Retomar quando Pedro priorizar.

### SimulImport
- [ ] Testes extensivos.
- [ ] Melhorias de UX.
- [ ] Production ready para primeiros test users.

## 🟢 Backlog

- [ ] Bidspark — validar eficácia com dados reais antes de abrir para test users.
- [ ] Bidspark — completar ML Ads automation.
- [ ] Canguu — retomar desenvolvimento quando Pedro abrir janela.
- [ ] Revisar repos a classificar.
