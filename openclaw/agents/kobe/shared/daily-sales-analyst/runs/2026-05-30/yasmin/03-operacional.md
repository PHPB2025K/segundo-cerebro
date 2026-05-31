<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **O dia foi puxado por volume, não por ticket.** 130 pedidos superam todos os benchmarks disponíveis: +19,0% vs 30d, +24,0% vs 60d e +16,6% vs mesmos sábados — com GMV seguindo na mesma direção (+13,6% vs 30d, +26,0% vs 60d, +10,8% vs mesmos sábados). Ticket R$43,68 está -4,6% vs 30d mas +1,5% vs 60d e dentro da banda histórica longa: o que a L01 descreveu como efeito de composição sazonal de sábado dominado pelo cluster IMB501 (ticket estruturalmente menor que outros top items) se confirma operacionalmente — sem sinal de erosão de preço.

- **O cluster IMB501 atingiu 54,6% do volume do dia** (71 de 130 pedidos: Tampa Preta 47 + Tampa Cinza 15 + Tampa Vermelha 9), próximo ao pico de 56,5% registrado em 25/05 na série 44%→47,5%→56,5% e acima da faixa regular de 44–47% dos ciclos de 22–24/05. Essa dominância puxou o `fulfillment_mix_yesterday_top10` para 91,5% Full — acima dos 84,7% de 7d e 78,1% de 30d — porque o cluster opera integralmente em Full (MLB3288536143, `logistic_type=fulfillment`). Confirma operacionalmente a assimetria entre base ativa (61% Cross-Docking) e campeões (Full) identificada pela L01 como dependência estrutural.

- **MLB6437847224 (Kit 6 Potes Vidro Hermético, `is_catalog=true`, Full) fecha com `available_quantity=7` pós-baixa de 3 pedidos do dia: cobertura prospectiva ~2,3 dias ao ritmo atual.** O sinal identificado pela L01/L02 se mantém intacto. Sem reposição confirmada em trânsito, qualquer pedido a partir de amanhã ultrapassa o estoque disponível e aciona cancelamento automático pelo ML — `is_catalog=true` implica perda de Buy Box com recuperação lenta, impacto direto na `cancellations_rate` e na janela Platinum (gap R$23.327, ETA 5 dias ao ritmo atual).

- **MLB3288536143 (Conjunto 5 Potes Vidro, Full, não-Catálogo) fecha com `available_quantity=149` pós-baixa de 71 pedidos do dia.** Ao ritmo de ~60–68 pedidos/dia estimado para o cluster (54,6% da média 7d de 125,7 pedidos), a cobertura prospectiva é de aproximadamente 2,2–2,5 dias — risco de ruptura no principal vetor de volume da conta que a L01/L02 não endereçaram explicitamente, focadas no MLB6437847224. Não é ruptura em Catálogo (sem perda de Buy Box), mas impacto em GMV seria desproporcionalmente maior que o item de 3 pedidos/dia.

---

### Sinais operacionais relevantes

- **Sinal:** MLB3288536143 com `available_quantity=149` pós-baixa de 71 pedidos = cobertura prospectiva ~2.2–2.5 dias ao ritmo do sábado, estimando o cluster em ~54% do avg_7d de 125,7 pedidos — **interpretação operacional:** risco de ruptura no item que concentrou 54,6% do volume do dia não estava coberto pela L01/L02; isoladamente, uma ruptura aqui impacta o resultado absoluto em magnitude muito maior que o MLB6437847224, embora sem o agravante de perda de Buy Box em Catálogo.

- **Sinal:** MLB6437847224 (Kit 6 Potes Vidro Hermético, `is_catalog=true`, Full) com `available_quantity=7` e 3 pedidos ontem — cobertura ~2,3 dias — **interpretação operacional:** confirma e reforça operacionalmente o sinal já identificado pela L01/L02 como risco imediato; o dado pós-baixa do dia analisado não muda o cálculo prospectivo — ruptura iminente em anúncio Catálogo ativo.

- **Sinal:** `fulfillment_mix_yesterday_top10=91,5% Full` vs 30d `78,1%` e 7d `84,7%` — nível mais concentrado em Full do que qualquer janela histórica disponível — **interpretação operacional:** divergência produto-específica gerada pelo domínio do cluster IMB501 (Full) nos pedidos do sábado, não migração sistêmica de modalidade; o único item Cross-Docking ativo no top10 (Kit 6 Canecas Porcelana 250ml Canelada, MLB6582682928, 4 pedidos) foi minoritário. Adiciona evidência à leitura da L01 de que a base Full do canal é estreita e concentrada nos campeões.

