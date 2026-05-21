<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- **O GMV do dia foi sustentado integralmente por ticket, não por alcance.** 91 pedidos praticamente idênticos ao bimestre (`changes.orders_vs_60d_pct=-0.2%`) e dentro da banda sazonal (`orders_vs_same_weekday_pct=-1.6%`), enquanto GMV subiu +33.3% vs 60d e +32.4% vs mesmos dias da semana. Ticket de R$55.91 vs R$41.86 (60d) = +33.6%, confirmado em 30d (+27.0%) e no controle sazonal (+34.6% sobre `same_weekday_avg.avg_ticket=R$41.53`). Confirma operacionalmente a tese da L01 de patamar via composição de mix, não por crescimento de alcance.

- **O campeão do dia opera em Cross-docking e desequilibrou o mix de fulfillment.** O Conjunto 5 Potes Tampa Preta liderou com 23 pedidos (~25.3% do volume individual) em `logistic_type=cross_docking`, puxando `fulfillment_mix_yesterday_top10.full_pct` para 56.3% — distante do padrão de 30d (73.9%) e de 7d (77.7%). Divergência produto-específica, não sistêmica: sem esse único anúncio no topo, o mix do dia estaria próximo da banda histórica. Isso evidencia operacionalmente o que a L01 apontou sobre a base Full da conta ser estreita — o mix diário é altamente sensível ao produto que lidera.

