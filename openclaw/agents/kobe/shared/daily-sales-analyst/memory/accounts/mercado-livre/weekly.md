# Weekly — Mercado Livre

## Estrutura

Consolidação semanal da conta. Atualizada toda segunda de manhã ou após 7 entradas diárias acumuladas.

## Template

### Semana: [DD/MM a DD/MM/AAAA]

#### Tese semanal
[Tese consolidada da semana baseada nas leituras diárias]

#### Padrões observados
- [Padrão 1]
- [Padrão 2]

#### Hipóteses ativas
- [Hipótese 1 — status: confirmada/enfraquecida/em aberto]

#### Riscos acumulados
- [Risco 1 — persistência: X dias]

#### Sinais para próxima semana
- [Sinal 1 — condição falsificável]

#### Ressalvas da semana
- [Ressalva 1 — frequência: X ocorrências]

---

## Memória diária acumulada

_Blocos diários abaixo. Job `daily-memory-ingest-ml.py` adiciona um bloco por dia. Rotação automática mantém os últimos 14 dias._

### Dia analisado: 2026-06-04
_ingestido em 2026-06-05T09:40:42-03:00 BRT | confiança L05: media | insights L05: 3 (2 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- MercadoLíder Platinum — gap R$ 3.744,66, progresso 98,73%, ETA estimado 0,8 dias ao ritmo R$ 4.870,92/dia, Faturamento de hoje R$ 8.712 (1,79x o pace); confirmar no próximo snapshot se medalha_atual virou platinum ou se ponta saindo da janela rolling 60d compensou a entrada do dia 04/06
- Kit 6 Canecas Porcelana Lisa Reta 200ml (MLB6232315532, Catálogo gold_pro Full): 6 unidades pós-baixa de 16 pedidos, trajetória descendente em 3 ciclos (28→6 entre 02/06 e 04/06) sem evidência de restock — único Catálogo gold_pro do topo; ruptura derruba Buy Box
- Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full): restock parcial confirmado (0→9 unidades desde paused em 02/06), mas 18 pedidos no dia mantêm runway sub-dia; 7º ciclo do padrão de ruptura recorrente
- Cluster IMB501 em 49,4% do dia (13º ciclo de concentração): IMB501C 41 + IMB501V 28 em Full no MLB3288536143 (nível regular 0,71 idêntico há 13 ciclos, available_quantity=89 pós-baixa de 69 pedidos, restock confirmado retroativamente de 13→89) + IMB501P 20 em Cross-Docking no MLB4535865317 (estoque robusto 8.310 un); a divergência -13pp Full vs 30d é integralmente IMB501P puxando
- Kit 4 Potes 640ml Tampa Azul-petróleo (MLB5402326666, Full): nível preocupante 0,66 no 2º ciclo (menor nível do snapshot, abaixo do threshold 0,85); 4 pedidos no dia coerente com perda de exposição orgânica — próximo ciclo classifica como recorrente ou pontual
- ADS: fatia de 55,25% do faturamento (R$ 4.813,97 / R$ 8.712,49), ROAS 14,37x, ACOS 10,68% — segundo ponto consecutivo na faixa 50-55% após piso de 48,1% em 01/06; série já não é monotonicamente descendente
- ratings_negative 0,41 estagnou (não avançou vs 01/06 mas não reverteu da alta vs 22-23/05); claims_rate 0,0017 (34% do threshold 0,005); cancellations_rate oficial em zero apesar dos 3 cancelamentos do dia (1,67% sobre 180 pedidos) — divergência semântica esperada entre janela curta e janela longa ML
- Pendências estruturais do pacote ML (13º ciclo consecutivo desde 22/05): breakdown ADS spend/revenue por platform_item_id; série temporal de nível de qualidade por anúncio + drivers; lista granular de cancelamentos order_id↔platform_item_id↔motivo; ETA de reposição em trânsito ao CD do ML; available_quantity por variação em anúncios multi-variação

