<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly com quatro entradas diárias recentes (22–25/05) e hipóteses ativas bem documentadas — base operacional suficiente para leitura de continuidade e confirmação de hipóteses. Monthly.md sem tese mensal preenchida, o que limita âncora de longo prazo fora dos campos `avg_60d`; a leitura bimestral depende inteiramente dos dados históricos do pacote. Todos os blocos `ml_snapshot` disponíveis com `status: ok`; base robusta para a leitura de hoje.

---

### Leitura temporal

- **Patamar vs todas as janelas:** GMV R$7.394,36 está +57,5% acima do `avg_30d` (R$4.696,25) e +76,7% acima do `avg_60d` (R$4.185,11). Orders 143 superam `avg_30d` em +40,1% e `avg_60d` em +46,8%. A elevação é simultânea em volume e ticket (R$51,71 vs avg_60d R$42,95, +20,4% via `changes.ticket_vs_60d_pct`): o dia não é efeito de ticket-pull isolado — alcance e mix subiram juntos.

- **Controle de dia da semana:** Entre as últimas quatro terças-feiras (`same_weekday_avg` R$5.404,72), hoje é a segunda maior GMV da série, atrás apenas de 28/04 (R$7.546,03, período pós-feriado). A +36,8% vs o próprio grupo sazonal (`changes.gmv_vs_same_weekday_pct`), o resultado não é explicável por sazonalidade de terça — a conta opera em nível estruturalmente superior aos seus pares temporais.

- **Trajetória intra-janela:** `avg_7d` (R$5.261,62) > `avg_30d` (R$4.696,25) > `avg_60d` (R$4.185,11) — progressão monotônica ascendente em GMV, confirmando aceleração contínua. O dia de hoje confirma e estende o vetor, não é pico isolado.

- **Hipóteses anteriores:** (1) Concentração IMB501: memória registrava escalada 44%→47,5%→56,5% — hoje Tampa Preta (40) + Tampa Cinza (12) + Tampa Vermelha (12) = 64 pedidos / 143 = **44,8%**, recuo aparente; hipótese de concentração crescente permanece em aberto, pois 25/05 era segunda de baixo volume total (efeito de denominador, não de demanda real do cluster). (2) Health dos campeões: `health=0,71` (MLB3288536143) e `health=0,75` (MLB4073003575) confirmados no mesmo patamar pelo **sétimo ciclo consecutivo** — degradação não avançou mas tampouco reverteu. (3) ACOS spike de 25/05 (14,15%): hoje recua para 10,96% com ROAS 13,9x, sugerindo que o pico era parcialmente efeito de segunda (baixo orgânico) — mas permanece elevado vs 22–23/05 (4,4%), não houve retorno à base.

---

### Leitura estratégica

- **Lente 1 — Patamar vs banda histórica:** A conta rompeu a banda de 60 dias com consistência entre janelas. Com `gmv_vs_7d_pct=+40,5%`, `gmv_vs_30d_pct=+57,5%` e `gmv_vs_60d_pct=+76,7%` convergindo na mesma direção, e o controle de dia da semana confirmando desempenho acima dos pares sazonais, o sinal qualifica como rompimento de patamar — não ruído, não acomodação. O único limitador para classificar como "em ganho de patamar consolidado" é a dependência estrutural que sustenta o resultado (ver Lente 5): o crescimento é real, mas a estrutura que o produz é frágil.

- **Lente 3 — Dependência e modalidade de envio:** O cluster IMB501 (MLB3288536143, três variações no mesmo anúncio) somou 64 pedidos = 44,8% do dia, integralmente via modalidade de envio Full. `top3_concentration=53,1%` e `top5_concentration=69,9%`. Os campeões do dia operaram 94,4% em modalidade de envio Full (`fulfillment_mix_yesterday_top10.full_pct`), contra 40,7% na base ativa (`account_overview.active_analysis.fulfillment_mix.full_pct`) — os campeões são exceção Full em uma base majoritariamente Cross-Docking (59,3%). A assimetria persiste da série anterior: ruptura de reposição no CD do ML nos dois anúncios principais (MLB3288536143 com `available_quantity=396` e MLB4073003575 com `available_quantity=78`) afetaria o vetor Full de forma desproporcional ao peso que Full representa na base geral.

- **Lente 4 — Buy Box catálogo vs ranking categoria:** Os dois campeões principais (MLB3288536143 e MLB4073003575) são Clássico (`gold_special`, `is_catalog=false`), competindo por ranking de categoria — não por Buy Box. Ambos operam com nível de qualidade do anúncio em zona regular (0,71 e 0,75 respectivamente), o que significa que o ML comprime progressivamente o posicionamento orgânico desses anúncios na categoria. O GMV subiu apesar dessa degradação porque ADS cobre a lacuna orgânica (confirmado pela Lente 5). Sinal crítico adicional: Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, `is_catalog=false`, Full) com `available_quantity=2` e 4 pedidos hoje — alta probabilidade de ruptura ativa; pedidos sobre estoque zero geram cancelamentos prospectivos com impacto em `cancellations_rate` numa janela em que o MercadoLíder Platinum está a ~10 dias.

