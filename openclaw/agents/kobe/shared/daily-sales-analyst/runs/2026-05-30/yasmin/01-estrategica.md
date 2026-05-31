<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly.md acumulou cinco entradas diárias (22–26/05) com hipóteses ativas rastreadas e padrões identificados; monthly.md sem tese mensal preenchida (conta com ~6 semanas de operação sob Yasmin). Janelas 7d (7 dias completos), 30d (29 dias) e 60d (59 dias) disponíveis. `ml_snapshot` completo — reputação, MercadoLíder, mix de modalidade de envio, `top_items_details` e `ads_summary` presentes. Base robusta para tese neste ciclo; hipóteses das cinco entradas anteriores avaliadas abaixo.

---

### Leitura temporal

- **vs 30d e 60d (patamar):** O dia (`pedidos_validos=130`, `gmv=R$5.678,64`) está acima das médias de 30d (`orders_vs_30d_pct=+19,0%`, `gmv_vs_30d_pct=+13,6%`) e 60d (`orders_vs_60d_pct=+24,0%`, `gmv_vs_60d_pct=+26,0%`) em duas janelas longas simultâneas. Não é ruído pontual — é consistência de patamar.

- **vs 7d (aceleração/desaceleração):** GMV -13,3% abaixo da `avg_7d=R$6.550,59` com pedidos +3,4%. O ticket médio hoje (R$43,68) está abaixo do 7d (R$52,11) — a semana recente foi distorcida por dias de ticket elevado; o sábado opera com composição naturalmente dominada pelo cluster IMB501 de menor valor unitário. Sem sinal de desaceleração estrutural.

- **vs mesmos dias da semana (sazonalidade):** Sábado tem variância histórica alta (58 a 184 pedidos nos últimos 4). Hoje (130 pedidos, GMV R$5.678,64) está +16,6% em pedidos e +10,8% em GMV acima da média dos 4 sábados anteriores (`avg=111,5 / R$5.125,86`). O resultado supera o controle sazonal — o dia foi genuinamente forte no seu próprio benchmark.

- **Hipóteses anteriores:** (a) MLB3288536143 `health=0,71` há sete ciclos consecutivos — **oitavo ciclo confirmado**; ausência de recuperação consolida hipótese de estagnação no nível preocupante. (b) Restock da Kit 6 Canecas Lisas 200ml (MLB6232315532): `available_quantity` agora em 61 unidades (vs 31 pós-venda em 26/05) — **restock confirmado**, risco de ruptura de Buy Box Catálogo suspenso neste ciclo. (c) Kit Canecas Porcelana Tulipa (MLB6167272090) ausente do top10 pelo segundo ciclo — **ruptura ou pausa presumida**, conforme antecipado nos três ciclos anteriores. (d) ADS share acima de 65% como gatilho de terceiro ciclo: share hoje é 59,5% — abaixo do gatilho original, mas ainda em zona ADS dominante; hipótese em aberto.

---

### Leitura estratégica

- **Patamar em alta; ticket em compressão por composição de sábado, não por deterioração de preço:** A conta opera consistentemente acima dos patamares de 30d e 60d em pedidos e GMV — o movimento tem consistência de tendência, não de evento. O ticket hoje (R$43,68 vs R$45,77 em 30d e R$52,11 em 7d) reflete composição sazonal: o cluster IMB501 (MLB3288536143, variações Tampa Preta 47 + Tampa Cinza 15 + Tampa Vermelha 9 = 71 pedidos = 54,6% do volume) domina sábados e tem ticket estruturalmente mais baixo. Não há erosão de preço médio — há efeito de mix intrínseco ao perfil do dia.

- **Cluster IMB501 no oitavo ciclo com health em nível preocupante — ADS cobrindo déficit orgânico silencioso:** MLB3288536143 concentrou 54,6% do volume do dia com `health=0,71` (nível preocupante) pelo oitavo ciclo consecutivo. Como `is_catalog=false`, o anúncio compete exclusivamente por ranking de categoria — e `health` nessa faixa reduz progressivamente a exposição orgânica atribuída pelo ML. O fato de o anúncio continuar vendendo não contradiz a erosão: o ADS de Himmel (`share=59,5%`, ACOS subindo de 4,4% para 8,23% na série recente) está compensando o alcance orgânico perdido. Isso não é ADS amplificando orgânico saudável — é ADS substituindo exposição que deveria ser orgânica.

- **Dependência de Full nos campeões é estruturalmente assimétrica:** `fulfillment_mix_yesterday_top10=91,5% Full` contra `account_overview.active_analysis.fulfillment_mix.full_pct=39%` na base geral. Os campeões operam quase exclusivamente em Full, enquanto dois terços da base ativa depende de Cross-Docking. Isso significa que qualquer ruptura de estoque nos top 3 em Full impacta desproporcionalmente o resultado. Sinal crítico hoje: MLB6437847224 (Kit 6 Potes Vidro Hermético, `is_catalog=true`, Full) com `available_quantity=7` e 3 pedidos no dia — cobertura de ~2,3 dias. Ruptura em Catálogo implica perda de Buy Box com recuperação lenta, distinta de anúncio Clássico.

