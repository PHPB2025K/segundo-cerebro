<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O dia foi sustentado integralmente por ticket, não por volume: 84 pedidos ficam -15,4% vs avg_30d (99,3) e -17,6% vs same_weekday_avg (102,0), enquanto o GMV de R$4.622 se sustenta em +3,4% vs 30d e -2,1% vs mesmos dias — carregado por ticket de R$55,02 (+22,3% vs avg_30d de R$45,00 / +29,8% vs avg_60d de R$42,40). O volume de 84 pedidos é praticamente idêntico à sexta de 08/05 (83 pedidos, R$3.700) — a diferença de GMV entre as duas sextas comparáveis é inteiramente explicada pelo ticket mais alto, não por mais alcance. Confirma operacionalmente a leitura estratégica da L01: a conta mantém faturamento sem crescer volume.

- O resultado ficou estruturalmente apoiado em poucos produtos (top3_concentration=48,8%; top5=64,3%), com o Conjunto 5 Potes Tampa Preta como líder absoluto (20 pedidos, ~23,8% do total). O dado operacional relevante é que esse produto opera em Cross-Docking, e sua liderança puxou o fulfillment_mix_yesterday_top10 para Full 47,1% / Cross-Docking 52,9% — inversão expressiva em relação ao padrão mensal (fulfillment_mix_30d: Full 73,7% / Cross-Docking 26,3%) e semanal (fulfillment_mix_7d: Full 74,9%). A divergência é produto-específica: sem o líder Tampa Preta, o restante do top10 teria mix próximo ao histórico. Confirma o risco de dependência levantado pela L01 e adiciona evidência ao ponto da L02 de que a base Full do canal é estreita — a liderança Full no histórico depende dos campeões Full se manterem ativos e com posição.

- Os dois anúncios Full mais relevantes do dia acumulam penalização ativa no mesmo ciclo em que o líder Cross-Docking dominou: Kit 4 Potes 1050ml (MLB4073003575, 11 pedidos, health=0,75) e Conjunto 5 Potes Tampa Vermelha (MLB3288536143, 10 pedidos, health=0,71) — ambos abaixo do limiar 0,85 do ML. O fato de ainda aparecerem no top 3 do dia com health degradada sugere que ADS pode estar sustentando a visibilidade desses anúncios apesar da penalização orgânica — mecanismo de compensação que a L01 descreveu como risco silencioso. A direção do health (caindo, estável ou em recuperação) é o dado ausente mais crítico para avaliar se a erosão está progredindo.

- ADS respondeu por R$3.228,78 de R$4.622,03 — share de 69,8% — com ROAS 10,9x e ACOS 4,55%. A campanha sustentou o dia com eficiência, mas a concentração próxima de 70% do GMV em mídia paga em um dia em que o mix de modalidade de envio já estava distorcido pelo líder Cross-Docking levanta a hipótese operacional de que a campanha do Himmel pode estar priorizando o Tampa Preta (ou outro produto Cross-Docking) em detrimento dos campeões Full — o que amplificaria tanto a dependência quanto a distorção de modalidade observada. Não é possível confirmar sem a composição do revenue_ads por anúncio, mas é informação que a Condensadora precisa ter presente.

---

### Sinais operacionais relevantes

- **Sinal:** Conjunto 5 Potes Tampa Preta (Cross-Docking, 20 pedidos, ~23,8% do volume) liderou o dia e inverteu o fulfillment_mix_yesterday_top10 para Cross-Docking-dominante (52,9%) contra o padrão mensal Full-dominante (73,7%) — **interpretação operacional:** divergência produto-específica e pontual, não sistêmica; mas evidencia que a liderança de Full no histórico é estreita — um único produto Cross-Docking com performance acima do normal reverte o mix do dia inteiro. Se os campeões Full continuarem perdendo exposição orgânica, esse padrão pode se tornar recorrente.

- **Sinal:** Kit 4 Potes 1050ml (MLB4073003575, Full, health=0,75, 11 pedidos) e Conjunto 5 Potes Tampa Vermelha (MLB3288536143, Full, health=0,71, 10 pedidos) seguem gerando volume apesar de health abaixo de 0,85 nos dois casos — **interpretação operacional:** confirma que esses anúncios ainda têm tração, mas sem saber a direção do health não é possível distinguir entre estabilização e erosão progressiva. A penalização orgânica no ML é gradual — o volume pode se manter por alguns ciclos antes de colapsar. Esse é o risco estrutural que a L01 identificou e que ainda não tem direção confirmada.

