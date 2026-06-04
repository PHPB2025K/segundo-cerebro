<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória acumulada robusta: 10+ ciclos diários disponíveis na weekly.md (22/05 a 02/06), com hipóteses ativas documentadas e rastreáveis. Reputação, mix de modalidade de envio e MercadoLíder presentes no pacote (cobertura 100% em 7d e 30d). Único ponto de atenção: `ads_summary.status: "ok"` com `spend_yesterday_brl: 0,0` e `revenue_ads_yesterday_brl: 0,0` apesar de `campaigns_active_count: 12` — dado declarado como ok, mas resultado zero é tratado como potencial anomalia operacional, não como dado faltante.

---

### Leitura temporal

- **vs 7d (semana imediata):** GMV R$6.401 está -20,1% vs avg_7d (R$8.010) e pedidos -14,1% — a base de 7d inclui o pico de R$9.210 (02/06) e R$9.953 (01/06), o que infla a comparação. A queda vs 7d é acomodação pós-picos, não reversão de tendência.

- **vs 30d e 60d:** GMV +5,9% vs avg_30d (R$6.044) e +34,1% vs avg_60d (R$4.775); pedidos +15,4% e +31,1% respectivamente. Ambas as janelas longas apontam na mesma direção: patamar atual está estruturalmente acima do bimestre anterior. Ticket R$45,08 está -8,3% vs 30d (R$49,14) e +2,2% vs 60d (R$44,10) — compressão explicada por composição do cluster IMB501 de menor valor unitário dominando o dia, não deterioração de mix estrutural.

- **Mesmo dia da semana (quartas-feiras):** 87 (06/05) → 65 (13/05) → 91 (20/05) → 133 (27/05) → 142 (03/06). Crescimento monotônico nas comparações homólogas; dia de hoje +51,1% vs a média dos quatro pares históricos (`same_weekday_avg.avg_orders=94,0`). Sem nenhum sinal de reversão nessa janela.

- **Hipóteses anteriores:** MLB3288536143 (IMB501P Full) — reposição confirmada, qty=174 hoje contra ~13 em 01/06; risco imediato de ruptura atenuado, mas nível preocupante de qualidade (0,71) persiste. MLB6167272090 (Tulipa) — retornou ativa com qty=27 e 3 pedidos, padrão de ruptura/reposição resolvido temporariamente. MLB4073003575 (Kit 4 Potes 1050ml, qty=2 em 02/06) — ausente do top 10 hoje, reposição não confirmada; ausência no ranking sugere ruptura ou queda de visibilidade.

---

### Leitura estratégica

- **Orgânico revelou piso real sem suporte de ADS:** `ads_summary.spend_yesterday_brl=0,0` com `campaigns_active_count=12` é o dado mais estrategicamente relevante do pacote. A conta gerou R$6.401 com ADS share de 0% — contra a série histórica de 48-55% dos dois ciclos anteriores (R$5.059 em 02/06, R$4.578 em 01/06). O resultado coloca o piso orgânico em R$6.401: +5,9% vs 30d, +34,1% vs 60d, +51,1% vs média das quartas. Hipótese: o orgânico tem consistência estrutural própria; ADS amplifica mas não sustenta sozinho. A diferença entre hoje sem ADS (R$6.401) e os dias com ADS ativo (R$8-9k) estima o incremento de mídia em R$1.600-2.600/dia — relevante para leitura da amplitude, não para a base.

- **Patamar de 60d rompido e sustentado ao longo de semanas:** O GMV de hoje representa +34% vs avg_60d, e as comparações homólogas semanais mostram crescimento consistente sem interrupção (87→65→91→133→142 pedidos nas quartas). Não é pico isolado — é mudança de patamar operacional que se confirma em duas janelas longas simultaneamente. A queda vs 7d é barulho de base alta pós-picos.

- **MercadoLíder Platinum na faixa de decisão:** `gap_revenue_brl=R$7.854,71`, `progress_pct=97,35%`, `eta_dias_estimado=1,6 dias` ao ritmo de R$4.802/dia. O dia de hoje (R$6.401) operou acima do ritmo mínimo necessário (R$7.854 ÷ 1,6 ≈ R$4.909). A janela rolling de 60 dias descarta os dias fracos de início de abril enquanto absorve o volume acumulado de junho — promoção está no próximo ciclo ou dois. O risco não é o volume: é o `cancellations_rate`. Hoje zerado (`cancellations_rate=0`), mas a série recente de cancelamentos (3→3→2→6→9→4 nos últimos ciclos) e ratings_negative em 0,41 (terceiro ponto consecutivo acima de 0,39) são vetores latentes que, se se materializarem em taxa oficial, podem comprometer a elegibilidade técnica mesmo com faturamento acima do threshold.

