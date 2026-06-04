<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base com limitações relevantes: último daily disponível é 2026-05-20 (gap de ~12 dias), weekly.md e monthly.md são templates vazios sem conteúdo acumulado — sem hipóteses ativas para confirmar ou refutar, sem tese mensal consolidada. `shop_performance` indisponível (HTTP 404 — Saúde da Loja suspensa nesta sessão). `fulfillment_mix_30d` e `fulfillment_mix_7d` indisponíveis por gap estrutural pendente (backfill do `logistic_type`). `ads_summary` indisponível (HTTP 403 — escopo OAuth de Ads não habilitado). `top_items_details.items` veio vazio, sem detalhe individual dos anúncios do top 10. Programa de Afiliados Shopee e Cashback em Moedas Shopee não disponíveis por limitação da Open API — esperado por design. Tese seed v1 do Pedro (02/06/2026) sem ciclos validados anteriores: esta leitura é o primeiro ponto de evidência após o gap.

---

### Leitura temporal

- **vs 60d baseline:** 68 pedidos vs média 60d de 79,7 (`changes.orders_vs_60d_pct=-14,7%`), mas faturamento em R$ 3.092,25 vs média 60d de R$ 3.147,98 (`changes.gmv_vs_60d_pct=-1,8%`) — a divergência entre volume e faturamento é explicada integralmente pelo ticket: R$ 45,47 hoje vs R$ 39,51 no 60d (`changes.ticket_vs_60d_pct=+15,1%`). O bimestre mostra uma conta que operava em patamar de volume mais alto (~79,7 pedidos/dia) e foi comprimindo volume nos 30 dias mais recentes, com ticket compensando parcialmente em faturamento.

- **vs 30d e 7d:** média 30d em 58,9 pedidos, mas 7d em apenas 47,6 — a semana que antecede este dia foi notavelmente fraca. O salto de 68 pedidos (+42,9% vs 7d) não é tendência confirmada; é o dia mais forte de uma semana fraca, dentro de um mês que já opera abaixo do bimestre. Faturamento +31,2% vs 30d e +52,7% vs 7d amplificam o sinal, mas o patamar de referência (30d) já estava deprimido.

- **Controle de dia da semana:** mesmos dias da semana nas últimas 4 semanas: 70, 52, 72 e 96 pedidos (média 72,5; R$ 2.802,22). Hoje com 68 pedidos (-6,2% vs peers de semana) mas faturamento de R$ 3.092,25 (+10,4%) — volume ligeiramente abaixo dos pares sazonais, mas receita acima, novamente pela elevação de ticket (R$ 45,47 hoje vs R$ 38,65 na média dos pares). O dia não é forte em alcance; é acima da média em valor por pedido.

- **Hipóteses anteriores:** sem daily desde 20/05 e sem conteúdo acumulado em weekly/monthly — nenhuma hipótese ativa a confirmar ou refutar.

---

### Leitura estratégica

- **Compressão de volume estrutural no mês, ticket segurando faturamento:** A trajetória 60d→30d mostra queda de ~26% na média diária de pedidos (79,7 → 58,9), com faturamento caindo menos (-25%) porque ticket subiu de R$ 39,51 para R$ 40,02. Hoje o ticket está em R$ 45,47 — 15% acima do baseline 60d. A leitura mais honesta é que a conta está vendendo menos unidades, com composição de mix migrando levemente para produtos de valor unitário mais alto. Para uma conta com papel Volume/Giro, isso é um sinal ambíguo: o faturamento se sustenta, mas o motor de escala (volume de pedidos) está em compressão há pelo menos 30 dias.

- **Risco de ruptura iminente nos campeões — sinal crítico:** `account_overview.active_analysis.out_of_stock_count=41` — 68% dos 60 anúncios ativos estão sem estoque no snapshot pós-fechamento. Dentre os `out_of_stock_ids`, estão presentes os três produtos que lideraram o dia: item_id `23993264258` (Jarra Medidora de Vidro 500ml — 19 pedidos, 28% do volume), `45554989236` (Kit 6 Canecas Tulipa 250ml — 15 pedidos) e `22393168887` (Conjunto 5 Potes de Vidro Redondos Tampa Preta — 15 pedidos). Os três juntos representaram 72,1% do faturamento do dia e encerraram o dia em estoque zero. A superfície de venda efetiva da conta no ciclo seguinte é aproximadamente 19 dos 60 anúncios ativos — todos os outros sem cobertura prospectiva.

