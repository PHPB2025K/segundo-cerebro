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

### Dia analisado: 2026-06-12
_ingestido em 2026-06-13T07:16:11-03:00 BRT | confiança L05: alta | insights L05: 3 (2 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- MercadoLíder Platinum confirmado em 12/06 (sales_60d R$ 321.406, R$ 25.406 acima do threshold, power_seller_status=platinum) — vocabulário muda: não é mais ETA Platinum, é manutenção sob pressão de cancellations_rate; ritmo necessário pra manter ~R$ 4.933/dia, dia de hoje 30% acima
- Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full, sem nível de qualidade calculado pelo ML): 10º+ ciclo seguido paused com available_quantity=0; mais 5 pedidos no dia; acumulado mínimo da série 38 pedidos prospectivamente cancelados — confirmar amanhã status, available_quantity e se restock entrou; ratings_negative=0,41 segue como vetor latente paralelo
- Kit 4 Potes 1050ml Azul-petróleo (MLB4073003575, Full, gold_pro, em nível regular 0,75): available_quantity caiu de 19 pra 13 em 24h, 3º ciclo seguido de cobertura crítica (~1,9 dias) — confirmar amanhã se restock entrou (estoque > 20) ou se cruzou abaixo de 6
- Cluster IMB501 (MLB3288536143, em nível regular 0,71 no 18º+ ciclo idêntico, Full, gold_special, is_catalog=false): carregou 51,3% do top3 (Tampa Preta 39 + Cinza 20 + Vermelha 18); estoque 1.563 un descarta ruptura; risco é erosão lenta de ranking de categoria, não evento agudo; gatilho de alinhamento Himmel segue sendo cruzar abaixo de 0,68
- Fatia do ADS no faturamento foi de 42,0% (R$ 2.688,95 / R$ 6.397,92) com ROAS 11,41x e ACOS 9,96% — 2º ponto válido consecutivo ≤ 45% após 09/06 (44,3%); um terceiro ciclo abaixo de 45% com GMV ≥ R$ 6 mil consolida hipótese de autonomia orgânica como fato; ponto 11/06 segue suspenso por lag de API
- Mix de modalidade de envio do top10 12/06 em Full 87,9% / Cross-Docking 12,1% é artefato de composição produto-específica (cluster IMB501 Full carregou o topo, Cross-Docking quase ausente); base ativa account_overview permanece 41,5% Full / 58,5% Cross-Docking — registrar como ponto-zero pra detectar inversão amanhã
- Kit 4 Potes 520ml Quadrado (MLB6657404498, Cross-Docking, sem nível calculado): apareceu no top10 com 7 pedidos sobre sold_quantity histórico de 6 — listing efetivamente sem histórico pré-12/06; pendência identificar se é criação/reativação e se foi ADS-induzido; pode estar distorcendo a leitura do ADS share do dia
- Pendências estruturais persistentes do pacote ML (22º+ ciclo desde 22/05): breakdown ADS spend/revenue por platform_item_id; lista granular cancelamentos order_id↔platform_item_id↔motivo↔mecanismo; ETA reposição em trânsito ao CD do ML por anúncio; série temporal interna de nível de qualidade por anúncio; data_created/last_updated por listing

