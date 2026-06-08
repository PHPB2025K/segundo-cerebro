<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- O dia operou no regime de supply depletado confirmado: 84 pedidos (−23,8% vs `same_weekday_avg.avg_orders=110,25`) e GMV R$4.115 (−20,8% vs `same_weekday_avg.avg_gmv=R$5.200`) encaixam na banda histórica dos domingos de 17-24/05 (98-100 pedidos, R$4.996-R$5.180), mas abaixo dessas referências. O vetor é o mesmo documentado pela L01: Conjunto 5 Potes Tampa Vermelha (MLB3288536143, Full) reapareceu ativo após pausa com zero estoque em 06/06, gerou 10 pedidos com estoque residual de ~12 unidades e encerrou com `available_quantity=2` — restock insuficiente já praticamente consumido, ciclo de ruptura na iminência de nova volta. O domingo de 31/05 (189 pedidos, R$8.267) com o líder Full em plena capacidade confirma que o patamar duplo identificado pela L01 não é abstração estratégica: é diferença operacional observável de 2,25× nos pedidos e 2× no GMV no mesmo dia da semana.

- O ticket médio R$49,00 (+10,5% vs `historical.avg_60d.avg_ticket=R$44,33`, +2,1% vs `historical.avg_30d.avg_ticket=R$47,98`) é efeito de composição de mix, não ganho estrutural: com o cluster IMB501 em volume restrito (Full líder com supply residual), produtos de ticket unitário maior ganharam peso relativo — Kit 4 Potes 800ml (8 pedidos), Kit 6 Canequinhas (6 pedidos), Pote 520ml e Kit 4 Potes 1050ml (4 pedidos cada). Operacionalmente, o canal não expandiu alcance; redistribuiu faturamento entre produtos de maior valor diante do vácuo do campeão. Confirma o mecanismo descrito pela L01.

- O mix de modalidade de envio do dia (Full 67,2% vs `fulfillment_mix_30d.full_pct=80,1%`, −12,9pp) divergiu do padrão mensal por razão produto-específica: Tampa Cinza (MLB4535849169, Cross-Docking, 10 pedidos) e Tampa Preta (MLB4535865317, Cross-Docking, 10 pedidos) empataram com Tampa Vermelha (MLB3288536143, Full, 10 pedidos) no topo do ranking. Nos dias de Full líder em plena capacidade, a variante Full puxa 40-100 pedidos e domina o mix; hoje, com supply residual, as duas variantes Cross-Docking absorveram a fatia proporcional. A divergência é produto-específica e pontual — mas adiciona evidência operacional à L01 sobre a estreiteza da base Full do canal: um único anúncio determina 10-13pp do mix de modalidade de envio do topo da conta.

- ADS share de 64,2% (`ads_summary.revenue_ads_yesterday_brl=R$2.642` / `metrics.gmv=R$4.115`) com ROAS 8,78x e ACOS 9,01% — dentro da faixa eficiente, mas no segundo ciclo consecutivo acima de 60%. O padrão confirma operacionalmente o mecanismo identificado pela L01 e endossado pela L02: gasto de campanha (~R$300) estável, GMV comprimido pelo supply depletado, ratio inflado por denominador menor. Não é ineficiência de campanha — é artefato de supply. Acionamento de Himmel para ajuste não tem motivação operacional neste ciclo.

---

### Sinais operacionais relevantes

- **Sinal:** MLB3288536143 (Conjunto 5 Potes Tampa Vermelha, Full) encerrou com `available_quantity=2` após 10 pedidos, confirmando restock de ~12 unidades pós-pausa com zero estoque em 06/06 — **interpretação operacional:** o restock de ~12 unidades não cobre um domingo (menor volume da semana); nos dias úteis com ritmo histórico de 40-100 pedidos/dia, o estoque residual de 2 unidades se esgota em horas. Nova pausa é prospectivamente imediata, repetindo o ciclo documentado em pelo menos 3 episódios desde 01/06. Cada nova pausa com pedidos ativos alimenta `cancellations_rate` (06/06: 67 pedidos prospectivamente canceláveis) e corrói a margem de segurança do MercadoLíder Platinum (`sales_60d_revenue_brl=R$298.699`, apenas R$2.699 acima do threshold em janela rolling).

- **Sinal:** Kit 4 Potes de Vidro 640ml Azul-petróleo (MLB5402326666, Full, Clássico) com `health=0,66` — 4º+ ciclo consecutivo abaixo de 0,85, menor nível calculado entre todos os top 10 — **interpretação operacional:** o padrão de 4 ciclos sem recuperação é o mais longo de degradação ativa no snapshot atual e confirma penalização ML progressiva sobre ranking orgânico de categoria. Com 3 pedidos no dia (vs 4 em ciclos anteriores), há indício de erosão incremental de exposição. Está a 0,03pp do limiar L02 (0,63) para acionamento de alinhamento Yasmin–Himmel sobre cobertura ADS preventiva.

