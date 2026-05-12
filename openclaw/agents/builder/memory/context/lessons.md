---
title: "lessons"
created: 2026-04-14
type: agent
agent: builder
status: active
tags:
  - agent/builder
---

# Lições — Builder

_Erros e aprendizados. [ESTRATÉGICA] = permanente, [TÁTICA] = expira 30 dias._

### 2026-03-17 — Zero testes em automação de ADS é inaceitável [ESTRATÉGICA]
**Contexto:** Auditoria completa do Bidspark revelou arquitetura sólida mas zero testes unitários.
**Lição:** Qualquer projeto que mexe com dinheiro real (bids, budgets) precisa de testes de regressão antes de produção. Sem testes, uma mudança silencia o guardrail.
**Ação:** Fase 1 do plano de ação: implementar suite mínima de testes antes de produção.

### 2026-03-17 — Credenciais em CLAUDE.md — risco de segurança [ESTRATÉGICA]
**Contexto:** Auditoria encontrou Client ID e Client Secret em texto puro no CLAUDE.md do Amazon Ads (Bidspark).
**Lição:** Arquivos de contexto de IA (CLAUDE.md, .cursorrules, etc.) são frequentemente commitados e lidos por LLMs. NUNCA colocar credenciais neles.
**Ação:** Alertar Pedro para remover. Usar 1Password ou env vars exclusivamente.

### 2026-03-17 — Bidspark está em sandbox, não em produção [TÁTICA]
**Contexto:** CLAUDE.md do Amazon Ads aponta para sandbox environment.
**Lição:** Antes de ativar otimizações automáticas com dinheiro real: confirmar que `AMAZON_ADS_ENVIRONMENT=production` no `.env`.
**Expira:** 2026-04-17

### 2026-05-05 — Provar rota real de deploy antes de refatorar produção [ESTRATÉGICA]
**Contexto:** Estoque Budamix recebeu PRs no repo novo, mas produção ainda rodava build rsync histórico na VPS sem ponte GitHub→VPS.
**Lição:** Antes de anunciar correção em produção, validar remote canônico, CI/deploy script, commit servido e smoke no domínio real. Push sem ponte de deploy é só backup.

### 2026-05-05 — Supabase Edge Functions precisam de auto-deploy [ESTRATÉGICA]
**Contexto:** Canggu teve regressões por funções stale em produção.
**Lição:** Projeto com Edge Functions críticas deve ter GitHub Actions ou checklist obrigatório de deploy por função, especialmente quando `_shared/` muda.

### [ESTRATÉGICA] Guard final antes de API externa é obrigatório em rotas legadas (2026-05-11)
**Lição:** Prompt e banco não bastam quando há Edge Function legada enviando resposta externa. Toda rota que chama ML/WhatsApp/marketplace precisa de validação determinística imediatamente antes do POST.

### [TÁTICA] Evolution/RH: normalizar `@lid` evita cegueira de inbound (2026-05-11)
**Lição:** Webhook/poller/debounce de WhatsApp precisam aceitar `@lid`, `@c.us` e `@s.whatsapp.net`, resolver por pushName/aliases e logar desconhecidos em vez de descartar.
**Expira:** 2026-06-10

### [TÁTICA] Amazon Orders: filtrar FBA removal no ingest (2026-05-11)
**Lição:** Pedidos de remoção FBA entram no feed como orders, mas não são vendas. Filtrar no sync por `SalesChannel=Non-Amazon`, `FulfillmentChannel=AFN`, datas dummy 1995/S01 e preservar auditoria ao cancelar legados.
**Expira:** 2026-06-10
