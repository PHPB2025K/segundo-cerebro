<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O dia sustentou GMV acima da banda histórica do mesmo dia da semana (+31.6% vs média R$3.841) com volume de pedidos praticamente idêntico ao padrão (-2.7%). O mecanismo não foi tração ampla — foi qualidade do pedido. O ticket de R$56.19 fez o trabalho que o volume não fez, confirmando operacionalmente a tese da Estratégica de elevação ticket-driven ao longo do bimestre. O dia não é exceção: é mais um ponto da série que a Estratégica identificou como padrão emergente.

- A concentração operacional foi alta: os três primeiros produtos responderam por 47.8% dos pedidos, com o líder (Conjunto 5 Potes Tampa Preta) carregando 24.4% sozinho. O que torna isso operacionalmente relevante é o **tipo** de anúncio no topo: o líder opera em cross_docking, sem Frete Grátis — e mesmo assim puxou o dia. Isso é consistente com a hipótese estratégica de dependência de poucos produtos, mas adiciona um detalhe operacional: o produto que mais vendeu não é o de melhor condição logística da conta.

- O fulfillment mix do dia (57% Full / 43% cross_docking) divergiu significativamente da janela 7d (78% / 22%) e 30d (74% / 26%). A causa operacional direta é o peso do produto líder em cross_docking: com 22 pedidos do top seller saindo em cross_docking, o mix do dia naturalmente puxou para fora do padrão Full. Isso não representa deterioração de Full — é distorção de mix por concentração no produto #1. Mas é informação relevante para a Tática: em dias com líder muito dominante em cross_docking, a taxa de Full no dia vai parecer menor mesmo sem mudança estrutural.

- ADS respondem por estimados 60% do GMV do dia (R$3.041 de R$5.057) com ACOS eficiente (4.33%), o que adiciona evidência operacional à hipótese estratégica de amplificação ADS sobre seleção de produto de maior valor. O mix atribuído à campanha provavelmente inclui os produtos de fulfillment com ticket mais alto — mas sem desagregação ADS por produto, essa conexão é operacionalmente inferida, não confirmada.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 06 Canequinhas com Suporte Acrílico com estoque em 3 unidades e anúncio ativo — **interpretação operacional:** ruptura iminente sem contenção visível; se o anúncio for pausado por estoque nos próximos 1-2 dias, contamina a série de leitura de volume da conta e elimina um ponto do mix de cauda que a Tática havia identificado como variável confundidora em potencial. Confirma o alerta iminente levantado pela Estratégica.

- **Sinal:** Produto líder do dia (Conjunto 5 Potes Tampa Preta, 22 pedidos) opera em cross_docking, sem Frete Grátis, e sem dado de health disponível — **interpretação operacional:** a ausência de health nesse anúncio impede avaliar se a liderança de volume é produto de exposição saudável ou de campanha compensando queda de orgânico. Sendo o anúncio responsável por quase 1 em cada 4 pedidos do dia, a falta de saúde documentada é ponto cego operacional relevante.

- **Sinal:** Kit 4 Potes de Vidro 1050ml Retangular (segundo maior produto, 13 pedidos) em fulfillment com health 0.75 — **interpretação operacional:** saúde abaixo do limiar de 0.85 no segundo anúncio mais vendido e de maior ticket relativo. Adiciona evidência ao sinal que a Tática pediu para Yasmin checar: se o health está em deterioração (e não em estabilidade em 0.75), o anúncio pode estar perdendo exposição orgânica enquanto o ADS compensa o volume — o que tornaria a dependência ADS ainda mais real do que a hipótese estratégica atual sugere.

- **Sinal:** Conjunto 5 Potes Tampa Vermelha (5 pedidos, em catálogo) com health 0.71 — **interpretação operacional:** é o anúncio de pior saúde entre os listados, e opera em catálogo (catalog_product_id presente), o que o expõe à competição direta de outros vendedores no mesmo listing. Health baixo em anúncio de catálogo é sinal operacional de vulnerabilidade dupla: perda de ranking próprio + risco de Buy Box para concorrente na mesma página de produto. Não é o maior produto do dia, mas é o de maior fragilidade estrutural entre os ativos.

