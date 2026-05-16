<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- A Store sustentou o GMV via elevação de ticket (+25% vs 30d), com volume caindo -21% no mesmo período — operacionalmente, o dia da Store funcionou porque os pedidos que vieram valeram mais, não porque o fluxo foi forte. Isso confirma a tese estratégica de resiliência frágil: o mecanismo de sustentação do GMV é qualidade de pedido, não volume, e 79% desses pedidos veio de dois produtos (Conjunto 5 Potes Vidro Redondos Tampa Preta e Jarra Medidora de Vidro 500ml). O dia performou, mas sem redundância operacional.

- A Oficial 2 não apenas vendeu pouco — a conta praticamente não recebeu tráfego durante o dia. A distribuição horária revela apenas 9 janelas com qualquer atividade, com picos isolados às 15h (4 pedidos) e 23h (4 pedidos), e ausência total em blocos inteiros do dia que seriam naturalmente ativos. Esse padrão de chegada de pedidos não é demanda baixa — é ausência de distribuição de impressões. Adiciona evidência operacional direta à hipótese tática de verificação de ADS e exposição da Conta 2: o comportamento horário é o sinal mais concreto do dia.

- A Shop 3 sustentou volume no patamar de 30d, mas com rotação de mix identificável: Kit 6 Canecas Tulipa e Kit 6 Canecas Retas responderam por 59% dos pedidos — produtos de menor valor unitário que os potes herméticos. Essa composição explica mecanicamente a compressão de ticket (-15,4% vs 30d). Além disso, 3 cancelamentos em 27 pedidos (~11%) formam uma taxa relativa que não se replica na Store (3%) nem na Oficial 2 (zero) — sinal conta-específico que precisa ser verificado.

- No agregado, a Store carregou 60% dos pedidos e do GMV do canal num dia em que a Oficial 2 deveria contribuir com cerca de 28–30% mas entregou 15%. A divisão operacional entre as três contas confirma que o número consolidado da Shopee mascara um desequilíbrio real na arquitetura do canal, exatamente como a Estratégica havia apontado.

---

### Sinais operacionais relevantes

- **Sinal:** Oficial 2 com distribuição horária extremamente fragmentada — apenas 9 horas com atividade, ausência total em blocos inteiros do dia — **interpretação operacional:** não é dia de demanda fraca com pedidos distribuídos; é padrão de conta sem tráfego consistente, o que operacionalmente aponta para ausência de cobertura de campanha, redução de ADS ou problema de listing; adiciona evidência concreta à hipótese tática que já identificou o diagnóstico de exposição como prioridade.

- **Sinal:** 3 cancelamentos na Shop 3 em 27 pedidos válidos (~11% de taxa) contra zero na Oficial 2 e 3% na Store — **interpretação operacional:** a concentração relativa na Shop 3 não é desprezível; se os 3 cancelamentos estiverem no mesmo SKU ou categoria, muda de evento pontual para problema de produto específico naquela conta; não generalizar para o canal — o sinal é exclusivo da Conta 3.

- **Sinal:** Store com top 5 produtos cobrindo 100% dos pedidos válidos, e top 2 sozinhos em 79% — **interpretação operacional:** o dia funcionou operacionalmente dependente de dois itens; a concentração extrema que a Estratégica identificou como risco estrutural se manifestou hoje como realidade de execução, não como hipótese; qualquer descontinuidade nesses dois produtos não tem amortecedor no mix atual da conta.

- **Sinal:** Ticket médio da Oficial 2 (R$73,42) acima da média de 30d (R$59,72, +22,9%) mesmo com colapso de volume — **interpretação operacional:** os poucos pedidos que chegaram à Oficial 2 foram de maior valor individual, o que sugere que o problema não é de qualidade de demanda ou conversão — é de alcance; o público que chega converte bem, mas o tráfego simplesmente não chegou em volume suficiente.

