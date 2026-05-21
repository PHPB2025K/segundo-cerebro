<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- **O dia foi integralmente sustentado por ticket, sem ganho de alcance (confirma L01).** 91 pedidos quase idênticos ao bimestre (`orders_vs_60d=-0,2%`) e ao mesmo dia da semana (`orders_vs_same_weekday_pct=-1,6%`), enquanto GMV cresceu +33,3% vs 60d e +32,4% vs mesmas quartas — sustentado pelo ticket de R$55,91 vs `avg_60d.avg_ticket=R$41,86` (+33,6%) e `avg_30d.avg_ticket=R$44,03` (+27,0%). O canal não alcançou mais compradores; extraiu mais receita por pedido. Confirma operacionalmente o patamar ticket-driven identificado pela L01 e a trajetória ascendente contínua de ticket nas três janelas.

- **Mix de fulfillment divergiu 17,6pp do padrão mensal por causa de um único anúncio (adiciona evidência à L01, Lente Op 3).** O Conjunto 5 Potes Tampa Preta liderou o dia com 23 pedidos (~25,3% do volume) e opera em Cross-Docking — o que puxou `fulfillment_mix_yesterday_top10.full_pct` para 56,3% contra `fulfillment_mix_30d.full_pct=73,9%` e `fulfillment_mix_7d.full_pct=77,7%`. A divergência é produto-específica e pontual, não sistêmica: um único anúncio liderando em Cross-Docking explica os 17,6pp de desvio. Operacionalmente, isso evidencia que o peso Full no mix diário é volátil conforme qual campeão lidera — a base Full depende de quem vende no dia, não de profundidade do portfólio. Adiciona evidência concreta à leitura da L01 sobre base Full estruturalmente estreita.

- **Health degradada nos dois campeões Full do top5 — e um deles está em Catálogo, não em Clássico como a L01 descreveu (contradiz L01 neste ponto específico, Lente Op 4).** Kit 4 Potes 1050ml (2º do dia, 13 pedidos, `health=0,75`, `is_catalog=false`, fulfillment) e Conjunto 5 Potes Tampa Vermelha (5º do dia, 5 pedidos, `health=0,71`, fulfillment) têm penalização ativa de ranking pelo ML. A L01 classificou ambos como `is_catalog=false` — mas o dado do pacote mostra que Tampa Vermelha (MLB3288536143) tem `is_catalog=true` e `catalog_product_id=MLB44224272`. Isso muda o mecanismo de dano: para anúncios em Catálogo, health degradada pressiona Buy Box ML diretamente, não apenas posição em categoria via ranking Clássico; e recuperação de Buy Box em catálogo é mais lenta do que recuperação de posição orgânica. O risco operacional do 5º produto do dia é mais grave do que a L01 descreveu.

- **ADS carregou 59,8% do GMV com eficiência alta — e amplificou o dia num contexto de mix de fulfillment já distorcido (confirma risco estrutural L01, Lente Op 5).** `revenue_ads_yesterday_brl=R$3.041,56` / `gmv=R$5.087,71` = 59,8% share. ROAS de 11,6x (`R$3.041,56` / `spend=R$262,19`). `avg_acos_pct=4,64%` — campanha eficiente. Mas num dia em que o campeão do dia (maior volume) opera em Cross-Docking e o mix Full já estava deprimido, há sinal de que o ADS pode ter amplificado um produto fora do mix Full ideal. Não é problema de execução — é informação para a Condensadora: eficiência de campanha e composição de fulfillment não andam na mesma direção hoje.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas Acrílico com Suporte de Madeira Acrílico (MLB4410218897, fulfillment, `status=active`) encerrou o snapshot de 21/05 com `available_quantity=3` após 3 pedidos em 20/05, sem evidência de resolução antes da coleta. — **Interpretação operacional:** estoque em nível crítico com anúncio ativo; qualquer pedido em 21/05 pode levar a ruptura e cancelamentos subsequentes que contaminarão o `cancellations_rate` hoje em zero; o risco identificado pela L01 e a ação definida pela L02 não foram neutralizados antes do snapshot — ainda em aberto.

- **Sinal:** Conjunto 5 Potes Tampa Vermelha (MLB3288536143) confirmado como `is_catalog=true` (`catalog_product_id=MLB44224272`) com `health=0,71` e `logistic_type=fulfillment`. — **Interpretação operacional:** o dado do pacote contradiz a classificação da L01 (que o tratou como Clássico); para um anúncio de Catálogo, health=0,71 pressiona diretamente a elegibilidade à Buy Box ML — perda de Buy Box implica perda de tráfego pago eficiente e posição no slot principal do catálogo, com tempo de recuperação mais longo do que em anúncio Clássico. Este é o sinal de maior gravidade subavaliada do dia.

- **Sinal:** 3 cancelamentos no dia (3/91 pedidos = ~3,3%), com `cancellations_rate=0` na janela longa ML (`reputation.cancellations_rate`). — **Interpretação operacional:** o sinal precoce do dia é perceptível mas ainda não contaminou a reputação; a origem dos 3 cancelamentos é desconhecida — pode incluir o Kit 06 Canequinhas Acrílico (estoque crítico), mas requer confirmação granular; se concentrados em um único anúncio, o padrão é mais grave do que 3 cancelamentos pulverizados sugerem.

