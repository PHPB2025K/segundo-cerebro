# Skill: Budget Optimizer — Spark v2.0

_Alocação e redistribuição de budget entre Meta Ads e Google Ads baseada em performance._

---

## Quando usar
- Início de mês: definir alocação do budget mensal entre plataformas
- Semanalmente: avaliar se redistribuição é necessária
- Quando uma plataforma supera significativamente a outra
- Quando budget está sendo desperdiçado numa plataforma
- Projeção de gasto vs resultado até fim do período
- Quando Pedro/Kobe consideram aumentar budget total
- Quando precisa justificar pedido de mais budget com projeção de retorno

## Parâmetros Base

| Parâmetro | Valor | Fonte |
|---|---|---|
| Budget mensal total | R$1.500 | decisions.md |
| Alocação padrão | Meta 60% (R$900) / Google 40% (R$600) | playbook.md |
| Budget diário Meta | ~R$30/dia | Calculado |
| Budget diário Google | ~R$20/dia | Calculado |
| ROAS breakeven | 1.43x | business.md |
| CPA máximo (aprendizado) | R$35 (50% do lucro bruto) | business.md |

---

## Budget Mínimo Viável por Tipo de Campanha

Abaixo desses valores, a campanha não acumula dados suficientes para otimizar:

| Tipo de campanha | Budget mínimo diário | Razão |
|---|---|---|
| Meta — Conversão | R$5/dia (~R$150/mês) | Precisa de ~50 impressões/dia para learning |
| Meta — Alcance/Tráfego | R$3/dia (~R$90/mês) | Menor exigência de volume |
| Google — Search | R$5/dia (~R$150/mês) | CPC médio R$1-2 = 3-5 cliques/dia mínimo |
| Google — Display Retargeting | R$3/dia (~R$90/mês) | CPM baixo, precisa de menos budget |
| Google — Performance Max | R$10/dia (~R$300/mês) | Precisa de volume para ML funcionar |

**Regra:** Se o budget disponível não cobre o mínimo viável de uma campanha, não lançar essa campanha. Melhor concentrar budget em menos campanhas funcionais do que espalhar em muitas sem dados.

**Com R$1.500/mês:** Comporta 4-5 campanhas no total entre Meta e Google. Não mais.

---

## Regras de Alocação

### Alocação Inicial (Fase Aprendizado)
- **Meta 60% / Google 40%** — padrão do playbook
- Razão: Meta tem mais dados de e-commerce BR e é mais visual (bom para produtos da GB). Google pega intenção de busca ativa.
- **Válido enquanto:** Não houver 30+ dias de dados comparativos entre plataformas

### Rebalanceamento Semanal

Toda semana (preferencialmente segunda-feira), avaliar:

```
⚡ CHECK SEMANAL DE ALOCAÇÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Plataforma | ROAS 7d | CPA 7d | Spend 7d | % do total | Tendência |
|---|---|---|---|---|---|
| Meta | Xx | R$X | R$X | X% | 📈/📉/➡️ |
| Google | Xx | R$X | R$X | X% | 📈/📉/➡️ |

Diagnóstico: [ambas ok / uma superando / ambas abaixo]
Ação: [manter / redistribuir / diagnosticar antes]
```

### Triggers de Redistribuição

| Condição | Ação | Limite | Frequência |
|---|---|---|---|
| ROAS de uma plataforma >2x da outra por 7+ dias | Mover 10% do budget da pior para melhor | Plataforma inferior nunca <20% do total | Máximo 1 redistribuição por semana |
| Uma plataforma com ROAS < breakeven por 14 dias | Reduzir para 20%, realocar para outra | Mínimo 20% para manter aprendizado | Após diagnóstico da causa |
| Ambas performando acima da meta | Manter alocação. Preparar justificativa de aumento de budget total. | — | — |
| Ambas abaixo da meta | **NÃO redistribuir.** Problema não é alocação — diagnosticar causa raiz primeiro. | — | — |
| Uma plataforma sem dados (API pendente) | 100% na plataforma com dados. Realocação quando 2ª plataforma integrar. | Transição gradual 80/20 → 60/40 em 4 semanas | — |

### Redistribuição gradual (nunca abrupta)

| Semana | De 60/40 para 70/30 |
|---|---|
| Semana 1 | 65/35 |
| Semana 2 | 70/30 (se dados confirmam) |

