<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- O dia foi sustentado por volume, não por ticket: 150 pedidos válidos (+8,5% vs `avg_30d.avg_orders=138,3` e +18,6% vs `same_weekday_avg.avg_orders=126,5`), enquanto o GMV ficou quase flat na comparação sazonal (R$6.397,92, +0,5% vs `same_weekday_avg.avg_gmv=R$6.364,26`). O mecanismo é composicional — o cluster IMB501 (MLB3288536143, Full, 77 pedidos = 51,3% do top3, variações Tampa Preta 39 + Cinza 20 + Vermelha 18) dominou o dia com ticket unitário menor (~R$42), deprimindo `ticket_medio=R$42,65` em −15,3% vs sextas anteriores (`same_weekday_avg.avg_ticket=R$50,31`) e −10,5% vs 30d (`ticket_vs_30d_pct`). Confirma operacionalmente a leitura da L01: expansão real de patamar em pedidos com compressão de ticket como consequência compositional do mix, não erosão de preço.

- O mix de modalidade de envio do top10 divergiu para cima: `fulfillment_mix_yesterday_top10.full_pct=87,9%` vs `fulfillment_mix_30d.full_pct=78,9%` (+9pp Full) e vs `fulfillment_mix_7d.full_pct=76,0%` (+11,9pp). A causa é produto-específica — MLB3288536143 (Full) carregou sozinho 77 pedidos, enquanto o único Cross-Docking com volume relevante no topo foi MLB6657404498 (Kit 4 Potes 520ml Quadrado, 7 pedidos, 12,1% do mix resolvido de 58 ordens). É a direção oposta ao padrão documentado em 07/06 e 09/06, quando campeões Cross-Docking puxaram o mix para baixo. A base ativa permanece 41,5% Full / 58,5% Cross-Docking — sem mudança estrutural; a divergência de ontem é artefato de composição do topo.

- MLB6167272090 (Kit 6 Canecas Tulipa 250ml, `status=paused`, `available_quantity=0`) gerou 5 pedidos hoje — 10º+ ciclo consecutivo do padrão documentado desde 31/05 (4, 11, 6, 12 e agora 5 pedidos/dia nas entradas da memória). Cada pedido nesse anúncio pausado converte-se em cancelamento prospectivo garantido. O dia adiciona evidência direta ao risco estrutural principal identificado pela L01 e confirma que a ação operacional demandada pela L02 não foi executada antes do fechamento do dia — anúncio permanece pausado com estoque zerado.

- MLB4073003575 (Kit 4 Potes 1050ml, Full, `health=0,75`) fechou em `available_quantity=13` pós-baixa de 7 pedidos, sem restock confirmado: memória de 11/06 registrava 19 unidades, queda líquida de 6 com 7 pedidos consumidos (consistente com consumo sem reposição, variação marginal de 1 un). Cobertura prospectiva ≈ 1,9 dias ao ritmo de 7 pedidos/dia (`avg_7d`). Terceiro ciclo consecutivo de cobertura crítica sem alívio — adiciona evidência ao sinal 2 da L01 e à ação 2 da L02.

---

### Sinais operacionais relevantes

- **Sinal:** MLB6167272090 (Kit 6 Canecas Tulipa 250ml) permaneceu `status=paused`, `available_quantity=0` com 5 pedidos gerados hoje, 10º+ ciclo consecutivo — **interpretação operacional:** série documentada acumula mínimo de 38 pedidos prospectivos (31/05: 4; 05/06: 11; 06/06: 6; 11/06: 12; 12/06: 5); com `transactions_completed=6.993`, cada ~35 cancelamentos adicionais move aproximadamente 0,5pp no `cancellations_rate`; a taxa oficial permanece em zero (`reputation.cancellations_rate=0`), mas a margem de segurança para o Platinum é estreita e não se manifesta no volume — o risco é silencioso enquanto a acumulação progride.

- **Sinal:** MLB4073003575 (Kit 4 Potes 1050ml, Full, `available_quantity=13`, `health=0,75`) completou o 3º ciclo consecutivo de cobertura crítica sem restock confirmado — **interpretação operacional:** cobertura prospectiva ≈ 1,9 dias; ruptura nesse anúncio Full ativo adiciona cancelamentos prospectivos sobre a janela Platinum e retira velocidade de ranking de categoria de um segundo vetor; a combinação com a Tulipa pausada configuraria dois Full simultâneos pressionando `cancellations_rate`, que é a cadeia de risco mais delicada identificada em múltiplos ciclos da memória.

- **Sinal:** MLB6657404498 (Kit 4 Potes Vidro 520ml Quadrado, Cross-Docking) apareceu no top10 com 7 pedidos, mas o snapshot registra `sold_quantity=6` histórico e `health=null` — **interpretação operacional:** sold_quantity acumulado de 6 indica anúncio com praticamente zero histórico pré-ontem; a entrada no top10 com 7 pedidos em um listing nesse estágio merece verificação de origem — se ADS-induzida por Himmel, pode estar distorcendo a leitura do ROAS do dia ao incluir produto sem social proof consolidado; se orgânica, sugere emergência natural que pode não se sustentar sem histórico de reputação de listing.

