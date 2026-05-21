<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O dia foi sustentado integralmente por ticket, não por volume: 91 pedidos praticamente idênticos ao bimestre (-0.2% vs 60d) e dentro da banda do dia da semana (-1.6% vs mesmos dias), enquanto o GMV subiu +33.3% vs 60d e +32.4% vs mesmos dias. Isso confirma operacionalmente a leitura estratégica de ganho de patamar via ticket — o canal não acelerou em alcance, mas em valor médio por pedido.

- O resultado ficou visivelmente apoiado em poucos produtos: o campeão do dia (Conjunto 5 Potes Tampa Preta, 23 pedidos) respondeu por 25.3% do volume total; top 3 concentrou 48.4% e top 5 chegou a 59.3%. Isso não é anomalia do dia — é o padrão estrutural apontado pela Estratégica. O que o dia acrescenta operacionalmente é que o produto que liderou é Cross-Docking, não Full, o que distorceu a composição de fulfillment do dia inteiro.

- A composição de fulfillment dos top 10 de ontem (56.3% Full) ficou 17.6 pp abaixo da média de 30 dias (73.9% Full) e 21.4 pp abaixo dos 7 dias (77.7% Full). Essa queda não é deterioração sistêmica — é efeito direto do campeão do dia ser Cross-Docking com 23 pedidos. Operacionalmente, o canal entregou bem abaixo do seu patamar habitual de cobertura Full no dia, o que reforça a evidência estratégica de que a base Full é estreita e concentrada em poucos anúncios.

- O Kit 06 Canequinhas Acrílico entrou no dia com estoque em cobertura crítica (3 unidades disponíveis, 3 pedidos gerados ontem, anúncio ativo e sem pausa). Esse é o único ponto do dia com risco operacional imediato — confirma e adiciona urgência ao sinal levantado pela Estratégica e à ação definida pela Tática.

---

### Sinais operacionais relevantes

- **Sinal:** campeão do dia (Conjunto 5 Potes Tampa Preta, 23 pedidos) opera em Cross-Docking, não em Full — **interpretação operacional:** a liderança desse produto puxa o mix de fulfillment do dia para baixo do padrão mensal; quando esse item lidera, o canal opera com menor proporção de Full do que seu histórico sugere, o que pode afetar tempo de entrega percebido e score logístico pontualmente.

- **Sinal:** fulfillment mix do top 10 de ontem (56.3% Full) está 17.6 pp abaixo da média 30d (73.9%) — **interpretação operacional:** a divergência é produto-específica, não sistêmica, mas confirma que os anúncios Full que geram 74% dos pedidos no mês não foram os que lideraram ontem; há dependência de produto líder que, quando é Cross-Docking, muda a composição operacional do dia inteiro.

- **Sinal:** Conjunto 5 Potes Tampa Vermelha (MLB3288536143, `is_catalog=true`, health=0.71) gerou apenas 5 pedidos — variante da mesma família do líder do dia (IMB501), mas a versão Tampa Vermelha ficou 4.6x abaixo da Tampa Preta em volume — **interpretação operacional:** a queda de performance dentro da mesma família pode ser consequência direta do health abaixo do limiar de penalização ML em anúncio de catálogo; adiciona evidência operacional ao risco estratégico de erosão orgânica progressiva já identificado.

- **Sinal:** Kit 06 Canequinhas Acrílico (MLB4410218897) com `available_quantity=3`, anúncio ativo, 3 pedidos gerados ontem — **interpretação operacional:** cobertura de estoque está zerada para o próximo ciclo de demanda; o ML continuará recebendo pedidos nesse anúncio enquanto ele estiver ativo; risco imediato de cancelamento prospectivo que pode contaminar `cancellations_rate` e `delayed_handling_rate` — sinal urgente, não sistêmico, mas com janela operacional de 24h.