- **Sinal:** Cancelamentos=2 no terceiro ciclo não-zero disponível consecutivo (25/05: 3, 26/05: 3, 30/05: 2 — ciclos 27–29/05 sem entrada de memória diária) sem breakdown de origem — **interpretação operacional:** a hipótese de causa comum levantada nas memórias de 25–26/05 não foi refutada; dois cancelamentos num dia de volume sólido, sem anúncio pausado identificado no snapshot, mantém origem não atribuível e padrão ativo. Não é anomalia isolada — é série não encerrada.

- **Sinal:** `health=0,71` do MLB3288536143 no oitavo ciclo consecutivo idêntico, com concentração do cluster no dia chegando a 54,6% — patamar próximo ao pico de 56,5% de 25/05 — **interpretação operacional:** cada ciclo de alta concentração em item com `health` estagnado no nível preocupante amplifica a exposição a qualquer evento de reclassificação pelo ML; ADS share de 59,5% sustentando exatamente esse item no seu melhor dia sazonal (sábado) adiciona evidência à hipótese da L01 de substituição orgânica por mídia paga.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O dia operou dentro das bandas esperadas em volume, GMV, ticket e reputação. Nenhum anúncio ativo com status pausado, `cancellations_rate=0` na janela de reputação ML, reputação verde estável. O desvio operacional identificável é de uma única dimensão, mas concentrada: dois anúncios em Full simultaneamente abaixo de 3 dias de cobertura prospectiva num mesmo dia de volume elevado — MLB6437847224 (~2,3 dias, Catálogo) e MLB3288536143 (~2,2–2,5 dias, Clássico dominante). Cada um isolado seria sinal de atenção preventiva; os dois simultâneos no vetor central de receita elevam o nível acima de incidental. Sobe para **anomalia moderada** se o próximo pacote mostrar `available_quantity` abaixo de 50 no MLB3288536143 — ou `available_quantity` zerado / `status=paused` no MLB6437847224.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual o `available_quantity` atual e status de reposição em trânsito ao CD do ML para MLB3288536143 (Conjunto 5 Potes Vidro, Full)? — **motivada por:** `available_quantity=149` pós-baixa de 71 pedidos implica cobertura prospectiva de ~2,2–2,5 dias ao ritmo estimado do cluster; risco de ruptura no item que gerou 54,6% do volume não foi endereçado explicitamente pela L01/L02.

- **Pergunta:** Qual o `available_quantity` atual e ETA de reposição em trânsito para MLB6437847224 (Kit 6 Potes Vidro Hermético, `is_catalog=true`, Full)? — **motivada por:** `available_quantity=7` pós-baixa identificado como ruptura iminente pela L01/L02 e confirmado operacionalmente; próximo ciclo pode mostrar ruptura ativa.

- **Pergunta:** Os 2 cancelamentos do dia compartilham `platform_item_id` com os cancelamentos de 25/05 e 26/05? — **motivada por:** padrão de três ciclos não-zero disponíveis sem breakdown de origem; hipótese de causa comum latente não encerrada desde 25/05.

- **Pergunta:** Qual o breakdown de `revenue_ads_yesterday` por `platform_item_id` — a verba de Himmel está concentrada no MLB3288536143 (cluster IMB501 com `health=0,71`) ou distribuída? — **motivada por:** ACOS 8,23% no terceiro ponto acima do baseline de 4,4% com share 59,5%; sem atribuição por anúncio, não é possível confirmar se o custo crescente de cobertura está concentrado no campeão degradado ou reflete mix saudável.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia é que a conta fechou com dois itens Full simultâneos entre 2 e 3 dias de cobertura prospectiva — e o de maior impacto potencial em GMV (MLB3288536143, 54,6% do dia, ~2,2–2,5 dias) não estava no radar da L01/L02, que focaram corretamente no risco de Catálogo do MLB6437847224. A tese de ganho de patamar e a urgência da janela Platinum estão intactas — o que esta leitura acrescenta é que o sábado forte foi construído sobre um nível de estoque Full que, se não reposto antes do próximo ciclo de alta demanda, pode transformar o risco de reputação de hipótese em evento. A Condensadora deve considerar que a ação de reposição do MLB6437847224 levantada pela L02 provavelmente precisa incluir verificação do estoque do cluster IMB501 no mesmo movimento operacional com Yasmin.