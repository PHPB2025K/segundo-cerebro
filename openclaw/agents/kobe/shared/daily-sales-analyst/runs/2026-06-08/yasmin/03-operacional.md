<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **Volume e GMV sustentados por volume real, com ticket comprimido por composição — não por erosão:** 201 pedidos = +62,8% vs `avg_30d` (123,5) e +76,3% vs `avg_60d` (114,0). Ticket médio de R$ 44,03 está -8,4% vs 30d (R$ 48,08), mas +2,4% vs 60d (R$ 43,01) — a compressão vs 30d é integralmente efeito de composição do cluster IMB501 de menor valor unitário dominando o topo (43,3% do volume), não deterioração estrutural de ticket. O GMV de R$ 8.850 é o segundo Monday consecutivo acima de R$ 8.500 (01/06: R$ 9.814; média histórica de segundas: R$ 5.697 via `same_weekday_avg`), confirmando operacionalmente o patamar elevado identificado pela L01 — o dia não adiciona novidade, confirma.

- **Cluster IMB501 com 43,3% do volume, mas mix de modalidade de envio voltou ao padrão histórico após distorção de 07/06:** IMB501C (Tampa Cinza, 41 pedidos, Full) + IMB501P (Tampa Preta, 28 pedidos, Cross-Docking) + IMB501V (Tampa Vermelha, 18 pedidos, Full) = 87 pedidos = 43,3% do dia; `top3_concentration=44,3%` e `top5_concentration=61,2%`. Concentração alta e consistente com os ciclos recentes. O mix da modalidade de envio do top10 (Full 78,5% / Cross-Docking 21,5%, via `fulfillment_mix_yesterday_top10`) ficou -1,1pp vs 30d (Full 79,6%, `fulfillment_mix_30d`) — diferença não material. Isso contrasta diretamente com 07/06, quando o supply depletado do MLB3288536143 distorceu o mix para Full 67,2% (-12,9pp). O restock confirmado (`available_quantity`: 2 → 1.056 no MLB3288536143) restaurou o equilíbrio de modalidade de envio — fato operacional relevante para a Condensadora.

- **Dois vetores Full em cobertura de estoque crítica: risco prospectivo concreto e simultâneo para a janela Platinum recém conquistada:** MLB4073003575 (Kit 4 Potes 1050ml, Full, `health=0,75`) com `available_quantity=33` após 15 pedidos → runway prospectivo ~2,2 dias ao ritmo atual. MLB6073033006 (Kit 6 Canequinhas Acrílico, Full, `health=null`) com `available_quantity=19` após 11 pedidos → runway ~1,7 dias. Ambos em Full: ruptura gera cancelamentos automáticos que entram na janela rolling do Platinum (`cancellations_rate` oficial = 0). A memória documenta o MLB4073003575 chegando a 2 unidades em 02/06 e 33 unidades em 07/06 — o restock não está cobrindo o ritmo do novo patamar. Este é o sinal #1 da L01 confirmado com dados do dia; adiciona a simultaneidade dos dois vetores, que a L01 apontou mas a leitura de hoje torna mais concreta.

- **ADS share 47,1% consolida série orgânica descendente — sétimo ponto consecutivo, segundo ciclo abaixo de 50%:** spend R$ 429,97, revenue_ads R$ 4.169,41, ROAS 9,70x, ACOS 11,67%, share 47,1% (4.169 / 8.850). A série de 22/05 a 08/06: 69,9% → 56,7% → 60,7% → 59,5% → 51,4% → 48,1% → **47,1%** — monotonicamente descendente enquanto o GMV subiu 80% no mesmo período. O ACOS de 11,67% está no primeiro ciclo acima de 10% da série, mas o ROAS de 9,70x (muito acima do limiar de ineficiência) indica que a campanha segue eficiente. Confirma o sinal #3 da L01 — segundo ciclo consecutivo abaixo de 50% em dia de alto GMV.

---

### Sinais operacionais relevantes

- **Sinal:** MLB4073003575 (Kit 4 Potes 1050ml, Full) com `available_quantity=33` pós-baixa de 15 pedidos → runway prospectivo ~2,2 dias — **interpretação operacional:** padrão recorrente documentado desde 02/06 (chegou a 2 unidades naquele ciclo); o restock entre 07/06 e 08/06 repôs estoque, mas insuficiente para cobrir o ritmo do novo patamar. Sem ETA confirmado de novo restock ao CD do ML, o anúncio pode pausar antes do próximo snapshot e gerar cancelamentos automáticos que entram direto na janela rolling Platinum.

- **Sinal:** MLB6073033006 (Kit 6 Canequinhas Acrílico, Full) com `available_quantity=19` pós-baixa de 11 pedidos → runway prospectivo ~1,7 dias — **interpretação operacional:** primeira aparição em zona crítica confirmada neste nível. `health=null` (volume insuficiente para cálculo ML, não indicativo de saúde OK). A simultaneidade com MLB4073003575 em cobertura crítica é o que eleva o risco: dois Full podendo pausar no mesmo janela, amplificando impacto no mix de modalidade de envio do topo e no `cancellations_rate` Platinum.

- **Sinal:** 6 cancelamentos no dia (3,0% dos 201 pedidos) — **interpretação operacional:** não é o maior valor da série (01/06: 9; 31/05: 6), mas a impossibilidade de atribuir por `platform_item_id` (pendência estrutural de 18+ ciclos) impede separar cancelamentos de comprador/vendedor de cancelamentos automáticos por ruptura. Com dois Full em cobertura < 2,5 dias, qualquer cancelamento automático prospectivo dos próximos dias viria se somar à série e pressionar a janela Platinum antes do `cancellations_rate` oficial mostrar sinal.

