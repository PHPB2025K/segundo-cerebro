<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly.md e monthly.md são templates vazios sem nenhuma entrada acumulada — não há tese semanal, tese mensal, hipóteses ativas nem padrões registrados para confirmar ou refutar. A base numérica (7d/30d/60d, mesmo dia da semana) está disponível e populada com 60 dias de histórico, o que sustenta leitura temporal sólida. O data quality check flagou o volume Amazon como "partial" por spike positivo atípico — não é bloqueio, mas reduz a confiança em leituras de curtíssimo prazo. Sem memória interpretativa acumulada, esta leitura serve como ponto de partida, não como confirmação de tese pré-existente.

---

### Leitura temporal

- **Trajetória progressiva entre janelas:** A média de pedidos segue escada consistente — 60d: 26,6 → 30d: 28,5 → 7d: 34,9 → hoje: 45. Cada janela está acima da anterior. Esse padrão cruzado em três horizontes distintos é o sinal mais robusto disponível e sugere aceleração sustentada, não oscilação.

- **Mesmo dia da semana reforça o sinal:** As quatro últimas segundas-feiras (22, 24, 33, 29) têm média de 27 pedidos e mostram tendência de alta nas duas mais recentes (33 e 29). Hoje, com 45, está 67% acima da média dos pares sazonais — expressivo, e coerente com a aceleração observada nas janelas maiores.

- **Ticket estável em todas as janelas (~R$40-41):** O crescimento de GMV está sendo inteiramente conduzido por volume, sem mudança de mix de preço. Isso é relevante: o ticket não está comprimindo (o que sinalizaria problema de composição) nem inflado (o que sinalizaria evento pontual de produto caro).

- **Sem hipóteses anteriores para testar:** A ausência de weekly/monthly impede confirmar ou refutar qualquer tese pré-existente. As leituras que seguem são construção primária, não validação.

---

### Leitura estratégica

- **A aceleração entre janelas tem consistência suficiente para ser lida como trajetória.** Quando 7d > 30d > 60d de forma monotônica — em pedidos, GMV e mesmo dia da semana — o movimento deixa de ser ruído e começa a parecer mudança de patamar. Um único dia atípico num histórico de média estável seria ponto fora; aqui, o próprio histórico recente já estava elevado antes de hoje.

- **A conta está sendo sustentada por dois produtos.** Conjunto 5 Potes Preta e Jarra Medidora de Vidro 500ml somam 24 dos 45 pedidos (~53%), com concentração top-3 em 60%. Isso não é leitura negativa do dia — é a estrutura da conta. Em qualquer cenário de crescimento, essa dependência significa que o patamar alto é frágil por construção: pertence aos dois campeões, não à conta.

- **100% FBA com ticket estável é o lado operacionalmente saudável desse quadro.** Sem fragmentação entre FBA/FBM, sem compressão de ticket, sem cancelamentos relevantes (2 de 47 transações). A operação não está pressionada onde os dados conseguem enxergar.

- **A ausência de memória interpretativa é, por si só, um dado.** Sem registro de como a conta chegou a esse patamar, não é possível distinguir se a aceleração é recente, se já foi mais alta antes, ou se há ciclos sazonais documentados. A leitura de hoje é a primeira âncora interpretativa da série.

---

### Tese da conta

**Em ganho de patamar — confiança moderada.**

A conta apresenta sinal consistente de subida estrutural visível em 60d, 30d, 7d e mesmo dia da semana — quatro janelas que convergem na mesma direção, com ticket estável e operação FBA íntegra. A tese de ganho de patamar é a mais honesta com os dados disponíveis. A confiança é moderada (não alta) porque a memória interpretativa está zerada — não há registro de como se chegou aqui, se isso já aconteceu antes ou se existe um teto observado no histórico que o dado numérico puro não revela.

---

### Risco estrutural principal

**Risco:** Concentração estrutural em dois ASINs (Conjunto 5 Potes Tampa Preta + Jarra Medidora 500ml) que respondem por ~53% dos pedidos do dia, dentro de um top-5 que concentra 71% do volume.

**Por que importa:** O patamar de crescimento que a tese identifica não pertence à conta de forma distribuída — pertence a dois produtos. Qualquer disrução em Buy Box, FBA, estoque ou listing de um desses ASINs derruba o patamar diretamente, sem segundo vetor que absorva. Crescimento sobre base concentrada é frágil por definição.

**Histórico:** Não há registro anterior para determinar se essa concentração é padrão crônico da conta ou aumento recente. Este é o primeiro registro.

**Sinal de confirmação:** Se a concentração dos top-2 se mantiver acima de 50% dos pedidos por mais dois ciclos semanais (próximas duas segundas), a dependência deixa de ser leitura de um dia e passa a ser padrão documentado da conta.

---

### Sinais a observar

1. **Sustentação da trajetória na semana:** Se o GMV diário se mantiver acima de R$1.400 por pelo menos 4 dos próximos 6 dias, a tese de ganho de patamar se consolida — deixando de ser padrão emergente para ser nova linha de base da conta.

2. **Concentração dos campeões:** Se Conjunto 5 Potes Preta e Jarra Medidora continuarem acima de 10 pedidos combinados por mais 2 dias nos próximos 5, a dependência estrutural nos dois ASINs fica confirmada como característica da conta, não evento do dia.

3. **Buy Box e disponibilidade dos ASINs líderes (se disponível no pacote):** Qualquer degradação de Buy Box abaixo de 85% nos dois ASINs campeões por 2 dias consecutivos constitui risco imediato ao patamar identificado — e inviabiliza qualquer discussão de escala de ADS antes de resolução.