- **Dependência crônica de 2-3 anúncios sem cauda emergente:** `top3_concentration=60,6%`, cluster IMB501 responde por 60,6% do dia (86 pedidos). Com 181 pausados vs 77 ativos (proporção 2,35:1), a cauda está morta — padrão crônico, registrado desde o primeiro ciclo disponível (22/05) sem movimento de segundo vetor aparecendo. A base ativa opera 61% Cross-Docking (`account_overview.active_analysis.fulfillment_mix.cross_docking_pct=61,0`), mas os campeões vivem em Full (top10 yesterday 59,7% Full) — assimetria estrutural que amplifica o impacto de qualquer ruptura no topo.

---

### Tese da conta

**Vulnerável.** A conta está em ganho real de patamar — GMV +34% vs 60d, crescimento monotônico nas comparações homólogas, MercadoLíder Platinum a 1-2 dias, e orgânico revelou hoje consistência estrutural sem ADS. Mas a arquitetura que sustenta esse ganho é frágil: resultado concentrado em 2-3 anúncios em Full com nível de qualidade em zona preocupante há 11+ ciclos (MLB3288536143 em 0,71), único anúncio em Catálogo com cobertura de ~2-3 dias (MLB6232315532, qty=22), e cauda morta sem segundo vetor emergente depois de 10+ ciclos monitorados. O ganho de patamar é consistente e factual; a estrutura que o carrega não tem redundância.

---

### Risco estrutural principal

**Risco:** Concentração crônica no cluster IMB501 (MLB3288536143, Full, `health=0,71`) com nível de qualidade do anúncio em zona preocupante há 11+ ciclos, sem segundo vetor ativo na cauda.

**Por que importa:** MLB3288536143 respondeu por 56 pedidos hoje = 39,4% do GMV total do dia. O nível de qualidade do anúncio em 0,71 (nível preocupante) indica que o ML já penaliza exposição orgânica progressivamente. Se o nível cair abaixo de 0,70, o anúncio entra em Básico ML — perda de exposição em ranking de categoria que afeta diretamente o principal vetor de pedidos. Com cauda morta (181 pausados), não há anúncio secundário capaz de absorver a queda. A reposição de estoque (qty=174 hoje) resolve o risco imediato de ruptura, mas não o risco de exposição — são vetores independentes.

**Histórico:** presente como risco registrado desde 22/05 (memória semanal), sem resolução em nenhum dos 11 ciclos. Nível 0,71 estável há múltiplos ciclos; direção interna não observável pelo pacote.

**Sinal de confirmação:** `health` do MLB3288536143 cair abaixo de 0,68 em qualquer snapshot confirma erosão ativa e desbloqueia necessidade de alinhamento Yasmin–Himmel sobre drivers (claims, atrasos, listing) e plano de recuperação. Paralelo: MLB6232315532 (único Catálogo ativo no top 10) com `available_quantity ≤ 5` ou `status=paused` nos próximos 2 dias confirma ruptura de Buy Box — recuperação em Catálogo é mais lenta que em Clássico.

---

### Sinais a observar

1. **ADS spend retornando nos próximos 2 ciclos:** Se `ads_summary.spend_yesterday_brl` retornar a níveis históricos (R$300-500) e GMV cruzar R$8.000, confirma que o orgânico é estrutural e ADS é amplificador — base saudável sustenta crescimento independente de mídia. Se ADS seguir em zero por mais 1 ciclo com GMV abaixo de R$6.000, hipótese passa a ser que parte do "orgânico" de hoje beneficiou-se de tráfego residual ou attribution lag.

2. **MLB6232315532 (Kit 6 Canecas Lisas — Catálogo Full) com `available_quantity ≤ 5` nos próximos 2 dias:** cobertura atual de ~2,4 dias ao ritmo de hoje (22 unidades / 9 pedidos). Ruptura neste anúncio derruba Buy Box no único vetor Catálogo da conta — recuperação de posição em Catálogo é estruturalmente mais lenta que em Clássico. Sinal diretamente ligado ao risco principal e ao ETA Platinum.

3. **`power_seller_status` mudando para `platinum` no próximo snapshot (se reputação disponível):** com gap R$7.854 e ritmo R$4.802/dia, ETA é 1,6 dias. Sinal positivo de confirmação: `power_seller_status=platinum` no próximo pacote. Sinal de risco: `cancellations_rate` saindo de zero no próximo snapshot — dado que a série recente de cancelamentos (incluindo os 4 de hoje) ainda não está na métrica oficial da janela longa, qualquer elevação nos próximos 1-3 ciclos pode comprometer a elegibilidade técnica no momento exato da promoção.