- **Dois campeões em Full com health degradada geraram volume relevante mas sob penalização orgânica ativa.** Kit 4 Potes 1050ml Retangular (`MLB4073003575`, health=0.75, 13 pedidos, #2 do dia) e Conjunto 5 Potes Tampa Vermelha (`MLB3288536143`, health=0.71, 5 pedidos) somaram 18 pedidos com penalização de ranking no ML em curso. Em dia de ADS share dominante (59.8%), a penalização orgânica fica mascarada pelo tráfego pago — a conversão aparece no agregado, mas o custo está sendo absorvido pela campanha Himmel. Adiciona evidência operacional ao risco estrutural identificado pela L01.

- **ADS realizado em 59.8% do GMV com ROAS 11.6x — eficiente, mas concentrado num dia de mix divergente.** `ads_summary.revenue_ads_yesterday_brl=R$3.041,56` / `gmv=R$5.087,71` = 59.8% de share; ROAS: R$3.041,56 / R$262.19 = 11.6x; ACOS 4.64%. A eficiência da campanha Himmel é real. O dado operacional que a Condensadora precisa saber é que esse share dominante coincidiu com o dia em que o produto que liderou o volume é Cross-docking — se a campanha está priorizando o Conjunto 5 Potes Tampa Preta, o crescimento de GMV está sendo construído sobre estrutura de fulfillment distante do padrão mensal.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas com Suporte de Madeira Acrílico (`MLB4410218897`, status=active) gerou 3 pedidos com `available_quantity=3` — estoque efetivamente zerado ao final do dia, anúncio permanecendo ativo. — **Interpretação operacional:** qualquer pedido gerado hoje já configura cancelamento prospectivo que compromete `reputation.cancellations_rate=0`. Confirma e adiciona urgência operacional ao sinal #1 da L01 e à ação #1 da L02 — a janela de 24h começa neste ciclo, não amanhã.

- **Sinal:** O campeão do dia (Conjunto 5 Potes Tampa Preta, Cross-docking, 23 pedidos) puxou `fulfillment_mix_yesterday_top10.full_pct` para 56.3%, contra 73.9% no padrão 30d e 77.7% no 7d. — **Interpretação operacional:** divergência produto-específica confirmada; a base Full da conta é concentrada em poucos anúncios, e o mix diário oscila significativamente conforme qual campeão domina. O padrão 7d mais recente (77.7% Full) sugere que dias recentes tiveram perfil de campeão diferente do de ontem.

- **Sinal:** ADS share de 59.8% em dia em que o campeão de volume é Cross-docking — coincidência ou causalidade não verificável sem a composição do `revenue_ads` por anúncio. — **Interpretação operacional:** se a campanha Himmel está priorizando o Conjunto 5 Potes Tampa Preta, o crescimento de GMV está sendo viabilizado sobre uma estrutura de fulfillment menos vantajosa do que o histórico mensal — sem evidência de problema hoje, mas sinal operacional relevante que a Granular precisa confirmar ou descartar.

- **Sinal:** Kit 4 Potes 1050ml Retangular (`MLB4073003575`, #2 do dia, 13 pedidos) opera em Full com `health=0.75` — abaixo do limiar 0.85, com penalização de ranking no ML ativa. — **Interpretação operacional:** em dia de ADS share dominante, o tráfego pago compensa a perda orgânica e o produto ainda converte — mas isso mascara a erosão. Adiciona evidência à hipótese da L01 e à ação #3 da L02: sem saber a direção do health (caindo/estável/recuperando), não é possível saber se a compensação de ADS é provisória ou se está segurando uma queda progressiva.

- **Sinal:** Kit 6 Canecas Porcelana Tulipa Lisa 250ml (`MLB6167272090`, `is_catalog=true`, `logistic_type=fulfillment`, `available_quantity=21`) gerou 5 pedidos no dia — cobertura implícita de ~4 dias no CD do ML. — **Interpretação operacional:** anúncio em catálogo Full com estoque em janela de alerta; ruptura em catálogo Full demora mais para recuperar posição do que ruptura em clássico, e o lead time de reposição em CD não permite reação tardia. Confirma o sinal #3 da L01.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.** O dia apresentou dois desvios operacionais isolados e identificados: (1) Kit 06 Canequinhas Acrílico zerou estoque com anúncio ativo — risco de cancelamento prospectivo em janela de 24h; (2) mix de fulfillment divergiu do padrão 30d por efeito de um único produto no topo (56.3% Full vs 73.9%). Nenhum dos dois configura bloqueio de execução hoje — reputação limpa (`5_green`, `cancellations_rate=0`, `power_seller_status=gold`), sem anúncios pausados com pedidos e sem out_of_stock confirmado. A classificação sobe para **moderada** se amanhã: o Kit 06 Canequinhas seguir ativo e gerar novo pedido sem estoque, ou se o health de MLB4073003575 ou MLB3288536143 recuar mais um ponto. Permanece **leve** se a ação da L02 (verificação de estoque e pausa preventiva) for executada hoje.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual é a composição do `revenue_ads_yesterday_brl` por anúncio — quais produtos a campanha Himmel estava empurrando ontem? — **Motivada por:** ADS share de 59.8% num dia em que o campeão de volume é Cross-docking (Conjunto 5 Potes Tampa Preta); se o produto #1 foi impulsionado pelo ADS, explica simultaneamente o mix divergente e sustenta a hipótese de que o GMV do dia está sendo construído sobre estrutura de fulfillment diferente do padrão histórico.

- **Pergunta:** Qual é a direção do health de MLB4073003575 (Kit 4 Potes 1050ml, health=0.75) e MLB3288536143 (Conjunto 5 Potes Tampa Vermelha, health=0.71) — estabilizando, caindo ou recuperando? — **Motivada por:** ambos geraram volume relevante (#2 e #5 do dia) com penalização ativa; a decisão da L02 entre observação e acionamento de Himmel para cobertura preventiva depende diretamente dessa direção.

- **Pergunta:** Qual o `available_quantity` atual do Kit 06 Canequinhas Acrílico (MLB4410218897) e quantos pedidos já foram gerados hoje? — **Motivada por:** anúncio ativo com estoque zerado ao final do dia de ontem; cada pedido adicional hoje é cancelamento prospectivo que compromete `reputation.cancellations_rate=0`.

- **Pergunta:** Há reposição programada para o Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full, is_catalog, available=21) com chegada em CD em ≤3 dias? — **Motivada por:** cobertura implícita de ~4 dias e anúncio em catálogo Full — ruptura nessa modalidade tem recuperação mais lenta do que em clássico, e o lead time de reabastecimento Full não permite ação reativa.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o número forte — é a sobreposição silenciosa entre dois elementos: o ADS share de 59.8% e o campeão do dia em Cross-docking. Se a campanha Himmel está priorizando o Conjunto 5 Potes Tampa Preta (único campeão viável com estoque farto e `health=null` sem penalização visível), o crescimento de GMV está sendo construído sobre uma estrutura de fulfillment distante do padrão mensal (56.3% Full vs 73.9%), enquanto os campeões em Full com health degradada (Kit 4 Potes 1050ml e Conjunto 5 Potes Tampa Vermelha) convertem mas com erosão orgânica mascarada pelo tráfego pago. Isso não aparece no agregado do dia — o resultado é bom. O risco silencioso é que a conta pode estar sistematicamente depriorizado seus campeões Full (que acumulam saúde degradada) enquanto ADS empurra o Cross-docking de topo — um desequilíbrio que só fica visível quando a campanha recuar ou quando o health cair mais. A Condensadora deve decidir se esse sinal tem peso suficiente para ir além da ação de estoque pontual que a L02 já estruturou.