- **Sinal:** Kit 6 Canecas Tulipa Lisa 250ml (MLB6167272090, Full, available_quantity=12 POST-baixa, 6 pedidos ontem) — cobertura prospectiva de ~2 dias ao ritmo atual — **interpretação operacional:** ruptura iminente em anúncio Full ativo no top 5; entrada em ruptura em modalidade Full remove a posição no CD do ML sem possibilidade de reação imediata no mesmo dia. Pedidos gerados após ruptura resultam em cancelamento automático, pressionando cancellations_rate (hoje em 0). O risco é prospectivo: os 6 pedidos de ontem já foram atendidos.

- **Sinal:** ADS share de 69,8% como primeiro ponto de dado registrado para essa série — sem histórico comparável em memória (weekly/monthly zerados, lacuna em 2026-05-21) — **interpretação operacional:** não é possível afirmar se 69,8% é padrão recorrente, valor alto ou comportamento atípico do dia. Este é o ponto zero da série, conforme definido pela L02. O valor é relevante como referência inicial — não como anomalia confirmada.

- **Sinal:** 1 cancelamento no dia com cancellations_rate=0 na janela de reputação — **interpretação operacional:** evento isolado sem padrão identificável. Não há sinal de problema concentrado ou recorrente. Irrelevante operacionalmente enquanto isolado; registrar para monitoramento de recorrência.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

Dois desvios operacionais identificáveis no dia: (1) inversão de modalidade de envio no top10 — Cross-Docking 52,9% vs padrão mensal Full 73,7% — produzida por um único líder de dia, portanto produto-específica e não sistêmica; (2) cobertura de estoque em ruptura iminente no Kit 6 Canecas Tulipa Lisa 250ml (~2 dias de runway em modalidade Full). Os dois desvios são independentes entre si e isolados — sem padrão acumulado conectando-os. Reputação permanece em 5_green, cancellations_rate=0, sem anúncio pausado gerando pedidos, GMV dentro da banda dos mesmos dias (-2,1%). Para subir para anomalia moderada: health em queda confirmada nos campeões Full (0,75 e 0,71) combinada com ruptura efetiva no Kit 6 Canecas, ou ADS share ultrapassando 75% por 3 dias consecutivos. Para descer para ausência de anomalia: reposição do Kit 6 Canecas confirmada e saúde dos campeões Full estabilizada por 2 dias.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual é a direção do health do Kit 4 Potes 1050ml (MLB4073003575, health=0,75) e do Conjunto 5 Potes Tampa Vermelha (MLB3288536143, health=0,71) nos últimos 7 dias — estabilizando, caindo ou em recuperação? Há histórico de health disponível para esses dois anúncios na janela recente? — **motivada por:** Sinal 2; a direção é a variável que separa "erosão progredindo" de "estabilização com penalização moderada" — sem ela, o risco estrutural da L01 permanece hipótese aberta.

- **Pergunta:** Qual é o estoque real do Kit 6 Canecas Tulipa Lisa 250ml no CD do ML (MLB6167272090) agora, e há reposição programada ou em trânsito? — **motivada por:** Sinal 3; available_quantity=12 POST-baixa com ritmo de 6 pedidos/dia indica cobertura de ~2 dias; sem reposição confirmada, ruptura é iminente e pressiona cancellations_rate a partir de amanhã.

- **Pergunta:** Qual é a composição do revenue_ads de ontem por anúncio — especificamente, o Conjunto 5 Potes Tampa Preta (MLB4535865317, Cross-Docking) aparece como destino relevante da verba da campanha do Himmel? — **motivada por:** cruzamento entre Sinal 4 e Sinal 1; se ADS está priorizando o líder Cross-Docking do dia, isso explica operacionalmente tanto o share de 69,8% quanto a inversão de modalidade — e é informação crítica para quando a L02 decidir revisar a segmentação da campanha nos próximos ciclos.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é a queda de volume — estrutural nas sextas, dentro da dispersão histórica — nem o GMV levemente abaixo dos mesmos dias (-2,1%): é que a conta faturou dentro da banda esperada com a estrutura interna funcionando diferente do padrão. O Full enfraqueceu (dois campeões Full com health degradada e atuando abaixo do limiar), o Cross-Docking liderou por conta de um único produto, e ADS compensou com share de 69,8% — o número do dia parece normal, mas o mecanismo interno que o gerou não é. Esse é exatamente o risco silencioso que a L01 descreveu: enquanto ROAS é alto e o GMV fica na banda, a erosão orgânica dos campeões Full passa invisível. O sinal que pode escapar mais facilmente é o Kit 6 Canecas Tulipa Lisa 250ml: se entrar em ruptura amanhã, o impacto não aparece como queda — aparece como ausência de volume no top 5, que pode ser confundida com oscilação natural do dia. Verificar reposição hoje é a ação que distingue uma ruptura planejada de uma surpresa operacional.