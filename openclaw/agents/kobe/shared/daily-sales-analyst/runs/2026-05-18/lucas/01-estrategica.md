<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Memória sem histórico acumulado nas três contas — weekly e monthly são templates vazios sem entradas reais, rules sem exceções documentadas. Não há hipóteses anteriores ativas, sem diários anteriores carregados no pacote. Esta leitura é ponto de partida: todas as teses são de primeira geração, apoiadas apenas nos dados quantitativos das janelas históricas disponíveis (7d, 30d, 60d e mesmos dias da semana), sem âncoras de memória qualitativa. Confiança ajustada para moderada; teses mais fortes requerem confirmação nos próximos ciclos.

---

### Leitura temporal

- **Budamix Store (conta principal):** O dia ficou -27% vs 30d e -35,6% vs 60d em pedidos, mas o ticket subiu consistentemente (+8,5% vs 30d, +14,7% vs 60d), indicando que quem compra está comprando mais por pedido. Nos mesmos dias da semana, a queda é -27,6% — o dia não foi fraco apenas em termos absolutos, foi fraco para uma segunda-feira. A janela de 7d já mostrava desaceleração (-5,8% pedidos vs 7d), sugerindo que o enfraquecimento não é pontual de ontem, mas já está instalado há pelo menos uma semana. O 60d era mais alto que o 30d (91,6 vs 80,8 pedidos/dia), confirmando que a conta está em trajetória de queda de patamar, não oscilação dentro de banda estável.

- **Budamix Oficial (Conta 2):** Queda severa em pedidos (-47% vs 30d, -55,7% vs 60d), mas o GMV caiu bem menos (-13,3% vs 30d) e o ticket explodiu (+63,4% vs 30d). Isso indica que a conta está convergindo para transações de maior valor, com menor volume. Nos mesmos dias da semana, a queda é -53,3% em pedidos mas -26,6% em GMV — o padrão é consistente. Fenômeno já estava presente no 7d (pedidos -23,4%, GMV +21,6%), o que sugere que essa dinâmica de "menos pedidos, maior ticket" não é acidental de ontem: está se consolidando ao longo da semana recente.

- **Budamix Shop (Conta 3):** A queda aqui é a mais abrupta de todas — -58,5% vs 7d, -65,9% vs 30d, -71,7% vs 60d em pedidos. GMV segue o mesmo padrão de colapso (-49,7% vs 7d, -65,9% vs 60d). O ticket subiu levemente (+15,8% vs 30d), mas não compensa o volume perdido. Nos mesmos dias da semana, -62,1% pedidos e -58,3% GMV. A conta opera em múltiplas janelas muito abaixo de qualquer referência histórica. Não é ruído de um dia.

- **Padrão cross-conta:** As três contas caíram em volume, mas a magnitude e a natureza da queda divergem — Store caiu moderadamente e manteve ticket; Oficial colapsou em pedidos mas o GMV sustentou via ticket alto; Shop colapsou em ambas as dimensões. Isso afasta a hipótese de evento externo uniforme (campanha encerrada, bug de plataforma) e aponta para dinâmicas específicas por conta.

---

### Leitura estratégica

- **A Budamix Store está em desaceleração estrutural, não flutuação.** A queda acumulada de patamar entre 60d e 30d (91,6 → 80,8 pedidos médios) e a continuidade da queda na última semana e no dia fazem essa trajetória consistente em três janelas. O ticket subindo sugere que o problema não é de conversão em transações grandes, mas de volume total de tráfego ou exposição. A conta ainda representa a maior parte do GMV Shopee, então sua trajetória define o patamar da plataforma.

- **A Budamix Oficial está em transição de perfil, não em queda simples.** O colapso de pedidos com sustentação de GMV via ticket elevado — padrão já visível na semana — é hipótese de reposicionamento (deliberado ou de mercado): a conta está atraindo menos compradores, mas compradores de maior valor. Isso pode ser resultado de mudança de mix, ajuste de preços ou mudança de exposição. Sem confirmação da causa, a leitura é hipótese — mas o padrão é consistente nas três janelas disponíveis.

- **A Budamix Shop está em queda real, não acomodação.** Volume colapsado de forma consistente em 7d, 30d, 60d e mesmos dias da semana, sem compensação de ticket que sustente o GMV. A conta representa o menor volume das três, mas a magnitude da deterioração é a mais grave proporcionalmente. O risco aqui é que a conta esteja perdendo exposição ou relevância de forma acumulada — e sem memória histórica qualitativa, não há como distinguir se isso é deterioração recente ou crônica.

- **A concentração de produto é estrutural e onipresente.** As três contas apresentam top3 com 68–89% dos pedidos. Em Store e Shop, isso já gera quality flag de warning. A ausência de segundo vetor significa que qualquer oscilação nos campeões (Conjunto 5 Potes Redondos na Store, Kit 6 Canecas Tulipa nas contas menores) se traduz diretamente em oscilação de GMV. Esse risco já existia antes de ontem — mas a queda de volume nas três contas simultâneas o torna mais exposto.

---

### Tese da conta

**Shopee (plataforma, três contas) — em queda real, com gradação por conta.**

A trajetória é consistente em múltiplas janelas: o patamar de 60d era mais alto que o de 30d em todas as três contas, e o 7d está abaixo do 30d. O dia confirma a direção, não é o ponto de partida. A queda não é uniforme — Store cai moderadamente com ticket subindo, Oficial colapsa em volume com GMV parcialmente sustentado, Shop colapsa em ambas as dimensões. A tese de queda real é sustentada pela consistência temporal (60d → 30d → 7d → dia), não pelo dia isolado. Base de memória qualitativa é zero, o que reduz a confiança sobre *causas* — mas a direção dos números é inequívoca.

---

### Risco estrutural principal

- **Risco:** Concentração extrema em poucos produtos (top3 com 68–89% dos pedidos) nas três contas, sem segundo vetor estabelecido.
- **Por que importa:** Qualquer oscilação de exposição, estoque, preço ou competitividade nos campeões (Conjunto 5 Potes Redondos na Store, Kit 6 Canecas Tulipa nas contas menores) se traduz diretamente em queda de GMV sem amortecimento de cauda. Numa trajetória já descendente, esse mecanismo amplifica o impacto de qualquer choque externo.
- **Histórico:** Sem memória qualitativa acumulada, não é possível dizer se essa concentração é crônica ou recente. Os dados de produto disponíveis mostram o padrão hoje — a persistência histórica não está documentada.
- **Sinal de confirmação:** Concentração top3 acima de 75% na Store por mais 2 dias seguidos, combinada com queda de pedidos dos campeões específicos (Conjunto 5 Potes Redondos e Jarra Medidora 500ml), confirma que a concentração está piorando e é fator ativo na queda — não apenas padrão estático.

---

### Sinais a observar

1. **GMV diário da Budamix Store abaixo de R$ 2.200 por 2 dias seguidos** confirma que a desaceleração já ultrapassou a banda dos piores dias de 30d e está em novo patamar inferior — não oscilação.

2. **Pedidos da Budamix Oficial acima de 20/dia com ticket médio acima de R$ 90 por 3 dias seguidos** confirmaria a hipótese de transição de perfil (menos volume, maior valor) como padrão estabelecido, não flutuação de um ciclo.

3. **Pedidos da Budamix Shop abaixo de 12/dia por mais 3 dias seguidos** (vs média de mesmo dia da semana de 23,75) confirmaria queda estrutural de exposição ou posicionamento nessa conta — distinguindo erosão real de evento pontual.