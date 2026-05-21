<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` estão em template vazio — sem consolidações anteriores, sem hipóteses ativas para confirmar ou refutar. Esta leitura inaugura a tese; não há histórico acumulado para ancorar diagnóstico longitudinal profundo. As janelas operacionais compensam: 7d (7 dias com dado), 30d (30 dias) e 60d (60 dias) disponíveis com coverage 100%. `ml_snapshot` completo — reputação, mix fulfillment (7d e 30d), detalhes dos top 10 e ADS summary todos com `status: ok`. Base factual do dia é robusta; base interpretativa histórica ainda é semente.

---

### Leitura temporal

- **Ticket em ganho de patamar confirmado em duas janelas:** `ticket_vs_30d_pct=+27.0%` e `ticket_vs_60d_pct=+33.6%`. O ticket saiu de R$41.86 (avg 60d) para R$55.91 — não é oscilação, é deslocamento de patamar. O volume de pedidos, por sua vez, está flat vs 60d (`orders_vs_60d_pct=-0.2%`) e apenas -8.9% vs 30d — a conta não está perdendo alcance, está vendendo mais caro por pedido.

- **A semana recente (7d) puxa o volume para baixo:** `avg_orders_7d=115.1` vs `pedidos_validos=91` (`orders_vs_7d_pct=-20.9%`), mas `gmv_vs_7d_pct=-4.3%` apenas — o 7d foi inflado por dias de volume alto que não se repetiram. O GMV resistiu porque o ticket do dia (R$55.91) está 21% acima do ticket médio 7d (R$46.17). Ontem foi um dia de menor volume dentro de um ciclo mais intenso, não sinal de deterioração.

- **Controle de sazonalidade confirma ganho:** As quatro quartas-feiras anteriores registraram R$2.984, R$3.006, R$5.619 e R$3.758 (avg R$3.842). Ontem: R$5.088 — `gmv_vs_same_weekday_pct=+32.4%`, com pedidos flat (`orders_vs_same_weekday_pct=-1.6%`). O dia 29/04 (R$5.619) foi o único comparável; as duas quartas intermediárias (06/05 e 13/05) ficaram em ~R$3.000, sugerindo que maio teve queda de volume que ontem interrompeu — mas a base de comparação de quarta é favorável, não excepcional.

- **Sem hipóteses ativas a confirmar ou refutar** — memória em construção.

---

### Leitura estratégica

- **Lente 1 — Patamar vs banda histórica:** O ganho de GMV é inteiramente de ticket, não de alcance. `gmv_vs_60d_pct=+33.3%` com `orders_vs_60d_pct=-0.2%` é a assinatura de uma conta que mudou mix de produto (kits maiores, tickets mais altos) ou reprecificou — e esse deslocamento se mantém em 30d e 60d. Não é ruído de um dia; é trajetória confirmada nas duas janelas longas e no controle de dia da semana.

- **Lente 5 — Mercado Ads dominante, orgânico não testado:** `ads_summary.revenue_ads_yesterday_brl=R$3.041,56` sobre `gmv=R$5.087,71` = **ADS share de 59,8%** — zona de ADS dominante. ROAS 11,6x e ACOS 4,64% são números excepcionalmente eficientes, mas escondem um dado crítico: o orgânico puro entregaria aproximadamente R$2.046 no dia. A conta não tem histórico de como se comporta sem o nível atual de campanha; a eficiência de Himmel é real, mas o patamar de GMV é inseparável dela.

- **Lente 4 — Health degradada nos campeões, exposição orgânica comprometida:** `MLB4073003575` (Kit 4 Potes 1050ml, 2º colocado com 13 pedidos) tem `health=0.75` — penalização ML ativa. `MLB3288536143` (Conjunto 5 Potes Tampa Vermelha, 5º colocado) tem `health=0.71` — penalização mais severa. Ambos competem fora de catálogo (`is_catalog=false`), ou seja, dependem inteiramente de posição em categoria — que a penalização corrói progressivamente. Aparecerem no top 10 apesar da health degradada é hipótese de que ADS está sustentando visibilidade onde o orgânico recuou. Sem ADS, a posição desses anúncios em categoria seria mais baixa.

- **Lente 3 — Dependência de campeões + estoque crítico em posição de cauda:** `top3_concentration=48.4%`, `top5_concentration=59.3%` — estrutura de dependência moderada, mas 174 anúncios pausados contra 82 ativos (ratio 2:1) indica cauda morta dominante; a conta funciona de um núcleo pequeno. `MLB4410218897` (Kit 06 Canequinhas Acrílico, 10º colocado) tem `available_quantity=3` em Full — ruptura iminente. `MLB6167272090` (Kit 6 Canecas Porcelana, 6º colocado) tem `available_quantity=21` em Full — vetor emergente com estoque estreito.

---

### Tese da conta

**Vulnerável.** O patamar de GMV está genuinamente mais alto do que há 30-60 dias — confirmado em múltiplas janelas e no controle de dia da semana. Mas esse patamar repousa sobre três fragilidades simultâneas: (1) ADS representa ~60% do faturamento com orgânico não testado de forma independente; (2) os dois principais campeões em categoria têm health penalizada (0.75 e 0.71), o que sugere que a posição orgânica deles em ranking está comprometida e ADS está mascarando essa deterioração; (3) ao menos um anúncio ativo da cauda superior está a 3 unidades da ruptura. A reputação está verde-gold com taxas saudáveis (`cancellations_rate=0`, `claims_rate=0.0025`), o que descarta deterioração operacional — o risco é estrutural de exposição, não de comportamento.

---

### Risco estrutural principal

**Risco:** Health degradada nos anúncios campeões (`MLB4073003575` health=0.75 e `MLB3288536143` health=0.71) sendo compensada por Mercado Ads — os dois respondem por 36 dos 91 pedidos do dia (39,6% do volume sozinhos) e competem exclusivamente por ranking de categoria, não por Buy Box.

**Por que importa:** Anúncios com health abaixo de 0.85 perdem posição orgânica progressivamente no ranking ML. Se as campanhas de Himmel forem pausadas, ajustadas ou tiverem orçamento reduzido, esses dois anúncios não têm exposição orgânica saudável para sustentar o volume atual. O GMV cai não por falta de demanda, mas por invisibilidade. Além disso, health degradada persistente pode agravar a penalização ao longo do tempo — não é ponto fixo.

**Histórico:** Sem memória anterior consolidada; não é possível afirmar se essa health já foi registrada antes ou se é deterioração recente. Esta é a leitura inaugural.

**Sinal de confirmação:** `MLB4073003575` e `MLB3288536143` mantendo health abaixo de 0.80 por 3 dias consecutivos (se disponível no pacote) confirma penalização orgânica ativa e persistente — não leitura pontual. Combinado com redução de pedidos nesses SKUs sem mudança de campanha ADS, confirma o mecanismo.

---

### Sinais a observar

1. **ADS share superar 60% do GMV por 3 dias seguidos** confirma dependência estrutural consolidada — o orgânico não sustenta o patamar atual sem o nível de investimento de Himmel. Calcular diariamente: `revenue_ads_yesterday_brl / gmv`. Janela: próximos 5 dias úteis.

2. **`MLB4073003575` (Kit 4 Potes 1050ml) com health abaixo de 0.80 em 2 dos próximos 3 dias com dado disponível** confirma penalização progressiva no 2º campeão de volume — neste caso, a exposição orgânica do anúncio está em deterioração ativa, não em ponto baixo recuperável. Se disponível no pacote.

3. **`MLB4410218897` (Kit 06 Canequinhas Acrílico) sem `available_quantity` ou com ruptura confirmada na próxima leitura** encerra esse vetor de cauda — se não reabastecido em Full, some do ranking por ausência de estoque no CD do ML.