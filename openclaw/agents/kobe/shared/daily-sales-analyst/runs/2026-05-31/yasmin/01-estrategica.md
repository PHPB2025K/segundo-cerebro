<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória recente robusta: weekly.md com 6 entradas diárias de 22/05 a 30/05; monthly.md sem tese preenchida (template vazio). Todos os blocos do `ml_snapshot` retornaram `status:ok` — reputação, fulfillment mix, mercadolider, ads_summary e account_overview disponíveis com 100% de cobertura. Ressalva operacional: `no_health_data_count=62` dos 82 anúncios ativos sem nível de qualidade calculado, tornando a leitura de saúde da base parcial. Status DADOS_PARCIAIS reflete volume +77,6% acima do avg_30d fora da banda normal, mas reconciliação bate com perfeição (`order_delta=0`, `revenue_delta=0`).

---

### Leitura temporal

- **Ruptura de banda em todas as janelas:** O dia (`pedidos_validos=189`, `gmv=R$8.267,83`) está acima de 7d (+44,2% em pedidos / +24,9% em GMV, `avg_7d.avg_gmv=R$6.621,90`), de 30d (+77,6% / +62,0%, `avg_30d.avg_gmv=R$5.102,43`) e de 60d (+73,7% / +84,0%, `avg_60d.avg_gmv=R$4.494,18`). Com `days_with_data=57`, o movimento não é artefato de janela curta — rompe o patamar de bimestre com consistência em ambas as dimensões.

- **Controle de sazonalidade:** Os quatro domingos anteriores têm banda de R$4.359–R$5.180 e média de R$4.223,06 / 86,25 pedidos (`same_weekday_avg`). O dia rompe o teto em +95,8% de GMV e +119,1% de pedidos. A explicação sazonal não cobre o movimento — o dia foi estruturalmente acima do padrão do dia da semana.

- **Trajetória de Platinum:** O progresso acumulado nos últimos 10 ciclos documentados saiu de 81,34% (22/05) para 93,28% hoje; o gap comprimiu de R$55.226 para R$19.876. O dia contribuiu R$8.267,83 sobre um `ritmo_diario_brl=R$4.602,05` — 79,7% acima do pace médio, maior entrada documentada na série recente.

- **Hipóteses anteriores:** (a) Kit 6 Canecas Tulipa (MLB6167272090) em ruptura iminente — **confirmada**: `status=paused`, `available_quantity=0`, 4 pedidos gerados hoje = cancelamentos prospectivos garantidos; risco documentado desde 22/05 finalmente se materializou. (b) MLB3288536143 com cobertura crítica pós-30/05 — **confirmada parcialmente**: `available_quantity=38` no snapshot após 121 unidades vendidas no dia; cobertura inferior a 1 dia ao ritmo atual. (c) Nível de qualidade 0,71 do MLB3288536143 estável — nono ciclo idêntico, direção ainda não observável externamente; gatilho de alinhamento Yasmin–Himmel era abaixo de 0,70, ainda não acionado.

---

### Leitura estratégica

- **Lente 1 — Patamar:** A conta rompeu o teto da banda de 60d em GMV e pedidos de forma consistente em todas as janelas, incluindo o controle de dia da semana. A compressão de ticket (-8,8% vs 30d, `ticket_vs_30d_pct`) não contradiz o movimento — é efeito de composição: o cluster IMB501 (menor valor unitário) respondeu por 64% do volume, e o ticket vs 60d segue positivo (+5,9%, `ticket_vs_60d_pct`). O patamar de R$8k+ em um domingo representa nível inédito na série documentada.

- **Lente 3 — Concentração e modalidade de envio:** O cluster IMB501 (três variações no mesmo MLB3288536143) gerou 121 dos 189 pedidos do dia (64%), todos via modalidade de envio Full. A assimetria estrutural se aprofundou: `fulfillment_mix_yesterday_top10.full_pct=89,6%` vs `account_overview.active_analysis.fulfillment_mix.full_pct=39,0%` — os campeões operam quase exclusivamente em Full enquanto 61% da base ativa está em Cross-Docking. `top3_concentration=64,0%` por múltiplos ciclos sem segundo vetor emergindo confirma dependência estrutural crônica, não recente. Com `available_quantity=38` no MLB3288536143, a conta está a menos de um dia de ruptura no único vetor que sustenta o novo patamar.

- **Lente 4 — Buy Box catálogo vs ranking de categoria:** MLB3288536143 (`is_catalog=false`, `listing_type=gold_special`) e MLB4073003575 (`is_catalog=false`) competem por posição em categoria — não por Buy Box. Com `health=0,71` (nível regular — nono ciclo) no MLB3288536143 e `health=0,75` (nível regular — série contínua) no MLB4073003575, a exposição orgânica desses dois anúncios está sob pressão sistêmica. A hipótese de que ADS (Himmel) compensa a degradação do ranking orgânico permanece indecidível sem breakdown de `revenue_ads` por `platform_item_id`, mas a coincidência de ADS share elevado com nível de qualidade estagnado sustenta a leitura. MLB6232315532 (Kit 6 Canecas Lisas, `is_catalog=true`, `gold_pro`, `available_quantity=54`) é o único anúncio de Catálogo no top do dia e está com estoque confortável pós-restock confirmado em 30/05 (31→61→54 hoje).

