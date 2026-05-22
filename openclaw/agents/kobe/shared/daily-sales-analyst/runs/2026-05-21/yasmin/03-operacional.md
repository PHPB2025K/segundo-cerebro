<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- **O GMV foi sustentado integralmente por ticket, não por alcance.** Os 101 pedidos estão dentro da banda normal do bimestre (`orders_vs_60d_pct=+6,0%`) e alinhados ao padrão de quinta (`orders_vs_same_weekday_pct=-1,7%`), enquanto o GMV de R$ 6.113 ficou +57,1% vs 60d e +30,5% acima das últimas 4 quintas. O ticket de R$ 60,52 (+48,1% vs avg 60d de R$ 40,86; +36,4% vs avg 30d de R$ 44,36) é o único driver real do resultado. O canal não cresceu em alcance — cresceu em valor médio por pedido. Confirma operacionalmente a leitura da L01 sobre ticket-led growth.

- **A família IMB501 dominou o dia e puxou o mix de modalidade de envio para Cross-Docking de forma produto-específica.** As três variações dos Conjuntos 5 Potes de Vidro Redondos (Tampa Preta: 31 pedidos; Tampa Cinza: 13; Tampa Vermelha: 9), todas em Cross-Docking, somaram 53 dos 101 pedidos (52,5% do volume). Com o Kit 10 Potes 1050ml (16 pedidos, também Cross-Docking) como segundo colocado, os quatro primeiros do ranking responderam por 69 pedidos via Cross-Docking — resultado direto: `fulfillment_mix_yesterday_top10.cross_docking_pct=80,2%`, invertendo radicalmente o padrão 7d (77% Full) e 30d (73,6% Full). A divergência não é sistêmica — é produto-específica. Isso adiciona evidência operacional concreta à hipótese da L01 sobre ascensão do cluster IMB501: é possível rastrear a causa da inversão de mix até esses quatro anúncios.

- **Ruptura iminente no Kit 06 Canequinhas Acrílico confirmada operacionalmente.** O anúncio (MLB4410218897) entrou o dia com `available_quantity=1`, operou em Full, gerou 3 pedidos, e segue `status=active`. Cada pedido adicional a partir de agora é cancelamento prospectivo garantido, com impacto direto em `reputation.cancellations_rate` — hoje zerada na janela oficial da API. Confirma e adiciona urgência ao sinal levantado pela L01 e à ação definida pela L02 para Yasmin. A janela operacional é imediata.

- **ADS respondeu por 75,1% do GMV com eficiência excepcional, num dia de mix de modalidade de envio invertido.** `revenue_ads_yesterday_brl=R$ 4.593,66` / `GMV=R$ 6.113,02` = 75,1% de share. ROAS de 13,44x, ACOS de 4,71% (`ads_summary.avg_acos_pct`). A campanha está operando com eficiência alta — mas o dia em que esse resultado se materializou foi justamente o dia com maior distorção de mix de modalidade de envio registrada. Se o ADS de Himmel está priorizando os anúncios IMB501 (Cross-Docking), ele está construindo resultado sobre uma estrutura de modalidade diferente do histórico 7d/30d. Não é problema operacional hoje — é dado estrutural que a Condensadora precisa receber.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas Acrílico (MLB4410218897) com `available_quantity=1` e `status=active`, tendo gerado 3 pedidos ontem em Full — **interpretação operacional:** cada pedido adicional nas próximas horas é cancelamento prospectivo garantido. `reputation.cancellations_rate` está zerada na janela oficial; qualquer cancelamento aqui começa a contaminar esse indicador e o `delayed_handling_rate=0,001`, ainda baixo. Janela de ação é de horas, não de dias.

- **Sinal:** Família IMB501 (três variações) operando com `health=null` e respondendo por 52,5% do volume do dia — **interpretação operacional:** `health=null` não é equivalente a saudável — significa que o ML não tem volume histórico suficiente nesses anúncios para calcular o índice. Com a família dominando mais da metade dos pedidos, qualquer degradação operacional (listing, atraso de coleta Cross-Docking, claim) não terá sinalização precoce via health. A ausência do indicador nesse nível de concentração é um risco operacional silencioso.

- **Sinal:** Kit 4 Potes 1050ml Retangular (MLB4073003575) com `health=0,75` gerando 8 pedidos ontem em Full — **interpretação operacional:** único campeão do dia com health calculado e penalizado (abaixo do limiar 0,85). Penalização ativa de exposição orgânica em curso. Se o orgânico está comprometido, os 8 pedidos de ontem podem ser ADS compensando exposição degradada — o que tornaria esse anúncio dependente de campanha para manter volume, não demanda orgânica.

- **Sinal:** Kit 6 Canecas Tulipa 250ml (MLB6167272090) com `available_quantity=14` e ritmo de ~5 pedidos/dia em Full — **interpretação operacional:** runway de aproximadamente 3 dias antes de ruptura. Anúncio opera em Full — estoque no CD do ML exige lead time de reposição maior que Cross-Docking. Não é urgência de hora, mas é alerta de dia confirmado pela L01 e L02.

