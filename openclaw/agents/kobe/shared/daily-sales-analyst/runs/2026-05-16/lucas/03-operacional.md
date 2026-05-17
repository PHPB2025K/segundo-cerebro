<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- A Store sustentou o resultado da plataforma quase inteiramente via produto único: Conjunto 5 Potes de Vidro Redondos Tampa Preta (IMB501P) com 31 dos 57 pedidos da conta (~54%). O GMV da Store ficou próximo da média dos últimos 7 dias (-1.8%), mas essa estabilidade é artificial — volume já está 31.4% abaixo do 30d, e o que segura o número é um único produto funcionando. Isso confirma operacionalmente o risco de dependência identificado pela Estratégica: a conta não tem segundo vetor, tem um campeão e bastidores.

- A Oficial 2 operou de forma descolada das outras duas contas: ticket de R$71.93 acima da média 7d (R$60.02) e GMV 21.4% acima do 7d — único vetor positivo da plataforma. O produto líder (Kit 4 Potes de Vidro 800ml Quadrado com 7 pedidos) é de maior valor unitário, e os 3 primeiros produtos da conta concentram 72.7% dos pedidos com mix distinto das outras contas. Isso adiciona evidência à hipótese estratégica de mix shift na Oficial 2: o dia foi sustentado por produtos mais caros, não por mais pedidos.

- A Shop 3 confirmou operacionalmente a dupla deterioração apontada pela Estratégica: ticket comprimido para R$52.03 contra média 7d de R$63.19 (-17.7%), GMV 31.8% abaixo do 7d. Os produtos líderes (Kit 2 Potes 800ml com 7 pedidos e Kit 6 Canecas Retas com 5) são itens de menor valor médio, o que é coerente com a compressão de ticket. A conta hoje entregou menos volume e mix mais barato simultaneamente — sem mecanismo de compensação visível.

- O cancelamento registrado na plataforma está concentrado na Oficial 2 (única conta com cancelamento no dia). Isoladamente não forma padrão, mas sua ocorrência na conta com menor volume e maior ticket merece rastreamento — um cancelamento em 22 pedidos tem peso percentual diferente de um em 57.

---

### Sinais operacionais relevantes

- **Sinal:** distribuição horária da Store inclui 3 pedidos às 0h e 3 pedidos às 2h, padrão incomum fora da janela comercial — **interpretação operacional:** pode indicar pedido via promoção agendada, campanha noturna ou comportamento orgânico residual; não altera o resultado do dia, mas aponta execução em janela atípica que merece checagem se o padrão se repetir; não generalizar para as outras contas onde essa janela não aparece.

- **Sinal:** Oficial 2 não registrou pedidos após 20h (apenas 1 pedido no horário) e encerrou a atividade antes das 21h — **interpretação operacional:** o padrão de venda da Oficial 2 foi inteiramente diurno e vespertino (picos às 10h e 15h), diferente da Store que tem tração até as 21-22h; isso pode refletir perfil de audiência diferente entre as contas, ou ausência de campanha noturna ativa na Oficial 2 neste dia.

- **Sinal:** Shop 3 registrou todos os 20 pedidos na janela das 10h às 19h, sem nenhum pedido antes das 10h ou após 19h — **interpretação operacional:** operação completamente concentrada em horário comercial/vespertino, sem atividade noturna. Dado que a conta está com GMV e ticket em queda simultânea, a ausência de qualquer volume fora da janela comercial estreita ainda mais o espaço de recuperação diária; confirma deterioração operacional já apontada pela Estratégica.

- **Sinal:** ticket da Oficial 2 hoje (R$71.93) está 20.4% acima do 30d (R$59.73), com Kit 4 Potes 800ml como líder e top 3 concentrando 72.7% dos pedidos — **interpretação operacional:** a conta não entregou mais pedidos, entregou pedidos mais caros; isso é coerente com mix shift para produtos de maior valor, como apontou a Estratégica; a questão que a Granular precisa responder é se esse mix mais caro é novo ou se sempre foi padrão da Oficial 2 — só a comparação histórica de mix resolve.

