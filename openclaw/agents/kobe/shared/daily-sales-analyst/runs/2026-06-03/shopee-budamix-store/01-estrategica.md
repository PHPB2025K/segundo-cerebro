<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base fraca: última entrada diária em 20/05 (gap de 14 dias), `weekly.md` e `monthly.md` são templates vazios sem histórico preenchido. Tese seed v1 (02/06/2026) não passou por nenhum ciclo formal de validação anterior. `shop_performance` indisponível (HTTP 404), `ads_summary` inacessível (HTTP 403 — escopo OAuth pendente), `top_items_details` retornou vazio (sem granularidade por anúncio), `fulfillment_mix` histórico indisponível por backfill pendente de `logistic_type`. Programa de Afiliados Shopee e Cashback em Moedas Shopee não disponíveis por limitação estrutural da Open API. Leitura hoje é factual sobre volume, ticket e estoque; inconclusiva sobre Saúde da Loja, stack pago e mix histórico de modalidade de envio.

---

### Leitura temporal

- **vs 7d e mesmos dias da semana:** o dia (56 pedidos, R$ 2.398,92) está acima da média recente de 7 dias (`avg_7d.avg_orders=48,7`, `changes.orders_vs_7d_pct=+15,0%`) e praticamente flat vs o controle de mesmo dia da semana (`same_weekday_avg.avg_orders=57,0`, `changes.orders_vs_same_weekday_pct=-1,8%`). A recuperação vs 7d reflete retorno após o vale agudo de 27/05 (34 pedidos, R$ 1.350) — não sinaliza aceleração estrutural, apenas normalização dentro do patamar atual.

- **vs 30d:** pedidos quase estáveis (`changes.orders_vs_30d_pct=-2,9%`) com faturamento acima (`changes.gmv_vs_30d_pct=+9,1%`) sustentado por ticket mais alto (`ticket_vs_30d_pct=+12,5%`). A média de 30 dias (`avg_30d.avg_orders=57,7`) e o dia de hoje estão convergindo — a conta se acomodou nesse patamar de 55–60 pedidos/dia há cerca de um mês.

- **vs 60d — contração de patamar confirmada:** o baseline de 60 dias é `avg_60d.avg_orders=77,7` e `avg_60d.avg_gmv=R$ 2.976,33`. O dia representa `changes.orders_vs_60d_pct=-27,9%` e `changes.gmv_vs_60d_pct=-19,4%`. A conta não está oscilando em torno do baseline da tese seed do Pedro — ela opera consistentemente abaixo dele há ao menos 30 dias. Não há hipóteses anteriores documentadas para confirmar ou refutar (memória vazia), mas a estrutura dos dados históricos torna a contração inequívoca.

- **Ticket compensando parcialmente:** ticket médio hoje (R$ 42,84) está +11,9% acima do baseline 60d (R$ 38,30 / `historical.avg_60d.avg_ticket`). O faturamento perdeu menos do que o volume porque cada pedido vale mais — mas o ganho de ticket não cobre a queda de 28% em pedidos. O faturamento absoluto de 60d (R$ 2.976,33/dia) não está sendo recuperado.

---

### Leitura estratégica

- **Contração de patamar, não ruído:** a conta operava a ~77 pedidos/dia no bimestre baseline e está consolidada em ~57 nos últimos 30 dias. Não há evidência de que o patamar inferior seja transitório — o controle de mesmo dia da semana (flat, -1,8%) confirma que isso não é sazonalidade pontual. A conta mudou de degrau. A tese seed do Pedro foi formulada sobre o baseline 60d; a conta que ele observou naquele período está ~28% menor em volume hoje.

- **Estoque em colapso silencioso — risco prospectivo crítico:** `account_overview.active_analysis.out_of_stock_count=41` de 60 anúncios ativos, ou seja, **68,3% da base ativa tem estoque zero** no snapshot pós-fechamento. Entre os IDs sem estoque estão `23993264258` (Jarra Medidora de Vidro 500ml — líder do dia com 22 pedidos), `22393168887` (Conjunto 5 Potes Tampa Preta — 10 pedidos) e `45554989236` (Kit 6 Canecas Tulipa 250ml — 8 pedidos). Os três produtos que representaram 70,2% do volume do dia encerraram o ciclo sem fôlego prospectivo. A conta de Volume/Giro está vendendo o lastro de estoque dos campeões — quando esse lastro acabar, o canal para. Risco não é do dia que passou; é do D+1 em diante.