- **Sinal:** Kit 6 Tigelas de Vidro 250ml com 20 unidades disponíveis e sem dado de health — **interpretação operacional:** estoque não crítico ainda (não é ruptura iminente), mas combinado com ausência de health, é segundo produto de cauda em zona de atenção. Se reposição não estiver em andamento, pode replicar o padrão do Kit Canequinhas com Suporte Acrílico em alguns dias.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O dia operou dentro do padrão esperado em volume e reputação, sem ruptura de execução visível. O que constitui desvio operacional perceptível é a combinação de: (1) mix de fulfillment desviante do padrão 7d/30d por peso do produto líder em cross_docking, e (2) dois produtos de fulfillment com health abaixo do limiar entre os cinco maiores do dia. Nenhum dos dois, isolado, eleva para anomalia moderada: o fulfillment mix tem causa identificável no comportamento do líder, e o health baixo é dado que precisa de comparação temporal (está deteriorando ou estável em 0.75?) para ter peso operacional. A ausência de health em 64 dos 82 anúncios ativos é estrutural e não é novidade do dia — mas impede afirmar "tudo dentro do padrão" com a mesma segurança que teria em uma base com health completo. O que eleva de "sem anomalia" para "leve" é que os sinais operacionais existem e precisam de verificação pontual — não que algo esteja quebrado.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** o Kit 06 Canequinhas com Suporte Acrílico tem reposição prevista ou agendada? — **motivada por:** estoque em 3 unidades com anúncio ativo identificado no snapshot; ruptura iminente que pode contaminar a série de leitura dos próximos dias conforme levantado pela Tática.

- **Pergunta:** o health do Kit 4 Potes de Vidro 1050ml Retangular caiu nos últimos 7 dias ou está estável em 0.75? — **motivada por:** sinal de health abaixo do limiar no segundo maior produto do dia; a distinção entre deterioração ativa e estabilidade em 0.75 determina se há perda de exposição orgânica em andamento ou apenas um teto de saúde que a campanha já está compensando.

- **Pergunta:** o Conjunto 5 Potes Tampa Vermelha (em catálogo, health 0.71) está perdendo posição para concorrentes no mesmo listing de catálogo? — **motivada por:** anúncio de catálogo com a pior saúde identificada entre os ativos; vulnerabilidade dupla (ranking próprio + Buy Box de catálogo) que a Granular pode verificar via posição relativa no catálogo MLB44224272.

- **Pergunta:** o anúncio do produto líder (Conjunto 5 Potes Tampa Preta, MLB4535865317) tem health disponível e qual é a posição de ranking atual? — **motivada por:** ausência de dado de health para o anúncio que carregou 24.4% dos pedidos do dia; sem essa informação, não é possível afirmar se a liderança é sustentada por exposição orgânica saudável ou compensada por campanha.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o GMV ou o ticket em si — é a **assimetria de qualidade logística no topo do mix**: o produto que mais vendeu (Conjunto 5 Potes Tampa Preta, 22 pedidos) opera em cross_docking, sem Frete Grátis e sem dado de health, enquanto os anúncios de fulfillment que sustentam o ticket elevado estão com health abaixo do limiar. Isso significa que a hierarquia de produto do dia não é a hierarquia de produto mais saudável da conta — é uma inversão operacional silenciosa que a Estratégica identificou como dependência de campeão, mas que hoje ganha uma camada adicional: o campeão não é o anúncio de melhor condição. Se a Condensadora carregar apenas o número (GMV acima do histórico, ticket elevado, sem cancelamentos), o risco operacional fica invisível. O ponto que merece atenção é: a conta está performando bem no número e fragilizando no mix de qualidade de anúncio — e a ruptura iminente do Kit Canequinhas com Suporte Acrílico é o único sinal que requer ação ainda hoje para não contaminar a série de observação dos próximos dias.