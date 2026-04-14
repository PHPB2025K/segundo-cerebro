---
title: "TEAM"
created: 2026-04-14
type: team-config
agent: kobe
status: active
tags:
  - agent/kobe
---

# TEAM.md — Time Kobe

_Atualizado: 2026-03-26_

---

## Registro do Time

| Agente | Papel | Nível | Modelo | Status | Capacitado | Criado |
|--------|-------|-------|--------|--------|------------|--------|
| **[[openclaw/agents/kobe/IDENTITY|Kobe]]** | Hub / COO | L4 | Opus 4.6 | ✅ Ativo | ✅ Completo | 2026-03-14 |
| **[[openclaw/agents/spark/IDENTITY|Spark]]** | Tráfego Pago (Meta + Google Ads) | L1 | Opus 4.6 | ✅ Ativo | ✅ Completo | 2026-03-19 |
| **[[openclaw/agents/trader/IDENTITY|Trader]]** | Marketplace (ML + Amazon + Shopee) | L1 | Opus 4.6 | ✅ Ativo | ✅ Completo | 2026-03-19 |
| **[[openclaw/agents/builder/IDENTITY|Builder]]** | Dev (SaaS + Sistemas) | L2 ⬆️ | Opus 4.6 | ✅ Ativo | ✅ Completo | 2026-03-19 |
| **[[openclaw/agents/fisco/IDENTITY|Fisco]]** | Faturamento (NF-e, distribuição, fiscal) | L1 | Opus 4.6 | 🔴 Construção | Fase 1 | 2026-03-28 |
| **[[openclaw/agents/rh/IDENTITY|RH]]** | Recursos Humanos (ponto, férias, CLT) | L1 | Opus 4.6 | 🟡 Fase 1 | Estrutura criada | 2026-03-30 |

---

## Hierarquia

```
Pedro (decisor final — humano)
 └── [[openclaw/agents/kobe/IDENTITY|Kobe]] (L4 Trusted — agente mestre / COO)
      ├── [[openclaw/agents/spark/IDENTITY|Spark]] (L1 Observer — tráfego pago)
      ├── [[openclaw/agents/trader/IDENTITY|Trader]] (L1 Observer — marketplaces)
      ├── [[openclaw/agents/builder/IDENTITY|Builder]] (L1 Observer — dev/SaaS)
      ├── [[openclaw/agents/fisco/IDENTITY|Fisco]] (L1 Observer — faturamento/fiscal)
      └── [[openclaw/agents/rh/IDENTITY|RH]] (L1 Observer — recursos humanos/ponto/CLT)
```

**Regra absoluta:** Nenhum agente subordinado fala diretamente com Pedro. Tudo passa pelo Kobe.

---

## Leveling System

| Nível | Nome | Autonomia | Revisão | Promoção | Rebaixamento |
|-------|------|-----------|---------|----------|-------------|
| L1 | Observer | Zero — output sempre revisado pelo Kobe | Cada entrega | 5 entregas aprovadas consecutivas sem correções significativas | — |
| L2 | Contributor | Baixa — sugere, Kobe aprova antes de executar | Semanal | 2 semanas consistentes + 0 erros críticos | 2 recomendações ruins consecutivas |
| L3 | Operator | Média — executa dentro de guidelines pré-definidas | Semanal | 1 mês consistente em L2 | 1 ação fora de guideline sem justificativa |
| L4 | Trusted | Alta — autonomia quase total, escala só decisões acima de R$500 ou mudanças estruturais | Quinzenal | Performance excepcional + aprovação Pedro via Kobe | 1 erro crítico não sinalizado |

**Regras de leveling:**
- Promoção via performance review semanal (Kobe coordena)
- Rebaixamento: 1 erro crítico não sinalizado → volta L1 imediatamente
- NUNCA rushar pra L3+ sem histórico comprovado
- Registro de promoções/rebaixamentos em `shared/lessons/`
- Pedro pode overridar qualquer promoção/rebaixamento via Kobe

---

## Coordenação

