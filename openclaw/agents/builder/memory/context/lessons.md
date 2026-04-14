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