- **Sinal:** Tampa Cinza (MLB4535849169, Cross-Docking, `available_quantity=86`) empatou em 10 pedidos com o líder Full depletado — **interpretação operacional:** a variante Cross-Docking absorveu demanda que o Full não conseguiu capturar. Operacionalmente funcional hoje, mas o anúncio tem `sold_quantity=14` vs `sold_quantity=6.845` do líder Full — historial de venda radicalmente diferente. Não há garantia de que mantém o mesmo nível de exposição nos ciclos seguintes fora do contexto de demanda represada pelo Full depletado.

- **Sinal:** Kit 2 Potes de Vidro 800ml Quadrado (MLB3918271667, Full, `is_catalog=true`) — único anúncio Catálogo (`is_catalog=true`) entre os top 10, 3 pedidos, `available_quantity=23` POST-baixa, `health=null` — **interpretação operacional:** cobertura prospectiva ~7-8 dias ao ritmo de domingo; sem risco imediato. `health=null` significa que o ML não computa nível de qualidade por volume insuficiente — não sinaliza saúde, apenas ausência de cálculo. É o único vetor de Buy Box de Catálogo no topo do dia; estoque abaixo de ~10 unidades começa a expor a posição.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.** O dia executou dentro do padrão operacional dos domingos de capacidade reduzida — 1 cancelamento não-sistemático, reputação verde estável (`color=5_green`, `cancellations_rate=0`, `claims_rate=0,0018`), nenhum anúncio top 10 pausado com pedidos ativos. O sinal que impede classificar como "sem anomalia relevante" é o `available_quantity=2` de MLB3288536143 ao final do dia: o anúncio voltou a operar em beira de pausa após restock de ~12 unidades — volume que o menor dia da semana consumiu integralmente. A anomalia não está na execução de 07/06; está no padrão recorrente que ela representa: terceiro restock insuficiente em sete dias, confirmando que o ciclo de ruptura não foi endereçado. Para subir para anomalia moderada: `cancellations_rate` sair de zero (confirmando que pedidos prospectivos de 06/06 ou iminentes de 07/06 entraram na janela oficial ML), ou um segundo campeão Full atingir `available_quantity < 5` simultaneamente.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** qual o `status` e `available_quantity` atual de MLB3288536143 (Conjunto 5 Potes Tampa Vermelha, Full) no snapshot pós-07/06? — **Motivada por:** `available_quantity=2` ao final do dia; nova pausa é prospectivamente imediata (Sinal 1 e Leitura Op 1).

- **Pergunta:** há lote de reposição confirmado em trânsito para MLB3288536143 no CD do ML — volume e ETA? — **Motivada por:** três episódios de restock insuficiente desde 01/06 sugerem subdimensionamento crônico do lote; o volume do próximo lote define se o ciclo bifásico pode ser quebrado ou é estrutural (Sinal 1).

- **Pergunta:** qual a direção interna do `health` de MLB5402326666 (Kit 4 Potes 640ml) nos últimos 4 ciclos — estabilizado em 0,66 ou em queda incremental? — **Motivada por:** 4º ciclo em nível preocupante, a 0,03pp do limiar L02 (0,63) para acionamento de alinhamento Yasmin–Himmel sobre cobertura ADS preventiva (Sinal 2).

- **Pergunta:** qual o breakdown de `revenue_ads_yesterday_brl` por `platform_item_id` em 07/06 — a campanha do Himmel priorizou quais anúncios nos dias de supply comprimido do Full líder? — **Motivada por:** ADS share de 64,2% com Full líder em capacidade residual; sem o breakdown, não é possível afirmar se a campanha priorizou os Cross-Docking com estoque ou tentou capturar demanda para o Full quase esgotado, o que seria ineficiente e potencialmente geraria cancelamentos prospectivos adicionais (Lente Op 5).

---

### Destaque para a Condensadora

O fato operacional que a Condensadora não deve perder ao compor a mensagem final: o restock de MLB3288536143 foi de ~12 unidades — volume que um domingo, o menor dia da semana, consumiu integralmente. A conta está, neste momento, na iminência do quarto episódio de pausa documentado em sete dias. O dia 07/06 em si executou dentro do esperado para o regime de supply depletado; o risco não está no passado — está nas próximas horas, quando o `available_quantity=2` residual se esgota e o ciclo ruptura → cancelamentos prospectivos → pressão em `cancellations_rate` se repete com demanda de dia útil (40-100 pedidos/dia histórico). A Condensadora deve carregar não o volume do dia, mas o dado de velocidade de consumo: ~12 unidades em menos de um domingo é evidência operacional de que o lote de reposição está sistematicamente subdimensionado para a demanda do canal. A L01 e L02 identificaram o vetor — o operacional de hoje confirma e adiciona urgência de ritmo ao padrão.