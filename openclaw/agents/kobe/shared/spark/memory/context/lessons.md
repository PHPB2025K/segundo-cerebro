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


### 2026-05-01 — Shopee Wallet não substitui relatório de Ads [TÁTICA]
**Contexto:** Wallet API retornou `SPM_DEDUCT` com recargas/débitos de ADS, mas o número oficial da plataforma Shopee Ads foi maior e traz vendas/ROAS.
**Lição:** Wallet é conciliação financeira, não performance/consumo oficial de campanhas.
**Ação concreta:** Para DRE, usar número oficial da plataforma ou export; Wallet apenas alerta diferença.
**Expira:** 2026-05-31

### 2026-05-01 — Amazon Ads API mensal funciona para Sponsored Products [TÁTICA]
**Contexto:** Report mensal abril/2026 via Amazon Ads API v3 concluiu e trouxe gasto, vendas, ROAS, ACOS, cliques e impressões.
**Lição:** Para fechamento mensal Amazon Ads, preferir report API quando disponível; esperar estado sair de PENDING antes de concluir.
**Expira:** 2026-05-31

---


### 2026-05-02 — Amazon Ads: resolver IDs live antes de executar [TÁTICA]
**Contexto:** Na execução de Potes Herméticos Tampa Bambu, uma tentativa com IDs de snapshot retornou `ENTITY_NOT_FOUND`.
**Erro/Problema:** IDs analisados em snapshot podem não ser os IDs live corretos no momento da execução.
**Lição:** Separar análise de execução; antes de PATCH/POST, refazer lookup live de keywords/targets/campaigns.
**Ação concreta:** Resolver IDs live imediatamente antes de aplicar mudanças e registrar tentativas antigas como FAILED.
**Cross-ref:** pending D+7 Amazon Ads
**Expira:** 2026-06-01

### 2026-05-02 — Amazon Ads: logs precisam distinguir Exact/Broad/Auto/Product Targeting [TÁTICA]
**Contexto:** Uma ação de escala foi registrada como `ESCALAR_WINNER_EXACT` mesmo com winners em Alcance/Broad.
**Erro/Problema:** Action type impreciso dificulta auditoria D+7 e aprendizado do funil.
**Lição:** O log deve refletir origem/match type real da ação.
**Ação concreta:** Usar action types separados ou descrição clara para escala Exact, Broad/Phrase, Auto target e Product Targeting.
**Cross-ref:** amazon_ads_actions_log
**Expira:** 2026-06-01

### 2026-05-02 — Nome de grupo pode esconder o core semântico do produto [TÁTICA]
**Contexto:** `Potes Redondos Plástico` parecia conflito com termos de vidro, mas Pedro corrigiu que o produto é vidro com tampa plástica.
**Erro/Problema:** Cortar keyword por nome interno ambíguo teria eliminado termos core eficientes.
**Lição:** Validar composição/título/anúncio antes de classificar termo como irrelevante por semântica.
**Ação concreta:** Em grupos ambíguos, checar produto real antes de recomendar negativas/cortes.
**Cross-ref:** decisions.md — Potes Redondos Plástico
**Expira:** 2026-06-01

## Lições Expiradas (arquivo)

_Lições TÁTICAS removidas após expiração. Mantidas aqui apenas para referência histórica._

### 2026-03-19 — Meta Ads: system user limitado por Business Manager [TÁTICA]
**Contexto:** Kobe tentou criar System User pra token permanente, mas BM da GB já atingiu limite.
**Erro/Problema:** Limite de System Users no BM impossibilita token permanente.
**Lição:** Usar Long-lived token (60 dias) com monitoramento de expiração.
**Ação concreta:** Verificar token semanalmente no health check. Alertar Kobe 7 dias antes da expiração. Token atual expira ~15/05.
**Cross-ref:** `accounts.md` → Protocolo de Token Meta
**Expira:** 2026-04-19


---

_Novas lições são adicionadas conforme o Spark opera. Cada erro é uma oportunidade de melhorar o sistema._
