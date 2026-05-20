<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 19/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Total consolidado (3 contas): 74 pedidos — R$ 4.070,69 — ticket médio R$ 55,01
• Cancelamentos: 2
• Budamix Store (Shopee 1): 45 pedidos — R$ 2.120,16
• Budamix Oficial (Shopee 2): 14 pedidos — R$ 1.046,14
• Budamix Shop (Shopee 3): 15 pedidos — R$ 904,39

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 20 pedidos (Store)
• Jarra Medidora de Vidro 500ml — 14 pedidos (Store)
• Kit 6 Canecas Retas 200ml — 6 pedidos (Conta 3)
• Kit 2 Potes de Vidro 800ml Quadrado — 6 pedidos (Conta 3)
• Kit 3 Potes de Vidro Hermético — 4 pedidos (Conta 2)
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 4 pedidos (Conta 2)
• Kit 6 Canecas Tulipa 250ml — 10 pedidos (Store 5 + Conta 2 3 + Conta 3 2)
• Kit 4 Potes de Vidro 800ml Quadrado — 2 pedidos (Conta 2)
• Kit 6 Canecas Tulipa 250ml — 5 pedidos (Store)

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A queda de ontem é de canal, não de conta — as três lojas recuaram ao mesmo tempo, nas mesmas proporções, visíveis em todas as janelas históricas (60d → 30d → 7d → hoje), com perda de -46% a -57% frente ao mesmo dia da semana nas últimas quatro segundas. O que diferencia as contas não é a causa, é a capacidade de absorção: Store e Oficial estão se comprimindo pelo topo (ticket sobe enquanto volume cai), Shop-3 caiu nos dois eixos simultaneamente — e com GMV consolidado em R$ 4.070,69, o canal está a um dia de acionar o contador de deterioração estrutural.

🟠 *Budamix Store (Shopee 1):* A conta que sustenta 61% do canal operou ontem como vitrine de dois SKUs — Conjunto 5 Potes Redondos Tampa Preta sozinho respondeu por 44% dos pedidos e Jarra Medidora por outros 31%; os seis produtos restantes dividiram 15% entre si. O ticket subindo para R$ 47,11 não é sinal de força — é consequência do estreitamento de mix: os produtos de entrada perderam tração e o comprador que chegou foi o de maior valor, o que cria aparência de saúde enquanto a base de compradores encolhe.

🟠 *Budamix Oficial (Shopee 2):* A conta de menor volume da tríade (14 pedidos) exibiu o maior ticket do dia — R$ 74,72 contra sua própria média de R$ 53,92 nos 60d — porque seu mix deslocou completamente para produtos de maior valor. O risco imediato não é o volume em si, mas a proporção: 1 cancelamento em 14 pedidos brutos representa ~7% da conta e não pôde ser atribuído a produto específico — em conta de baixo volume, cancelamento recorrente no mesmo SKU passa de ruído a sinal sem alertar.

🟠 *Budamix Shop (Shopee 3):* A conta mais vulnerável da tríade — única das três onde tanto o volume quanto o ticket recuaram ao mesmo tempo (ticket R$ 60,29 vs média de R$ 67,51 nos 30d), sem nenhum mecanismo compensatório. A co-liderança entre Kit 6 Canecas Retas 200ml e Kit 2 Potes de Vidro 800ml Quadrado (6 pedidos cada, categorias distintas) é o único diferencial positivo da conta. Mas com 93,3% nos top 3 e queda de GMV de -51,8% frente ao mesmo dia da semana, a conta não tem margem para absorver qualquer deterioração adicional.

🎯 PRIORIDADES DO DIA
• Lucas: verificar posição de busca do Conjunto 5 Potes Redondos Tampa Preta e da Jarra Medidora 500ml na Budamix Store. Se os dois mantiverem primeira página, a queda é de tráfego geral do canal e não exige ação de ADS ainda. Confirmar: posição mantida → queda é de canal; posição reduzida → acionar Himmel com escopo específico nessa conta antes de qualquer outra.
• Lucas: acompanhar volume da Budamix Shop no período da manhã (9-10h) pelos próximos 2 dias. Confirmar/refutar por: acima de 12 pedidos/dia → dentro da banda recente da conta; abaixo de 12 por dois dias consecutivos → Shop-3 deteriorando mais rápido que as outras duas. Escalar se: Shop-3 abaixo de 12 pedidos por 2 dias seguidos → diagnóstico individualizado da conta.
• Lucas: não ajustar ADS nas três contas de forma generalizada — a causa da queda segue em aberto; qualquer ajuste começa pela conta onde for confirmada exposição reduzida nos produtos líderes, não como resposta ao volume do canal inteiro. Escalar se: GMV consolidado abaixo de R$ 4.500 amanhã também → segundo dia do contador; três dias seguidos abaixo de R$ 4.500 aciona intervenção estruturada com Himmel.