### Dia analisado: 2026-06-11
_ingestido em 2026-06-12T07:15:19-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida (MLB6232315532, Catálogo Premium gold_pro Full, sem nível de qualidade calculado pelo ML): fechou 11/06 com available_quantity=4 após 5 pedidos, 4º ciclo monotonicamente descendente (35→28→11→5→4) sem restock confirmado — confirmar amanhã status (active/paused), available_quantity e se ETA de reposição no CD do ML entrou
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara (MLB6167272090, Full, sem nível calculado): available_quantity=5 após 12 pedidos/16 itens, runway abaixo de 0,5 dia, 9º+ ciclo de cobertura crítica desde 31/05 — confirmar status, available_quantity e se restock entrou
- Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, gold_pro Full, em nível regular 0,75): available_quantity=19 após 7 pedidos (-9 líquidas em 24h sem restock), 3º ciclo consecutivo de cobertura curta — confirmar se restock entrou ou se runway cruzou abaixo de 12 unidades
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, gold_special Full, em nível regular 0,71 no 18º+ ciclo idêntico): carregou 63,2% do dia em 117 pedidos (IMB501P 66 Tampa Preta + IMB501V 27 Tampa Vermelha + IMB501C 24 Tampa Cinza), estoque confortável 1.523 un (~12 dias); risco é estrutural (concentração), não operacional no líder
- Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo (MLB5402326666, gold_special Full, Clássico, em nível preocupante 0,66): 6º+ ciclo idêntico, available_quantity=37 (~5 dias) — risco é exposição orgânica em ranking de categoria; gatilho de alinhamento com Himmel segue sendo cair abaixo de 0,63 em dois ciclos
- ADS Mercado Ads do dia 11/06 inutilizável (spend_yesterday_brl=0,0 com campaigns_active_count=13) — provável lag de API; tese de ADS share descendente (série 69,9%→44,3% desde 22/05) fica suspensa até próximo ciclo com dado válido; verificar amanhã se valor retornou
- Mix de modalidade de envio do top10 em 100% Full vs 78,9% em 30d e 75% em 7d — divergência produto-específica (apenas listagem Full do IMB501 carregou o cluster, ausência das Cross-Docking do cluster no topo sem causa atribuível pelo pacote); base ativa segue 41,5% Full / 58,5% Cross-Docking — registrar como ponto a observar se padrão se repete
- Pendências estruturais persistentes do pacote ML (21º+ ciclo desde 22/05): breakdown ADS spend/revenue por platform_item_id; lista granular cancelamentos order_id↔platform_item_id↔motivo; ETA de reposição em trânsito ao CD do ML por anúncio; série temporal interna de nível de qualidade por anúncio; ranking de categoria/Buy Box por listagem

### Dia analisado: 2026-06-10
_ingestido em 2026-06-11T07:14:14-03:00 BRT | confiança L05: alta | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- MLB6232315532 (Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida, Catálogo Premium gold_pro, Full, sem nível de qualidade calculado pelo ML): fechou 10/06 com available_quantity=5 após 7 pedidos, runway ≤0,7 dia, padrão de depleção desde 26/05 (35→28→11→restock→5) — confirmar amanhã status (active/paused), available_quantity e se ETA de reposição entrou
- MLB4741367603 (Kit 6 Canecas Tulipa Coloridas De Porcelana Para Café E Chá 250ml Colorida, Catálogo Clássico, Full, sem nível calculado): available_quantity=14 após 5 pedidos, runway ~2,8 dias — confirmar status e cobertura
- MLB3918271667 (2 Potes Vidro Marmita Tampa Hermética 4 Travas Vedação 800ml Verde, Catálogo Clássico, Full, sem nível calculado): available_quantity=12 após 4 pedidos, runway ~3,0 dias — confirmar status e cobertura; configuração inédita de três Catálogos Full em janela crítica de 72h é o ponto zero da série
- MLB4073003575 (Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo, Full, nível regular 0,75): manteve 28 un após 12 pedidos (restock parcial inferido ~12 un), runway ~2,3 dias — confirmar se restock continuou ou se cobertura caiu abaixo de 15
- MLB5402326666 (Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo, Clássico Full, nível preocupante 0,66): 6º ciclo idêntico, estoque 43 un / ~6 dias — risco é exposição orgânica em ranking; gatilho de alinhamento com Himmel é cair abaixo de 0,63
- Fatia do ADS no faturamento foi de 59,7% (R$ 4.813,22 / R$ 8.063,87) com ROAS 11,67x e ACOS 12,12%, gasto R$ 412,15 (+57% vs 09/06) — 1º ponto acima de 55% em dia de denominador forte suspende a série descendente 22/05–09/06 (69,9%→44,3%); próximos 2 ciclos definem se foi desvio pontual ou reversão da hipótese de autonomia orgânica
- 8 cancelamentos no dia (4,3% sobre 185) é o nível mais alto da série recente; cancellations_rate oficial permanece em zero (janela longa); nenhum top10 em status=paused no snapshot reduz chance de atribuição direta a ruptura, mas combinação com três Catálogos Full em runway crítico é a cadeia de risco mais delicada da Platinum
- Pendências estruturais persistentes do pacote ML (20º+ ciclo desde 22/05): breakdown ADS spend/revenue por platform_item_id; lista granular cancelamentos order_id↔platform_item_id↔motivo; ETA de reposição em trânsito ao CD do ML; série temporal interna de nível de qualidade por anúncio; continuidade entre MLB6073033006 (memória 08-09/06) e MLB6438497744 (top10 10/06) na família Canequinhas 100ml Madeira

