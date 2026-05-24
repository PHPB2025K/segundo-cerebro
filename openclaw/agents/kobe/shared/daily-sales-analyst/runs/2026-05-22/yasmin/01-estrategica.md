<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

`ml_snapshot` completo (`status: ok`) em todas as dimensões — reputação, mix de modalidade de envio em três janelas, `top_items_details`, `ads_summary` e `account_overview` com cobertura 100%. `DADOS_PARCIAIS` no Layer 0 é restrito a contas Shopee; ML está íntegro (`reconciliation.ok: true`). Weekly.md contém bloco diário de 2026-05-22 ingestido por ciclo L05 anterior — tratado aqui como memória de hipóteses ativas. Monthly.md permanece template-semente sem histórico mensal acumulado; `last_daily_file` aponta para 2026-05-20, com 2026-05-21 fora da memória diária. Históricas 30d e 60d permanecem intactas. Base suficiente para tese de patamar e risco estrutural.

---

### Leitura temporal

- **Patamar bimestral consolidado, ticket como único vetor de ganho:** O GMV de R$4.622,03 está +16,3% acima da média 60d de R$3.975,41 (`changes.gmv_vs_60d_pct`) e +3,4% acima da média 30d de R$4.470,29 (`changes.gmv_vs_30d_pct`). O ticket médio de R$55,02 está +29,8% vs 60d e +22,3% vs 30d (`changes.ticket_vs_30d_pct`). O volume de pedidos, ao contrário, está -10,4% vs 60d e -15,4% vs 30d — a conta fatura mais com menos pedidos há pelo menos 30 dias consecutivos. O patamar acima do histórico bimestral é real, mas inteiramente sustentado por composição de mix, não por crescimento de alcance.

- **Pullback vs 7d atenuado pelo controle de dia da semana:** A média 7d foi de R$5.555,18 com 113,3 pedidos — pico que distorce o comparativo. O controle de sextas (`same_weekday_last_4`) revela faixa de R$3.214 a R$6.465, com média R$4.718,81; o GMV de hoje está -2,1% dessa média (`changes.gmv_vs_same_weekday_pct`), dentro da variação natural do dia. As últimas quatro sextas sugerem alternância alto-baixo (01/05 R$6.465 → 08/05 R$3.700 → 15/05 R$5.494 → 22/05 R$4.622), mas com quatro pontos isso é insuficiente para tese de ciclo — é observação que aguarda a próxima sexta para ser confirmada ou descartada.

- **Hipóteses ativas do ciclo L05 (2026-05-22):** ADS share de 69,9% e nível de qualidade de anúncio degradado de MLB4073003575 (0,75, Padrão inferior) e MLB3288536143 (0,71, Padrão inferior) foram registrados na memória como "segundo ponto da série". O dado desta sessão confirma ambos sem evolução em nenhuma direção. Sem registro de 2026-05-21, não há terceiro ponto que permita confirmar ou descartar tendência — as hipóteses seguem como candidatas ativas, não conclusões.

- **MercadoLíder Platinum na janela de decisão:** A janela rolling 60d (`mercadolider.sales_60d_revenue_brl`: R$240.773,23) coloca o progresso em 81,34% (`platinum.progress_pct`) com gap de R$55.226,77 e ETA de 13,8 dias ao ritmo atual de R$4.012,89/dia. O GMV de hoje (R$4.622,03) está acima do ritmo necessário — contribuição positiva ao ETA. A conta está na faixa "no ritmo, sustentar = mover": manter o patamar atual avança o ETA; qualquer queda sustentada de volume o estende sem alarme imediato no agregado.

---

### Leitura estratégica

- **Lentes 1 + 6 — Ganho de patamar ticket-driven, Platinum viável mas com margem estreita:** A conta saiu de R$42,40 de ticket médio (60d) para R$55,02 (+29,8%) com volume caindo — esse tipo de ganho é estruturalmente mais frágil do que crescimento por alcance, pois depende de que os produtos de maior valor permaneçam visíveis e competitivos. Para o Platinum, o progresso de 81,34% com ETA 13,8 dias é real e factível, mas a janela rolling é sensível: dias abaixo de R$4.000 desaceleram o ETA sem que o resultado pareça crítico no curto prazo, enquanto a saída de pedidos antigos da janela de 60d pode comprimir o faturamento acumulado sem nenhum dia ruim visível.

- **Lente 2 — Reputação verde com sinal silencioso em avaliações:** A conta tem `color=5_green`, `power_seller_status=gold`, cancelamentos oficiais nulos e `delayed_handling_rate=0,0012` — estruturalmente elegível para Mercado Líder sem restrição. O campo `ratings_negative=0,39` (39% das avaliações negativas) está acima do padrão esperado para MercadoLíder Gold e foi registrado no ciclo anterior como hipótese associada aos dois anúncios Full com nível de qualidade de anúncio degradado. Com `claims_rate=0,0025` (0,25%) ainda há margem até o threshold de risco de 0,5%. O sinal não é risco confirmado — é indicador precoce que se torna relevante se `claims_rate` acelerar nos próximos ciclos.

