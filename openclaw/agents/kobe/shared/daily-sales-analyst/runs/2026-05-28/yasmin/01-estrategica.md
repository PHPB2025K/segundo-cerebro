<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base sólida em janelas longas (57 dias de dado em 60d, 30d completo, 7d completo) e ml_snapshot com todos os blocos populados (`reputation`, `fulfillment_mix`, `top_items_details`, `account_overview`, `mercadolider` — todos `status: ok`). Weekly.md traz memória diária de 22 a 26/05 (5 ciclos), com hipóteses ativas rastreáveis. Ressalva central: `ads_summary` veio estruturalmente válido (`status: ok`) mas com `spend_yesterday_brl=R$0` e `revenue_ads_yesterday_brl=R$0` com 11 campanhas ativas — dado presente, semanticamente ambíguo; tese sobre Mercado Ads condicionada a verificação de origem. Data Readiness marcou `volume_band_mercado-livre` como `partial` por spike positivo (+53,6% vs 30d), não bloqueante, mas a leitura de rompimento de patamar será tratada como hipótese, não fato, até confirmação nos próximos ciclos.

---

### Leitura temporal

- **vs 60d e 30d:** GMV de R$8.463 está +95,9% sobre `avg_60d.avg_gmv=R$4.320` e +69,3% sobre `avg_30d.avg_gmv=R$4.999`. Pedidos +56,9% sobre 60d e +53,6% sobre 30d. Ticket sobe junto — +24,9% vs 60d (`changes.ticket_vs_60d_pct`) e +10,3% vs 30d. Volume e ticket crescendo simultaneamente descarta explicação de substituição de mix por item de maior valor; a expansão é multidimensional. Importante: a própria média 30d já estava acima da 60d (`R$4.999 vs R$4.320`), indicando que a conta vinha ganhando patamar gradualmente antes do dia de hoje.

- **vs mesmos dias da semana:** Média dos 4 quintas anteriores em R$5.312 (`same_weekday_avg.avg_gmv`), com pico em R$6.539 (14/05). Hoje R$8.463 supera o teto histórico dos pares de dia da semana em 29%. Não é efeito de sazonalidade — o mesmo dia da semana nunca gerou esse volume na série disponível. O controle de sazonalidade reforça, não neutraliza, a leitura de rompimento.

- **vs 7d:** Média 7d em R$5.789 (`avg_7d.avg_gmv`), ela mesma já acima de 30d e 60d. Hoje +46,2% sobre a média recente. A aceleração que a janela curta sinalizava foi amplificada, não interrompida, pelo dia de hoje.

- **Hipóteses anteriores (22–26/05):** (1) Health estagnado de MLB3288536143 (0,71) e MLB4073003575 (0,75) — oitavo ciclo idêntico confirmado, direção ainda inconclusiva; gatilho de ação (cair abaixo de 0,68 / 0,70) não acionado. (2) ADS share elevado e ACOS acima de baseline — ruptura radical hoje: `spend=R$0`, `revenue=R$0`; a série de 49–70% de ADS share registrada de 22 a 26/05 não tem continuidade aparente neste ciclo. (3) Estoque crítico em MLB6754669844 e MLB6739252838 — transita de risco para iminência factual: `available_quantity=3` e `available_quantity=2` respectivamente após o volume do dia.

---

### Leitura estratégica

- **Lente 1 — Rompimento de patamar em formação:** Três janelas temporais distintas e o controle de sazonalidade convergem no mesmo sentido — 60d, 30d, 7d e mesmo dia da semana estão todos abaixo do resultado de hoje, e a distância não é marginal (+46% a +96%). A própria trajetória da média 30d sobre a 60d confirma que o movimento não é pontual; o dia de hoje é o pico de uma curva que já subia. Hipótese de rompimento de patamar ganha consistência em múltiplas janelas — mas exige 2–3 ciclos adicionais no novo patamar para diferenciar de pico isolado.

- **Lente 5 — Mercado Ads zerado com maior dia recente:** `ads_summary.spend_yesterday_brl=R$0` e `revenue_ads_yesterday_brl=R$0` com `campaigns_active_count=11`. ROAS e ACOS incalculáveis; ADS share = 0% do GMV de R$8.463. A série anterior registrava 49–70% de ADS share com ROAS 7–14x. Se o dado é acurado (pausa operacional por Himmel ou decisão de teste), o orgânico gerou sozinho o maior dia recente — implicação estratégica relevante: a conta tem capacidade orgânica superior ao que os ciclos com ADS dominante permitiam enxergar. Se há gap de atribuição ou atraso de API, a leitura orgânica fica suspensa e o patamar do dia pode ser parcialmente ADS não atribuído. Sem confirmação da origem, a tese orgânica é hipótese — não fato.