- **Zero alavancas de exposição ativas:** a conta opera fora do Shopee Mall (`mall_status="not_mall"`, `mall_pct=0%`), sem Vendedor Indicado (`is_preferred_seller=false`), sem Programa de Frete Grátis em nenhum anúncio (`fsp_pct=0%`). Shopee Ads inacessível (403). Programa de Afiliados Shopee e Cashback em Moedas Shopee indisponíveis por limitação da Open API. A exposição orgânica da conta depende exclusivamente de Avaliação da Loja (não disponível hoje) e relevância de keyword — e há 253 anúncios `unlisted` vs 60 ativos, sugerindo catálogo massivamente desmobilizado. Isso cria um ambiente onde qualquer ruptura nos campeões não tem alavanca de reposição imediata de exposição.

- **Concentração top3 abaixo do baseline — sinal ambíguo:** concentração top3 hoje é 70,2% vs baseline 60d de 82,2% — aparente melhora de cauda. Mas com os três campeões agora sem estoque prospectivo e 41/60 anúncios zerando, a leitura mais provável é que outros anúncios com volume menor simplesmente continuaram ativas enquanto os líderes esgotavam. Não há evidência de desenvolvimento de segundo vetor real — é redução dos líderes, não fortalecimento da cauda.

---

### Status da tese seed (Lente 6)

**Em observação.** Primeiro ciclo formal. O mix do dia (unitários e conjuntos pequenos liderando — Jarra Medidora, Potes Redondos, Canecas) é coerente com Volume/Giro. O ticket (R$ 42,84) está dentro do esperado para papel de giro (R$ 40,45 no baseline). A concentração elevada em poucos campeões também é padrão histórico da tese. O que não é coerente é o **volume sistematicamente abaixo do baseline da tese** (-27,9% vs 60d) — mas 1 ciclo de validação é insuficiente para refinar ou enfraquecer a tese formalmente. O papel pode estar certo; o que pode estar errado é a escala esperada.

---

### Tese da conta

**Vulnerável.** A conta tem número de pedidos estabilizado, ticket saudável e concentração não-alarmante no dia — mas a estrutura por baixo está frágil: 68% dos anúncios ativos sem estoque, os três campeões que geraram 70% do volume do dia agora em ruptura prospectiva, zero alavancas de visibilidade ativas (sem Vendedor Indicado, sem Shopee Mall, sem Programa de Frete Grátis), e Shopee Ads inacessível. O resultado de hoje ainda foi sustentado pelo estoque remanescente dos líderes. A fragilidade não aparece no número de hoje — aparece no que vai acontecer quando esse estoque não existir amanhã.

---

### Risco estrutural principal

**Risco:** ruptura iminente nos três campeões do dia, que encerraram o ciclo com estoque zero prospectivo — Jarra Medidora de Vidro 500ml, Conjunto 5 Potes Tampa Preta e Kit 6 Canecas Tulipa 250ml representaram 70,2% do volume do dia e figuram em `account_overview.active_analysis.out_of_stock_ids`.

**Por que importa:** a conta não tem segundo vetor saudável. Com os três líderes sem estoque e 41/60 anúncios já zerando, o catálogo operável colapsa para ~19 anúncios com estoque. Mesmo que a demanda se mantenha, não há produto para capturá-la. O efeito na Saúde da Loja (taxa de não cumprimento, Taxa de Cancelamento do Vendedor) vai aparecer nos próximos ciclos — mas sem `shop_performance` disponível, a erosão é invisível até ser tarde.

**Histórico:** memória anterior vazia — não há registro de episódio anterior de ruptura simultânea nos três campeões. Este é o primeiro ciclo com esse dado explicitado.

**Sinal de confirmação:** faturamento abaixo de R$ 1.500 nos próximos 2 dias, com queda de pedidos abaixo de 30, confirma que a ruptura nos campeões está se traduzindo em colapso operacional imediato. Se `shop_performance` voltar disponível, taxa de não cumprimento (NFR) acima de 2% confirma que os pedidos sem cobertura já estão afetando as métricas estruturais.

---

### Sinais a observar

1. **Faturamento abaixo de R$ 1.500 por 2 dias seguidos (D+1 e D+2)** confirma que a ruptura simultânea nos três campeões está derrubando a operação — nível em que a conta não consegue substituir o volume com o catálogo remanescente de ~19 anúncios com estoque.

2. **Ticket médio acima de R$ 55 por 3 dias consecutivos** indica que os itens de baixo ticket e alto giro (Jarra Medidora, Potes unitários) esgotaram e a conta está vendendo apenas os itens mais caros ou menos rotacionados — divergência do papel Volume/Giro hipotetizado que exigiria status "enfraquecida" na tese seed após o terceiro ciclo.

3. **`out_of_stock_count` mantendo ou aumentando acima de 40 no próximo snapshot disponível (se disponível)** confirma que a conta não repôs estoque nos campeões e o colapso estrutural do catálogo é persistente — não pontual.