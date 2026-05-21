<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Dado que a L01 identificou risco operacional iminente** no Kit 06 Canequinhas Acrílico (`available_quantity=3`, 3 pedidos gerados ontem com status ativo): esta é a única situação que justifica ação hoje sem aguardar confirmação em mais de um ciclo — estoque ≤ 5 em anúncio de giro ativo é exceção à regra de "não agir com dado de um dia". Ação antes que o ML gere cancelamento automático.

- **Dado que a tese estratégica identifica erosão orgânica progressiva nos anúncios campeões em Full**, e que `MLB3288536143` (`is_catalog=true`, health=0.71) é anúncio em catálogo abaixo do limiar de penalização ML: per Lente Tática 4, ruptura de posição em catálogo demora a recuperar — Yasmin investiga causa do health antes de qualquer outra ação sobre esse anúncio. `MLB4073003575` (health=0.75, `is_catalog=false`) segue a mesma lógica de observação dirigida para verificar direção — estabilizando, caindo ou recuperando.

- **Dado que a tese estratégica classifica a conta como vulnerável mas com ADS eficiente em primeira leitura** (ROAS 11,6x, ACOS 4,33%, `ads_summary`): a postura correta é **não acionar Himmel e não ajustar campanha**. O share de 59,8% sobre um único dia sem histórico anterior não é base para decisão de ADS — é base para registro de ponto zero e observação de série.

- **Dado que weekly.md e monthly.md são templates vazios**, esta análise não tem tese anterior para confirmar ou refutar: toda a leitura de patamar e dependência ADS é inaugural. Tática hoje é ancorar os indicadores-chave como linha de base sem introduzir variável que impeça leitura dos próximos dias.

---

### O que fazer hoje

**1. Yasmin:** verificar `available_quantity` e status do anúncio campeão de canequinhas com estoque em cobertura crítica (3 unidades em Cross-Docking, 3 pedidos gerados ontem com anúncio ativo) — risco operacional imediato: novos pedidos sem reposição configuram cancelamentos prospectivos que impactam `reputation.cancellations_rate` e `delayed_handling_rate`; o anúncio não está pausado, então o ML continuará recebendo pedidos — **sinal de resultado:** se reposição for acionada em 24h e nenhum cancelamento for gerado, risco neutralizado; se o anúncio entrar em ruptura ou gerar cancelamento registrado, classificar como variável confundidora e registrar data de ocorrência para isolar impacto na reputação nos próximos ciclos.

**2. Yasmin:** verificar causa e direção do health nos dois anúncios campeões em Full com penalização ativa — o anúncio em catálogo (`MLB3288536143`, health=0.71, `is_catalog=true`, estoque=369) tem prioridade per Lente 4: health < 0.85 em catálogo é sinal de perda de posição que demora a recuperar; Yasmin investiga o que está gerando a penalização (reclamações, atraso, qualidade do listing) antes de qualquer outra ação sobre esse anúncio; em seguida, verifica direção do health do anúncio Clássico com penalização (`MLB4073003575`, health=0.75) — **sinal de resultado:** health estável ou em recuperação nos dois = observar sem ação; health caindo em qualquer um dos dois = alinhar com Himmel sobre cobertura ADS preventiva nesse anúncio específico antes que posição orgânica deteriore mais.

**3. Yasmin:** registrar como ponto zero da série: ticket médio do dia (R$55,91), ADS share (R$3.041,56 / R$5.087,71 = 59,8%), ROAS (11,6x), ACOS (4,33%) e health dos dois campeões penalizados — motivo: weekly e monthly estão sem tese histórica; sem esse registro hoje, os próximos dias não terão linha de base para identificar movimento de ADS share ou deterioração de health — **sinal de resultado:** se nos próximos 3 dias o ticket permanecer acima de R$50 e o ADS share ficar entre 55–65% com ROAS mantendo acima de 8x, confirma estrutura estável que pode ser observada sem intervenção; se ADS share superar 65% com ticket caindo abaixo de R$48, hipótese de dependência ADS compensando perda orgânica se fortalece.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajustar, pausar ou redistribuir campanhas:** ROAS de 11,6x e ACOS de 4,33% (`ads_summary`) são resultado de campanha eficiente em leitura inaugural sem histórico — qualquer ajuste hoje introduz variável que impede separar efeito de comportamento natural da conta. A L01 é explícita: campanha eficiente em fase de leitura é para observar, não mexer. Premissa de acionamento requer share acima de 60% por 3 dias consecutivos com ROAS em queda, não um único dia de share elevado com ROAS em máxima histórica.

- **Não tratar a queda de volume vs 7d (-20,9% em pedidos) como alerta de degradação da conta:** o controle por dia da semana (`orders_vs_same_weekday_pct=-1,6%`, média histórica 92,5 pedidos) e a janela de 60d (`orders_vs_60d_pct=-0,2%`) mostram volume dentro do padrão estrutural da conta. A média de 7d foi puxada por dias de maior volume que incluem provavelmente ticket menor — tratar essa comparação como alerta seria precipitado e levaria a intervenções desnecessárias em campanha ou mix.

- **Não sinalizar migração de anúncios de Cross-Docking para Full como ação tática:** o campeão do dia (Conjunto 5 Potes Tampa Preta, 23 pedidos, Cross-Docking) mostra que Cross-Docking pode sustentar volume expressivo. A divergência entre base ativa (34,1% Full) e pedidos 30d (73,9% Full) é estrutural e relevante, mas a decisão sobre migração envolve logística, custo de CD e estratégia de mix — extrapola tática diária e pertence a Kobe/Trader, não a uma ação de Yasmin hoje.

---

### Escalonamento

**observar**

A reputação está limpa (`5_green`, `cancellations_rate=0`, `claims_rate=0.0025`), o volume está dentro da banda histórica e a campanha de Himmel está em zona de máxima eficiência. A exceção que justifica ação hoje é o risco operacional pontual de estoque crítico em canequinhas — resolvido pela Yasmin sem necessidade de Himmel ou Kobe. Para o risco estrutural principal identificado pela L01 (health em deterioração + ADS dominante), o padrão correto é coletar a série antes de acionar qualquer agente externo. **Gatilho para alinhar com Himmel:** health de qualquer um dos dois campeões penalizados continuando a cair no próximo ciclo com dado disponível, **ou** ADS share superando 65% com ROAS caindo abaixo de 8x. **Gatilho para escalar para Kobe:** ADS share acima de 60% por 3 dias consecutivos com health dos campeões em queda — confirma dependência ADS estrutural sobre orgânico deteriorado, decisão que extrapola a tática diária de Yasmin.