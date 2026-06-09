<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória semanal robusta: 11 blocos diários acumulados (22/05–07/06) com hipóteses ativas rastreadas ciclo a ciclo. Monthly.md está no template vazio — sem tese mensal consolidada para cruzar. `ml_snapshot` completo: `reputation`, `mercadolider`, `fulfillment_mix` (7d/30d/top10), `top_items_details`, `ads_summary` e `account_overview` todos com `status: ok`. Base autoriza tese com confiança média-alta, limitada apenas pela ausência de tese mensal formal e pela impossibilidade de atribuir ADS por `platform_item_id` (pendência estrutural ativa há 18 ciclos).

---

### Leitura temporal

- **vs 60d e 30d — ruptura de patamar confirmada:** GMV +80,5% vs 60d (`avg_gmv` R$ 4.901 → R$ 8.850 no dia) e +49,1% vs 30d (`avg_gmv` R$ 5.936); pedidos +76,3% e +62,8% nas mesmas janelas. Ticket levemente comprimido vs 30d (`-8,4%`), coerente com composição do cluster IMB501 de menor valor unitário no topo — não é erosão de ticket, é efeito de mix.

- **vs mesmos dias da semana — novo patamar confirmado em dois ciclos consecutivos:** as quatro segundas anteriores (`same_weekday_last_4`) registraram R$ 3.664 → R$ 4.184 → R$ 5.127 → R$ 9.814 (01/06). Hoje R$ 8.850 é o segundo ponto acima de R$ 8.500 em segunda-feira consecutiva — média do controle sazonal era R$ 5.697. O dia 01/06 não foi um pico isolado; este ciclo confirma o patamar elevado como nova referência para segundas-feiras.

- **vs 7d — aceleração dentro da nova banda:** avg_7d R$ 7.484 → dia R$ 8.850 (+18,3%), pedidos +24,6%. A semana mais recente já opera num patamar acima do 30d, e hoje ainda supera a média semanal — a aceleração não inverteu.

- **Hipótese ativa confirmada — MercadoLíder Platinum:** desde 22/05 a memória rastreava a trajetória para Platinum (gap R$ 55k → R$ 42k → R$ 19k → R$ 11k → R$ 3,8k → 0). Hoje `power_seller_status=platinum` e `gap_revenue_brl=0`, `progress_pct=100`, `vendas_acima_threshold=4.994`. A promoção que os ciclos anteriores marcavam como "confirmar no próximo snapshot" **materializou-se neste ciclo**.

---

### Leitura estratégica

- **Lente 6 — Platinum conquistado; eixo estratégico muda de "atingir" para "manter":** a conta alcançou `platinum` com `sales_60d_revenue_brl=R$ 301.153` (+1,7% acima do threshold R$ 296.000) e `sales_60d_count_paid=6.778` (3,9x o threshold de 1.725 vendas). `próxima_medalha=null` — não há nível seguinte. O `ritmo_diario_brl=R$ 5.019` é o floor necessário para sustentar a janela rolling de 60 dias. GMV de hoje (R$ 8.850) opera 76% acima do ritmo mínimo. O risco imediato não é perder o Platinum por faturamento, mas pelos **indicadores de qualidade**: `cancellations_rate=0`, `claims_rate=0,0018` (36% do threshold de 0,005), `delayed_handling_rate=0,0009` — todos folgados. Entretanto, `ratings_negative=0,41` permanece em padrão persistente (0,39→0,41 em múltiplos ciclos), e qualquer cancelamento automático de anúncio com estoque crítico (como ocorreu em 06/06 com MLB3288536143 pausado com 67 pedidos) entrará na janela oficial antes do threshold aparecer no indicador agregado — risco silencioso, não bloqueante hoje.

- **Lente 5 — ADS share abaixo de 50% em dia de alto volume: orgânico em expansão estrutural:** ROAS `4.169,41 / 429,97 = 9,70x`, ACOS `11,67%`, ADS share `4.169,41 / 8.850,18 = 47,1%`. A série monotonicamente descendente desde 22/05 — 69,9% → 56,7% → 60,7% → 59,5% → 51,4% → 48,1% → **47,1%** — enquanto o GMV sobe é o sinal estrutural mais relevante da conta no período: o orgânico cresceu proporcionalmente mais rápido que a campanha. Himmel não escalou investimento no mesmo ritmo do volume; a conta está entregando mais com a mesma verba. Fragilidade latente existe (quase 50% de ADS dependency), mas a direção é a correta.

- **Lente 3 — Dependência de modalidade de envio: campeões em Full divergem da base, restock IMB501 avança a cobertura, mas Kit 4 Potes 1050ml permanece exposto:** mix do top10 ontem: Full 78,5% / Cross-Docking 21,5% (`fulfillment_mix_yesterday_top10`); base ativa: Full 42,1% / Cross-Docking 57,9% (`account_overview.active_analysis.fulfillment_mix`); 30d: Full 79,6%. Os campeões operam quase integralmente via modalidade de envio Full — 36pp acima da base. O `MLB3288536143` (Conjunto 5 Potes Tampa Cinza/Vermelha) retornou com `available_quantity=1.056` após o ciclo crítico de 06/06–07/06 (que havia registrado 2 unidades); restock confirmado, cobertura restaurada. Porém `MLB4073003575` (Kit 4 Potes 1050ml Full) tem `available_quantity=33` com 15 pedidos no dia (~2,2 dias de cobertura) — segunda aparição em zona estreita em 7 dias.