- **Lente 5 — Mercado Ads vs orgânico:** ADS gerou R$4.484,87 (`revenue_ads_yesterday_brl`) com gasto R$321,93 (`spend_yesterday_brl`) — ROAS 13,9x, ACOS 10,96%. Esses números representam **60,6% do GMV do dia** (R$4.484,87 / R$7.394,36), mantendo a conta em zona **ADS dominante**. A eficiência do dia é forte (ROAS 13,9x, acima de 5x), mas não altera o diagnóstico estrutural: o orgânico responde por ~39% do volume, enquanto os dois campeões têm nível de qualidade do anúncio degradado que corrói ranking progressivamente. A dependência de ADS não é maquiagem de ineficiência hoje, mas é maquiagem de saúde orgânica declinante nos anúncios líderes.

- **Lente 6 — MercadoLíder:** Medalha atual MercadoLíder Gold confirmada (`power_seller_status=gold`, `real_level=null`, sem proteção ativa). Progresso para Platinum: `sales_60d_revenue_brl=R$253.539,34`, gap `R$42.460,66` (`platinum.gap_revenue_brl`), progresso 85,66%. Ritmo atual `R$4.225,66/dia`; ETA ~10 dias. O dia de hoje (R$7.394,36) opera 75% acima do ritmo necessário para o prazo corrente — a janela se comprime a cada dia nesse patamar. Métricas de qualidade fora de risco: `claims_rate=0,0022` (threshold 0,005), `cancellations_rate=0`, `delayed_handling_rate=0,0012`. A única ameaça à janela é o impacto prospectivo de cancelamentos automáticos decorrentes de rupturas ativas (Kit 6 Canecas Tulipa 250ml).

---

### Tese da conta

**Vulnerável.** A conta opera em patamar significativamente acima da banda histórica e em trajetória de aceleração consistente entre janelas — o resultado de hoje é o segundo maior de uma terça-feira na série e confirma expansão real de alcance, não apenas variação de ticket. No entanto, a estrutura que sustenta esse resultado é frágil em dois eixos simultâneos: os dois campeões Clássico em Full (que concentram 44,8%+ do volume via o cluster IMB501 + Kit 4 Potes 1050ml) operam em nível de qualidade regular pelo sétimo ciclo consecutivo, com ADS de Himmel preenchendo a lacuna orgânica que a degradação de ranking produz; e o ADS share em 60,6% coloca a conta em dependência estrutural de mídia paga sobre uma base orgânica que enfraquece silenciosamente. Crescimento real, sobre estrutura vulnerável.

---

### Risco estrutural principal

- **Risco:** Campeões Clássico em nível de qualidade do anúncio regular pelo sétimo ciclo consecutivo (MLB3288536143 `health=0,71`; MLB4073003575 `health=0,75`) com ADS ocupando sistematicamente a lacuna orgânica gerada pela compressão de ranking — dependência circular: quanto mais o orgânico é erodido, mais ADS sustenta o resultado, mas a causa raiz (nível de qualidade degradado) não é endereçada.
- **Por que importa:** Qualquer redução de verba, pausa de campanha ou pressão de ACOS que torne o investimento insustentável expõe o orgânico real dos dois campeões — que já opera com ranking comprimido pelo ML. A recuperação de nível de qualidade em anúncio Clássico é lenta (depende de métricas acumuladas de serviço e reviews); não há reversão rápida disponível. O crescimento de patamar registrado nas últimas semanas seria parcialmente artificial, construído sobre fundação que se corrói por baixo.
- **Histórico:** Presente desde ao menos 22/05 (primeira entrada na weekly com dado de health dos campeões) — não é novo. O que é novo hoje é o GMV mais alto, que amplia a superfície de risco: mais volume dependendo da mesma base frágil.
- **Sinal de confirmação:** ADS share acima de 65% por dois ciclos consecutivos com ACOS acima de 12% configura o ponto de escalonamento para alinhamento Yasmin–Himmel. Se, após qualquer ajuste de campanha, o GMV cair ≥ 25% em relação ao `avg_7d` atual (abaixo de ~R$3.950), confirma que o orgânico não sustenta o patamar sem cobertura de ADS.

---

### Sinais a observar

1. **MercadoLíder Platinum — iminência de promoção:** Com o dia em R$7.394,36 vs ritmo atual de R$4.225,66/dia, o gap `R$42.460,66` deve cair para abaixo de R$38k no próximo ciclo. Se `mercadolider.platinum.gap_revenue_brl` cruzar abaixo de R$30.000 com progresso acima de 90%, entra na janela de iminência — qualquer dia abaixo de R$3.500 a partir daí adia a conquista, e qualquer `cancellations_rate` acima de zero pode inviabilizar a promoção pelos limiares de qualidade independentemente do faturamento.

2. **Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090) — ruptura ativa:** Com `available_quantity=2` e 4 pedidos hoje (sétimo ciclo monitorado, memória de 22/05 já flagrava consumo de ~6 pedidos/dia com estoque 7→2), o próximo pacote deve mostrar ruptura confirmada. Se `status=paused` ou `available_quantity=0` com pedidos, confirma cancelamentos prospectivos entrando em `cancellations_rate` — sinal a cruzar com os thresholds de qualidade na janela de ETA Platinum.

3. **ACOS e ADS share — novo regime ou normalização:** A série dos últimos 4 ciclos (ACOS: 4,57%→4,43%→14,15%→10,96%; ADS share: 69,9%→49,5%→56,7%→60,6%) ainda não permite leitura de tendência. Se nos próximos 2 ciclos o ACOS se estabilizar abaixo de 8% com ADS share abaixo de 55%, o regime de eficiência de campanha se confirma dentro do histórico; se ACOS permanecer acima de 10% com share acima de 60% por dois dias seguidos, configura novo patamar de menor eficiência que justifica alinhamento Yasmin–Himmel sobre cobertura e mix de campanhas.