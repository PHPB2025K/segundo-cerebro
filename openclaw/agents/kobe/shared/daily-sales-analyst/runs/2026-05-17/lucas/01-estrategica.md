<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Memória das três contas é estrutural mas vazia de conteúdo: `weekly.md` e `monthly.md` são templates não populados; nenhum daily anterior está disponível no pacote. Não há hipóteses ativas, teses semanais ou mensais para confirmar ou refutar — as três contas começam do zero hoje. As janelas de 7d, 30d e 60d estão disponíveis e internamente consistentes para as três contas; o único flag de readiness é que Shop 3 operou 43.8% abaixo da banda de 30d (registrado como "partial" pelo pipeline). Base suficiente para leitura temporal comparada; insuficiente para validação de hipóteses históricas.

---

### Leitura temporal

**Store (Conta 1)**
- vs 60d: pedidos −23.5%, GMV −9.0% — a conta está abaixo do patamar do bimestre em volume, mas ticket +18.9% amortece a maior parte da queda de GMV.
- vs 30d: pedidos −10.1%, GMV +2.8% — estabilização relativa no mês; o ticket elevado sustenta o GMV próximo à média mensal apesar do volume menor.
- vs 7d: pedidos +17.7%, GMV +31.4% — recuperação expressiva frente à semana imediata, indicando que os dias anteriores foram particularmente fracos.
- vs mesmo dia da semana: pedidos −5.5%, GMV +6.2% — dentro da variação sazonal normal; sazonalidade não explica o afastamento do 60d.

**Oficial / Conta 2**
- vs 60d: pedidos −30.9%, GMV −28.4% — conta operando claramente abaixo do patamar do bimestre em todas as dimensões.
- vs 30d: pedidos −17.2%, GMV −23.3% — a queda se aprofunda na janela mensal, sem ticket compensando (ticket −7.3% vs 30d).
- vs mesmo dia da semana: pedidos −22.5%, GMV −26.9% — sazonalidade descartada como explicação; os sábados anteriores entregaram consistentemente acima de 20 pedidos.
- vs 7d: a média de 7d (21 pedidos) já está abaixo da de 30d (30.2) — a fraqueza recente é padrão acumulado, não evento pontual.

**Shop / Conta 3**
- vs 60d: pedidos −53.3%, GMV −54.6% — conta operando na metade do volume do bimestre; queda presente em todas as dimensões.
- vs 30d: pedidos −43.8%, GMV −47.7% — a queda não suaviza em janela mais curta.
- vs mesmo dia da semana: pedidos −43.4%, GMV −38.8% — os quatro sábados anteriores entregaram entre 23 e 30 pedidos; sazonalidade não explica a queda.
- vs 7d: −37.5% pedidos — e o próprio 7d (média 24 pedidos) já está abaixo do 30d (26.7) e do 60d (32.1) — a série de curto prazo já estava comprometida antes de ontem.

---

### Leitura estratégica

- **Store** opera em encolhimento de volume com sustentação de GMV via elevação de ticket — padrão que, se mantido nos próximos ciclos, configuraria acomodação num patamar inferior de pedidos com mix de maior valor médio. O risco é que a elevação de ticket reflita mix momentâneo, não estrutural: quando o Conjunto 5 Potes (que concentra ~49% dos pedidos da conta) oscilar, o GMV ficará exposto ao vácuo de volume deixado pelo 60d. A concentração de 89% nos top 3 não aparenta ser novidade, mas é o mecanismo que torna esse risco imediato.

- **Oficial / Conta 2** apresenta queda consistente em pedidos e GMV em todas as janelas relevantes (30d, 60d, mesmo dia da semana), sem mecanismo de compensação visível — diferente de Store, onde o ticket sobe para amortizar. A média de 7d já está abaixo da de 30d, sugerindo que a fraqueza não é de ontem. Hipótese (não confirmada): perda de exposição ou competitividade — mas sem dado de posição de anúncio ou ADS no pacote, não é verificável agora.

