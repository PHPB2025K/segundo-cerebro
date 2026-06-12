<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Robusta: weekly.md com 14 entradas diárias (22/05–10/06), janelas 7d/30d/60d disponíveis com cobertura plena (days_with_data: 7/30/59), reputação e mix de modalidade de envio presentes no pacote com `coverage_pct=100%`. Exceção crítica: `ml_snapshot.ads_summary.spend_yesterday_brl=0,0` com `campaigns_active_count=13` — padrão inconsistente que contradiz todos os ciclos da memória recente (10/06: R$412,15; 09/06: ~R$274; 08/06: ~R$430), indicando provável lag de API Mercado Ads. Dados de ADS são inutilizáveis neste ciclo; confiança da leitura sobre vetor orgânico vs pago está suspensa.

---

### Leitura temporal

- **vs 60d e 30d — patamar de volume confirmado, ticket em compressão:** O dia (`pedidos_validos=185, gmv=R$7.304,72`) está +55,7% em pedidos e +43,0% em GMV sobre `avg_60d` (118,8 pedidos / R$5.106,88) e +36,9% / +12,7% sobre `avg_30d` (135,1 / R$6.481,90). O patamar de volume é real e documentado em múltiplos ciclos — não é ruído. O ticket, porém, comprimiu consistentemente: R$39,48 hoje vs R$47,97 em 30d (`ticket_vs_30d_pct=-17,7%`) e R$42,99 em 60d (`ticket_vs_60d_pct=-8,2%`), reflexo direto do peso crescente do cluster IMB501 (Tampa Preta 66 + Tampa Vermelha 27 + Tampa Cinza 24 = 117 pedidos = `top3_concentration=63,2%`).

- **vs mesmos dias da semana — mais pedidos, menos GMV que as quintas recentes:** `orders_vs_same_weekday_pct=+26,9%` (avg 145,75), mas `gmv_vs_same_weekday_pct=-1,7%` (avg R$7.433,59). As duas quintas anteriores foram mais fortes em GMV: R$8.617 em 04/06 e R$8.463 em 28/05. O dia gerou o maior volume de pedidos das últimas 4 quintas mas o menor GMV das últimas 3 — a divergência não é queda de exposição, é mix: quando IMB501 domina acima de 60% do volume, o ticket médio da conta cai e o GMV não acompanha o crescimento de pedidos.

- **vs 7d — aceleração de pedidos com GMV estável:** `orders_vs_7d_pct=+13,5%` com `gmv_vs_7d_pct=-2,1%` (avg_7d: 163,0 pedidos / R$7.460,91). A última semana já operava com esse padrão — volume em alta, ticket comprimindo. A hipótese de trajetória ADS share descendente (69,9%→44,3% desde 22/05), que seria a explicação para o crescimento orgânico proporcional, fica **temporariamente indecidível** por ausência de dado válido de Mercado Ads.

- **Hipóteses anteriores — confirmações e suspensões:** (a) MLB6232315532 (Catálogo Canecas Lisas 200ml) foi apontado na memória de 10/06 com `available_quantity=5` e ruptura iminente → hoje `available_quantity=4` com 5 pedidos: **confirmado em trajetória de ruptura**. (b) MLB4073003575 restock parcial reportado em 10/06 (28 un) → hoje 19 un após 7 pedidos: **restock não resolveu** — terceiro ciclo de cobertura crítica. (c) Tese ADS share descendente → **suspensa** neste ciclo.

---

### Leitura estratégica

- **Lente 1/3 — Volume em novo patamar, mas sustentado por concentração extrema em um único anúncio:** A elevação de patamar (+56% pedidos vs 60d) é estruturalmente real mas operacionalmente frágil: MLB3288536143 responde por 63,2% do volume do dia em suas três variações (tampa Preta/Vermelha/Cinza), operando em `health=0,71` (nível regular) no 18º+ ciclo consecutivo idêntico. Um anúncio em nível regular não explora a totalidade da exposição Platinum — o patamar de pedidos existe apesar da qualidade degradada do líder, não por causa de uma operação saudável. `paused=125` vs `active=82` (`paused > active × 1,52`) confirma que a cauda está morta; o segundo vetor estrutural não existe: a conta opera com um líder e cross-docking de suporte.

- **Lente 3/4 — Itens adjacentes em ruptura recorrente abortam formação de segundo vetor:** Kit 6 Canecas Tulipa 250ml (`MLB6167272090`, `available_quantity=5`, 12 pedidos hoje) e Kit 6 Canecas Lisas 200ml (`MLB6232315532`, Catálogo `gold_pro`, `available_quantity=4`, 5 pedidos hoje) somam 17 pedidos (9,2% do dia) e estão em ruptura praticamente imediata — a Tulipa com menos de 0,5 dia de runway e a Canecas Lisas com menos de 1 dia. Este é o único Catálogo no topo: quando `MLB6232315532` pausar por estoque, a posição de Buy Box em catálogo vai para concorrente e a recuperação é mais lenta que para Clássico. `MLB4073003575` (Kit 4 Potes 1050ml, `available_quantity=19`, 7 pedidos) está no terceiro ciclo de cobertura curta sem solução definitiva. A formação de segundo vetor está sendo sistematicamente abortada por gestão de reposição insuficiente nos itens adjacentes.

