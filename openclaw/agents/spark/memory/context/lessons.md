---
title: "lessons"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Lições Aprendidas — [[openclaw/agents/spark/IDENTITY|Spark]] v2.0

_Erros e aprendizados. Consultar ANTES de recomendar qualquer mudança._
_Tags: [ESTRATÉGICA] = permanente | [TÁTICA] = expira em 30 dias_

---

## Como usar este arquivo

1. **ANTES de recomendar:** verificar se existe lição relevante aqui
2. **Ao registrar:** usar o template abaixo — sem exceção
3. **Lições TÁTICAS:** verificar data de expiração semanalmente, remover expiradas
4. **Lições ESTRATÉGICAS:** nunca expiram, nunca são removidas
5. **Cross-reference:** se a lição gerou regra no playbook, anotar referência cruzada

---

## Template de Lição

```markdown
### [DATA] — [Título curto] [ESTRATÉGICA|TÁTICA]
**Contexto:** O que aconteceu
**Erro/Problema:** O que deu errado
**Lição:** O que fazer diferente
**Ação concreta:** Mudança específica no comportamento do Spark
**Cross-ref:** [playbook.md seção X | decisions.md | nenhum]
**Expira:** [YYYY-MM-DD para TÁTICA | Nunca para ESTRATÉGICA]
```

---

## Lições Ativas

### Herdadas do Kobe (pré-ativação)


### 2026-03-17 — Meta Ads API v21.0: checar sunset dates [TÁTICA]
**Contexto:** Meta deprecia versões da API a cada ~2 anos.
**Erro/Problema:** Nenhum erro ainda — lição preventiva.
**Lição:** Verificar periodicamente se v21.0 ainda é suportada. Migrar com antecedência.
**Ação concreta:** Incluir verificação de versão da API no health check mensal.
**Cross-ref:** `accounts.md` → Sunset de API Meta
**Expira:** 2026-06-17



### 2026-05-03 — Amazon Ads sem entrega exige diagnóstico estrutural [TÁTICA]
**Contexto:** Redinha Frutas ficou 0/0/0 em abril/15d/7d; Kit Jardinagem estava inactive com entrega residual antiga.
**Lição:** Sem impressões/cliques não existe otimização de ACoS. Validar product ads, estoque/FBA, listing, categoria e Buy Box antes de mexer em bid.
**Ação concreta:** Classificar como experimento de tração/diagnóstico com confidence explícita e D+7 definido.
**Expira:** 2026-06-02

---

## Lições Expiradas (arquivo)

_Lições TÁTICAS removidas após expiração. Mantidas aqui apenas para referência histórica._

### [TÁTICA] Shopee Wallet não substitui relatório de Ads (2026-05-01)
**Lição:** Wallet é conciliação financeira, não performance/consumo oficial de campanhas; para DRE, usar número oficial da plataforma ou export e tratar Wallet apenas como alerta de diferença.
**Expira:** 2026-05-31

### [TÁTICA] Amazon Ads API mensal funciona para Sponsored Products (2026-05-01)
**Lição:** Para fechamento mensal Amazon Ads, preferir report API quando disponível; esperar estado sair de PENDING antes de concluir.
**Expira:** 2026-05-31

### [TÁTICA] Amazon Ads: 0 impressão após experimento indica elegibilidade antes de bid (2026-05-11)
**Lição:** Quando campanha/experimento fica com 0 impressões, 0 cliques e 0 vendas após janela de D+6/D+7, investigar listing ativo, Buy Box, elegibilidade, categoria e relevância antes de aumentar bid.
**Expira:** 2026-06-10

## Auditoria — Consolidação Profunda 2026-05-15

### Táticas expiradas removidas
- ### 2026-03-19 — Meta Ads: system user limitado por Business Manager [TÁTICA] — expirada em 2026-04-19.


### 2026-05-13 — Amazon Ads deve seguir protocolo de 5 camadas [ESTRATÉGICA]
**Contexto:** Pedro exigiu análise máxima antes de novas recomendações Amazon Ads.
**Lição:** Spark deve analisar Amazon Ads em 5 camadas: funil/estratégia, campanha, ASIN-listing/Buy Box, keyword-search term/histórico de bids e síntese macro. Não recomendar ação apenas por ACoS isolado.
**Ação concreta:** Usar v4.3 do playbook Amazon Ads/BidSpark antes de qualquer corte, escala ou harvest.
**Cross-ref:** decisions.md; `projects/analise-semanal-skill-amazon.md` v4.3
**Expira:** Nunca


### 2026-05-13 — Amazon Ads log interno deve ser validado antes de próxima rodada manual [TÁTICA]
**Contexto:** Execução Tulipa teve 7/7 success na Amazon Ads API, mas falhou em `amazon_ads_actions_log` por FK/constraints.
**Lição:** Se a API externa muda bid mas o log interno não registra, a auditoria D+7 fica capenga.
**Ação concreta:** Antes da próxima rodada manual, validar schema/fluxo de log para round, entity_id e action_type.
**Cross-ref:** pending.md
**Expira:** 2026-06-12
