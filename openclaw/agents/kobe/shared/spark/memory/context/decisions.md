---
title: "decisions"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Decisões Permanentes — [[openclaw/agents/spark/IDENTITY|Spark]] v2.0

_Decisões do Pedro/Kobe que não mudam. Consultar SEMPRE antes de agir._
_Só o Pedro (via Kobe) pode adicionar, alterar ou revogar decisões aqui._

---

## Como usar este arquivo

1. **ANTES de qualquer ação:** verificar se existe decisão relevante aqui
2. **Se uma decisão aqui contradiz algo no playbook.md:** a decisão vence
3. **Para adicionar decisão:** apenas Kobe pode escrever. Spark pode sugerir, Kobe registra.
4. **Para revogar decisão:** Kobe registra como `[REVOGADA em DATA]` — não apaga.

---

## Arquitetura & Hierarquia

| Decisão | Data | Origem |
|---|---|---|
| Comunicação: Spark → Kobe → Pedro. NUNCA direto com Pedro. | 2026-03-20 | Pedro |
| Nível: L1 Observer. Todo output revisado pelo Kobe. | 2026-03-20 | Pedro |
| Modelo: GPT-5.5 via ChatGPT Pro para execução e estratégia do domínio ADS, alinhado ao restante do time. | 2026-04-25 | Pedro |
| Spark só se comunica com outros agentes quando Kobe autorizar explicitamente. | 2026-03-20 | Pedro |

## Budget & Financeiro

| Decisão | Data | Origem |
|---|---|---|
| Budget inicial: R$1.500/mês. | 2026-03-20 | Pedro |
| Limite de decisão autônoma: R$500. Acima disso, precisa aprovação. | 2026-03-20 | Pedro |
| Plataformas autorizadas: Meta Ads + Google Ads. | 2026-03-20 | Pedro |

## Operacional

| Decisão | Data | Origem |
|---|---|---|
| Execução de mudanças: NUNCA sem aprovação explícita do Kobe. | 2026-03-20 | Pedro |
| Learning Phase: Não mexer por 7-14 dias. Exceção: CPA >3x meta OU budget esgotando em <4h. | 2026-03-20 | Kobe |
| Scaling: Máximo 20% de aumento por vez, a cada 3-5 dias. | 2026-03-20 | Kobe |
| Naming convention: `[Plataforma]_[Objetivo]_[Público]_[Fase-Funil]_[Data]` | 2026-03-20 | Kobe |

## Relatórios & Comunicação

| Decisão | Data | Origem |
|---|---|---|
| Todos os relatórios entregues ao Kobe — nunca diretamente ao Pedro. | 2026-03-20 | Pedro |
| Duas versões quando para Pedro: técnica (registro) + negócio (repasse). | 2026-03-20 | Kobe |

---

## Marketplace Ads — Fechamento financeiro

| Decisão | Data | Origem |
|---|---|---|
| Shopee Ads oficial para DRE deve vir da plataforma Shopee Ads; Wallet API serve só para conciliação/alerta de recarga/débito. | 2026-05-01 | Pedro/Kobe |
| Amazon Ads Sponsored Products mensal via API é fonte oficial quando o report conclui com dados. | 2026-05-01 | Kobe |


## Amazon Ads — Otimização abril/2026

| Decisão | Data | Origem |
|---|---|---|
| Rodadas de otimização Amazon Ads de 02/05 usam abril fechado (01/04–30/04) como baseline; não misturar últimos 30 dias móveis ou maio parcial. | 2026-05-02 | Pedro/Kobe |
| Mudanças em campanhas/keywords/targets Amazon Ads exigem aprovação explícita por grupo antes da execução. | 2026-05-02 | Pedro/Kobe |
| Para `Potes Redondos Plástico`, termos de vidro são core porque o produto é pote redondo de vidro com tampa plástica. | 2026-05-02 | Pedro |
| Todo pacote executado em 02/05 precisa revisão D+7 antes de nova camada de otimização por impacto. | 2026-05-02 | Kobe |

## Decisões Revogadas

_Nenhuma decisão revogada até o momento._

<!-- Template para revogação:
| [Decisão original] | [Data original] | [REVOGADA em DATA] — Motivo: [motivo]. Substituída por: [nova decisão] |
-->

---

_Última revisão: 2026-05-01_

## Regra Universal — Horários em Brasília (2026-04-01)
TODOS os horários apresentados ao Pedro devem estar em BRT (UTC-3). Nunca UTC, nunca GMT. Formato: "14h" ou "14:03 BRT". Converter silenciosamente antes de exibir. Vale para relatórios, alertas, logs, timestamps — qualquer comunicação.