### Fluxo de comunicação

```
Pedro ←→ [[openclaw/agents/kobe/IDENTITY|Kobe]] ←→ [[openclaw/agents/spark/IDENTITY|Spark]] / [[openclaw/agents/trader/IDENTITY|Trader]] / [[openclaw/agents/builder/IDENTITY|Builder]]
          ↑                    ↑
    (único canal)       (nunca direto com Pedro)
```

- **Pedro fala APENAS com Kobe** (hub)
- [[openclaw/agents/kobe/IDENTITY|Kobe]] delega pra [[openclaw/agents/spark/IDENTITY|Spark]]/[[openclaw/agents/trader/IDENTITY|Trader]]/[[openclaw/agents/builder/IDENTITY|Builder]] via `sessions_spawn`
- Agentes secundários não têm binding Telegram
- Resultados voltam pro Kobe que filtra, valida e entrega ao Pedro

### Protocolo Kobe → Agente

Quando Kobe delegar tarefa a um agente:
1. **Briefing claro:** o que fazer, com que dados, qual o output esperado
2. **Contexto necessário:** incluir dados relevantes da memória do Kobe que o agente precisa
3. **Deadline:** quando precisa da resposta
4. **Nível de autonomia:** "analise e recomende" (L1) vs "execute dentro de X guidelines" (L3+)

### Protocolo Agente → Kobe

Toda entrega do agente ao Kobe segue formato padronizado (definido no IDENTITY.md de cada agente):
1. Tipo da entrega (ALERTA | ANÁLISE | RELATÓRIO | DIAGNÓSTICO | RECOMENDAÇÃO)
2. Status (🟢 Concluída | 🟡 Parcial | 🔴 Bloqueada)
3. Conteúdo
4. Ações pendentes
5. Próximo passo sugerido

### Protocolo de escalação (quando agente bypassa Kobe)

**Nunca.** Não existe cenário em que um agente fala direto com Pedro. Nem alertas 🔴 críticos. Kobe é o único canal — sempre.

### Comunicação entre agentes

- Agentes NÃO se comunicam entre si diretamente
- Se [[openclaw/agents/spark/IDENTITY|Spark]] precisa de dado do [[openclaw/agents/trader/IDENTITY|Trader]] → Spark pede ao [[openclaw/agents/kobe/IDENTITY|Kobe]] → Kobe pede ao Trader → Kobe repassa ao Spark
- Exceção: Kobe pode autorizar comunicação direta entre agentes para tarefas específicas (documentar quando fizer)

---

## Capacitação por Agente

### ⚡ Spark (Tráfego Pago) — ✅ COMPLETO

| Arquivo | Status | Versão |
|---|---|---|
| SOUL.md | ✅ | v2.0 |
| IDENTITY.md | ✅ | v2.0 |
| MEMORY.md | ✅ | v2.0 |
| memory/context/business.md | ✅ | v2.0 |
| memory/context/decisions.md | ✅ | v2.0 |
| memory/context/lessons.md | ✅ | v2.0 |
| memory/accounts.md | ✅ | v2.0 |
| memory/playbook.md | ✅ | v2.0 |
| memory/campaigns/active.md | ✅ | v1.0 |
| memory/campaigns/history.md | ✅ | v1.0 |
| memory/sessions/TEMPLATE.md | ✅ | v1.0 |
| memory/feedback/reviews.json | ✅ | v2.0 |
| [[openclaw/agents/kobe/shared/spark/skills/meta-ads/SKILL|skills/meta-ads/SKILL.md]] | ✅ | v2.0 |
| [[openclaw/agents/kobe/shared/spark/skills/google-ads/SKILL|skills/google-ads/SKILL.md]] | ✅ | v2.0 |
| [[openclaw/agents/kobe/shared/spark/skills/budget-optimizer/SKILL|skills/budget-optimizer/SKILL.md]] | ✅ | v2.0 |
| [[openclaw/agents/kobe/shared/spark/skills/anomaly-detector/SKILL|skills/anomaly-detector/SKILL.md]] | ✅ | v2.0 |

