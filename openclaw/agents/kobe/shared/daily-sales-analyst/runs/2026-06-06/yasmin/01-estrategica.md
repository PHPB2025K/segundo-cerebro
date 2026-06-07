<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly.md tem 10 entradas consecutivas (22/05–05/06), sustentando leitura de tendência. ml_snapshot completo com reputação, fulfillment_mix, top_items_details e ads_summary. monthly.md sem tese consolidada (template vazio). Única limitação estrutural relevante: `available_quantity` em MLB3288536143 é do anúncio pai, não por variação — granularidade de ruptura por cor não é possível.

---

### Leitura temporal

- **vs 30d e 60d — patamar nominal, não real:** GMV de R$ 6.611 aparece +13,8% vs avg_30d (R$ 5.810, `changes.gmv_vs_30d_pct`) e +31,1% vs avg_60d (R$ 5.041). Mas 79 dos 162 pedidos (`orders=67+6+6`) vieram de três anúncios com `status=paused` e `available_quantity=0` — ordens prospectivamente canceláveis. GMV líquido estimado (162−79 pedidos × ticket médio R$ 40,81) é ~R$ 3.390, abaixo do avg_30d. O patamar declarado é artefato de ruptura, não ganho estrutural.

- **vs 7d — reversão vs pico da semana:** avg_7d de R$ 7.946 e 171,7 pedidos (`historical.avg_7d`) refletem os ciclos de 01–05/06 (R$ 7.742–R$ 9.210). O dia recua -16,8% GMV vs essa banda — coerente com a ruptura do vetor Full principal. A semana recente foi o pico da série 60d; hoje é o primeiro ciclo da reversão confirmada.

- **vs mesmo dia da semana — sazonalidade não explica:** +40,3% pedidos e +28,2% GMV vs média dos últimos quatro sábados (115,5 pedidos, R$ 5.159 — `same_weekday_avg`). O sábado não é um dia fraco por si; o número bruto de hoje parece forte. A contaminação de ruptura (~49% do volume em anúncio pausado) invalida a leitura positiva.

- **Hipóteses anteriores confirmadas:** a memória de 05/06 antecipou "checar amanhã se status virou paused" para MLB3288536143 — confirmado. O gap MercadoLíder em zero e progress=100% há 2 ciclos sem conversão formal (`power_seller_status` ainda `gold`) segue como hipótese em aberto pelo segundo dia consecutivo.

---

### Leitura estratégica

- **Lente 3 + 1 — Ruptura do vetor Full principal distorce toda a leitura de patamar:** MLB3288536143 (Conjunto 5 Potes Vidro — família IMB501, `logistic_type=fulfillment`, `status=paused`, `available_quantity=0`) é o anúncio líder da conta há 15+ ciclos, concentrando 40–56% do volume diário na série histórica (`weekly.md`). Hoje gerou 67/162 pedidos (41,4%) como ordens prospectivamente canceláveis. Somando MLB6582682928 (Kit 6 Canecas Canelada, `status=paused`, `available_quantity=0`, 6 pedidos) e MLB5322494954 (Kit 2 Potes 1520ml, `status=paused`, `available_quantity=0`, 6 pedidos), o total é **79/162 pedidos (48,8%) em ruptura ativa**. Os Cross-Docking ativos da família IMB501 (MLB4535865317 Tampa Preta e MLB4535865311 Tampa Cinza, ambos com estoque robusto >8.000 un) sustentam fluxo, mas com menor exposição orgânica que o Full pausado — a queda de patamar é estruturalmente prevista até reposição e reativação.

- **Lente 6 — MercadoLíder Platinum na janela mais crítica da promoção:** `sales_60d_revenue_brl=R$ 298.736` vs threshold R$ 296.000, `sales_60d_count_paid=6.743` vs threshold 1.725, `gap_revenue_brl=0`, `progress_pct=100%`, `eta_dias_estimado=0` — segundo ciclo consecutivo com critério financeiro cruzado e `power_seller_status` ainda `gold`. As quality metrics estão inteiramente dentro do envelope Platinum: `claims_rate=0,18%` (threshold < 1%), `cancellations_rate=0` (threshold ≤ 0,5%), `delayed_handling_rate=0,09%` (threshold < 6%). O risco agora é que os 79 cancelamentos prospectivos de hoje entrem na janela oficial ML antes do reconhecimento formal — `cancellations_rate` saindo de zero para > 0,5% bloquearia ou atrasaria a promoção. É o momento de maior fragilidade da conta no ciclo de upgrade, coincidindo com a maior ruptura operacional da série.

