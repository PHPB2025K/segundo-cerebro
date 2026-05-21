<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` carregados mas sem conteúdo histórico — apenas templates vazios sem nenhuma entrada documentada. Nenhuma hipótese anterior existe para confirmar ou refutar; esta leitura é ponto de partida da memória, não validação de ciclo. Dados ML opcionais robustos: reputação, mix de fulfillment (7d, 30d, top10 do dia), health individual dos campeões e ADS summary disponíveis com cobertura 100% — base técnica sólida para a análise de hoje.

---

### Leitura temporal

- **Trajetória de patamar em 60d:** GMV médio saiu de R$3.817 (60d) → R$4.396 (30d) → R$5.315 (7d), com ticket acompanhando: R$41,86 → R$44,03 → R$46,17. O dia (`gmv=R$5.087`, `ticket_vs_60d_pct=+33,6%`) está acima da banda do 30d (+15,7%) e bem acima do 60d (+33,3%). A conta não oscila dentro de uma banda — ela veio subindo de patamar ao longo do bimestre. O dia de ontem é leitura dentro desse patamar elevado, não rompimento acima dele.

- **Divergência volume vs ticket:** Orders ontem (91) abaixo da média 30d (99,9, `orders_vs_30d_pct=-8,9%`) e muito abaixo da média 7d (115,1, `orders_vs_7d_pct=-20,9%`), mas o GMV superou ambos. O controle de sazonalidade confirma: 91 pedidos vs média das últimas 4 quartas-feiras (92,5 pedidos, `orders_vs_same_weekday_pct=-1,6%`) — volume ontem foi absolutamente normal para uma quarta. O GMV de R$5.087 vs média dessas mesmas quartas (R$3.841, `gmv_vs_same_weekday_pct=+32,4%`) é ganho de ticket, não de alcance. O GMV só ficou abaixo de uma das últimas 4 quartas homólogas (2026-04-29, R$5.618 — que parece ter sido dia atípico). A trajetória de GMV é sustentada por mix de valor, não por crescimento de volume.

- **7d elevado — possível distorção por pico pontual:** A média 7d de 115,1 pedidos sugere dias com volume acima do padrão histórico na semana corrente. Ontem, ao registrar 91 pedidos, ficou abaixo dessa média — mas sem daily anterior documentado, não é rastreável qual dia da semana foi responsável pelo pico que elevou a média 7d. Leitura inconclusiva sobre se ontem representa desaceleração ou simplesmente retorno à linha base pós-pico.

- **Hipóteses anteriores:** Memória semanal e mensal vazias. Nada a confirmar, enfraquecer ou refutar.

---

### Leitura estratégica

- **Ticket como vetor estrutural, não volume:** A conta construiu +33,3% de GMV em 60d com volume praticamente estável (`orders_vs_60d_pct=-0,2%`). Ontem o ticket chegou a R$55,91 — 21% acima até da média 7d (R$46,17). Os top 10 do dia incluem kits de maior valor (Kit 10 Potes a R$~100+, Kit 2 Potes com 8 unidades em 3 pedidos — média de 2,67 unidades/pedido), sugerindo migração de mix para produtos de maior valor médio como possível motor. Hipótese plausível, não confirmada sem série histórica de mix de produto documentada.

- **ADS dominante com eficiência extrema — fragilidade latente real:** Himmel gerou R$3.041,56 (`ads_summary.revenue_ads_yesterday_brl`) com R$262,19 de gasto (`spend_yesterday_brl`) — ROAS 11,6x, ACOS 4,64% (`avg_acos_pct`). Esses números representam **59,8% do GMV do dia** (R$3.041/R$5.087), colocando a conta em zona de **ADS dominante**. A eficiência é excepcional, mas o risco é estrutural: se as 11 campanhas ativas forem pausadas ou reduzirem alcance, o orgânico precisaria absorver ~R$3.000/dia sem suporte de mídia paga — e os dois maiores drivers Full têm health degradada (ver próximo bullet). Campanha eficiente não neutraliza exposição orgânica em deterioração.

- **Health dos campeões como erosão silenciosa de orgânico:** Kit 4 Potes 1050ml Retangular (MLB4073003575, #2 com 13 pedidos) tem `health=0,75` — 10 pontos abaixo do limiar ML de penalização (0,85). Conjunto 5 Potes Tampa Vermelha (MLB3288536143, #5 com 5 pedidos) tem `health=0,71`. Ambos são Full com estoque adequado (166 e 362 unidades) — a health degradada não deriva de ruptura logística. Em contexto de 59,8% ADS share, a hipótese é que o tráfego pago mascare a perda de posição orgânica desses anúncios: eles vendem via campanha, mas acumulam penalização de ranking natural. Sem dado de posição de categoria, é hipótese plausível e falsificável, não fato confirmado.

- **Divergência de fulfillment: o #1 vendedor está fora do Full:** Conjunto 5 Potes Tampa Preta (MLB4535865317, 23 pedidos — 25,3% do volume do dia) opera em `cross_docking`, não Full. A janela 7d aponta Full em 77,7% e a 30d em 73,9% do volume total da conta, mas o top 10 de ontem ficou em apenas 56,3% Full (`fulfillment_mix_yesterday_top10.full_pct`) — a divergência vem diretamente do #1, que puxa o mix do dia para baixo do padrão recente. A base ativa como um todo é 34,1% Full (`account_overview.active_analysis.fulfillment_mix.full_pct`), muito abaixo dos campeões — confirmando que Full está concentrado no giro alto, não na cauda. Com 174 anúncios pausados vs 82 ativos, a cauda viva é pequena e o portfólio depende de poucos itens Full para sustentar o patamar de volume.

---

### Tese da conta

A conta ML está **vulnerável** — não pelos números de hoje, que estão acima da banda histórica em GMV e ticket, mas pela estrutura que os sustenta. O ganho de patamar dos últimos 60d se apoia em dois pilares frágeis: campanhas Himmel respondendo por ~60% do GMV com eficiência excepcional, mas sem orgânico robusto como plano B; e dois dos maiores drivers Full acumulando penalização de health progressiva (`health=0,75` e `health=0,71`) sem sinal de reversão observável. A reputação `5_green/gold` (`reputation.color`, `power_seller_status`) preserva a base estrutural, e a ausência de hipóteses anteriores documentadas impede confirmar se essa combinação é padrão antigo ou degradação recente — o que eleva a incerteza. Classificação **vulnerável** é a mais honesta dado o estado da memória e a evidência disponível.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads como vetor dominante do GMV (59,8% do dia, `ads_summary.revenue_ads_yesterday_brl / metrics.gmv`) sem suporte orgânico sólido nos campeões — evidenciado por health degradada em Kit 4 Potes 1050ml Retangular (`health=0,75`, `MLB4073003575`) e Conjunto 5 Potes Tampa Vermelha (`health=0,71`, `MLB3288536143`), os dois principais drivers Full da conta.

**Por que importa:** Se as campanhas reduzirem investimento, forem pausadas ou perderem qualidade de score, o orgânico que deveria absorver o volume está enfraquecido justamente nos anúncios de maior giro em Full. A dinâmica pode se tornar não linear: menos ADS → menos vendas → health continua deteriorando → menos orgânico → espiral de exposição que não se resolve adicionando verba de volta.

**Histórico:** Sem memória anterior documentada, não é possível afirmar se essa dependência é nova (período pós-assunção de Yasmin em 22/04) ou padrão crônico. Risco identificado pela primeira vez nesta leitura — não confirmado por série, mas sustentado pelos dados do dia.

**Sinal de confirmação:** ADS share acima de 55% por 3 dias consecutivos confirma que 59,8% não é anomalia de um dia. Combinado com health do Kit 4 Potes 1050ml (`MLB4073003575`) permanecendo abaixo de 0,80 nos próximos 2 ciclos com dado disponível, configura dependência estrutural confirmada.

---

### Sinais a observar

1. **ADS share acima de 50% por 3 dias seguidos** (calculado como `revenue_ads_brl / gmv_total` no pacote diário) confirma que a dependência de 59,8% de hoje é padrão estrutural, não pico pontual de campanha.

2. **Kit 4 Potes 1050ml Retangular (MLB4073003575) registrando menos de 10 pedidos/dia por 2 dias consecutivos** confirmaria que a `health=0,75` já se traduz em perda de exposição orgânica observável — sinal especialmente relevante em dias sem pico de campanha ADS.

3. **Kit 06 Canequinhas Acrílico (MLB4410218897) com `available_quantity` zerado ou anúncio pausado nos próximos 2 dias** confirma ruptura iminente: o anúncio encerrou ontem com 3 unidades e registrou 3 pedidos no dia — estoque praticamente nulo, com risco de cancelamentos afetando `reputation.cancellations_rate` nos próximos ciclos.