<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly.md e monthly.md chegam como templates sem conteúdo — sem tese semanal nem mensal consolidada para confrontar. O daily de ontem (2026-05-20) está carregado como chave de memória mas seu conteúdo não é acessível nesta sessão. A base ML específica chegou completa (`ml_snapshot` com reputação, MercadoLíder, mix de modalidade de envio e ads_summary disponíveis) e a série histórica de 59 dias cobre adequadamente 30d e 60d. Hipóteses anteriores ficam sem ancoragem formal — a leitura de hoje constrói referência, não confirma tese pré-existente.

---

### Leitura temporal

- **Trajetória de 60d e 30d indica elevação de patamar em GMV, com ticket como motor.** GMV do dia (R$ 6.113) está +57,7% vs `avg_60d` (R$ 3.877) e +38,7% vs `avg_30d` (R$ 4.407). Pedidos, contudo, crescem muito menos: +7,9% vs 60d, +1,7% vs 30d. O ticket médio segue trajetória contínua de alta em todas as janelas: R$ 41,44 (60d) → R$ 44,36 (30d) → R$ 47,25 (7d) → R$ 60,52 (hoje). Não é pico isolado; a subida de ticket está se consolidando ao longo de três janelas distintas.

- **7d mostra inversão entre pedidos e GMV.** Vs 7d, pedidos caíram -15,1% (`changes.orders_vs_7d_pct`) enquanto GMV subiu +8,8% (`changes.gmv_vs_7d_pct`). A semana recente operou com média de 118,9 pedidos/dia e ticket de R$ 47,25 — hoje o dia tem 101 pedidos mas ticket de R$ 60,52. A hipótese é de rotação de mix: a família IMB501 (Potes de Vidro Redondos) domina hoje em unidades, mas o Kit 10 Potes 1050ml (16 pedidos) e o ticket médio mais alto sugerem que o peso de produtos de maior valor subiu.

- **Controle de dia da semana confirma GMV excepcional, volume normal.** A média das últimas 4 quintas-feiras equivalentes é 102,75 pedidos / R$ 4.686 (`same_weekday_avg`). Hoje: 101 pedidos (−1,7%) / R$ 6.113 (+30,5%). O volume de pedidos está exatamente dentro do esperado para uma quinta — a excepcionalidade do resultado está inteiramente no ticket, não em alcance.

- **Mix de modalidade de envio do dia diverge dramaticamente da janela 7d/30d.** Os top 10 de ontem concentram 80,2% dos pedidos em Cross-Docking (`fulfillment_mix_yesterday_top10.cross_docking_pct`), invertendo a dominância de Full observada nos últimos 7 dias (Full: 77,0%, `fulfillment_mix_7d.full_pct`) e 30 dias (Full: 73,6%). Os campeões do dia são da família IMB501, todos em Cross-Docking — enquanto os anúncios habitualmente líderes em Full (Kit 4 Potes com `logistic_type=fulfillment`) cederam espaço. Esse desvio na composição do dia versus a série de 7d/30d é sinal de rotação temporária de campeões, não de mudança de operação.

---

### Leitura estratégica

- **O canal subiu de patamar em faturamento, mas o mecanismo é ticket e não volume — e o ticket depende da composição do dia.** A trajetória contínua de ticket em todas as janelas (+46% vs 60d, `changes.ticket_vs_60d_pct`) confirma que o mix de produtos vendidos está se deslocando para itens de maior valor médio. Contudo, o controle de dia da semana mostra que pedidos não cresceram — a conta não está atingindo mais compradores, está capturando mais receita por pedido. Essa diferença importa estruturalmente: ticket elevado sustentado por concentração de produto específico é mais frágil do que ticket elevado por diversificação de portfólio.

- **ADS é o vetor dominante do canal, com eficiência elevada e fragilidade latente proporcional.** ADS gerou R$ 4.593,66 (`ads_summary.revenue_ads_yesterday_brl`) sobre gasto de R$ 341,72 — ROAS de 13,44x e ACOS de 4,71% (`avg_acos_pct`). Isso representa **75,1% do GMV do dia** (R$ 4.594 / R$ 6.113). O canal orgânico entregou aproximadamente R$ 1.519 — menos de 25% do total. Campanha eficiente mascara dependência: qualquer redução de verba por Himmel retira imediatamente três quartos do volume. Isso não é diagnóstico de operação doente — é mapeamento de fragilidade estrutural que coexiste com bom resultado.

