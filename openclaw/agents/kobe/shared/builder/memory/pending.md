# Pendências — Builder

_Atualizado: 2026-05-01_

## 🔴 Prioridade Alta

### Budamix Central
- [ ] Estoque Fase 1.5 — aguardar validação visual do Pedro.
- [ ] Estoque Fase 2 — movimentações, role `operator`, contramov, sync app→planilha 2min.
- [ ] Estoque — investigar SKU duplicado na aba ESTOQUE.
- [ ] Full — Etapa 1E monitoramento Shopee: alerta se alguma conta passar de 6h sem sync.
- [ ] Full — validação cruzada ML Full e Amazon FBA equivalente à Shopee 1D.

### Canggu
- [ ] Segurança B1 — service_role/JWT tracked, ghost function, CORS, verify_jwt, secrets legados.
- [ ] Resiliência B3 — retry LLM, UNIQUE `whatsapp_message_id`, dedup, fallback textual.
- [ ] Prompt Ana — instruções para sticker/localização/contato.
- [ ] Troca da senha temporária do admin pelo Pedro (sem registrar o valor em pendências).

### Ponto Certo / RH
- [ ] Deploy produção do módulo Conversas RH se ainda estiver só local.
- [ ] Smoke mobile/desktop do admin Conversas RH em produção.

### Budamix E-commerce / Blog / Social Studio
- [ ] Social Studio — QA autenticado do preview completo até Fase 5.
- [ ] Social Studio — decidir merge/deploy produção após QA.
- [ ] Social Studio — executar refactor wizard step-by-step.
- [ ] Blog Budamix — inspeção visual manual do post de teste e cleanup.
- [ ] Blog WF0 — polir payload de resposta `pillar_focus`.
- [ ] Vercel Preview — configurar envs públicas de Preview ou deploy CLI com envs explícitas.
- [ ] Vercel Token Budamix E-commerce — completar item 1Password para rollback/hotfix CLI.

### Bidspark — Segurança/Testes
- [ ] Remover credenciais do CLAUDE.md — Client ID + Secret em plain text no Amazon Ads.
- [ ] Trocar ambiente para produção — `AMAZON_ADS_ENVIRONMENT=production` no `.env` antes de ativar otimizações reais.
- [ ] Suite mínima de testes — zero testes atualmente. Implementar testes nos caminhos que mexem com dinheiro.


### Infra OpenClaw / Agentes
- [ ] Fisco/OpenClaw — diagnosticar bloqueio de sessions_spawn com `agentId=fisco` retornando `allowed: none`; validar policy/runtime/gateway e restaurar roteamento direto.

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
- [ ] Revisar repos a classificar.
