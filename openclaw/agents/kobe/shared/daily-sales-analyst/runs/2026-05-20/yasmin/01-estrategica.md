<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` estão como templates vazios — sem tese acumulada, hipóteses ativas ou padrões registrados anteriores. Esta análise não tem tese anterior para confirmar ou refutar; funciona como ponto de entrada da memória narrativa. As janelas 7d, 30d e 60d estão disponíveis e com cobertura completa. O `ml_snapshot` chegou íntegro: reputação, mix fulfillment (30d/7d/top10/base ativa), top\_items\_details, ads\_summary e account\_overview — base factual sólida, ausência apenas de profundidade narrativa histórica.

---

### Leitura temporal

- **vs 60d e vs mesmos dias da semana (âncoras mais estáveis):** Volume praticamente idêntico ao bimestre (`orders_vs_60d_pct=-0.2%`) e dentro da banda do dia da semana (`orders_vs_same_weekday_pct=-1.6%`, média histórica 92.5 pedidos). O que diverge de forma consistente é o ticket: R$55,91 vs R$41,86 da média de 60d (`ticket_vs_60d_pct=+33.6%`) e R$41,53 dos mesmos dias da semana. GMV +33.3% vs 60d e +32.4% vs mesmos dias da semana. A leitura é clara: o volume não cresceu, mas o GMV subiu de patamar pelo ticket — padrão consistente em todas as janelas disponíveis.

- **vs 30d:** `orders_vs_30d_pct=-8.9%`, `gmv_vs_30d_pct=+15.7%`, `ticket_vs_30d_pct=+27.0%`. A mesma dinâmica: volume levemente abaixo da média mensal, GMV acima. O ticket do dia não é anomalia isolada — está 27% acima da média dos últimos 30 dias, o que indica que o mix de maior valor se instalou ao longo do mês, não em um evento pontual.

- **vs 7d (janela mais recente):** `orders_vs_7d_pct=-20.9%`, `gmv_vs_7d_pct=-4.3%`. A média da semana (115,1 pedidos, R$5.315,70) é o pico recente. O volume caiu em relação a ela, mas o GMV caiu apenas 4.3%. Hipótese: os dias de maior volume da semana recente foram sustentados por anúncios de ticket menor. Sem diário anterior disponível no pacote, a hipótese permanece aberta.

- **Série mesmos dias da semana:** 65 pedidos (13/5, R$2.984), 87 (6/5, R$3.005), 134 (29/4, R$5.618), 84 (22/4, R$3.758). Alta volatilidade; o pico de 134 em 29/04 é outlier provável (evento ou promoção). Excluindo-o, média seria ~78.7 pedidos — o dia de ontem (91) estaria acima. GMV de R$5.087 é o maior entre os 4 pares históricos do dia da semana, inclusive acima do dia de 134 pedidos em volume. Reforça a tese de ticket estruturalmente mais alto sustentando GMV mesmo com volume mais baixo.

---

### Leitura estratégica

- **Lente 1 — Patamar vs banda:** Em múltiplas janelas independentes (60d: +33.3%, mesmos dias da semana: +32.4%, 30d: +15.7%), o GMV rompeu o patamar histórico sem que o volume tenha crescido. Isso caracteriza **ganho de valor médio por pedido, não ganho de alcance**. O ticket de R$55,91 está 34% acima do bimestre e 27% acima do mês — movimento de patamar confirmado em janela dupla. Se a causa é mix shift intencional (SKUs de maior valor ganhando peso), ADS puxando para itens mais caros, ou compressão de itens de baixo ticket por ruptura/pausa, não é distinguível com os dados disponíveis. O fato é: o patamar de GMV subiu por ticket, não por volume.

- **Lente 5 — ADS vs orgânico:** ADS (Himmel) gerou R$3.041,56 com investimento de R$262,19 — ROAS calculado de **11,6x**, ACOS de 4,33% (`ads_summary`). Esses valores representam **59,8% do GMV do dia** (R$3.041,56 / R$5.087,71): conta em zona de **ADS dominante**. O ROAS é excepcionalmente eficiente, mas a estrutura é frágil: 60% do faturamento depende de campanhas ativas de Himmel. Com `health` abaixo de 0.85 em dois dos top 5 (`MLB4073003575` health=0.75, `MLB3288536143` health=0.71), hipótese é que ADS está progressivamente compensando perda de exposição orgânica nesses anúncios — resultado financeiro visível estável, custo de manutenção crescente não detectável no número agregado.

- **Lente 3 — Dependência e fulfillment:** A base ativa tem 34.1% em Full (`account_overview.active_analysis.fulfillment_mix.full_pct`), mas a janela 30d mostra 73.9% dos pedidos via Full (`fulfillment_mix_30d.full_pct`) — divergência de 39.8 pp. Os anúncios Full representam 34% da base, mas geram 74% dos pedidos: **os campeões são exceção Full dentro de uma base majoritariamente Cross-Docking**. `paused=174` vs `active=82` (ratio 2.12x, acima do limiar de 1.5x) confirma cauda morta dominante. Os top 10 de ontem geraram apenas 56.3% Full (`fulfillment_mix_yesterday_top10.full_pct`) vs 73.9% do 30d — o campeão do dia (Conjunto 5 Potes Tampa Preta, 23 pedidos, `logistic_type=cross_docking`) puxou a composição de ontem para mais Cross-Docking do que o padrão mensal. Qualquer ruptura no mix Full afeta desproporcionalmente o faturamento.

- **Lente 2 — Exposição vs reputação:** `reputation.color=5_green`, `power_seller_status=gold`, `cancellations_rate=0`, `claims_rate=0.0025`, `delayed_handling_rate=0.001`. Estrutura de reputação limpa — a queda de volume vs 7d é hipótese de demanda/mix, não de exposição degradada pela reputação. Contudo, `low_health_count=7` na base ativa e health abaixo de 0.85 em dois anúncios campeões são deterioração de listing que **precede** impacto na reputação agregada — são sinais precoces que a métrica oficial ainda não captura.

---

### Tese da conta

A conta opera em **acomodação com ganho de patamar de ticket** — o volume permanece estável ao longo do bimestre, mas o GMV subiu estruturalmente pelo mix de maior valor, confirmado em janelas de 30d, 60d e controle de dia da semana. Contudo, a conta está **vulnerável**: ~60% do faturamento depende de ADS (Himmel) extremamente eficiente que pode estar mascarando erosão orgânica progressiva nos anúncios campeões (`MLB4073003575` health=0.75, `MLB3288536143` health=0.71). A cauda está morta (174 pausados vs 82 ativos), a base Full é estreita (34% da base gera 74% dos pedidos), e a memória histórica não tem tese anterior para confirmar se essa concentração e dependência de ADS são crônicas ou se aprofundaram recentemente. Classificação: **vulnerável** — números saudáveis sobre estrutura concentrada e ADS-dependente, sem segundo vetor visível em formação.

---

### Risco estrutural principal

- **Risco:** Dependência de Mercado Ads (Himmel) sustentando ~60% do GMV sobre anúncios campeões com `health` em deterioração progressiva.

- **Por que importa:** `MLB4073003575` (Kit 4 Potes 1050ml, 2º do dia, 13 pedidos) com `health=0.75` e `MLB3288536143` (Conjunto 5 Potes Tampa Vermelha, 5º do dia, 5 pedidos) com `health=0.71` estão abaixo do limiar de penalização ML (0.85) e perdem posição orgânica progressivamente. Com ADS representando 59.8% do GMV, as campanhas de Himmel provavelmente absorvem o tráfego que esses anúncios perderiam no orgânico — o resultado financeiro permanece visível e estável enquanto o orgânico se deteriora silenciosamente. Se as campanhas forem reduzidas ou pausadas, o GMV orgânico desses anúncios será menor do que o histórico sugere, porque parte crescente desse histórico já é ADS, não orgânico real.

- **Histórico:** Sem diário anterior disponível no pacote; não é possível confirmar se a `health` desses anúncios estava mais alta em semanas anteriores. Este é o primeiro registro documentado desse risco — candidato a risco estrutural, ainda não confirmado como deterioração recente.

- **Sinal de confirmação:** `health` de `MLB4073003575` abaixo de 0.70 **ou** de `MLB3288536143` abaixo de 0.65 no próximo ciclo com dado disponível, **e** ADS share permanecendo acima de 55% no mesmo período — confirmaria que ADS compensa erosão orgânica crescente, não amplifica orgânico saudável.

---

### Sinais a observar

1. **ADS share acima de 60% por 3 dias consecutivos** (`revenue_ads_yesterday_brl / totals.gmv`): confirmaria que o orgânico não sustenta o patamar atual de GMV e que a dependência de Himmel é estrutural, não episódica. Tornaria a classificação **vulnerável** mais grave.

2. **`health` de `MLB4073003575` (Kit 4 Potes 1050ml) caindo abaixo de 0.70 ou de `MLB3288536143` (Conjunto 5 Potes Tampa Vermelha) caindo abaixo de 0.65 no próximo ciclo com dado disponível**: confirmaria aceleração da penalização ML nos dois anúncios campeões com maior `sold_quantity` e alto giro histórico — risco de saída progressiva do ranking de categoria antes que apareça no GMV agregado.

3. **Ruptura de estoque em `MLB4410218897` (Kit 06 Canequinhas Acrílico) nos próximos 1-2 dias**: `available_quantity=3` com 3 pedidos gerados ontem — estoque praticamente zerado. Se o anúncio gerar novos pedidos sem reposição, há risco de cancelamento ou atraso que impacta `reputation.cancellations_rate` e `delayed_handling_rate` nos próximos ciclos. Sinal confirmado se o anúncio entrar em out-of-stock registrado ou gerar cancelamento capturado na métrica de reputação (se disponível no pacote).