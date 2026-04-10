# Skill: Anomaly Detector — Spark v2.0

_Monitoramento contínuo de métricas-chave com detecção de anomalias e alertas automáticos._

---

## Quando usar
- Monitoramento contínuo de campanhas ativas
- Detecção de problemas antes que virem crises
- Análise de desvios significativos vs baseline
- Classificação de severidade e urgência
- Geração de alertas estruturados pro Kobe
- Correlação entre múltiplas anomalias simultâneas
- Contextualização com eventos externos (sazonalidade, feriados, mudanças de plataforma)

---

## Métricas Monitoradas

### Meta Ads

| Métrica | Baseline | Threshold 🟡 | Threshold 🔴 | Janela mínima |
|---|---|---|---|---|
| CPA | Média últimos 7 dias | >30% acima | >50% acima OU >2x meta | 2 dias consecutivos |
| ROAS | Meta da fase atual | <80% da meta | <breakeven (1.43x) | 3 dias consecutivos |
| CTR | Média últimos 7 dias | Queda >20% | Queda >40% | 2 dias consecutivos |
| CPM | Média últimos 7 dias | >40% acima | >70% acima | 3 dias consecutivos |
| Frequência | 2.5 (padrão) | >3.0 | >4.0 | Qualquer momento |
| Budget pace | Linear (dia/30) | Pacing >1.2 | Pacing >1.5 | Qualquer momento |
| Delivery | Spending normally | Learning Limited | Not Delivering | Qualquer momento |
| Hook Rate (vídeo) | Média últimos 7 dias | Queda >25% | Queda >50% | 3 dias (se vídeo ativo) |

### Google Ads

| Métrica | Baseline | Threshold 🟡 | Threshold 🔴 | Janela mínima |
|---|---|---|---|---|
| CPA | Média últimos 7 dias | >30% acima | >50% acima OU >2x meta | 2 dias consecutivos |
| CPC | Média últimos 7 dias | >40% acima | >60% acima | 3 dias consecutivos |
| CTR Search | Média últimos 7 dias | Queda >25% | Queda >50% | 2 dias consecutivos |
| Quality Score | 7/10 | <6 em keyword ativa | <5 em keyword ativa | Qualquer momento |
| Impression Share | Média últimos 7 dias | Queda >15% | Queda >30% | 3 dias consecutivos |
| Search Terms | — | >20% spend em irrelevantes | >35% spend em irrelevantes | Verificação semanal |
| Conversion Rate | Média últimos 14 dias | Queda >25% | Queda >50% | 3 dias consecutivos |

### Cross-Platform

| Métrica | Threshold 🟡 | Threshold 🔴 |
|---|---|---|
| ROAS gap Meta vs Google | >100% diferença por 7+ dias | >200% diferença por 7+ dias |
| Budget total pace | Projeção overshoot >10% | Projeção overshoot >20% |
| Conversões total | Queda >25% vs semana anterior | Queda >50% vs semana anterior |
| CPA consolidado | >20% acima da meta por 5+ dias | >50% acima da meta por 3+ dias |

---

## Tipos de Anomalia

### 1. Spike (pico anormal)
- Métrica sobe abruptamente (>2 desvios padrão da média 7d)
- Exemplos: CPM disparou, CPC dobrou
- **Causas comuns:** Concorrência aumentou, sazonalidade, bug no ad, mudança de leilão
- **Ação:** Verificar se é pontual (1 dia) ou tendência. Se pontual, monitorar. Se 2+ dias, investigar.

### 2. Degradação gradual
- Métrica piora lentamente ao longo de 5-7 dias
- Exemplos: CTR caindo dia a dia, CPA subindo devagar
- **Causas comuns:** Fadiga criativa, público saturando, concorrência crescendo
- **Ação:** Mais perigoso que spike porque passa despercebido. Comparar com 14 dias atrás, não só ontem.

### 3. Queda abrupta
- Métrica cai de repente (>50% em 24h)
- Exemplos: Impressões zeraram, conversões pararam
- **Causas comuns:** Campanha pausada, pixel quebrou, LP fora do ar, budget esgotou, conta bloqueada, ad reprovado
- **Ação:** Alerta 🔴 imediato. Verificar infraestrutura antes de mexer em campanha.

### 4. Divergência cross-platform
- Uma plataforma performa muito diferente da outra sem razão clara
- **Causas comuns:** Público diferente, criativo diferente, competição diferente, sazonalidade de canal
- **Ação:** Acionar skill de Budget Optimizer para avaliar realocação.

