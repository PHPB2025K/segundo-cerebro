<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O volume de 140 pedidos seguiu padrão bimodal típico do ML, mas com intensidade fora do histórico: o bloco 8–11h concentrou aproximadamente 54 pedidos (~38% do total), com progressão crescente hora a hora (11→13→14→16), e o bloco noturno 20–22h contribuiu com ~32 pedidos (~23%). A estrutura é normal; a magnitude de cada bloco não é. Isso adiciona evidência operacional direta à hipótese tática de investigar ação de ADS ou boost de exposição no período — o padrão de aceleração gradual no bloco manhã é consistente com campanha ativa, não com tráfego orgânico disperso.

- Ticket e volume subiram simultaneamente (R$46,71 vs R$41,53 no 30d, +12,5%), o que operacionalmente afasta a leitura de promoção de volume que achata margem. O mix se deslocou para produtos de maior valor unitário — ou a exposição favoreceu os itens mais caros da conta. Isso confirma a leitura estratégica de que o dia não é volume puro: há qualidade de mix embutida no GMV.

- O resultado do dia foi operacionalmente construído sobre a família IMB501 (potes de vidro redondos em três cores): 70 pedidos dos 140 totais — 50% exato num dia já excepcional. O spike de volume foi, em grande parte, um spike dessa família. O risco de concentração identificado pela Estratégica não está apenas presente — foi o vetor central da performance de hoje. Não há segundo vetor operacionalmente capaz de absorver eventual queda dessa família.

- Cancelamentos (3 de 140, ~2,1%) são operacionalmente irrelevantes e não apresentam padrão concentrado identificável nos dados disponíveis.

---

### Sinais operacionais relevantes

- **Sinal:** bloco 8–11h com progressão crescente 11→13→14→16 pedidos hora a hora — **interpretação operacional:** aceleração consistente de tráfego nesse período, não pico pontual; padrão compatível com campanha ou boost de exposição ativo — adiciona evidência à investigação tática pedida por Yasmin junto a Himmel.

- **Sinal:** ticket acima da banda histórica (30d e 60d) simultaneamente com volume muito acima do histórico — **interpretação operacional:** não é ticket mascarando volume fraco; é mix mais pesado ocorrendo junto com volume alto — a exposição do dia favoreceu produtos de maior valor unitário, o que tem implicação direta sobre qual anúncio ou campanha estava ativa.

- **Sinal:** família IMB501 (Tampa Preta + Vermelha + Cinza) = 70 pedidos = 50% do dia em um dia com 140 pedidos — **interpretação operacional:** a performance excepcional do canal é, operacionalmente, a performance excepcional dessa família; a concentração confirma com evidência direta o risco estrutural levantado pela Estratégica e reforça que qualquer instabilidade nessa família afeta metade da operação de forma imediata.

- **Sinal:** KIT2YW1520 (Kit 2 Potes Vidro 1520ml) apareceu com 21 pedidos, tornando-se o segundo produto individual do dia — **interpretação operacional:** há um candidato a segundo vetor, mas operacionalmente distante: 15% vs 32% do líder; não alivia a dependência estrutural em nível relevante, e é incerto se o volume desse produto reflete tração própria ou arrasto do dia forte.

- **Sinal:** itens/pedido = 1,11 (156 itens, 140 pedidos) — **interpretação operacional:** comportamento operacional limpo; nenhuma distorção de bundles inflados ou agrupamento artificial puxando GMV; o volume é real e unitário.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada.**

O dia apresenta desvio operacional em múltiplas dimensões simultaneamente: volume +51,8% vs mesma quarta-feira histórica, +43,4% vs 30d; ticket +12,5% vs 30d; GMV +60,9% vs mesma quarta-feira — tudo fora da banda ao mesmo tempo, com dados reconciliados e sem flags de qualidade no canal. Não é anomalia crítica porque não há sinal de ruptura, listing frágil, cancelamento sistêmico ou problema de fulfillment — o canal operou sem falha identificada. Mas a magnitude do desvio positivo, sem causa documentada e sobre memória rasa (weekly e monthly em template vazio), impede classificar como ausência de anomalia: um dia fora da banda em todas as métricas principais precisa de âncora antes de ser tratado como padrão. O que reduziria para anomalia leve é confirmação de causa (ADS ativo validado por Yasmin/Himmel) — o desvio continuaria, mas teria explicação operacional. O que elevaria para anomalia crítica é descoberta de Buy Box instável ou exposição artificial como vetor principal do spike.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** os 45 pedidos do Conjunto 5 Potes Tampa Preta (IMB501P) estão distribuídos ao longo do dia ou concentrados no bloco 8–11h? — **motivada por:** o bloco manhã foi o mais intenso do dia e o IMB501P é o produto dominante; concentração simultânea sugere que exposição específica nesse produto nesse período explica parte relevante do spike.

- **Pergunta:** os 3 cancelamentos estão associados a qual produto ou horário? — **motivada por:** com 50% da conta concentrada na família IMB501, mesmo 3 cancelamentos são informativos se estiverem todos nessa família — sinalizaria problema pontual num produto campeão que passaria despercebido no volume total.

- **Pergunta:** o KIT2YW1520 (Kit 2 Potes 1520ml) tem histórico de aparecer como segundo vetor nos dias disponíveis (12/05 e anteriores) ou hoje foi comportamento atípico puxado pelo dia forte? — **motivada por:** o produto apareceu com 21 pedidos num dia excepcional — é relevante saber se isso é padrão próprio ou arrasto do volume geral antes de tratá-lo como candidato a segundo vetor.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o número de pedidos — é que o spike de 140 pedidos foi construído com 50% de dependência de uma única família de produtos, num dia cujo bloco manhã sozinho gerou mais de um terço do resultado. O canal performou excepcionalmente, mas a fragilidade estrutural apontada pela Estratégica não está na periferia da performance de hoje: ela é o vetor central. Se a investigação de Yasmin confirmar que houve ação de ADS no período 13–14/05, o encadeamento operacional fica claro: o canal depende de campanha para sustentar esse patamar, e a campanha dependeu de um produto. Esse encadeamento de dependências não é urgência operacional para hoje — mas é o risco silencioso que pode passar despercebido se a Condensadora focar apenas no resultado positivo do dia.