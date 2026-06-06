<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base robusta: weekly.md com 9 entradas consecutivas desde 22/05 (ciclo mais longo observado), hipóteses ativas com múltiplos pontos de confirmação, ml_snapshot completo com reputação, fulfillment mix, ads_summary e mercadolider. monthly.md ainda sem consolidação (template vazio — sem âncora mensal formal). Ressalva pontual: available_quantity não está desagregado por variação em anúncios multi-variação, pendência estrutural recorrente que limita leitura de cobertura granular no cluster IMB501.

---

### Leitura temporal

- **Patamar:** GMV de ontem (R$ 7.742, `metrics.gmv`) está -2,3% vs 7d (`changes.gmv_vs_7d_pct`) mas +37% vs 30d e +57,9% vs 60d (`changes.gmv_vs_60d_pct`). O recuo leve vs 7d é acomodação intra-semana dentro de banda elevada — não deterioração. Vs mesmo dia da semana (avg R$ 5.353, `same_weekday_avg.avg_gmv`), o dia fica +44,6%: a conta opera sistematicamente acima do padrão histórico desta sexta-feira.

- **Trajetória de 60 dias:** `mercadolider.ritmo_diario_brl = R$ 4.934/dia` sobre a janela 60d confirma que a conta elevou seu piso operacional de forma consistente — não é pico isolado. O delta 30d vs 60d (+37% GMV em 30d, +57,9% em 60d) mostra que a aceleração começou antes e manteve; não há inversão nem acomodação nesta comparação.

- **MercadoLíder Platinum — tese confirmada:** A hipótese central das últimas semanas (`gap` caindo de R$ 55.226 em 22/05 para R$ 11.621 em 02/06, R$ 3.810 em 04/06) chega ao ponto definitivo: `mercadolider.platinum.gap_revenue_brl = 0`, `progress_pct = 100%`, `sales_60d_revenue_brl = R$ 296.060` (threshold R$ 296.000), `sales_60d_count_paid = 6.683` (threshold 1.725). O faturamento cruzou o threshold. `power_seller_status` permanece `gold` — promoção formal ainda não registrada pelo ML.

- **Hipóteses anteriores:** Tulipa pausada com cancelamentos prospectivos (hipótese ativa desde 22/05) se confirma no 7º+ ciclo: `MLB6167272090` aparece `status=paused`, `available_quantity=0`, com 11 pedidos no dia = 11 cancelamentos prospectivos garantidos. Nível de qualidade do Conjunto 5 Potes Vidro Tampa Cinza (`MLB3288536143`) em 0,71 pelo ~15º ciclo consecutivo — tendência horizontal sem reversão observada. Kit 4 Potes 640ml (`MLB5402326666`) em `health=0,66` pelo 2º ciclo em nível preocupante, confirmando deterioração.

---

### Leitura estratégica

- **Lente 6 — Platinum cruzado, promoção pendente:** A conta atingiu os dois critérios do MercadoLíder Platinum pela janela 60d rolling (`revenue=R$296.060 vs threshold R$296.000`; `vendas=6.683 vs threshold 1.725`). Métricas de qualidade estão bem abaixo dos limites: `claims_rate=0,0018` (36% do threshold de 0,5%), `cancellations_rate=0` oficial, `delayed_handling_rate=0,0009`. O lag entre threshold cruzado e atualização da medalha é esperado no sistema ML — mas `cancellations_rate` em zero é o vetor de risco imediato: os 11 cancelamentos prospectivos da Tulipa pausada, se entrarem na janela oficial antes do reconhecimento formal, podem criar pressão justamente na transição.

- **Lente 3 — Dependência de modalidade de envio: divergência campeões vs base:** `fulfillment_mix_yesterday_top10.full_pct = 62,9%` vs `fulfillment_mix_30d.full_pct = 81,1%` — os campeões de ontem usaram proporcionalmente menos Full que o padrão de 30 dias. A causa é estrutural: Tampa Vermelha (`MLB4535659243`) e Tampa Preta (`MLB4535865317`) operam Cross-Docking e tomaram posições 2 e 3 enquanto a Tulipa (Full, pausada) gerou pedidos que serão cancelados. A base ativa da conta (`account_overview.active_analysis.fulfillment_mix.full_pct = 41%`) é muito mais Cross-Docking que o top 10 — campeões continuam sendo exceção Full dentro de uma base majoritariamente Coleta. O líder de volume em Full (`MLB3288536143`, `available_quantity=58` pós-42 pedidos = cobertura ~1,4 dias) é o ponto mais frágil desta assimetria.