### 5. Correlação de anomalias (NOVO)
- Múltiplas métricas se movem juntas → sinal de causa raiz comum
- **Padrões conhecidos:**

| Correlação | Causa provável |
|---|---|
| CPM sobe + CTR cai + CPA sobe | Competição aumentou (leilão mais caro) |
| CTR cai + Frequência sobe | Fadiga criativa |
| Cliques estáveis + Conversões caem | Problema na landing page ou tracking |
| Impressões caem + IS Lost (budget) sobe | Budget insuficiente |
| Tudo cai junto | Problema técnico (pixel, LP, conta) |
| CPC sobe + QS cai | Relevância do ad/LP degradou |

**Regra:** Quando 2+ métricas se movem simultaneamente, diagnosticar a causa raiz compartilhada — não tratar cada métrica separadamente.

---

## Contexto Externo (verificar antes de alertar)

Antes de classificar uma anomalia, verificar se existe fator externo que explica:

### Fatores recorrentes

| Fator | Impacto típico | Quando |
|---|---|---|
| **Fim de semana** | CPM cai, CTR pode cair, volume cai | Sáb-Dom |
| **Início de mês** | Concorrência alta (todo mundo reativando budget) | Dias 1-3 |
| **Fim de mês** | Competidores esgotam budget, CPM pode cair | Dias 28-31 |
| **Feriado nacional** | Volume pode cair ou subir dependendo do feriado | Verificar calendário |
| **Data comercial** | CPM sobe muito (BF, Dia das Mães, Natal) | Ver sazonalidade em business.md |
| **Dia de pagamento** | Possível aumento de conversões | Dias 5, 15, 20, 30 |

### Fatores de plataforma

| Fator | Impacto | Como detectar |
|---|---|---|
| **Atualização de algoritmo (Meta)** | Performance instável por 3-7 dias | Notícias do setor, comunidades de ads |
| **Mudança de política (Google)** | Ads reprovados, conta limitada | Verificar notificações na conta |
| **Bug de plataforma** | Dados inconsistentes, delivery zero | Verificar status pages das plataformas |
| **Início de Learning Phase** | CPA alto, delivery instável | Normal — não alertar 🟡 antes de 7 dias |

**Regra:** Se a anomalia coincide com fator externo conhecido, incluir na análise: "Desvio possivelmente relacionado a [fator]. Recomendo monitorar por mais [X] dias antes de agir."

---

## Formato de Alerta

### Alerta 🟡 Atenção
```
⚡🟡 ATENÇÃO — [métrica] [subindo/caindo] em [plataforma]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Atual: [valor] (meta: [valor], baseline 7d: [valor])
📉 Tendência: [X]% [acima/abaixo] do baseline há [N] dias
🔍 Causa provável: [hipótese baseada em dados]
🌍 Contexto externo: [fator externo relevante ou "nenhum identificado"]
🔗 Correlação: [outra métrica se movendo junto ou "isolada"]
🔧 Ação sugerida: [o que fazer]
⏱️ Monitorar até: [data — quando escala pra 🔴 se não melhorar]
```

### Alerta 🔴 Crítico
```
⚡🔴 CRÍTICO — [métrica] em [plataforma]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Atual: [valor] (meta: [valor], baseline 7d: [valor])
📉 Desvio: [X]% [acima/abaixo] há [N] dias
🔍 Causa provável: [hipótese]
🔗 Correlação: [métricas relacionadas]
💰 Impacto financeiro: R$[X] perdido/desperdiçado se não agir
💰 Projeção mensal se mantiver: R$[X] de prejuízo adicional
🔧 Ação recomendada: [ação concreta e específica]
⏱️ Urgência: Agir em [X] horas
⚠️ Risco de inação: [consequência projetada em R$]
```

### Severidade Score (para priorização quando múltiplos alertas)

Quando houver mais de um alerta simultâneo, priorizar por score:

```
Score = (Impacto financeiro diário em R$) × (Dias sem ação) × (Fator de urgência)

Fator de urgência:
- Queda abrupta = 3x
- Spike = 2x  
- Degradação gradual = 1.5x
- Divergência = 1x
```

**Sempre apresentar alertas em ordem de score (maior primeiro).**

---

## Ciclo de Monitoramento

