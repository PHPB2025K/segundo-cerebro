<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Robusta. weekly.md com 13 blocos diários (22/05–08/06), hipóteses ativas documentadas em série contínua, janelas 7d/30d/60d completas e sem ruptura operacional declarada. ml_snapshot com todos os blocos presentes e status ok — reputação, MercadoLíder, mix de modalidade de envio e ADS disponíveis. Base suficiente para tese forte.

---

### Leitura temporal

- **Rompimento de patamar em múltiplas janelas:** GMV de R$8.220 (`metrics.gmv`) está +33,9% vs `avg_30d.avg_gmv=R$6.140` (`changes.gmv_vs_30d_pct`) e +62,6% vs `avg_60d.avg_gmv=R$5.057` (`changes.gmv_vs_60d_pct`). Não é oscilação dentro de banda: a conta opera ~40% acima do nível médio dos últimos 60 dias, com o ganho embutido progressivamente nas três janelas (7d R$7.359 > 30d R$6.140 > 60d R$5.057). Ticket acompanha: +10,7% vs 60d (`changes.ticket_vs_60d_pct`), o que indica melhora de mix, não apenas de volume.

- **Série de terças — primeiro recuo após 4 semanas de alta:** A série de mesmos dias da semana foi monotonicamente ascendente de R$4.081 (12/05) → R$5.760 (19/05) → R$7.394 (26/05) → R$9.154 (02/06). O dia (R$8.220) é o primeiro ponto negativo nessa série (-10,2% vs 02/06), mas ainda +24,6% vs a média das 4 terças anteriores (`same_weekday_avg.avg_gmv=R$6.597`). O recuo interrompe a aceleração, não a tendência de alta.

- **Hipóteses anteriores — duas fechadas neste ciclo:** (1) A hipótese de expansão orgânica acumulou o 9º ponto consecutivo de queda de ADS share: 69,9% (22/05) → 44,3% hoje (calculado: `revenue_ads=R$3.644/gmv=R$8.220`). Com dois ciclos consecutivos abaixo de 50% e ROAS 14,9x, a hipótese transita para fato: orgânico sustenta estruturalmente, ADS amplifica. (2) MercadoLíder Platinum confirmado no snapshot: `power_seller_status=platinum`, `sales_60d_revenue_brl=R$308.840` vs threshold R$296.000, `gap_revenue_brl=0`, `progress_pct=100%`. Hipótese ativa desde 05/06 encerrada.

- **7d vs 30d:** `avg_7d.avg_orders=161` vs `avg_30d.avg_orders=128,3` (`changes.orders_vs_7d_pct=+4,3%`; `orders_vs_30d_pct=+30,9%`). O patamar recente (7d) já é consistentemente acima do mês. A aceleração não é puxada por um dia atípico — é o nível atual da conta.

---

### Leitura estratégica

- **Lente 1 + 6 — Patamar e MercadoLíder:** A confirmação do Platinum (`power_seller_status=platinum`, `sales_60d=R$308.840`, excedente de R$12.840 acima do threshold) encerra o capítulo de perseguição e abre o de manutenção. O ritmo diário atual de R$5.147 (`mercadolider.ritmo_diario_brl`) está 4,4% acima do mínimo necessário para sustentar o threshold (R$296.000/60 ≈ R$4.933/dia). O patamar é adequado para manter — mas a margem de segurança não é larga, e o risco real agora não é volume; é `cancellations_rate` saindo de zero na janela oficial ML. O dia teve 6 cancelamentos (`metrics.cancelamentos`) sem atribuição por anúncio possível pelo pacote; `cancellations_rate=0` na janela longa da API reflete o histórico acumulado, não o fluxo recente. O acúmulo de cancelamentos diários (~3-6 nos últimos ciclos) pode começar a aparecer na janela oficial a qualquer momento.

- **Lente 3 — Dependência estrutural de anúncio e modalidade de envio:** Top3 em 53,6% (`top3_concentration`), top5 em 66,7% (`top5_concentration`), com `paused=131` vs `active=77` confirmando cauda morta dominante (proporção 1,70 — acima do limiar de 1,5). Os líderes operam majoritariamente em Full (`fulfillment_mix_yesterday_top10.full_pct=75,3%`), enquanto a base ativa é 42,9% Full / 57,1% Cross-Docking (`account_overview.active_analysis.fulfillment_mix`). Campeões são exceção, não norma — a estreiteza estrutural do topo (2-3 anúncios Full carregando ~50%+ do volume) é crônica desde ao menos 22/05 e não mostrou reversão em nenhuma janela disponível. **Hipótese:** a estabilidade do patamar atual é função direta do abastecimento contínuo de um punhado de SKUs Full — ruptura em qualquer um dos top 2 afeta ~40-50% do volume imediatamente.

- **Lente 4 — Ranking de categoria e saúde dos anúncios:** 100% dos top 10 são `is_catalog=false` — sem exposição de Buy Box Catálogo neste conjunto. O risco de exposição orgânica em ranking é inteiramente determinado pelo nível de qualidade dos anúncios. Campeão MLB3288536143 (`health=0,71`, nível regular — 18º+ ciclo idêntico), MLB4073003575 (`health=0,75`, nível regular), MLB5402326666 (`health=0,66`, nível preocupante — 6º ciclo) e MLB4931700052 (`health=0,75`, nível regular). Com ADS share caindo de 69,9% para 44,3% ao longo de 18 dias, o escudo pago que compensava parcialmente a degradação orgânica está diminuindo. O crescimento atual ocorre *apesar* da degradação crônica do nível de qualidade — não por causa de sua recuperação.

