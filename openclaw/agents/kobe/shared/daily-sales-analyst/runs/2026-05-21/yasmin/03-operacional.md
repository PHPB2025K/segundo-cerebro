<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O volume do dia ficou plano em relação às bandas históricas — 100 pedidos vs avg_30d 99,3 (+0,7%) e avg same_weekday 102,75 (-2,7%) — mas o GMV atingiu R$6.082,82 (+38% vs 30d, +56,5% vs 60d). A execução confirma operacionalmente a leitura da L01: o resultado foi integralmente sustentado por ticket (R$60,83, +37,1% vs 30d), não por expansão de alcance. O canal não captou mais pedidos — captou mais valor por pedido. Dentro da banda de volume, o dia foi completamente normal; no GMV, foi excepcional.

- O mix de fulfillment do top 10 divergiu 53,6 pontos do padrão mensal: `fulfillment_mix_yesterday_top10.full_pct=20%` vs `fulfillment_mix_30d.full_pct=73,6%`. A divergência é produto-específica, não sistêmica: os três primeiros colocados — Conjunto 5 Potes Tampa Preta (31 pedidos), Kit 10 Potes Herméticos 1050ml (16 pedidos) e Conjunto 5 Potes Tampa Cinza (13 pedidos) — são todos `logistic_type=cross_docking` e concentraram 60% do volume do dia (`top3_concentration=60`). Adiciona evidência operacional à hipótese da L01 de que o vetor de geração de GMV atual não depende de Full nos campeões — mas o histórico mensal deixa claro que, estruturalmente, Full ainda é o padrão dominante da conta (73,6% em 30d).

- O único anúncio Full com health calculada no top 10 — Kit 4 Potes 1050ml (MLB4073003575, 8 pedidos, `health=0.75`, `logistic_type=fulfillment`) — operou o dia inteiro com penalização ML ativa (limiar: 0,85). Os outros 9 itens do top 10 têm `health=null`: não significa saúde plena, significa que o ML não calculou health por volume insuficiente. A base Full do dia operou penalizada no único ponto onde o ML efetivamente mensurou saúde. Confirma o sinal da L01 sobre degradação de listing no campeão Full.

- O Kit 06 Canequinhas Acrílico (MLB4410218897, `logistic_type=fulfillment`, `available_quantity=2`) registrou 3 pedidos no dia. A execução operacional criou pedidos que superam o estoque disponível: a ruptura não é iminente, já aconteceu. Esse fato não estava visível nas métricas agregadas do dia e adiciona urgência operacional concreta ao risco identificado pela L01 e à ação definida pela L02 — cada ciclo sem reposição no CD do ML é um ciclo com cancelamento prospectivo incubado.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas Acrílico (MLB4410218897) registrou 3 pedidos com `available_quantity=2` em `logistic_type=fulfillment` — pedidos gerados superam estoque disponível no CD do ML. — **Interpretação operacional:** Pelo menos 1 pedido do dia não tem cobertura de estoque. Como o item opera em Full, o ML gerencia o envio diretamente; o lojista não controla o timing do cancelamento. A janela antes de impacto em `reputation.cancellations_rate` (hoje em 0%) já está aberta.

- **Sinal:** Kit 10 Potes Herméticos 1050ml (MLB4676726433) foi o 2º maior volume do dia — 16 pedidos — com `available_quantity=78` em `logistic_type=cross_docking`. — **Interpretação operacional:** Ao giro de ontem, cobertura estimada de ~5 dias. Como opera em Cross-docking, a reposição exige abastecimento físico na expedição Budamix antes da coleta do ML — não é ajuste de CD externo. O item integra o top 3 que concentrou 60% do volume; queda de disponibilidade aqui comprime o vetor principal de GMV do dia.

- **Sinal:** Kit 4 Potes 1050ml (MLB4073003575, `logistic_type=fulfillment`) operou o dia com `health=0.75`, abaixo do limiar ML de 0,85. — **Interpretação operacional:** É o único item Full do top 10 com health calculada, com `sold_quantity=961` histórico e 8 pedidos ontem — relevância real rodando com penalização ativa. Sem trajectory disponível (apenas leitura pontual de hoje), não é possível determinar se está caindo, estabilizando ou se recuperando. A penalização pode estar comprimindo exposição e limitando o que esse anúncio geraria sem a penalização.