- **Lente 3 — Dependência estrutural com estoque em ruptura iminente nos vetores secundários:** IMB501 cluster (MLB3288536143, variações Tampa Preta+Cinza+Vermelha) concentrou 51,2% do volume em um único anúncio (`top3_concentration=51.2%`), todos em Full com `available_quantity=282` — estoque seguro no vetor principal. Contudo: MLB6754669844 (Kit 10 Potes 640ml, Full, `available_quantity=3` com 11 pedidos no dia) e MLB6739252838 (Kit 10 Potes 320ml 6un, Cross-Docking, `available_quantity=2` com 4 pedidos) estão em véspera de ruptura ou já rompidos. A assimetria entre campeões em Full (top10 do dia: 94,8% Full vs base ativa: 40,2% Full em `account_overview.active_analysis.fulfillment_mix.full_pct`) confirma a tese recorrente: os anúncios que performam vivem em Full; a base que controla reposição é majoritariamente Cross-Docking. Qualquer ruptura em Full afeta proporcionalmente mais GMV do que o mix da base sugere.

- **Lente 6 — MercadoLíder Platinum em zona de promoção iminente:** Gap em R$33.193 (`platinum.gap_revenue_brl`), progresso 88,79%, ETA 7,6 dias ao ritmo médio de R$4.380/dia. O faturamento de hoje (R$8.463) operou 93% acima do ritmo médio necessário — se o dia representa o novo patamar e não pico pontual, o ETA real é inferior a 7,6 dias. `cancellations_rate=0` e `claims_rate=0.0019` (38% do threshold 0,005) mantêm as métricas de qualidade limpas. Com gap abaixo de R$35k e progresso acima de 88%, a conta entra em zona onde cancelamentos automáticos por ruptura de estoque (MLB6754669844, MLB6739252838) ou piora de health dos campeões têm impacto assimétrico no timing da promoção.

---

### Tese da conta

**Em ganho de patamar** — o movimento é consistente em três janelas temporais independentes (30d acima de 60d, 7d acima de 30d, dia de hoje acima de tudo na série disponível do mesmo dia da semana) e não se explica por sazonalidade. A trajetória de ticket ascendente (+24,9% vs 60d) e pedidos crescendo junto descarta mix-shift como explicação isolada. O fato de o maior dia recente ter ocorrido com ADS aparentemente zerado, se confirmado, indica que o ganho de patamar tem raiz orgânica — o que eleva a qualidade da tese. A fragilidade persiste na estrutura: concentração de 51,2% em um único anúncio com health em nível preocupante há 8 ciclos, dois anúncios de cauda em ruptura iminente de estoque, e 176 anúncios pausados vs 82 ativos sinalizando cauda morta dominante. O patamar está sendo ganho, mas sobre uma base estreita e sem segundo vetor consolidado.

---

### Risco estrutural principal

**Risco:** Health estagnado em nível preocupante/regular dos dois anúncios de maior peso — MLB3288536143 (`health=0.71`, nível preocupante, oitavo ciclo idêntico, 51,2% do volume do dia) e MLB4073003575 (`health=0.75`, nível regular, oitavo ciclo idêntico, 15 pedidos do dia) — sem evidência de ação corretiva no pacote e com dependência crescente em Full concentrada nesses dois anúncios.

**Por que importa:** Anúncios em nível preocupante perdem exposição orgânica progressivamente no algoritmo ML. Com ADS zerado hoje, toda a performance de R$8.463 veio de orgânico — e os dois maiores vetores orgânicos estão com qualidade degradada há 8 ciclos. Se o algoritmo atualizar posicionamento com base no health atual, a conta perde exposição exatamente no momento em que está ganhando patamar. O ganho seria revertido de forma silenciosa sem alteração aparente no produto ou no preço.

**Histórico:** Registrado desde 22/05 como segundo ciclo consecutivo; oitavo ciclo hoje. Presente em todos os diários semanais. Nenhuma ação corretiva registrada na memória disponível.

**Sinal de confirmação:** Health de MLB3288536143 cair abaixo de 0,68 em qualquer ciclo, ou MLB4073003575 cair abaixo de 0,70 — gatilho para alinhamento Yasmin sobre drivers de qualidade do anúncio (completude de ficha, atributos, imagens). Se health permanecer estável por mais 3 ciclos na mesma faixa, hipótese de piso de nível ganha força e reduz a urgência.

---

### Sinais a observar

1. **`ads_summary.spend_yesterday_brl` retornar a valor positivo no próximo ciclo** confirma que o zero de hoje foi anomalia de atribuição, atraso de API ou pausa operacional pontual de Himmel — e exige recalibrar a leitura orgânica de hoje; permanecer em zero pelo segundo ciclo consecutivo confirma pausa real e eleva a qualidade da tese de expansão orgânica estrutural.

2. **GMV ≥ R$6.500 por 2 dias seguidos nos próximos 3 ciclos** — usando como novo piso o teto histórico dos pares de dia da semana (R$6.539, 14/05) — confirma rompimento de patamar real e consolida a tese; GMV abaixo de R$5.000 no próximo ciclo reclassifica hoje como pico pontual sem continuidade.

3. **MLB6754669844 (Kit 10 Potes 640ml) ou MLB6739252838 (Kit 10 Potes 320ml 6un) com `available_quantity=0` ou `status=paused` no próximo pacote** confirma ruptura ativa — impacto direto em `cancellations_rate` nos próximos 3–5 ciclos e potencial atraso no ETA de MercadoLíder Platinum se cancelamentos automáticos forem gerados (monitorar se `cancellations_rate` sai de zero, se disponível no pacote).