- **Lente 5 — Mercado Ads:** ROAS 14,9x (R$3.644/R$244,53), ACOS 6,31% (`ads_summary.avg_acos_pct`), ADS share 44,3%, 13 campanhas ativas. O 9º ponto descendente consecutivo da série de ADS share confirma como fato o que era hipótese desde 01/06: o orgânico está crescendo proporcionalmente mais rápido que a campanha. Não há ineficiência de ADS a endereçar — Himmel opera dentro do envelope de máxima eficiência (ROAS > 8x, ACOS < 10%). O movimento de queda de share é estrutural, não operacional.

---

### Tese da conta

**Vulnerável — com novo patamar conquistado mas sustentação estruturalmente concentrada.**

A conta atingiu MercadoLíder Platinum e opera inequivocamente em novo patamar (+62,6% vs avg_60d). A expansão orgânica está confirmada como fato após 9 ciclos consecutivos de queda de ADS share (69,9% → 44,3%) com GMV ascendente — não é campanha inflando resultado. No entanto, a sustentação deste patamar repousa sobre 2-3 anúncios Full com nível de qualidade degradado cronicamente (`health=0,71` por 18+ ciclos no líder; `health=0,66` por 6 ciclos em MLB5402326666) e cauda morta dominante (paused 131 vs active 77). O crescimento acontece apesar da degradação, não porque ela foi resolvida — qualquer recuperação de nível de qualidade nos campeões representaria um vetor adicional de crescimento orgânico ainda não ativado. Enquanto o segundo vetor Full de peso comparável não emergir e o nível de qualidade dos líderes permanecer degradado sem direção, a conta é **vulnerável na estrutura**, mesmo sendo saudável no número.

---

### Risco estrutural principal

**Risco:** Degradação crônica do nível de qualidade dos anúncios campeões Full — MLB3288536143 em `health=0,71` (nível regular, 18º+ ciclo idêntico), MLB5402326666 em `health=0,66` (nível preocupante, 6º ciclo), MLB4073003575 e MLB4931700052 ambos em `health=0,75` (nível regular, ciclos consecutivos) — sem direção observável e sem intervenção documentada.

**Por que importa:** Anúncios em nível regular e nível preocupante recebem posicionamento progressivamente inferior em ranking de categoria pelo ML. MLB3288536143 concentrou 42,9% do volume do dia (70 pedidos) e está há 18+ ciclos em nível regular sem qualquer variação registrada. Com ADS share em queda sistemática (44,3%), o componente pago que parcialmente compensava essa degradação está encolhendo — se o health cair abaixo de 0,70 no líder, o impacto em exposição orgânica será imediato e sem amortecedor proporcional. O risco não é de ruptura operacional pontual; é de erosão lenta de visibilidade no canal que pode reverter silenciosamente o ganho de patamar.

**Histórico:** Presente desde 22/05 (primeiro registro disponível). MLB3288536143 em 0,71 há 18+ ciclos, MLB4073003575 em 0,75 por ciclos consecutivos, MLB5402326666 entrou em nível preocupante em 02/06 e persistiu por 6 ciclos. Nenhuma intervenção documentada. O risco é crônico, não novo.

**Sinal de confirmação:** `health` de MLB3288536143 abaixo de 0,70 no próximo snapshot, OU `health` de MLB5402326666 abaixo de 0,63 em dois ciclos consecutivos, confirma deterioração em curso vs estabilização no patamar atual. Adicionalmente: com `no_health_data_count=59` de 77 anúncios ativos, a leitura de saúde sistêmica da base é parcial — o risco pode ser mais abrangente do que o top 10 indica.

---

### Sinais a observar

1. **Kit 4 Potes 1050ml (MLB4073003575) — cobertura iminente:** `available_quantity=28` com 20 pedidos no dia = runway estimado ≤ 1,4 dias sem restock. Padrão recorrente desde ao menos 26/05 (chegou a 2 unidades em 02/06, restock insuficiente documentado em 08/06). Se o próximo snapshot mostrar `available_quantity < 10` ou `status=paused`, confirma a terceira ruptura do ciclo — impacto direto em ~11,9% do volume do dia e pressão adicional sobre `cancellations_rate` da reputação Platinum.

2. **Série de terças — acomodação ou reversão:** 06/09 (R$8.220) foi o primeiro recuo na série de terças após 4 semanas de alta consecutiva. Se 06/16 fechar acima de R$9.000, a série retoma aceleração e a tese de ganho de patamar consolida; se fechar abaixo de R$7.500 por dois terças consecutivas, configura acomodação real do novo patamar, não continuação de alta.

3. **ADS share abaixo de 40% pelo segundo ciclo consecutivo:** 9 pontos descendentes confirmam expansão orgânica como fato; o próximo limiar relevante é 40%. Se 06/10 fechar com ADS share abaixo de 40%, consolida que o orgânico já sustenta a maioria do faturamento de forma autônoma — e que qualquer revisão de campanha por Himmel (pausa, redução de verba) causaria impacto limitado no volume total, sinalizando saúde estrutural de tráfego acima do patamar de campanha-dependência.