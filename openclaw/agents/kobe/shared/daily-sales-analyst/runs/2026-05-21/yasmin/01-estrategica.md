<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

weekly.md e monthly.md chegaram como templates vazios — sem teses semanais, hipóteses ativas ou padrões acumulados. O daily anterior (2026-05-20.md) é referenciado mas não forneceu conteúdo para esta sessão. As janelas numéricas (7d/30d/60d) estão completas com cobertura 100% em `logistic_type`; `ml_snapshot` entregou reputação, mix de modalidade de envio, ADS e MercadoLíder — base quantitativa robusta. Esta leitura é ponto de partida analítico: não há hipóteses anteriores para confirmar ou refutar.

---

### Leitura temporal

- **7d vs ontem:** Pedidos de ontem (101) estão -15,1% abaixo da média 7d (118,9), mas o GMV está +8,8% acima (R$ 6.113 vs avg R$ 5.616). A média 7d carrega uma quinta (14/05) com 140 pedidos e R$ 6.540 — outlier de volume que ontem não repetiu em quantidade, mas superou em ticket. O sinal é: volume recuou, valor sustentou.

- **30d e 60d — rompimento de patamar:** GMV de ontem está +38,7% acima da média 30d (R$ 4.407, campo `changes.gmv_vs_30d_pct`) e +57,1% acima da média 60d (R$ 3.892, `changes.gmv_vs_60d_pct`). Pedidos estão apenas +1,7% e +6,0% nas mesmas janelas. O ticket percorreu R$ 40,86 → R$ 44,36 → R$ 47,25 → R$ 60,52 ao longo de 60d→30d→7d→ontem — expansão consistente, não salto isolado.

- **Controle de dia da semana (quintas):** Ontem ficou +30,5% acima da média das últimas 4 quintas em GMV (`changes.gmv_vs_same_weekday_pct=+30,5%`), com pedidos -1,7% (`orders_vs_same_weekday_pct`). Controlando sazonalidade, o GMV está estruturalmente acima do padrão de quinta. A quinta de 07/05 (R$ 3.176) funcionou como piso; a de 14/05 (R$ 6.540) como teto recente — ontem ficou entre esses dois extremos.

- **Trajetória ticket vs volume:** A dissociação entre GMV crescendo (+57% em 60d) e pedidos crescendo marginalmente (+6% em 60d) é a leitura central da conta. Não é um canal ganhando alcance — é um canal ganhando valor por pedido. Isso exige explicação por mix de produto, não por volume de mercado.

---

### Leitura estratégica

- **Ticket-led growth com emergência de novo cluster de produto:** A expansão de ticket de R$ 40,86 (60d avg) para R$ 60,52 (ontem) coincide com os Conjuntos 5 Potes de Vidro (Tampa Preta/Cinza/Vermelha — família IMB501) ocupando o top 3 e somando 53 dos 101 pedidos (52,5%) em um único dia. Esses anúncios têm `logistic_type=cross_docking`, `is_catalog=false`, `health=null` (sem penalização calculada) e estoques amplos (8.378/9.197/8.283 unidades). **Fato:** família IMB501 domina volume e, por ser de ticket mais alto, puxa o ticket médio para cima. **Hipótese:** a ascensão desse cluster está sendo amplificada por ADS e pode estar deslocando produtos Full que dominavam a janela 7d.

- **Discrepância estrutural de modalidade de envio:** O mix de ontem no top 10 foi 80,2% Cross-Docking / 19,8% Full (`fulfillment_mix_yesterday_top10`), invertendo o padrão da janela 7d (Full 77%, Cross-Docking 23%, `fulfillment_mix_7d`) e diferindo expressivamente da base ativa (Full 33,3%, Cross-Docking 66,7%, `account_overview.active_analysis.fulfillment_mix`). Isso significa que a janela 7d ainda carrega o peso de produtos Full que não lideraram ontem. Se os campeões Cross-Docking (família IMB501) sustentarem esse ritmo, o mix da conta em janelas curtas convergirá para mais Cross-Docking — com impactos em exposição e ranking que dependem de entender se esses anúncios têm posicionamento orgânico estável ou são movidos majoritariamente por ADS.

- **ADS como motor isolado — eficiência excepcional e dependência estrutural:** Himmel operou ontem com gasto de R$ 341,72 e receita atribuída de R$ 4.593,66 — ROAS de **13,44x** e ACOS de **4,71%** (`ads_summary`). Esses números representam **75,1% do GMV do dia** (R$ 4.594 / R$ 6.113), colocando a conta em **zona de ADS dominante**. A eficiência é notável, mas a dependência é estrutural: sem o orgânico mensurável de forma isolada, não há como avaliar qual patamar a conta sustenta por conta própria. O ganho de patamar de GMV que os números mostram pode ser real — ou pode ser uma amplificação de ADS que mascara a base orgânica real.