### Dia analisado: 2026-06-02
_ingestido em 2026-06-03T07:16:19-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, Full, nível regular 0,75): available_quantity=2 pós-baixa de 12 pedidos — confirmar amanhã se reposição entrou, se status virou paused ou se ruptura se materializou; define se o novo patamar de R$ 9k se sustenta nos próximos 2 dias.
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara (MLB6167272090, Full, paused, available_quantity=0): oitavo ciclo do padrão, 8 pedidos prospectivamente cancelados — monitorar cancellations_rate da reputação nos próximos 1-3 snapshots; sair de zero confirma entrada da série acumulada na janela oficial e aperta diretamente o ETA Platinum.
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida (MLB6232315532, Catálogo gold_pro Full, sem nível de qualidade calculado pelo ML): available_quantity=28 pós-baixa de 11 pedidos, cobertura ~2,5 dias — único Catálogo no top 5; ruptura derruba Buy Box.
- MercadoLíder Platinum: gap R$ 11.621,68, progresso 96,07%, ETA 2,5 dias ao ritmo médio R$ 4.739/dia — Faturamento de hoje (R$ 9.210) 79% do gap em um único dia; promoção ao alcance de 2-3 dias mas diretamente vulnerável a movimento adverso no cancellations_rate.
- Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo (MLB5402326666, Full, nível preocupante 0,66): menor nível do snapshot, abaixo do threshold 0,85 — primeira aparição em zona crítica; observar próximo ciclo para classificar como recorrente ou pontual e tentar identificar driver (claims, atrasos, listing).
- ADS share recuperou de 48,1% (01/06) para 54,9% hoje (R$ 5.059 / R$ 9.210), quebrando série monotonicamente descendente desde 22/05; ROAS 14,45x e ACOS 4,7% no piso de eficiência — hipótese aberta: os 8 pedidos da Tulipa pausada podem estar inflando o numerador; sem breakdown por platform_item_id (12º ciclo de pendência), não é possível separar aceleração real de artefato métrico.
- Cluster IMB501 respondeu por 99 pedidos = 50,3% do dia, mas NÃO é homogêneo em modalidade: Tampa Preta (MLB4535865317) opera Cross-Docking com estoque robusto (8.327 un, sem risco); Tampa Cinza+Vermelha compartilham MLB3288536143 em Full (available_quantity agregado=137, nível regular 0,71 no 11º ciclo idêntico) — comunicar como bloco único perde a diferença material entre os vetores.
- Pendências estruturais recorrentes desde 22/05 (12º ciclo): (1) breakdown ADS spend/revenue por platform_item_id; (2) lista granular cancelamentos order_id↔platform_item_id↔motivo; (3) série temporal de nível de qualidade por anúncio; (4) ETA de reposição ao CD do ML; (5) available_quantity por variação em anúncios multi-variação; (6) drivers de nível de qualidade por anúncio.

