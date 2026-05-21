<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Base operacional sólida: janelas 7d/30d/60d e mesmos dias da semana disponíveis e populados; ML Snapshot com reputação, mix fulfillment, health dos anúncios e ADS summary. Ponto fraco relevante: weekly.md e monthly.md são templates vazios — não há teses consolidadas nem hipóteses ativas anteriores para confirmar ou refutar. A leitura de hoje é base inaugural, não confirmação de tese madura.

---

### Leitura temporal

- **vs mesmos dias da semana (4 comparações):** pedidos praticamente estáveis (-2.7% vs média 92.5), mas GMV +31.6% vs média R$3.841 e ticket R$56.19 vs R$41.53 histórico do dia (+35%). O descolamento pedidos/GMV é consistente nos 4 pares observados — o dia é normal em volume, anormal em receita por pedido.

- **vs 30d:** pedidos abaixo (-9.9%), GMV acima (+15%), ticket +27.6%. A conta não está ganhando volume no mês — está ganhando receita por pedido. O padrão não é crescimento amplo.

- **vs 60d:** pedidos neutros (-1.3%), GMV +32.5%, ticket +34.2%. Em dois meses, o canal dobrou a expansão de GMV sem crescimento proporcional de pedidos. Isso não é acomodação dentro de uma banda — é uma elevação consistente de ticket ao longo do bimestre.

- **vs 7d:** pedidos -21.8%, GMV -4.9%. A semana recente teve dias de volume mais alto (média 115 pedidos). Hoje está abaixo dos picos recentes, mas o ticket elevado amorteceu o GMV. O 7d mais alto em pedidos + ticket hoje mais alto cria distorção: o 7d mede um período com mais pedidos em ticket menor; hoje inverte a proporção.

---

### Leitura estratégica

- **Lente 1 — Patamar vs banda:** A conta não ganhou patamar em pedidos — está dentro da banda 30/60d em volume. O que saiu da banda é o ticket médio, de forma consistente em múltiplas janelas. Isso não é pico isolado: é padrão bimestral de elevação de valor por pedido. A questão é se esse padrão é sustentável ou é produto do mix de campanha ADS ativo.

- **Lente 2 — Exposição vs faturamento:** Reputação verde (5_green), Mercado Líder Gold, zero cancelamentos na métrica de reputação. Exposição estrutural intacta. A queda em pedidos vs 7d não tem correlato operacional — hipótese é ciclo de demanda dentro da semana, não erosão de exposição. Confirmação: se pedidos voltarem a 100+ nos dias úteis fortes sem mudança de campanha, é sazonalidade.

- **Lente 3 — Dependência e fulfillment:** O top seller do dia (Conjunto 5 Potes Tampa Preta, 24.4% dos pedidos) é cross_docking e sem Frete Grátis. O mix fulfillment do dia (57% Full / 43% cross_docking) divergiu significativamente do padrão 7d (78% Full / 22% cross_docking) por conta desse peso do líder. A conta tem 82 anúncios ativos, mas na prática o resultado é carregado pelos mesmos 2-3 SKUs — top 3 com 47.8% dos pedidos. Dependência crônica confirmável, mas sem histórico consolidado, ainda é hipótese forte.

- **Lente 5 — ADS vs orgânico:** Himmel gerou R$3.041 de R$5.057 de GMV — cerca de 60% da receita do dia, com ACOS de 4.33%. A campanha está eficiente, mas a proporção ADS/total é alta. **Hipótese:** a elevação do ticket está associada ao mix de produto que as 11 campanhas ativas estão priorizando (itens de maior valor como Kit 4 Potes 1050ml em #2). Se confirmado, o GMV expandido não é orgânico — é amplificação ADS sobre demanda selecionada. Sem dado de share ADS por produto, essa hipótese não pode ser resolvida hoje.

---

### Tese da conta

**Acomodação com trajetória de elevação ticket-driven.** Em 60 dias, o GMV subiu +32.5% sem crescimento de pedidos (-1.3%), padrão que aparece consistentemente no controle por dia da semana (+31.6% GMV vs -2.7% pedidos). A conta não ganhou alcance — ganhou valor por pedido. Reputação verde e Mercado Líder Gold sustentam a exposição estrutural, portanto a expansão não está sendo ameaçada por deterioração operacional visível. O ponto de tensão é a dependência de ADS (~60% do GMV em um único dia): ainda não é possível separar se o ticket elevado é preferência orgânica de compra ou produto de campanha orientada a itens de maior valor. Sem semanas consolidadas, a tese fica em **acomodação** — não vulnerável no número, mas com dependência de ADS não validada como estrutural.

---

### Risco estrutural principal

**Risco:** Expansão de GMV sustentada por ticket elevado com ~60% de contribuição ADS — sem confirmação de que o orgânico sustenta o patamar de forma independente.

**Por que importa:** Se Himmel ajustar verba, campanhas ou mix de produto impulsionado, o ticket pode normalizar para a faixa histórica (~R$41-44) e o GMV contrai para a banda de pedidos atuais — em torno de R$3.800-4.000, não R$5.000+. Crescimento de receita que depende de ADS para sustentar ticket não é ganho estrutural de canal.

**Histórico:** Não há histórico consolidado (weekly/monthly vazios). Padrão identificado hoje pela primeira vez como hipótese emergente a partir da consistência bimestral dos dados de ticket.

**Sinal de confirmação:** GMV acima de R$4.800 em pelo menos 3 dos próximos 5 dias com spend ADS abaixo de R$180 confirmaria que o orgânico tem base independente. Se o GMV cair abaixo de R$4.000 em dia de spend reduzido, hipótese de dependência ADS vira confirmação.

---

### Sinais a observar

1. **Ticket médio abaixo de R$46 por 2 dias seguidos** confirmaria que a elevação bimestral é ADS-sustentada e não preferência de compra orgânica — e a tese de acomodação saudável passaria a vulnerável.

2. **Kit 4 Potes de Vidro 1050ml Retangular com health abaixo de 0.75 ou saindo do top 3 por 3 dias consecutivos** confirmaria deterioração de ranqueamento do segundo maior anúncio — relevante porque é o produto que mais contribui para o ticket elevado (fulfillment, sem Frete Grátis, health já em 0.75 hoje).

3. **Kit 06 Canequinhas de 100ml com Suporte Acrílico com estoque zerado** — disponível_quantity está em 3 unidades; ruptura iminente. Se o anúncio for pausado por estoque nos próximos 1-2 dias, confirma vulnerabilidade de cauda com exposição ativa sem backup de reposição.