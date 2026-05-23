<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **O GMV do dia foi integralmente sustentado por ticket, não por volume:** 84 pedidos estão -15,4% abaixo da média 30d (99,3) e -17,6% abaixo da média das sextas anteriores (102,0), enquanto o GMV de R$4.622,03 supera a média 30d em +3,4% e fecha a -2,1% vs mesmas sextas — dentro da banda. Ticket médio de R$55,02 está +22,3% vs 30d e +29,8% vs 60d. Isso confirma operacionalmente o que a L01 identificou como dinâmica central da conta: patamar de GMV sustentado por crescimento de valor médio por pedido, sem expansão de alcance. O dia não adiciona informação nova à tese — reproduz o padrão com fidelidade.

- **A família IMB501 carregou 44% do volume e distorceu o mix de modalidade de envio por composição interna:** Tampa Preta (Cross-Docking, 20 pedidos) + Tampa Vermelha (Full, 10 pedidos) + Tampa Cinza (Cross-Docking, 7 pedidos) = 37 pedidos. Os dois membros Cross-Docking da família puxaram o `fulfillment_mix_yesterday_top10.full_pct` para 47,1%, inversão de 27,8 p.p. em relação ao histórico 7d (74,9%) e 30d (73,7%). A divergência é produto-específica e confirma operacionalmente a hipótese de composição da L01: a família IMB501 não tem dominância modal uniforme entre variações — quando as cores Cross-Docking lideram, o mix de modalidade de envio dos campeões cai estruturalmente, sem que isso signifique mudança de perfil da conta.

- **Três dos maiores anúncios em Full apresentam vulnerabilidade operacional simultânea, invisível no resultado agregado:** Kit 4 Potes 1050ml (health=0,75, 11 pedidos) e Conjunto 5 Potes Tampa Vermelha (health=0,71, 10 pedidos) operam penalizados abaixo do limiar ML de 0,85 — 21 pedidos combinados (25% do volume), ambos em Full. O Kit 6 Canecas Porcelana Tulipa Lisa 250ml (Full, 6 pedidos) tem `available_quantity=9` no snapshot pós-baixa: ao ritmo de 6 pedidos/dia, cobertura prospectiva de ~1,5 dia. A coexistência de health degradada nos dois campeões Full de maior volume e estoque crítico no terceiro anúncio Full em atividade é o ponto que adiciona evidência ao risco apontado pela L01 — o orgânico residual da conta (~30% do GMV) está concentrado em anúncios em Full operacionalmente pressionados.

- **ADS respondeu por 69,9% do GMV com eficiência elevada, confirmando a dependência estrutural apontada pela L01:** `ads_summary.revenue_ads_yesterday_brl=R$3.228,78` / GMV R$4.622,03 = share 69,9%; gasto R$296,96; ROAS 10,87x; ACOS 4,57%. Orgânico residual estimado ~R$1.393 (~30%). A campanha sustenta o dia com eficiência notável — mas a convergência entre ADS dominante e Full pressionado significa que o canal funciona bem com todos os elementos ativos e eficientes; a margem para absorver perturbação (ruptura de estoque em Full, pausa técnica de campanha, queda de health) é estreita.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, Full, ativo) com `available_quantity=9` pós-baixa e 6 pedidos ontem — cobertura prospectiva de ~1,5 dia — **interpretação operacional:** qualquer pedido além do estoque disponível nos próximos dias gera cancelamento automático pelo ML, pressionando `cancellations_rate` (hoje em 0 na janela longa) e potencialmente pausando o anúncio em Full; o gatilho de verificação definido pela L02 (quantidade < 5 = reposição urgente) está a menos de um ciclo de ser ativado.

- **Sinal:** Kit 4 Potes 1050ml Azul-petróleo (health=0,75) e Conjunto 5 Potes Tampa Vermelha (health=0,71) — os dois maiores anúncios em Full — somam 21 pedidos (25% do dia) operando com health penalizada, ambos sem trajetória confirmada (segundo ponto da série, conforme L05/weekly) — **interpretação operacional:** a exposição orgânica desses anúncios está sendo progressivamente reduzida pelo ML; o fato de ainda figurarem no top3 é sustentado pelo sold_quantity acumulado (977 e 5.738, respectivamente), não por health recuperada — isso significa que o buffer de ranqueamento existe hoje mas não é renovável se a health continuar deteriorando.

- **Sinal:** Mix de modalidade de envio dos top10 do dia em Full 47,1% vs histórico 7d 74,9% — diferença de 27,8 p.p. causada pela família IMB501 com peso nas variações Cross-Docking (Tampa Preta 20 pedidos + Tampa Cinza 7 pedidos = 32,1% do volume total) — **interpretação operacional:** o desvio é de composição, não estrutural; mas quando a família IMB501 dominar o dia, o `fulfillment_mix_yesterday_top10.full_pct` naturalmente ficará deprimido — a Condensadora precisa separar esse efeito composicional de um eventual movimento real de migração Cross-Docking, para não gerar falso alarme de mudança de perfil da conta.

