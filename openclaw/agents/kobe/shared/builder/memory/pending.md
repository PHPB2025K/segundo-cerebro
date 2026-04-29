# Pendências — Builder

_Atualizado: 2026-04-28_

## 🔴 Prioridade Alta

### Budamix E-commerce / Blog / Social Studio
- [ ] Social Studio — QA autenticado do preview: criar/listar/arquivar ideia, geração de copy, editor manual, render PNG e wizard.
- [ ] Social Studio — decidir merge/deploy para produção da branch `feat/social-studio-phase2` após QA.
- [ ] Blog/N8N — remover service role hardcoded do WF4 e mover para credential/env do N8N.
- [ ] Budamix E-commerce — alinhar `main` local ahead 2 com `origin/main` antes da próxima entrega em produção.
- [ ] Vercel Preview — configurar envs públicas de Preview no dashboard ou padronizar deploy CLI com envs explícitas.

### Bidspark — Segurança
- [ ] Remover credenciais do CLAUDE.md — Client ID + Secret em plain text no Amazon Ads.
- [ ] Trocar ambiente para produção — `AMAZON_ADS_ENVIRONMENT=production` no `.env` antes de ativar otimizações reais.

### Bidspark — Testes
- [ ] Suite mínima de testes — zero testes atualmente. Implementar testes nos caminhos que mexem com dinheiro (bids, budgets, guardrails).

## 🟡 Prioridade Média

### Atlas Finance — Relatórios
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