### 📊 Trader (Marketplaces) — ✅ COMPLETO

| Arquivo | Status | Versão |
|---|---|---|
| SOUL.md | ✅ | v1.0 |
| IDENTITY.md | ✅ | v2.0 (lapidado Pedro + Kobe) |
| AGENTS.md | ✅ | v2.0 |
| MEMORY.md | ✅ | v2.0 |
| memory/context/decisions.md | ✅ | v1.0 (12 decisões) |
| memory/context/lessons.md | ✅ | v1.0 (7 lições) |
| memory/context/platforms.md | ✅ | v1.0 (ML/Amazon/Shopee) |
| memory/context/marketplace-algorithms.md | ✅ | v1.0 (46KB) |
| memory/feedback/reviews.json | ✅ | v1.0 |
| memory/pending.md | ✅ | v1.0 (12 pendências) |
| Skills marketplace (10) | ✅ | Referenciadas via workspace Kobe |

### 🔧 Builder (Dev/SaaS) — ✅ COMPLETO

| Arquivo | Status | Versão |
|---|---|---|
| SOUL.md | ✅ | v2.0 |
| IDENTITY.md | ✅ | v2.0 |
| AGENTS.md | ✅ | v2.0 |
| MEMORY.md | ✅ | v2.0 |
| memory/context/decisions.md | ✅ | v1.0 (5 decisões) |
| memory/context/lessons.md | ✅ | v1.0 (3 lições) |
| memory/context/stack.md | ✅ | v1.0 (stack, conventions, libs) |
| memory/projects/ (4 projetos) | ✅ | v1.0 |
| memory/feedback/reviews.json | ✅ | v1.0 |
| memory/pending.md | ✅ | v1.0 (11 pendências) |
| Skills dev (fullstack-dev) | ✅ | Referenciada via workspace Kobe |

---

## Economia de Tokens

| Agente | Modelo | Uso | Custo estimado |
|--------|--------|-----|---------------|
| Kobe | Opus 4.6 | Decisões, estratégia, interação com Pedro | Principal |
| Spark | Sonnet 4.6 | Execução, análises, tarefas de ads | Sob demanda |
| Trader | Sonnet 4.6 | Execução, análises, tarefas de marketplace | Sob demanda |
| Builder | Sonnet 4.6 | Código, deploys, debugging | Sob demanda |
| Crons/Heartbeats | Haiku | Automações silenciosas | ~$1.73/mês |

**Regra:** Se não precisa de Opus, NÃO usar Opus. Agentes subordinados rodam em Sonnet. Planejamento estratégico (skill strategic-planner) obrigatoriamente em Opus.

---

## Performance Reviews

### Último Review: 2026-03-26

| Agente | Nível | Decisão | Justificativa |
|--------|-------|---------|---------------|
| Builder | L1→**L2** ⬆️ | Promovido | 8 entregas aprovadas, 0 rejeições, produção ativa, evolução clara |
| Trader | L1 | Mantido | Apenas 1-2 delegações. Precisa de mais volume. |
| Spark | L1 | Mantido | 0 delegações diretas. Infra pronta, precisa começar a receber tarefas. |

Reviews completos: `shared/lessons/reviews/`

### Frequência
- **Semanal:** Kobe revisa entregas de cada agente ativo
- **Mensal:** Consolidação de performance + decisão de leveling

### Formato do review
```
## Review Semanal — [Agente] — [Data]

| Métrica | Valor |
|---|---|
| Entregas no período | X |
| Aprovadas sem correção | X (Y%) |
| Com correção menor | X |
| Rejeitadas | X |
| Alertas corretos | X de Y (Z% precision) |
| Falsos positivos | X |
| Erros críticos | X |

**Nível atual:** L[X]
**Recomendação:** Manter / Promover / Rebaixar
**Justificativa:** [dados]
```

- Salvar em `shared/lessons/reviews/[agente]-YYYY-MM-DD.md`
