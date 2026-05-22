<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O GMV de R$6.082,82 foi sustentado inteiramente por ticket, não por alcance. Volume (100 pedidos) ficou em linha com 30d (+0,7%) e dentro da banda do mesmo dia da semana (-2,7%), enquanto o ticket de R$60,83 — 37,1% acima da média 30d e 44,7% acima de 60d — foi o elemento que explicou o desvio de GMV sem expansão de pedidos. Confirma operacionalmente a tese da L01: o canal não cresceu em alcance, cresceu em valor médio por pedido.

- O resultado ficou concentrado em poucos produtos e com perfil de fulfillment radicalmente invertido vs padrão recente. `top3_concentration=60%` (60 de 100 pedidos divididos entre Conjunto 5 Potes Tampa Preta com 31 pedidos, Kit 10 Potes 1050ml com 16, e Conjunto 5 Potes Tampa Cinza com 13) e `top5_concentration=76%`. Os três líderes são todos `logistic_type: cross_docking`, o que puxou `fulfillment_mix_yesterday_top10.full_pct` para 20% contra `fulfillment_mix_7d.full_pct=77%` e `fulfillment_mix_30d.full_pct=73,6%` — uma inversão de +57 pontos percentuais vs semana recente. A divergência é produto-específica, não sistêmica: quando a família IMB501 (três variações, 52 pedidos combinados) e o KIT10YW1050 dominam o dia, o perfil de fulfillment da conta muda por composição, não por mudança estrutural de configuração. Confirma e detalha a leitura da L01 sobre mudança de liderança de produto.

- ADS sustentou 75,5% do GMV do dia (`ads_summary.revenue_ads_yesterday_brl = R$4.593,66` / `recipient.totals.gmv = R$6.082,82`) com ROAS de 13,4x e ACOS de 4,71% — eficiência alta. Ao cruzar com a composição do dia, emerge uma questão operacional relevante: a campanha de Himmel priorizou produtos Cross-docking que dominaram o volume, o que significa que ADS está construindo volume em cima de uma estrutura de fulfillment menos robusta que o padrão histórico da conta. Não é problema operacional hoje — mas é informação que a Condensadora deve carregar: bom resultado financeiro + perfil de fulfillment abaixo do padrão coexistem no mesmo dia.

- Dois anúncios Full no top 10 confirmam e adicionam precisão ao risco levantado pela L01 e à ação definida pela L02. Kit 06 Canequinhas Acrílico (`available_quantity=2`, 3 pedidos ontem, `status=active`) está em ruptura técnica consumada — os pedidos gerados já superam o estoque disponível. Kit 6 Canecas Porcelana 250ml (`available_quantity=19`, 5 pedidos ontem, fulfillment) tem cobertura de ~3–4 dias no ritmo atual. O Kit 4 Potes 1050ml Retangular (`health=0.75`, fulfillment, 8 pedidos ontem) é o único campeão do dia com health calculado e abaixo do limiar de penalização (0,85) — e segue gerando volume, o que adiciona evidência à hipótese da L01 de que ADS pode estar compensando exposição orgânica degradada nesse anúncio.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas Acrílico gerou 3 pedidos ontem com `available_quantity=2` e `status=active` em fulfillment — **interpretação operacional:** ruptura técnica já consumada; pedidos aceitos sem cobertura de estoque são cancelamentos prospectivos que vão afetar `reputation.cancellations_rate` antes de aparecer na API ML (janela longa). Confirma e adiciona urgência ao alerta crítico da L01 e à ação imediata definida pela L02.

- **Sinal:** Fulfillment mix do top 10 ontem foi 80% cross_docking — inversão de +57pp vs `fulfillment_mix_7d.full_pct=77%` e +54pp vs `fulfillment_mix_30d.full_pct=73,6%` — **interpretação operacional:** divergência produto-específica causada pela dominância da família IMB501 (cross_docking, três variações, 52 pedidos) e do KIT10YW1050 (cross_docking, 16 pedidos). Quando esses produtos lideram o dia, o fulfillment da conta reflete a composição do topo, não uma mudança de estrutura. Confirma a leitura da L01 de que a base Full da conta é estreita.

- **Sinal:** Kit 10 Potes 1050ml 1050ml (KIT10YW1050) gerou 16 pedidos com `available_quantity=76` — cobertura de ~4–5 dias no ritmo atual, anúncio em cross_docking — **interpretação operacional:** não é urgência operacional hoje, mas é o segundo maior volume do dia e não foi sinalizado pela L01 ou L02 como ponto de atenção. Se o ritmo se mantiver e não houver confirmação de reposição, a janela de atenção de estoque abre nos próximos dias. Evidência nova, não antecipada pelas camadas anteriores.

