<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly.md contém 8 entradas diárias acumuladas (22/05–01/06) com hipóteses ativas e série contínua de estoque e saúde por anúncio; monthly.md é template sem conteúdo preenchido para junho. Todos os blocos ml_snapshot estão presentes com coverage 100%. A principal lacuna persistente (11º ciclo sem resolução): breakdown de ADS spend/revenue por platform_item_id e available_quantity por variação dentro de anúncios multi-variação. Base suficiente para tese forte em patamar e exposição estrutural; tese sobre drivers intra-ADS segue parcial.

---

### Leitura temporal

- **Mesmo dia da semana (terças):** R$4.230 (05/05) → R$4.081 (05/12) → R$5.760 (05/19) → R$7.394 (05/26) → R$9.210 (02/06). Cinco pontos consecutivos, cada semana acima da anterior. A média histórica de terças é R$5.366 (`same_weekday_avg.avg_gmv`); hoje é +71,6% acima disso. Não é ruído nem sazonalidade — é aceleração estrutural semanal confirmada.

- **Patamar 30d/60d:** GMV de R$9.210 está +73,6% acima da média 30d (R$5.306) e +107% acima da média 60d (R$4.448). A média de 7 dias já está elevada em R$7.758 e hoje ainda supera essa baseline em +18,7%. A conta não está oscilando dentro de uma banda — está empurrando o teto para cima em todas as janelas simultaneamente.

- **Volume vs ticket:** `orders_vs_30d_pct=+77,0%` vs `gmv_vs_30d_pct=+73,6%`, com `ticket_vs_30d_pct=-2,0%`. O ticket hoje (R$46,76) está ligeiramente abaixo do 30d (R$47,69) mas +11,5% vs 60d (R$41,92). O ganho é inteiramente de volume — o ticket não está corroendo, está sendo comprimido pelo mix do dia (Tampa Preta Cross-Docking em 56 pedidos, de menor valor agregado por unidade, puxando o ticket para baixo em relação à semana recente).

- **Hipóteses anteriores:** (1) Ruptura iminente do Kit 4 Potes 1050ml (MLB4073003575) — **confirmada**: memória de 01/06 apontava available_quantity=13 no snapshot; hoje, após 12 pedidos, `available_quantity=2`. Ruptura é praticamente certa. (2) Ciclo pausada/venda/cancelamento da Tulipa (MLB6167272090) — **não resolvido, reativado**: memória de 01/06 registrava reposição parcial de 2 unidades; hoje anúncio volta a `status=paused`, `available_quantity=0`, com 8 pedidos no dia — oitavo evento do padrão recorrente. (3) Descida do ADS share como sinal de orgânico em expansão — **parcialmente enfraquecida**: após cair de 69,9% para 48,1% em série de 10 ciclos, hoje sobe para 54,9%, quebrando a monotonia descendente.

---

### Leitura estratégica

- **Lente 1 — Patamar:** A conta rompeu o teto de 30d e 60d de forma consistente, não pontual. Cinco terças seguidas com crescimento sequencial, 7d baseline (R$7.758) já 46% acima do 30d — o patamar se realimentou. A tese de acomodação está descartada; a questão agora é qual é o piso do novo patamar. Hipótese: o volume incremental é sustentado pela combinação de ADS eficiente (ROAS 14,45x, ACOS 4,7%) com o cluster IMB501 em Full consolidando presença orgânica, mas a estrutura ainda não tem segundo vetor independente do cluster — o patamar é real mas concentrado.

- **Lente 3 + 4 — Dependência e modalidade de envio:** O cluster IMB501 (Tampa Preta MLB4535865317 + Tampa Cinza/Vermelha MLB3288536143) respondeu por 99 pedidos = 50,3% do dia (`top3_concentration`). A dependência estrutural é crônica — ela aparece em todos os 8 ciclos da weekly.md. O mix de modalidade de envio do top 10 no dia foi 48,1% Full / 51,9% Cross-Docking (`fulfillment_mix_yesterday_top10`), contrastando com a janela de 7 dias (Full 84,0% / Cross-Docking 16,0% — `fulfillment_mix_7d`). Essa divergência não é contradição: Tampa Preta (56 pedidos, Cross-Docking) dominou o dia e deslocou o mix diário, enquanto a base semanal reflete dias anteriores mais Full-pesados. O risco está na assimetria: quando a dependência do dia recai sobre um anúncio Cross-Docking sem controle de estoque no CD do ML, a Budamix retém a alavanca — mas quando recai sobre Full (MLB3288536143, MLB4073003575), a ruptura é silenciosa e sem mecanismo de reposição imediata.

- **Lente 5 — ADS:** R$350,07 em gasto gerou R$5.059,39 em receita atribuída — ROAS 14,45x, ACOS 4,7%, ADS share 54,9% do GMV. A campanha de Himmel opera em nível de eficiência extrema (ROAS >8x, ACOS <8%); o aumento de share hoje vs 01/06 (48,1% → 54,9%) pode ser efeito composicional: os 8 pedidos da Tulipa pausada que virarão cancelamentos podem ter sido atribuídos a ADS e inflado o numerador sem confirmar receita realizada. Sem breakdown por platform_item_id, essa hipótese permanece em aberto. Mesmo assim, a conta está em zona de ADS dominante (>50%) — não fragilidade aguda, mas estruturalmente vulnerável a pausa de campanhas.

