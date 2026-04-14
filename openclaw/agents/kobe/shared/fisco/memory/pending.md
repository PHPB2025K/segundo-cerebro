---
title: "pending"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Pendências — [[openclaw/agents/fisco/IDENTITY|Fisco]]

_Atualizado: 2026-04-01_

## 🔥 URGENTE

- [ ] **Deletar NFs de teste** — Filial: 011–027 (17 NFs rascunho). Matriz: 611–616 (6 NFs rascunho). Pedro deleta manualmente no Bling ou Fisco tenta via DELETE /nfe/{id}
- [ ] **Bug refresh token Filial** — 403 "empresa inativa" no refresh automático. Re-autorizar manualmente quando expirar. Investigar com suporte Bling.

## 🟡 MÉDIO PRAZO

- [ ] **product-packaging.json** — Preencher pesos e volumes de todos os SKUs. Bloqueador para próximas NFs (Bling não calcula peso automaticamente)
- [ ] **Faturamento B2B março** — Levantar parcela B2B da Filial para calibrar o Motor de Distribuição (Módulo A) corretamente. Atualmente usamos 100% varejo.
- [ ] **Automatizar detecção de excedente** — Lógica de cruzar NFs transferência vs vendas deve ser codificada no Módulo C do Fisco
- [ ] **Contatos IDs Bling Matriz** — Registrar IDs dos 3 CNPJs no Bling da Matriz (já existem, mas não foram mapeados aqui)

## 📋 BACKLOG

- [ ] **NFs de entrada** — Registrar no Bling as NFs de importação das container 598/600 como entradas
- [ ] **Monitor Simples Nacional** — Módulo E: acompanhar faturamento acumulado 2026 por CNPJ vs teto R$4,8M/ano
