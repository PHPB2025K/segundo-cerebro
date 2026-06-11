<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Robusta para a sessão. Memória semanal ativa com 9 ciclos diários acumulados (05/06–09/06), rules.md e monthly.md carregados. Janelas 7d, 30d e 60d disponíveis com `coverage_pct=100%` em todos os blocos de modalidade de envio. Blocos `ml_snapshot` completos sem indisponibilidade: reputação, mercadolider, fulfillment_mix, top_items_details, ads_summary e account_overview presentes. Hipóteses ativas dos ciclos anteriores têm base suficiente para confirmação, enfraquecimento ou refutação.

---

### Leitura temporal

- **Trajetória de 60d confirmada em aceleração consistente:** GMV do dia R$8.063,87 está +56,0% vs `historical.avg_60d.avg_gmv=R$5.167,52` (`changes.gmv_vs_60d_pct`) e +25,4% vs `historical.avg_30d.avg_gmv=R$6.430,90`. O controle sazonal por dia da semana (quarta-feira) mostra escada sem ruído: R$2.984 → R$5.087 → R$7.150 → R$6.401 → R$8.063 nos últimos quatro ciclos equivalentes — consistência atravessa três janelas independentes, não é ponto fora da curva.

- **Pedidos crescem mais rápido que ticket, por composição:** 185 pedidos (+60,2% vs 60d, +39,9% vs 30d, +71,7% vs mesmos dias) enquanto `ticket_medio=R$43,59` recua -10,4% vs 30d. Não é deterioração estrutural de valor: o cluster IMB501 carregando 60,5% do volume (produto de menor valor unitário) puxa o ticket médio da conta para baixo por peso, não por compressão de preço. GMV e pedidos crescem juntos; o mix é que mudou.

- **Hipótese de expansão orgânica estrutural enfraquecida por reversão de ADS share:** A memória registrava série monotonicamente descendente de ADS share — 69,9% (22/05) → 44,3% (09/06) em 9 pontos, com 3 ciclos abaixo de 50% sugerindo consolidação orgânica. Hoje o share reverteu para 59,7% (`revenue_ads_yesterday_brl=R$4.813,22 / gmv=R$8.063,87`), com gasto absoluto de R$412,15 (+57% vs R$262,19 em 09/06). A série descendente foi suspensa — não refutada em um ponto, mas enfraquecida o suficiente para exigir nova série de 2–3 ciclos antes de reclassificação.

- **MercadoLíder Platinum consolidado, eixo muda de conquistar para proteger:** `mercadolider.sales_60d_revenue_brl=R$315.455,14` está R$19.455 acima do threshold R$296.000, `gap_revenue_brl=0`, `progress_pct=100%`, `power_seller_status=platinum`. GMV do dia (R$8.063) opera 53% acima do `ritmo_diario_brl=R$5.257,59`. A hipótese de promoção foi confirmada e encerrada; hipótese ativa agora é manutenção — o único vetor que pode ameaçar a medalha no curto prazo é `cancellations_rate` saindo de zero por rupturas automáticas em Full.

---

### Leitura estratégica

- **Lentes 1 + 3 — Ganho de patamar real com dependência estrutural crônica como mecanismo exclusivo de crescimento:** A expansão é genuína e atravessa três janelas temporais. Mas o mecanismo é IMB501-dependente há 14+ ciclos: `top3_concentration=60,5%` corresponde exatamente ao cluster IMB501 (Tampa Preta+Vermelha 89 pedidos em MLB3288536143 + Tampa Cinza 23 pedidos em MLB4535865311). A cauda entregou 96 pedidos distribuídos em 7+ anúncios com nenhum item acima de 12 pedidos — ainda não configura segundo vetor robusto, confirma padrão crônico. A conta cresce pelo topo; a base não acompanha. A razão paused/active de 128/79 (1,62x, acima do threshold 1,5x) confirma cauda morta dominante sem sinais de reversão.

- **Lentes 3 + 4 — Três anúncios de Catálogo em ruptura simultânea, inédito na série recente:** `MLB6232315532` (Kit 6 Canecas Lisas 200ml, `listing_type=gold_pro`, `is_catalog=true`, Full) tem `available_quantity=5` após 7 pedidos no dia — runway ≤ 0,7 dia, ruptura provável já em andamento. É o único gold_pro do top 10; anúncio Premium em Catálogo perde Buy Box imediatamente na ruptura, com recuperação mais lenta que Clássico. Adicionalmente: `MLB4741367603` (Tulipa 250ml, Catálogo Clássico, `available_quantity=14`, 5 pedidos, ~2,8 dias) e `MLB3918271667` (Kit 2 Potes 800ml, Catálogo Clássico, `available_quantity=12`, 4 pedidos, ~3 dias). Três Catálogos em zona crítica simultânea é configuração nova — os ciclos anteriores registravam no máximo um Catálogo por vez em risco.

