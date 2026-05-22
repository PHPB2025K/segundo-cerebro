<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Memória robusta em histórico de janelas (7d/30d/60d com cobertura 100%), ml_snapshot completo (reputação, fulfillment, ads, account overview). Ressalvas: `weekly.md` e `monthly.md` são templates vazios — sem tese acumulada ou hipóteses anteriores para confirmar ou refutar; a leitura de hoje é ponto de ancoragem, não confirmação de trajetória já mapeada. `last_daily_file: 2026-05-20.md` indica continuidade operacional, mas o conteúdo não veio no pacote, portanto hipóteses da véspera ficam inacessíveis.

---

### Leitura temporal

- **60d → 30d → 7d → dia: escalada de ticket consistente em todas as janelas.** `avg_ticket_60d = R$42,05` → `avg_ticket_30d = R$44,36` → `avg_ticket_7d = R$47,25` → `ticket_dia = R$60,83`. Nenhuma janela reverte o movimento; a aceleração se intensifica nos últimos 7 dias. O GMV de hoje (R$6.082,82) está +56,5% vs 60d e +38% vs 30d sem crescimento equivalente de volume (`orders_vs_60d_pct = +8,2%`; `orders_vs_30d_pct = +0,7%`). O canal não cresceu em alcance — cresceu em valor por pedido.

- **Volume recuou vs semana recente, mas não vs patamar de mais longo prazo.** `orders_vs_7d_pct = -15,9%` (118,9 → 100), mas `orders_vs_30d_pct = +0,7%` e `orders_vs_60d_pct = +8,2%`. A última semana teve volume acima do padrão; o dia de hoje é o 30d em volume mas supera o 30d com folga em GMV. Não é queda de patamar — é normalização de volume sobre base ticket elevada.

- **Controle de sazonalidade (quintas-feiras) reforça o sinal de ticket, não de volume.** Últimas 4 quintas: 81/3.608 → 115/5.420 → 75/3.176 → 140/6.540. O GMV de hoje (R$6.082) é o segundo maior da série, com apenas 100 pedidos — abaixo da quinta passada (140 pedidos) mas 29,8% acima da média do dia da semana em GMV (`gmv_vs_same_weekday_pct = +29,8%`). O ticket de hoje (R$60,83) destoa de todas as quintas anteriores — indica que a aceleração de ticket não é artefato de dia específico.

- **Sem hipóteses anteriores registradas para refutar ou confirmar** — `weekly.md` e `monthly.md` são templates. A escalada de ticket é o padrão dominante observável com base disponível; não há tese prévia a testar contra ele.

---

### Leitura estratégica

- **A escalada de ticket é o vetor estratégico da conta, mas sua origem está encoberta por dependência de ADS.** `ads_summary.revenue_ads_yesterday_brl = R$4.593,66` sobre `gmv = R$6.082,82` representa **ADS share de 75,5%** — bem acima do limiar de fragilidade latente (≥50%). ROAS calculado: R$4.593,66 / R$341,72 = **13,4x**; ACOS: 4,71%. Himmel opera com eficiência excepcional, mas 3 em cada 4 reais do GMV dependem das campanhas ativas. Se o ticket mais alto reflete mix de produto direcionado por campanhas (kits de maior valor em destaque), parte do ganho de ticket pode ser construção de ADS, não demanda orgânica estrutural. Não há como separar os dois vetores com os dados disponíveis.

- **O mix de fulfillment do dia diverge sistematicamente do padrão recente, sinalizando uma mudança de liderança de produto.** `fulfillment_mix_7d.full_pct = 77%` vs `fulfillment_mix_yesterday_top10.full_pct = 20%`. Isso significa que os 6 dias anteriores à janela foram Full-dominantes em ~85%+, mas ontem o top 10 foi 80% Cross-docking. O motivo é estrutural no portfólio: os três campeões de volume do dia — Conjunto 5 Potes Tampa Preta (31 pedidos, MLB4535865317), Conjunto 5 Potes Tampa Cinza (13 pedidos, MLB4535865311) e Conjunto 5 Potes Tampa Vermelha (8 pedidos, MLB4535659243) — são todos `logistic_type: cross_docking`, com estoque folgado (8.379 / 9.197 / 8.283 unidades) e `health: null`. Quando a família IMB501 domina, o perfil de fulfillment da conta muda radicalmente, o que tem implicações para a velocidade de entrega e a elegibilidade competitiva no ranking.

