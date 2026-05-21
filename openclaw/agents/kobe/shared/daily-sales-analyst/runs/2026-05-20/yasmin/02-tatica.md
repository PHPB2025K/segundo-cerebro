<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Dado que a tese L01 é "vulnerável" por dependência de ADS (59,8% share) sobre base orgânica degradada, a decisão central para os próximos dias é não introduzir variável em sistema que ainda não tem série histórica qualitativa.** A campanha de Himmel opera com ROAS 11,6x e ACOS 4,33% (`ml_snapshot.ads_summary`) — eficiência em nível que torna qualquer ajuste ativo um risco de quebrar o que sustenta o patamar de R$5.000+. Ação correta: registrar os indicadores como ponto zero e observar trajetória por 3-5 dias antes de qualquer movimento.

- **Dado que o risco operacional imediato identificado pela L01 é o estoque crítico em item de cauda ativa (Kit 06 Canequinhas Acrílico com Suporte, `available_quantity = 4`, ~3 pedidos ontem), a decisão é agir hoje neste ponto específico antes que a ruptura gere cancelamentos.** Não é risco macro para o volume da conta, mas ruptura em item ativo gera cancelamentos prospectivos que impactam `reputation.cancellations_rate` — hoje em zero, proteger antes de qualquer deterioração.

- **Dado que a L01 identificou dois campeões em Full com health penalizada (`health = 0,75` e `0,71`) como núcleo do risco estrutural, a decisão é checar direção (estável / caindo / subindo) antes de qualquer movimento com Himmel.** Sem saber se o health está em recuperação ou em erosão contínua, qualquer ação é especulação — a direção é o dado que falta para separar "aguardar" de "alinhar com Himmel sobre cobertura preventiva".

- **Dado que `weekly.md` e `monthly.md` estão sem conteúdo e hoje é a primeira leitura qualitativa desde que Yasmin assumiu (22/04), a decisão é tratar o dia como linha de base da série, não como dado a reagir.** O ticket de R$55,91, ADS share de 59,8% e GMV de R$5.087,71 existem sem contexto qualitativo que permita distinguir sazonalidade, efeito ADS temporário ou expansão real de mix — registrar sem agir é o que preserva a capacidade de leitura futura.

---

### O que fazer hoje

1. **Yasmin:** verificar `available_quantity` do item de cauda com cobertura crítica (Kit 06 Canequinhas Acrílico com Suporte, 4 unidades declaradas, ~3 pedidos/dia ontem, `logistic_type = fulfillment`) e confirmar se há reposição viável em 24-48h junto à expedição — motivo: ao ritmo atual, o horizonte de ruptura é 1 a 2 dias; ruptura em anúncio ativo sem reposição gera cancelamentos que impactam `reputation.cancellations_rate`, hoje em zero (`ml_snapshot.reputation`) — sinal de resultado: reposição confirmada em 24h = risco neutralizado e anúncio permanece no top ativo; sem reposição e anúncio pausado espontaneamente pelo ML = registrar como variável confundidora para a leitura dos próximos dias.

2. **Yasmin:** checar a direção (estável / caindo / subindo) do `health` dos dois campeões em Full com penalização ativa (Kit 4 Potes 1050ml em 0,75 e Conjunto 5 Potes de Vidro Tampa Vermelha em 0,71, `top_items_details`) — motivo: a tese L01 aponta esses dois como núcleo do risco estrutural de exposição orgânica; sem saber se o health está em queda contínua ou estabilizando, qualquer decisão sobre cobertura ADS é especulação; se ambos estiverem caindo, a hipótese de erosão de ranking orgânico se confirma e exige alinhamento preventivo com Himmel antes que o ADS seja obrigado a compensar ainda mais — sinal de resultado: health estável ou em recuperação nos dois = manter observação sem ação; health caindo em um ou em ambos = Yasmin alinha com Himmel sobre cobertura nos próximos dias.

3. **Yasmin:** registrar formalmente como ponto zero da série qualitativa: ADS share 59,8% (R$3.041,56 / R$5.087,71), ROAS 11,6x, ACOS 4,33%, ticket médio R$55,91 e GMV R$5.087,71 — motivo: memória qualitativa estava em branco; sem linha de base não há como julgar nos próximos dias se o ticket continua em expansão (confirmando a tese L01 de upgrade de mix) ou se reverte (indicando que era ADS-driven e sazonal); o registro de hoje permite que o próximo ciclo já seja comparativo — sinal de resultado: ticket acima de R$52 por 2+ dias com spend estável confirma expansão real de mix; ADS share acima de 62% com ticket caindo abaixo de R$50 em dia de spend normal indica que a expansão era inteiramente mediada pelo investimento em ADS.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel para ajustar, escalar ou pausar campanhas.** Com ROAS 11,6x e ACOS 4,33% e memória qualitativa zerada, qualquer alteração introduz uma variável que impede separar comportamento natural de efeito de intervenção; a L01 é explícita: campanha eficiente em fase inaugural de série é para observar, não para mexer — a regra de "ADS share ≥ 50% + ROAS > 5x + ACOS < 10% = não mexer" está ativa aqui.

2. **Não interpretar a queda de -20,9% em pedidos vs 7d como deterioração e agir sobre ela.** A L01 identifica o outlier de 29/04 (134 pedidos, R$5.618) como responsável por inflar a média de 7d; os pedidos do dia (91) estão praticamente no patamar de 60d (`orders_vs_60d_pct = -0,2%`) e alinhados com o mesmo dia da semana (`orders_vs_same_weekday_pct = -1,6%`) — tratar esse delta negativo de 7d como sinal de fraqueza e reagir seria agir sobre artefato estatístico, não sobre tendência real.

3. **Não pausar, redirecionar ou escalar anúncios com health baixa sem confirmar a direção primeiro.** O health de Kit 4 Potes 1050ml (0,75) e Conjunto 5 Potes Tampa Vermelha (0,71) pode estar estabilizando — anúncios em penalização que estão em plateau representam risco diferente de anúncios em queda ativa; agir sem saber a direção pode interromper processo natural de normalização ou introduzir variável que dificulta atribuir causa correta à evolução futura.

---

### Escalonamento

**observar**

A conta não apresenta risco operacional que exija acionamento imediato de Himmel ou Kobe. A reputação está verde-estável (`5_green`, `cancellations_rate = 0`, `power_seller_status = gold`), todas as campanhas ativas operam com eficiência alta, e os anúncios do top não têm `status: paused` com pedidos abertos. O único risco operacional imediato (estoque crítico das Canequinhas Acrílico) é resolvível pela Yasmin na operação — não envolve ADS nem decisão estrutural. O escalonamento sobe de "observar" para "alinhar com Himmel" se o health dos campeões Full cair por mais 2 ciclos consecutivos (sinalizando erosão orgânica progressiva que ADS precisará compensar com maior cobertura) ou se o ADS share ultrapassar 65% mantendo ROAS alto (indicando que o patamar está sendo comprado, não conquistado organicamente). Sobe para "escalar para Kobe" se ADS share ficar acima de 55% por 3 dias consecutivos com health continuando a cair — configurando dependência estrutural que extrapola decisão tática diária e exige discussão sobre recomposição de catálogo ou mix de fulfillment.