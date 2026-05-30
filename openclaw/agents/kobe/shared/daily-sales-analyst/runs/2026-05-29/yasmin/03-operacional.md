<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **Volume e ticket confirmam rompimento de patamar em todas as janelas:** 143 pedidos representam +35.4% vs média 30d (105.6) e +37.5% vs mesmos dias da semana (avg 104); GMV R$7.597 supera em +51.1% a média 30d e +49.8% o controle de dia da semana; ticket R$53.13 está +11.6% acima do 30d e +26.3% acima do 60d. Volume e ticket sobem juntos — não é efeito de composição de mix, é duplo vetor. Confirma operacionalmente a tese da L01 de rompimento de patamar nas três janelas.

- **Cluster IMB501 respondeu por 45.5% do dia, concentração retornando ao topo da série:** Tampa Preta (40 pedidos) + Tampa Vermelha (14) + Tampa Cinza (11) = 65 pedidos no mesmo listing MLB3288536143. `top3_concentration=51%`, `top5_concentration=65%`. A concentração de 45.5% supera o patamar de 26/05 (44.8%) e retoma a trajetória documentada no weekly — portfólio operacional estreito sustentando o resultado mais forte da série. O ponto operacional relevante: esse resultado passou por um único anúncio não-catálogo, Full, com health=0.71 no oitavo ciclo idêntico.

- **Mix de modalidade de envio do dia: 100% Full** (`fulfillment_mix_yesterday_top10.full_pct=100%`) contra 77.0% Full em 30d e 84.4% em 7d. A divergência é produto-específica — todos os campeões do dia operam em Full, enquanto a base ativa da conta é 61% Cross-Docking (`account_overview.active_analysis.fulfillment_mix.cross_docking_pct=61%`). A intensidade da concentração Full no top10 do dia confirma operacionalmente a assimetria estrutural da L01: o resultado recorde foi gerado inteiramente pela modalidade sujeita às rupturas iminentes mapeadas.

- **Anúncio pausado com estoque zero gerou 19 pedidos:** MLB6167272090 (Kit 6 Canecas Tulipa 250ml) está `status=paused`, `available_quantity=0`, mas registrou 19 pedidos no dia — 13.3% do volume total. Esses 19 pedidos são cancelamentos prospectivos ainda fora da `reputation.cancellations_rate` (hoje em 0). O risco identificado pela L01 desde o ciclo de 22/05 se confirma na execução: o anúncio não parou de receber pedidos mesmo após pausa e zeragem de estoque. A convergência entre o ETA de Platinum (~5.9 dias) e o janelamento de processamento desses cancelamentos é o dado operacional mais grave do dia.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 6 Canecas Tulipa 250ml (MLB6167272090) com `status=paused`, `available_quantity=0` gerou 19 pedidos no dia — **interpretação operacional:** cancelamentos prospectivos garantidos fora da métrica oficial; se processados como iniciados pelo vendedor, `cancellations_rate` sai de 0 dentro de 3–5 ciclos, comprometendo elegibilidade para MercadoLíder Gold exatamente no ETA de 5.9 dias para Platinum. Confirma e materializa o risco estrutural principal da L01.

- **Sinal:** Três anúncios Full com cobertura inferior a 1.5 dia — Kit 10 Potes 1050ml — 6 un (MLB4676751119, `available_quantity=1`, ~5 pedidos/dia → cobertura <1 dia), Kit 10 Potes 640ml — 6 un (MLB6754669844, `available_quantity=2`, ~3 pedidos/dia → <1 dia), Kit 10 Potes 1050ml — 10 un (MLB4676726433, `available_quantity=9`, ~8 pedidos/dia → ~1.1 dia) — **interpretação operacional:** ruptura confirmada no próximo ciclo para dois deles sem reposição em trânsito confirmada; três rupturas simultâneas em Full comprimem ainda mais o portfólio operacional ativo e reforçam a cadeia de risco da L01.

- **Sinal:** Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo gold_pro Full) aparece com `available_quantity=72` pós-baixa de 9 pedidos — **interpretação operacional:** na memória de 26/05 estava com 31 unidades e cobertura ~2.1 dias; hoje 72 unidades sugerem reposição ao CD do ML entre 26/05 e 29/05. Cobertura prospectiva ~8 dias ao ritmo de ~9 pedidos/dia. Se confirmado pela Granular, o único anúncio em Catálogo ativo saiu da zona crítica — redução parcial do risco de Catálogo mapeado pela L01, ponto positivo contra o backdrop de rupturas.

- **Sinal:** Health de MLB3288536143 (0.71) e MLB4073003575 (0.75) no **oitavo ciclo idêntico** sem variação observável — **interpretação operacional:** nem deterioração ativa nem recuperação; o dia não acrescenta sinal novo aqui. O gatilho da L02 (<0.68 em qualquer dos dois) permanece em aberto, mas estabilidade por oito ciclos é dado relevante por si só — os dois campeões funcionam no patamar penalizado sem piora aparente.