### Dia analisado: 2026-06-09
_ingestido em 2026-06-10T07:24:51-03:00 BRT | confiança L05: media | insights L05: 3 (2 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- MLB4073003575 (Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo, Full, nível regular 0,75): caiu 33→28 un entre 08/06 e 09/06, ritmo acelerou 15→20 ped/dia, runway ~1,4 dia — confirmar amanhã se restock entrou, se status virou paused ou se cobertura caiu abaixo de 15
- MLB6073033006 (Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico, Full, sem nível de qualidade calculado pelo ML, mapping_confidence=medium): caiu 19→11 un entre 08/06 e 09/06, runway ~1,4 dia, segundo ciclo consecutivo no limiar crítico — confirmar amanhã status, available_quantity e se Budamix conseguiu acionar reposição
- MLB3288536143 (Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita, IMB501P/V, Full, nível regular 0,71 no 18º+ ciclo idêntico): restock confirmado entre 08/06 (1.056) e 09/06 (1.407) absorvendo o consumo do dia; listing carrega sozinha 41,7% do volume — qualquer pausa, ruptura ou queda de nível atinge ~40% da conta
- MLB5402326666 (Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo, Full, Clássico, nível preocupante 0,66): 6º ciclo idêntico, available_quantity=51, runway ~8,5 dias — risco é exposição orgânica em ranking de categoria, não cobertura; gatilho de alinhamento com Himmel é cair abaixo de 0,63 em dois ciclos
- Mix de modalidade de envio do top10 (Full 75,3% / Cross-Docking 24,7%) divergiu -4,5pp vs 30d (79,8%) integralmente por dois Cross-Docking no topo: MLB4535865311 Tampa Cinza (15 pedidos) e MLB4676131007 Kit 10 Potes 520ml (7 pedidos) — não é reversão estrutural, é composição produto-específica; Flex segue em 0% (desligado por decisão operacional, sem anomalia)
- Fatia do ADS no faturamento foi de 44,3% (R$ 3.644,88 / R$ 8.220,56) com ROAS 14,9x e ACOS 6,31% — 9º ponto descendente consecutivo desde 22/05 (69,9%→44,3%), 3º ciclo abaixo de 50%; próximo limiar analítico é cruzar abaixo de 40%, que consolidaria autonomia orgânica estrutural do canal
- 6 cancelamentos no dia (3,6% sobre 168), nenhum top10 em status=paused, cancellations_rate oficial permanece em zero — padrão recorrente 3-6/dia há múltiplos ciclos sem atribuição possível pelo pacote; relevante pois convive agora com dois Full em runway crítico que adicionariam cancelamentos prospectivos se pausarem
- Pendências estruturais persistentes do pacote ML (19º+ ciclo desde 22/05): série temporal interna de nível de qualidade por anúncio; breakdown ADS spend/revenue por platform_item_id; lista granular cancelamentos order_id↔platform_item_id↔motivo; ETA de reposição em trânsito ao CD do ML por anúncio

### Dia analisado: 2026-06-08
_ingestido em 2026-06-09T07:24:52-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Mercado Líder Platinum confirmado em 08/06 com sales_60d R$ 301.153 (threshold R$ 296.000), gap=0, progress=100%, power_seller_status=platinum — eixo muda de conquistar para manter; ritmo necessário R$ 5.019/dia, faturamento do dia 76% acima — risco imediato é cancellations_rate sair de zero por ruptura automática, não volume
- Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico (MLB6073033006, 914C_BA, Full, sem nível de qualidade calculado pelo ML) — 19 unidades pós-baixa, runway efetivo ~1,1 dia ao ritmo de unidades (vende 1,55 un/pedido); primeira aparição em zona crítica, mapping_confidence=medium mas title e raw_title convergem, slack_short_name=null — confirmar amanhã se restock entrou, se status virou paused ou se available_quantity caiu abaixo de 8
- Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo (MLB4073003575, KIT4YW1050, Full, nível regular 0,75) — 33 unidades pós-baixa de 15 pedidos, runway ~2,1 dias; padrão recorrente desde 02/06 (chegou a 2 un naquele ciclo); restock entre 07/06 e 08/06 insuficiente pro ritmo do novo patamar — confirmar amanhã se reposição entrou ou se cobertura caiu abaixo de 15
- Restock do Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, IMB501C/V, Full) confirmado: 2 → 1.056 unidades; nível regular 0,71 persiste há 17+ ciclos; mix de modalidade de envio do top10 voltou ao padrão (Full 78,5% vs 30d 79,6%, -1,1pp) — restauração estrutural, não compensação emergencial
- Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo (MLB5402326666, KIT4YW640, Full, Clássico, nível preocupante 0,66) — 5º ciclo idêntico, estoque confortável (58 un, ~3,6 dias); direção não observável pelo pacote; gatilho de alinhamento com Himmel é cair abaixo de 0,63
- ADS share 47,1% (R$ 4.169 / R$ 8.850), ROAS 9,70x, ACOS 11,67% — 7º ponto da série descendente desde 22/05 (69,9% → 47,1%), 2º ciclo consecutivo abaixo de 50%, 1º ciclo com ACOS acima de 10% mas dentro do envelope eficiente; próximo dia útil define se hipótese de expansão orgânica vira fato consolidado
- 6 cancelamentos no dia (3,0% sobre 201) sem atribuição possível por platform_item_id ↔ motivo; nenhum top10 paused no snapshot reduz chance de ruptura automática nos top10 mas não elimina cenário fora do topo; cancellations_rate oficial permanece em zero (janela longa, não substituível pela métrica do dia)
- Pendências estruturais do pacote ML (18º ciclo consecutivo desde 22/05): breakdown ADS spend/revenue por platform_item_id; série temporal interna de nível de qualidade por anúncio + drivers; lista granular cancelamentos order_id ↔ platform_item_id ↔ motivo ↔ mecanismo; ETA de reposição em trânsito ao CD do ML por anúncio; hour_distribution por platform_item_id (pico de 21h sozinha = 19,4% do dia sem causa atribuível)

