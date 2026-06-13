<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base robusta: 14+ ciclos diários na weekly.md, monthly.md com template criado mas sem tese mensal preenchida (pipeline em maturação, não consolidação consolidada). Todas as janelas temporais disponíveis e populadas: 7d (7 dias), 30d (30 dias), 60d (59 dias). `ml_snapshot` completo — `reputation`, `fulfillment_mix_30d/7d/yesterday_top10`, `top_items_details`, `ads_summary` e `account_overview` todos com `status: ok`. Sem ressalvas materiais sobre disponibilidade; hipóteses anteriores têm série suficiente para teste.

---

### Leitura temporal

- **Patamar 60d confirmado em duas métricas:** `metrics.pedidos_validos=150` está +24,1% vs `historical.avg_60d.avg_orders=120,9` e `metrics.gmv=R$6.397,92` está +19,4% vs `avg_60d.avg_gmv=R$5.359,58` (`changes.orders_vs_60d_pct=+24,1%`, `changes.gmv_vs_60d_pct=+19,4%`). A expansão está presente em ambas as métricas independentes — não é artefato de ticket nem de composição. A conta opera num patamar bimestral estruturalmente mais alto.

- **Controle de sazonalidade:** `same_weekday_avg.avg_orders=126,5` / `avg_gmv=R$6.364,26`. O dia (150 pedidos / R$6.397,92) está +18,6% em pedidos e +0,5% em GMV acima das últimas quatro sextas. O volume cresce; o GMV empata. A diferença é ticket: `metrics.ticket_medio=R$42,65` vs `same_weekday_avg.avg_ticket=R$50,31` (−15,3%). O controle de dia da semana descarta efeito sazonal — a compressão de ticket é compositional (IMB501 dominando), não deterioração de preço.

- **Posicionamento no 7d:** O dia está −8,6% em pedidos e −12,1% em GMV vs `historical.avg_7d` (164,1 pedidos / R$7.281,26). A semana de 06–11/06 incluiu dias de R$8k–R$9k. O dia de hoje é comparado com um pico — opera abaixo da semana, mas dentro da banda de 30d (`gmv_vs_30d_pct=−2,9%`). O 7d foi o outlier; hoje é a normalidade do patamar atual.

- **Hipóteses anteriores — confirmação e nova fase:** A trajetória para MercadoLíder Platinum, monitorada desde 04/06 com gap descendente ciclo a ciclo, foi **confirmada**: `ml_snapshot.mercadolider.medalha_atual=platinum`, `power_seller_status=platinum`, `sales_60d_revenue_brl=R$321.406,28` (threshold R$296.000 superado em R$25.406). O eixo analítico muda de "conquistar" para "manter". A hipótese de série ADS descendente (69,9% em 22/05 → 42,0% hoje, com uma lacuna por lag de API em 11/06) recebe novo ponto de dados consistente com expansão orgânica — hipótese se consolida como tendência, mas a lacuna de 11/06 impede declarar fato definitivo.

---

### Leitura estratégica

- **Patamar estrutural com compressão de ticket compositional (Lente 1):** A conta ganhou patamar real em 60 dias — pedidos e GMV ambos acima em +24% e +19%. O controle de sazonalidade confirma: a sexta de hoje está acima da média histórica de sextas em volume. A compressão de ticket (`ticket_vs_30d_pct=−10,5%`) não é erosão de preço: o cluster IMB501 (`MLB3288536143`, ticket ~R$42) carregou 51,3% do top3 em dia onde outros produtos de maior ticket ficaram fora do topo. O risco não é o ticket — é a dependência do mix que deprime o ticket quando o cluster domina.

- **Platinum conquistado — risco migra para manutenção silenciosa (Lente 6):** `power_seller_status=platinum` com ritmo atual de R$5.356/dia e threshold de manutenção ~R$4.933/dia (R$296k ÷ 60d). O dia de hoje (R$6.397) opera 29,6% acima do pace necessário. A vulnerabilidade não é volume — é reputação: `cancellations_rate=0` (API, janela longa), mas `MLB6167272090` (`status=paused`, `available_quantity=0`) gerou 5 pedidos hoje pelo 9º+ ciclo consecutivo. Esses pedidos viram cancelamentos prospectivos garantidos que entram na janela oficial com delay e, acumulados, podem mover a taxa sem aviso no volume.

- **ADS em novo piso de série — orgânico ganhando autonomia (Lente 5):** ADS share 42,0% (`revenue_ads_yesterday_brl=R$2.688,95` / `gmv=R$6.397,92`), ROAS 11,41x (`R$2.688,95 ÷ R$235,62`), ACOS 9,96%. Este é o menor valor válido da série 22/05–12/06 (69,9%→42,0%), com GMV acima da média de 30d. O padrão de 10+ ciclos mostra: ADS cresce em valor absoluto enquanto o orgânico cresce mais rápido — o orgânico está carregando proporcionalmente mais. A 42% de share, ADS amplifica mas não domina. Hipótese de autonomia orgânica crescente passa de candidata para tendência, dependente de confirmação nos próximos 2 ciclos.