- **Lentes 5 e 6 — ADS e MercadoLíder Platinum:** ADS share do dia = 51,4% (`revenue_ads_yesterday_brl=R$4.245,82` / `gmv=R$8.267,83`), ROAS 10,05x, ACOS 8,69% — quinto ponto consecutivo de ADS share entre 49,5% e 69,9% (série 22/05 a 31/05). O orgânico nunca sustentou mais de ~50% sozinho na série registrada; a conta opera em zona de ADS dominante de forma estrutural, não episódica. Com `mercadolider.platinum.gap_revenue_brl=R$19.876,77` e `progress_pct=93,28%`, o dia de hoje acelerou decisivamente o ETA para Platinum (4,3 dias ao ritmo atual). A promoção está ao alcance de uma semana — mas é diretamente vulnerável a cancelamentos automáticos por ruptura no MLB3288536143, que entrariam na janela 60d rolling imediatamente.

---

### Tese da conta

**Vulnerável.** A conta está em ganho de patamar real — GMV e pedidos rompem a banda de 60d de forma consistente em todas as janelas comparativas, e a trajetória de MercadoLíder Platinum (93,28% de progresso, ETA 4,3 dias) é o reflexo financeiro de uma acumulação consistente ao longo de semanas. O problema é que esse patamar repousa sobre estrutura frágil: um único anúncio (MLB3288536143, Full, nível regular 0,71) gerou 64% dos pedidos do dia com apenas 38 unidades disponíveis — cobertura inferior a um dia ao ritmo atual. ADS sustenta mais de 50% do faturamento há pelo menos 10 ciclos sem melhora observada no nível de qualidade dos dois principais campeões. MLB6167272090 confirmou hoje a ruptura prevista desde 22/05 (pausado, 4 cancelamentos prospectivos). A conta está simultaneamente no pico histórico de patamar e na maior fragilidade operacional documentada — o próximo ciclo decide se o patamar se consolida ou retrai abruptamente.

---

### Risco estrutural principal

- **Risco:** Ruptura iminente de estoque no MLB3288536143 (Conjunto 5 Potes de Vidro Redondos, modalidade de envio Full), anúncio que concentrou 64% dos pedidos do dia com `available_quantity=38` após 121 unidades vendidas.
- **Por que importa:** Uma ruptura aqui não é perda de um produto — é colapso do patamar inteiro. Quando estoque no CD do ML zera em Full, o anúncio pausa automaticamente; recompor posição leva dias (trânsito de reposição + reindexação). Com `health=0,71` (nível regular), queda adicional por inatividade pode deprimir ainda mais o nível de qualidade, atrasando recuperação de ranking pós-reposição. Cancelamentos automáticos por falta de estoque impactam `cancellations_rate` da reputação — hoje em zero — e comprimem diretamente o progresso para Platinum via janela 60d rolling, podendo reverter o ETA de 4,3 dias para semanas.
- **Histórico:** Risco documentado desde 30/05 com cobertura estimada em 2-4 dias ao ritmo médio. O volume de hoje (121 unidades, ~2,4x o ritmo projetado) consumiu a folga sem reposição confirmada no pacote.
- **Sinal de confirmação:** `available_quantity` do MLB3288536143 chegando a zero ou `status=paused` no próximo snapshot confirma ruptura ativa. Aumento de `cancellations_rate` acima de zero nos próximos 3-5 ciclos confirma impacto no termômetro de reputação.

---

### Sinais a observar

1. **`available_quantity` do MLB3288536143 abaixo de 10 ou `status=paused` no próximo snapshot** confirma ruptura em curso — ao ritmo do dia (121 unidades), as 38 disponíveis não cobrem 24h; se reposição não entrou no CD do ML antes do fechamento do estoque, o anúncio pausa e o vetor de 64% do volume é suspenso; dois dias seguidos sem esse anúncio no ar confirmam reversão do patamar.

2. **`cancellations_rate` da reputação saindo de zero nos próximos 3 ciclos** confirma que os cancelamentos prospectivos do MLB6167272090 (Tulipa, pausado, 4 pedidos hoje com `available_quantity=0`) e/ou qualquer cancelamento automático por ruptura do MLB3288536143 já entraram na janela oficial da API — a métrica oficial hoje está em zero com 6 cancelamentos no dia; subida da taxa oficial sinaliza erosão silenciosa do termômetro antes de aparecer no agregado.

3. **Progresso MercadoLíder Platinum ultrapassando 96% com gap abaixo de R$12k em 2 dias seguidos** confirma que a promoção está no gatilho imediato de comunicação para Yasmin — ao ritmo de R$4.602/dia, o gap de R$19.876 fecha em ~4,3 dias; mas se MLB3288536143 pausar por falta de estoque, o ritmo diário colapsa e o ETA sobe abruptamente; os dois sinais — estoque e progresso — devem ser lidos em conjunto no próximo ciclo.