### Dia analisado: 2026-06-07
_ingestido em 2026-06-08T07:15:16-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, IMB501V, Full, nível regular 0,71) voltou ativo no snapshot 08/06 com available_quantity=2 após 10 pedidos no dia — restock estimado em ~12 unidades; confirmar amanhã se anúncio voltou a paused, se cobertura caiu abaixo de 5 ou se chegou novo lote
- Cluster IMB501 empatou em 10/10/10 pedidos = 35,7% do dia entre Tampa Vermelha (Full, supply residual), Tampa Cinza (MLB4535849169, Cross-Docking, 86 un) e Tampa Preta (MLB4535865317, Cross-Docking, 8.275 un) — comunicar como bloco perde a diferença material; apenas a variante Full está em risco
- Mix Full do dia 67,2% caiu -12,9pp vs 30d (80,1%) por efeito produto-específico do supply depletado; base ativa segue 42,1% Full / 57,9% Cross-Docking — campeões vivem em Full, estreiteza do topo é a vulnerabilidade estrutural confirmada
- MercadoLíder Platinum 3º ciclo consecutivo com sales_60d R$ 298.699 vs threshold R$ 296.000, sales_60d_count_paid 6.725 vs 1.725, gap=0, progress=100%, power_seller_status ainda gold; ritmo necessário R$ 4.978/dia, GMV de 07/06 R$ 4.115 (-17,3% vs ritmo) — confirmar se medalha atualizou ou se dia de Faturamento alto saindo da janela rolling 60d compensou
- Kit 4 Potes 640ml Azul-petróleo (MLB5402326666, KIT4YW640, Full, Clássico) em nível preocupante 0,66 no 4º+ ciclo idêntico, estoque robusto (75 un, ~25 dias) — risco é exposição orgânica, não cobertura; gatilho de alinhamento com Himmel é cair abaixo de 0,63
- ADS no 2º ciclo consecutivo acima de 60% (64,2% do Faturamento, R$ 2.642 / R$ 4.115, ROAS 8,78x, ACOS 9,01%) — mecanismo é denominador comprimido pelo supply depletado, não escalada de campanha; gatilho de alinhamento com Himmel (ACOS > 30% ou nível de campeão Full < 0,63) segue distante
- Único anúncio Catálogo no top 10 é 2 Potes Vidro Marmita Tampa Hermética 4 Travas Vedação 800ml Verde (MLB3918271667, Full, sem nível de qualidade calculado pelo ML, available_quantity=23, cobertura ~7-8 dias no ritmo do domingo) — sem urgência hoje, observar em dias úteis pois ruptura derrubaria Buy Box
- Pendências estruturais do pacote ML (17º ciclo consecutivo desde 22/05): breakdown ADS spend/revenue por platform_item_id; série temporal de nível de qualidade por anúncio + drivers; lista granular cancelamentos order_id↔platform_item_id↔motivo↔mecanismo; ETA de reposição em trânsito ao CD do ML; available_quantity por variação em anúncios multi-variação