### Dia analisado: 2026-06-01
_ingestido em 2026-06-02T07:10:37-03:00 BRT | confiança L05: media | insights L05: 3 (2 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, Full, nível preocupante 0,71 — décimo primeiro ciclo idêntico): 118 pedidos no dia e available_quantity=13 no snapshot 02/06 09:50 UTC; confirmar amanhã se reposição entrou, se caiu abaixo de 5 ou se virou paused — define se o patamar de ~R$ 10k se sustenta ou colapsa.
- Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, Full, nível regular 0,75 — décimo primeiro ciclo idêntico): available_quantity=13 após 14 pedidos; segundo Full em cobertura crítica simultânea ao IMB501.
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida (MLB6232315532, Catálogo gold_pro Full, sem nível de qualidade calculado pelo ML): available_quantity=35 após 19 pedidos, cobertura ~1,6 dias; terceiro vetor Full em zona estreita — ruptura em Catálogo derruba Buy Box.
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara (MLB6167272090, Full, sem nível calculado): reapareceu ativa com 2 unidades após pausar em 31/05 com zero — reposição parcial entre 31/05 e 02/06 confirmada, mas próximas vendas acionam pausa.
- MercadoLíder Platinum: gap R$ 16.112, progresso 94,56%, ETA 3,5 dias ao ritmo médio R$ 4.665/dia — Faturamento do dia (R$ 9.953) 113% acima do pace; cancellations_rate oficial em zero, mas série crescente (3→3→2→6→9 em 5 dias) é vetor latente; qualquer movimento adverso aperta a janela.
- 9 cancelamentos no dia (4,4% dos 206 pedidos) — maior valor absoluto da série recente, sem atribuição por anúncio possível pelo pacote; ratings_negative subiu de 0,39 para 0,41 (movimento na direção errada em 6.297 transações, mas cor verde mantida e claims_rate em 38% do threshold).
- ADS share monotonicamente descendente desde 22/05: 69,9% → 56,7% → 60,7% → 59,5% → 51,4% → 48,1%, com GMV ascendente — primeiro ciclo abaixo de 50%; ROAS 10,6x e ACOS 8,89% no piso da série; orgânico expandindo proporcionalmente mais rápido que campanha.
- Pendências estruturais recorrentes do pacote ML (desde 22/05): (1) breakdown ADS spend/revenue por platform_item_id; (2) lista granular de cancelamentos com order_id↔platform_item_id↔motivo; (3) série temporal de nível de qualidade por anúncio; (4) estoque em trânsito ao CD do ML / ETA de reposição Full; (5) available_quantity por variação dentro de anúncios multi-variação; (6) timestamp de reativação/reposição da Tulipa.

### Dia analisado: 2026-05-31
_ingestido em 2026-06-01T07:11:08-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 2_

**Memória para o próximo ciclo (da L05):**
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, Full, nível regular 0,71 — décimo ciclo idêntico): cluster IMB501 fez 121 pedidos (66 Tampa Preta + 28 Tampa Cinza + 27 Tampa Vermelha) e fechou com 38 unidades agregadas pós-baixa; confirmar amanhã se reposição entrou, se available_quantity caiu abaixo de 10 ou se status virou paused — define se patamar de R$ 8k se sustenta ou retrai
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara (MLB6167272090, Full, status=paused, available_quantity=0): 4 pedidos no dia que viram cancelamentos prospectivos — monitorar cancellations_rate da reputação nos próximos 3-5 snapshots; sair de zero confirma entrada na janela oficial e aperta ETA Platinum
- Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, Full, nível regular 0,75): 30 unidades pós-baixa de 16 pedidos, cobertura prospectiva ~1,9 dias — vira crítico imediato se MLB3288536143 pausar; verificar amanhã se reposição entrou ou se cobertura caiu abaixo de 1 dia
- ADS: spend R$ 422,53, revenue R$ 4.245,82, ROAS 10,05x, ACOS 8,69%, fatia 51,4% do Faturamento — piso da série de 10 ciclos (49,5%-69,9%) em dia de pico, sugere componente orgânico relevante no crescimento; ADS não escalou proporcionalmente ao volume; gatilho L02 (ACOS > 10% com fatia > 60% por dois ciclos) segue não atingido
- MercadoLíder Platinum: gap R$ 19.876,77, progresso 93,28%, ETA 4,3 dias ao ritmo R$ 4.602/dia — Faturamento do dia (R$ 8.267,83) 79,7% acima do pace; promoção ao alcance de uma semana mas diretamente vulnerável a qualquer cancelamento automático nos dois Full em cobertura curta
- 6 cancelamentos no dia é o maior valor da série recente (25/05: 3, 26/05: 3, 30/05: 2, 31/05: 6); candidato natural de até 4 é a Tulipa pausada, os 2 restantes sem fonte identificável no pacote — relevante se cancellations_rate sair de zero
- Ticket R$ 43,75 está 13,4% abaixo do avg_7d (R$ 50,49) e 8,8% abaixo do avg_30d, mas vs 60d segue positivo (+5,9%) — efeito de composição do cluster IMB501 (menor valor unitário) carregando 64% do volume, não compressão estrutural; registrar pra evitar leitura falsa em ciclos futuros
- Pendências estruturais recorrentes do pacote ML (desde 22/05): (1) breakdown ADS spend/revenue por platform_item_id; (2) lista granular de cancelamentos com order_id↔platform_item_id↔motivo; (3) série temporal de nível de qualidade por anúncio; (4) estoque em trânsito ao CD do ML / ETA de reposição Full; (5) ritmo 7d por platform_item_id; (6) available_quantity por variação dentro de anúncios multi-variação