- **Lente 5 — ADS com ACOS acima de 10% pelo segundo ciclo e share revertido sobre base forte:** ROAS calculado 11,67x (`R$4.813/R$412`), ACOS 12,12% — segundo ciclo acima de 10% em três dias (08/06: 11,67%; 09/06: 6,31%; 10/06: 12,12%). A instabilidade do ACOS é mais relevante do que o nível em si (ainda confortável vs gatilho operacional). O ADS share de 59,7% sobre GMV de R$8.063 (dia forte, não denominador comprimido como em 07/06) indica que Himmel escalou campanha ativamente — o orgânico cresceu, mas ADS cresceu proporcionalmente mais. A hipótese de autonomia orgânica não foi refutada, mas perdeu a série como suporte.

- **Lentes 2 + 6 — Reputação em máxima estrutural com vetor latente de degradação por ruptura de estoque:** `reputation.color=5_green`, `power_seller_status=platinum`, `cancellations_rate=0`, `claims_rate=0,0015` (30% do threshold 0,005), `delayed_handling_rate=0,0008`. Estrutura de exposição máxima mantida. O vetor de risco é indireto: 8 cancelamentos no dia (padrão recorrente de 3–8/dia sem atribuição possível pelo pacote), combinados com três Catálogos a 1–3 dias de ruptura automática, criam pipeline de cancelamentos prospectivos que ainda não aparece na métrica oficial (janela longa). `cancellations_rate=0` é o ativo mais valioso da medalha Platinum — mais frágil à ruptura de estoque do que a qualquer tendência orgânica.

---

### Tese da conta

**Vulnerável.** O patamar é real e crescente — GMV +56% vs 60d, pedidos +60%, MercadoLíder Platinum consolidado com folga de R$19.455 sobre o threshold. Mas o crescimento opera sobre estrutura com pontos únicos de falha: dependência crônica de um cluster (IMB501 em 60,5% do volume há 14+ ciclos sem segundo vetor emergindo), três anúncios de Catálogo em ruptura simultânea iminente — configuração sem precedente na série memória —, e o único Premium (gold_pro) a menos de 1 dia de perder Buy Box. O dia de 10/06 não alterou a tese: confirmou que a expansão de patamar ocorreu sem diversificação da base e com acumulação de risco de estoque nos anúncios que mais afetam a posição competitiva no canal Catálogo.

---

### Risco estrutural principal

**Risco:** Ruptura simultânea de múltiplos anúncios de Catálogo — com perda de Buy Box no único gold_pro da conta — alimentando cancelamentos automáticos que ameaçam o `cancellations_rate` que sustenta o MercadoLíder Platinum.

**Por que importa:** `MLB6232315532` (gold_pro, `is_catalog=true`, `available_quantity=5`, Full) é o único anúncio Premium no topo — sua ruptura elimina o vetor de Buy Box em Catálogo com timeline de recuperação mais longa que qualquer Clássico. Os outros dois Catálogos (`MLB4741367603` e `MLB3918271667`) em 2–3 dias de runway criam concentração de rupturas num intervalo de 72 horas. Ruptura em Full gera cancelamento automático. Com `cancellations_rate=0` hoje, mesmo uma série pequena (3–5 cancelamentos automáticos confirmados por platform_item_id) pode sair de zero na janela oficial ML — o único threshold que, se cruzado, degrada a Platinum de forma estrutural independente de volume ou reputação de cor.

**Histórico:** Padrão de depleção recorrente em `MLB6232315532` documentado desde 26/05 (ciclo 35→28→11→restock→5); `MLB4073003575` com ruptura documentada desde 02/06 e restock recorrentemente insuficiente para o ritmo. O mecanismo é conhecido: ritmo de crescimento de pedidos ultrapassa o cadenciamento de restock para o CD do ML em Full. Não é evento — é ciclo.

**Sinal de confirmação:** `MLB6232315532` com `status=paused` ou `available_quantity=0` no próximo snapshot confirma início de perda de Buy Box no Catálogo gold_pro. `cancellations_rate > 0` em qualquer snapshot dos próximos 3 ciclos confirma que as rupturas automáticas já entraram na janela oficial — ameaça ativa à Platinum mesmo com `color=5_green` mantido.

---

### Sinais a observar

1. **`MLB6232315532` (Kit 6 Canecas Lisas 200ml, único gold_pro Catálogo) com `available_quantity ≤ 0` ou `status=paused` no próximo snapshot** — confirma ruptura de Buy Box no Catálogo Premium; se os outros dois Catálogos (`MLB4741367603` e `MLB3918271667`) também pausarem no mesmo intervalo de 72 horas, a perda de posição em Catálogo passa de evento isolado para episódio de degradação simultânea, configuração nova na série.

2. **`cancellations_rate > 0` em qualquer snapshot dos próximos 3 ciclos (`ml_snapshot.reputation.cancellations_rate`)** — saída de zero confirma que cancelamentos recorrentes (padrão 3–8/dia há múltiplos ciclos) entraram na janela oficial ML; combinada com rupturas automáticas em Full, eleva risco para a medalha Platinum de latente para ativo mesmo sem mudança no volume ou na cor da reputação.

3. **ADS share abaixo de 48% por 2 ciclos consecutivos após 10/06 confirmaria que o dia de hoje (59,7%) foi desvio e a série orgânica prossegue; ADS share acima de 55% por 2 ciclos consecutivos confirmaria que a série descendente 22/05–09/06 foi sazonal e o canal segue ADS-dependente** — os próximos dois ciclos são o teste falsificável da hipótese de autonomia orgânica estrutural documentada na memória desde 01/06.