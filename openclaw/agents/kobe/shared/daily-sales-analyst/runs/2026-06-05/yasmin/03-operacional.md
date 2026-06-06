<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- O dia foi sustentado por volume, não por ticket. 164 pedidos = +39% vs 30d, +47,9% vs 60d e +54,4% vs mesmo dia da semana (avg 106 pedidos) — expansão real de alcance. Ticket R$47,21 ficou -6,3% vs mesmo dia da semana (R$50,39) e -1,4% vs 30d: compressão leve explicada por composição, não por deterioração estrutural. O cluster IMB501 (Tampa Cinza Full + Tampa Vermelha Cross-Docking + Tampa Preta Cross-Docking = 79 pedidos = 48,2% do volume) carrega valor unitário menor que o mix histórico. O resultado confirma operacionalmente a tese da L01 de patamar via volume no bimestre — e o leve recuo vs 7d (-2,8% pedidos, -2,3% GMV) é acomodação intra-semana dentro de banda elevada, sem sinal de deterioração.

- O mix de modalidade de envio divergiu significativamente do padrão histórico: `fulfillment_mix_yesterday_top10.full_pct = 62,9%` vs `fulfillment_mix_30d.full_pct = 81,1%` — delta de -18,2pp, a maior divergência registrada na série disponível. A causa é produto-específica: as variações Cross-Docking do cluster IMB501 (Tampa Vermelha MLB4535659243 com 20 pedidos + Tampa Preta MLB4535865317 com 17 pedidos = 37 pedidos Cross-Docking combinados) ocuparam as posições 2 e 3 do dia, superando qualquer outra linha em Cross-Docking. A divergência não é sistêmica — não indica mudança na base da conta — mas confirma operacionalmente a lente estratégica da L01 sobre a assimetria entre campeões Full e base majoritariamente Cross-Docking: quando o IMB501 Cross-Docking acelera, o mix do dia inverte de forma visível.

- O maior gerador de volume da conta em modalidade Full (MLB3288536143, Conjunto 5 Potes Vidro Tampa Cinza, 42 pedidos = 25,6% do dia) fechou com `available_quantity=58` no snapshot POST-baixa dos 42 pedidos — cobertura prospectiva de ~1,4 dias ao ritmo de hoje. Segue no ~16º ciclo consecutivo com `health=0,71`, estagnado, sem reversão. Cada novo ciclo de cobertura curta sem confirmação de restock entrante é mais uma evidência para o risco estrutural que a L01 identificou como principal — a operação do dia não trouxe alívio nem agravamento sobre o ETA: reforça que o sinal de urgência de restock da L02 está operacionalmente correto.

- A Tulipa (MLB6167272090, Full, `status=paused`, `available_quantity=0`) gerou 11 pedidos no dia — visíveis em `top_products` com 11 orders —, todos cancelamentos prospectivos garantidos, ainda não contabilizados nos 5 `cancelamentos` registrados em `metrics` (que são do dia). Com `reputation.cancellations_rate=0` oficial e threshold Platinum formalmente cruzado, esses 11 pedidos somam-se à série acumulada de ciclos anteriores documentada na weekly: 8º+ ciclo consecutivo do padrão, e cada ciclo adiciona pressão sobre a janela oficial ML. A operação de ontem confirma o risco da L01 de coincidência de timing entre cancelamentos acumulados e promoção pendente — não contradiz, não adiciona dimensão nova, confirma com mais uma rodada.

---

### Sinais operacionais relevantes

- **Sinal:** Tulipa (MLB6167272090) gerou 11 pedidos com `status=paused` e `available_quantity=0`, adicionando mais uma carga ao padrão recorrente de cancelamentos prospectivos — **interpretação operacional:** esses 11 pedidos não aparecem nos 5 `cancelamentos` do dia; entram na fila de processamento ML e, quando cancelados automaticamente, pressionam `cancellations_rate` da reputação numa janela em que a conta aguarda reconhecimento formal do Platinum com `gap_revenue_brl=0`. É o sinal mais sensível do dia — silencioso nas métricas de superfície, mas operacionalmente carregado.

- **Sinal:** `fulfillment_mix_yesterday_top10.full_pct = 62,9%` vs `fulfillment_mix_30d.full_pct = 81,1%` — divergência de -18,2pp puxada pelo IMB501 Cross-Docking nas posições 2 e 3 — **interpretação operacional:** a divergência é produto-específica e recorrente (identificada em ciclos anteriores na weekly), não sistêmica. Mas confirma que a base Full do canal é estreita e dependente de poucos campeões: quando as variações Cross-Docking do IMB501 aceleram, o mix do dia inverte visualmente — o canal não mudou, a composição do dia mudou.

- **Sinal:** MLB3288536143 (Conjunto 5 Potes Vidro Tampa Cinza, Full) com `available_quantity=58` após 42 pedidos → cobertura prospectiva ~1,4 dias ao ritmo do dia, `health=0,71` pelo ~16º ciclo consecutivo — **interpretação operacional:** a cobertura não fecha o fim de semana ao ritmo atual sem restock confirmado. Risco é prospectivo (pedidos futuros D em diante). Adiciona evidência à ação 1 da L02 sobre ETA urgente — o ciclo de ontem não trouxe alívio.

