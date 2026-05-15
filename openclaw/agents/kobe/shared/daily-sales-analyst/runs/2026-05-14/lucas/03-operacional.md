<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- **Conta 1 (Store) operou essencialmente como dois anúncios, não como uma conta.** De 35 pedidos, 30 itens vieram de dois produtos (Jarra Medidora + Potes Vidro Redondos), e 9 dos 35 pedidos aconteceram na janela 21-22h. A conta não está apenas concentrada por produto — está concentrada por produto *e* por janela horária, o que reduz o número de pontos de falha para absorver qualquer deterioração. Confirma e intensifica o risco de dependência estrutural levantado pela Estratégica: o mecanismo operacional da queda não é difuso, é cirúrgico nos dois campeões em horário específico.

- **Conta 2 (Oficial) mostra padrão horário operacionalmente distinto das outras duas contas.** Pedidos concentrados no diurno (8h-18h) e ausência total entre 19-21h — enquanto Conta 1 e Conta 3 têm tração nesse período. Combinado com ticket médio elevado (R$71,66 vs R$52,80 em 60d), o dia reforça a hipótese de mix-shift da Estratégica com uma dimensão adicional: não é apenas o que está sendo comprado, mas *quando* — o perfil de horário sugere comprador diferente (mais diurno, menor impulsividade noturna), o que poderia explicar tanto o ticket maior quanto o volume menor de forma coerente.

- **Conta 3 (Shop) gerou mais GMV que Conta 1 e superou sua própria média de 7d, com o maior ticket das três contas.** A hierarquia histórica de contribuição de GMV se inverteu no dia: Conta 3 responde por ~41% do GMV total da plataforma. Isso não é sinal de crescimento de Conta 3 isolado — é consequência da queda de Conta 1. Operacionalmente, a plataforma está rodando com estrutura de sustentação diferente da histórica, e Conta 3 é hoje o único vetor funcional dentro do esperado, confirmando a leitura da Estratégica de "em acomodação".

- **A ausência de cancelamentos nas três contas é operacionalmente positiva, mas não altera a leitura de volume.** Os pedidos que chegaram foram concluídos. O problema da plataforma não está em execução pós-pedido — está em geração de demanda, particularmente em Conta 1, onde o declínio multi-janela (60d→30d→7d→hoje) continua sem sinal de reversão.

---

### Sinais operacionais relevantes

- **Sinal:** Conta 1 (Store) com 30 dos 35 itens vendidos em apenas dois SKUs e 9 dos 35 pedidos concentrados na janela 21-22h — **interpretação operacional:** a conta está operando com dependência dupla: de produto *e* de horário; perda de exposição nos campeões no período noturno seria suficiente para zerar o resultado da conta; a checagem priorizada pela Tática (visibilidade dos campeões nos horários de pico) tem base operacional sólida neste dado.

- **Sinal:** Conta 2 (Oficial) com gap completo de pedidos entre 19h e 21h, enquanto tem presença diurna (8h-18h) e um pedido às 21h — **interpretação operacional:** a ausência nesse período pode indicar exposição desligada ou perfil de comprador concentrado em horário comercial; se for exposição, é oportunidade de receita perdida; se for perfil, reforça a hipótese de mix-shift para comprador de maior valor; inconclusivo com um ponto, mas é dimensão operacional que não aparece olhando só pedidos e ticket.

- **Sinal:** Inversão da hierarquia de GMV — Conta 3 (Shop, R$1.769) > Conta 2 (R$1.289) > Conta 1 (R$1.225), sendo que Conta 1 é historicamente a principal — **interpretação operacional:** a estrutura de contribuição da plataforma mudou no dia; a Condensadora não deve tratar o GMV agregado como "plataforma Shopee funcionando" — a composição é fundamentalmente diferente do padrão histórico.

