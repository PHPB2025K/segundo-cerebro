<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly e monthly estão em templates vazios — sem consolidação histórica acumulada para a conta ML. Não há hipóteses ativas de leituras anteriores para confirmar ou refutar; esta análise serve como ponto de partida da memória, não como verificação de tese. Em compensação, todos os blocos ML opcionais estão disponíveis com cobertura total (reputação, mix fulfillment, top items com health e estoque, ads_summary, account overview) — a leitura estrutural é robusta. A limitação é temporal, não qualitativa.

---

### Leitura temporal

- **60d e 30d — mudança de composição, não de alcance.** A conta saiu de R$3.817 (média 60d) para R$5.057 hoje (+32,5% no GMV), com pedidos essencialmente flat (–1,3% vs 60d) e ticket subindo de R$41,86 para R$56,19 (+34,2%). O padrão se repete no 30d: pedidos –9,9%, GMV +15%, ticket +27,6%. O crescimento não veio de mais volume — veio de mix de maior valor unitário. A trajetória é consistente em duas janelas longas.

- **7d — pico de volume que não se sustentou, mas GMV segura.** A média dos últimos 7 dias registrou 115,1 pedidos e ticket de R$46,17 — o período inclui dias de pico. Hoje o volume recuou para 90 pedidos (–21,8%) mas o GMV ficou em R$5.057 (–4,9%) porque o ticket subiu a R$56,19. O recuo de pedidos vs 7d é a maior divergência do pacote; controlado pelo mesmo dia da semana, é ruído de sazonalidade, não deterioração.

- **Mesmo dia da semana — suporte sólido ao resultado.** Média das 4 quartas anteriores: 92,5 pedidos e R$3.841 de GMV. Hoje: 90 pedidos (–2,7%) e R$5.057 (+31,6%). Volume totalmente alinhado à sazonalidade; GMV expressivamente acima. O ticket elevado de hoje não é anomalia do dia — é aceleração de uma tendência que já estava presente nas comparações 30d e 60d. A quarta de 29/04 (134 pedidos, R$5.618) foi outlier e distorce levemente a média 7d para cima.

- **Hipóteses anteriores:** Sem memória consolidada, não há teses ativas a confirmar ou refutar. Esta leitura inaugura o histórico.

---

### Leitura estratégica

- **Deslocamento estrutural de ticket, não de volume.** A elevação de ticket de R$41,86 (60d) para R$56,19 hoje (+34,2%) aparece de forma consistente em todas as janelas — não é efeito de um dia nem de sazonalidade. Os anúncios de maior valor unitário (Kit 4 Potes 1050ml, Kit 10 Potes 1050ml) estão ganhando peso relativo no mix. A conta cresce em GMV sem crescer em alcance de pedidos — positivo para faturamento, mas aumenta a dependência de um núcleo pequeno de SKUs de alto ticket.

- **Mercado Ads sustenta o resultado, mas a proporção é dominante.** As campanhas de Himmel geraram R$3.041 de receita com R$262 de investimento — ROAS de 11,6x e ACOS de 4,33%, ambos excelentes. Mas essa receita representa **60,1% do GMV do dia**. A conta está em zona de ADS dominante: eficiente hoje, mas estruturalmente exposta. Se as campanhas forem pausadas, ajustadas ou sofrerem mudança de algoritmo ML, o GMV não tem base orgânica equivalente para absorver o impacto.

- **Health dos campeões — ADS mascara penalização.** O 2º maior anúncio por pedidos (Kit 4 Potes 1050ml, 13 pedidos, em Full) opera com health 0,75 — zona de penalização ML. O 5º (Conjunto 5 Potes Tampa Vermelha, 5 pedidos, em Full) tem health 0,71. Dois dos cinco maiores do dia estão penalizados. A conta entrega resultado mesmo assim — o que sugere que o ADS está compensando a exposição orgânica reduzida. Essa combinação é silenciosa: o número parece saudável, mas a exposição orgânica dos campeões está deteriorada.

- **Cauda morta e concentração estrutural.** 174 anúncios pausados contra 82 ativos — os pausados excedem os ativos em 2x. O top 3 concentra 47,8% dos pedidos. Os anúncios vencedores usam Full em proporção muito acima da média da base: 57-77% no top 10 vs 34% na conta toda. A operação vive de um núcleo enxuto de anúncios em Full; a cauda em Coleta sustenta pouco volume e não oferece segundo vetor consolidado.

---

### Tese da conta

**Vulnerável.** O GMV está em trajetória de alta consistente nos últimos 30 e 60 dias, sustentado por elevação real de ticket — isso é positivo e estruturalmente relevante. Mas a arquitetura que entrega esse resultado é frágil em três dimensões simultâneas: aproximadamente 60% do GMV atribuído ao Mercado Ads com ROAS elevado mas sem base orgânica equivalente por baixo; os dois maiores anúncios por volume de pedidos com health penalizado (0,75 e 0,71); e concentração alta em poucos anúncios Full sem segundo vetor consolidado. O número parece saudável; a estrutura que o produz está exposta.

---

### Risco estrutural principal

**Risco:** Dois dos maiores anúncios da conta (Kit 4 Potes 1050ml e Conjunto 5 Potes Tampa Vermelha) operam com health na zona de penalização (0,75 e 0,71) enquanto ~60% do GMV é atribuído a campanhas de Mercado Ads. O ADS está compensando a redução de exposição orgânica causada pela penalização — sem que isso apareça no resultado agregado.

**Por que importa:** Qualquer ajuste nas campanhas de Himmel (pausa, redução de verba, mudança de algoritmo) expõe o ranking real desses anúncios — já penalizados — sem o amparo do tráfego pago. A conta pode perder GMV de forma abrupta e assimétrica, muito mais rápido do que a trajetória de alta sugere.

**Histórico:** Sem memória anterior consolidada, não é possível confirmar se esse é padrão recorrente ou degradação recente. Esta é a primeira leitura formalizada da conta.

**Sinal de confirmação:** Health do Kit 4 Potes 1050ml ou do Conjunto 5 Potes Tampa Vermelha caindo abaixo de 0,70 nos próximos ciclos, ou GMV abaixo de R$4.000 por 2 dias consecutivos com spend ADS constante, confirma que a degradação está se aprofundando além do limiar de compensação.

---

### Sinais a observar

1. **Health dos dois campeões penalizados:** Se Kit 4 Potes 1050ml e Conjunto 5 Potes Tampa Vermelha mantiverem health abaixo de 0,80 por 3 ciclos seguidos, a penalização de ranking passa de hipótese a problema operacional ativo — e a dependência de ADS para compensação deixa de ser contingente.

2. **Ruptura iminente no Kit 06 Canequinhas Com Suporte Acrílico:** O anúncio encerrou o dia com 3 unidades disponíveis após 3 pedidos. Sem reposição em 24–48h, o estoque zera — gerando cancelamentos prospectivos que impactam a taxa de cancelamentos da conta nos próximos ciclos sem sinalização no agregado de hoje.

3. **ADS share como estrutural vs alavanca:** Se o share de Mercado Ads sobre o GMV permanecer acima de 55% por mais de 3 dias seguidos sem crescimento paralelo de pedidos em anúncios não impulsionados, a dependência de mídia paga está se consolidando como arquitetura da conta — não como amplificador pontual.