- **Shop / Conta 3** é o sinal mais grave do canal Shopee neste pacote. A série de curto prazo (7d) já estava abaixo do 30d, que por sua vez está abaixo do 60d — a deterioração é acumulada e não circunscrita a um dia. Soma-se a isso concentração total nos top 5 (100% dos pedidos), com o Kit 2 Potes 800ml Quadrado respondendo por 47% do volume: não há segundo vetor que absorva qualquer oscilação dos produtos ativos.

- As três contas **divergem**, o que inviabiliza leitura de plataforma como bloco. Store sustenta o GMV total (58% do GMV Shopee); Oficial e Shop contraem. O total agrega o que está sustentado e mascara o que está se deteriorando.

---

### Tese da conta

**Store — em acomodação.** O patamar de pedidos recuou em relação ao bimestre, mas o ticket elevado sustenta o GMV próximo à média de 30d. A conta opera num nível inferior em volume, compensado por mix de maior valor médio. Sem memória diária anterior, a tese é de ponto de partida — consistente com as janelas disponíveis, mas ainda sem confirmação de ciclo.

**Oficial / Conta 2 — vulnerável.** As quedas são consistentes entre janelas (30d, 60d, mesmo dia da semana) e não têm mecanismo de compensação. A média de 7d já está abaixo da de 30d, indicando que a fraqueza recente não é evento isolado. A conta está operando num patamar menor em todas as dimensões sem sinal de reversão identificável nos dados disponíveis.

**Shop / Conta 3 — em queda real.** Deterioração observável e alinhada em todas as janelas (7d < 30d < 60d), com a série de curto prazo já comprometida antes de ontem. Não se trata de um dia fraco numa conta estável — a contração está acumulada, sem segundo vetor operante e com concentração total nos top 5 produtos.

---

### Risco estrutural principal

**Risco:** Conta 3 (Shop) em deterioração consistente com concentração de 100% nos top 5 produtos e ausência completa de cauda — zero segundo vetor.

**Por que importa:** Uma conta sem cauda não absorve choque. O Kit 2 Potes 800ml Quadrado responde por 47% dos pedidos da conta; se esse produto perde ranking, exposição ou disponibilidade de estoque, não há produto substituto que sustente o volume. A deterioração já está estabelecida em 30d e 60d, o que significa que qualquer intervenção (ADS, cupom, precificação) opera sobre base já enfraquecida.

**Histórico:** Sem memória diária anterior disponível para esta conta — não é confirmável há quantas semanas essa deterioração está em curso. A sequência 7d < 30d < 60d nas médias de pedidos (24 < 26.7 < 32.1) sugere que o declínio é gradual e acumulado, não uma quebra abrupta recente.

**Sinal de confirmação:** GMV de Shop abaixo de R$1.100 com Kit 2 Potes 800ml Quadrado abaixo de 5 pedidos por 2 dos próximos 3 dias — confirmaria que a deterioração é estrutural e não está se revertendo.

---

### Sinais a observar

1. **Shop / Conta 3 — produto líder:** Kit 2 Potes de Vidro 800ml Quadrado abaixo de 5 pedidos por 2 dos próximos 3 dias confirmaria erosão de demanda ou exposição no produto que responde por quase metade do volume da conta — e descartaria a hipótese de que ontem foi um outlier dentro de uma base estável.

2. **Oficial / Conta 2 — patamar de GMV:** GMV abaixo de R$1.500 por mais 2 dias ao longo da semana, com ticket permanecendo abaixo de R$58 (vs média 30d de R$59.72), confirmaria que a conta estabeleceu uma nova faixa de patamar menor e não está em oscilação dentro da banda histórica.

3. **Store / Conta 1 — sustentação de ticket:** Ticket médio abaixo de R$40 por 2 dias seguidos indicaria que a elevação atual (R$44.55) não é estrutural — e nesse caso o GMV voltaria a ficar exposto à queda de volume, revelando patamar real abaixo da média de 30d.