- **Ausência total de boosters estruturais de visibilidade:** A conta opera fora do Shopee Mall (`mall_status="not_mall"`), sem Vendedor Indicado (`is_preferred_seller=false`), e com Programa de Frete Grátis ativo em 0% dos anúncios ativos (`fsp_pct=0.0%`). Nenhuma das três alavancas de visibilidade estrutural da plataforma está ativa. Com Shopee Ads indisponível (HTTP 403), não é possível calcular share do canal pago nem avaliar se o faturamento é sustentado por tráfego orgânico ou campanha. A dependência total de mídia paga não é calculável; o risco de exposição orgânica sem qualquer booster é real e não quantificável neste ciclo.

- **Cauda morta dominante amplifica a fragilidade:** 253 anúncios não-listados + 1 banido vs 60 ativos — a conta opera sobre um catálogo funcionalmente enxuto. Com 41 dos 60 ativos sem estoque e `top_items_details` vazio (sem dado de variação individual dos campeões), não é possível avaliar se a concentração no top 3 está ligada a variações específicas (cor, tamanho) ou ao anúncio pai inteiro. O `quality_flag` de `high_top3_concentration` (72,1% hoje vs baseline 82,2%) registra o padrão, mas com catálogo efetivo de ~19 anúncios, qualquer queda adicional de estoque concentra ainda mais.

---

### Status da tese seed (Lente 6)

**Em observação.** O comportamento do dia tem sinais coerentes com Volume/Giro: líderes são produtos de giro (jarra unitária, kits porcelana acessíveis, potes vidro), concentração top3 em 72,1% — abaixo do baseline 82,2%, sugerindo leve distribuição da cauda no dia. Entretanto, o ticket de R$ 45,47 está 12,4% acima do baseline de R$ 40,45 e 17,7% acima da média dos pares de dia da semana — leve pressão para cima que, em isolado, é ruído, mas é consistente com a compressão de volume observada na janela 30d. Com gap de 12 dias na memória diária, weekly e monthly sem conteúdo e tese seed v1 sem ciclos validados anteriores, não há base para classificar acima de "em observação" — esta leitura serve como ponto de partida.

---

### Risco estrutural principal

**Risco:** 41 dos 60 anúncios ativos sem estoque no snapshot pós-fechamento, com os três campeões do dia (Jarra Medidora de Vidro 500ml, Kit 6 Canecas Tulipa 250ml e Conjunto 5 Potes de Vidro Redondos Tampa Preta) entre os itens zerados. A superfície de venda prospectiva da conta é ~19 anúncios — menos de um terço do catálogo ativo.

**Por que importa:** Os três anúncios zerados responderam por R$ 2.230 dos R$ 3.092 do dia (72%). Anúncios ativos sem estoque na Shopee acumulam penalidade de relevância orgânica — a plataforma rebaixa posição de anúncios que não entregam. Em uma conta sem Vendedor Indicado, fora do Shopee Mall e sem Programa de Frete Grátis ativo, a relevância orgânica dos campeões é o principal vetor de exposição disponível. Erosão de posição em D+1, D+2 é prospectiva mas plausível se o reabastecimento não for imediato.

**Histórico:** gap de 12 dias na memória diária impede determinar se o OOS massivo é situação nova (ruptura recente) ou crônica (padrão de operação). Sem essa informação, o risco é tratado como alerta crítico até evidência contrária.

**Sinal de confirmação:** Jarra Medidora de Vidro 500ml, Kit 6 Canecas Tulipa 250ml e Conjunto 5 Potes Tampa Preta somando ≤5 pedidos combinados no próximo ciclo diário confirma ruptura efetiva nos três campeões e demanda escalada imediata para Lucas.

---

### Sinais a observar

1. **Ruptura dos campeões nos próximos 2 dias:** Jarra Medidora de Vidro 500ml (item_id `23993264258`), Kit 6 Canecas Tulipa 250ml (item_id `45554989236`) e Conjunto 5 Potes Tampa Preta (item_id `22393168887`) somando ≤5 pedidos combinados em qualquer dos dois próximos ciclos confirma ruptura efetiva no principal vetor de faturamento da conta — reabastecimento urgente via Lucas.

2. **`out_of_stock_count` na account_overview cair abaixo de 20 nos próximos 3 ciclos** confirma reabastecimento efetivo e retorno da superfície de venda; permanecer acima de 35 por 3 ciclos consecutivos confirma OOS como condição estrutural crônica, não evento pontual — sinal para revisão de gestão de estoque com o Pedro (se disponível no próximo snapshot).

3. **Ticket médio acima de R$ 48 por 3 dias consecutivos a partir de hoje** confirma migração de mix para produtos de valor mais alto e exige refinamento da tese seed: o papel Volume/Giro puro pode estar evoluindo para híbrido com tração em kits de maior valor. Ticket abaixo de R$ 42 por 2 dias seguidos confirma normalização e sustenta o papel atual sem ajuste.