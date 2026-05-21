<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` são templates vazios — sem consolidação semanal ou tese mensal populada. Yasmin é focal point desde 22/04/2026 (~4 semanas), então a base narrativa está em formação. Compensação parcial: dados numéricos de 7d, 30d e 60d estão presentes e coerentes; `ml_snapshot` completo com reputação, fulfillment, ads_summary e account_overview. Sem hipóteses ativas anteriores para confirmar ou refutar — leitura de hoje serve como ponto de ancoragem inicial.

---

### Leitura temporal

- **Vs 60d e mesmos dias da semana:** GMV `+33.3%` vs `historical.avg_60d.avg_gmv=R$3.817,90` e `+32.4%` vs `same_weekday_avg.avg_gmv=R$3.841,73` — sinal consistente em duas janelas independentes. Orders praticamente estáveis: `-0.2%` vs 60d e `-1.6%` vs mesmo dia da semana. O ganho de GMV não veio de alcance — o ticket passou de R$41,86 (60d) para R$55,91 hoje (`changes.ticket_vs_60d_pct=+33.6%`).

- **Vs 30d:** `gmv_vs_30d_pct=+15.7%`, `orders_vs_30d_pct=-8.9%`, `ticket_vs_30d_pct=+27.0%`. A leitura se sustenta na janela mais curta: crescimento de GMV com compressão de volume é o padrão do mês, não do dia.

- **Vs 7d:** `gmv_vs_7d_pct=-4.3%`, `orders_vs_7d_pct=-20.9%`. O dia ficou abaixo da média semanal recente (`avg_7d.avg_orders=115.1`, `avg_7d.avg_gmv=R$5.315,70`). A distância entre a média 7d e a média 30d (115 vs 99,9 pedidos) indica que dias recentes foram acima do ritmo do mês — ontem pode ser acomodação dentro de um pico de 7d ou início de desaceleração; com memória diária ausente, não há como distinguir entre os dois.

- **Controle de sazonalidade:** os 4 últimos mesmos dias da semana foram R$2.984 / R$3.005 / R$5.618 / R$3.758. Ontem (R$5.087) está acima da média do grupo (R$3.841) e próximo ao pico de 29/04. O dia não foi fraco — foi forte para o dia da semana, reforçando a leitura de ganho de ticket, não de retração.

---

### Leitura estratégica

- **Ticket como único vetor de crescimento, não volume.** O ticket expandiu de R$41,86 (60d) para R$55,91 (+33.6%), confirmado em 30d (+27%) e no controle de dia da semana (+34.6% sobre `same_weekday_avg.avg_ticket=R$41,53`). A hipótese mais provável: deslocamento de mix em direção a kits de maior valor unitário — Kit 4 Potes 1050ml (`MLB4073003575`, 13 pedidos, ~R$70+ médio) e Kit 10 Potes 1050ml (`MLB4676726433`, 5 pedidos, ticket elevado). O alcance da conta está estagnado; o resultado cresce por composição, não por amplitude.

- **ADS Himmel como vetor primário, não amplificador.** `ml_snapshot.ads_summary.revenue_ads_yesterday_brl=R$3.041,56` sobre `gmv=R$5.087,71` representa **ADS share de 59,8%** — zona de ADS dominante. ROAS calculado: R$3.041,56 / R$262,19 = **11,6x**; ACOS 4,64% — eficiência extrema, mas que mascara a fragilidade latente: o orgânico carrega ~R$2.046 do dia (~40%). A eficiência da campanha Himmel é real; a dependência estrutural também.

- **Campeões são atípicos vs base em fulfillment e health.** Mix do top10 de ontem: Full 56,3%, Cross-docking 43,7% (`fulfillment_mix_yesterday_top10`). Mix da base ativa inteira: Full 34,1%, Cross-docking 65,9% (`account_overview.active_analysis.fulfillment_mix`). Os campeões operam com quase o dobro de Full em relação à média da conta. Simultaneamente, dois campeões com volume expressivo têm health degradada: Kit 4 Potes 1050ml (`MLB4073003575`, health=0,75, 13 pedidos) e Conjunto 5 Potes Tampa Vermelha (`MLB3288536143`, health=0,71, 5 pedidos). Health abaixo de 0,85 implica penalização progressiva no orgânico por parte do ML — o que, em conta ADS-dependente, reduz o orgânico residual sem aviso no agregado.

- **Cauda morta dominante e ponto de ruptura em estoque.** 174 anúncios pausados vs 82 ativos (`account_overview.totals`) — razão de 2,1x: a conta opera concentrada em poucos SKUs ativos. Kit 06 Canequinhas Acrílico (`MLB4410218897`, status=active) tem `available_quantity=3` após gerar 3 pedidos ontem — estoque efetivamente zerado. Kit 6 Canecas Porcelana Tulipa (`MLB6167272090`, status=active, Full) tem `available_quantity=21` com ritmo de 5 pedidos/dia — aproximadamente 4 dias de estoque em CD do ML, com lead time de reposição.

---

### Tese da conta

**Vulnerável.** O GMV acima da banda histórica (+33,3% vs 60d) é consistente em múltiplas janelas e confirmado pelo controle de sazonalidade — o patamar é real. Mas a estrutura por trás dele descansa em dois vetores frágeis: Mercado Ads como fonte primária de ~60% do GMV e expansão de ticket sem crescimento de volume. Reputação `5_green` com `power_seller_status=gold` e `cancellations_rate=0` limpam o risco de exposição estrutural no curto prazo. O perigo não é o resultado de hoje — é que o patamar atual exige campanhas ativas, anúncios campeões saudáveis e estoque de Full sem ruptura. A combinação de health degradada em dois dos três maiores anúncios, estoque crítico em Kit 06 Canequinhas Acrílico e ADS share dominante cria um portfólio de vulnerabilidades que não aparece no número do dia.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads como vetor primário do GMV (ADS share 59,8%), sem evidência de que o orgânico sustenta o patamar atual de forma autônoma.

**Por que importa:** Qualquer redução de verba, pausa de campanha ou queda de eficiência nas 11 campanhas ativas (Himmel) pode resultar em queda imediata de R$2.000–R$3.000/dia. O orgânico que sustenta os 40% restantes depende de anúncios com health degradada (MLB4073003575, MLB3288536143) e de campeões com estoque em risco de ruptura — o que comprime ainda mais o piso orgânico.

**Histórico:** `weekly.md` e `monthly.md` em branco — sem como confirmar se esse nível de ADS share é recente ou padrão da conta desde antes de 22/04. A ausência de histórico narrativo impede classificar se é escalada recente ou equilíbrio já estabelecido.

**Sinal de confirmação:** ADS share acima de 55% por 3 dias consecutivos (com `ads_summary` disponível no pacote) confirmaria que a dependência de mídia não é pontual — é o modelo operacional atual da conta.

---

### Sinais a observar

1. **Ruptura iminente em Kit 06 Canequinhas Acrílico (`MLB4410218897`):** `available_quantity=3` após 3 pedidos ontem. Se o anúncio aparecer com `out_of_stock_count` incrementado ou zero pedidos por 2 dias seguidos, ruptura confirmada — acionar Yasmin para verificar reposição ou pausa preventiva antes de impactar `cancellations_rate` da conta.

2. **Health dos campeões Kit 4 Potes 1050ml e Conjunto 5 Potes Tampa Vermelha:** MLB4073003575 (health=0,75) e MLB3288536143 (health=0,71). Se qualquer um cair abaixo de 0,70 ou se o volume de pedidos desses dois anúncios recuar mais de 30% em relação ao ritmo atual por 2 dias seguidos, confirma penalização ML em progressão no orgânico — risco amplificado pela ADS dependência.

3. **Estoque em Full de Kit 6 Canecas Porcelana Tulipa (`MLB6167272090`):** `available_quantity=21`, ritmo de 5 pedidos/dia, logistic_type Full. Se `available_quantity` não aparecer reposto nos próximos 3 dias, ruptura em CD do ML é prospectiva — com lead time de reabastecimento Full, o impacto aparece antes da reação ser possível.