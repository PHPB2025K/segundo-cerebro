<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O dia sustentou GMV sólido via ticket elevado (R$55.80), com volume essencialmente flat vs mesmo dia da semana (−1.6%). Operacionalmente, o resultado foi composto por dois motores distintos: o produto líder (Conjunto 5 Potes Tampa Preta, 24% dos pedidos) rodando em cross_docking, enquanto os itens que puxam ticket médio para cima (KIT4YW1050, KIT10YW1050) operam em Full. Isso confirma a leitura da Estratégica — o ganho de GMV vem do mix de valor, não de força de volume.

- O mix Full ontem nos top 10 caiu para 57.1% ante 77.7% no 7d, reflexo direto do produto campeão de volume operar fora do Full. Não é desvio crítico, mas reforça o alerta estratégico: a vantagem competitiva de Full está concentrada nos itens de ticket, não no líder de pedidos — qualquer perda de posicionamento nos itens Full (via health ou estoque) não vai aparecer no produto que mais vende, vai aparecer no GMV por pedido.

- Dois itens Full com tração real no dia estão com health abaixo do threshold: KIT4YW1050 (0.75, 13 pedidos, 2º lugar) e Conjunto 5 Potes Tampa Vermelha (0.71, 5 pedidos). Continuam vendendo agora, o que confirma o diagnóstico da Estratégica: a erosão de ranking ainda não se materializou em queda de vendas, mas o sinal precoce está presente. Esse é exatamente o padrão de deterioração silenciosa que a Tática indicou como prioridade de checagem.

- Um listing pausado com estoque zerado (Kit 06 Canequinhas com Suporte Acrílico, 914C_BAV) aparece com 3 pedidos no dia — comportamento operacionalmente atípico que não encontra explicação óbvia nos dados disponíveis.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 6 Tigelas (TL6250) com 20 unidades disponíveis em Full e 5 pedidos no dia; Kit 2 Potes 1050ml (KIT2YW1050) com 15 unidades disponíveis e 3 pedidos em 8 itens — **interpretação operacional:** cobertura de estoque Full de 4 dias para Tigelas e menos de 2 dias em itens para Kit 2 Potes, ao ritmo observado; ruptura em Full implica perda imediata do benefício logístico e descida de ranking orgânico — adiciona evidência concreta à ação que a Tática já recomendou.

- **Sinal:** 914C_BAV gerou 3 pedidos com listing pausado e estoque zerado — **interpretação operacional:** pedidos capturados antes do pause ou janela de indisponibilidade com sincronização defasada; se confirmados sem estoque, risco de cancelamento concentrado nesse item nos próximos dias — anômalo por natureza, mas isolado.

- **Sinal:** ADS atribuiu aproximadamente 60% do GMV do dia (R$3,041 de R$5,077) com ACOS de 4.33% — **interpretação operacional:** dependência de tráfego pago é relevante, mas a eficiência está bem calibrada; o risco latente é que, se health degradado forçar os anúncios Full a competirem mais por posição, o ADS vai sustentar exposição que antes era orgânica — custo pode subir antes de aparecer no ACOS.

- **Sinal:** produto líder de volume (Conjunto 5 Potes Tampa Preta, 22 pedidos) opera em cross_docking, enquanto os itens que sustentam o ticket operam em Full — **interpretação operacional:** a conta tem dois perfis logísticos ativos com funções distintas; se o ML priorizar exposição para itens Full, o produto líder de volume pode oscilar mais nos dias de menor demanda orgânica.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.** A performance agregada do dia está dentro do esperado — volume flat no mesmo dia da semana, GMV acima do histórico via ticket, sem queda de reputação, sem ruptura de estoque declarada. Dois desvios operacionais perceptíveis, mas isolados: (1) 914C_BAV com pedidos gerados em listing pausado com estoque zerado — atípico e potencialmente gerador de cancelamentos não planejados; (2) queda no mix Full ontem (57.1% vs 77.7% no 7d), explicável pelo perfil do líder de volume, mas que reduz a vantagem logística do dia. Nenhum dos dois compromete a execução hoje. O que elevaria para **anomalia moderada**: 914C_BAV confirmar cancelamentos por falta de estoque nos próximos dias, ou queda adicional do mix Full acompanhada de redução de pedidos nos itens de ticket.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** os 3 pedidos do 914C_BAV foram confirmados com estoque disponível ou estão em risco de cancelamento por ruptura? — **motivada por:** listing pausado com estoque zerado gerando pedidos no dia; comportamento atípico que pode resultar em cancelamentos concentrados e impacto pontual na métrica de cancelamento da conta.

- **Pergunta:** qual é a previsão de reposição para TL6250 e KIT2YW1050 no CD do ML? — **motivada por:** cobertura de estoque Full estimada em 2-4 dias para ambos ao ritmo atual; ruptura implica perda do benefício Full com impacto direto em ranking e na composição de GMV que a conta vem sustentando.

- **Pergunta:** o health score do KIT4YW1050 (0.75) está em deterioração ativa ou estabilizado nesse nível no 7d? — **motivada por:** item é o 2º maior vendedor do dia em Full e aparece como risco central da Estratégica; diferenciar deterioração em curso de patamar estável muda a urgência da ação tática recomendada.

---

### Destaque para a Condensadora

O GMV positivo e o ticket elevado tendem a dominar a leitura do dia, mas os dois riscos práticos que a Tática sinalizou se apresentaram com evidência concreta hoje: estoque Full em cobertura de 2-4 dias em itens ativos (TL6250 e KIT2YW1050) e um listing pausado com estoque zero gerando pedidos (914C_BAV) — ambos silenciosos na métrica agregada, mas com potencial de materialização em cancelamentos ou ruptura de Full nos próximos dias. O dia em si não trouxe fato operacional novo além do que a Estratégica e a Tática já mapearam, mas confirmou que os sinais de risco não são hipotéticos: estão visíveis nos dados de ontem. A Condensadora deve garantir que esses dois pontos operacionais cheguem a Yasmin com concretude, sem ficarem mascarados pelo número positivo de GMV.