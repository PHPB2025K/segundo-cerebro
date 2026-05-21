<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Risco operacional imediato, não tático.** A L01 identificou ruptura prospectiva no Kit 06 Canequinhas Acrílico (`MLB4410218897`, `available_quantity=3` após 3 pedidos ontem) como sinal a observar. A postura tática correta não é observar — é agir: o anúncio está ativo com estoque efetivamente zerado, e qualquer pedido gerado hoje configura cancelamento prospectivo que impacta `cancellations_rate` da reputação. Este é o único ponto que exige ação no dia, com ou sem mais dados.

- **Cobertura de Full em segundo campeão de canecas entra em janela de alerta.** A L01 apontou Kit 6 Canecas Porcelana Tulipa (`MLB6167272090`, `logistic_type=fulfillment`, `available_quantity=21`, ~5 pedidos/dia) com ~4 dias de cobertura no CD do ML. O lead time de reabastecimento Full impede reação tardia — a checagem de hoje define se há tempo hábil para providenciar reposição antes da ruptura no CD.

- **Não acionar Himmel.** A tese da L01 classifica ADS share em 59,8% com ROAS 11,6x e ACOS 4,64% como campanha eficiente em fase inaugural sem histórico narrativo. A decisão tática consequente é não introduzir variável: registrar os números de hoje como ponto zero da série e observar por 3-5 dias. Qualquer ajuste agora impede separar comportamento orgânico de efeito de campanha — e a conta não tem memória semanal/mensal populada para calibrar o risco dessa perturbação.

- **Health degradada nos campeões de Full exige checagem de direção, não de valor absoluto.** A L01 sinalizou MLB4073003575 (health=0,75) e MLB3288536143 (health=0,71) como vulnerabilidade que amplifica o risco de ADS dependência — se o orgânico erode enquanto ADS compensa, o risco não aparece no agregado. A decisão tática é checar se o health está estabilizando, caindo ou recuperando: isso define se a ação fica em observação ou escala para alinhamento com Himmel sobre cobertura preventiva.

---

### O que fazer hoje

**1. Yasmin:** verificar `available_quantity` do campeão Kit 06 Canequinhas Acrílico com suporte de madeira acrílico (anúncio ativo, 3 unidades em estoque, 3 pedidos gerados ontem) e decidir entre reposição emergencial em 24h ou pausa preventiva controlada — motivo: anúncio ativo com estoque zerado gera cancelamentos prospectivos que impactam `cancellations_rate` da reputação (`reputation.cancellations_rate=0` hoje; cada cancelamento ML compromete a série limpa) — sinal de resultado: se reposição confirmada em 24h ou pausa executada antes de novo pedido, risco neutralizado; se anúncio seguir ativo com zero estoque por mais um ciclo, registrar como variável confundidora na leitura dos próximos dias.

**2. Yasmin:** checar cobertura de estoque no CD do ML do Kit 6 Canecas Porcelana Tulipa (logistic_type Full, `available_quantity=21`, ritmo médio de 5 pedidos/dia → ~4 dias de cobertura) e confirmar se há reposição programada — motivo: ruptura em anúncio Full não pode ser corrigida em tempo real; o impacto aparece antes da reação ser possível, e este anúncio compõe os top6 por pedidos do dia — sinal de resultado: reposição programada com chegada em ≤3 dias = risco encaminhado; ausência de reposição confirmada = Yasmin alerta Trader sobre ruptura prospectiva em CD.

**3. Yasmin:** registrar direção do health dos dois campeões de potes de vidro em Full (Kit 4 Potes 1050ml com health=0,75 e Conjunto 5 Potes Tampa Vermelha com health=0,71) comparando com o valor de ontem, se disponível, ou marcando hoje como ponto zero da série de direção — motivo: a tese da L01 aponta que health degradada erode o orgânico de forma invisível no agregado porque ADS compensa; sem saber a direção (caindo/estável/recuperando), a decisão sobre acionar Himmel para cobertura preventiva não tem base — sinal de resultado: health estável ou subindo em ambos = observação por mais 2 dias sem ação; health caindo em qualquer um dos dois = Yasmin alinha com Himmel sobre cobertura preventiva antes que o orgânico perca posição com campanha mascarando o movimento.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajustar ou escalar as campanhas de Mercado Ads.** ADS share de 59,8% com ROAS 11,6x e ACOS 4,64% (`ml_snapshot.ads_summary`) configura campanha eficiente — a regra da lente tática 5 é explícita: não mexer. A memória semanal/mensal está vazia, o que significa que não há referência sobre se esse share é recente ou padrão estabelecido. Qualquer ajuste de verba, segmentação ou pausa agora introduz variável que impede distinguir efeito de campanha de comportamento orgânico — exatamente quando a conta mais precisa de dados limpos para construir a série de base.

- **Não tratar a variação negativa vs 7d como sinal de retração da conta.** O dia registrou `-20,9%` em pedidos vs `avg_7d` (91 vs 115,1), mas o mesmo dia da semana dos últimos 4 ciclos médios R$3.841 vs R$5.087 de hoje — o dia foi forte, não fraco. A leitura estratégica da L01 confirmou em duas janelas independentes (60d e mesmo dia da semana) que o patamar de GMV está acima da banda histórica. Agir em cima de desvio vs 7d sem controlar sazonalidade seria decisão baseada em métrica errada.

- **Não pausar nem redirecionar os anúncios campeões com health degradada (MLB4073003575 e MLB3288536143) sem antes confirmar a direção do health.** Health de 0,75 e 0,71 estão abaixo do limiar de 0,85, mas a postura correta depende de saber se estão caindo ou estabilizando. Pausar anúncio com health baixo mas estável remove GMV sem corrigir a causa da penalização — e ambos os anúncios geraram 13 e 5 pedidos ontem respectivamente, o que indica que ainda há conversão mesmo com penalização. Ação forte neste ponto requer pelo menos 2 dias de direção confirmada.

---

### Escalonamento

**Classificação: observar**

A conta não apresenta risco de reputação imediato (`reputation.color=5_green`, `cancellations_rate=0`, `power_seller_status=gold`), e a única ação operacional urgente — o estoque crítico do Kit 06 Canequinhas Acrílico — é resolúvel por Yasmin sem necessidade de Himmel ou Kobe. A dependência estrutural de ADS (59,8% de share) é o risco principal identificado pela L01, mas com ROAS 11,6x e ACOS 4,64%, a campanha está em fase de leitura inaugural eficiente: não há o que corrigir hoje. A ausência de histórico narrativo (weekly/monthly vazios) reforça a postura de coletar dados limpos antes de qualquer movimento estrutural. **Mudança de classificação:** se ADS share permanecer acima de 55% por 3 dias consecutivos com disponibilidade do `ads_summary` no pacote, Yasmin abre discussão com Kobe sobre dependência estrutural da conta em mídia paga — essa decisão extrapola a tática diária. Se health dos dois campeões em Full cair abaixo de 0,70 ou se o volume de pedidos desses anúncios recuar mais de 30% por 2 dias seguidos, Yasmin alinha com Himmel sobre cobertura preventiva antes que a erosão orgânica apareça no agregado.