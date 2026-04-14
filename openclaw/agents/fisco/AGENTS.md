---
title: "AGENTS"
created: 2026-04-14
type: team-config
agent: fisco
status: active
tags:
  - agent/fisco
---

# AGENT.md — Arquitetura Técnica do Agente Fisco

---

## Integração: Bling (ERP)

| Item | Detalhe |
|------|---------|
| API | Bling API v3 |
| Credenciais | 1Password ("Bling API - GB Comércio" e "Bling API - Filial") |
| Escopo | Consultar pedidos, emitir NF-e, gerenciar estoque, consultar extrato |

---

## 5 Módulos Core

### A — Emissão de NF-e Interna
- Gerar rascunhos de NF-e para transferências e vendas internas.
- Validar impostos e NCMs conforme regras da FOUR Contabilidade.
- **Trigger:** Sob demanda ou após distribuição de estoque.

### B — Distribuição de Estoque (Cross-CNPJ)
- Analisar volume de vendas por CNPJ.
- Sugerir transferências entre Matriz e Filial para balancear faturamento.
- Gerar documentos de transferência.

### C — Conciliação Fiscal
- Cruzar vendas dos marketplaces (ML, Shopee, Amazon) com NFs emitidas.
- Identificar pedidos sem nota ou notas com valores divergentes.

### D — Monitoramento Simples Nacional
- Acompanhar faturamento acumulado (RBT12).
- Alertar proximidade de mudança de faixa ou estouro do limite (R$ 4.8M).

### E — Tax Rules Engine
- Manter base de regras tributárias atualizada em `config/tax-rules.json`.
- Validar alíquotas de ICMS/ST por estado.

---

## Crons

| Cron | Frequência | Modelo | Ação |
|------|-----------|--------|------|
| Bling Token Refresh | Cada 5h | Haiku | Garante que tokens OAuth não expirem |
| Monitor Simples | Semanal Seg 10h | Sonnet | Checa faturamento acumulado |
| Conciliação | Diário 02h | Sonnet | Cruza vendas vs notas |