- **Sinal:** Kit 4 Potes 1050ml Retangular (`health=0.75`, fulfillment, MLB4073003575) gerou 8 pedidos ontem — único anúncio com health calculado no top 10, e abaixo do limiar de penalização (0,85) — **interpretação operacional:** o fato de gerar volume mesmo com health penalizado sugere que exposição orgânica degradada está sendo compensada por ADS, não por ranking natural. Adicionaria evidência direta à hipótese da L01 sobre ADS sustentando anúncios com exposição orgânica comprometida — relevante para a leitura futura de dependência de campanha.

- **Sinal:** 3 cancelamentos registrados no dia com `reputation.cancellations_rate=0` na API ML — **interpretação operacional:** o gap entre métrica do dia (sinal precoce) e a taxa oficial (janela longa) é esperado e não indica inconsistência. Com a ruptura técnica ativa no Canequinhas, os próximos cancelamentos têm causa provável identificada. Se `metrics.cancelamentos` subir acima de 5/dia por 2 ciclos consecutivos, é sinal precoce de que o impacto já vazou para a reputação antes de aparecer no indicador oficial.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada.**

Dois vetores operacionais desviaram simultaneamente: (1) fulfillment mix com inversão de mais de 50pp vs padrão 7d e 30d — produto-específico, mas operacionalmente relevante em termos de velocidade de entrega e elegibilidade competitiva; (2) ruptura técnica ativa no Kit 06 Canequinhas Acrílico, com pedidos aceitos sem cobertura de estoque. O que elevaria para **anomalia crítica**: cancelamentos do Canequinhas contaminando `reputation.cancellations_rate` nos próximos ciclos ou um segundo anúncio Full entrando em ruptura (Canecas Porcelana tem ~3–4 dias de cobertura). O que reduziria para **anomalia leve**: reposição do Canequinhas confirmada em <24h neutraliza o único vetor com impacto em reputação; a divergência de fulfillment, sozinha, seria leve — é informação de composição, não risco operacional isolado.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Quantos pedidos do Kit 06 Canequinhas Acrílico (MLB4410218897) estão em estado que ainda permite cancelamento controlado pela operação antes que o ML cancele automaticamente? — **motivada por:** ruptura técnica confirmada no dia (2 unidades disponíveis, 3 pedidos gerados), com impacto direto em `reputation.cancellations_rate` se a ação não for tomada em <24h conforme definido pela L02.

- **Pergunta:** Qual a causa do `health=0.75` no Kit 4 Potes 1050ml Retangular (MLB4073003575) — claims, atraso de handling, qualidade do listing — e qual a direção do indicador nos últimos 7 dias (estabilizando, caindo ou recuperando)? — **motivada por:** único anúncio no top 10 com health calculado e abaixo do limiar de penalização; a L02 definiu observação de trajetória antes de ação, e a direção é o dado que transita de "observar" para "alinhar com Himmel".

- **Pergunta:** Qual o `available_quantity` atual do Kit 10 Potes 1050ml (KIT10YW1050, MLB4676726433) e há confirmação de reposição pendente? — **motivada por:** segundo maior volume do dia (16 pedidos), cobertura estimada de ~4–5 dias, não sinalizado como ponto de atenção pela L01 ou L02 — evidência nova gerada pela composição específica do dia.

- **Pergunta:** Qual a composição do `revenue_ads_yesterday_brl = R$4.593,66` por anúncio — quais produtos Himmel priorizou nas campanhas ontem? — **motivada por:** divergência entre perfil Cross-docking que dominou o dia e padrão Full histórico da conta; se as campanhas priorizaram ativamente IMB501 e KIT10YW1050, a relação entre ADS share elevado e fulfillment divergente deixa de ser coincidência e vira hipótese operacional confirmável.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o número — é a estrutura por trás do número. Um GMV de R$6.082,82 (+38% vs 30d) foi entregue com 80% do top 10 em Cross-docking contra um padrão histórico de 73–77% Full, com 75,5% do resultado dependente de campanha ADS, com um anúncio Full em ruptura técnica ativa e outro com cobertura de ~3–4 dias. O bom resultado financeiro e a fragilidade operacional não são sinais contraditórios — são o mesmo dia visto de ângulos diferentes. A Condensadora precisa evitar que o GMV elevado encubra o Kit 06 Canequinhas Acrílico: é o único ponto do dia com risco de impacto em reputação se não for tratado ainda hoje, e é exatamente o tipo de sinal que desaparece dentro de um resultado positivo.