<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Pacote ML robusto: `ml_snapshot` completo com reputação, mix fulfillment (7d, 30d, top10), detalhes dos top 10 e account overview (coverage 100%). Ressalva relevante: `weekly.md` e `monthly.md` são templates sem entrada histórica — sem hipóteses ativas registradas para confirmar ou refutar, esta leitura serve como referência inaugural, não confirmação de tese. `last_daily_file: 2026-05-20.md` referenciado, mas não entregue no pacote; hipóteses do dia anterior são irrecuperáveis nesta sessão.

---

### Leitura temporal

- **vs 60d** (`changes.gmv_vs_60d_pct=+56.5%`, `ticket_vs_60d_pct=+44.7%`, `orders_vs_60d_pct=+8.2%`): O GMV de ontem é 56% acima da média bimestral com pedidos quase planos. A trajetória de ticket é a causa — R$42,05 (60d) → R$44,36 (30d) → R$47,25 (7d) → R$60,83 (ontem). Escalada consistente em todas as janelas; não é pico isolado.

- **vs 30d** (`gmv_vs_30d_pct=+38.0%`, `orders_vs_30d_pct=+0.7%`): Mesma leitura confirmada em janela menor. O mês corrente está sendo puxado por ticket, não por alcance. O volume de pedidos (100 vs avg_30d 99,3) está na média — o crescimento de GMV é inteiramente explicado por ticket médio.

- **vs mesmos dias da semana** (avg R$4.685,96, 102,75 pedidos): GMV +29,8% com pedidos -2,7%. Ponto de comparação mais revelador: na quinta-feira de 14/05 foram 140 pedidos e R$6.539,97; ontem foram 100 pedidos e R$6.082,82 — nível de receita semelhante com 40 pedidos a menos. O ticket está compensando volume.

- **vs 7d** (`gmv_vs_7d_pct=+8.3%`, `orders_vs_7d_pct=-15.9%`): A semana recente tinha volume alto (avg 118,9 pedidos) com ticket mais baixo (R$47,25). Ontem inverteu: menos pedidos, ticket maior. Hipótese: encerramento de período promocional que captava pedidos de menor valor nas semanas anteriores, com a conta retornando a mix de maior ticket. Não confirmável sem contexto de campanha Himmel ou alteração de preço registrada.

---

### Leitura estratégica

- **Ticket como vetor real de crescimento, mix de fulfillment como sinal não explicado**: O GMV de ontem veio de ticket +37% acima da média de 30d com volume plano. Mas o dado mais dissonante é o mix de fulfillment: 7d e 30d mostram 73–77% Full; ontem o top 10 operou 80% Cross-docking (`fulfillment_mix_yesterday_top10.cross_docking_pct=80.0`). Os três primeiros colocados — Conjunto 5 Potes Tampa Preta (31 pedidos), Kit 10 Potes 1050ml (16 pedidos) e Conjunto 5 Potes Tampa Cinza (13 pedidos) — são todos `logistic_type=cross_docking`. A conta gerou seu melhor nível recente de GMV com os campeões Cross-docking, não Full — o que inverte o padrão histórico declarado. **Hipótese:** o ganho de ticket veio de mix (kits maiores, maior valor unitário) e não de ganho de exposição via Full; isso significa que a exposição orgânica atual não depende integralmente de Full para faturar, mas também não confirma que a conta esteja ganhando ranking por essa via.

- **Orgânico integral em dia de pico — sinal ambíguo**: `ads_summary.spend_yesterday_brl=0,00` com 11 campanhas nominalmente ativas. O GMV de R$6.082,82 foi 100% orgânico. Se intencional (Himmel pausou campanhas), a conta demonstra musculatura orgânica real neste patamar. Se técnico (falha de veiculação não registrada), o resultado não é replicável quando ADS retornar. Sem contexto de Himmel, a leitura do ADS share (0%) é fato, mas a interpretação de saúde orgânica é **hipótese não confirmável nesta sessão**.