- **Concentração estrutural em campeão degradado e cobertura crítica emergente (Lentes 3 e 4):** `MLB3288536143` (IMB501) carrega 51,3% do top3 com `health=0,71` (nível regular) no 18º+ ciclo idêntico. É `is_catalog=false` — compete por ranking de categoria, onde health degradada suprime progressivamente a visibilidade orgânica. `available_quantity=1.563` descarta risco de ruptura; o risco é a estagnação da saúde do anúncio como vetor de erosão lenta. Em paralelo, `MLB4073003575` (Kit 4 Potes 1050ml, `health=0,75`, nível regular) tem `available_quantity=13` — 3º ciclo consecutivo de cobertura crítica (~1,9 dias ao ritmo de 7 pedidos/dia) sem restock confirmado na memória. A diferença material: IMB501 é risco crônico de exposição; Kit 4 Potes 1050ml é risco iminente de ruptura operacional.

---

### Tese da conta

**Vulnerável.** A conta ML da Budamix operou uma expansão de patamar real nos últimos 60 dias (+24% pedidos, +19% GMV) e acaba de concluir a transição para MercadoLíder Platinum — conquista que levou múltiplos ciclos e que reposiciona o canal estruturalmente. O orgânico está ganhando autonomia progressiva (ADS share 69,9%→42,0% em 3 semanas sem queda de GMV). No entanto, a conta é **vulnerável** por dois vetores persistentes que coexistem com os números saudáveis: (1) o anúncio que carrega metade do volume (`MLB3288536143`) opera com nível de qualidade estagnado em 0,71 há 18+ ciclos, com exposição orgânica progressivamente comprimida pelo ML e sem sinal de recuperação no pacote; (2) `MLB6167272090` (Tulipa 250ml) está pausado com estoque zero pelo 9º+ ciclo consecutivo gerando cancelamentos prospectivos garantidos — acumulado sobre a janela longa do ML, este é o único vetor capaz de derrubar a medalha Platinum recém-conquistada sem sinalização antecipada no volume.

---

### Risco estrutural principal

- **Risco:** Ciclo crônico de ruptura operacional em `MLB6167272090` (Kit 6 Canecas Tulipa 250ml) — `status=paused`, `available_quantity=0`, 5 pedidos gerados no dia de hoje que se convertem em cancelamentos prospectivos garantidos. Padrão documentado desde 31/05, sem restock confirmado em 9+ ciclos consecutivos.

- **Por que importa:** MercadoLíder Platinum exige `cancellations_rate ≤ 0,5%` (cancelamentos pelo vendedor). A taxa oficial atual é 0 — janela longa do ML. Com `transactions_completed=6.993`, cada ~35 cancelamentos acumulados move a taxa em 0,5 pontos percentuais. Os 9+ ciclos do padrão acumularam volume de pedidos prospectivos (ciclos com 4–12 pedidos/dia no anúncio pausado) que pode já estar próximo ou dentro da janela oficial. O risco não se manifesta no número de hoje — se manifesta quando a taxa oficial sai de zero, sem aviso prévio no faturamento.

- **Histórico:** Não é evento — é padrão estrutural. Documentado em 31/05 (4 pedidos), 05/06 (11 pedidos), 06/06 (6 pedidos), 11/06 (12 pedidos/16 itens por memória) e hoje (5 pedidos). Yasmin foi informada em múltiplos ciclos; resolução operacional não foi confirmada no pacote.

- **Sinal de confirmação:** `ml_snapshot.reputation.cancellations_rate` sair de zero em qualquer snapshot dos próximos 5 ciclos confirma que os cancelamentos acumulados começaram a entrar na janela oficial ML — risco direto e imediato à manutenção do Platinum. `MLB6167272090` permanecer `status=paused` com `available_quantity=0` no próximo ciclo confirma que a falha operacional não foi resolvida.

---

### Sinais a observar

1. **`ml_snapshot.reputation.cancellations_rate` > 0 em qualquer snapshot dos próximos 5 ciclos** — saída de zero confirma que os cancelamentos prospectivos acumulados da Tulipa (`MLB6167272090`, 9+ ciclos de pausa com pedidos) entraram na janela oficial ML; risco direto e imediato à manutenção do MercadoLíder Platinum (threshold: ≤ 0,5%); o sinal pode aparecer sem queda de GMV, sem alerta no volume.

2. **`MLB4073003575` com `available_quantity` ≤ 6 ou `status=paused` no próximo snapshot** — `available_quantity=13` hoje, 3º ciclo consecutivo de cobertura crítica sem restock confirmado (~1,9 dias ao ritmo atual); ruptura desse anúncio Full (`logistic_type=fulfillment`, `health=0,75`, nível regular) adiciona cancelamentos prospectivos e remove velocidade de venda do ranking de categoria de um segundo vetor crítico.

3. **ADS share ≤ 45% por dois ciclos consecutivos com GMV ≥ R$6.000** — se o próximo ciclo com `ads_summary` válido (11/06 teve lag de API) confirmar share abaixo de 45% com denominador forte, a hipótese de expansão orgânica estrutural se converte de tendência em fato consolidado; dois pontos com denominador saudável abaixo de 45% encerram o debate sobre se o orgânico sustenta o canal sem ADS dominante.