- **Lente 4 — Catálogo recuperado, Clássico com saúde degradada:** Kit 6 Canecas Lisas 200ml (`MLB6232315532`, único `is_catalog=true` + `listing_type=gold_pro` do top 10) mostrou `available_quantity=30` após 13 pedidos — recuperou do piso de 11 unidades registrado em 04/06, confirmando restock entre 04/06 e 05/06. Cobertura atual ~2,3 dias ao ritmo de hoje. Os dois anúncios Clássico com nível de qualidade calculável no top 10 mostram: `MLB3288536143` em nível preocupante (0,71, ~15 ciclos) e `MLB5402326666` em nível preocupante (0,66, 2º ciclo). Anúncios Clássico com health degradada perdem posição em ranking de categoria progressivamente — o ganho de exposição orgânica nesses anúncios está sendo erodido sem visibilidade de reversal.

- **Lente 5 — ADS share dominante, eficiência alta mas estrutura dependente:** ADS gerou R$ 4.268 com gasto de R$ 304 (`ads_summary`) — ROAS 14,03x, ACOS 7,27%, **ADS share = 55,1%** do GMV (`4.268/7.742`). Zona de ADS dominante pelo 5º+ ciclo consecutivo (série 48–57% desde 22/05). Eficiência excelente não neutraliza a fragilidade estrutural: qualquer pausa de campanha por Himmel retira mais da metade do faturamento. O orgânico existe mas não sustentaria o patamar atual de forma independente com base nos dados disponíveis.

---

### Tese da conta

**Vulnerável.** A conta opera no patamar mais alto de sua história observada (+57,9% vs 60d), cruzou o threshold financeiro do MercadoLíder Platinum e ADS roda com eficiência excepcional (ROAS 14x). Mas a estrutura tem três fragilidades simultâneas e persistentes que impedem qualificação como saudável: o líder de volume absoluto (`MLB3288536143`, Full, 25,6% dos pedidos) está em nível de qualidade preocupante há ~15 ciclos com estoque de ~1,4 dias; o segundo vetor em canecas (Tulipa) opera em ruptura recorrente gerando cancelamentos prospectivos no momento exato em que a conta aguarda reconhecimento formal do Platinum; e o resultado depende de ADS acima de 50% do GMV sem evidência de que o orgânico sustenta o patamar de forma autônoma. O número é forte, a fundação é frágil.

---

### Risco estrutural principal

**Risco:** Ruptura iminente do anúncio `MLB3288536143` (Conjunto 5 Potes Vidro Tampa Cinza, Full) combinada com acumulação silenciosa de cancelamentos automáticos no momento de transição para Platinum.

**Por que importa:** `MLB3288536143` é o maior gerador unitário de pedidos da conta (42/164 = 25,6% do dia, ~15 ciclos consecutivos como líder). Opera via modalidade Full — ruptura não é reativada em horas; reposição ao CD do ML tem lead time de dias. Com `available_quantity=58` pós-42 pedidos, a cobertura prospectiva é de ~1,4 dias ao ritmo de hoje. Simultaneamente, os 11 pedidos da Tulipa pausada (`MLB6167272090`, `status=paused`, `available_quantity=0`) são cancelamentos prospectivos garantidos, somados a padrões recorrentes anteriores (7º+ ciclo). A combinação de ruptura do líder Full + cancelamentos acumulados de Tulipa tem o potencial de mover `cancellations_rate` de zero para positivo exatamente quando o ML processa a elegibilidade Platinum — janela de maior risco operacional que a conta já enfrentou.

**Histórico:** Não é novo. A cobertura crítica do `MLB3288536143` foi sinalizada em 01/06 (`available_quantity=13`), com reposição chegando entre ciclos. A Tulipa em ruptura recorrente está documentada desde o ciclo 22/05. O que é novo é a coincidência temporal com o threshold Platinum cruzado: o risco de cancelamentos entrar na janela oficial existe há semanas, mas o timing agora é o pior possível.

**Sinal de confirmação:** `cancellations_rate` da reputação (`ml_snapshot.reputation.cancellations_rate`) sair de zero em qualquer snapshot das próximas 72h confirma que a série acumulada de cancelamentos automáticos entrou na janela oficial ML e se torna vetor ativo contra o reconhecimento formal da medalha.

---

### Sinais a observar

1. **`available_quantity` do `MLB3288536143` (Conjunto 5 Potes Vidro Tampa Cinza, Full) abaixo de 20 unidades no próximo snapshot** confirma ruptura iminente no maior vetor de volume da conta e aciona verificação urgente de ETA de reposição ao CD do ML com Yasmin.

2. **`cancellations_rate` (`ml_snapshot.reputation.cancellations_rate`) sair de zero nos próximos 1–3 snapshots** confirma que os cancelamentos automáticos acumulados (Tulipa + eventuais outros) entraram na janela oficial ML — risco direto à elegibilidade Platinum formal independente do faturamento já cruzado.

3. **`power_seller_status` permanecer `gold` por mais 2 ciclos com `gap_revenue_brl=0` e `progress_pct=100%`** indica lag maior que o esperado no sistema ML ou barreira não visível no pacote — acionar verificação direta no painel ML via Yasmin para confirmar se há algum critério qualitativo bloqueando a promoção formal.