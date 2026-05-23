<!-- llm_used=true model=gpt-5.5 fallback=false -->
### Leitura operacional do dia

- O dia funcionou mais por ticket do que por volume: `metrics.pedidos_validos=84` ficou abaixo de 30d (`historical.changes.orders_vs_30d_pct=-15,4%`) e dos mesmos dias da semana (`orders_vs_same_weekday_pct=-17,6%`), enquanto `metrics.gmv=4622,03` ficou acima de 30d (`gmv_vs_30d_pct=+3,4%`) e quase alinhado às sextas (`gmv_vs_same_weekday_pct=-2,1%`). Isso confirma operacionalmente a leitura da L01: não houve expansão de alcance, houve sustentação por `ticket_medio=55,02`, acima de 30d (`ticket_vs_30d_pct=+22,3%`).

- A venda ficou concentrada nos campeões do dia: o Conjunto 5 Potes de Vidro Redondos Tampa Preta fez `20` pedidos, cerca de 23,8% dos `84` pedidos válidos; `metrics.top3_concentration=48,8%` e `top5_concentration=64,3%`. Isso confirma o risco de dependência levantado pela L01, com um detalhe operacional importante: o campeão opera em Cross-Docking (`top_items_details[0].logistic_type=cross_docking`), puxando o mix dos top 10 para fora do padrão mensal.

- O mix de modalidade de envio dos campeões divergiu bastante do mês: `ml_snapshot.fulfillment_mix_yesterday_top10.full_pct=47,1%` e `cross_docking_pct=52,9%`, contra `fulfillment_mix_30d.full_pct=73,7%` e `cross_docking_pct=26,3%`. A divergência parece produto-específica, não sistêmica, porque a base ativa da conta é majoritariamente Cross-Docking (`account_overview.active_analysis.fulfillment_mix.cross_docking_pct=66,7%`), mas o histórico de pedidos recentes era majoritariamente Full. Isso adiciona evidência à cautela da L02 de não tomar decisão estrutural de modalidade de envio hoje.

- ADS sustentou grande parte do resultado com eficiência alta: `ads_summary.revenue_ads_yesterday_brl=3228,78` sobre `recipient.totals.gmv=4622,03` dá share de aproximadamente 69,9%; `spend_yesterday_brl=296,96` dá ROAS aproximado de 10,9x e `avg_acos_pct=4,57`. Operacionalmente, isso reforça a L01 e a L02: Mercado Ads está dominante, mas não ineficiente; mexer nele hoje confundiria a leitura do que é dependência e do que é campanha saudável.

### Sinais operacionais relevantes

- **Sinal:** queda de pedidos sem queda proporcional de GMV — **interpretação operacional:** o dia não perdeu faturamento porque o mix vendido teve ticket maior; `orders_vs_30d_pct=-15,4%` com `gmv_vs_30d_pct=+3,4%` e `ticket_vs_30d_pct=+22,3%` mostra sustentação por valor médio, não por tração de volume.

- **Sinal:** campeão Cross-Docking liderou o dia — **interpretação operacional:** o Conjunto 5 Potes de Vidro Redondos Tampa Preta fez `20` pedidos e opera em Cross-Docking, ajudando a inverter o mix dos top 10 para `cross_docking_pct=52,9%` versus `26,3%` no 30d; isso é desvio relevante de execução, mas concentrado em produto.

- **Sinal:** dois campeões Full seguem com health abaixo do limiar observado pela L01/L02 — **interpretação operacional:** Kit 4 Potes de Vidro 1050ml Retangular tem `health=0,75` e Conjunto 5 Potes de Vidro Redondos Tampa Vermelha tem `health=0,71`; como ambos venderam bem ontem (`11` e `10` pedidos), a conta continua realizando venda em anúncios com penalização ativa ou potencialmente limitada.

- **Sinal:** item Full de canecas ficou com estoque curto pós-baixa — **interpretação operacional:** Kit 6 Canecas Porcelana Tulipa Lisa 250ml vendeu `6` pedidos e está com `available_quantity=9` no snapshot pós-baixa; não há problema retroativo nos pedidos de ontem, mas há risco prospectivo de ruptura se mantiver ritmo parecido nos próximos ciclos.

- **Sinal:** houve `1` cancelamento no dia enquanto `reputation.cancellations_rate=0` — **interpretação operacional:** o cancelamento diário é sinal precoce isolado, ainda sem reflexo na reputação de janela longa; não caracteriza deterioração de exposição, mas merece separação por anúncio se repetir.

### Anomalias ou ausência de anomalia

**anomalia leve** — a execução teve desvios perceptíveis, mas sem bloqueio operacional: volume abaixo das referências, GMV sustentado por ticket, mix dos top 10 deslocado para Cross-Docking e ADS share em 69,9%. A reputação segue verde (`reputation.color=5_green`), `cancellations_rate=0`, os anúncios campeões estão ativos e o cancelamento do dia foi isolado. Subiria para moderada se o mesmo conjunto persistir por mais ciclos com pedidos abaixo de 90, ADS share ≥60% e health dos campeões abaixo de 0,80; desceria se o volume voltar à banda sem depender tanto de ADS ou de poucos campeões.

### O que precisa ser investigado pela Granular

- **Pergunta:** o Conjunto 5 Potes de Vidro Redondos Tampa Preta concentrou vendas em algum horário específico ou vendeu distribuído ao longo do dia? — **motivada por:** liderança do campeão Cross-Docking e alteração do mix de modalidade de envio dos top 10.

- **Pergunta:** a receita de ADS veio principalmente dos campeões com health baixo ou do campeão Cross-Docking sem health calculado? — **motivada por:** ADS share de aproximadamente 69,9% combinado com divergência de modalidade de envio e campeões penalizados.

- **Pergunta:** o health de Kit 4 Potes de Vidro 1050ml Retangular (`0,75`) e Conjunto 5 Potes de Vidro Redondos Tampa Vermelha (`0,71`) está caindo, estável ou recuperando nos últimos dias? — **motivada por:** repetição do risco apontado pela L01/L02, ainda sem série temporal suficiente.

- **Pergunta:** o Kit 6 Canecas Porcelana Tulipa Lisa 250ml tem reposição confirmada ou estoque real adicional fora do Full? — **motivada por:** `available_quantity=9` pós-baixa após `6` pedidos no dia, com risco prospectivo de ruptura.

- **Pergunta:** o cancelamento do dia pertenceu a algum dos campeões ou a item fora do top 10? — **motivada por:** `metrics.cancelamentos=1` ainda isolado contra `reputation.cancellations_rate=0`, mas relevante se estiver concentrado em anúncio crítico.

### Destaque para a Condensadora

O fato operacional mais importante é que o dia preservou GMV por ticket e ADS, não por volume, enquanto a execução ficou concentrada em poucos produtos e com mix dos top 10 mais Cross-Docking do que o padrão mensal. Isso reforça a leitura L01/L02 de dependência, mas sem justificar ação sobre ADS hoje porque a eficiência segue alta; o risco silencioso é a combinação de campeões com health baixo e item Full de canecas com pouca cobertura pós-baixa, que pode distorcer os próximos dias se virar ruptura ou perda de exposição.