- **Lente 5 — ADS share inflado por volume de ruptura, eficiência declarada irreal:** ADS gerou R$ 4.002 com gasto de R$ 392 — ROAS 10,2x, ACOS 7,15%, share 60,5% do GMV nominal (`ads_summary`). Com MLB3288536143 sendo o maior vetor de pedidos do dia e operando em Full com 13 campanhas ativas, hipótese é que parte dos 67 pedidos foi atribuída a campanha (breakdown por `platform_item_id` indisponível — pendência do 16º ciclo). Se confirmado, o revenue_ads reverterá com os cancelamentos, invalidando o ROAS declarado. ADS share real pode estar acima de 60% após ajuste — fragilidade latente independente da eficiência nominal.

- **Lente 4 — Qualidade de anúncio degradada nos campeões restantes:** Dos anúncios ativos no top 10, MLB5402326666 (Kit 4 Potes 640ml) tem `health=0,66` (nível preocupante — terceiro ciclo consecutivo abaixo de 0,85, confirmando recorrente como antecipado em memória 05/06). MLB4931700052 (Kit 4 Potes 800ml) e MLB5322494954 (Kit 2 Potes 1520ml — este pausado) têm `health=0,75` (nível regular). MLB4076957145 e MLB4073064873 em `health=0,85` (limite inferior do nível bom). Com o líder Full pausado, o volume migra para anúncios com qualidade degradada — exposição orgânica estruturalmente inferior na cauda que precisa compensar.

---

### Tese da conta

**Vulnerável.** A conta entrou em ruptura do seu principal vetor operacional (MLB3288536143, Full, família IMB501 — 40–56% do volume em 15+ ciclos da série semanal) no momento exato em que aguarda reconhecimento formal de MercadoLíder Platinum (segundo ciclo com gap=0 sem conversão). O GMV nominal de R$ 6.611 é artefato: GMV líquido estimado ~R$ 3.390 — abaixo do avg_30d. A reputação estrutural é verde e sólida, e o histórico financeiro 60d é robusto. Mas a vulnerabilidade não é financeira: é a coincidência de ruptura de volume com janela de promoção, onde 79 cancelamentos prospectivos podem bloquear o upgrade ou ameaçar sua manutenção. A conta não está em queda estrutural no longo prazo — está em crise operacional de curto prazo no pior momento possível.

---

### Risco estrutural principal

**Risco:** 79 cancelamentos prospectivos de anúncios paused+zero (48,8% dos pedidos do dia) ativando `cancellations_rate` na janela oficial ML durante o período de reconhecimento de MercadoLíder Platinum.

**Por que importa:** `cancellations_rate` oficial está em 0 (`reputation.cancellations_rate=0`). Se as 79 ordens de anúncios pausados (MLB3288536143: 67, MLB6582682928: 6, MLB5322494954: 6) forem processadas como cancelamentos automáticos pelo ML, o rate sai de zero para uma faixa que pode cruzar 0,5% (threshold de "cancelamentos pelo vendedor" para manutenção de qualquer nível MercadoLíder). Com `transactions_completed=6.622`, 79 cancelamentos representam ~1,19% da base — acima do threshold de 0,5% se ML os classificar na categoria correta. O cenário mais crítico: promoção Platinum ocorre após os cancelamentos já entrarem na janela, resultando em medalha concedida e imediatamente em risco.

**Histórico:** O padrão de ruptura recorrente foi rastreado em múltiplos ciclos. Tulipa (MLB6167272090) gerou 7-8 ciclos de ruptura com 4-18 pedidos prospectivos sem mover o rate oficial. O presente evento é 4-17x maior em volume. A memória de 05/06 já sinalizava explicitamente o risco de status=paused para MLB3288536143 — a ruptura não é surpresa operacional, é confirmação de hipótese madura.

**Sinal de confirmação:** `ml_snapshot.reputation.cancellations_rate` sair de zero no próximo snapshot confirma que os cancelamentos do dia 06/06 entraram na janela oficial ML e o risco está ativo.

---

### Sinais a observar

1. **`cancellations_rate` sair de zero em 1–3 snapshots** — se o campo `ml_snapshot.reputation.cancellations_rate` registrar qualquer valor > 0 nos próximos ciclos, as ordens prospectivas do dia 06/06 entraram na janela oficial ML; dois ciclos consecutivos > 0 com valor crescente confirmam série ativa que ameaça elegibilidade Platinum antes ou após promoção.

2. **`power_seller_status` virar `platinum` no próximo snapshot** — se a medalha atualizar antes de os cancelamentos serem absorvidos pela janela oficial, a janela de risco agudo fecha (reconhecimento antecede impacto); se não virar por mais 2 ciclos com `progress_pct=100%` e gap=0, hipótese de bloqueio silencioso por métrica não visível no pacote (ex: ratings_negative=0,41 em análise interna ML) merece escalação via Yasmin.

3. **MLB3288536143 seguir com `status=paused` por 2 dias seguidos** — confirma queda real de patamar de pedidos (de ~R$ 7-9k/dia da série recente para ~R$ 3-4k/dia com base nos Cross-Docking ativos), validando que IMB501P e IMB501C em Cross-Docking não compensam a exposição Full perdida; o período entre pausa e reativação é o intervalo de retração estrutural da conta.