- **Cauda parada e concentração de família:** Com 173 anúncios pausados para 84 ativos (ratio 2,06x, limiar crítico: 1,5x per Lente 3), a conta opera com cauda morta dominante. O `top3_concentration=59,4%` é concentrado em variações de cor de uma única família (IMB501). A dependência não é apenas de anúncio — é de família inteira. Dois alertas adicionais: (a) Kit 4 Potes 1050ml (MLB4073003575) tem `health=0,75` — abaixo do limiar de 0,85, com penalização de exposição orgânica em curso; (b) Kit 06 Canequinhas Acrílico (MLB4410218897) tem `available_quantity=1` e gerou 3 pedidos ontem — ruptura nas próximas horas.

---

### Tese da conta

A conta Mercado Livre está **em ganho de patamar**, sustentado por expansão de ticket médio ao longo de 60 dias — não por crescimento de volume. O motor visível desse movimento é o Mercado Ads operado por Himmel (ROAS 13,44x, 75,1% do GMV), com a família IMB501 de potes de vidro emergindo como cluster dominante via Cross-Docking. O patamar de GMV é real nos números; a fragilidade está na estrutura: 75% de dependência de ADS sem orgânico isolável, cauda morta dominante (2:1 pausados/ativos), e base de memória qualitativa zerada que impede avaliar se esse ganho é trajetória nova ou reprise de padrão já observado. A tese é construída exclusivamente sobre janelas numéricas — robustas, mas sem confirmação histórica acumulada.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads como único vetor verificável de GMV, sem orgânico autônomo mensurável.

**Por que importa:** Com 75,1% do faturamento atribuído às campanhas de Himmel (`ads_summary.revenue_ads_yesterday_brl / totals.gmv`), qualquer pausa, corte de verba ou queda de eficiência de campanha afeta o GMV diretamente sem amortecedor. O ganho de patamar documentado nas janelas 30d e 60d pode estar sendo sustentado pela mesma estrutura — o que significaria que o "novo patamar" é dependente de um nível de investimento em ADS que, se reduzido, revela um piso orgânico ainda desconhecido. Adicionalmente, a cauda morta (173 pausados vs 84 ativos) concentra o tráfego em poucos anúncios, amplificando a exposição de cada falha.

**Histórico:** Primeira leitura estruturada — weekly/monthly vazios. Não é possível afirmar se a dependência é crônica ou emergiu com a ascensão da família IMB501. Primeiro registro.

**Sinal de confirmação:** ADS share acima de 60% por 3 dias consecutivos confirma dependência estrutural. A leitura do orgânico isolado requer teste coordenado com Yasmin/Himmel: redução monitorada de verba por 2-3 dias para observar piso de GMV.

---

### Sinais a observar

1. **Ticket médio acima de R$ 55 por 3 dias consecutivos** confirma que o mix de produtos de maior valor (família IMB501 + kits 1050ml) está consolidando novo patamar estrutural de ticket — não foi evento pontual do dia. Ticket abaixo de R$ 48 por 2 dias seguidos indica reversão para o patamar anterior.

2. **Kit 06 Canequinhas Acrílico (MLB4410218897) com `available_quantity=1`:** qualquer pedido adicional nas próximas 24h vira cancelamento prospectivo garantido. Ruptura aqui impacta `reputation.cancellations_rate` (atualmente zerada na janela oficial da API) e o `delayed_handling_rate`. Verificar com Yasmin reabastecimento imediato; se não houver, pausar o anúncio evita dano à reputação. Kit 6 Canecas Tulipa (MLB6167272090, `available_quantity=14`, 5 pedidos/dia) tem runway de ~3 dias — segundo alerta operacional.

3. **MercadoLíder Platinum — ritmo abaixo de R$ 3.940/dia por 5 dias consecutivos** desacelera o ETA atual de 15 dias estimados para fechar o gap de R$ 59.091 (`mercadolider.platinum.gap_revenue_brl`). Ontem (R$ 6.113) contribuiu bem acima do ritmo necessário — mas se o dia foi puxado por ADS excepcional não recorrente, dias mais fracos consumirão o colchão acumulado. O monitoramento é do GMV diário vs R$ 3.939/dia de ritmo necessário; dias abaixo por semana seguida mudam a leitura de "iminente" para "em risco de atraso".