- **MercadoLíder Platinum está no horizonte imediato — janela operacional apertada:** Com `gap_revenue_brl=R$23.327,75`, `progress_pct=92,12%` e `eta_dias_estimado=5,1 dias` ao ritmo atual (`ritmo_diario_brl=R$4.544,54`), a promoção para Platinum está dentro da janela dos próximos 5–6 dias. O GMV de hoje (R$5.678,64) está acima do pace necessário (~R$4.545/dia), contribuindo positivamente. O risco não é o ritmo médio — é evento adverso concentrado: cancelamentos automáticos por anúncio pausado com pedidos, ruptura no cluster Full IMB501 ou `cancellations_rate` saindo de zero podem atrasar a promoção de maneira relevante e direta.

---

### Tese da conta

A conta está **em ganho de patamar** — GMV e pedidos consistentemente acima das bandas de 30d e 60d, com MercadoLíder Platinum a menos de R$24k de faturamento e ETA de 5 dias. O ganho é, no entanto, **estruturalmente vulnerável** em dois eixos sobrepostos: o principal campeão orgânico (cluster IMB501, 54,6% do volume) opera com nível de qualidade do anúncio em nível preocupante há oito ciclos consecutivos sem sinal de recuperação, e o ADS de Himmel está cobrindo progressivamente esse déficit de alcance — com ACOS saindo de 4,4% para 8,23% na série recente como sinal do custo crescente dessa cobertura. A promoção para Platinum é iminente e real; a fragilidade estrutural por debaixo do resultado é igualmente real.

---

### Risco estrutural principal

- **Risco:** Erosão orgânica progressiva do cluster IMB501 (MLB3288536143) por `health` estagnado no nível preocupante (0,71) por oito ciclos consecutivos, com ADS de Himmel cobrindo o déficit de alcance — gerando dependência circular entre mídia paga e campeão degradado.

- **Por que importa:** MLB3288536143 concentrou 54,6% do volume do dia e é o principal vetor de venda da conta. Com `is_catalog=false`, compete exclusivamente por ranking de categoria; `health=0,71` (a três centésimos do gatilho de queda em 0,68) reduz progressivamente a exposição orgânica atribuída pelo ML. O custo da cobertura por ADS está subindo (ACOS: 4,4% → 10,96% → 8,23% na série de três ciclos) sem que a causa raiz — qualidade do anúncio — melhore. Se `health` cruzar 0,68, o ML pode reclassificar o anúncio de forma abrupta, impactando ranking e elegibilidade de promoções simultaneamente; o ADS não compensa queda de posição em categoria por degradação de `health`.

- **Histórico:** Risco presente desde o primeiro ciclo de memória disponível (22/05), identificado como crônico nas entradas de 22, 23, 24, 25 e 26/05. Oitavo ciclo consecutivo sem movimento.

- **Sinal de confirmação:** `health` do MLB3288536143 caindo abaixo de 0,68 em qualquer ciclo (gatilho L02 documentado na memória) **ou** ACOS da conta acima de 12% por dois ciclos consecutivos — o segundo indicando que o ADS está precisando compensar queda de alcance orgânico maior do que a série recente sugere.

---

### Sinais a observar

1. **MLB6437847224 (Kit 6 Potes Vidro Hermético, Catálogo Full) — ruptura iminente:** Com `available_quantity=7` e 3 pedidos no dia, cobertura está em ~2,3 dias. Se o próximo pacote mostrar `available_quantity < 3` ou `status=paused`, confirma ruptura ativa em anúncio Catálogo (`is_catalog=true`) — perda de Buy Box com recuperação lenta e impacto direto em `cancellations_rate` e na janela de MercadoLíder Platinum.

2. **MercadoLíder Platinum — ritmo nos próximos 5 dias:** Se `gap_revenue_brl` cair abaixo de R$10.000 até 2026-06-04 ao ritmo atual, a promoção está confirmada dentro da janela. Se o gap parar de fechar por dois dias consecutivos (GMV diário abaixo de R$3.500), identifica evento adverso — cancelamentos automáticos ou ruptura de Full — consumindo a janela.

3. **ADS share e ACOS na série — terceiro ciclo acima do baseline:** ACOS em 8,23% é o terceiro ponto acima do baseline histórico de 4,4%. Se o próximo ciclo fechar com ACOS > 10% **e** ADS share > 60%, confirma que o ADS está em modo de substituição (cobrindo déficit orgânico), não de amplificação — gatilho para alinhamento Yasmin–Himmel sobre mix de campanhas e cobertura por `platform_item_id`.