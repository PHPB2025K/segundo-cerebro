<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Janelas quantitativas completas — 7d com 7 dias, 30d com 30 dias, 60d com 60 dias, série de mesmos dias da semana com 4 observações. Base numérica sólida. weekly.md e monthly.md são templates vazios sem nenhuma entrada histórica registrada; nenhuma hipótese ativa para confirmar ou refutar. A leitura de hoje serve como ponto de partida da memória qualitativa, não como confirmação de tese prévia — a confiança da classificação está sustentada pelos dados quantitativos, não por padrão qualitativo acumulado.

---

### Leitura temporal

- **Patamar de longo prazo (60d e mesmos dias da semana):** 90 pedidos está na linha da média de 60d (91.2) e dos mesmos dias da semana (92.5) — volume estável e consistente com o histórico longo. O GMV de R$5.057 está 32.5% acima da média de 60d e 31.6% acima dos mesmos dias da semana. A divergência entre volume e faturamento é inequívoca e recorrente em todas as janelas: o patamar de GMV subiu sem que o volume de pedidos tenha subido.

- **Posição no mês (30d):** GMV +15% acima da média mensal com pedidos -9.9% abaixo. Ticket médio de R$56.19 está 27.6% acima dos R$44 de média mensal. O padrão persiste na janela de 30d — não é flutuação de curto prazo.

- **Curto prazo (7d):** Pedidos -21.8% abaixo da média de 7 dias (115.1), GMV apenas -4.9% abaixo. A semana recente teve mais pedidos a ticket menor; hoje inverte essa proporção. Sem memória qualitativa, não é possível atribuir causa — pode ser composição de dias da semana na janela 7d, mudança de mix em curso, ou ambos.

- **Série de quartas-feiras:** Alta volatilidade em volume (65 → 87 → 134 → 84 → 90) e em GMV (R$2.984 → R$3.005 → R$5.618 → R$3.758 → R$5.057). O pico de 29/04 é outlier claro; excluindo-o, as últimas três quartas-feiras mostram GMV em elevação (R$3.005 → R$3.758 → R$5.057) com volume em leve alta (87 → 84 → 90) — trajetória consistente com expansão de ticket estrutural, não evento isolado.

---

### Leitura estratégica

- **O ticket médio é o vetor estrutural ativo da conta.** Expansão de +34% vs 60d e +35% vs mesmos dias da semana não se explica por flutuação diária — o patamar de ticket mudou. A hipótese mais provável é mix shift em direção a produtos de maior valor unitário: a família YW (potes retangulares 1050ml) responde por 21 pedidos hoje (KIT4YW1050 + KIT10YW1050 + KIT2YW1050) com tickets significativamente maiores que os líderes de volume. Esse deslocamento de mix sustenta GMV mesmo quando o volume total oscila, tornando a conta estruturalmente menos sensível a flutuações de conversão.

- **A conta opera com dois vetores distintos.** Top 3 em 47.8% e top 5 em 58.9% — concentração real, mas com dois eixos separados: família IMB501 (potes redondos, tampos coloridos) como vetor de volume, família YW (potes retangulares 1050ml) como vetor de valor. Essa separação reduz o risco de colapso por produto único em comparação com contas de vetor único, mas não elimina a dependência estrutural dos líderes.

- **Saúde degradada nos anúncios de maior valor é contradição interna.** KIT4YW1050 — segundo maior em pedidos e provavelmente o maior em GMV unitário — opera com health 0.75, abaixo do limiar crítico de 0.85. IMB501V está em 0.71. Saúde baixa no ML afeta posicionamento orgânico e elegibilidade de ADS sobre esses anúncios. A expansão de GMV via ticket pode estar mascarando perda de exposição que ainda não se traduziu em queda de volume — risco que só aparece quando a degradação atravessa um limiar de ranking.

- **ADS opera com eficiência aparente (ACOS 4.33%), mas com peso relevante no resultado.** R$3.041 de GMV atribuído ao ADS sobre R$5.057 total (≈60%) indica dependência significativa do tráfego pago. Sem baseline orgânico histórico, não é possível avaliar se essa proporção é estrutural ou pontual — isso precisa ser calibrado nas próximas entradas de memória.

---

### Tese da conta

**Em ganho de patamar.** O GMV está consistentemente acima das janelas de 30d (+15%) e 60d (+32.5%), com volume de pedidos estável — o que configura elevação de patamar de faturamento via expansão de ticket, não via aceleração de volume. Reputação sólida (verde, gold), Full respondendo por 57-78% dos pedidos nas janelas recentes, cancelamentos baixos. A ausência de memória qualitativa prévia impede confirmar se esta trajetória é inflexão recente ou progressão esperada, mantendo a confiança em nível moderado: os dados sustentam a classificação, mas sem âncora histórica para calibrar a profundidade ou reversibilidade da mudança.

---

### Risco estrutural principal

- **Risco:** Saúde degradada em anúncios líderes — KIT4YW1050 (health 0.75) e Conjunto 5 Potes Tampa Vermelha (health 0.71), ambos abaixo do limiar crítico de 0.85. Adicionalmente, 63 dos 81 anúncios ativos não têm dado de health disponível, o que impede avaliar a amplitude real do problema.

- **Por que importa:** Health baixa no ML reduz elegibilidade para posições de destaque e pode comprometer a eficiência do ADS (campanhas sobre anúncios com health degradada têm menor retorno e menor alcance). Se o segundo maior vendedor da conta opera com health 0.75, a expansão de GMV sustentada pelo ticket pode ser corroída por perda silenciosa de exposição — deterioração que se acumula antes de aparecer no número de pedidos.

- **Histórico:** Primeiro registro formal — não há memória anterior para determinar se essa degradação é nova ou crônica. Essa é a distinção mais importante a estabelecer nos próximos dias.

- **Sinal de confirmação:** KIT4YW1050 com health abaixo de 0.80 por 3 ou mais dias consecutivos (se health disponível no pacote) confirma deterioração ativa; alternativamente, pedidos desse produto abaixo de 8/dia por 2 dias seguidos é sinal operacional de perda de exposição.

---

### Sinais a observar

1. **Ticket médio acima de R$52 por 3 dias consecutivos** — confirma que a expansão observada é patamar novo e não efeito de mix pontual, consolidando a tese de ganho de patamar. Ticket abaixo de R$48 em 2 dos próximos 5 dias enfraquece a tese e levanta hipótese de mix volátil.

2. **Pedidos do KIT4YW1050 abaixo de 8/dia por 2 dias seguidos** — sinaliza que a health 0.75 está se traduzindo em perda real de exposição, não apenas métrica de qualidade sem efeito prático. Esse sinal ativa o risco estrutural identificado.

3. **Ruptura de estoque do Kit 06 Canequinhas Suporte Acrílico (914C_BAV)** — com 3 unidades disponíveis e 3 pedidos registrados ontem, a ruptura é iminente. Out-of-stock em anúncio ativo no ML gera penalização de health e pode afetar o ranking do anúncio mesmo após reabastecimento. Sinal binário: se o anúncio aparecer como indisponível nos próximos 1-2 dias, o risco se materializou.