### Dia analisado: 2026-05-30
_ingestido em 2026-05-31T07:13:05-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 2_

**Memória para o próximo ciclo (da L05):**
- Cluster IMB501 (MLB3288536143, Full) atingiu 54,6% do dia (47 Tampa Preta + 15 Tampa Cinza + 9 Tampa Vermelha = 71 pedidos / 75 unidades) com available_quantity=149 pós-baixa — cobertura ~2 dias ao ritmo do sábado, ~3,5-4 dias ao ritmo médio de 7d; verificar amanhã se reposição entrou ou se available_quantity caiu abaixo de 80.
- Conjunto Kit 6 Potes Vidro Hermético (MLB6437847224, Catálogo Full, health=null por baixo volume) com available_quantity=7 pós-baixa de 3 pedidos — cobertura ~2,3 dias; confirmar amanhã se reposição entrou, se available_quantity caiu abaixo de 3 ou se status=paused.
- Oitavo ciclo idêntico do nível de qualidade do Jogo Potes De Vidro 5 Peças Claro (0,71) e do Kit 4 Potes De Vidro Hermético 1050ml Tampa Azul-petróleo (0,75) — direção interna não observável; nono ciclo com queda de qualquer um abaixo de 0,70 aciona gatilho de alinhamento com Himmel.
- ADS: spend R$307,04, revenue R$3.381,57, ROAS 11,01x, ACOS 8,23%, fatia 59,5% do Faturamento — terceiro ponto da série pós-baseline (4,4 → 10,96 → 8,23), não monotônica; gatilho L02 é ACOS > 10% com fatia > 60% por dois ciclos consecutivos.
- Restock do Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml (MLB6232315532, Catálogo gold_pro Full) confirmado: 31 → 61 unidades entre 26/05 e 30/05 — risco de Buy Box suspenso nos próximos ciclos curtos.
- 2 cancelamentos no terceiro ciclo não-zero disponível (25/05: 3, 26/05: 3, 30/05: 2), nenhum top anúncio paused, breakdown order_id↔platform_item_id ausente — hipótese de causa comum permanece em aberto; relevante se cancellations_rate da reputação sair de zero.
- MercadoLíder Platinum: gap R$23.327,75, progresso 92,12%, ETA 5,1 dias ao ritmo R$4.544,54/dia — Faturamento do dia (R$5.678,64) acima do pace; qualquer cancelamento automático nos dois Full em cobertura crítica comprime diretamente a janela.
- Pendências estruturais recorrentes do pacote ML (desde 22/05): (1) breakdown ADS spend/revenue por platform_item_id; (2) lista granular de cancelamentos com order_id↔platform_item_id↔motivo; (3) série temporal de nível de qualidade por anúncio; (4) estoque em trânsito ao CD do ML / ETA de reposição Full.