- **Sinal:** MLB6582682928 (Kit 6 Canecas 250ml Canelada Preta, Cross-Docking) com `available_quantity=8` após 7 pedidos hoje → cobertura prospectiva ~1,1 dias ao ritmo de hoje — **interpretação operacional:** o risco é menor que nos anúncios Full porque Cross-Docking opera com estoque Budamix (reposição direta, sem lead time de CD do ML). Mas ao ritmo atual, qualquer aceleração amanhã zera o estoque disponível. Não é urgência crítica, é sinal de monitoramento para Granular confirmar estoque físico disponível na expedição.

- **Sinal:** MLB6167272090 (Tulipa) ainda presente no `top_products` com 11 pedidos e 11 unidades — apesar de `status=paused` e `available_quantity=0` no snapshot — **interpretação operacional:** os pedidos foram gerados no período do dia analisado (BRT 05/06), provavelmente antes ou durante o período em que o anúncio estava pausado no sistema ML. A presença no ranking de vendas com zero de estoque e status pausado confirma que o mecanismo de geração de cancelamentos automáticos está ativo, não interrompido.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada.**

Três vetores operacionais simultâneos no mesmo dia: (1) Tulipa gerando 11 cancelamentos prospectivos garantidos em `status=paused` / `available_quantity=0` — 8º+ ciclo do padrão — com `cancellations_rate` oficial em zero e promoção Platinum pendente; (2) divergência de -18,2pp no mix de modalidade de envio do top10 vs 30d, a maior da série disponível, causada pelo domínio Cross-Docking do IMB501 nas posições 2 e 3; (3) cobertura prospectiva do maior gerador Full (`MLB3288536143`) em ~1,4 dias sem confirmação de ETA de restock. Nenhum dos três é inédito — todos têm precedente na série weekly — mas a coincidência no mesmo dia, com threshold Platinum cruzado e promoção ainda não registrada, eleva o peso operacional coletivo acima do limiar de "leve". Para descer para anomalia leve: ETA de restock confirmado para MLB3288536143 dentro de 24h + `cancellations_rate` = 0 no próximo snapshot. Para subir para crítica: `cancellations_rate` > 0 no próximo snapshot, confirmando entrada dos cancelamentos na janela oficial ML.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual o status de processamento atual dos 11 pedidos da Tulipa (MLB6167272090) — foram cancelados automaticamente pelo ML, estão em fila ou há algum em andamento? — **motivada por:** sinal 1 acima: Tulipa com 11 pedidos em `status=paused` / `available_quantity=0`, cada pedido em andamento é um cancelamento automático prospectivo que pressiona `cancellations_rate` na janela de transição Platinum.

- **Pergunta:** Dos 5 cancelamentos registrados em `metrics.cancelamentos` do dia, qual a atribuição por `platform_item_id` — vieram da Tulipa, do MLB3288536143 ou de outro anúncio? — **motivada por:** sinal 1 e leitura 4: 5 cancelamentos no dia com Tulipa como candidato natural mas sem breakdown `order_id × platform_item_id × motivo` no pacote, impedindo separar causa concentrada de causa pulverizada.

- **Pergunta:** `available_quantity` do MLB3288536143 (Conjunto 5 Potes Vidro Tampa Cinza) está desagregado por variação de cor/tampa — qual variação específica está mais próxima da ruptura dentro dos 58 agregados? — **motivada por:** leitura 3 e sinal 3: cobertura ~1,4 dias sobre agregado que combina Tampa Cinza + Tampa Vermelha + Tampa Preta no mesmo anúncio multi-variação; pendência estrutural recorrente desde 22/05 na weekly.

- **Pergunta:** Qual o estoque físico atual na expedição Budamix para MLB6582682928 (Kit 6 Canecas 250ml Canelada Preta, Cross-Docking) — os 8 `available_quantity` do snapshot refletem o estoque real disponível para coleta ML ou há mais em prateleira ainda não sincronizado? — **motivada por:** sinal 4: cobertura ~1,1 dias ao ritmo de hoje; modalidade Cross-Docking permite reposição direta sem lead time de CD, mas exige confirmar se o estoque físico está disponível antes de classificar como sem risco.

---

### Destaque para a Condensadora

O fato operacional que não pode ser enterrado em métrica: a Tulipa (MLB6167272090) registrou 11 pedidos no dia com `status=paused` e `available_quantity=0` — 11 cancelamentos prospectivos que não aparecem nos 5 `cancelamentos` de hoje, mas que se somam a uma série acumulada de ciclos documentada desde 22/05. O número "5 cancelamentos" nas métricas de superfície subestima a pressão real sobre `cancellations_rate` da reputação, que ainda está em zero oficial. Com threshold Platinum cruzado (`gap_revenue_brl=0`, `progress_pct=100%`) e `power_seller_status` ainda `gold`, a conta está exatamente na janela de maior sensibilidade: mais um ciclo com cancelamentos automáticos da Tulipa entrando no sistema pode ser o evento que move `cancellations_rate` de zero para positivo antes do reconhecimento formal da medalha. A L01 e a L02 já identificaram esse risco — a operação de ontem não o neutralizou, adicionou mais uma carga. É o fato operacional central do dia.