- **Lente 4 — Health crônico degradado nos vetores de volume:** `MLB3288536143` `health=0,71` (nível regular) há 17+ ciclos; `MLB5402326666` `health=0,66` (nível preocupante) há 4+ ciclos; `MLB4073003575` `health=0,75` (nível regular). Esses três anúncios geraram 54 pedidos hoje (26,9% do total) enquanto operam em faixas que o ML penaliza com redução de ranking orgânico. A conta cresceu de patamar **com os campeões degradados** — o que significa que parte do crescimento é sustentada por ADS e reputação Platinum compensando a perda de exposição orgânica nesses anúncios, não por melhora de ranking. Estruturalmente, a conta poderia converter mais com health restaurado.

---

### Tese da conta

**Em ganho de patamar.** A evidência é consistente em três janelas temporais independentes (7d, 30d, 60d), confirmada pelo controle sazonal (segundo Monday consecutivo acima de R$ 8.500 vs média de R$ 5.697), e coroada pela promoção a MercadoLíder Platinum — resultado direto da trajetória de 45 dias rastreada na memória. O orgânico está expandindo em proporção maior que ADS (share desceu de 70% para 47% enquanto GMV subiu 80%), sinalizando que o ganho de patamar tem componente estrutural, não apenas de mídia. A dependência do cluster IMB501 em Full permanece alta, e a degradação crônica de health nos campeões é o risco que pode limitar o teto desse patamar — mas nenhum dos dois qualifica como deterioração no ciclo atual.

---

### Risco estrutural principal

**Risco:** Degradação crônica de nível de qualidade nos anúncios campeões em Full — `MLB3288536143` (`health=0,71`, nível regular, 17+ ciclos), `MLB4073003575` (`health=0,75`, nível regular, 11+ ciclos) e `MLB5402326666` (`health=0,66`, nível preocupante, 4+ ciclos) — enquanto esses três anúncios concentram 26,9% dos pedidos e operam via modalidade de envio Full com gap de 36pp acima da base ativa.

**Por que importa:** ML reduz ranking orgânico progressivamente em anúncios com health abaixo de 0,85. Atualmente, ADS e o boost de MercadoLíder Platinum compensam parte dessa perda. Se ACOS subir (por campanha menos eficiente ou entrada de concorrente) ou se o boost Platinum não cobrir a erosão orgânica, esses anúncios perdem exposição sem sinal visível no faturamento de curto prazo — até que a queda seja grande o suficiente para aparecer nos números. O fato de a conta ter crescido de patamar **com** esses níveis degradados não significa que a degradação é inócua; significa que outros vetores (ADS, Platinum, restock) estão compensando.

**Histórico:** presente desde pelo menos 22/05 (primeiro registro na memória semanal disponível). Não melhorou, não piorou — estabilizou em patamar ruim. `MLB5402326666` entrou em zona ainda pior (0,66) no início de junho.

**Sinal de confirmação:** `MLB5402326666` (`health`) caindo abaixo de 0,63 em qualquer snapshot, ou `MLB3288536143` ou `MLB4073003575` registrando queda de saúde em relação ao valor atual por dois ciclos consecutivos — indicaria aceleração da erosão, não apenas estabilização no nível ruim.

---

### Sinais a observar

1. **Kit 4 Potes 1050ml (MLB4073003575, Full) — cobertura de estoque:** `available_quantity=33`, 15 pedidos hoje (~2,2 dias). Se o próximo snapshot registrar `available_quantity < 15` ou `status=paused`, ruptura em vetor Full ativo se materializa — impacta diretamente o Mix de modalidade de envio do top e o cancellations_rate da janela Platinum.

2. **Kit 6 Canequinhas Acrílico (MLB6073033006, Full) — cobertura crítica:** `available_quantity=19`, 11 pedidos hoje (~1,7 dias de cobertura). Primeiro aparece como sinalizador em dois ciclos consecutivos. Se `available_quantity < 8` ou `status=paused` no próximo snapshot, confirma segundo vetor Full em ruptura simultânea ao MLB4073003575.

3. **ADS share abaixo de 50% pelo segundo ciclo consecutivo em dia de GMV acima de R$ 7.000:** se confirmado nos próximos 2 dias úteis, a hipótese de expansão orgânica estrutural (orgânico crescendo mais rápido que campanha) deixa de ser hipótese e vira fato consolidado — muda a leitura estratégica sobre dependência de Himmel e abre espaço para avaliar se a verba ADS está sub-aproveitada ou bem calibrada.