---
title: "MOC — Importação GB"
created: 2026-05-21
type: moc
status: active
tags:
  - moc
  - importacao
  - business/importacao
  - gb-import-hub
---

# MOC — Importação GB

> Hub do ciclo completo de importação GB Importadora: regra fiscal canônica, sistema de gestão (GB Import Hub), planejamento estratégico (flywheel/cadência), SOPs operacionais e aprendizados técnicos.

---

## Empresa e contexto

| Dado | Valor |
|---|---|
| Razão Social | GB Importadora |
| Marca | Budamix |
| Sourcing | Yiwu, China (2 viagens, Canton Fair) |
| CNPJs operacionais | 6 |
| Matriz fiscal | Itajaí-SC (TTD 409, ICMS benefício) |
| Operação física | Pedreira-SP |
| Portos | Itajaí, Itapoá |
| Trading | Open Trade (ICMS 4%) |
| Contadora responsável | Suellen / FOUR Contabilidade |

## Regra fiscal canônica (v2.1)

> Fonte de verdade: [[business/importacao/estrategia-fiscal-gb]]
>
> **Mudança 24/04/2026:** Transferência Matriz→Filial **sem destaque de ICMS** (LC 87/96 §4º + LC 204/2023 + Conv. ICMS 109/2024 + Ajuste SINIEF 33/2024) e **IPI suspenso** (RIPI art. 43 X).

1. **Transferência Matriz→Filial = 90% fixo** (CFOP 6.152) — sem destaque ICMS, IPI suspenso
2. **10% permanece contábil na Matriz (SC)** — B2B direto com TTD 409 (ICMS efetivo 2,6%)
3. **Estoque físico 100% vai para Pedreira-SP**
4. **Reserva B2B residual da Filial (~4%)** é dinâmica
5. **Proporções dos CNPJs Simples** são dinâmicas (% B2B últimos 3 meses)
6. **Margem interna fixa 5%** (Filial→Simples = custo × 1.05)

## Estratégia e cadência

- [[projects/planejamento-importacao-2026]] — dimensionamento de cadência sob tese do flywheel (lotes de 4 × GB25011, 8 meses de simulação, método essencialista)
- Status atual: em recalibração para lotes de 2 a cada ~40-45 dias com 3 lotes vivos simultâneos
- Próximo deadline: balanço 70% GB25011 R$ 71.419 em 24/05/2026

## Sistema central

[[projects/gb-import-hub]] — URL https://import.budamix.com.br

| Schema | Tabela | O que guarda |
|---|---|---|
| Logístico | `containers` | ID, status (production→maritime→customs→road→finished) |
| Logístico | `vessel_tracking`, `container_milestones`, `tracking_alerts` | Terminal49 + Mapbox |
| Financeiro | `finance_pagamentos` | Sinal 30%, Numerário, 70% Balanço |
| Financeiro | `finance_numerario_itens` | Itens individuais por pagamento (PNI) |
| Conferência | `conferencias_numerario`, `conferencias_comunicacoes` | Validação custos |
| Referência | `referencias_mercado`, `referencias_ncm` | Precificação + NCM/tributos |
| Storage | `documents` | PDFs (Invoice, Packing List, BL, DI, XML, PNI) |

**17 Edge Functions** incluindo `extract-import-document`, `calculate-tax-references`, `fetch-vessel-position`, `terminal49-search/associate/register-webhook`.

## Ciclo do container (base empírica GB25011)

| Marco | Dia | Evento |
|---|:---:|---|
| Pedido + sinal 30% | D+0 | Pagamento upfront 30% |
| Balanço 70% | D+50 | No embarque |
| Chegada + numerário | D+85 | Container atraca |
| Nacionalização | D+100 | DI emitida |
| Janela de venda | D+100 a D+145 | Estoque disponível em todos os canais |

## Containers ativos (snapshot)

| Container | Status logístico | Status financeiro |
|---|:---:|:---:|
| GB25007 | finished | A preencher |
| GB25008 | finished | Container dedicado a kits Skiway |
| GB25009 | finished | Container dedicado IMB501 (Yiwu Lotus) |
| GB25010 | finished | 30% + numerário R$64.136,40 + 70% R$81.750 |
| GB25011 | road→finished | Numerário pago, 70% R$71.419 vence **24/05/2026** |
| GB26001 | A preencher | — |
| GB26002 | A preencher | — |

## SOPs operacionais

- [[automacoes/sops/abrir-nova-importacao]] — abertura no Hub (containers, finance_pagamentos, documents, tracking, DI)
- [[automacoes/sops/atualizar-pagamento-importacao]] — registro de pagamentos
- [[skills/gb-import-hub/SKILL]] — skill que executa via API

## Integração fiscal (NF transferência)

[[projects/financeflow]] + [[openclaw/agents/fisco/IDENTITY|Fisco]] emitem NF de transferência Matriz→Filial via Bling Matriz.

Aprendizados consolidados em [[knowledge/concepts/bling-api-v3-aprendizados]]:
- PUT `/nfe/{id}` substitui inteiro, não faz patch
- `cfop` e `impostos.*` no payload são ignorados (Bling usa Natureza de Operação cadastrada)
- Código do SKU em NF = código SIMPLES, sem prefixo CX
- Busca por `?codigo=` exato vs `?pesquisa=` textual
- Rate limit 3 req/s por conta

## Tracking marítimo

| Serviço | Função |
|---|---|
| Terminal49 | Tracking de embarcações via Edge Functions |
| Mapbox | Visualização geográfica (`get-mapbox-token`) |

## Índices relacionados

- [[business/importacao/_index]] — pasta `~/Documents/01-Importacao/`
- [[business/empresa/_index]] — Manuais (TTD 409, Full ML, Full Amazon)

## MOCs relacionados

- [[meta/mocs/MOC - Pedidos de Venda Atacado]] — pipeline B2B atacado pós-nacionalização
- [[meta/mocs/MOC - Taxas e Precificacao]] — fees marketplace para precificação
- [[meta/mocs/MOC - Token Management]] — OAuth Bling Matriz/Filial
- [[meta/mocs/MOC - Supabase Ecosystem]] — projeto Supabase do Hub (`ocxvwwaaqqxecmzhfxhb`)

---

*Criado: 2026-05-21 — Fase 4 de densificação do vault. Consolida os 6 hubs concorrentes que dispersavam a leitura sobre importação.*
