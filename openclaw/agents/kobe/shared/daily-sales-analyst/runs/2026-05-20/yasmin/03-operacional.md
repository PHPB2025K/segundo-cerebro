<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O dia foi sustentado integralmente por ticket, não por volume. 91 pedidos praticamente idênticos ao bimestre (`changes.orders_vs_60d_pct=-0,2%`) e dentro da banda do mesmo dia da semana (`orders_vs_same_weekday_pct=-1,6%`), enquanto o GMV avançou +33,3% vs 60d e +32,4% vs mesmos dias da semana. Confirma operacionalmente a leitura da L01 de patamar via ticket — o canal não acelerou em alcance, mas em valor médio por pedido. O resultado de R$5.087,71 não foi fruto de um dia excepcionalmente forte em volume, mas de mix de produtos de maior valor unitário convertendo no patamar habitual de alcance.

- O resultado ficou apoiado em poucos produtos — `top3_concentration=48,4%` e `top5_concentration=59,3%` — e o campeão do dia (Conjunto 5 Potes de Vidro Redondos Tampa Preta, 23 pedidos, ~25,3% do volume) opera em cross_docking. Isso puxou o `fulfillment_mix_yesterday_top10.full_pct` para 56,3%, versus 73,9% no 30d e 77,7% no 7d — divergência de ~17pp. A distorção é produto-específica, não sistêmica: um único anúncio com volume expressivo em cross_docking foi suficiente para comprimir o Full share do dia. Adiciona evidência operacional à leitura da L01 sobre base Full estreita: o mix Full "elevado" do histórico não é garantia estrutural — é função de qual produto lidera o dia.

- Os dois campeões de alto giro com health degradada identificados pela L01 continuaram convertendo ontem: Kit 4 Potes 1050ml Retangular (`health=0,75`, 13 pedidos, fulfillment) e Conjunto 5 Potes Tampa Vermelha (`health=0,71`, is_catalog=true, 5 pedidos, fulfillment). O fato de manterem pedidos com health abaixo do limiar de penalização ML (0,85) confirma operacionalmente a hipótese da L01: a campanha de ADS está sustentando a exposição que o algoritmo orgânico está retirando. A continuidade de vendas não sinaliza recuperação de health — pode ser inteiramente efeito de cobertura de mídia paga. Sem trajetória histórica (weekly/monthly vazios), impossível saber se 0,75 e 0,71 são estáveis ou em queda.

- O Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico (`MLB4410218897`, `available_quantity=3` na abertura do dia, `logistic_type=fulfillment`, `status=active`) gerou 3 pedidos. O dia fechou com `metrics.cancelamentos=3`. A sobreposição — 3 unidades disponíveis, 3 pedidos gerados, 3 cancelamentos no fechamento — sugere que ruptura e cancelamento podem ter se realizado simultaneamente. A origem dos cancelamentos é desconhecida, mas a coincidência de volumes é o dado operacional mais crítico do dia. Confirma e adiciona urgência ao sinal levantado pela L01 e à ação prioritária definida pela L02: a janela de prevenção pode já ter fechado.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas Acrílico (`MLB4410218897`) abriu o dia com `available_quantity=3`, gerou 3 pedidos com `status=active`, e o dia fechou com `metrics.cancelamentos=3` — **interpretação operacional:** se os cancelamentos são concentrados nesse anúncio, a ruptura já ocorreu e a `reputation.cancellations_rate` (hoje `=0` na janela longa) começa a ser contaminada. A janela identificada pela L01 como "24h antes que o ML cancele pedidos" pode já ter expirado ontem.

- **Sinal:** Fulfillment mix do dia (56,3% Full) ficou 17,6pp abaixo do 30d (73,9%) e 21,4pp abaixo do 7d (77,7%), inteiramente puxado pelo Conjunto 5 Potes Tampa Preta — um único anúncio cross_docking com 23 pedidos — **interpretação operacional:** a proporção de Full no resultado é função de quais produtos lideram o dia, não de composição estável da conta. O mix histórico elevado em Full não oferece buffer real se os campeões do dia forem cross_docking.

- **Sinal:** Conjunto 5 Potes Tampa Vermelha (`MLB3288536143`, `is_catalog=true`, `health=0,71`) e Kit 4 Potes 1050ml Retangular (`MLB4073003575`, `health=0,75`) mantiveram conversão com health abaixo do limiar — **interpretação operacional:** ADS cobriu a perda de exposição orgânica nesses dois anúncios também ontem. Sem trajetória de health disponível, não é possível distinguir entre estabilização e deterioração contínua — o que define a urgência de ação da L02.

- **Sinal:** Kit 6 Canecas Porcelana Tulipa Lisa 250ml (`MLB6167272090`, `is_catalog=true`, `fulfillment`, `available_quantity=21`, 5 pedidos no dia) — **interpretação operacional:** ao ritmo de 5 pedidos/dia, runway estimado de ~4 dias. Não é urgência de 24h como o Canequinhas Acrílico, mas o anúncio está em catálogo — recuperação de posição após ruptura é mais lenta. Sinal adjacente que merece monitoramento no ciclo seguinte.

