<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base robusta: 13 ciclos diários acumulados na weekly.md (22/05–04/06), ml_snapshot completo com todos os blocos em `status: ok` (reputação, mercadolider, fulfillment_mix 7d/30d/yesterday_top10, top_items_details, ads_summary, account_overview). Nota: o bloco do dia 04/06 já foi ingestido na weekly às 09:40 BRT; este pacote usa snapshot capturado às 14:25 UTC — divergências pontuais de `available_quantity` são esperadas e não invalidam a leitura. Monthly.md ainda é template sem tese preenchida.

---

### Leitura temporal

- **Mesmos dias da semana (controle de sazonalidade):** As últimas 5 quartas-feiras traçam uma série de ruptura de patamar inequívoca: R$3.176 (07/05) → R$6.540 (14/05) → R$6.113 (21/05, dip registrado na memória como oscilação) → R$8.464 (28/05) → R$8.648 (04/06). O dia de hoje é o segundo acima de R$8.000 em quarta-feira — não pico isolado. `changes.gmv_vs_same_weekday_pct = +42,4%` confirma que o dia está materialmente acima da média histórica do próprio dia da semana.

- **7d → 30d → 60d — trajetória consistente em todas as janelas:** GMV do dia (R$8.648) está +9,4% acima do avg_7d (R$7.903), +57,1% acima do avg_30d (R$5.506) e +90,9% acima do avg_60d (R$4.529). O fato de o 7d já estar 75% acima do 60d indica que a aceleração não é do dia de hoje: a conta operou em patamar estruturalmente mais alto nos últimos 30–7d do que na base bimestral inteira. Ticket estável (+1,4% vs 30d, +17,8% vs 60d) confirma que o crescimento é puxado por volume de pedidos, não por elevação de mix de produto.

- **Hipóteses anteriores — confirmação ou enfraquecimento:** A concentração do cluster IMB501 em ~49–50% (49,7% hoje) está documentada há 13 ciclos consecutivos: confirmada como padrão estrutural. A série de ADS share em torno de 50–57% nos últimos 5 ciclos (55,25% em 04/06 L05 anterior, 56,5% hoje) confirma estabilização pós-queda monotônica de maio: hipótese de "orgânico expandindo mais rápido que ADS" (registrada em 01/06) enfraqueceu. A health de MLB3288536143 em 0,71 permanece no 13º ciclo idêntico: sem direção, sem reversão.

- **MercadoLíder:** Progressão linear desde 22/05 (81,34%) até 98,71% hoje — gap reduzido de R$55.227 para R$3.810 em 13 ciclos. O ritmo diário médio (R$4.870/dia) é 2,27x o gap atual. `eta_dias_estimado = 0,8`: a promoção a Platinum está a ≤1 dia de threshold pelo cálculo simples de pace médio. A ressalva do pacote é válida: o ETA real depende de quais dias saem da janela rolling de 60d nos próximos ciclos — dias antigos com GMV alto podem segurar o denominador.

---

### Leitura estratégica

- **Mudança de patamar confirmada em múltiplas janelas — não ruído:** A conta passou de uma base de ~R$4.500/dia (60d) para ~R$7.900/dia (7d), com o dia de hoje em 1,91x o patamar bimestral. A consistência entre 7d, 30d, 60d e o controle por dia da semana (todas as janelas apontam na mesma direção com magnitudes proporcionais) descarta explicação por ruído estatístico ou sazonalidade. O crescimento é estrutural — mas foi construído sobre base com fragilidades não resolvidas: health degradada do anúncio líder, rupturas recorrentes dos Full fora do IMB501, e dependência de ADS para sustentar exposição.

- **Concentração IMB501 é padrão histórico — mas o vetor de risco está dentro dele:** O cluster IMB501 (Cinza 41 + Vermelha 28 + Preta 20 = 89 pedidos / 49,7% do dia) opera há 13 ciclos nessa faixa de concentração. A concentração em si não é risco novo — é padrão consolidado da conta. O risco real está dentro do cluster: MLB3288536143 (Tampa Cinza + Tampa Vermelha, Full) tem `health = 0,71` (nível regular) há 13 ciclos, indicando que o ML está reduzindo progressivamente o ranking orgânico desse anúncio. ADS está compensando a perda orgânica, mas o custo de manter visibilidade sobre um anúncio em nível regular tende a crescer à medida que a posição orgânica cai.