- **Cauda morta como fato estrutural permanente**: 174 anúncios pausados vs 82 ativos (`account_overview.totals`: paused 174 / active 82 = ratio 2,1×, acima do limiar de 1,5×). Top3 concentra 60% (`top3_concentration=60.0`), top5 concentra 76%. A conta opera em núcleo estreito — os três primeiros itens pertencem a duas famílias (IMB501 e KIT10YW1050). A dependência estrutural não é nova (o estado foi herdado antes da gestão Yasmin), mas está instalada: qualquer ruptura nos top 2 afeta diretamente 47% do volume do dia.

- **Saúde de listing degradada no único campeão Full do dia**: Kit 4 Potes 1050ml (`MLB4073003575`) — 4º lugar com 8 pedidos, `logistic_type=fulfillment`, `health=0.75`. Health abaixo de 0,85 indica penalização ML ativa. Com `sold_quantity=961` e status active, este anúncio tem histórico relevante mas está operando com penalização de exposição. Dos outros 9 top itens, `health=null` em todos — 64 dos 82 ativos estão sem health calculada (`no_health_data_count=64`); a leitura de saúde da base é estruturalmente parcial.

---

### Tese da conta

**Vulnerável.** O patamar de GMV está consistentemente acima da banda histórica de 30 e 60 dias — fato em múltiplas janelas — mas o crescimento é quase inteiramente suportado por ticket, não por expansão de alcance. A estrutura que sustenta esse patamar é estreita: 82 anúncios ativos contra 174 pausados, top 3 com 60% de concentração, um único anúncio em Full entre os campeões com health degradada (0.75), e dois itens do top 10 em estoque crítico. A conta está financeiramente acima do histórico e ao mesmo tempo operacionalmente frágil — qualquer ruptura em 1–2 posições do top 5 comprime o GMV de forma desproporcional.

---

### Risco estrutural principal

- **Risco:** Estoque crítico em anúncios do top 10 com alto giro — Kit 10 Potes Herméticos 1050ml (`MLB4676726433`, `available_quantity=78`, 16 pedidos ontem em Cross-docking) e Kit 06 Canequinhas Acrílico (`MLB4410218897`, `available_quantity=2`, 3 pedidos ontem, `sold_quantity=456`).
- **Por que importa:** O Kit Canequinhas está em ruptura efetiva: 2 unidades disponíveis, 3 pedidos no dia. Esses pedidos se convertem em cancelamentos nas próximas 24–48h. Em ML, cancelamentos por falta de estoque impactam `cancellations_rate` da reputação — hoje em 0% (`reputation.cancellations_rate=0`), qualquer aumento interrompe a trajetória limpa. O Kit 10 Potes 1050ml tem 78 unidades; ao ritmo de 16/dia, o horizonte de ruptura é ~5 dias se o giro se mantiver. Como opera em Cross-docking, a reativação após ruptura depende de reabastecimento físico na expedição Budamix — não basta ter estoque no depósito.
- **Histórico:** Sem registros anteriores em weekly.md ou monthly.md — primeira ocorrência documentada.
- **Sinal de confirmação:** Kit Canequinhas (`MLB4410218897`) gerando cancelamentos registrados nos próximos 2 dias confirma impacto em reputação. Kit 10 Potes 1050ml (`MLB4676726433`) saindo do top 5 ou zerando pedidos dentro de 4 dias confirma ruptura de estoque operacional.

---

### Sinais a observar

1. **Ticket médio acima de R$55 por 3 dias consecutivos** confirmaria que a escalada (R$42→R$60) é estrutural — mudança de mix ou precificação consolidada — e não pico isolado. Queda abaixo de R$48 em 2 dias seguidos indicaria retorno à banda anterior e refutaria a tese de mudança de patamar de ticket.

2. **Kit 06 Canequinhas Acrílico (`MLB4410218897`) gerando cancelamento registrado nas próximas 48h** (verificável via `metrics.cancelamentos` elevado ou mudança em `reputation.cancellations_rate` no próximo pacote com dado disponível) confirmaria que o estoque crítico já se converteu em problema de reputação.

3. **Mix fulfillment do dia retornando para Full >60% no próximo ciclo** refutaria a hipótese de inversão estrutural e indicaria que ontem foi anomalia — os campeões habituais em Full simplesmente não performaram. Persistência de Cross-docking >60% no top 10 por mais 2 dias consecutivos confirmaria mudança real no vetor de geração de GMV.