- **Sinal:** `ratings_negative=0,39` — 39% das avaliações da conta são negativas — **interpretação operacional:** reputação `color=5_green` e `cancellations_rate=0` indicam que o ML ainda não converteu isso em degradação de status formal. Mas 39% de avaliações negativas é sinal que precede queda de conversão orgânica sem aparecer no health de anúncio individual nem nos indicadores de reputação de curto prazo. Não bloqueia execução hoje — é sinal silencioso que merece registro.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.** O que sustenta a classificação: inversão abrupta de mix de modalidade de envio (80,2% Cross-Docking vs padrão 7d de 77% Full e 30d de 73,6% Full), causada por concentração produto-específica em família IMB501; Kit 06 Canequinhas ativo com estoque=1 gerando pedidos — risco operacional imediato aberto. O que mantém em "leve" e não eleva para "moderada": reputação verde e estável, 3 cancelamentos no dia representam taxa de 2,97% — dentro do esperado para o volume, sem padrão acumulado visível; GMV acima do histórico de quintas; ADS eficiente. Subiria para **moderada** se: novo cancelamento no Kit 06 Canequinhas ocorrer antes da ação de Yasmin (combinação de ruptura + impacto em reputação); ou se health de MLB4073003575 cair abaixo de 0,70 nas próximas leituras (duas frentes de degradação simultâneas — modalidade de envio e exposição orgânica de Full).

---

### O que precisa ser investigado pela Granular

- **Pergunta:** O Kit 06 Canequinhas Acrílico (MLB4410218897) já recebeu novos pedidos após o fechamento do dia de ontem, e o `available_quantity` ainda está em 1? — **motivada por:** Sinal 1 e Lente Op 2 — cada pedido adicional é cancelamento prospectivo garantido com `cancellations_rate` hoje zerada. A granular precisa confirmar se a janela de ação ainda está aberta ou se o dano já começou.

- **Pergunta:** Dos 3 cancelamentos do dia, quais anúncios os originaram — estão concentrados em um produto ou são pulverizados? — **motivada por:** Lente Op 2 — 3 cancelamentos sobre 101 pedidos é 2,97%; se concentrados no Kit 06 Canequinhas ou em outro anúncio Full, muda o diagnóstico de reputação e antecipa contaminação da janela de `cancellations_rate`.

- **Pergunta:** Qual a trajetória do health do Kit 4 Potes 1050ml Retangular (MLB4073003575) nos últimos 7 dias — caindo, estável em 0,75 ou recuperando? — **motivada por:** Sinal 3 e Lente Op 4 — penalização ativa com health calculado; saber a direção define se é degradação progressiva (requer ação preventiva) ou piso estabilizado (observação suficiente).

- **Pergunta:** Qual o breakdown do `revenue_ads_yesterday_brl` por anúncio na campanha de Himmel — quais produtos concentram a receita ADS? — **motivada por:** Lente Op 5 — ADS respondeu por 75,1% do GMV num dia de mix Cross-Docking dominante; se a campanha está concentrada nos anúncios IMB501, isso explica simultaneamente a inversão de mix e a eficiência excepcional, e tem implicações para o orgânico dos anúncios Full que não lideraram.

- **Pergunta:** O Kit 10 Potes 1050ml 10 unidades (MLB4676726433, `available_quantity=74`, 16 pedidos ontem em Cross-Docking) tem reposição prevista? — **motivada por:** segundo produto do dia em volume com runway de ~4-5 dias a esse ritmo — próximo alerta de estoque depois do Kit 06 Canequinhas e do Kit 6 Canecas Tulipa, merece mapeamento de pipeline logístico antes de entrar na zona crítica.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o GMV em si — é que o resultado de R$ 6.113 foi construído sobre uma estrutura de modalidade de envio invertida: 80,2% Cross-Docking num canal que nos 30 dias anteriores operou 73,6% Full. Quem causou a inversão foi a família IMB501, amplificada pelo ADS de Himmel (75,1% do GMV, ROAS 13,44x). Isso não é anomalia crítica — a eficiência está excepcional e o Cross-Docking é modalidade legítima da operação. Mas é dado que a Condensadora deve carregar: o patamar de GMV que a L01 identificou como "em ganho" está sendo construído sobre campeões sem health calculado, num mix de modalidade que diverge sistematicamente do histórico de médio prazo — e sem base qualitativa acumulada (weekly/monthly vazios) para avaliar se isso é padrão emergente ou evento de um dia.

O risco silencioso que pode passar enterrado em métrica: `ratings_negative=0,39`. Com 39% de avaliações negativas e reputação ainda verde, a conta está num estágio em que a percepção do comprador já está deteriorada, mas os indicadores formais de reputação do ML ainda não capturaram isso. Esse gap entre avaliações negativas e `color=5_green` é o tipo de sinal que precede queda de conversão orgânica antes de aparecer em qualquer health ou ranking — e num dia em que 75% do GMV passou pelo ADS, o orgânico degradado pode estar sendo mascarado pela campanha eficiente.