### Dia analisado: 2026-05-26
_ingestido em 2026-05-27T07:18:48-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Sétimo ciclo idêntico de nível de qualidade do Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, 0,71) e do Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, 0,75) — oitavo ciclo segue sendo o ponto de observação; gatilho L02 é cair abaixo de 0,68 em qualquer um dos dois.
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full ativo): 2 unidades pós-baixa de 4 pedidos do dia, sétimo ciclo de monitoramento sem reposição confirmada — verificar amanhã se anúncio segue ativo, se entrou em ruptura ou se cancelamento automático foi registrado.
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida (MLB6232315532, Catálogo gold_pro Full): primeiro ciclo na zona crítica com 31 unidades pós-baixa de 15 pedidos (cobertura prospectiva ~2,1 dias) — confirmar amanhã se reposição entrou ou se cobertura caiu abaixo de 10 unidades.
- 3 cancelamentos pelo segundo dia consecutivo, mesmo volume exato — sem breakdown order_id↔platform_item_id, origem não atribuível; monitorar se cancellations_rate da reputação sai de zero nos próximos 3-5 ciclos (sinal de fonte comum ativa).
- Cluster IMB501 (MLB3288536143, Full) em 44,8% do dia (Tampa Preta 40 + Tampa Cinza 12 + Tampa Vermelha 12 = 64 pedidos) — concentração retornou ao patamar histórico após o pico de 56,5% em 25/05 (efeito de denominador da segunda-feira de baixo volume).
- ADS carregou 60,7% do faturamento com ROAS 13,9x e ACOS 10,96% — terceiro ponto consecutivo de ACOS acima do baseline ~4,4% (22-23/05), mas ROAS muito acima do limiar de ineficiência; se próximo ciclo mantiver ACOS acima de 10% com fatia de ADS acima de 60%, vira gatilho de alinhamento Yasmin–Himmel sobre cobertura e mix de campanhas.
- MercadoLíder Gold com gap para Platinum em R$ 42.460,66, progresso 85,66%, ritmo R$ 4.225,66/dia, ETA ~10 dias — faturamento do dia (R$ 7.394) opera 75% acima do pace; fora do gatilho de Slack (gap > R$ 30k) mas qualquer cancellations_rate > 0 ou ruptura na Tulipa/Catálogo aperta a janela.
- Pendências estruturais recorrentes do pacote ML (desde 22/05): (1) breakdown ADS por platform_item_id; (2) lista granular de cancelamentos com order_id↔platform_item_id; (3) série temporal de nível de qualidade por anúncio; (4) ETA de reposição em trânsito ao CD do ML.

### Dia analisado: 2026-05-25
_ingestido em 2026-05-26T07:13:01-03:00 BRT | confiança L05: media | insights L05: 3 (0 fato, 3 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Cluster do Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, Full não-Catálogo) atingiu 56,5% do volume do dia — novo pico da série 44%→47,5%→56,5%; nível regular (0,71) no sexto ciclo idêntico, direção segue não observável; sétimo ponto é o decisivo para liberar ou não alinhamento Yasmin–Himmel sobre cobertura preventiva (gatilho L02: <0,68)
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida (MLB6232315532, Catálogo gold_pro Full): cobertura ~1,7 dias com ritmo do dia em 11 pedidos (acima dos ~6/dia histórico) — confirmar amanhã se reposição entrou ou se entrou em ruptura com perda de Buy Box
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades (MLB4676726433): pausado com estoque zero gerou 3 pedidos exatamente iguais aos 3 cancelamentos do dia — monitorar cancellations_rate nos próximos 3-5 ciclos; se subir acima de 0, confirma origem comum
- ADS respondeu por 56,7% do faturamento do dia com ACOS saltando de ~4,4% (22-23/05) para 14,15% e ROAS 7,67x — segundo ponto da nova série; próximo ciclo define ruído vs tendência de ineficiência
- Modalidade de envio: top10 do dia 79,5% Full / 20,5% Cross-Docking, coerente com 30d (74,7%/25,3%); base ativa segue assimétrica (36,7% Full / 63,3% Cross-Docking) — campeões vivem em Full, amplificando exposição a rupturas no topo
- MercadoLíder Platinum: gap R$46.615, progresso 84,25%, ETA ~11 dias ao ritmo atual de R$4.156/dia — Faturamento do dia (R$5.127) acima do pace; fora do gatilho de Slack (gap >R$30k), mas qualquer movimento adverso em cancellations_rate aperta a janela
- Pendências de pacote recorrentes para próximos ciclos: (1) série temporal de nível de qualidade por anúncio; (2) breakdown ADS spend/revenue por platform_item_id; (3) lista granular de cancelamentos com order_id↔platform_item_id↔mecanismo; (4) reposição em trânsito ao CD do ML por anúncio Full
- Ticket do dia R$47,48 está acima de 30d (+3,4%) e 60d (+10,8%), mas 11,8% abaixo do avg_7d — compressão intra-semana por composição de segunda-feira dominada pelo cluster IMB501 de menor valor médio, não deterioração estrutural