- **Lente 3 — Concentração crônica com cauda morta dominante:** Top 3 em 48,8% (`top3_concentration`) e top 5 em 64,3% (`top5_concentration`), sem segundo vetor emergente visível. A relação paused/active de 176:81 (2,17x, acima do threshold de 1,5x) indica cauda majoritariamente inativa — a conta opera sobre um subconjunto restrito de anúncios em Full e Cross-Docking. Não é risco novo, mas amplifica o impacto de qualquer ruptura em anúncio líder: sem cauda ativa, não há absorção automática de volume deslocado. A divergência entre mix de modalidade de envio 30d (Full 73,7%, `fulfillment_mix_30d`) e mix da base inteira (Full 33,3%, `account_overview.active_analysis.fulfillment_mix`) confirma que os campeões históricos estão desproporcionalmente em Full — enquanto a base usa Cross-Docking, o volume depende de estoque no CD do ML.

- **Lentes 4 + 5 — ADS dominante compensando nível de qualidade de anúncio degradado nos campeões Full:** ADS gerou R$3.228,78 (`ads_summary.revenue_ads_yesterday_brl`) com gasto de R$296,96, ROAS 10,87x e ACOS 4,57% — eficiência alta. Esses números representam 69,9% do GMV do dia, colocando a conta em zona de ADS dominante (> 50%). Os dois anúncios Full no top 3 — MLB4073003575 (Kit 4 Potes 1050ml, `health=0,75`, Padrão inferior) e MLB3288536143 (Conjunto 5 Potes Tampa Vermelha, `health=0,71`, Padrão inferior) — têm nível de qualidade de anúncio que reduz ranking orgânico ML progressivamente. Com ADS cobrindo essa lacuna de orgânico, o circuito fecha: nível de qualidade de anúncio degradado não pressiona ação corretiva enquanto ROAS é eficiente, e a degradação orgânica avança silenciosa sob a cobertura de mídia paga.

---

### Tese da conta

**Em acomodação.** O faturamento acima da banda 60d (+16,3%) é consistente e real, mas inteiramente sustentado por ticket elevado (+29,8% vs 60d) com volume em queda (-10,4%) — acomodação em patamar mais alto, não expansão de alcance. A reputação está verde estável e as métricas oficiais ML estão dentro dos limites — elegibilidade MercadoLíder Gold não está ameaçada. A vulnerabilidade estrutural não aparece no resultado: ADS dominante (69,9% share) com dois campeões Full em Padrão inferior de nível de qualidade de anúncio cria uma dependência que permanece invisível enquanto Himmel mantém eficiência de campanha e o ritmo diário sustenta o ETA do Platinum. A conta não está deteriorando, mas a estabilidade do patamar atual depende de variáveis não totalmente orgânicas.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads (69,9% share do GMV) sustentando exposição de dois campeões Full — MLB4073003575 (Kit 4 Potes 1050ml) e MLB3288536143 (Conjunto 5 Potes Tampa Vermelha) — que operam com nível de qualidade de anúncio em Padrão inferior (0,75 e 0,71 respectivamente), com perda progressiva de ranking orgânico ML compensada por tráfego pago.

**Por que importa:** Enquanto ADS sustenta o tráfego, a penalização orgânica dos dois anúncios não aparece no GMV. Se as campanhas de Himmel forem reduzidas, interrompidas ou encarecidas por pressão competitiva de lance, esses dois anúncios enfrentarão a penalização orgânica sem cobertura — e, com cauda morta dominante (176 pausados vs 81 ativos), não há absorção interna. O impacto potencial sobre o GMV é da ordem de 25–30%, sem nenhum evento único visível como gatilho.

**Histórico:** Registrado como "segundo ponto da série" no ciclo L05 de 2026-05-22; sem dado de 2026-05-21, não há confirmação de série acima de um ciclo. É hipótese estrutural com dois pontos idênticos — não tendência confirmada.

**Sinal de confirmação:** ADS share acima de 65% por mais 2 ciclos consecutivos com `health` de MLB4073003575 e MLB3288536143 permanecendo abaixo de 0,85 confirma o circuito como padrão estrutural ativo e aciona revisão por Yasmin junto a Himmel.

---

### Sinais a observar

1. **ADS dominância — limiar de estrutural:** ADS share acima de 65% nos próximos 2 ciclos consecutivos com ROAS > 5x confirma dependência estrutural de mídia paga como padrão da conta — não evento isolado. Share abaixo de 50% em qualquer ciclo refuta a hipótese para este período e sugere recuperação de orgânico.

2. **Kit 6 Canecas Tulipa 250ml (MLB6167272090) — ruptura em Full iminente:** `available_quantity=2` em modalidade Full com 6 pedidos registrados no dia anterior; próximo ciclo com `available_quantity=0` ou `status=paused` configura ruptura de vetor Full no top 5. Se o anúncio sair do top 10 por 2 dias seguidos sem reposição confirmada, o mix de modalidade de envio do dia e o GMV do cluster de canecas recuam sem reposição orgânica imediata.

3. **MercadoLíder Platinum — ritmo vs janela rolling:** GMV diário abaixo de R$3.500 por 2 dias consecutivos estende ETA de 13,8 para 20+ dias; GMV acima de R$4.500 por 3 ciclos comprime ETA para abaixo de 10 dias e coloca a promoção praticamente garantida. A alternância alto-baixo observada nas últimas quatro sextas (se confirmada na próxima, 2026-05-29) indicará que o ritmo semanal oscila sistematicamente e o ETA precisa ser lido por semana, não por dia.