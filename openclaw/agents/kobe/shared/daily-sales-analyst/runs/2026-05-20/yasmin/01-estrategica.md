<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` estão em estado de template — sem entradas históricas preenchidas. Esta é a leitura inaugural documentada da conta ML; não há hipóteses ativas anteriores para confirmar ou refutar. Base factual disponível: métricas do dia, históricos numéricos 7/30/60d e `ml_snapshot` completo com reputação, fulfillment mix, ADS e health dos anúncios. Confiança alta nos fatos do pacote; confiança baixa em trajetória interpretada, pela ausência de memória semanal e mensal.

---

### Leitura temporal

- **vs 60d (patamar bimestral):** GMV de R$5.087,71 está +33,3% acima da média bimestral de R$3.817,90 (`changes.gmv_vs_60d_pct`), com ticket médio R$55,91 vs R$41,86 (+33,6%) e pedidos praticamente estáveis (91 vs 91,2 médio, `changes.orders_vs_60d_pct=-0,2%`). A conta cresceu em valor unitário, não em volume — o padrão é consistente e não é ruído.

- **vs 30d (patamar mensal):** GMV +15,7% (`changes.gmv_vs_30d_pct`), ticket +27,0%, pedidos -8,9%. O mesmo padrão: ticket compensa e supera a queda de volume. A conta opera acima da banda de 30 dias em GMV mesmo vendendo menos pedidos.

- **vs mesmo dia da semana (sazonalidade):** Média dos 4 pares de quarta: R$3.841,73 / 92,5 pedidos (`same_weekday_avg`). Ontem: R$5.087,71 / 91 pedidos — GMV +32,4%, volume plano (-1,6%). O resultado não é explicado por sazonalidade favorável; é estrutural. A quarta de 2026-04-29 (R$5.618,66) é o único par próximo — hipótese de que o patamar atual subiu a partir do fim de abril, ainda sem memória para confirmar.

- **vs 7d (movimento recente):** Média dos últimos 7d: 115,1 pedidos / R$5.315,70 (`avg_7d`). Ontem ficou -20,9% em pedidos e -4,3% em GMV contra essa janela. A janela de 7d é a mais alta de todas, sugerindo dias recentes acima do padrão. Ontem representa acomodação dentro de uma janela elevada, não queda real — especialmente confirmado pelo controle de dia da semana.

---

### Leitura estratégica

- **Ticket como vetor estrutural (Lente 1 — patamar):** A conta não cresceu em alcance — cresceu em valor unitário. Pedidos estáveis vs 60d (-0,2%) enquanto GMV avança +33,3% é assinatura de mix shift: os anúncios que convertem são de ticket mais alto (kits maiores, conjuntos, variações de maior quantidade). O movimento aparece em todas as janelas (30d, 60d, mesmo dia da semana), impedindo classificação como ruído. Hipótese inaugural — sem memória para confirmar: a Budamix migrou progressivamente para SKUs de maior valor unitário no ML, elevando o ticket médio da conta de ~R$42 para ~R$56 no bimestre.

- **ADS como vetor dominante, com eficiência alta (Lente 5 — ADS vs orgânico):** ADS gerou R$3.041,56 (`revenue_ads_yesterday_brl`) com gasto de R$262,19 (`spend_yesterday_brl`) — ROAS 11,6x, ACOS 4,64% (`avg_acos_pct`). Esses números representam **59,8% do GMV do dia** (R$3.041,56 / R$5.087,71), colocando a conta em zona de **ADS dominante**. A eficiência das 11 campanhas ativas de Himmel é alta, mas há fragilidade latente: qualquer redução de verba ou pausa expõe uma base orgânica não dimensionada. Sem histórico de ADS share em weekly/monthly, não é possível dizer se essa dominância é nova ou padrão consolidado.

- **Saúde degradada em dois campeões (Lente 4 — ranking categoria):** `Kit 4 Potes 1050ml` (`MLB4073003575`, 2º lugar com 13 pedidos) tem `health=0,75` e `Conjunto 5 Potes Tampa Vermelha` (`MLB3288536143`, 5º lugar com 5 pedidos) tem `health=0,71` — ambos abaixo do limiar de penalização ML de 0,85. Esses dois anúncios são Clássicos (`is_catalog=false`) competindo por ranking de categoria MLB244658; health degradada implica perda progressiva de exposição orgânica. O fato de continuarem convertendo com health baixa reforça a hipótese de que ADS está compensando o que o algoritmo orgânico está retirando.

- **Portfólio com cauda morta e campeões em Full muito acima da base (Lente 3 — dependência):** 174 anúncios pausados para 82 ativos (proporção 2,1:1, contra limiar de atenção 1,5:1) confirma que a conta opera sobre base restrita. O mix fulfillment revela assimetria relevante: a base ativa tem 34,1% Full (`account_overview.active_analysis.fulfillment_mix.full_pct`), mas o fluxo real de pedidos nos últimos 30d e 7d é 73,9% e 77,7% Full — os anúncios em Full carregam mais de 2× sua representação no catálogo. Ontem os top10 puxaram para 56,3% Full (menos que o 7d) porque o líder, `Conjunto 5 Potes Tampa Preta` (23 pedidos), opera em cross_docking. Ruptura de estoque em CD do ML em qualquer campeão Full tem impacto desproporcional ao peso declarado na base.

---

### Tese da conta

**Vulnerável.** A conta ML da Budamix está em ganho de GMV real — confirmado nas janelas de 30d, 60d e mesmo dia da semana — sustentado por elevação estrutural de ticket médio (de ~R$42 para ~R$56 no bimestre), não por expansão de alcance. A estrutura por trás é frágil em três eixos simultâneos: (1) ADS representa 59,8% do faturamento do dia com ROAS 11,6x — eficiente, mas qualquer interrupção nas campanhas de Himmel expõe uma base orgânica não dimensionada; (2) dois campeões de alto giro operam com `health=0,75` e `health=0,71` — penalização ML ativa, com risco de perda progressiva de ranking de categoria; (3) portfólio com 174 pausados para 82 ativos e campeões em Full respondendo por proporção muito acima da sua representação no catálogo. Âncora positiva: reputação verde-ouro limpa (`color=5_green`, `power_seller_status=gold`, `cancellations_rate=0`, `transactions_canceled=0`), o que preserva elegibilidade estrutural para Mercado Líder — mas não neutraliza as fragilidades de composição.

---

### Risco estrutural principal

- **Risco:** Dependência de Mercado Ads em conta com health degradada nos campeões — ADS compensa organicamente o que a penalização ML está retirando em exposição de ranking. `Kit 4 Potes 1050ml` (`health=0,75`) e `Conjunto 5 Potes Tampa Vermelha` (`health=0,71`) são anúncios Clássicos de alto giro que perderam poder de ranking orgânico; a continuidade das vendas nesses itens depende de que as campanhas de Himmel mantenham cobertura sobre eles.
- **Por que importa:** A conta pode estar em equilíbrio instável — números saudáveis hoje, estruturalmente dependentes de investimento em ADS mascarando deterioração de listagem. Se o ACOS subir (lances mais caros em leilão) ou Himmel pausar campanhas que cobrem esses anúncios, a queda de GMV pode ser desproporcional à redução de verba, porque o ranking orgânico já não está funcionando como backup.
- **Histórico:** Sem weekly/monthly preenchidos — primeira leitura documentada. Não é possível afirmar se a degradação de health é recente ou crônica.
- **Sinal de confirmação:** `Kit 4 Potes 1050ml` ou `Conjunto 5 Potes Tampa Vermelha` com queda de pedidos em 2 dias seguidos sem redução declarada de verba ADS por Himmel confirma que o ranking orgânico desses itens está cedendo e o ADS não está sendo suficiente para compensar.

---

### Sinais a observar

1. **Health dos campeões não recuperando** — `Kit 4 Potes 1050ml` (`health=0,75`) e `Conjunto 5 Potes Tampa Vermelha` (`health=0,71`) mantendo ou piorando `health` por 3 dias seguidos confirma deterioração progressiva de ranking orgânico em MLB244658 e eleva o risco estrutural de dependência de ADS para esses itens.

2. **Ruptura iminente em Kit 06 Canequinhas Acrílico** (`MLB4410218897`, `available_quantity=3`, 3 pedidos ontem) — se o anúncio sair do ar por esgotamento nos próximos 1-2 dias, confirma vulnerabilidade de gestão de estoque em cauda de alto giro acumulado (`sold_quantity=455`). Sinal adjacente: `Kit 6 Canecas Porcelana Tulipa` (`MLB6167272090`, `available_quantity=21`, giro de 5 pedidos/dia) tem runway estimado de ~4 dias.

3. **ADS share acima de 50% por 3 dias consecutivos** — se a proporção receita Himmel / GMV total permanecer acima de 50% ao longo da semana (se `ads_summary` disponível no pacote), consolida a leitura de dependência estrutural de mídia paga e invalida hipótese de orgânico autônomo como base da conta.