- **Sinal:** ADS respondeu por 59.8% do GMV do dia (R$3.041,56 / R$5.087,71) com ACOS 4.33% e ROAS estimado de 11.6x — **interpretação operacional:** a eficiência é alta, mas a concentração de faturamento em ADS num dia em que o mix de fulfillment já estava distorcido pelo campeão Cross-Docking sugere que a campanha está puxando volume para uma estrutura de fulfillment menos vantajosa do que o histórico mensal; não é problema hoje, mas é o tipo de composição que, se repetida, compromete a leitura do mix Full como indicador confiável.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O volume e o GMV estão dentro das bandas históricas relevantes (60d, mesmos dias da semana) — a execução agregada do canal foi normal. O que eleva para "leve" é o conjunto de dois desvios pontuais coincidentes: (1) estoque em ruptura iminente num produto ativo com demanda recorrente (Kit 06 Canequinhas Acrílico), que tem janela operacional de 24h antes de gerar cancelamento — isolado, mas urgente; e (2) a composição de fulfillment do dia abaixo do padrão mensal por 17.6 pp, explicada pelo produto líder ser Cross-Docking, não por problema sistêmico. Os dois desvios têm causas identificáveis e são independentes entre si. Não há padrão acumulado que justifique "moderada". Subiria para "moderada" se o anúncio de canequinhas gerar cancelamento registrado no próximo ciclo, ou se o campeão Cross-Docking repetir liderança nos próximos dias com queda simultânea de health nos Full penalizados — aí a composição de fulfillment deixaria de ser pontual e viraria padrão.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** o anúncio do Kit 06 Canequinhas Acrílico (MLB4410218897) ainda está ativo com estoque zerado ou foi pausado após os 3 pedidos de ontem? — **motivada por:** sinal de cobertura crítica (3 unidades disponíveis, 3 pedidos gerados, anúncio ativo sem pausa); risco de cancelamento prospectivo com janela operacional de 24h identificado pela Tática.

- **Pergunta:** qual é a causa do health=0.71 no Conjunto 5 Potes Tampa Vermelha (MLB3288536143, `is_catalog=true`) — reclamações, atraso de envio, qualidade de listing ou outro fator? — **motivada por:** sinal de desempenho 4.6x abaixo da variante Tampa Preta da mesma família, com health abaixo do limiar de penalização ML em anúncio de catálogo; a Estratégica apontou que `health` em catálogo demora a recuperar.

- **Pergunta:** o health do Kit 4 Potes 1050ml (MLB4073003575, health=0.75) está estabilizado, em queda ou em recuperação em relação ao ciclo anterior? — **motivada por:** Estratégica identificou esse anúncio como segundo ponto de deterioração orgânica; o dia gerou 13 pedidos nele (2º lugar), mas sem dado de direção histórico do health, não é possível saber se a penalização está estabilizada ou aprofundando.

- **Pergunta:** por que o Conjunto 5 Potes Tampa Preta (MLB4535865317), campeão absoluto com 23 pedidos, opera em Cross-Docking e não em Full? Há planejamento de migração ou restrição de estoque no CD do ML? — **motivada por:** o produto líder do dia puxou o mix de fulfillment 17.6 pp abaixo do padrão mensal; entender se isso é estrutural (decisão de operação) ou transitório (ruptura de estoque no CD) muda completamente a leitura da composição futura do canal.

---

### Destaque para a Condensadora

O fato operacional mais relevante do dia não é o volume nem o ticket — é a composição. O campeão do dia (Conjunto 5 Potes Tampa Preta, 23 pedidos, Cross-Docking) liderou um canal que tem 73.9% dos seus pedidos mensais em Full, e com isso puxou o mix de fulfillment de ontem para 56.3% Full — 17.6 pp abaixo do padrão. Isso não é problema isolado: se esse produto continuará liderando dias com ADS ativo (59.8% do GMV veio de campanhas de Himmel), a composição de fulfillment do canal vai oscilar significativamente dependendo de qual produto lidera — e os produtos Full com health penalizado (MLB4073003575 e MLB3288536143) podem não ter tração orgânica suficiente para compensar. A conta confirma operacionalmente o risco estratégico de dependência estreita: quando o campeão é Cross-Docking e os Full estão com health deteriorado, o canal fica operacionalmente mais frágil do que o GMV agradável de R$5.087 sugere. Isso reforça, não contradiz, o que a Estratégica e a Tática identificaram. O segundo ponto urgente — estoque crítico em canequinhas (3 unidades, anúncio ativo) — é operacionalmente mais simples de resolver, mas tem janela curta: se não tratado em 24h, vira variável confundidora na reputação dos próximos ciclos.