- **Sinal:** `ads_summary.spend_yesterday_brl=0,00` e `revenue_ads_yesterday_brl=0,00` com 11 campanhas nominalmente ativas — GMV de R$6.082,82 gerado sem investimento registrado em Mercado Ads. — **Interpretação operacional:** ADS share do dia = 0%. O resultado — incluindo ticket elevado, concentração nos top 3 Cross-docking e volume plano — foi gerado sem ADS confirmado. A leitura de força orgânica é factualmente sustentada pelo dado, mas a interpretação (orgânico sólido vs dia com falha de veiculação) é irresolvível por este pacote sem confirmação de Himmel. A Lente Op 5 é inconclusiva.

- **Sinal:** Kit 6 Canecas Tulipa Lisa (MLB6167272090, `logistic_type=fulfillment`, `available_quantity=19`, 5 pedidos ontem) aparece em 6º lugar com estoque de cobertura estimada em ~4 dias ao giro atual. — **Interpretação operacional:** Não foi citado como risco crítico pela L01/L02, mas a combinação de Full + estoque baixo + giro diário coloca este item como segundo horizonte de ruptura após o Canequinhas. Não tem a urgência de hoje, mas está na janela operacional de curto prazo.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O fato operacional concreto que excede o padrão é a ruptura efetiva no Kit Canequinhas — pedidos gerados além do estoque disponível em Full, com janela de cancelamento já aberta. Isolado em um único item, com reputação intacta (5_green, `cancellations_rate=0`), volume e GMV dentro ou acima das bandas históricas e demais anúncios ativos, o enquadramento é leve. O que elevaria para **moderada**: cancelamentos do Canequinhas aparecendo registrados no próximo ciclo, ou confirmação de que o zero de ADS foi falha técnica (dia contaminado, não orgânico puro) acompanhada de queda de volume nas próximas leituras. O que sustenta manter em leve: o desvio está concentrado em um único ponto operacional, sem padrão acumulado visível, e a reputação ainda está na banda verde com `cancellations_rate=0` — o impacto ainda não se materializou.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual é o status operacional atual dos 3 pedidos registrados para o Kit 06 Canequinhas Acrílico (MLB4410218897)? Algum já foi cancelado, está em processamento sem cobertura ou gerou comunicação do ML ao lojista? — **Motivada por:** Sinal 1 — ruptura efetiva com 3 pedidos e `available_quantity=2` em Full; a janela de impacto em reputação já está aberta.

- **Pergunta:** Qual é a direção do `health` do Kit 4 Potes 1050ml (MLB4073003575) nos ciclos disponíveis — queda, estabilização ou recuperação em relação ao 0,75 registrado ontem? — **Motivada por:** Sinal 3 — único campeão Full com health calculada e penalização ativa; sem trajectory, nenhuma decisão de intervenção ou observação é informada.

- **Pergunta:** A composição do `revenue_ads` por anúncio nos ciclos recentes mostra que Himmel estava priorizando algum dos top 3 Cross-docking (IMB501P, KIT10YW1050, IMB501C)? Ou o zero de spend de ontem representa pausa deliberada de toda a campanha? — **Motivada por:** Sinal 4 — zero de ADS com 11 campanhas ativas; sem breakdown por anúncio, é impossível isolar se os campeões Cross-docking do dia são orgânicos estruturais ou beneficiários de campanha ativa nos dias anteriores.

- **Pergunta:** O Kit 6 Canecas Tulipa Lisa (MLB6167272090, `available_quantity=19`, `logistic_type=fulfillment`, 5 pedidos ontem) está no range de segurança de estoque ou é o próximo horizonte de ruptura em Full após o Canequinhas? — **Motivada por:** Sinal 5 — cobertura estimada de ~4 dias em Full com giro atual; não foi citado como risco prioritário pela L01/L02, mas está na mesma janela operacional de curto prazo do Canequinhas.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o ticket elevado nem o GMV acima das bandas — é a combinação de dois sinais que precisam ser lidos juntos: o Kit Canequinhas já está em ruptura efetiva com cancelamento prospectivo incubado, e o zero de ADS deixa inconclusiva a interpretação de força orgânica. Esses dois fatos limitam qualquer leitura otimista do dia sem ressalva. O risco de reputação identificado pela L01 está mais próximo de se materializar do que o pacote bruto sugere: `reputation.cancellations_rate=0` ainda não captura os pedidos registrados sem cobertura de estoque — essa métrica só move no próximo ciclo, quando o dano já terá acontecido. Se o dia for lido apenas como "GMV acima do histórico com ticket forte", o sinal mais urgente some. A Condensadora precisa carregar o Canequinhas como risco ativo, não como detalhe de inventário.