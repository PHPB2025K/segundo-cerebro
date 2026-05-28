<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Cinco blocos diários disponíveis na weekly.md (22–26/05), todas as janelas temporais (7d, 30d, 60d, mesmos dias da semana) com coverage 100%. Pacote ml_snapshot completo: reputação, MercadoLíder, mix de modalidade de envio (7d/30d/top10), top_items_details, ads_summary, account_overview. Limitações remanescentes: health calculado em apenas 3 dos 8 itens do top10 (outros `null`), 67 de 86 anúncios ativos sem health, ausência de breakdown ADS por platform_item_id (pendência documentada desde 22/05). `data_readiness=DADOS_PARCIAIS` reflete Shopee, não ML — reconciliação ML `ok`, sem impacto na leitura desta conta. Base entre as mais robustas dos últimos ciclos para formação de tese.

---

### Leitura temporal

- **Sinal consistente de alta em todas as janelas, sem contraindício temporal:** GMV R$7.150,57 supera avg_7d (`R$5.494,99`, +30,1%), avg_30d (`R$4.847,01`, +47,5%) e avg_60d (`R$4.258,18`, +67,9%). O ponto central é que o próprio avg_7d já estava 13% acima do avg_30d antes deste ciclo — o dia de hoje reforça uma trajetória que estava em formação, não inaugura um pico isolado.

- **Controle de sazonalidade confirma rompimento real:** 133 pedidos vs `same_weekday_avg.avg_orders=94,25` (+41,1%). GMV de hoje (R$7.150,57) supera as quatro últimas quartas-feiras, inclusive a melhor referência recente (29/04: R$5.618,66), e o faz com ticket R$53,76 — 21% acima do ticket médio histórico de quartas (~R$44,29). O rompimento não é de volume puro; é volume e ticket crescendo juntos (`ticket_vs_30d_pct=+16,0%`, `ticket_vs_60d_pct=+24,6%`), o que reforça que o mix de produto vendido está se deslocando para itens de maior valor médio.

- **Hipóteses anteriores — balanço:** (a) *Health degradado de MLB3288536143 (0,71) e MLB4073003575 (0,75)*: 8º ciclo idêntico sem worsening e sem reversão — hipótese de erosão orgânica progressiva sustentada, direção ainda indecidível pela série interna do ML. (b) *MLB4676726433 (Kit 10 Potes 1050ml) em ruptura/cancelamento automático* (gatilho 25/05): anúncio reapareceu ativo com `available_quantity=4` e 5 pedidos hoje — reativação confirmada, ruptura iminente no próximo ciclo. (c) *Kit 6 Canecas Tulipa MLB6167272090 com 2 unidades no ciclo 26/05*: snapshot atual mostra `available_quantity=16`, sinal de reposição, mas cobertura ainda apertada (6 pedidos hoje ≈ 2,7 dias). (d) *Kit 6 Canecas Lisas MLB6232315532 em zona crítica com ~31 unidades no ciclo 26/05*: `available_quantity=84` hoje — reposição chegou, risco de Buy Box imediato resolvido.

- **Mercado Ads: série de ACOS em tensão:** Baseline 22–23/05 em ~4,4%; ciclos 25/05 (14,15%) e 26/05 (10,96%) subiram. Hoje `avg_acos_pct=44,85%` reportado diverge do ACOS calculado total (R$463,31 / R$4.811,50 = 9,63%) — a métrica reportada é média simples por campanha, não ponderada por gasto; indica mix heterogêneo de campanhas com algumas em ineficiência alta. Tendência de ACOS médio de campanhas elevado está ativa, mas eficiência total do portfolio permanece forte (ROAS 10,38x).

---

### Leitura estratégica

- **Ganho de patamar real carregado por ADS dominante, não por orgânico em expansão:** ADS share = R$4.811,50 / R$7.150,57 = **67,3%** — território ADS dominante, acima de 65% hoje e em 22/05 (69,9%), com os dias intermediários oscilando entre 49,5% e 60,7%. O padrão é de ADS acima de 50% em todos os ciclos disponíveis. O patamar de GMV cresceu, mas o orgânico não avançou proporcionalmente: os dois vetores orgânicos principais (MLB3288536143 e MLB4073003575) têm `health` em nível regular (0,71 e 0,75) há 8 ciclos sem reversão — ML continua comprimindo seu ranking de categoria silenciosamente. O volume que esses anúncios entregam é sustentado por exposição paga, não por posição orgânica crescendo. ROAS 10,38x confirma eficiência pontual; ADS share acima de 65% confirma dependência estrutural.

- **Concentração estrutural no cluster IMB501 com health em degradação crônica — padrão histórico, não novo risco:** MLB3288536143 (todas as variações Tampa Preta/Cinza/Vermelha) somou 64 pedidos de 133 hoje = **48,1% do dia**. Série recente: 44% (22/05), 44% (23/05), 47,5% (24/05), 56,5% (25/05), 44,8% (26/05) — oscila entre 44% e 56%, sem sinal de segundo vetor absorvendo participação. `health=0,71` neste anúncio está a 0,01 do limiar de nível preocupante (< 0,70); `top3_concentration=49,6%` e `top5_concentration=66,2%` confirmam que a cauda existe mas não carrega. Dependência é crônica, não nova — sua relevância hoje é que ela amplifica o impacto de qualquer deterioração dos campeões.

