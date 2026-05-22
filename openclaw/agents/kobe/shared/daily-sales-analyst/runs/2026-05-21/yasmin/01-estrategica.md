<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` são templates vazios sem entradas reais — memória interpretativa nascente, sem hipóteses ativas para confirmar ou refutar. Os dados ML do pacote, no entanto, são robustos: reputação, mix de modalidade de envio (7d/30d/top10), MercadoLíder, ADS e top_items_details disponíveis com coverage 100%. A leitura factual é sólida; a leitura de trajetória histórica interpretativa é ponto de partida, não continuação de tese.

---

### Leitura temporal

- **Patamar em expansão clara nas janelas longas:** GMV hoje R$6.113,02 está +38,7% acima da `avg_30d` (R$4.406,82) e +57,3% acima da `avg_60d` (R$3.886,46). Pedidos (101) estão na média 30d (99,3) e praticamente empatados com o controle de mesmo dia da semana (102,75 pedidos, -1,7%). A discrepância entre ganho de GMV e estabilidade de pedidos é inteiramente explicada por ticket: R$60,52 hoje vs R$44,36 média 30d (`ticket_vs_30d_pct=+36,4%`) e R$42,05 média 60d (`ticket_vs_60d_pct=+43,9%`). A conta cresceu de patamar de faturamento sem crescer em alcance.

- **Controle de sazonalidade confirma o ganho:** GMV hoje +30,5% acima da `same_weekday_avg` (R$4.685,96). As últimas 4 quintas têm alta dispersão — R$3.176 (07/05) a R$6.540 (14/05) — mas hoje está no terço superior da faixa, não é ponto fora da curva positiva isolada. O padrão de quinta tem instabilidade intrínseca; a posição de hoje é consistente com o topo da banda.

- **vs 7d — inversão de mix:** Os últimos 7 dias tiveram média de 118,9 pedidos e ticket de R$47,25 — volume maior, ticket menor. O dia de hoje inverte: menos pedidos que o recente imediato (101 vs 118,9, `orders_vs_7d_pct=-15,1%`) mas GMV superior (+8,8%). O ritmo recente de 7d era de volume; hoje o driver foi mix de produto de maior valor unitário.

- **Sem hipóteses anteriores registradas:** `weekly.md` e `monthly.md` sem entradas. Toda leitura abaixo é tese inaugural, não confirmação.

---

### Leitura estratégica

- **Lente 1 + Lente 3 — Ticket é o motor, não volume:** A expansão de 36–44% de ticket nas janelas 30d e 60d indica deslocamento estrutural de mix — a conta passou a vender proporcionalmente mais unidades de maior valor (Kit 10 Potes 1050ml a ticket alto, potes em kit maior) sem aumentar alcance em pedidos. Isso é saudável se sustentado por demanda orgânica e diversificação de catálogo, mas preocupante se o deslocamento veio de ADS direcionando tráfego para SKUs específicos sem base orgânica. A concentração top 3 = 59,4% e top 5 = 76,2%, com a família IMB501 (Potes Vidro Redondos, variações Preta + Cinza + Vermelha) somando ~52% dos pedidos do dia por si só, indica que a cauda não está se formando — o crescimento de GMV é concentrado.

- **Lente 5 — ADS dominante com ROAS elevado:** ADS share calculado em **75,1%** (`revenue_ads_yesterday_brl=R$4.593,66` / `gmv=R$6.113,02`) com ROAS de **13,4x** (`4.593,66 / 341,72`) e ACOS de **4,71%** — campanha Himmel extremamente eficiente, mas a conta opera em zona de dependência severa de mídia paga. O orgânico residual estimado é ~R$1.519/dia. A eficiência do ADS pode mascarar a ausência de base orgânica: ROAS alto e ACOS baixo não são sinônimo de canal saudável estruturalmente quando o share ultrapassa 70%.

- **Lente 3 — Divergência de modalidade de envio e alertas de estoque críticos:** O mix de modalidade de envio do top 10 do dia (`fulfillment_mix_yesterday_top10`: Full 19,8%, Cross-Docking 80,2%) é o inverso do padrão 7d (Full 77%, Cross-Docking 23%) e 30d (Full 73,6%, Cross-Docking 26,4%). Hoje foram os anúncios em Cross-Docking — a família IMB501 — que dominaram, não os Full. Os Full que apareceram no top 10 apresentam alertas de estoque: **Kit 06 Canequinhas Acrílico (MLB4410218897)** com `available_quantity=1` e 3 pedidos no dia — ruptura praticamente consumada, com pedidos prospectivos em risco de cancelamento — e **Kit 6 Canecas Tulipa (MLB6167272090)** com `available_quantity=14` e 5 pedidos, ritmo que esgota o estoque em 2-3 dias. O **Kit 4 Potes 1050ml (MLB4073003575)** opera em Full com `health=0,75` — penalização ML ativa, reduzindo exposição orgânica progressivamente apesar de `available_quantity=160`.

- **Lente 6 — MercadoLíder Platinum em aproximação acelerada:** Conta em MercadoLíder Gold (`power_seller_status=gold`, `color=5_green`), `progress_pct=80,04%` para Platinum, gap de R$59.091 com ETA de 15 dias mantendo ritmo atual de R$3.948/dia. Hoje (R$6.113) está 55% acima do ritmo necessário — dia que comprime ativamente o gap. Porém, o dado de `ratings_negative=0,39` (39% de avaliações negativas) é assimétrico com a saúde operacional declarada: claims 0,25%, cancellations 0%, delayed_handling 0,1% estão dentro dos thresholds. Avaliações negativas elevadas não derrubam a medalha diretamente, mas impactam conversão e posicionamento de anúncio no médio prazo de forma silenciosa.

---

### Tese da conta

**Vulnerável.** A conta está em trajetória consistente de ganho de GMV — patamar expandido +57% vs 60d, ticket em escalada estrutural de +44% — mas o resultado é sustentado por estrutura frágil em dois eixos: (1) dependência severa de Mercado Ads, com ADS share de 75,1% do GMV do dia e orgânico residual estimado em ~R$1.500/dia, e (2) concentração extrema em família IMB501 com cauda morta expressiva (173 anúncios pausados vs 84 ativos). O crescimento de patamar é factual e consistente em mais de uma janela; a fragilidade estrutural também. Saudável no número, vulnerável na arquitetura.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads como vetor primário de faturamento — ADS share de 75,1% do GMV (`revenue_ads_yesterday_brl=R$4.593,66` / `gmv=R$6.113,02`), com orgânico residual estimado em ~R$1.519/dia.

**Por que importa:** Uma conta com 75% do GMV atribuído a mídia paga não tem base orgânica resiliente. Qualquer interrupção de campanhas — revisão de verba, mudança de algoritmo ML Ads, pausa técnica — derruba o faturamento em proporção imediata. O ROAS de 13,4x e ACOS de 4,71% são números de campanha excelentes, mas eficiência de ADS e resiliência orgânica são dois eixos independentes. A conta hoje cresce de GMV sem crescer organicamente em alcance.

**Histórico:** Sem weekly.md ou monthly.md preenchidos — não é possível confirmar se a dependência é crônica ou recente. Primeira observação registrada.

**Sinal de confirmação:** Se nos próximos 5 dias úteis o ADS share se mantiver consistentemente ≥60% do GMV enquanto o GMV permanece acima de R$5.000, a dependência é estrutural e não eventual. Se o ADS share cair abaixo de 50% sem queda proporcional de GMV, haveria sinal de orgânico se fortalecendo — cenário positivo.

---

### Sinais a observar

1. **Ruptura iminente do Kit 06 Canequinhas Acrílico (MLB4410218897):** `available_quantity=1` com 3 pedidos no dia. Se o anúncio for pausado por ruptura nos próximos 1-2 dias, os pedidos já registrados tornam-se cancelamentos prospectivos — impactando `reputation.cancellations_rate` na janela oficial ML nos ciclos seguintes. Sinal confirmado se o anúncio aparecer com status `paused` ou `closed` no próximo pacote com cancelamentos correspondentes.

2. **Trajetória MercadoLíder Platinum:** Progress 80,04%, ETA 15 dias no ritmo atual de R$3.948/dia. Se o GMV diário cair abaixo de R$3.500 por 3 dias consecutivos nas próximas 2 semanas, o ETA sobe acima de 20 dias e a promoção atrasa materialmente. Dias acima de R$5.000 (como hoje) comprimem o gap ativamente. Sinal de alerta: 3 dias seguidos abaixo de R$3.500.

3. **Avaliações negativas (39% ratings negativas, `reputation.ratings_negative=0,39`):** Índice assimétrico com as métricas operacionais do termômetro (todas dentro do limite). Se a proporção se mantiver ≥35% nas próximas leituras com dado disponível no pacote, há risco silencioso de erosão de conversão e posicionamento em categoria — que não aparece no termômetro verde de forma imediata, mas afeta ranking de Clássico (`gold_special`) ao longo do tempo. Sinal: proporção persistindo ≥35% por 2 ciclos semanais com dado confirmado.