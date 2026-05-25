<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória robusta: weekly.md com três entradas diárias consecutivas (22, 23 e 24/05) com hipóteses rastreáveis e progressão de ciclos. monthly.md preenchido apenas com template — sem tese mensal madura. Todos os blocos `ml_snapshot` retornaram `status: ok` (reputação, MercadoLíder, mix de modalidade de envio, ads_summary, account_overview), com cobertura de 100% nos pedidos das janelas de 7d e 30d. Base suficiente para tese com confiança média-alta. A ausência de breakdown de `revenue_ads_yesterday_brl` por `platform_item_id` — pendência registrada em todos os três ciclos anteriores — continua limitando a leitura de qual anúncio ADS sustenta.

---

### Leitura temporal

- **7d vs dia:** GMV do dia em R$5.024,80 contra média 7d de R$5.153,29 (`gmv_vs_7d_pct=-2,5%`), pedidos em 99 contra 95,6 (`orders_vs_7d_pct=+3,6%`). Dentro da banda — o sinal é de estabilização em patamar alto, não retração.

- **30d e 60d:** GMV +10,4% vs 30d (média R$4.549,64) e +22,7% vs 60d (média R$4.096,61). Pedidos essencialmente flat vs 30d (-0,7%) e +3,2% vs 60d. O ganho está inteiramente no ticket: +11,2% vs 30d e +18,8% vs 60d. A conta subiu de patamar de valor médio ao longo do bimestre — de R$42,73 para R$50,76 por pedido — sem expansão proporcional de volume.

- **Mesmos domingos:** média dos últimos quatro domingos em R$3.691,93 / 78,75 pedidos (`gmv_vs_same_weekday_pct=+36,1%`, `orders_vs_same_weekday_pct=+25,7%`). O domingo de 10/05 (54 pedidos, R$2.356) puxa a média para baixo; excluindo-o, a média dos outros três fica em ~R$4.137 / 87 pedidos — o dia ainda supera em +21,5% GMV. Dia forte no controle de sazonalidade, não exceção estatística.

- **Hipóteses anteriores:** todas as três hipóteses ativas confirmadas pelo quarto ciclo consecutivo: (1) nível de qualidade dos dois Full líderes em Clássico estagnado (MLB3288536143 em 0,71 e MLB4073003575 em 0,75, ambos nível regular — quarto ciclo); (2) ADS share sistematicamente acima de 65% (71,2% em 24/05, após 69,9% em 22/05 e breve recuo a 49,5% em 23/05); (3) ausência do Kit 6 Canecas Porcelana Tulipa (MLB6167272090) do top 10 — ruptura provável, conforme sinalizado na memória de 23 e 24/05.

---

### Leitura estratégica

- **Lente 1 — Patamar:** A conta está operando acima da banda de 30d e expressivamente acima da de 60d em GMV, sustentada exclusivamente por ticket em ascensão. O volume de pedidos está estável — não cresceu. Isso classifica o movimento como ganho de mix de valor ao longo do bimestre, não de alcance. A semana 7d mostra que esse patamar mais alto se estabilizou — a questão estratégica não é se o patamar é real (é), mas se é sustentável dada a estrutura que o carrega.

- **Lente 3 — Dependência de anúncio e modalidade de envio:** O cluster IMB501 (MLB3288536143, Tampa Preta + Vermelha + Cinza — anúncio único com variações) gerou 47 pedidos = 47,5% do volume diário, pelo terceiro ciclo consecutivo acima de 44%. A modalidade de envio dos campeões do dia é 83% Full (`fulfillment_mix_yesterday_top10.full_pct`) contra 32,5% Full na base ativa total (`account_overview.active_analysis.fulfillment_mix.full_pct`). Hipótese: o faturamento é carregado por anúncios em Full — que têm exposição superior — enquanto 67,5% da base ativa está em Cross-Docking e gera volume residual. A assimetria não é nova (30d também mostra 74,3% Full no mix giro), mas a dependência de 47,5% em um único anúncio já é concentração estrutural.

- **Lente 4 — Buy Box catálogo vs ranking de categoria:** Os dois líderes (Conjunto 5 Potes de Vidro e Kit 4 Potes 1050ml) são Clássico sem catálogo (`is_catalog=false`), competindo por ranking de categoria — não por Buy Box. Ambos com nível de qualidade em nível regular (0,71 e 0,75) pelo quarto ciclo sem recuperação. Anúncios Clássico com nível regular têm redução progressiva de exposição orgânica no ranking de categoria — o ML penaliza passivamente sem cancelar o anúncio. O único Catálogo de alto giro no top (Kit 6 Canecas Lisas 200ml, MLB6232315532, Premium Full, `is_catalog=true`) tem `available_quantity=25` com ~9 pedidos/dia: cobertura estimada de ~2,8 dias. Ruptura em Catálogo significa perda de Buy Box com recuperação lenta — diferente de Clássico, onde retomar estoque não restaura ranking imediatamente, mas restaura disponibilidade.

