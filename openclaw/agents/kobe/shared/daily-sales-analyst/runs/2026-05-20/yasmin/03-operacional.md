<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O GMV do dia foi sustentado por ticket elevado, não por força de volume: 91 pedidos praticamente idênticos ao par histórico de mesmo dia da semana (-1,6%), mas com ticket 34% acima do bimestre. O resultado operacional é real, mas narrow — qualquer queda no mix de SKUs de alto valor ou mudança na composição da campanha desfaz o número sem aviso de volume. Isso confirma diretamente a leitura estratégica de crescimento narrow dependente de composição de ADS/mix.

- A concentração do dia ficou excessivamente apoiada nos produtos líderes (top3 = 48,4%, top5 = 59,3%), com o campeão absoluto (Conjunto 5 Potes Tampa Preta, 23 pedidos) respondendo sozinho por 25,3% dos pedidos. Operacionalmente o dia performou, mas com margem estreita para absorver qualquer instabilidade nesse produto — exatamente o padrão de dependência de campeão identificado pela Estratégica como fragilidade estrutural.

- O fulfillment mix ontem (56,3% Full vs 77,7% no 7d e 73,9% no 30d) foi puxado pelo peso do líder em cross-docking. A divergência não é anomalia de execução — é reflexo direto da composição de vendas do dia: quando o campeão (cross-docking) puxa, o mix declina do padrão Full. Isso adiciona evidência à hipótese tática de que a operação é heterogênea internamente: o anúncio que mais vende não opera no fulfillment dominante da conta.

- Os cancelamentos (3 no dia) são baixos em termos absolutos e a reputação está verde (cancellations_rate=0 na janela longa), mas há um anúncio com available_quantity=3 que operou com 3 pedidos ontem — se esses pedidos confirmaram estoque, a ruptura pode já estar consumada. O risco não está nos cancelamentos de hoje, mas nos que ainda vão aparecer nas próximas horas caso o estoque já tenha zerado.

---

### Sinais operacionais relevantes

- **Sinal:** dois campeões em Full (Kit 4 Potes 1050ml, health=0,75; Conjunto 5 Potes Tampa Vermelha, health=0,71) operam abaixo do threshold ML de 0,85, enquanto ADS compensou a exposição ontem — **interpretação operacional:** o ADS está mascarando a degradação de ranking orgânico desses dois anúncios; a performance de ontem não reflete a saúde de exposição, apenas a eficiência da campanha. Isso adiciona evidência concreta à hipótese tática de operação frágil sob ADS dominante.

- **Sinal:** Kit 06 Canequinhas Acrílico (10º produto, 3 pedidos ontem) com available_quantity=3 — **interpretação operacional:** qualquer combinação de pedidos hoje já zera o estoque, gerando pausa automática do anúncio ou cancelamentos. O anúncio pode já estar indisponível no momento desta leitura, sem que isso apareça ainda nos cancelamentos do dia.

- **Sinal:** fulfillment mix ontem (56,3% Full) ficou 21 pontos abaixo do padrão 7d (77,7%) — **interpretação operacional:** divergência explicada pela concentração de pedidos no campeão cross-docking; não é degradação de infraestrutura Full, mas sinaliza que o dia dependeu de um produto fora do canal de fulfillment principal da conta.

- **Sinal:** ADS gerou R$3.041,56 de R$5.087,71 de GMV (~60% do dia) com ROAS 11,6x e ACOS 4,33% — **interpretação operacional:** motor funcionando com eficiência alta, mas o volume orgânico do dia é estimado em ~R$2.046 (40% do GMV). Sem histórico para comparar, não dá para afirmar se o orgânico está sustentando o patamar ou apenas complementando o ADS.

- **Sinal:** distribuição horária mostra concentração relevante entre 13h-15h (31 pedidos = 34% do volume), com comportamento de janela vespertina dominante — **interpretação operacional:** padrão compatível com ML geral, mas a ausência de referência histórica de horário para esta conta impede afirmar se isso é normal ou se o pico noturno (19-22h, apenas 15 pedidos = 16%) está mais fraco que o padrão.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O dia não apresenta ruptura de execução nem desvio sistêmico — reputação verde, cancelamentos baixos, volume alinhado ao par histórico de mesmo dia da semana, ADS eficiente. Mas há dois desvios operacionais perceptíveis e isolados: (1) o fulfillment mix divergiu 21 pontos do padrão 7d por composição de vendas, não por falha de infraestrutura; (2) um anúncio no top10 está em limiar de ruptura de estoque com janela de 24h. Esses dois pontos não configuram anomalia moderada porque não compartilham causa comum aparente — um é efeito de mix de dia, o outro é risco pontual de inventário. Subiria para **anomalia moderada** se o anúncio de baixo estoque já tiver gerado cancelamentos confirmados ou se health dos dois campeões em Full tiver caído nas leituras seguintes. Desceria para **sem anomalia** se o estoque do Kit 06 Canequinhas Acrílico for confirmado como suficiente e os health dos campeões estiverem estáveis.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** o Kit 06 Canequinhas Acrílico (MLB4410218897) ainda tem unidades disponíveis no momento atual, ou o anúncio já entrou em pausa/ruptura? — **motivada por:** sinal de available_quantity=3 com 3 pedidos ontem; a janela entre o fechamento do dia e esta leitura pode já ter consumado o out-of-stock.

- **Pergunta:** os 3 cancelamentos do dia estão concentrados em algum produto ou anúncio específico, ou são pulverizados? — **motivada por:** número absoluto baixo, mas com anúncio de risco de ruptura no top10; se os cancelamentos tocam o mesmo anúncio, o sinal muda de natureza.

- **Pergunta:** o health do Kit 4 Potes 1050ml (MLB4073003575) e do Conjunto 5 Potes Tampa Vermelha (MLB3288536143) está estável, caindo ou em recuperação em relação à leitura anterior disponível? — **motivada por:** ambos operam abaixo de 0,85 com fulfillment, e ADS está cobrindo a exposição; sem direção do health, não dá para calibrar urgência da intervenção.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o GMV elevado — é que o resultado foi produzido com dois campeões em penalização de ranking (health abaixo de 0,85) cobertos por ADS eficiente, um anúncio top10 à beira de ruptura de estoque, e o produto que mais vendeu operando fora do fulfillment principal da conta. O número de ontem é sólido; a estrutura que o sustentou não é. Esse é exatamente o risco silencioso que a Estratégica apontou como fragilidade central — e o dia confirma o padrão sem que a métrica agregada sinalize problema. A Condensadora deve preservar essa distinção: o dia foi operacionalmente funcional, mas com três pontos de tensão simultâneos que não aparecem no GMV.