**Nunca mover mais de 10% de uma vez.** Mudanças abruptas resetam learning nas duas plataformas.

---

## Distribuição por Funil (dentro de cada plataforma)

### Meta Ads (R$900/mês padrão)

| Fase | % | R$/mês | R$/dia | Campanhas |
|---|---|---|---|---|
| TOFU (Awareness) | 10% | R$90 | ~R$3 | Broad/Interesses — alcance |
| MOFU (Consideração) | 30% | R$270 | ~R$9 | Interesses — tráfego qualificado |
| BOFU (Conversão) | 40% | R$360 | ~R$12 | LAL Compradores — vendas |
| Retargeting | 20% | R$180 | ~R$6 | Visitantes/engajamento — recuperação |

### Google Ads (R$600/mês padrão)

| Fase | % | R$/mês | R$/dia | Campanhas |
|---|---|---|---|---|
| Search Branded | 10% | R$60 | ~R$2 | Proteção de marca |
| Search Genérico | 50% | R$300 | ~R$10 | Captura de demanda |
| Display Retargeting | 20% | R$120 | ~R$4 | Recuperar visitantes |
| Performance Max | 20% | R$120 | ~R$4 | Automação cross-channel |

**Nota:** Percentuais são ponto de partida. Ajustar com dados reais. Se BOFU está convertendo muito bem, pode migrar budget de TOFU para BOFU.

---

## Pacing (Controle de Ritmo de Gasto)

### Fórmula de pacing

```
Pacing Ratio = (% do budget gasto) ÷ (% do mês decorrido)

Pacing Ratio = 1.0 → No ritmo perfeito
Pacing Ratio > 1.2 → Gastando rápido demais 🟡
Pacing Ratio > 1.5 → Ritmo crítico 🔴
Pacing Ratio < 0.8 → Gastando devagar (under-delivery) 🟡
Pacing Ratio < 0.5 → Under-delivery severo 🔴
```

**Exemplo:**
- Dia 15 de 30 (50% do mês)
- Gastou R$900 de R$1.500 (60% do budget)
- Pacing Ratio = 60% ÷ 50% = 1.2 → 🟡 Gastando um pouco rápido

### Alertas de Pacing

| Trigger | Nível | Ação |
|---|---|---|
| Pacing Ratio > 1.2 | 🟡 | Informar Kobe. Sugerir redução de daily budget em X%. |
| Pacing Ratio > 1.5 | 🔴 | Alertar Kobe. Recomendar redução imediata ou pausa temporária. |
| Pacing Ratio < 0.8 | 🟡 | Under-delivery. Verificar: budget muito baixo? público muito restrito? bid muito baixo? |
| Uma plataforma esgotou 100% do budget mensal | 🔴 | Alertar Kobe. Pausar ou realocar. |

---

## Framework de Análise de Budget

### Projeção Mensal (calcular semanalmente)
```
⚡ SPARK — PROJEÇÃO DE BUDGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Período: [mês/ano] — Dia [X] de [30/31]
📊 Pacing Ratio: [X.X] — [🟢 no ritmo / 🟡 rápido / 🔴 crítico]

| Plataforma | Gasto | Budget | % gasto | Projeção mês | Pacing | Status |
|---|---|---|---|---|---|---|
| Meta | R$X | R$900 | X% | R$X | X.X | 🟢/🟡/🔴 |
| Google | R$X | R$600 | X% | R$X | X.X | 🟢/🟡/🔴 |
| **Total** | **R$X** | **R$1.500** | **X%** | **R$X** | **X.X** | — |

💰 ROAS consolidado: Xx (meta: >3x)
📈 Receita gerada até agora: R$X
📈 Receita projetada fim mês: R$X
📉 CPA médio consolidado: R$X (meta: <R$35)

🔧 Recomendação: [manter / redistribuir / reduzir pace / alertar sobre overspend]
```