### Dia analisado: 2026-05-24
_ingestido em 2026-05-25T09:24:01-03:00 BRT | confiança L05: media | insights L05: 3 (0 fato, 3 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Quinto ciclo do nível de qualidade do Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, hoje 0,71) e do Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, hoje 0,75) — ponto definidor da erosão orgânica.
- ADS share — se 25/05 fechar acima de 65% com nível dos campeões estagnado, aciona alinhamento Yasmin–Himmel sobre cobertura preventiva (segundo ponto consecutivo).
- Status pós-decisão do Kit 6 Canecas Porcelana 250ml Canelada Colorida (MLB6582645908): se pausado, registrar como variável confundidora para cancellations_rate; se ativo, monitorar cancelamentos automáticos.
- Estoque e ETA de reposição Full do Kit De 6 Canecas De Porcelana Lisa Reta 200 Ml (MLB6232315532) — confirmar se reposição entrou ou se cobertura caiu abaixo de 2 dias.
- Kit 6 Canecas Porcelana Tulipa (MLB6167272090) ausente pelo segundo ciclo — confirmar amanhã se está ativo, pausado ou esgotado.
- Cluster IMB501 atingiu 47,5% do volume do dia (vs 44% nos dois ciclos anteriores) — concentração crescente; observar se sustenta ou recua.
- Possível migração operacional do IMB501P de Cross-Docking (memória 22/05) para Full (snapshot 24/05) — confirmar se sustenta no próximo ciclo; muda leitura do mix de modalidade de envio.
- MercadoLíder Platinum: gap R$48.941, progresso 83,47%, ETA ~12 dias ao ritmo atual — fora do gatilho de Slack (gap > R$30k), mas qualquer ruptura confirmada no cluster de canecas com cancelamentos automáticos aperta a janela rapidamente.

