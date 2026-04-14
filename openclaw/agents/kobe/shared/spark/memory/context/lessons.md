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

### 2026-03-19 — Meta Ads: system user limitado por Business Manager [TÁTICA]
**Contexto:** Kobe tentou criar System User pra token permanente, mas BM da GB já atingiu limite.
**Erro/Problema:** Limite de System Users no BM impossibilita token permanente.
**Lição:** Usar Long-lived token (60 dias) com monitoramento de expiração.
**Ação concreta:** Verificar token semanalmente no health check. Alertar Kobe 7 dias antes da expiração. Token atual expira ~15/05.
**Cross-ref:** `accounts.md` → Protocolo de Token Meta
**Expira:** 2026-04-19

### 2026-03-17 — Meta Ads API v21.0: checar sunset dates [TÁTICA]
**Contexto:** Meta deprecia versões da API a cada ~2 anos.
**Erro/Problema:** Nenhum erro ainda — lição preventiva.
**Lição:** Verificar periodicamente se v21.0 ainda é suportada. Migrar com antecedência.
**Ação concreta:** Incluir verificação de versão da API no health check mensal.
**Cross-ref:** `accounts.md` → Sunset de API Meta
**Expira:** 2026-06-17

---

## Lições Expiradas (arquivo)

_Lições TÁTICAS removidas após expiração. Mantidas aqui apenas para referência histórica._

_Nenhuma lição expirada ainda._

---

_Novas lições são adicionadas conforme o Spark opera. Cada erro é uma oportunidade de melhorar o sistema._