### Simulação de Cenários (quando solicitado pelo Kobe)
```
📊 SIMULAÇÃO — Impacto de redistribuição
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Cenário | Meta | Google | ROAS esperado | Receita esperada | Risco |
|---|---|---|---|---|---|
| Atual (60/40) | R$900 | R$600 | Xx | R$X | Baseline |
| 70/30 | R$1.050 | R$450 | Xx | R$X | [risco] |
| 50/50 | R$750 | R$750 | Xx | R$X | [risco] |
| 80/20 | R$1.200 | R$300 | Xx | R$X | [risco] |

⚠️ Premissas: [CPA se mantém estável ao escalar — pode não ser verdade]
🔧 Recomendação: Cenário [X] porque [dados]
```

### Justificativa de Aumento de Budget (quando performance justifica)

Se ambas plataformas estão performando acima da meta, preparar para o Kobe:

```
⚡ SPARK — CASO PARA AUMENTO DE BUDGET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Performance atual:
- ROAS consolidado: Xx (meta: 3x) → [X]x acima da meta
- CPA: R$X (meta: R$35) → R$[X] abaixo da meta
- Impression Share (Google): X% → [X]% de oportunidade não capturada
- Frequência (Meta): X → ainda abaixo do limite

💰 Projeção com budget atual (R$1.500/mês):
- Receita estimada: R$X/mês
- Lucro bruto estimado: R$X/mês

💰 Projeção com budget proposto (R$[novo]/mês):
- Receita estimada: R$X/mês (+X%)
- Lucro bruto estimado: R$X/mês (+X%)

⚠️ Premissas e riscos:
- CPA pode subir 10-20% ao escalar (diminishing returns)
- Público pode saturar mais rápido com budget maior
- Recomendo escalar gradualmente: R$1.500 → R$2.000 → R$2.500 (em 3 meses)

🔧 Recomendação: Aumentar para R$[X]/mês. Distribuição: Meta [X]% / Google [X]%.
```

---

## Diminishing Returns (Retornos Decrescentes)

**Conceito crítico:** Dobrar o budget NÃO dobra o resultado. Cada real adicional tende a render menos que o anterior.

| Budget | ROAS esperado (hipotético) | Custo marginal |
|---|---|---|
| R$1.500/mês | 5x | Baseline |
| R$3.000/mês | 4x | CPA sobe ~20% |
| R$5.000/mês | 3.5x | CPA sobe ~40% |
| R$10.000/mês | 3x | CPA sobe ~60% |

**Regra:** Ao projetar cenários de aumento, sempre aplicar fator de degradação. Nunca projetar linearmente ("se R$1.500 dá X de receita, R$3.000 dá 2X"). Usar estimativa conservadora: cada 50% de aumento no budget gera 30-40% de aumento em resultado (não 50%).

**Sinais de que atingiu o teto do budget atual:**
- Impression Share (Google) > 90% em branded
- Frequência (Meta) subindo consistentemente mesmo com novos criativos
- CPA sobe proporcionalmente ao aumento de budget
- Audiência retargeting esgotada (todas as fases do funil saturadas)

---

## Relatório de Eficiência Mensal

No fechamento do mês, gerar para o Kobe:

```
⚡ SPARK — EFICIÊNCIA DE BUDGET [MÊS/ANO]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 RESUMO
| Plataforma | Investido | Receita | ROAS | CPA | Conversões |
|---|---|---|---|---|---|
| Meta | R$X | R$X | Xx | R$X | X |
| Google | R$X | R$X | Xx | R$X | X |
| **Total** | **R$X** | **R$X** | **Xx** | **R$X** | **X** |

📈 vs Mês anterior: [melhor / pior / primeiro mês]

🏆 Plataforma mais eficiente: [Meta/Google] (ROAS Xx vs Xx)
📉 Plataforma menos eficiente: [Meta/Google]

🔧 ALOCAÇÃO RECOMENDADA PARA PRÓXIMO MÊS:
| Plataforma | Mês atual | Recomendação | Mudança | Justificativa |
|---|---|---|---|---|
| Meta | X% (R$X) | X% (R$X) | [+X% / -X% / manter] | [dados] |
| Google | X% (R$X) | X% (R$X) | [+X% / -X% / manter] | [dados] |
```

---

## Regra de Ouro

> **Não existe alocação "certa" universal. A alocação ótima é determinada pelos dados da GB, não por benchmark de mercado. Conforme dados acumulam, os benchmarks internos (playbook.md) substituem as regras padrão deste documento.**

> **Budget é dinheiro real do Pedro. Cada realocação precisa de justificativa baseada em dados, não em feeling.**
