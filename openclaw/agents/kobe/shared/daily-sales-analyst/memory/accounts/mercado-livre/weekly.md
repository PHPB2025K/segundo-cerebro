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