### Dia analisado: 2026-05-23
_ingestido em 2026-05-24T07:10:47-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit 6 Canecas Porcelana Tulipa 250ml (MLB6167272090, Full, não-Catálogo): snapshot 24/05 09:50 UTC com 2 unidades pós-baixa de 9 pedidos, anúncio ativo, ritmo de 6-9 pedidos/dia em dois ciclos consecutivos — checar status, estoque e reposição em trânsito amanhã; se reposição não chegou, registrar como ruptura ativa e impacto em cancellations_rate.
- Conjunto 5 Potes de Vidro (MLB3288536143): nível de qualidade em 0,71 há três ciclos idênticos, available_quantity=469, cluster IMB501 (Tampa Preta+Vermelha+Cinza no mesmo anúncio) fez 40 pedidos = 44% do dia — quarta leitura define direção do nível.
- Kit 4 Potes 1050ml Tampa Azul-petróleo (MLB4073003575, Full): nível de qualidade em 0,75 há três ciclos, available_quantity=139, 11 pedidos — segunda métrica que precisa de quarta leitura para definir direção.
- Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo Full gold_pro): available_quantity=33 pós-baixa de 6 pedidos, cobertura estimada ~5,5 dias ao ritmo do dia — zona de atenção no horizonte de 5 dias por ser Catálogo (Buy Box demora a se recuperar).
- ADS share do dia em 49,5% (R$2.538,63 / R$5.124,32), ROAS ~9x, ACOS 4,43% — segundo ponto da nova série pós-22/05; ≤ 55% no próximo ciclo confirma orgânico em expansão, ≥ 65% reativa gatilho de escalonamento a Kobe no terceiro ciclo.
- MercadoLíder Platinum: gap R$51.794,49, progresso 82,5%, ritmo R$4.070/dia, ETA ~12,7 dias — GMV do dia acima do pace; qualquer cancelamento automático no Kit 6 Canecas Tulipa entra direto nessa janela apertada.
- ratings_negative=0,39 (39%) idêntico ao ciclo 22/05, claims_rate=0,0025 (metade do threshold 0,005), cancellations_rate=0 — vira relevante se claims_rate ultrapassar 0,005 ou se breakdown por anúncio chegar e concentrar negativos nos dois Full em Padrão inferior.
- Pendências de dado para o próximo pacote (consolidado): (1) breakdown de revenue_ads_yesterday_brl e spend_yesterday_brl por platform_item_id; (2) ritmo 7d por platform_item_id; (3) drivers de nível de qualidade por anúncio; (4) reposição em trânsito ao CD do ML por anúncio.

### Dia analisado: 2026-05-22
_ingestido em 2026-05-23T21:19:34-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full): consumo confirmado em ~6 pedidos/dia em 2 ciclos consecutivos, estoque 7→2; se próximo pacote mostrar anúncio pausado ou cancelamento automático, vira variável confundidora para reputação, ETA Platinum e leitura do cluster de canecas
- Nível de qualidade dos dois Full em Padrão inferior — Kit 4 Potes 1050ml Tampa Azul-petróleo (MLB4073003575, 0,75) e Jogo Potes 5 Peças Tampa Vermelha (MLB3288536143, 0,71) — segundo ponto idêntico entre ciclos, mas ML não expõe série interna; só o terceiro ponto define direção e desbloqueia ação com Himmel
- ADS share 69,9%, ROAS 10,87x, ACOS 4,57%, gasto R$296,96 — segundo ponto consecutivo acima de 65%; terceiro ciclo é o gatilho de escalonamento a Kobe sobre dependência estrutural
- Breakdown de revenue_ads_yesterday_brl por platform_item_id segue pendente desde 22/05 — sem ele, não dá pra confirmar se ADS prioriza os dois Full em Padrão inferior ou as variações Cross-Docking líderes do dia (registrar como dado necessário do próximo pacote)
- Cluster IMB501 sustentou 44% do dia (37 pedidos): Tampa Preta Cross-Docking 20, Tampa Vermelha Full 10, Tampa Cinza Cross-Docking 7; tratar como bloco ajuda a explicar a inversão do mix sem fragmentar; estoque robusto nas variações Cross-Docking (8.375 e 9.195 unidades)
- ratings_negative=0,39 (39%) idêntico ao ciclo anterior em conta verde Gold; claims_rate=0,0025 em 50% do threshold de risco (0,005); sem breakdown por anúncio, hipótese de concentração nos dois Full em Padrão inferior segue em aberto — vira relevante se claims_rate subir acima de 0,005
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 un (MLB6739241224, Cross-Docking): 6 unidades pós-baixa com 2 pedidos no dia, cobertura ~3 dias com amostra pequena; checagem preventiva sem urgência, Budamix controla reposição em Cross-Docking
- MercadoLíder Platinum: progresso 81,34%, gap R$55.226,77, ETA 13,8 dias ao ritmo atual de R$4.012,89/dia; GMV de hoje (R$4.622,03) está acima do ritmo necessário — fora do gatilho de Slack, vira relevante se gap cair abaixo de R$30k com progresso acima de 90%

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*