- **Lente 2/6 — Platinum sólido nos números, ratings_negative é vetor inobservável:** `power_seller_status=platinum`, `color=5_green`, `cancellations_rate=0`, `claims_rate=0,0013` (26% do threshold 0,005), `delayed_handling_rate=0,0007` — saúde estrutural no topo. `ritmo_diario_brl=R$5.335,49` vs pace mínimo ~R$4.933/dia para manter Platinum; o dia (R$7.304) contribui +47,9% acima do necessário. O risco silencioso é `ratings_negative=0,41` estagnado em múltiplos ciclos com `ratings_positive=0,56` — não é ruptura, mas é proporção anormal para uma conta Platinum que nunca teve breakdown por motivo de avaliação disponível no pacote.

- **Lente 5 — ADS indecidível, continuidade da tese de autonomia orgânica suspensa:** `spend_yesterday_brl=0,0` com `campaigns_active_count=13` é inconsistência: todos os 13 ciclos da memória com ADS disponível mostraram gasto entre R$262 e R$422. Zero spend com campanhas ativas é lag de API, não realidade operacional. Não é possível calcular ADS share nem ROAS para o dia. A série descendente de ADS share (69,9%→44,3% desde 22/05), que seria o sinal mais estratégico da conta, fica suspensa até o próximo ciclo com dado.

---

### Tese da conta

**Vulnerável.** A conta opera em patamar de volume claramente elevado (+56% pedidos vs 60d, MercadoLíder Platinum sólido com gap=R$0), mas a estrutura de sustentação é de alto risco de concentração: 63,2% do volume diário descansa em variações de um único anúncio (`MLB3288536143`) com `health=0,71` (nível regular) no 18º+ ciclo consecutivo; os itens adjacentes que poderiam compor segundo vetor (Tulipa 250ml, Canecas Lisas 200ml, Kit 1050ml) operam em cobertura crítica recorrente sem solução definitiva de reposição — e o único Catálogo do topo (`MLB6232315532`) está em ruptura virtual com `available_quantity=4`. O patamar de pedidos é real; a vulnerabilidade é que qualquer pausa no líder tira mais de 60% do volume de um dia, e os itens que deveriam absorver estão eles mesmos em zona de ruptura. A tese sobre ADS share (potencial autonomia orgânica estrutural) permanece temporariamente indecidível.

---

### Risco estrutural principal

**Risco:** Dependência crônica de anúncio único (`MLB3288536143`, nível regular `health=0,71`, 18+ ciclos) sem formação de segundo vetor funcional — abortada sistemáticamente por rupturas recorrentes de estoque nos itens adjacentes.

**Por que importa:** A conta tem MercadoLíder Platinum e volume elevado, mas qualquer pausa ou queda de `health` em `MLB3288536143` afeta proporcionalmente 60%+ do volume. Os itens que deveriam compor a cauda viva e eventualmente um segundo vetor (Tulipa 250ml, Canecas Lisas Catálogo, Kit 1050ml, Kit 640ml com `health=0,66` nível preocupante) voltam à zona crítica a cada ciclo — o que significa que a conta nunca consegue diversificar organicamente o volume, mesmo tendo 82 anúncios ativos. O patamar Platinum fica refém de um único anúncio em qualidade degradada.

**Histórico:** Documentado desde 22/05 (início da memória disponível). `top3_concentration` nunca saiu do intervalo 44–65% em nenhum ciclo registrado. `health=0,71` de MLB3288536143 aparece idêntico em todos os ciclos com dado. As rupturas nos adjacentes (Tulipa, Catálogo Canecas, Kit 1050ml) foram registradas em pelo menos 8 ciclos consecutivos sem resolução estrutural.

**Sinal de confirmação:** `top3_concentration` acima de 65% por dois ciclos consecutivos de quinta (dia de maior volume) enquanto Tulipa 250ml e Canecas Lisas 200ml aparecerem simultaneamente `status=paused` confirma que o segundo vetor foi abortado e a dependência aumentou — não acomodou.

---

### Sinais a observar

1. **MLB6232315532 (Kit 6 Canecas Lisas 200ml — único Catálogo do topo, `available_quantity=4` com 5 pedidos hoje):** Se o snapshot amanhã mostrar `status=paused` ou `available_quantity=0`, a posição de Buy Box no catálogo foi perdida e a reativação exige restock no CD do ML antes de recuperar ranking — ciclo mais lento que Clássico. Sinal: `status=paused` no próximo ciclo confirma ruptura de Buy Box em Catálogo; dois ciclos seguidos confirma perda de posição estrutural nesta página.

2. **ADS share no próximo ciclo com dado válido (`spend > 0`):** Quando o dado retornar, verificar se o ADS share cruza abaixo de 40% com GMV sustentado (dois ciclos consecutivos) — esse seria o sinal de confirmação da hipótese de autonomia orgânica estrutural, a mais relevante da conta neste momento. ADS share acima de 55% no retorno indicaria que o GMV de hoje foi artificialmente comprimido sem ADS, não que o orgânico expandiu.

3. **MLB4073003575 (Kit 4 Potes 1050ml, `available_quantity=19`, 7 pedidos hoje, runway ~2,7 dias):** Se o snapshot de 13/06 mostrar `available_quantity < 10` sem restock confirmado, o terceiro ciclo de cobertura crítica sem resolução definitiva classifica como falha estrutural de reposição — não episódio isolado — e aciona necessidade de alinhamento Yasmin sobre ETA de entrada no CD do ML para este item.