- **A conta entra no dia com concentração alta e segundo vetor incipiente.** `top3_concentration` é 59,4% e `top5_concentration` é 76,2%. Os 3 primeiros são todos variações da família IMB501 (Conjunto 5 Potes Redondos) em Cross-Docking — o que significa que um único anúncio pai, com variações de cor, carrega mais de 50% do volume. A base ativa tem 84 anúncios vs 173 pausados (`account_overview.totals`), o que sinaliza cauda quase inativa. Sem dado semanal consolidado, não é possível afirmar se essa concentração é padrão histórico ou recente — mas ela é estruturalmente elevada.

- **Dois anúncios em Full apresentam sinais de vulnerabilidade imediata de estoque.** Kit 6 Canequinhas Acrílico (`MLB4410218897`, `logistic_type=fulfillment`, `available_quantity=1`) registrou 3 pedidos com estoque de 1 unidade — ao menos 2 desses pedidos têm alta probabilidade de cancelamento prospectivo, com impacto direto no `cancellations_rate` da conta nos próximos ciclos. Kit 6 Canecas Tulipa (`MLB6167272090`, `logistic_type=fulfillment`, `available_quantity=14`) gerou 5 pedidos e tem estoque marginal em Full — ruptura provável em menos de 3 dias no ritmo atual.

---

### Tese da conta

**Vulnerável.** O canal exibe crescimento real de patamar em GMV — consistente em 30d e 60d, com ticket em trajetória de alta contínua, reputação verde, MercadoLíder Gold íntegro e ETA para Platinum estimado em ~15 dias. No entanto, três fragilidades estruturais coexistem com esse resultado: (1) ADS representa 75,1% do GMV com orgânico fraco (~R$ 1.500), criando dependência direta das campanhas de Himmel; (2) a conta opera com concentração top3 de 59,4% sustentada em variações de uma única família de produto (IMB501 Cross-Docking), sem segundo vetor visível; (3) dois anúncios em Full com estoque crítico (`available_quantity` de 1 e 14) geram cancelamentos prospectivos que podem pressionar o `cancellations_rate` justamente no momento em que a conta se aproxima do limiar Platinum. O número é forte; a estrutura embaixo do número é frágil.

---

### Risco estrutural principal

**Risco:** Dependência de ADS como vetor dominante de receita (75,1% do GMV) com orgânico incapaz de sustentar o patamar sem mídia paga.

**Por que importa:** Se Himmel reduzir verba, pausar campanhas ou se o ACOS médio subir (por aumento de concorrência, mudança de leilão ML ou rotação de catálogo), o canal não tem orgânico estrutural para absorver a queda. A conta estaria reportando crescimento de patamar que na prática pertence às campanhas — não à saúde intrínseca do canal.

**Histórico:** Sem weekly.md ou monthly.md com conteúdo, não é possível afirmar se esse share de ADS é padrão da conta ou fenômeno recente. O dado de hoje é o primeiro ponto formal disponível nesta análise estratégica.

**Sinal de confirmação:** ADS share acima de 65% em 3 dos próximos 5 dias úteis, mantendo GMV acima de R$ 5.000/dia, confirma dependência estrutural — não pico de campanha pontual.

---

### Sinais a observar

1. **ADS share acima de 65% por 3 dias consecutivos** (calculando `revenue_ads / gmv` diariamente, se disponível no pacote) confirma que a dependência de mídia paga é padrão operacional do canal, não evento. Isso eleva o risco estrutural de classificação para nível crítico.

2. **Kit 6 Canequinhas Acrílico (`MLB4410218897`) gerar 1+ cancelamento registrado nos próximos 2 ciclos** (`cancellations_rate` subindo de 0 em mais de um ciclo consecutivo) confirma que estoques críticos em Full estão convertendo em pedidos sem cobertura — e que o `cancellations_rate` atual de 0 é pré-ruptura, não histórico estável.

3. **Ticket médio abaixo de R$ 52 por 2 dias seguidos** (reversão para a banda do 7d de R$ 47,25) indicaria que o dia de hoje foi pico de composição, não consolidação de patamar — e que a trajetória de alta de ticket observada em 30d/60d não está sendo sustentada no ciclo mais recente.