- **Sinal:** Mix de Shop 3 dominado por canecas (CTL002 + KIT6CAR200 = 59% dos pedidos) numa conta que historicamente tinha maior presença de potes herméticos — **interpretação operacional:** a rotação de mix explica mecanicamente a compressão de ticket de -15,4% vs 30d; a questão operacional relevante é se essa rotação é efeito de ADS direcionado ou demanda orgânica — as respostas têm implicações opostas para qualquer ajuste de campanha.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada** — localizada na Oficial 2, com sinal secundário na Shop 3.

A Oficial 2 apresenta desvio operacional em múltiplas dimensões ao mesmo tempo: volume 51,8% abaixo do mesmo dia da semana histórico, distribuição horária com ausência de tráfego em blocos inteiros do dia, e ticket elevado que indica pedidos qualificados mas alcance insuficiente. A combinação dos três não é coincidência de métricas isoladas — é um padrão de conta sem exposição consistente. Na Shop 3, a taxa de cancelamento de 11% em contexto de compressão de ticket e rotação de mix indica que o funcionamento da conta não é completamente normal, mas ainda não configura anomalia moderada isolada. A Store, por contraste, opera dentro do padrão de desaceleração de volume com sustentação de GMV via ticket que já estava registrado nas janelas de 30d/60d — não é anomalia, é continuidade.

O que faria subir para anomalia crítica: Oficial 2 com o mesmo padrão horário fragmentado repetido amanhã, ou confirmação de listing inativo/estoque zero em produto relevante da conta. O que faria rebaixar para anomalia leve: distribuição horária da Oficial 2 mais uniforme no próximo dia, com volume retornando à faixa de 25–30 pedidos.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Os 3 cancelamentos da Shop 3 estão concentrados em algum SKU ou categoria específica? — **motivada por:** taxa de cancelamento de ~11% na Shop 3 contra 3% na Store e zero na Oficial 2; se concentrados em um produto, muda de evento pontual para problema de listing ou estoque naquele item específico.

- **Pergunta:** Em quais blocos horários a Oficial 2 registrou zero pedidos hoje, e esse padrão de lacuna horária aparece nos últimos 3–5 dias da conta? — **motivada por:** distribuição horária extremamente esparsa da Oficial 2 com ausência total em blocos que seriam naturalmente ativos; a recorrência ou não desse padrão horário é a evidência operacional mais direta para separar "dia ruim" de "problema de exposição sistêmico".

- **Pergunta:** A Oficial 2 tem algum produto com listing inativo, estoque zero ou penalidade de reputação nos últimos 3 dias? — **motivada por:** colapso de volume conta-específico com distribuição horária atípica; se ADS e exposição estiverem normais (conforme verificação da Tática), a próxima hipótese operacional é problema de listing ou estoque na conta 860803675.

- **Pergunta:** O mix de canecas (CTL002 + KIT6CAR200) na Shop 3 cresceu em participação relativa comparado às últimas 4 quintas-feiras da conta, ou é proporção historicamente estável? — **motivada por:** 59% dos pedidos da Shop 3 hoje em canecas, explicando compressão de ticket; saber se é rotação nova ou padrão histórico da conta define se é tendência a monitorar ou comportamento esperado.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não está no GMV consolidado da Shopee — está na forma como a Oficial 2 distribuiu (ou não distribuiu) pedidos ao longo do dia. A distribuição horária fragmentada, com ausência total de tráfego em blocos inteiros, é um sinal operacional mais concreto do que o simples volume baixo: operacionalmente, a conta não está sendo exposta de forma consistente. Isso reforça e adiciona granularidade à hipótese tática de verificação de ADS/exposição com Himmel via Lucas — não como checagem de rotina, mas como diagnóstico com evidência comportamental de que o problema tem cara de ausência de distribuição de impressões, não de demanda fraca. A Condensadora deve carregar esse ponto como o risco operacional mais urgente do dia — silencioso no número consolidado, visível no comportamento horário da Conta 2.