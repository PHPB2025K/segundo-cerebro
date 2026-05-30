<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

`weekly.md` cobre 5 ciclos consecutivos (22–26/05) com hipóteses ativas documentadas; `daily/` tem gap de 27/05 e 28/05 ausentes do rolling antes desta leitura. `monthly.md` é template vazio — sem tese mensal de referência. Todos os blocos `ml_snapshot` retornaram `status: ok`; janelas 7d (7 dias), 30d (30 dias) e 60d (59 dias) populadas. Base robusta para patamar e modalidade de envio; ausência dos dois diários recentes limita comparação intra-semana para 27 e 28/05.

---

### Leitura temporal

- **vs 60d e 30d — rompimento de patamar em múltiplas janelas:** GMV R$7.597 vs média 60d R$4.321 (`gmv_vs_60d_pct=+75.8%`) e vs média 30d R$5.029 (`gmv_vs_30d_pct=+51.1%`). Pedidos 143 vs médias de 102.7 e 105.6 respectivamente (`+39.2%` / `+35.4%`). Ticket R$53.13 vs 60d R$42.08 (`+26.3%`) e vs 30d R$47.61 (`+11.6%`). Todas as três dimensões (volume, ticket, GMV) estão acima da banda histórica simultaneamente — configuração que não é acomodação.

- **vs 7d — aceleração, não estabilização:** GMV +24.0% e pedidos +21.9% acima da própria média de 7d (avg_7d: R$6.125 / 117 pedidos). A semana em andamento já estava acima do patamar 30d; hoje está acima da própria semana. Trajetória semanal progressiva: R$4.622 (22/05) → R$5.494 (15/05 — sexta anterior mais forte) → R$7.394 (26/05, último ponto no rolling) → R$7.597 (hoje), com os mesmos seis dias úteis como denominador.

- **vs mesmos dias da semana — dia supera todos os 4 pares anteriores:** `gmv_vs_same_weekday_pct=+49.8%`, `orders_vs_same_weekday_pct=+37.5%`. Máximo anterior entre sextas: R$6.465 em 01/05. O dia não é uma sexta atipicamente fraca que infla a variação — é a sexta mais forte dos últimos 30 dias. Sazonalidade não explica o número; o patamar de base subiu.

- **Hipóteses anteriores:** a tese de ganho de patamar progressivo documentada em weekly (cluster IMB501 crescente, ticket ascendente, MercadoLíder gap reduzindo ciclo a ciclo) se confirma na trajetória. A ruptura da Tulipa (MLB6167272090) era prevista desde 22/05 (sétimo ciclo de monitoramento sem reposição confirmada); hoje se confirma: `status=paused`, `available_quantity=0`, 19 pedidos no dia. Os dois pontos de nível de qualidade em nível regular (MLB3288536143: 0.71, MLB4073003575: 0.75) completam o oitavo ciclo idêntico sem direção observável.

---

### Leitura estratégica

- **Lente 1 — Patamar rompido nas três janelas com suporte em volume e ticket:** a conta não flutua em torno de uma banda — cruzou para um patamar novo. O ganho não é mono-dimensional: volume (+39% pedidos vs 60d) e ticket (+26.3% vs 60d) sobem juntos, o que descarta explicação de mix de ocasião ou dia atípico isolado. A consistência em 7d, 30d, 60d e no controle de dia da semana elimina ruído sazonal como explicação dominante. Ganho de patamar é a leitura correta — não "acomodação em alta".

- **Lente 3 — Assimetria estrutural de modalidade de envio, ampliada:** top 10 do dia operou 100% via modalidade de envio Full (`fulfillment_mix_yesterday_top10.full_pct=100%`) enquanto a base ativa é 61% Cross-Docking (`account_overview.active_analysis.fulfillment_mix.cross_docking_pct=61%`). A janela 7d (Full: 84.4%) é mais concentrada que a 30d (Full: 77.0%) — a tendência de concentração dos campeões em Full se intensifica, não se dilui. Com `paused > active × 2.1` (176 pausados vs 82 ativos), a cauda da conta está operacionalmente morta; o resultado vem de uma fração pequena do portfólio, toda em Full. Qualquer ruptura no CD do ML afeta diretamente o vetor que gerou o rompimento de patamar.

- **Lente 5 — ADS dominante, eficiente, mas sem confirmação de orgânico autônomo:** ADS share calculado: R$4.630 / R$7.597 = **60.9%** — acima de 50%, zona de dependência estrutural. ROAS 12.2x (R$4.630 / R$379), ACOS 5.74% — campanha eficiente, Himmel opera bem. O problema não é ineficiência; é que sem as campanhas, o volume observado não é sustentável no patamar atual. O terceiro+ ponto consecutivo de share acima de 60% (22/05: 69.9%, 25/05: 56.7%, 26/05: 60.7%, hoje: 60.9%) confirma que a dependência não é pontual.