- **Sinal:** o único cancelamento do dia está na Oficial 2, conta com apenas 22 pedidos — **interpretação operacional:** 1 cancelamento em 22 pedidos representa ~4.5% de taxa de cancelamento na conta; em volume baixo, um único cancelamento distorce mais do que num volume alto; não há padrão com os dados do dia, mas se a conta registrar cancelamentos em 2-3 dias seguidos com volume igualmente baixo, o sinal se torna relevante.

---

### Anomalias ou ausência de anomalia

**anomalia leve**

O dia não tem desvio operacional que bloqueie execução. A Store operou com volume abaixo do 30d e 60d, mas isso é padrão da conta nas últimas semanas — não é anomalia do dia, é o patamar atual. A Shop 3 confirma deterioração, mas sem sinal novo em relação ao que vinha sendo registrado nas janelas históricas. O que eleva para "anomalia leve" é a combinação de dois desvios pontuais isolados: (1) presença incomum de pedidos da Store nas madrugadas (0h e 2h), sem precedente observável nos dados do dia; e (2) encerramento precoce da Oficial 2 em 20h sem atividade noturna num dia em que a conta está em processo de leitura de ticket divergente. Nenhum dos dois sozinho seria anomalia; juntos apontam para comportamento horário não-uniforme entre as contas que merece rastreamento. Para subir para "anomalia moderada" seria necessário que o cancelamento da Oficial 2 se repetisse ou que a distribuição noturna da Store fosse confirmada como padrão novo.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** os pedidos registrados pela Store às 0h e 2h estão associados a alguma campanha ativa ou cupom agendado, ou são orgânicos? — **motivada por:** sinal de distribuição horária atípica da Store com 6 pedidos fora da janela comercial usual, padrão não observado nas outras duas contas no mesmo dia.

- **Pergunta:** qual é o produto associado ao cancelamento na Oficial 2? — **motivada por:** sinal de cancelamento isolado numa conta com apenas 22 pedidos (impacto percentual de ~4.5%); se for o Kit 4 Potes 800ml (produto líder e de maior ticket), o impacto no GMV da conta é desproporcional.

- **Pergunta:** o mix da Oficial 2 hoje (liderado por produtos de ticket alto como Kit 4 Potes 800ml) é padrão recorrente desta conta ou este dia diverge do mix habitual? — **motivada por:** sinal de ticket em forte expansão na Oficial 2 (+20.4% vs 30d), com hipótese estratégica de mix shift; a Granular precisa confirmar se o Kit 4 Potes 800ml já liderava a conta nos dias anteriores ou se hoje foi uma composição atípica.

- **Pergunta:** a Shop 3 registrou algum produto de maior ticket (acima de R$70-80 unitário) no dia, ou o mix foi inteiramente composto pelos líderes atuais de menor valor? — **motivada por:** sinal de compressão de ticket na Shop 3 para R$52 contra média histórica de R$64-67; se produtos mais caros da conta simplesmente não venderam hoje, há hipótese de perda de exposição específica desses itens.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é a queda da plataforma — é a divergência estrutural entre as três contas que ficou mais nítida na execução. A Store opera no limite de sustentação por um único produto; a Shop 3 deteriora em volume e mix sem compensação; mas a Oficial 2 entregou GMV acima do seu próprio padrão recente com ticket em expansão e mix mais caro. Esse descolamento não é ruído: é a Oficial 2 operando sob lógica diferente das outras duas contas no mesmo dia, no mesmo canal. A Condensadora deve decidir se apresenta isso como sinal de atenção positivo (conta 2 diverge) ou como elemento de leitura de contexto — porque se a queda for apresentada como bloco ("Shopee caiu"), o sinal da Oficial 2 desaparece e a leitura perde precisão. O risco silencioso é tratar as três contas como um resultado uniforme quando a execução do dia mostrou comportamentos distintos em volume, ticket e distribuição horária.