- **Divergência de modalidade de envio entre campeões e base ativa é estrutural:** Os top 10 de ontem operam 68,6% Full / 31,4% Cross-Docking, enquanto a base ativa inteira é 39,7% Full / 60,3% Cross-Docking (`fulfillment_mix_yesterday_top10.full_pct = 68,6%` vs `account_overview.active_analysis.fulfillment_mix.full_pct = 39,7%`). A diferença de -28,9pp indica que os anúncios que geram volume são excepcionais dentro da base — e o que suaviza os campeões nesse dia é o IMB501P (MLB4535865317) em Cross-Docking. Dois dos três Full críticos fora do IMB501 (Tulipa e Canecas Lisas) estão com estoque sub-dia: MLB6167272090 com 5 unidades, MLB6232315532 com 11 unidades.

- **MercadoLíder Platinum iminente, mas com vulnerabilidade de timing:** Com gap de R$3.810, progress 98,71% e GMV do dia de R$8.648 (= 2,27x o ritmo necessário), a promoção está no horizonte imediato. A fragilidade não é de volume — é de qualidade: `cancellations_rate = 0` oficial, mas a Tulipa pausada (padrão de 7 ciclos) tem gerado cancelamentos prospectivos a cada ruptura. Se um volume de cancelamentos entrar na janela oficial antes do threshold ser cruzado, o `cancellations_rate` pode sair de zero e ameaçar os critérios de qualidade obrigatórios para Platinum (cancelamentos com devolução < 2%, pelo vendedor ≤ 0,5%).

---

### Tese da conta

**em ganho de patamar**

A conta ML da Budamix saiu estruturalmente de uma base de ~R$4.500/dia (60d) para ~R$7.900/dia (7d), com consistência confirmada em mesmos dias da semana, 30d e 60d — não ruído, não efeito de dia. O crescimento é puxado por volume, ADS eficiente (ROAS 14,3x) e exposição Full nos campeões. A conta está no limiar da promoção a MercadoLíder Platinum (gap R$3.810, progress 98,71%). O ganho de patamar está acontecendo apesar das fragilidades estruturais não resolvidas — concentração crônica em IMB501, health degradada do anúncio líder há 13 ciclos, e rupturas recorrentes nos dois Full de suporte (Tulipa e Catálogo Canecas Lisas) — não graças a uma base operacionalmente saudável.

---

### Risco estrutural principal

**Risco:** Degradação persistente do nível de qualidade do anúncio MLB3288536143 (Conjunto 5 Potes de Vidro — Tampa Cinza e Tampa Vermelha) em nível regular (health = 0,71) há 13 ciclos consecutivos sem reversão — sobre o anúncio que concentra ~39% do volume diário da conta.

**Por que importa:** O ML reduz progressivamente o ranking orgânico de anúncios com health abaixo de 0,85 (nível regular). O crescimento de GMV está sendo sustentado sobre um anúncio com exposição orgânica em declínio contínuo. ADS compensa hoje (ROAS 14,3x, eficiente), mas a dependência de mídia paga sobre o principal anúncio cria um custo de sustentação que cresce na proporção inversa da posição orgânica. Sem dado de driver interno da health (qual componente está degradado — atrasos, reclamações, completude de listing), não é possível endereçar a causa.

**Histórico:** Documentado desde 22/05 (primeiro ciclo disponível). Treze ciclos com o mesmo valor (0,71) — padrão que descarta oscilação pontual. Nenhuma reversão registrada.

**Sinal de confirmação:** MLB3288536143 com `health ≤ 0,68` em qualquer ciclo dos próximos 5 dias confirma erosão ativa e ativa gatilho de alinhamento Yasmin–Himmel sobre cobertura preventiva de campanha.

---

### Sinais a observar

1. **`mercadolider.medalha_atual = platinum` no próximo snapshot** — com gap de R$3.810 e ETA de 0,8 dias, o próximo ciclo deve confirmar ou não a promoção. Se o snapshot mostrar gap maior que R$3.810 (dias de alto GMV saindo da janela rolling), calcular novo ETA e verificar se o ritmo dos últimos 7d (R$4.870/dia) é suficiente para cruzar o threshold nos 2 dias seguintes.

2. **MLB6167272090 (Kit 6 Canecas Tulipa 250ml, Full) com `available_quantity ≤ 2` ou `status = paused` no próximo ciclo** — com 5 unidades e 18 pedidos no dia (sub-day runway), este é o 7º ciclo do padrão de ruptura recorrente. Ruptura gera cancelamentos prospectivos que entram na `cancellations_rate` da janela oficial ML — vetor direto de risco à elegibilidade Platinum precisamente no momento do threshold.

3. **MLB6232315532 (Kit 6 Canecas Lisas 200ml, único Catálogo gold_pro da conta, Full) com `available_quantity ≤ 5` por 2 ciclos consecutivos** — com 11 unidades e ritmo de 16 pedidos/dia (cobertura <1 dia), ruptura nesse anúncio derruba o Buy Box ML em Catálogo. Recuperação de Buy Box em anúncio Catálogo é mais lenta do que em Clássico — impacto de exposição persiste por dias após restock.