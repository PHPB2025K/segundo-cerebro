---
title: "CHANGELOG skills v2"
created: 2026-04-14
type: changelog
agent: kobe
status: active
tags:
  - agent/kobe
---

# CHANGELOG — Skills do Spark v1.0 → v2.0

_Auditoria e melhorias realizadas em 2026-03-20_

---

## Avaliação Geral

O Kobe criou uma base sólida para as 4 skills. As estruturas de relatório, naming conventions, e a árvore de diagnóstico estavam bem feitas. As melhorias focaram em **lacunas estratégicas e operacionais** que dariam ao Spark capacidade de análise mais profunda e tomada de decisão mais fundamentada.

| Skill | Nível de mudança | Melhorias principais |
|---|---|---|
| Meta Ads | Alto | Estratégia de públicos, iOS 14+, Estrutura de campanha GB, Matriz criativa |
| Google Ads | Alto | Bid strategy, Keywords, Ad extensions, Estrutura de campanha GB |
| Budget Optimizer | Médio-Alto | Diminishing returns, Budget mínimo viável, Pacing com fórmula, Caso para aumento |
| Anomaly Detector | Médio | Correlação de anomalias, Contexto externo, Falsos positivos, Checklist de infra |

---

## Detalhamento por Skill

### 1. Meta Ads — Melhorias

**Estratégia de Públicos (seção nova):**
- 5 camadas de público do mais quente ao mais frio (Retargeting → LAL Compradores → LAL Engajamento → Interesses → Broad)
- Regras de exclusão entre camadas para evitar overlap
- Tabela de Custom Audiences por fonte (Pixel, IG, FB Page, Lista de clientes)

**Consciência iOS 14+ / ATT (seção nova):**
- Impacto na atribuição (conversões sub-reportadas até 30%)
- Limitação de 8 eventos por domínio
- Como lidar: janela 7-day click, cruzar com UTM/GA4
- Alerta sobre ROAS medido vs ROAS real

**Estrutura de Campanha para GB (seção nova):**
- 4 campanhas específicas com budget, objetivo, público e função definidos
- Distribuição prática dos R$900/mês de Meta entre as campanhas
- Recomendação de sequência de lançamento (não tudo de uma vez)

**Matriz de Performance Criativa (novo):**
- Framework 2x2: CTR × ROAS → Winner / Tester / Revisar / Cortar
- Ação clara para cada quadrante

**Análise de Breakdowns (novo):**
- Tabela de quando solicitar cada breakdown (age, placement, device, region, hourly)
- Regra de economia de API: só solicitar quando necessário para diagnóstico

**Relatórios melhorados:**
- Snapshot diário agora inclui projeção de fim de mês e mudanças vs dia anterior
- Report semanal agora exige duas versões explícitas (técnica + negócio)

---

### 2. Google Ads — Melhorias

**Estratégia de Bidding (seção nova):**
- Tabela: quando usar cada bid strategy (Manual CPC, Enhanced, Target CPA, Target ROAS, Maximize)
- Budget mínimo por estratégia
- Progressão recomendada: Manual CPC → Target CPA → Target ROAS
- Regra: não trocar bid strategy com menos de 2 semanas de dados

**Estratégia de Keywords (seção nova):**
- Quando usar cada match type (Exact, Phrase, Broad)
- Keywords iniciais sugeridas para GB por nível de intenção (BOFU, MOFU, Branded)
- Lista de negativação obrigatória desde o dia 1 ("gratuito", "como fazer", "usado", etc.)

**Ad Extensions (seção nova):**
- 6 tipos de extensão com exemplos concretos para GB
- Prioridade de implementação
- Sitelinks, Callouts, Structured Snippets, Price, Image, Promotion

**Estrutura de Campanha para GB (seção nova):**
- 4 campanhas com budget, bid strategy, keywords/público e função
- Nota sobre PMax: só lançar com 30+ conversões/mês no account
- Distribuição dos R$600/mês entre as campanhas

**Quality Score expandido:**
- Meta de QS >7 com ação para QS <5 (investigar ou pausar)
- Impression Share com ações por cenário

**Relatório de negativação (formato novo):**
- Template padronizado com termos negativados, spend desperdiçado e economia estimada

---

### 3. Budget Optimizer — Melhorias

**Budget Mínimo Viável por campanha (seção nova):**
- Tabela com budget mínimo diário por tipo de campanha
- Regra: se budget não cobre mínimo, não lançar a campanha
- Conclusão: R$1.500/mês comporta 4-5 campanhas no total

**Pacing com fórmula (seção nova):**
- Fórmula de Pacing Ratio = (% budget gasto) ÷ (% mês decorrido)
- Classificação: 1.0 = perfeito, >1.2 = 🟡, >1.5 = 🔴, <0.8 = under-delivery
- Alertas integrados com threshold numérico

**Diminishing Returns (seção nova):**
- Tabela hipotética de ROAS por faixa de budget
- Regra: cada 50% de aumento no budget gera 30-40% de aumento em resultado (não linear)
- Sinais de que atingiu o teto do budget atual

**Justificativa de aumento de budget (template novo):**
- Formato para quando performance justifica pedir mais budget ao Pedro
- Inclui projeção de retorno, premissas e riscos
- Recomendação de escala gradual (não saltar de R$1.500 para R$5.000)

**Rebalanceamento semanal (novo):**
- Check semanal obrigatório com formato padronizado
- Regra: nunca mover mais de 10% de uma vez, máximo 1 redistribuição/semana

**Distribuição por funil detalhada:**
- Tabela com R$/mês e R$/dia para cada fase do funil em cada plataforma
- Facilita operacionalização (não precisa calcular toda vez)

---

### 4. Anomaly Detector — Melhorias

**Correlação de anomalias (seção nova):**
- Tabela de padrões conhecidos (CPM sobe + CTR cai = competição; CTR cai + Freq sobe = fadiga)
- Regra: quando 2+ métricas se movem simultaneamente, diagnosticar causa raiz compartilhada

**Contexto externo (seção nova):**
- Fatores recorrentes: fim de semana, início/fim de mês, feriados, dia de pagamento, datas comerciais
- Fatores de plataforma: atualização de algoritmo, mudança de política, bugs, Learning Phase
- Regra: se anomalia coincide com fator externo, incluir na análise e recomendar esperar

**Rastreamento de falsos positivos (seção nova):**
- Template de registro: ID, tipo, nível, resultado, motivo
- Auto-ajuste de thresholds: >30% falsos positivos → relaxar | 0 alertas + problemas reais → apertar
- Ciclo de revisão mensal

**Checklist de infraestrutura (novo):**
- Verificar pixel, tag, LP, conta, ads, token, budget ANTES de diagnosticar campanha
- Para cenários de "tudo caiu junto"

**Severity Score (novo):**
- Fórmula de priorização: Impacto financeiro × Dias sem ação × Fator de urgência
- Garante que alertas múltiplos sejam apresentados em ordem de importância

**Regra anti-dessensibilização (nova):**
- "Se está alertando 🟡 todos os dias, os thresholds estão errados"
- Alertas frequentes demais são piores que alertas ausentes
