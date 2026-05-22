<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` entregues são templates sem conteúdo preenchido; `last_daily_file` aponta para 2026-05-20.md mas seu conteúdo não integrou o pacote. Não há teses ativas, hipóteses acumuladas nem padrões semanais/mensais para confirmar ou refutar — a leitura de hoje é ponto de origem da série estratégica, não confirmação. O `ml_snapshot` compensa: status `ok` em todos os blocos, cobertura logística 100% em 7d e 30d, reputação e ADS presentes. Base operacionalmente rica, estrategicamente rasa.

---

### Leitura temporal

- **vs 30d e 60d — ticket como único motor de GMV:** O dia (`gmv=R$6.082,82 / pedidos=100 / ticket=R$60,83`) está +38% de GMV em relação à `avg_30d` (R$4.406,82) e +56,5% vs `avg_60d` (R$3.886,46). Os pedidos estão praticamente flat — +0,7% vs 30d e +8,2% vs 60d. O crescimento de GMV nas duas janelas longas é inteiramente ticket: +37,1% vs 30d e +44,7% vs 60d. A conta não ganhou alcance; ganhou mix de maior valor.

- **vs 7d — volume recuando após pico, ticket sustentando GMV:** A média dos últimos 7 dias registra 118,9 pedidos e GMV R$5.616,18 — ontem ficou -15,9% em volume e +8,3% em GMV. O distanciamento sugere que a semana recente foi puxada por pelo menos um dia de alto volume (confirmado: 2026-05-14 com 140 pedidos / R$6.539,97). O 7d está inflado; ontem é retração de volume com ticket compensando.

- **vs mesmo dia da semana — volume dentro da banda, GMV fora dela:** As últimas 4 quintas registraram 140 / 75 / 115 / 81 pedidos (avg 102,75 / GMV médio R$4.685,96). Ontem, com 100 pedidos (-2,7%), está dentro da variação sazonal de volume. O GMV de R$6.082,82, porém, está +29,8% acima da média de quinta — sinal de que o ticket elevado não é acidente do dia, é padrão que se destaca mesmo no controle sazonal.

- **Hipóteses anteriores:** Sem weekly.md ou monthly.md populados, não há hipóteses ativas para testar. Esta leitura inaugura a série — qualquer padrão identificado aqui é candidato, não confirmação.

---

### Leitura estratégica

- **Lente 5 — Resultado sustentado por ADS em zona dominante:** `ads_summary.revenue_ads_yesterday_brl=R$4.593,66` com `spend_yesterday_brl=R$341,72` gera ROAS de 13,4x e ACOS de 4,71% — campanha de Himmel eficiente por si. O problema estrutural está no share: **R$4.593,66 / R$6.082,82 = 75,5% do GMV atribuído a Mercado Ads**, bem acima do limiar de zona dominante (≥50%). Com `campaigns_active_count=11` de 14 campanhas, o resultado do canal está majoritariamente condicionado à manutenção ativa de mídia paga. O orgânico não é visível nos dados disponíveis — não é possível afirmar que ele existe em nível que sustente o patamar de GMV sem ADS.

- **Lente 3 — Concentração crônica com divergência crítica de modalidade de envio nos campeões:** Top 3 concentra 60% e top 5 concentra 76% dos pedidos; os produtos de #6 a #10 somam apenas 14 pedidos — sem cauda emergindo. O dado mais relevante é a divergência de modalidade de envio: `fulfillment_mix_yesterday_top10.cross_docking_pct=80%` (Full apenas 20%), enquanto a janela 30d da conta registra `full_pct=73,6%` e a janela 7d registra `full_pct=77%`. Os três campeões do dia — Conjunto 5 Potes Tampa Preta (`MLB4535865317`, `logistic_type=cross_docking`), Kit 10 Potes 1050ml (`MLB4676726433`, `cross_docking`) e Conjunto 5 Potes Tampa Cinza (`MLB4535865311`, `cross_docking`) — operam na modalidade de envio menos garantida. Isso diverge do padrão recente de 7d/30d e sinaliza que os anúncios que puxaram a conta nesses períodos (predominantemente Full) não foram os mesmos de ontem. A conta opera com base ativa de 33,7% Full / 66,3% Cross-Docking (`account_overview.active_analysis.fulfillment_mix`); os campeões do dia estão alinhados à base de listagens, mas desalinhados ao padrão de volume recente.

- **Lente 2 — Reputação saudável com dois sinais de ruptura prospectiva:** `reputation.color=5_green`, `power_seller_status=gold`, `cancellations_rate=0` e `delayed_handling_rate=0.001` — base operacional limpa na janela longa. Mas há dois sinais que ainda não aparecem na métrica oficial: (1) Kit 06 Canequinhas Acrílico (`MLB4410218897`) com `available_quantity=1` e 3 pedidos registrados ontem — ruptura praticamente certa, com cancelamentos prospectivos que entrarão no `cancellations_rate` dos próximos ciclos; (2) os 3 cancelamentos do dia (`metrics.cancelamentos=3`) ainda não impactam a taxa oficial, mas devem ser observados em relação ao anúncio de estoque crítico.

- **Lente 4 — Sem competição de Catálogo nos campeões, mas health degradada em #4:** Todos os 9 primeiros do top 10 têm `is_catalog=false` — competem por ranking de categoria (Clássico), não por Buy Box. O único anúncio em Catálogo no top 10 é o Kit 2 Potes 1050ml (`MLB6518176572`, `is_catalog=true`, `logistic_type=fulfillment`, 2 pedidos, #10) — irrelevante no volume do dia. Kit 4 Potes 1050ml (`MLB4073003575`, #4, 8 pedidos, `logistic_type=fulfillment`) tem `health=0.75` — abaixo do limiar 0.85 — indicando penalização ML ativa e exposição orgânica reduzida progressivamente. Os demais campeões não têm health calculada (65 dos 83 ativos no `no_health_data_count`); leitura de saúde da base é estruturalmente parcial.

---

### Tese da conta

**Vulnerável.** O GMV está acima da banda histórica em 30d e 60d, e a reputação está verde-gold sem erosão registrada — o número parece saudável. Mas a estrutura que o produz não é: **75,5% do GMV de ontem é atribuível a Mercado Ads** (Himmel), sem orgânico visível ou testável por trás; os campeões do dia operam em Cross-Docking (80% do top 10), divergindo da base 7d/30d que registrou 73–77% em Full; a concentração top 3 em 60% é padrão sem cauda emergindo; e há ruptura de estoque iminente no Kit 06 Canequinhas Acrílico (`available_quantity=1`). A conta cresceu de patamar em ticket — não em alcance orgânico. Essa tese ainda não pode ser confirmada como estrutural por falta de memória semanal/mensal, mas os dados de hoje não sustentam leitura de saúde.

---

### Risco estrutural principal

**Risco:** Dependência de ADS dominante (75,5% do GMV via Mercado Ads de Himmel) sem orgânico validado por trás.

**Por que importa:** Se as campanhas forem pausadas, ajustadas ou se o custo por clique subir por concorrência ou saturação de audiência, o GMV colapsa sem fallback orgânico conhecido. O ganho de patamar observado em 30d e 60d pode ser inteiramente dependente de investimento em mídia — não de posicionamento estrutural da conta por ranking, reputação ou Mais Vendido.

**Histórico:** weekly.md e monthly.md não têm dados populados; não é possível afirmar se essa dependência é nova ou crônica. Esta é a primeira leitura com dado de `ads_summary` disponível no pacote.

**Sinal de confirmação:** `revenue_ads_yesterday_brl / gmv` acima de 70% por 3 ciclos consecutivos com dados disponíveis confirma que a conta opera em regime de ADS dominante crônico — não de crescimento orgânico sustentado.

---

### Sinais a observar

1. **ADS share vs orgânico por 3 ciclos seguidos:** Se `revenue_ads_yesterday_brl / gmv` cair abaixo de 50% por 2 dias consecutivos mantendo GMV acima de R$5.500, confirma que orgânico está crescendo e reduzindo a dependência estrutural. Se permanecer acima de 70% por 3 ciclos, confirma regime de ADS dominante crônico — risco estrutural consolidado.

2. **Ruptura de estoque no Kit 06 Canequinhas Acrílico (`MLB4410218897`):** `available_quantity=1` com 3 pedidos registrados ontem. Qualquer pedido nas próximas 24–48h resulta em ruptura e cancelamento prospectivo. Se `reputation.cancellations_rate` subir no próximo ciclo com dado de reputação disponível, confirma que a ruptura impactou a saúde estrutural da conta.

3. **Trajetória de health do Kit 4 Potes 1050ml (`MLB4073003575`):** `health=0.75` (penalização ativa). Se o anúncio registrar queda de pedidos por 2 dias seguidos sem variação de estoque ou preço, confirma que a penalização ML está erodindo exposição orgânica deste campeão de categoria — risco silencioso que não aparece no GMV agregado até se acumular.