- **Sinal:** ADS share 60.9% (`revenue_ads_yesterday_brl=R$4.630,06` / `totals.gmv=R$7.597,76`), ROAS 12.2x, ACOS 5.74% — **interpretação operacional:** quarto ciclo consecutivo com share acima de 60% (22/05: 69.9%, 25/05: 56.7%, 26/05: 60.7%, hoje: 60.9%). ACOS normalizou vs pico de 10.96% em 26/05, campanha eficiente. O resultado recorde da série é 60.9% suportado por ADS — dependência elevada e estruturalmente estável, sem ativar gatilho de ineficiência. Confirma a leitura da L01 sobre dependência de mídia paga sem adicionar deterioração nova.

---

### Anomalias ou ausência de anomalia

**anomalia crítica**

O critério explícito da classificação cobre o caso: anúncio crítico (`Kit 6 Canecas Tulipa 250ml`, MLB6167272090) operou com volume expressivo (19 pedidos, 13.3% do dia) em estado pausado com estoque zero. Independente da performance geral do dia, 19 cancelamentos prospectivos garantidos sobre `cancellations_rate=0` dentro do janelamento de ETA para Platinum (~5.9 dias) é desvio operacional que compromete execução futura. Adicionalmente, três anúncios Full com cobertura <1.5 dia configuram segunda dimensão simultânea de comprometimento — não é ruído isolado, é padrão com causa comum (gestão de estoque Full).

Para descer a anomalia moderada: os 19 pedidos da Tulipa sendo absolvidos pelo sistema sem registro como cancelamentos pelo vendedor, e confirmação de reposição em trânsito para ao menos dois dos três Kit Potes no próximo snapshot.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Os 19 pedidos registrados sobre Kit 6 Canecas Tulipa 250ml (MLB6167272090, paused, available=0) já geraram cancelamentos automáticos pelo ML? Se sim, foram classificados como iniciados pelo vendedor ou pelo comprador? — **motivada por:** sinal 1 (Tulipa com volume sobre anúncio pausado/zerado), determinante para `cancellations_rate` e elegibilidade no ciclo de Platinum.

- **Pergunta:** Há reposição em trânsito ao CD do ML para Kit 10 Potes 1050ml — 6 un (MLB4676751119, available=1) e Kit 10 Potes 640ml — 6 un (MLB6754669844, available=2)? Qual o ETA de chegada ao CD? — **motivada por:** sinal 2 (cobertura <1 dia em dois anúncios Full), ruptura garantida no próximo ciclo sem reposição confirmada.

- **Pergunta:** A `available_quantity=72` do Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo Full gold_pro) confirma entrada de reposição entre 26/05 e 29/05? Em que volume entrou e qual a projeção de cobertura ao ritmo atual (~9 pedidos/dia)? — **motivada por:** sinal 3 (possível saída da zona crítica do único Catálogo ativo), relevante para avaliar se o risco de Catálogo da L01 foi parcialmente mitigado.

- **Pergunta:** O `revenue_ads_yesterday_brl=R$4.630,06` está concentrado em qual conjunto de anúncios? A campanha está priorizando o cluster IMB501 (MLB3288536143) ou há verba sendo direcionada para os anúncios de potes com ruptura iminente (MLB4676726433, MLB4676751119, MLB6754669844)? — **motivada por:** sinal 5 (ADS 60.9% do GMV) cruzado com sinal 2 (três ruptures iminentes em Full); relevante para L02 avaliar se a campanha está amplificando anúncios que vão pausar no próximo ciclo.

---

### Destaque para a Condensadora

O fato operacional que merece atenção não é o GMV — é o que está por baixo dele. O resultado mais forte da série (R$7.597) foi gerado em parte por um anúncio que estava pausado com estoque zero e ainda assim acumulou 19 pedidos. Esses 19 pedidos não aparecem em nenhuma métrica de reputação hoje — `cancellations_rate=0` — mas são cancelamentos prospectivos que entrarão na janela oficial em ciclos futuros. O timing é o problema: o ETA para Platinum é 5.9 dias, e a mesma semana que pode consolidar a promoção é a que concentra o maior volume de cancelamentos prospectivos pendentes da série. A Condensadora deve carregar isso como risco silencioso que a métrica do dia não mostra — não como alarme de execução presente, mas como gatilho iminente. O contrapeso positivo é o Kit 6 Canecas Lisas 200ml (Catálogo), que parece ter recebido reposição e saído da zona crítica — vale confirmar, porque se confirmado, o único anúncio Catálogo ativo está estabilizado, reduzindo parcialmente o espectro de riscos da L01.