- **Sinal:** MLB5402326666 (Kit 4 Potes 640ml, Full) com `health=0,66` — 4º+ ciclo consecutivo em nível preocupante, sem variação registrada — **interpretação operacional:** health estabilizado em patamar que o ML penaliza com redução de ranking orgânico; 16 pedidos hoje sugerem que ADS e boost Platinum estão compensando a perda de exposição orgânica. Gatilho da L02 é `health < 0,63` — a 0,03 da leitura atual. Sem série interna de direção, não é possível confirmar estabilização vs degradação vagarosa.

- **Sinal:** concentração horária intensa no bloco 20h-23h — 95 pedidos = 47,3% do total, com pico de 39 pedidos em 21h (19,4% do dia em uma única hora) — **interpretação operacional:** sem série histórica de distribuição horária por dia da semana disponível no pacote, não é possível classificar como padrão ou anomalia. O pico de 21h é muito acima de qualquer outra hora (próximas: 22h com 26, 23h com 18, 16h com 13). Se reflete configuração de lance ADS por horário, pode explicar eficiência/ineficiência concentrada que o ACOS médio agrega sem mostrar.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O resultado do dia é operacionalmente coerente com a tese de patamar elevado da L01: segundo Monday consecutivo acima de R$ 8.500, GMV +80,5% vs 60d, Platinum confirmado, ADS share na série descendente correta, mix de modalidade de envio restaurado ao padrão histórico. O que impede classificar como "sem anomalia" são dois desvios operacionais concretos e acionáveis: (1) dois anúncios Full com cobertura prospectiva de estoque abaixo de 2,5 dias (MLB4073003575 ~2,2d e MLB6073033006 ~1,7d), podendo pausar antes do próximo snapshot sem restock confirmado — padrão recorrente que o novo patamar de demanda tornou mais urgente; (2) 6 cancelamentos sem atribuição possível, em contexto onde o `cancellations_rate` oficial está em zero e qualquer cancelamento automático de ruptura entra diretamente na janela rolling Platinum recém conquistada. Para subir para "anomalia moderada" seria necessário um dos dois Full já pausar com pedidos pendentes, ou `cancellations_rate` oficial sair de zero no próximo snapshot.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** qual é o ETA de restock em trânsito ao CD do ML para MLB4073003575 (Kit 4 Potes 1050ml, 33 unidades) e MLB6073033006 (Kit 6 Canequinhas Acrílico, 19 unidades) — e existe lote já enviado que chega antes de ambos atingirem zero? — **Motivada por:** sinais #1 e #2 — ambos com runway < 2,5 dias ao ritmo atual em Full; sem ETA confirmado, não é possível dimensionar o risco Platinum nem priorizar qual dos dois é mais urgente.

- **Pergunta:** qual a direção do `health` do MLB5402326666 (Kit 4 Potes 640ml, 0,66) neste ciclo comparado ao ciclo anterior — estabilizou, caiu ou subiu? — **Motivada por:** sinal #4 — quarto ciclo em nível preocupante sem registro de variação; o gatilho de alinhamento com Himmel da L02 é `health < 0,63`, a apenas 0,03 da leitura atual; saber a direção é o que separa observação contínua de ação imediata.

- **Pergunta:** quais são os `platform_item_id` e motivos (comprador, vendedor, automático) dos 6 cancelamentos do dia? — **Motivada por:** sinal #3 — sem atribuição, não é possível confirmar se algum viria de ruptura automática nos anúncios em cobertura crítica, o que mudaria a leitura de risco Platinum de "prospectivo" para "já iniciado".

- **Pergunta:** a concentração de 47,3% dos pedidos no bloco 20h-23h (com pico de 39 em 21h) é recorrente em segundas-feiras ou foi específica deste ciclo? — **Motivada por:** sinal #5 — sem série histórica horária disponível no pacote; se o padrão for recorrente, informa calibragem de ADS por janela horária com Himmel; se for específico do dia, merece investigação de causa.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o volume recorde de segunda-feira — isso a L01 já cobriu como confirmação de patamar. É que o restock do MLB3288536143 restaurou o mix de modalidade de envio do topo de volta ao padrão histórico (Full 78,5% vs 30d Full 79,6%), revertendo a distorção de 07/06 — o canal está rodando com a estrutura esperada, não em modo de compensação emergencial.

O risco silencioso que pode passar despercebido: MLB4073003575 e MLB6073033006 estão **simultaneamente** com cobertura < 2,5 dias em Full. O MLB4073003575 chegou a 2 unidades em 02/06 e foi reposto parcialmente; com o novo patamar de demanda (+62,8% vs 30d), a mesma quantidade de restock que antes durava uma semana agora dura dois dias. Se ambos pausarem no mesmo ciclo — o que é plausível ao ritmo atual sem restock confirmado —, o mix de modalidade de envio do topo colapsa novamente para o padrão distorcido de 07/06, os cancelamentos automáticos entram na janela rolling de um Platinum que tem `cancellations_rate` em zero e ainda não tem amortecimento acumulado, e o que seria "manutenção de patamar" vira evento de degradação de reputação num momento em que a promoção tem menos de 24h. A Condensadora deve carregar isso como risco operacional ativo, não como "dois anúncios com estoque baixo".