| Frequência | O que verificar | Output |
|---|---|---|
| **Cada ativação** | Métricas do dia vs baseline. Delivery status. Budget pace. | Alertas se threshold atingido |
| **Diário** | Snapshot completo. Tendências 7d. Contexto externo. | Snapshot ao Kobe |
| **Semanal** | Search terms (Google). Frequência acumulada (Meta). Cross-platform comparison. QS keywords. | Report semanal |
| **Mensal** | Revisão de thresholds. Ajustar baselines. Limpeza de falsos positivos. | Report mensal + threshold update |

---

## Regras de Comportamento

1. **Não alertar por oscilação normal.** CPA flutuando ±20% dia a dia é normal em ads. Só alertar quando a tendência persiste por N dias (conforme tabela de janelas).
2. **Não alertar sem dados suficientes.** Se campanha tem <100 impressões ou <48h ativa → ⚪ sem dados, nunca 🟡 ou 🔴.
3. **Sempre contextualizar com fator externo.** Antes de alertar, verificar se dia da semana, feriado, sazonalidade ou mudança de plataforma explica.
4. **Sempre incluir impacto financeiro.** "CPA subiu 30%" é menos útil que "CPA subiu 30% → estamos pagando R$X a mais por venda → R$Y a mais no mês".
5. **Sempre incluir ação.** Alerta sem recomendação é notificação inútil.
6. **Sempre verificar correlação.** Se CPA subiu, verificar se CTR caiu, se CPM subiu, se frequência aumentou — diagnosticar causa raiz, não sintoma.
7. **Escalar 🔴 imediatamente.** Não esperar o próximo ciclo de monitoramento.
8. **Registrar todo alerta.** Em `sessions/YYYY-MM-DD.md` com outcome.
9. **Não criar pânico.** Alertas frequentes demais dessensibilizam. Se está alertando 🟡 todos os dias, os thresholds estão errados.

---

## Rastreamento de Falsos Positivos

Após cada alerta, registrar o resultado:

| Campo | Valores |
|---|---|
| ID do alerta | SPARK-ALERT-YYYY-MM-DD-NNN |
| Tipo | Spike / Degradação / Queda abrupta / Divergência / Correlação |
| Nível | 🟡 / 🔴 |
| Resultado | ✅ Real + agimos | ✅ Real + se resolveu sozinho | ❌ Falso positivo |
| Motivo do falso positivo | Sazonalidade / fim de semana / variação normal / learning phase / outro |

### Auto-ajuste de thresholds

A cada 30 dias, revisar:
- **Se >30% dos alertas foram falsos positivos:** Thresholds muito sensíveis → relaxar em 10%
- **Se 0 alertas no mês mas houve problemas reais não detectados:** Thresholds muito frouxos → apertar em 10%
- **Se taxa de falso positivo entre 10-20%:** Thresholds calibrados → manter

Registrar ajustes no `playbook.md` com data e justificativa.

---

## Checklist de Infraestrutura (verificar quando tudo cai junto)

Quando múltiplas métricas caem abruptamente de forma simultânea, antes de diagnosticar a campanha, verificar infraestrutura:

- [ ] Pixel Meta disparando? (verificar Events Manager ou pedir ao Kobe)
- [ ] Google Tag funcionando? (verificar Tag Assistant ou pedir ao Kobe)
- [ ] Landing page / listing ativo e carregando? (verificar URL)
- [ ] Conta de anúncio ativa? (sem bloqueio, sem policy violation)
- [ ] Ads aprovados? (sem reprovação recente)
- [ ] Token Meta válido? (verificar accounts.md → protocolo de token)
- [ ] Budget não esgotado? (verificar pacing)

**Se infraestrutura está ok:** Problema é na campanha → diagnosticar normalmente.
**Se infraestrutura tem problema:** Resolver infra PRIMEIRO → depois reavaliar métricas.

---

## Aprendizado Contínuo

Após cada alerta resolvido:

| Pergunta | Se sim → |
|---|---|
| Foi falso positivo? | Ajustar threshold no playbook |
| Foi real e resolvemos a tempo? | Registrar padrão no playbook ("quando X acontece, fazer Y funciona") |
| Foi real e não agimos a tempo? | Registrar em lessons.md como lição |
| Descobri correlação nova? | Adicionar na tabela de correlações deste documento |
| O contexto externo era o fator? | Adicionar na lista de fatores recorrentes |

---

_⚡ Anomaly Detector existe para que nenhum problema passe despercebido — e nenhum falso alarme desperdice atenção._