- **Sinal:** Conta 3 com ticket médio de R$76,93, o mais alto das três contas, acima da própria média de 30d (R$67,43, +14%) — **interpretação operacional:** ticket elevado com volume próximo à média de 7d sugere ou mix mais pesado (kits maiores) ou menor pressão promocional; se for ausência de cupom/ADS mais agressivo, o desempenho de Conta 3 pode estar sendo sustentado com margem melhor, o que muda a leitura do resultado relativo da conta.

- **Sinal:** Concentração top3 de 91,4% na Conta 1 (Store) com quality flag registrado pelo sistema — **interpretação operacional:** o sistema sinalizou anomalia de concentração; o dado operacional confirma que não é artefato estatístico — os dois produtos líderes venderam 17 e 13 unidades respectivamente em um dia de 35 pedidos totais; não há terceiro produto com tração real.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada** — localizada em Conta 1 (Store), com múltiplas dimensões convergentes: volume abaixo do mínimo histórico das últimas quatro quartas, concentração extrema em dois SKUs (91,4% top3 com quality flag ativo), tração horária excessivamente dependente da janela noturna (21-22h), e GMV que não é sustentado por profundidade de mix. A anomalia não é crítica porque não há ruptura de listing, cancelamento sistêmico ou bloqueio operacional — os pedidos que chegaram foram concluídos e o sistema de coleta validou os dados. Para subir a crítica, bastaria confirmar perda de posição de ranking nos campeões no período noturno. Para Conta 2 e Conta 3, o comportamento está dentro do que o contexto operacional do dia indica como esperado — a base vazia de weekly/monthly impede afirmar "sem anomalia" com total segurança para essas contas, mas os sinais observados são consistentes com as hipóteses em aberto, não com desvios inesperados.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** A posição de ranking dos produtos campeões da Conta 1 (Jarra Medidora e Potes Vidro Redondos) especificamente no período 19-22h caiu em relação à semana anterior? — **motivada por:** sinal de tração horária excessivamente concentrada no noturno com queda de volume abaixo do mínimo histórico de quartas; se a exposição noturna dos dois SKUs enfraqueceu, esse é o mecanismo operacional central da deterioração de Conta 1 — exatamente a checagem que a Tática priorizou, com dimensão horária adicional.

- **Pergunta:** O gap de pedidos na Conta 2 entre 19h-21h é padrão recorrente nos dias anteriores (2026-05-07 a 2026-05-12) ou foi específico de 2026-05-14? — **motivada por:** sinal de ausência total de pedidos nesse período em Conta 2, enquanto as outras duas contas têm presença; se for recorrente, é característica do perfil de comprador da conta; se for novo, sugere exposição alterada nesse horário.

- **Pergunta:** O ticket elevado de Conta 3 (R$76,93) está sendo sustentado por produto específico de valor mais alto ou pela ausência de cupom/desconto ativo nesta conta no dia? — **motivada por:** sinal de inversão da hierarquia de GMV com Conta 3 superando Conta 1, com ticket quase o dobro; distinguir se o resultado é mix ou ausência de pressão promocional muda a interpretação de sustentabilidade do desempenho relativo da conta.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia é que Conta 1 (Store) está funcionando como dois anúncios com janela noturna — não como uma conta. A combinação de dependência em dois SKUs + concentração em período específico do dia significa que a conta não tem defesa operacional: qualquer oscilação de posição dos campeões no horário 21-22h é o resultado inteiro da conta. Isso confirma e adiciona precisão ao risco estrutural apontado pela Estratégica, e sustenta operacionalmente a priorização da Tática para checar exposição dos campeões — com o dado adicional de que a checagem deveria ser específica para o período noturno, não genérica. O risco silencioso que pode passar despercebido no agregado: o GMV total da plataforma (R$4.284) parece razoável como número, mas está sendo sustentado por uma estrutura onde Conta 3 passou a ser o maior contribuidor individual — uma inversão de hierarquia que indica que a plataforma está funcionando com uma composição diferente da histórica, não com saúde distribuída entre as três contas.