- **Dois anúncios Full em zona de ruptura iminente no top 10.** `MLB4410218897` (Kit 06 Canequinhas Acrílico) tem `available_quantity = 2` com 3 pedidos no dia — ruptura técnica em andamento; esses pedidos provavelmente resultam em cancelamentos que impactam `reputation.cancellations_rate` nos próximos ciclos. `MLB6167272090` (Kit 6 Canecas Porcelana 250ml) tem `available_quantity = 19` com 5 pedidos no dia — estoque para ~3–4 dias no ritmo atual; item em Full sem reposição visível no pacote. Nenhum dos dois é campeão de volume, mas ambos são Full, e ruptura em Full tem recuperação mais lenta do que em Cross-docking.

- **A saúde estrutural da conta como registrada pela API ML é sólida, mas com lacuna de visibilidade relevante.** `reputation.color = 5_green`, `power_seller_status = gold`, `cancellations_rate = 0`, `claims_rate = 0,25%`, `delayed_handling_rate = 0,1%` — todos dentro de parâmetros saudáveis. Contudo, `account_overview.active_analysis.no_health_data_count = 65` dos 83 ativos não têm health calculado, e `low_health_count = 7` inclui `MLB4073003575` (Kit 4 Potes 1050ml Retangular) com `health = 0,75` — abaixo do limiar de penalização (0,85). O Kit 4 Potes é um anúncio Full com 8 pedidos no dia; exposição orgânica degradada nele pode estar sendo compensada por ADS sem que a conta perceba o vazamento de ranking.

---

### Tese da conta

**Vulnerável.** O GMV está em patamar historicamente elevado — +56,5% vs 60d, +38% vs 30d — sustentado por escalada de ticket consistente em todas as janelas disponíveis. Essa é a melhor leitura financeira dos últimos dois meses. Mas a estrutura que sustenta esse resultado é frágil em três dimensões simultâneas: 75,5% do GMV atribuído a Mercado Ads sem confirmação do que o orgânico sustentaria sozinho; cauda morta dominante (173 anúncios pausados contra 83 ativos, ratio 2,1:1) indicando que a conta vive de um portfólio estreito; e dois anúncios Full próximos da ruptura no top 10. A conta está performando bem no número e mal na estrutura que suporta o número — sem weekly/monthly acumulados, não é possível confirmar se essa configuração é padrão histórico ou acumulação recente de fragilidade.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads acima de 75% do GMV sem evidência de base orgânica estrutural.

**Por que importa:** Com ADS share de 75,5%, qualquer pausa, redução de orçamento ou perda de eficiência nas campanhas de Himmel impacta diretamente 3/4 do faturamento. O crescimento de ticket pode parcialmente refletir direcionamento de tráfego pago para SKUs de maior valor — se for o caso, o ticket cairia junto com o GMV ao pausar campanhas. A conta não tem segunda camada de sustentação visível: cauda com 173 anúncios pausados, top 3 concentrando 60% do volume, orgânico indistinguível do ADS nos dados disponíveis.

**Histórico:** Dado indisponível — sem tese semanal ou mensal acumulada para confirmar se essa dependência de ADS é padrão de longa data da conta ou configuração recente. A partir do pacote de hoje, é a primeira leitura com share calculável.

**Sinal de confirmação:** ADS share acima de 65% por 3 dos próximos 5 dias confirma dependência estrutural; queda de GMV proporcional à queda de investimento ADS em qualquer ciclo de teste confirma que o orgânico não sustenta o patamar atual.

---

### Sinais a observar

1. **ADS share permanecendo acima de 70% pelos próximos 3 dias confirma que o crescimento de GMV e a escalada de ticket são ADS-dependentes, não refletem demanda orgânica estrutural** (calculável via `ads_summary.revenue_ads_yesterday_brl / gmv` a cada ciclo).

2. **Kit 06 Canequinhas Acrílico (`MLB4410218897`, `available_quantity = 2`) gerando cancelamentos nos próximos 1–2 ciclos** — se `metrics.cancelamentos` subir acima de 5 pedidos/dia em mais de um dia consecutivo, é sinal precoce de erosão de `reputation.cancellations_rate` antes de aparecer na métrica oficial da API.

3. **Ticket médio abaixo de R$50 por 2 dias seguidos indicaria reversão do mix de produto** — se a família IMB501 (Cross-docking, ticket mais baixo) ceder liderança para os kits YW (Cross-docking, ticket mais alto) ou os anúncios Full, o ticket se sustenta; se o oposto ocorrer, o patamar de GMV atual se revela dependente da composição específica de hoje, não tendência consolidada.