- **Sinal:** Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades (MLB6739241224, Cross-Docking) com `available_quantity=6` pós-baixa e 2 pedidos ontem — cobertura prospectiva estimada em ~3 dias ao ritmo histórico típico — **interpretação operacional:** não é urgência hoje, mas está na mesma zona de atenção do Kit 6 Canecas Tulipa; se os dois atingirem estoque zerado nos próximos 2 ciclos simultaneamente, funcionam como variável confundidora para o GMV e o mix dos dias seguintes.

- **Sinal:** 1 cancelamento do dia contra `reputation.cancellations_rate=0` na janela longa ML — **interpretação operacional:** evento isolado, sem impacto na reputação hoje. A relevância é preventiva: se o Kit 6 Canecas Tulipa começar a gerar cancelamentos automáticos por ruptura nos próximos dias, esse contador começa a se mover — e o cancelamento de ontem passa a ser retrospectivamente o primeiro ponto de uma série, não um episódio isolado.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.**

O resultado agregado do dia foi normal: GMV dentro da banda 30d e -2,1% das sextas, reputação verde (5_green), nenhum anúncio pausado com pedidos, 1 cancelamento isolado contra `cancellations_rate=0` histórico. Os desvios são no perfil de execução, não no número: mix de modalidade de envio invertido por composição da família IMB501, health penalizada nos dois campeões Full de maior volume, e estoque crítico prospectivo no Kit 6 Canecas Tulipa. Os três sinais são independentes entre si — não têm causa comum que sugira problema sistêmico — e nenhum bloqueou ou comprometeu a execução do dia analisado. Para subir para anomalia moderada seria necessário: Kit 6 Canecas Tulipa pausado com pedidos pendentes, ou health em queda documentada (terceiro ponto com vetor negativo confirmado), ou segundo cancelamento ligado a ruptura de estoque. Nenhuma dessas condições se materializou em 22/05.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual é a `available_quantity` atual do Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090) e o `status` permanece `active`? — **motivada por:** estoque pós-baixa de 9 unidades com ritmo de ~6 pedidos/dia = ~1,5 dia de cobertura prospectiva; gatilho de verificação imediata definido pela L02; queda abaixo de 5 ativa ação de reposição urgente antes que o ML pause automaticamente.

- **Pergunta:** Qual é a direção atual do `health` do Kit 4 Potes 1050ml Azul-petróleo (MLB4073003575, health=0,75) e do Conjunto 5 Potes Tampa Vermelha (MLB3288536143, health=0,71) — caindo, estável ou em recuperação em relação ao ponto anterior? — **motivada por:** L01 confirmou "segundo ponto da série" em ambos; a direção — não o valor absoluto — é o que desbloqueia ou descarta o alinhamento de Yasmin com Himmel sobre cobertura preventiva no próximo ciclo.

- **Pergunta:** Qual é a composição do `revenue_ads_yesterday_brl` (R$3.228,78) por anúncio — Himmel estava priorizando a família IMB501 (que liderou em Cross-Docking) ou o resultado dessas variações foi majoritariamente orgânico? — **motivada por:** ADS share de 69,9% com inversão do mix de modalidade de envio dos campeões; se a campanha está empurrando as variações Cross-Docking da IMB501, o ADS está gerando volume em modalidade de envio menos favorável que o histórico mensal — o que muda a leitura de onde o orgânico real está operando e o que os ~30% de GMV orgânico efetivamente representam.

- **Pergunta:** `available_quantity` atual do Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades (MLB6739241224, Cross-Docking) — pós-baixa estava em 6 unidades com 2 pedidos ontem — cobertura prospectiva ~3 dias? — **motivada por:** dois produtos simultâneos com estoque próximo de zero nos próximos 2 ciclos funcionam como variável confundidora para GMV e mix — vale confirmar posição antes do próximo pacote para não confundir ruptura com queda orgânica.

---

### Destaque para a Condensadora

O resultado agregado do dia (GMV dentro da banda, reputação verde, ROAS excepcional) não revela o que está acontecendo no substrato operacional: os três maiores anúncios em Full da conta operam pressionados simultaneamente — dois com health penalizada sem trajetória confirmada, um com estoque prospectivo de ~1,5 dia. O orgânico residual da conta, estimado em ~30% do GMV, está concentrado exatamente nesses anúncios em Full. Isso significa que a dependência de ADS documentada pela L01 (69,9% do GMV) é ainda mais estrutural do que o número sugere: o canal não tem um segundo vetor orgânico saudável em reserva caso algum desses anúncios saia do ar ou perca posição por health. A Condensadora deve avaliar se esse risco silencioso entra na mensagem ao lado do dado positivo de ticket — a L02 já definiu o Kit 6 Canecas Tulipa como gatilho de ação imediata para Yasmin, o que torna pelo menos esse item candidato a menção direta sem alarmar desnecessariamente sobre os demais.