- **Sinal:** Mix de fulfillment do top10 de ontem (Full 56,3%) desviou 17,6pp do padrão 30d (Full 73,9%) por causa do campeão Cross-Docking (Conjunto 5 Potes Tampa Preta, 23 pedidos). — **Interpretação operacional:** divergência produto-específica e pontual; mas o padrão operacional revela que a conta não tem profundidade em Full para manter o mix histórico quando o líder do dia não é Full — a robustez do mix é dependente de qual anúncio lidera.

- **Sinal:** Kit 6 Tigelas de Vidro 250ml (MLB6167272090, `is_catalog=true`, `available_quantity=21`, `health=null`, 5 pedidos ontem, fulfillment). — **Interpretação operacional:** 21 unidades em catálogo com ritmo de 5 pedidos/dia = cobertura de ~4 dias; `health=null` não significa saudável — significa volume insuficiente para o ML calcular; não é emergência hoje, mas é o próximo ponto de atenção em catálogo se o ritmo se mantiver nos próximos 2–3 ciclos.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.** Volume e GMV ficaram dentro das bandas históricas (`orders_vs_60d=-0,2%`, `gmv_vs_same_weekday=+32,4%` explicado pelo ticket documentado); a distribuição horária é normal com concentração no período comercial (13–15h); não há anúncio pausado com pedidos em aberto no top10. O que sustenta a classificação em leve: (1) estoque crítico no Kit 06 Canequinhas Acrílico ativo sem resolução confirmada no snapshot; (2) 3 cancelamentos sem origem determinada — sinal precoce não destrinchado; (3) Tampa Vermelha confirmada como catálogo com `health=0,71`, risco mais grave do que a L01 descreveu, mas ainda sem evidência de perda de Buy Box materializada. Nenhum sinal bloqueia a operação hoje de forma isolada. Subiria para **anomalia moderada** se os cancelamentos do dia forem confirmados como originados do item com estoque crítico (concentração de causa), ou se Tampa Vermelha perder Buy Box nos próximos 1–2 ciclos (catálogo + health degradada + sinal de posição).

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Os 3 cancelamentos do dia são de qual(is) anúncio(s)? Algum é do Kit 06 Canequinhas Acrílico (MLB4410218897)? — **Motivada por:** Sinal 3 (cancelamentos sem origem conhecida) cruzado com Sinal 1 (item com estoque crítico ativo no mesmo dia).

- **Pergunta:** Qual o `available_quantity` atual do Kit 06 Canequinhas Acrílico (MLB4410218897) em 21/05? Houve pausa ou cancelamento neste ciclo? — **Motivada por:** Sinal 1 (estoque=3 no snapshot de 21/05, ação definida pela L02 ainda em aberto).

- **Pergunta:** Qual a direção (`health` estável / caindo / recuperando) e a causa do `health=0,71` do Conjunto 5 Potes Tampa Vermelha (MLB3288536143, `is_catalog=true`, fulfillment)? Claims, atraso de entrega ou qualidade do listing? — **Motivada por:** Sinal 2 (anúncio de catálogo com health crítico — risco de Buy Box, não apenas ranking; contradiz leitura da L01 sobre o mecanismo de dano).

- **Pergunta:** O `revenue_ads` de ontem está concentrado no Conjunto 5 Potes Tampa Preta (Cross-Docking, campeão do dia) ou distribuído entre os campeões Full? Qual anúncio gerou mais receita via ADS? — **Motivada por:** Lente Op 5 (ADS share 59,8% num dia em que o campeão era Cross-Docking — sinal de que a campanha pode ter priorizado produto fora do mix Full ideal; relevante para Himmel no próximo alinhamento).

- **Pergunta:** Qual o `available_quantity` atual do Kit 6 Tigelas de Vidro 250ml (MLB6167272090, `is_catalog=true`, `available_quantity=21`, 5 pedidos em 20/05)? — **Motivada por:** Sinal 5 (cobertura de ~4 dias em catálogo sem health calculável — próximo ponto de atenção antes de ruptura em anúncio de catálogo).

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não está no GMV ou no ticket — está numa correção de gravidade: o Conjunto 5 Potes Tampa Vermelha (5º do dia, `health=0,71`, fulfillment) é um anúncio **em Catálogo** (`is_catalog=true`, confirmado no pacote), não Clássico como a L01 descreveu. Isso muda o mecanismo de penalização — health degradada em catálogo pressiona Buy Box ML diretamente, e recuperação de Buy Box é mais lenta e menos previsível do que recuperação de posição em ranking de categoria. A conta tem dois vetores de degradação orgânica silenciosa no top5 (health=0,75 e health=0,71), e o de maior impacto potencial opera em catálogo com um mecanismo de dano mais grave. Se isso passar despercebido no Slack, a mensagem final comunicará o risco em nível errado de urgência. O restante do dia — volume, GMV, ADS, mix de fulfillment — comportou-se dentro do esperado para o padrão ticket-driven já documentado pela L01, sem novidade operacional relevante além do que as camadas anteriores já capturaram.