- **Lente 5 — Mercado Ads:** ADS share em 71,2% (`revenue_ads_yesterday_brl=R$3.578,05` / `gmv=R$5.024,80`), ROAS ~11,3x, ACOS 4,22% — eficiência excepcional. Mas a série dos últimos três ciclos (69,9% → 49,5% → 71,2%) mostra que o recuo de 23/05 foi exceção, não tendência: o ADS share voltou ao nível anterior sem mudança estrutural detectável. A hipótese de que o orgânico estava se fortalecendo (share 49,5% em 23/05) foi refutada em 24/05. A conta opera com ADS dominante de forma persistente — o que é eficiente enquanto Himmel sustenta as campanhas, e frágil se elas pararem ou o ROAS cair.

- **Lente 6 — MercadoLíder:** MercadoLíder Gold, progresso para Platinum em 83,47% (`progress_pct`), gap de R$48.941 (`platinum.gap_revenue_brl`), ETA ~11,9 dias ao ritmo atual de R$4.117,65/dia. O dia (R$5.024,80) está acima do pace necessário, contribuindo positivamente. Métricas de qualidade dentro dos thresholds: `cancellations_rate=0`, `claims_rate=0,0024` (50% do limite de 0,005), `delayed_handling_rate=0,0012`. O `ratings_negative=0,39` (39%) é elevado mas sem série para definir tendência — não constitui risco imediato. Zona de gap entre R$30k–R$100k: sustentar ritmo avança, reduzir atrasa significativamente. Qualquer combinação de ruptura em Full campeão + cancelamentos automáticos entra diretamente nessa janela apertada.

---

### Tese da conta

**Vulnerável.** O patamar de GMV e ticket é real — confirmado em 30d e 60d, acima da banda histórica — mas a estrutura que o sustenta acumula fragilidades sem resolução ao longo de quatro ciclos: nível de qualidade dos dois Full líderes em Clássico estagnado em nível regular sem recuperação (0,71 e 0,75), ADS dominante acima de 65% como vetor principal (71,2%), concentração de 47,5% em um único anúncio com variações, e estoque crítico em dois anúncios do cluster de canecas (MLB6232315532 com ~2,8 dias de cobertura em Catálogo; MLB6582645908 com 1 unidade restante em Cross-Docking). O resultado financeiro parece saudável porque as alavancas ainda funcionam — mas a erosão orgânica dos campeões, se não revertida, vai aparecer no faturamento antes de aparecer nos cancelamentos ou na reputação.

---

### Risco estrutural principal

**Risco:** Degradação persistente do nível de qualidade dos dois Full líderes em Clássico (Conjunto 5 Potes de Vidro — MLB3288536143 — em 0,71 e Kit 4 Potes 1050ml — MLB4073003575 — em 0,75, ambos nível regular), pelo quarto ciclo consecutivo sem recuperação, com dependência de ADS acima de 65% de share para compensar a perda de exposição orgânica.

**Por que importa:** Anúncios Clássico em nível regular perdem posição no ranking de categoria progressivamente no ML — sem sinal brusco e sem cancelamento imediato. O ADS (Himmel) está cobrindo essa perda de orgânico com eficiência alta agora (ROAS ~11x), mas se as campanhas forem pausadas, ajustadas ou o ROAS cair, o orgânico que deveria sustentar o patamar não está saudável o suficiente. O resultado é um GMV que pode colapsar mais rápido do que os indicadores de reputação antecipam.

**Histórico:** Risco presente desde pelo menos 22/05 — segundo ponto idêntico registrado na memória daquele ciclo. Nenhum ciclo de recuperação desde então. A trajetória é estabilização em nível ruim, não deterioração, mas também não melhora.

**Sinal de confirmação:** MLB3288536143 ou MLB4073003575 com `health < 0,70` (cruzando para nível preocupante) no ciclo de 25/05, com ADS share acima de 65% no mesmo dia, transita o risco de latente para crítico — ponto de ação com Yasmin e Himmel. Complementarmente, GMV abaixo de R$4.500 por dois dias consecutivos a partir de agora, sem mudança de campanha, indica que a erosão orgânica está aparecendo no resultado.

---

### Sinais a observar

1. **Nível de qualidade de MLB3288536143 e MLB4073003575 no ciclo de 25/05 (quinto ciclo):** `health` acima de 0,85 em qualquer dos dois reverte o risco estrutural; abaixo de 0,70 em qualquer dos dois — com ADS share acima de 65% no mesmo dia — aciona alinhamento Yasmin–Himmel sobre cobertura preventiva e investigação de drivers do nível de qualidade.

2. **Ruptura no cluster de canecas — duplo vetor:** MLB6582645908 (Kit 6 Canecas 250ml, `available_quantity=1`) parecendo pausado ou com cancelamentos automáticos no próximo pacote; e MLB6232315532 (Kit 6 Canecas Lisas 200ml, Catálogo Full Premium, ~2,8 dias de cobertura) com `available_quantity` abaixo de 10 e perda de Buy Box confirmada. Os dois eventos simultâneos pressionam `cancellations_rate` e estreitam a janela MercadoLíder Platinum dentro do ETA de ~12 dias.

3. **ADS share no ciclo de 25/05:** segundo ponto consecutivo acima de 65% com nível de qualidade dos campeões estagnado (0,71 e 0,75) aciona alinhamento Yasmin–Himmel sobre diagnóstico de cobertura preventiva — gatilho definido na memória do ciclo 24/05 e que se torna exigível com o dado de amanhã.