- **Lente 6 — MercadoLíder Platinum:** Gap de R$11.621,68 com progresso 96,07% e ETA de 2,5 dias ao ritmo de R$4.739,64/dia (`mercadolider.platinum`). O GMV de hoje (R$9.210) equivale a 79,3% do gap restante em um único dia — a promoção para Platinum está ao alcance de 2–3 dias sem novos retrocessos. A ameaça não é o volume: é a qualidade. `cancellations_rate=0` na API (janela longa), mas a série de cancelamentos diários (`metrics.cancelamentos`) nas últimas semanas acumulou 3→3→2→6→9→2 (hoje: 2). Os 8 pedidos do anúncio Tulipa (MLB6167272090) pausado com estoque zero são cancelamentos prospectivos garantidos e ainda não aparecem na métrica oficial — quando entrarem na janela rolling, pressionam o threshold de ≤ 0,5% que é pré-requisito para manter a medalha.

---

### Tese da conta

A conta Mercado Livre está **em ganho de patamar**. A evidência não é o dia — é a série de cinco terças consecutivas com crescimento sequencial (R$4.081 → R$9.210), o 7d baseline já 46% acima do 30d médio, e a confirmação em mais de duas janelas temporais. O volume está se estruturando num nível novo, não oscilando dentro da banda histórica. A vulnerabilidade que impede classificar como "saudável" é tripla e simultânea: (1) dependência crônica de 50,3% do volume em um único cluster (IMB501), sem segundo vetor estrutural; (2) ruptura praticamente certa do Kit 4 Potes 1050ml em Full (available_quantity=2) que remove um dos suportes do novo patamar; (3) ciclo crônico da Tulipa gerando cancelamentos prospectivos recorrentes que ameaçam a janela de Platinum — a conquista mais próxima da trajetória.

---

### Risco estrutural principal

**Risco:** Ciclo crônico de pausa-venda-cancelamento do Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090). `status=paused`, `available_quantity=0`, 8 pedidos gerados hoje = 8 cancelamentos prospectivos confirmados. É o oitavo evento do padrão em 11 ciclos documentados na weekly.md.

**Por que importa:** Cada ciclo de cancelamento automático alimenta o `cancellations_rate` oficial do ML (janela rolling). A métrica hoje é 0,0 na API, mas a série de `metrics.cancelamentos` diária (3→3→2→6→9→2→8 prospectivos hoje) está em trajetória crescente. O threshold de Platinum exige `cancellations_rate ≤ 0,5%` — com 6.390 transações completas (`transactions_completed`), cada 32 cancelamentos representa 0,5 ponto percentual. O acúmulo dos ciclos da Tulipa, mais os cancelamentos dos anúncios pausados em histórico, pode mover esse indicador da zona verde para a zona de risco antes da promoção ser consolidada. Além disso, `ratings_negative=0,41` já está em 41% das avaliações — cancelamentos recorrentes intensificam essa pressão.

**Histórico:** Presente de forma contínua desde pelo menos 22/05 na weekly.md. Não é novo — é sistêmico. O padrão "reposição parcial → pausar novamente → novos pedidos → cancelamentos" ocorreu em 31/05 (4 pedidos paused) e hoje replica com escala maior (8 pedidos paused), sugerindo que a reposição não resolve o problema de forma durável.

**Sinal de confirmação:** `reputation.cancellations_rate` sair de 0,0 no próximo snapshot confirma que os cancelamentos acumulados já entraram na janela oficial de avaliação do ML. Combinado com o status de MLB6167272090 ainda como paused com available_quantity=0 no snapshot de amanhã, confirma o ciclo ativo — não episódico.

---

### Sinais a observar

1. **`reputation.cancellations_rate` > 0,0 no próximo snapshot (se disponível):** Confirma que os cancelamentos prospectivos da Tulipa (MLB6167272090 — 8 hoje, 4 em 31/05) entraram na janela rolling oficial. Se sair de zero com o ETA de Platinum em 2,5 dias, a promoção pode ser travada por métrica de qualidade, não por faturamento. Sinal crítico nos próximos 3 ciclos.

2. **MLB4073003575 (Kit 4 Potes 1050ml) com `available_quantity=0` ou `status=paused` no snapshot de amanhã:** Após 12 pedidos hoje com only 2 unidades restantes, ruptura em Full é praticamente certa. Confirmar se gera cancelamentos automáticos (second Full crítico simultâneo ao IMB501 — replica o padrão de risco identificado em 30/05 e 31/05). Dois Full em ruptura simultânea = compressão direta do volume do novo patamar.

3. **GMV sustentado acima de R$7.000 nos próximos 3 dias úteis (excluindo fins de semana):** Confirmaria que o novo patamar (R$7k–R$9k) é estrutural e não efeito pontual da terça acelerada. GMV abaixo de R$6.500 por 2 dias seguidos após o pico de hoje reabre a hipótese de oscilação dentro de banda — não de ganho de patamar consolidado.