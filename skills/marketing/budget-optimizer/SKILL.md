---
name: budget-optimizer
description: >
  Otimização de budget entre campanhas de ads (Meta Ads + Google Ads). Usar quando:
  rebalancear budget entre campanhas, decidir onde alocar mais verba, identificar campanhas
  com budget insuficiente ou excessivo, otimizar distribuição de spend para maximizar ROAS,
  planejar budget mensal de ads, definir regras de escala automática, analisar eficiência
  de alocação, pacing de budget, CBO vs ABO no Meta, portfolio bidding no Google Ads,
  simulação de cenários de budget, budget da GB Importadora, quanto gastar em ads.
---

# Budget Optimizer — Skill de Otimização de Verba

> Usado por [[openclaw/agents/spark/IDENTITY|Spark]]

Otimização inteligente de alocação de budget entre campanhas e plataformas de ads.
Cross-platform: Meta Ads + Google Ads.
Contexto: GB Importadora (Budamix), ROAS mínimo 10x, ticket R$100-300, margem ~70%.

---

## Quando Usar Esta Skill

1. Pedro ou Kobe pede para otimizar distribuição de budget
2. Análise de eficiência de alocação entre campanhas/plataformas
3. Planejamento de budget mensal/semanal
4. Decisão de escalar ou reduzir verba em campanhas específicas
5. Comparativo Meta vs Google — onde o real rende mais
6. Configuração de regras de escala automática

---

## Princípios de Otimização

### 1. Budget segue performance, não intenção

Alocar mais verba onde ROAS é comprovadamente alto. Não alocar por "achar" que vai funcionar. Dados > intuição.

**Exceção:** Campanhas novas em fase de aprendizado precisam de budget mínimo para sair do learning phase. Não cortar cedo demais.

### 2. Escala tem limite

Toda campanha tem um ponto de saturação onde mais budget = ROAS decrescente. Identificar esse ponto é o trabalho principal do optimizer.

**Sinais de saturação:**
- ROAS caindo conforme budget sobe
- Frequency > 3x na mesma audiência (Meta)
- Impression Share de 90%+ com CPC subindo (Google)
- CPA subindo > 20% sem mudança de targeting

### 3. Meta vs Google — não são iguais

| Aspecto | Meta Ads | Google Ads |
|---|---|---|
| **Natureza** | Demand generation (cria demanda) | Demand capture (captura demanda existente) |
| **Quando escala bem** | Público grande, creative forte | Keywords com volume, produto buscado |
| **Risco principal** | Creative fatigue, audience saturation | CPC inflação em keywords competitivas |
| **Budget mínimo recomendado** | 2-3x CPA alvo por ad set/dia | Suficiente para não perder >20% IS por budget |
| **Fase de aprendizado** | ~50 conversões em 7 dias | ~15 conversões em 30 dias (Smart Bidding) |

### 4. Regra dos 80/20

80% do budget nas campanhas comprovadas (ROAS acima da meta). 20% em teste (novas campanhas, novos públicos, novos criativos). Nunca 100% em teste. Nunca 100% no que já funciona (precisa de renovação).

---

## Framework de Alocação

### Passo 1: Classificar campanhas

| Categoria | Critério | Ação de budget |
|---|---|---|
| 🟢 **Winner** | ROAS > meta (10x) por 7+ dias consecutivos | Escalar 15-20% por semana (máx) |
| 🟡 **Learning** | < 7 dias ou < 50 conversões (Meta) / < 15 (Google) | Manter budget mínimo, não julgar ainda |
| 🟠 **Marginal** | ROAS entre 5x-10x (abaixo da meta mas positivo) | Otimizar antes de escalar (targeting, creative, bid) |
| 🔴 **Loser** | ROAS < 5x por 7+ dias com spend significativo | Reduzir 30-50% ou pausar |

### Passo 2: Calcular budget ótimo

**Para Meta Ads:**
```
Budget mínimo por ad set = CPA alvo × 2-3 (para sair do learning)
Budget de escala = Aumentar 15-20% a cada 3-5 dias (se ROAS se mantém)
Budget máximo = Ponto onde ROAS começa a cair (monitorar diariamente)
```

**Para Google Ads:**
```
Budget mínimo = Suficiente para não perder >20% Impression Share por budget
Budget de escala = Ajustar Target ROAS/CPA gradualmente (não budget bruto)
Budget máximo = 100% de Impression Share em keywords core
```

### Passo 3: Rebalancear

```
PROTOCOLO DE REBALANCEAMENTO SEMANAL:

1. Coletar métricas de todas as campanhas ativas (últimos 7 dias)
2. Classificar cada campanha (Winner/Learning/Marginal/Loser)
3. Calcular ROAS marginal de cada Winner (quanto ROAS muda com +10% budget)
4. Mover budget de Losers → Winners com melhor ROAS marginal
5. Manter Learning intocadas (dar tempo)
6. Documentar mudanças em sessions/YYYY-MM-DD.md
```