### Dia analisado: 2026-06-06
_ingestido em 2026-06-07T07:14:58-03:00 BRT | confiança L05: media | insights L05: 3 (2 fato, 1 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- Anúncio líder Full Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (MLB3288536143, IMB501V, nível regular 0,71, paused, available_quantity=0) — 67 pedidos prospectivamente canceláveis; confirmar amanhã se cancellations_rate saiu de zero, se status virou active ou se segue paused
- Kit 6 Canecas Porcelana 250ml Canelada (MLB6582682928, Cross-Docking, paused, available_quantity=0): 6 pedidos prospectivos no dia, mapping_confidence=medium — monitorar status e reativação
- Kit 2 Potes Vidro 1520ml Tampa Hermético Travas Vedação Verde-escuro (MLB5322494954, Cross-Docking, paused, available_quantity=0, nível regular 0,75): 6 pedidos prospectivos — monitorar status
- Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo (MLB5402326666, Full ativo, nível preocupante 0,66): 3º ciclo idêntico estabilizado; gatilho de alinhamento com Himmel é cair abaixo de 0,63
- MercadoLíder Platinum: 2º ciclo consecutivo com sales_60d_revenue R$ 298.736 vs threshold R$ 296.000, gap=0, progress=100%, sales_60d_count_paid=6.743 vs threshold 1.725, mas power_seller_status ainda gold; ratings_negative=0,41 (vs ratings_positive=0,56) é hipótese de bloqueio silencioso — confirmar no próximo snapshot se medalha atualizou ou se dia de Faturamento alto saindo da janela rolling 60d compensou a entrada
- Mix de modalidade de envio do dia (Full 72,8% top10) é artefato contábil — Full válido pós-cancelamento estimado em ~41,4%, alinhado com base ativa (Full 41,3%) e -39pp vs 30d (Full 80,8%); registrar como ponto zero da série para comparação no próximo ciclo
- Cauda Full ativa entregou 24 pedidos somados (MLB4931700052 6 + MLB5402326666 6 + MLB4076957145 4 + MLB4073064873 4 + MLB6518176572 4) — capacidade de substituição ~36% do volume do líder pausado; observar amanhã se essa razão melhora ou piora com o líder ainda fora
- Pendências estruturais do pacote ML (16º ciclo consecutivo desde 22/05): breakdown ADS spend/revenue por platform_item_id; série temporal de nível de qualidade por anúncio + drivers; lista granular cancelamentos order_id↔platform_item_id↔motivo↔mecanismo (vendedor/comprador); ETA de reposição em trânsito ao CD do ML; available_quantity por variação em anúncios multi-variação

### Dia analisado: 2026-06-05
_ingestido em 2026-06-06T07:06:51-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- MercadoLíder: gap_revenue_brl=0, progress_pct=100%, sales_60d_revenue_brl R$ 296.060 vs threshold R$ 296.000, sales_60d_count_paid 6.683 vs threshold 1.725 — 1º ciclo com critério financeiro cruzado e power_seller_status ainda gold; confirmar no próximo snapshot se medalha atualizou ou se Faturamento alto saindo da janela rolling 60d compensou a entrada do dia
- Jogo Potes Vidro 5 Peças Tampa Cinza (MLB3288536143, IMB501C, Full): 42 pedidos = 25,6% do dia, available_quantity=58 pós-baixa, ~16º ciclo em nível regular (0,71) idêntico — checar amanhã se reposição entrou, se cobertura caiu abaixo de 30 ou se status virou paused
- Kit 6 Canecas Porcelana Tulipa 250ml (MLB6167272090, Full, paused, available_quantity=0): 11 pedidos no dia, 8º+ ciclo do padrão de ruptura prospectiva — monitorar cancellations_rate nos próximos 1-3 snapshots; sair de zero confirma entrada da série acumulada na janela oficial ML
- Kit 4 Potes 640ml Tampa Azul-petróleo (MLB5402326666, Clássico Full): nível preocupante (0,66) no 2º ciclo abaixo do threshold 0,85, estoque confortável (~17 dias de cobertura) — risco é exposição orgânica em ranking de categoria; 3º ciclo decide recorrente vs pontual
- Cluster IMB501 em 48,2% do dia (3º produto a 3º produto): IMB501C 42 pedidos Full no MLB3288536143 + IMB501V 20 pedidos Cross-Docking no MLB4535659243 + IMB501P 17 pedidos Cross-Docking no MLB4535865317; divergência -18,2pp Full vs 30d é integralmente produto-específica, não estrutural
- ADS: fatia de 55,1% do Faturamento (R$ 4.268,26 / R$ 7.742,32), ROAS 14,03x, ACOS 7,27%, gasto R$ 304,23 — 5º+ ciclo na faixa 48-57%; gatilho de revisão com Himmel (ACOS > 30% ou fatia > 60% por 2 ciclos) segue distante
- Reputação: color=5_green, claims_rate=0,0018 (36% do threshold 0,005), cancellations_rate=0, delayed_handling_rate=0,0009, ratings_negative estagnado em 0,41 — vetor latente se cancellations_rate sair de zero antes do reconhecimento formal Platinum
- Pendências estruturais do pacote ML (15º ciclo consecutivo desde 22/05): breakdown ADS spend/revenue por platform_item_id; série temporal de nível de qualidade por anúncio + drivers; lista granular de cancelamentos order_id↔platform_item_id↔motivo; ETA de reposição em trânsito ao CD do ML; available_quantity por variação em anúncios multi-variação

### Dia analisado: 2026-06-04
_ingestido em 2026-06-05T11:44:52-03:00 BRT | confiança L05: media | insights L05: 3 (1 fato, 2 hipótese/risco latente) | prioridades L05: 3_

**Memória para o próximo ciclo (da L05):**
- MercadoLíder Platinum — gap R$ 3.810, progresso 98,71%, ETA estimado 0,8 dias ao ritmo R$ 4.870/dia, Faturamento de hoje R$ 8.648 (1,78x o pace); confirmar no próximo snapshot se medalha_atual virou platinum ou se dia de alto Faturamento saindo da janela rolling 60d compensou a entrada do dia 04/06
- Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo gold_pro Full): 11 unidades pós-baixa de 16 pedidos, trajetória monotonicamente decrescente em 3 ciclos (35→28→11 entre 26/05 e 04/06) sem evidência de restock — único Catálogo gold_pro do topo; ruptura derruba Buy Box em Catálogo
- Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full): 5 unidades pós-baixa de 18 pedidos, 7º ciclo do padrão de ruptura recorrente; runway prospectivo ~7h ao ritmo do dia
- Kit 4 Potes 640ml Tampa Azul-petróleo (MLB5402326666, Full): em nível preocupante 0,66 no 2º ciclo abaixo do threshold 0,85; 4 pedidos no dia coerente com perda de exposição orgânica — 3º ciclo decide recorrente vs pontual
- Cluster IMB501 em 49,7% do dia (14º ciclo de concentração no mesmo patamar): IMB501C 41 + IMB501V 28 em Full no MLB3288536143 (nível regular 0,71 idêntico há 13 ciclos, available_quantity=88 pós-baixa de 69 pedidos, runway prospectivo ~1,3 dias) + IMB501P 20 em Cross-Docking no MLB4535865317 (estoque robusto 8.310); a divergência -13pp Full vs 30d é integralmente produto-específica, não estrutural
- ADS: fatia de 56,5% do Faturamento (R$ 4.886,83 / R$ 8.647,61), ROAS 14,27x, ACOS 10,64% — estável na faixa 50-57% pelos últimos 5 ciclos; gatilho de revisão com Himmel (ACOS > 30% ou fatia > 60% por 2 ciclos) segue distante
- ratings_negative 0,41 estagnado, claims_rate 0,0017 (34% do threshold 0,005), cancellations_rate oficial em zero apesar dos 4 cancelamentos do dia (2,2% sobre 179 pedidos) — divergência semântica esperada entre janela curta e janela longa ML; vetor latente se entrar na janela oficial antes do threshold Platinum
- Pendências estruturais do pacote ML (14º ciclo consecutivo desde 22/05): breakdown ADS spend/revenue por platform_item_id; série temporal de nível de qualidade por anúncio + drivers; lista granular de cancelamentos order_id↔platform_item_id↔motivo; ETA de reposição em trânsito ao CD do ML; available_quantity por variação em anúncios multi-variação

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

---

*Histórico semanal abaixo. Não sobrescrever — adicionar nova entrada acima.*
