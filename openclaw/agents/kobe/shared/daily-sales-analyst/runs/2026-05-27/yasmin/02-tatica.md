<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a L01 identificou ruptura iminente em Full (MLB4676726433, available_quantity=4, 5 pedidos hoje, Frete Grátis ativo), a decisão é ação imediata da Yasmin:** modalidade Full significa que quando o estoque no CD do ML zerar, o anúncio sai do ar sem controle da Budamix — cancelamentos automáticos alimentam `cancellations_rate` hoje em 0%, e o threshold de elegibilidade Platinum é 0,5% com gap de R$38.760 e ETA de 9 dias. O momento de agir é antes da ruptura, não depois.

- **Dado que a tese da L01 é ADS dominante eficiente sustentando o patamar (ROAS 10,38x, ACOS calculado 9,63%), a decisão é não acionar Himmel hoje:** hoje marca o segundo ponto da série de share acima de 65% (22/05: 69,9%; hoje: 67,3%). O gatilho documentado de alinhamento Yasmin–Himmel é o **terceiro** ciclo consecutivo acima de 65% — ainda falta um ponto. Mexer em campanha eficiente antes do gatilho introduz variável em sistema com tese em confirmação e destrói a leitura da série.

- **Dado que o risco estrutural da L01 é orgânico estagnado nos campeões (MLB3288536143 health=0,71, MLB4073003575 health=0,75, 8º ciclo sem reversão), a decisão é observar mais 2 ciclos antes de qualquer ação:** o gatilho de ação é `health < 0,68` em MLB3288536143 — está a 0,03 do limiar. Sem confirmação de direção (caindo vs. estável), qualquer movimento é prematuro.

- **Dado que MLB6167272090 (Canecas Tulipa, Full, available_quantity=16) entregou 6 pedidos hoje (cobertura ~2,7 dias), a decisão é colocar em checagem preventiva mas sem ação imediata:** não atingiu o limiar de ≤5 unidades em campeão de alto giro. A leitura da memória 26/05 registrava 2 unidades — reposição chegou, risco de curtíssimo prazo recuou. Yasmin monitora se o estoque está caindo ou se reposição sustenta cobertura.

---

### O que fazer hoje

1. **Yasmin:** verificar `available_quantity` do Kit 10 Potes Herméticos 1050ml (MLB4676726433, Full, today=4 unidades, Frete Grátis ativo, 5 pedidos hoje) e confirmar se há reposição em trânsito ao CD do ML — risco operacional imediato porque ao ritmo de hoje o anúncio entra em ruptura antes do próximo ciclo; ruptura em Full com Frete Grátis gera cancelamento automático pelo ML que alimenta `cancellations_rate` (hoje 0%, threshold Platinum 0,5%), e o anúncio já registrou episódio idêntico em 25/05 (pausado com estoque zero + 3 cancelamentos confirmados) — **sinal de resultado:** reposição confirmada em trânsito ao CD do ML = risco neutralizado no horizonte de 24h; anúncio pausado sem reposição confirmada = registrar como variável confundidora e monitorar `cancellations_rate` nos próximos 5 ciclos antes de qualquer leitura de reputação.

2. **Yasmin:** registrar ADS share de hoje (67,3% — R$4.811,50 / R$7.150,57) e comparar com o ciclo de amanhã para definir se configura o terceiro ponto consecutivo da série acima de 65% (22/05: 69,9%; hoje: 67,3%) — motivo: a tese da L01 aponta que dois pontos acima de 65% já estão na conta; o terceiro ciclo acima de 65% é o gatilho documentado de alinhamento Yasmin–Himmel sobre cobertura e mix de campanhas; o ACOS médio reportado de 44,85% (média simples por campanha, não ponderado por gasto) sinaliza mix heterogêneo de campanhas que Himmel precisa conhecer antes de qualquer ajuste — **sinal de resultado:** ADS share amanhã ≥ 65% = Yasmin alinha com Himmel nos próximos 1–2 dias sobre mix de campanhas; ADS share < 60% = tese de dominância estrutural enfraquece, observar mais 3 ciclos.

3. **Yasmin:** observar se `available_quantity` do Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full, today=16 unidades, 6 pedidos hoje ≈ cobertura 2,7 dias) está caindo ou se reposição sustenta — motivo: memória 26/05 registrava 2 unidades, o atual de 16 sugere reposição parcial, mas ao ritmo de 6 pedidos/dia o anúncio reentra na zona de risco (≤5 unidades) em ~2 ciclos sem nova reposição; anúncio em Full significa mesma dinâmica de ruptura sem aviso que já ocorreu nesta conta — **sinal de resultado:** `available_quantity` ≥ 10 no próximo ciclo = cobertura adequada, manter em monitoramento passivo; `available_quantity` ≤ 5 = vira ação imediata de mesma natureza que MLB4676726433.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajustar ou redistribuir campanhas Mercado Ads:** ROAS calculado do portfolio é 10,38x e ACOS calculado é 9,63% — campanha eficiente pela regra dura da L02 (ROAS > 5x, ACOS < 10%). O ACOS médio reportado de 44,85% é artefato de média simples entre 11 campanhas com pesos diferentes, não performance real do portfolio. Mexer em campanha eficiente antes do terceiro ponto da série acima de 65% é precipitado — sem esse ponto, não há evidência de ineficiência estrutural que justifique intervenção.

- **Não pausar, redirecionar ou alterar configuração de MLB3288536143 (health=0,71) e MLB4073003575 (health=0,75) por conta do health baixo:** health em nível regular há 8 ciclos sem worsening confirmado. A série interna do ML não está disponível para determinar direção (caindo, estável ou recuperando). Esses dois anúncios somaram ~66% dos pedidos do campeão do dia. Intervir sem saber a direção do health pode destruir a concentração que sustenta o faturamento sem ganho operacional. O gatilho de ação é `health < 0,68` em MLB3288536143 — ainda não atingido.

- **Não interpretar o ACOS médio de campanhas de 44,85% como sinal de campanha ineficiente que precisa de corte imediato:** sem breakdown ADS por platform_item_id (pendência documentada desde 22/05), não é possível saber qual campanha está puxando o ACOS médio para cima. Cortar ou pausar sem esse dado pode afetar exatamente a campanha que está sustentando o share dos campeões. A decisão sobre mix de campanhas fica em espera até o terceiro ponto da série de share ≥ 65% e, preferencialmente, até que Himmel compartilhe o breakdown por anúncio.

---

### Escalonamento

**observar** — com uma ação operacional imediata dentro da alçada da Yasmin.

A única decisão urgente hoje é MLB4676726433: é risco operacional claro (estoque ≤ 5 unidades em Full com giro ativo), Yasmin resolve diretamente verificando reposição no CD do ML. Não envolve Himmel nem Kobe. Para ADS: o segundo ponto da série de share acima de 65% está na conta, mas o gatilho de alinhamento com Himmel exige o terceiro ponto — **amanhã é o dia decisivo**: se ADS share fechar ≥ 65%, Yasmin alinha com Himmel sobre mix de campanhas e o dado de breakdown por anúncio nos próximos 1–2 dias. Se ADS share consolidar acima de 65% por 3 dias consecutivos com ROAS mantendo alta, Yasmin abre discussão com Kobe sobre dependência estrutural da conta em mídia paga — mas esse gatilho não foi atingido hoje.