- **Sinal:** ADS share chegou a 42,0% (`revenue_ads_yesterday_brl=R$2.688,95` / `gmv=R$6.397,92`), menor ponto válido da série 22/05–12/06 (69,9%→42,0%), com ROAS 11,41x e ACOS 9,96%, em dia de GMV acima da média de mesmos dias da semana — **interpretação operacional:** este é o segundo ciclo válido consecutivo abaixo de 45% (09/06: 44,3%; 12/06: 42,0%), com denominadores saudáveis em ambos; confirma operacionalmente a tendência de expansão orgânica estrutural identificada pela L01 — dois pontos válidos abaixo de 45% com GMV ≥ R$6.000 estão a um ciclo de consolidar a hipótese como fato.

- **Sinal:** 3 cancelamentos do dia (2,0% sobre 150 pedidos), com `cancellations_rate=0` na janela longa e nenhum breakdown `order_id ↔ platform_item_id ↔ motivo` disponível no pacote — **interpretação operacional:** volume modesto, mas a Tulipa pausada é candidata natural para pelo menos parte deles; sem atribuição, não é possível confirmar se cancelamentos do dia já iniciaram a entrada na janela oficial ML ou se são de outros anúncios; permanece como pendência estrutural do pacote (22º+ ciclo desde 22/05).

---

### Anomalias ou ausência de anomalia

**Anomalia leve**

Os dois desvios presentes — MLB6167272090 no 10º+ ciclo de pausa com pedidos e MLB4073003575 no 3º ciclo consecutivo de cobertura crítica — são padrões rastreados na memória desde 31/05 e 09/06, respectivamente, sem agravamento agudo novo hoje. O dia operou dentro das bandas de 30d em volume e GMV, reputação permanece 5_green platinum, `cancellations_rate=0`, e nenhum campeão entrou em ruptura por evento novo. O nível sobe para **anomalia moderada** se no próximo snapshot MLB6167272090 seguir `paused` (11º ciclo de acumulação) e MLB4073003575 cruzar para `available_quantity ≤ 6` ou `status=paused` — dois vetores Full simultâneos sobre `cancellations_rate` numa janela Platinum recém-conquistada. O nível desce para **sem anomalia relevante** se Yasmin confirmar restock em trânsito para ambos com ETA dentro das próximas 24h.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual o `status` e `available_quantity` atuais de MLB6167272090 (Tulipa 250ml), e há ETA de restock confirmado para o CD do ML? — **motivada por:** 10º+ ciclo de pausa com pedidos prospectivos; a resposta desta pergunta define se o `cancellations_rate` Platinum tem margem de segurança ou está já dentro da janela de risco.

- **Pergunta:** MLB4073003575 (Kit 4 Potes 1050ml) — `available_quantity` atual e algum lote em trânsito confirmado ao CD do ML? — **motivada por:** 3 ciclos consecutivos de cobertura crítica sem restock confirmado; com 13 unidades e ritmo de 7/dia, qualquer pedido acima de 13 a partir de agora dispara cancelamento automático.

- **Pergunta:** MLB6657404498 (Kit 4 Potes 520ml Quadrado, Cross-Docking, `sold_quantity=6`) — é anúncio recém-criado ou reativado? O volume de ontem (7 pedidos) foi ADS-induzido ou orgânico? — **motivada por:** sold_quantity histórico de 6 com 7 pedidos em um único dia indica listing de zero histórico emergindo no topo; origem do volume é necessária para interpretar se o ADS share do dia inclui produto sem base de reputação de listing.

- **Pergunta:** Dos 3 cancelamentos do dia, qual é o `platform_item_id` e motivo de cada um? — **motivada por:** sem atribuição não é possível estimar quanto da acumulação prospectiva da Tulipa já entrou na janela oficial do ML nem separar cancelamentos do anúncio pausado de cancelamentos com outras origens.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia é que MLB6167272090 (Tulipa 250ml) completou o 10º+ ciclo consecutivo `paused` com `available_quantity=0` gerando mais 5 pedidos prospectivamente cancelados — sem resolução operacional visível no pacote. A série documentada acumula no mínimo 38 pedidos prospectivos; com `transactions_completed=6.993` e threshold Platinum em `cancellations_rate ≤ 0,5%`, a margem de segurança é matematicamente estreita e completamente invisível no GMV e no volume do dia. A L01 identificou este como o único vetor capaz de derrubar o Platinum recém-conquistado sem sinalização prévia no faturamento; a L02 demandou ação de Yasmin hoje; o dia de 12/06 confirma que o ciclo continuou sem resolução. Não há fato operacional novo que altere a tese — mas há confirmação de que o risco silencioso progride enquanto a conta apresenta números saudáveis. A Condensadora deve avaliar se o Slack carrega esse risco de forma explícita ou se é informação interna de ciclo — a resposta muda dependendo de se Yasmin reportou providência ou silêncio.