- **Lente 6 — MercadoLíder Platinum iminente, com risco de integridade operacional:** gap R$26.538 (`platinum.gap_revenue_brl`), progresso 91.03% (`platinum.progress_pct`), ETA 5.9 dias ao ritmo atual de R$4.491/dia (`ritmo_diario_brl`). O dia de hoje (R$7.597) está 69% acima do ritmo necessário — cada dia no patamar atual encurta o ETA. A ameaça à promoção não é de volume: é de `cancellations_rate`. Hoje ela é 0 (`reputation.cancellations_rate=0`). Os 19 pedidos sobre MLB6167272090 pausada com estoque zero são cancelamentos prospectivos garantidos que ainda não entraram na métrica oficial. Se entrarem antes da janela 60d fechar o ciclo, podem comprometer a exigência de cancelamentos pelo vendedor ≤ 0.5%.

---

### Tese da conta

A conta está em **ganho de patamar** — rompimento consistente em 7d, 30d, 60d e controle de dia da semana, com base dupla em volume e ticket. Simultaneamente, está **vulnerável**: o ganho repousa inteiramente sobre anúncios em modalidade de envio Full com múltiplos estoques em ruptura confirmada ou iminente (ver risco principal), ADS sustentando 60.9% do GMV, e dois campeões em nível de qualidade de anúncio nível regular por oito ciclos sem movimento (MLB3288536143: health=0.71; MLB4073003575: health=0.75). O Platinum está a ~6 dias — mas a mesma semana que pode consolidar a promoção é a que concentra o maior volume de rupturas operacionais da série recente.

---

### Risco estrutural principal

**Risco:** Cadeia de rupturas simultâneas em anúncios Full no topo do portfólio, com pelo menos um já confirmado e três em janela de 1–2 dias.

- MLB6167272090 (Kit 6 Canecas Porcelana Tulipa 250ml): `status=paused`, `available_quantity=0`, 19 pedidos no dia → 19 cancelamentos prospectivos garantidos.
- MLB4676726433 (Kit 10 Potes 1050ml — 10 un): `available_quantity=9`, 8 pedidos no dia → cobertura ~1,1 dias; ruptura iminente.
- MLB4676751119 (Kit 10 Potes 1050ml — 6 un): `available_quantity=1`, 5 pedidos no dia → ruptura no próximo ciclo.
- MLB6754669844 (Kit 10 Potes 640ml — 6 un): `available_quantity=2`, 3 pedidos no dia → ruptura no próximo ciclo.

**Por que importa:** Em modalidade de envio Full, reposição exige logística ao CD do ML — não é imediata como Cross-Docking. A perda simultânea de 4 anúncios em Full, num momento em que os campeões são 100% Full e a cauda de Cross-Docking está pausada em 176 anúncios, comprime o portfólio operacional ativo para menos ainda. Mais crítico: os 19 cancelamentos da Tulipa entram na `cancellations_rate` oficial, que hoje é 0 — qualquer subida coloca em risco a exigência de qualidade do MercadoLíder Gold (≤ 0.5% cancelamentos pelo vendedor) exatamente na janela de promoção para Platinum.

**Histórico:** Tulipa sinalizada como crítica desde 22/05 (7 ciclos de observação sem reposição confirmada; weekly.md registra progressão de estoque 7→2→0). Os Kit 1050ml com estoque crítico são novos na posição de risco, mas o padrão estrutural de rupturas iminentes em Full é recorrente na conta.

**Sinal de confirmação:** `reputation.cancellations_rate` saindo de 0 nos próximos 3–5 ciclos confirma que os cancelamentos da Tulipa entraram na métrica oficial da API ML e que o risco de elegibilidade de qualidade para MercadoLíder é real.

---

### Sinais a observar

1. **`reputation.cancellations_rate` sair de 0 em qualquer ciclo dos próximos 5 dias** → confirma que os 19 pedidos de MLB6167272090 (Tulipa, paused, available=0) converteram em cancelamentos registrados; se combinado com `ratings_negative` subindo além de 0.41 (`reputation.ratings_negative` atual), muda a tese de vulnerável para risco ativo de comprometimento da elegibilidade de qualidade para MercadoLíder Gold antes do Platinum.

2. **MLB4676726433 (Kit 10 Potes 1050ml — 10 un) com `available_quantity=0` ou `status=paused` no próximo snapshot** → segunda ruptura ativa confirmada em Full com 8 pedidos/dia; se simultânea a MLB4676751119 (1 unidade) e MLB6754669844 (2 unidades), a perda de 4 anúncios Full em simultâneo reduz o volume disponível da faixa de patamar atual e aperta o ETA do Platinum de ~6 para estimativa acima de 10 dias.

3. **GMV abaixo de R$5.500 por 2 dias seguidos nos próximos 7 dias** → reversão do patamar conquistado; em contexto de rupturas Full confirmadas, seria sinal de que a perda de posição dos anúncios pausados/esgotados já contaminou o ranking dos campeões remanescentes — não simples variação de sazonalidade.