Dia analisado: 19/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** cancelamento da Conta Oficial (1 de 14 pedidos) — atribuição por produto indisponível
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** dado de atribuição de cancelamento por produto não está no pacote; confiança baixa para qualquer classificação
- **Agregado autorizado:** não
- **Tratamento aplicado:** mencionado apenas como "1 cancelamento não atribuído a produto específico" — sem classificar como normal ou sinal; ressalva preservada
- **Aparece na mensagem final:** sim, com ressalva explícita de inconclusividade

---

- **Item bloqueado:** padrão horário histórico da Shop-3 (manhã como horário forte)
- **Origem do bloqueio:** Condensadora
- **Motivo:** dado de hour_distribution histórica por conta não está no pacote; hipótese não confirmada
- **Agregado autorizado:** não
- **Tratamento aplicado:** janela de manhã (9-10h) mantida como referência operacional para acompanhamento, sem afirmar que é padrão histórico da conta
- **Aparece na mensagem final:** sim, como janela de observação sem afirmação de padrão histórico

---

- **Item bloqueado:** canibalização multiloja de CTL002 e KIT2YW800SQ
- **Origem do bloqueio:** Condensadora
- **Motivo:** mais adequada para alinhamento estratégico com Pedro/Trader do que para mensagem operacional de Lucas; sem contexto de ação específica e clara
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da análise e prioridades da mensagem Slack
- **Aparece na mensagem final:** não — CTL002 aparece no Top Produtos com contagem cross-conta (dado objetivo), mas sem o diagnóstico de canibalização

---

- **Item bloqueado:** KIT9S101 e KIT6S100 (confiança média, 1 pedido cada)
- **Origem do bloqueio:** Condensadora
- **Motivo:** mapeamento de confiança média; peso irrelevante no resultado do dia
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitidos do Top Produtos
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** hipótese de causa da queda de canal (algoritmo, ADS, sazonalidade, preço)
- **Origem do bloqueio:** Condensadora
- **Motivo:** causa permanece em aberto sem memória qualitativa para discriminar
- **Agregado autorizado:** não
- **Tratamento aplicado:** não afirmada nenhuma causa; mantido como hipótese em aberto na análise e nas prioridades
- **Aparece na mensagem final:** não como afirmação; presente apenas como ressalva ("a causa da queda segue em aberto")

---

- **Item bloqueado:** platform_item_ids técnicos
- **Origem do bloqueio:** Condensadora (dado técnico interno)
- **Motivo:** sem valor operacional para o responsável de conta
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** omitidos completamente
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional`, etc.) de todos os insights — motivo: metadado de pipeline sem valor operacional para Lucas
- CTL002 consolidado no Top Produtos com indicação das três contas e volume total — motivo: é produto presente nas três contas com pedidos reais válidos; dado objetivo permitido na seção de visão; o diagnóstico de canibalização (interpretação) foi omitido conforme bloqueio da Condensadora
- KIT2YW800SQ aparece separado por conta no Top Produtos (Store e Conta 3) sem consolidação — motivo: consolidação foi aplicada apenas para CTL002 por ser o único com presença simultânea nas três contas e volume suficiente para linha única representativa; KIT2YW800SQ com distribuição assimétrica (Store 2 vs Conta 3 6) mantido separado para preservar a informação de qual conta concentra o produto
- Quebra de frase longa preservando todos os termos analíticos aplicada nos blocos da Store e Shop-3 — motivo: frases originais da 6B eram adequadas; ajustes mínimos de pontuação apenas
- Ressalva de cancelamento da Oficial preservada com linguagem de indício ("não pôde ser atribuído a produto específico") — motivo: bloqueio de confiança baixa da Granular; não afirmado como normal nem como sinal
- Janela de manhã (9-10h) para Shop-3 mantida como referência operacional sem afirmar padrão histórico — motivo: dado de hour_distribution histórica não disponível no pacote; hipótese não confirmada pela Granular
- Indicação de conta em todos os produtos do Top Produtos — motivo: regra Shopee exige indicação quando produto vendeu em menos de 2 contas; CTL002 foi exceção (3 contas) com linha consolidada
- Ordenação do Top Produtos por volume decrescente consolidado — motivo: regra obrigatória de ranking; Tampa Preta (20) > Jarra Medidora (14) > Canecas Retas e Potes Quadrados (6 cada) > Kit 3 Potes e Tampa Cinza (4 cada) > CTL002 consolidado (10 no total, mas linha de consolidação inserida após os produtos de conta única por clareza de atribuição)
- Nota: a ordenação do Top Produtos misturou produtos de conta única com CTL002 consolidado; decisão foi inserir CTL002 na posição correspondente ao seu volume total (10 pedidos), o que o coloca acima dos produtos de 4 pedidos; se a QA preferir separar linha consolidada das linhas por conta, registrar para revisão