- **Sinal:** ADS respondeu por ~59,8% do GMV do dia (`ads_summary.revenue_ads_yesterday_brl=R$3.041,56` / `totals.gmv=R$5.087,71`) com ROAS 11,6x e ACOS 4,64%, num dia em que o mix de fulfillment estava distorcido pelo líder cross_docking — **interpretação operacional:** a campanha de Himmel sustentou resultado alto num dia em que a composição de fulfillment era menos vantajosa que o histórico. A eficiência é alta, mas o volume de ADS correndo sobre estrutura Full comprimida (~56% vs ~74% habitual) é informação operacional relevante para a série de observação de ADS share que a L02 definiu como registro de linha de base.

---

### Anomalias ou ausência de anomalia

**anomalia leve** — com risco de upgrade para moderada dependendo da origem dos cancelamentos.

O dia se manteve dentro das bandas esperadas em volume e GMV (confirmado pelo controle de mesmo dia da semana), sem ruptura de reputação ou exposição. A anomalia operacional perceptível é isolada: o Kit 06 Canequinhas Acrílico (`MLB4410218897`) pode ter zerado estoque no próprio dia gerando os 3 cancelamentos, e o mix de fulfillment divergiu ~17pp do 30d por razão produto-específica. Nenhum dos desvios, isoladamente, aponta para causa acumulada ou ruptura sistêmica. O que sobe para **anomalia moderada**: confirmação de que os 3 cancelamentos se originam desse anúncio — dois desvios simultâneos com causa comum (estoque zero → cancelamento → impacto em `cancellations_rate`) já qualificam nível moderado e colocam a reputação (hoje `cancellations_rate=0`) sob pressão real.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Os 3 cancelamentos do dia têm origem concentrada no Kit 06 Canequinhas Acrílico (`MLB4410218897`) ou estão distribuídos por outros anúncios? — **motivada por:** sobreposição de 3 unidades disponíveis + 3 pedidos gerados + 3 cancelamentos no fechamento do dia — se concentrados, a ruptura já ocorreu e contamina `cancellations_rate`.

- **Pergunta:** Qual a `available_quantity` atual (2026-05-21) do Kit 06 Canequinhas Acrílico (`MLB4410218897`) — o estoque já zerou ou ainda há unidades? — **motivada por:** leitura de ruptura iminente com 3 unidades na abertura e 3 pedidos gerados ontem; a confirmação de zero define se a ação é de contenção ou ainda de prevenção.

- **Pergunta:** A trajetória de `health` do Kit 4 Potes 1050ml Retangular (`health=0,75`) e do Conjunto 5 Potes Tampa Vermelha (`health=0,71`) nos últimos 3 dias está caindo, estável ou em recuperação? — **motivada por:** health degradada confirmada nos dois campeões em Full; a direção é o dado que falta para classificar o risco como iminente (queda) ou contido (estável/subindo) e definir se a L02 precisa acionar Himmel para reforço de cobertura.

- **Pergunta:** Qual a `available_quantity` atual do Kit 6 Canecas Porcelana Tulipa Lisa 250ml (`MLB6167272090`, `is_catalog=true`, `available_quantity=21`, ~5 pedidos/dia, runway ~4 dias)? — **motivada por:** sinal adjacente de ruptura a curto prazo em anúncio de catálogo, onde a recuperação de posição pós-ruptura é estruturalmente mais lenta.

- **Pergunta:** O Kit 4 Potes 1050ml Retangular (`MLB4073003575`) e o Conjunto 5 Potes Tampa Vermelha (`MLB3288536143`) estão cobertos por campanha ativa nas 11 campanhas de Himmel? — **motivada por:** hipótese da L01 de que ADS compensa loss de ranking orgânico nesses dois anúncios; cobertura ou ausência por campanha ativa é o dado que confirma ou refuta operacionalmente essa hipótese.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o GMV — é a possível sobreposição entre ruptura de estoque e cancelamento no Kit 06 Canequinhas Acrílico: 3 unidades disponíveis, 3 pedidos gerados, 3 cancelamentos no fechamento. Se os cancelamentos são desse anúncio, a conta já consumiu a margem de reputação hoje — `cancellations_rate=0` e `transactions_canceled=0` podem já não refletir o estado real da janela em atualização. A L01 identificou esse risco; a L02 definiu a checagem como prioritária; a leitura operacional do dia sugere que a janela de prevenção pode ter fechado ontem, e o risco passa de prospectivo para realizado. O que a Condensadora precisa carregar: a ação de Yasmin para confirmar a origem dos cancelamentos deixou de ser "verificar antes que aconteça" e pode já ser "entender o que aconteceu e conter o impacto em reputação". O restante do dia — volume no patamar, ticket sustentando GMV, ADS eficiente — foi operacionalmente coerente com a tese da L01, sem novidade de peso além desse ponto.