- **Mix de modalidade de envio: campeões 100% Full ontem, base ativa 40,7% Full — assimetria que concentra exposição a rupturas no topo:** `fulfillment_mix_yesterday_top10.full_pct=100%` vs `account_overview.active_analysis.fulfillment_mix.full_pct=40,7%` (7d: 78,9%, 30d: 76,0%). Os anúncios que geram o faturamento vivem em Full; o restante da base opera predominantemente em Cross-Docking (59,3%). Essa assimetria é estrutural e se mantém estável nas últimas semanas. O corolário direto: MLB4676726433 (Kit 10 Potes 1050ml, Full, `available_quantity=4`, Frete Grátis ativo) com 5 pedidos hoje está em ruptura iminente — e a modalidade Full implica que quando o estoque no CD do ML zerar, o anúncio sai do ar sem aviso prévio controlado pela Budamix.

- **MercadoLíder Platinum: janela de promoção se comprime com aceleração de GMV — mas cancellations_rate é o freio real:** `progress_pct=86,91%`, `gap_revenue_brl=R$38.759,96`, `eta_dias_estimado=9 dias` ao ritmo de R$4.287,33/dia. O GMV de hoje (R$7.150,57) é 66,7% acima do ritmo diário — este ciclo comprime o ETA. Com gap abaixo de R$40k, a trajetória Platinum é factível em horizonte de 9–12 dias mantendo o pace. O bloqueio não é de faturamento; é de qualidade: `cancellations_rate=0` hoje, mas MLB4676726433 em ruptura iminente via Full é o mecanismo mais direto para gerar cancelamentos automáticos que alimentam a métrica oficial. Threshold Platinum para cancelamentos: < 2% (atual: 0%). Qualquer aumento em `cancellations_rate` não é apenas operacional — é risco de elegibilidade direta ao próximo nível.

---

### Tese da conta

A conta Mercado Livre está **em ganho de patamar**. O sinal é consistente em todas as janelas (7d, 30d, 60d, controle de dia da semana) e o próprio avg_7d já estava acima do avg_30d antes deste ciclo — hoje é reforço de tendência, não pico isolado. A ressalva estratégica central é que o patamar em alta é **estruturalmente dependente de Mercado Ads** (ADS share acima de 50% em todos os ciclos recentes, 67,3% hoje): o orgânico não está em expansão proporcional ao crescimento de GMV, os dois vetores principais têm health em nível regular há 8 ciclos sem reversão, e a concentração no cluster IMB501 (~48% do dia) é crônica. **O faturamento cresceu; a base orgânica que o sustentaria sem ADS não acompanhou.**

---

### Risco estrutural principal

**Risco:** ADS dominante como sustentação do patamar de GMV, com orgânico estruturalmente estagnado nos anúncios campeões.

**Por que importa:** Com ADS share acima de 60% como padrão recente, qualquer interrupção ou redistribuição de campanha por Himmel derruba o patamar imediatamente, sem mecanismo orgânico de amortecimento. O problema se aprofunda porque os dois campeões orgânicos (MLB3288536143, `health=0,71`; MLB4073003575, `health=0,75`) estão em nível regular há 8 ciclos — ML comprime progressivamente o ranking de categoria desses anúncios, e o ADS não resolve a degradação de health, apenas mascara seus efeitos no faturamento. Se `health` de MLB3288536143 cair para nível preocupante (< 0,70), a lacuna orgânica que ADS precisa cobrir aumenta, elevando custo de dependência e fragilizando o patamar de forma não linear.

**Histórico:** Risco documentado desde 22/05 (primeiro ciclo com ADS share acima de 65% e health estagnado em dois anúncios). Todos os ciclos subsequentes confirmam a dependência sem reversão do orgânico — não é hipótese nova, é padrão estabelecido de 6 ciclos.

**Sinal de confirmação:** `health` de MLB3288536143 caindo para 0,68 ou abaixo em qualquer dos próximos 5 ciclos, **combinado** com ADS share acima de 65% pelo terceiro ciclo consecutivo em semana regular, confirmaria o risco como maduro e acionável (gatilho de alinhamento Yasmin–Himmel documentado desde memória 22/05).

---

### Sinais a observar

1. **MLB4676726433 (Kit 10 Potes 1050ml) em ruptura ou gerando cancelamentos no próximo ciclo:** `available_quantity=4` com 5 pedidos hoje — se o próximo pacote mostrar anúncio pausado ou `cancellations_rate > 0` na reputação oficial, confirma o padrão de ruptura em Full com cancelamento automático que já ocorreu em 25/05. Janela: próximo ciclo diário. Impacto direto em `cancellations_rate` da janela Platinum, que hoje está em 0% com threshold de 0,5% para elegibilidade.

2. **ADS share acima de 65% por 2 ciclos consecutivos na próxima semana confirma dependência estrutural consolidada:** Hoje (67,3%) e 22/05 (69,9%) são os dois pontos acima do limiar; se amanhã ou depois fechar acima de 65%, configura o terceiro ponto da série de dominância — gatilho de alinhamento Yasmin–Himmel documentado na memória de 22/05. Qualquer ciclo abaixo de 50% de ADS share nos próximos 5 dias, por outro lado, sugere expansão orgânica e enfraquece a tese de dependência estrutural. Janela: próximos 3 ciclos diários.

3. **GMV abaixo de R$5.000 por 2 dias consecutivos nos próximos 7 dias reclassificaria hoje como spike, não patamar:** O avg_7d de R$5.494,99 precisa se sustentar para confirmar mudança de nível. Dois dias consecutivos abaixo de R$5.000 indicariam que o movimento recente é pico pontual — especialmente relevante porque hoje o dia foi carregado por ADS em dia de alta eficiência, e o componente orgânico subjacente pode ser menor. Janela: próximos 7 dias, com piso de R$5.000 como linha de corte.