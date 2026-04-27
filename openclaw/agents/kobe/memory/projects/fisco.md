---
title: "fisco"
created: 2026-04-26
type: memory-project
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - project
---
# Projeto: Agente Fisco (Faturamento)

_Criado: 2026-03-28 | Status: Fase 1 — Fundação_

---

## Resumo

Quarto agente do time Kobe. Automatiza o fluxo fiscal interno da GB Importadora: distribuição de estoque entre CNPJs, emissão de NFs de transferência e venda interna via API Bling, conciliação fiscal e monitoramento de limites do Simples Nacional.

## Decisões Registradas

- 2026-03-28: Pedro aprovou arquitetura com 5 módulos (A-E), fases 1-4
- 2026-03-28: Bling Plano Mercúrio confirmado — API v3 disponível
- 2026-03-28: Contador = FOUR Contabilidade (Suellen) — valida regras fiscais
- 2026-03-28: Fisco consome dados do Trader (sem duplicar integrações de marketplace)
- 2026-03-28: Fase 1 em modo draft (gera NF mas não emite)
- 2026-03-28: TTD 409: 2,6% por 36 meses (início 12/01/2026), depois 1%
- 2026-03-28: Regras fiscais configuráveis em JSON, não hardcoded
- 2026-03-28: Nome do agente: Fisco

## Bloqueios Atuais

- Integração Bling API v3 não iniciada (Builder, Fase 1)
- Credenciais OAuth do Bling ainda não registradas no 1Password
- Validação formal das regras fiscais pela Suellen pendente

## Arquivos

- `shared/fiscal/AGENT.md` — arquitetura completa
- `shared/fiscal/config/tax-rules.json` — regras fiscais configuráveis
- `shared/fiscal/memory/` — memória do agente (a criar)

## Fases

| Fase | Status | Notas |
|------|--------|-------|
| 1 - Fundação (Bling API + config) | 🟡 Arquitetura pronta, integração pendente | Builder precisa implementar |
| 2 - Motor de Distribuição | 🔴 | Depende do Trader fornecer dados |
| 3 - Emissão de NFs | 🔴 | Modo draft primeiro |
| 4 - Conciliação + Monitor | 🔴 | Últimos módulos |


## Ver também

- [[openclaw/agents/kobe/IDENTITY]] — agente proprietário
- [[openclaw/agents/kobe/SOUL]] — princípios estáveis
- [[memory/context/business-context]] — contexto operacional
- [[business/importacao/estrategia-fiscal-gb]] — referência canônica detectada no conteúdo
- [[meta/mocs/MOC - Token Management]] — referência canônica detectada no conteúdo