---

## Regras de Escala Automática

### Regras de proteção (sempre ativas)

| Regra | Trigger | Ação | Plataforma |
|---|---|---|---|
| **Kill switch** | CPA > 2x meta por 2 dias consecutivos | Pausar campanha | Meta + Google |
| **Budget cap** | Spend diário > 150% do budget definido | Reduzir budget ao original | Meta |
| **ROAS floor** | ROAS < 3x por 3 dias consecutivos | Reduzir budget 50% | Meta + Google |

### Regras de escala (quando performance comprova)

| Regra | Trigger | Ação | Cooldown |
|---|---|---|---|
| **Scale up** | ROAS > 12x por 3 dias consecutivos | Aumentar budget 20% | 3 dias |
| **Scale down** | ROAS entre 7x-10x por 5 dias | Reduzir budget 15% | 5 dias |
| **Creative refresh** | CTR caiu > 30% vs média 14 dias | Alertar para novo creative | — |

### Implementação

**Meta Ads:** Regras automatizadas via Meta Ads API (ou manual via Ads Manager):
```
Condition: ROAS > 12 (últimos 3 dias)
Action: Increase daily budget by 20%
Max budget: R$[definir por campanha]
Schedule: Daily at 06:00 BRT
```

**Google Ads:** Regras automatizadas ou scripts:
```
Condition: ROAS > 12 AND impressions > 100 (últimos 3 dias)
Action: Increase budget by 20%
Max budget: R$[definir por campanha]
Frequency: Daily
```

---

## Framework de Planejamento Mensal

### Input necessário

1. Budget total disponível para ads no mês
2. Performance do mês anterior (por campanha e plataforma)
3. Sazonalidade esperada (eventos, datas comemorativas)
4. Novos produtos ou campanhas planejadas

### Output

```
## Plano de Budget — [Mês/Ano]

### Distribuição por plataforma
| Plataforma | % do Total | Valor | Justificativa |
|---|---|---|---|

### Distribuição por campanha
| Campanha | Plataforma | Budget diário | Budget mensal | ROAS esperado |
|---|---|---|---|---|

### Reserva de teste
| Teste | Budget | Objetivo | Duração |
|---|---|---|---|

### Triggers de rebalanceamento
- Se [campanha X] atingir ROAS > [Y] em 7 dias → mover R$[Z] de [campanha W]
- Se [campanha X] não atingir ROAS > [Y] em 14 dias → pausar e realocar

### Datas de revisão
- Semana 1: [data] — primeira revisão
- Semana 2: [data] — rebalanceamento se necessário
- Semana 3: [data] — preparar para próximo mês
```

---

## Análise de Eficiência — Template

### Cross-Platform

| Métrica | Meta Ads | Google Ads | Delta |
|---|---|---|---|
| Spend | R$ | R$ | |
| Revenue | R$ | R$ | |
| ROAS | x | x | |
| CPA | R$ | R$ | |
| Conversions | | | |
| **ROAS Marginal** | x | x | |

**ROAS Marginal** = Quanto ROAS muda para cada R$100 a mais investido. A plataforma com maior ROAS marginal recebe o próximo incremento de budget.

### Por Campanha (dentro de cada plataforma)

| Campanha | Spend | Revenue | ROAS | CPA | Status | Ação |
|---|---|---|---|---|---|---|
| [nome] | R$ | R$ | x | R$ | 🟢🟡🟠🔴 | Escalar/Manter/Otimizar/Pausar |

---

## Contexto GB Importadora

| Parâmetro | Valor | Fonte |
|---|---|---|
| ROAS mínimo | 10x | Decisão Pedro |
| Ticket médio | R$100-300 | USER.md |
| Margem bruta | ~70% | USER.md |
| Custo agências (atual) | R$9k/mês | USER.md |
| Meta Ads — campanhas | 16 (todas pausadas em Mar/2026) | Spark MEMORY |
| Google Ads — campanhas | A verificar (integração pendente) | — |
| Gasto histórico Meta | R$27.432,69 total | Spark MEMORY |

### CPA máximo calculado

```
CPA máximo = Ticket médio × (Margem bruta - Margem mínima desejada)
CPA máximo = R$200 × (0.70 - 0.20) = R$100
```

Ou seja: se CPA passar de R$100, a campanha está consumindo margem demais.

---

## Referências

- Meta Ads skill: `skills/marketing/meta-ads/SKILL.md`
- Google Ads skill: `skills/marketing/google-ads/SKILL.md`
- Anomaly detector: `skills/marketing/anomaly-detector/SKILL.md`
- Design system: `skills/design/report-design-system/SKILL.md`
