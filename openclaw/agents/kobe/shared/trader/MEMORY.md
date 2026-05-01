---
title: "MEMORY"
created: 2026-04-26
type: memory
agent: trader
status: active
tags:
  - agent/trader
---
# MEMORY.md — Trader

_Último update: 2026-05-01 04:00 BRT (Consolidação Profunda)._

---

## Índice de arquivos

- [[openclaw/agents/kobe/shared/trader/SOUL|SOUL]]
- [[openclaw/agents/kobe/shared/trader/IDENTITY|IDENTITY]]
- [[openclaw/agents/kobe/shared/trader/memory/context/decisions|Decisões]]
- [[openclaw/agents/kobe/shared/trader/memory/context/lessons|Lições]]
- [[openclaw/agents/kobe/shared/trader/memory/pending|Pendências]]

### Sessões preservadas
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-05|Sessão 2026-04-05]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-06|Sessão 2026-04-06]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-07|Sessão 2026-04-07]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-08|Sessão 2026-04-08]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-09|Sessão 2026-04-09]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-10|Sessão 2026-04-10]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-11|Sessão 2026-04-11]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-12|Sessão 2026-04-12]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-13|Sessão 2026-04-13]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-14|Sessão 2026-04-14]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-15|Sessão 2026-04-15]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-16|Sessão 2026-04-16]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-17|Sessão 2026-04-17]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-18|Sessão 2026-04-18]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-19|Sessão 2026-04-19]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-20|Sessão 2026-04-20]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-22|Sessão 2026-04-22]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-23|Sessão 2026-04-23]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-24|Sessão 2026-04-24]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-25|Sessão 2026-04-25]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-26|Sessão 2026-04-26]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-27|Sessão 2026-04-27]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-28|Sessão 2026-04-28]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-29|Sessão 2026-04-29]]
- [[openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-30|Sessão 2026-04-30]]

---

## Quem sou

Especialista sênior de marketplaces da GB Importadora. Opero Mercado Livre, Amazon BR e Shopee. Coordenado pelo Kobe; resultado sempre passa pelo Kobe antes do Pedro.

## Regras invioláveis

- **QA financeiro:** extrato parcial nunca entra como fechamento completo.
- **Horários:** tudo em BRT.
- **Custo/margem:** sempre validar fonte canônica antes de recomendar preço, margem ou fechamento.
- **Plataformas:** ML + Amazon + Shopee 3 contas; CNPJ×marketplace segue decisão permanente.

## Estado real — Consolidação Profunda 2026-05-01

### Mudanças materiais dos últimos 15 dias
- Importação 2026 validou que Shopee é canal dominante em vários SKUs e que ruptura/ranking precisam ser analisados por canal, não só consolidado.
- Budamix Central Full fechou `zero_cost=0` após corrigir fonte da planilha de precificação, matching multi-fonte e remoção/filtro de fantasmas Amazon.
- Planilha oficial de precificação passou a ser `1u74a...`; planilha `1dUoZ...` é legado/operacional e não deve ser usada para custo de anúncio.
- Módulo Estoque passou a expor Full/Físico/Consolidado; total de estoque ficou em torno de R$ 709k após parser BR corrigido.

### O que NÃO mudou
- Fechamento financeiro de março segue aberto por ads spend real.
- Validação defensiva ML Full/Amazon FBA e monitoramento Shopee 1E seguem pendentes.
- Links Amazon/base Ana e PCM001 seguem em backlog estagnado.

## Pendências prioritárias

1. Ads spend março por plataforma.
2. Refazer fechamento março com extratos completos + ads spend correto.
3. Validar ML Full/Amazon FBA com profundidade equivalente à Shopee.
4. Implementar healthcheck de sync Shopee 1E.
5. Manter margem por produto ligada ao custo real da planilha oficial.

---
_Consolidação Profunda 2026-05-01: sessões brutas de março removidas por já estarem consolidadas; índice reflete estado real pós-30/04._
