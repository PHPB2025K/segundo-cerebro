<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Dado que o risco operacional imediato identificado pela L01 é ruptura consumada no Kit 06 Canequinhas (MLB4410218897)** — `available_quantity=1` com 3 pedidos registrados no dia em anúncio ainda `active` em Full — a decisão tática prioritária é proteger a reputação antes que o ML pause automaticamente e converta os pedidos em cancelamentos que impactam `cancellations_rate`. Isso não depende de confirmar hipótese: o dado é factual e o risco é imediato.

- **Dado que a L01 identificou ADS share de 75,1% do GMV com ROAS 13,4x e ACOS 4,71%** — campanha Himmel em zona de máxima eficiência — a decisão tática é **não tocar em ADS**. A regra da Lente 5 é clara: quando share ≥50% + ROAS >5x + ACOS <10%, qualquer ajuste introduz variável num sistema sem histórico interpretativo (weekly/monthly vazios). A ação correta é registrar o ponto zero da série, não otimizar.

- **Dado que a L01 sinaliza Kit 6 Canecas Tulipa (MLB6167272090) com `available_quantity=14` e ritmo de 5 pedidos/dia em Full** — cobertura estimada de 2-3 dias — a decisão tática é verificar e acionar reposição antes da ruptura. Diferente do Canequinhas (crise já consumada), aqui há janela de 24-48h antes que vire risco operacional. Ação preventiva, não emergencial.

- **Dado que a L01 registra Kit 4 Potes 1050ml (MLB4073003575) com `health=0,75` em Full** e que há 7 anúncios com health abaixo de 0,85 na conta (`account_overview.active_analysis.low_health_count=7`), a decisão tática é checar a direção do health — estável, caindo ou recuperando — antes de qualquer movimento. Health baixo estático é diferente de health em queda: só o segundo justifica ação.

---

### O que fazer hoje

**1. (Prioridade máxima — risco operacional)**
**Yasmin:** verificar status e estoque do anúncio Kit 06 Canequinhas Acrílico (`available_quantity=1`, logistic_type=fulfillment, 3 pedidos registrados ontem) e acionar reposição no CD do ML ou cancelamento controlado dos pedidos em aberto — motivo: com 1 unidade em Full e 3 pedidos do dia, o ML pode pausar o anúncio automaticamente e gerar cancelamentos involuntários que impactam `reputation.cancellations_rate` na janela oficial; cancelamento controlado pela Yasmin é menos danoso à reputação do que cancelamento automático pelo ML — sinal de resultado: se reposição chegar ao CD antes da pausa automática, risco neutralizado; se anúncio aparecer `paused` no próximo pacote sem reposição confirmada, registrar como variável confundidora para a leitura dos próximos dias de reputação.

**2. (Preventivo — janela de 24-48h)**
**Yasmin:** verificar cobertura de estoque do anúncio Kit 6 Canecas Tulipa Lisa (`available_quantity=14`, logistic_type=fulfillment, 5 pedidos ontem) e providenciar reposição ou alerta ao Trader sobre ritmo de esgotamento — motivo: ao ritmo de 5 pedidos/dia, o estoque no CD do ML esgota em 2-3 dias; ruptura em Full reduz exposição e pode afetar posição no ranking enquanto o anúncio fica inativo aguardando reabastecimento — sinal de resultado: reposição confirmada com cobertura para ≥7 dias = risco neutralizado; ausência de movimento com estoque caindo abaixo de 5 unidades = acionar alerta prioritário.

**3. (Observação estrutural — ponto zero da série)**
**Yasmin:** registrar ADS share de hoje (75,1% — R$4.593,66 de R$6.113,02) e ticket médio (R$60,52) como ponto zero da série de observação — motivo: primeira leitura estruturada sem histórico interpretativo confirmado (weekly/monthly vazios); sem série, não é possível confirmar se dependência de ADS é crônica ou se ticket elevado é sustentável organicamente — sinal de resultado: ADS share ≥60% por 3 dias consecutivos confirma dependência estrutural e abre discussão com Kobe; ticket ≥R$55 por 3 dias sem alteração de spend confirma que o deslocamento de mix é orgânico; ticket abaixo de R$46 em dia de spend reduzido confirma que o ticket alto é ADS-driven.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajustar campanhas ADS ML.** ROAS de 13,4x e ACOS de 4,71% (`ads_summary`) colocam as campanhas na zona de máxima eficiência da Lente 5 — mexer agora introduz variável num sistema sem histórico, impede separar efeito de ajuste de comportamento natural e pode quebrar uma campanha que está funcionando. A dependência de 75,1% de share é risco estrutural que a L01 identificou para observação de médio prazo, não gatilho de ajuste imediato.

- **Não tomar ação sobre Kit 4 Potes 1050ml (health=0,75 em Full) sem antes checar direção do health.** A L01 registra a penalização, mas não há série histórica para saber se 0,75 é piso estabilizado ou queda em curso. Pausar ou redirecionar anúncio com health baixo mas estável é pior do que manter — a regra proíbe intervenção sem saber se o health está caindo, estável ou em recuperação. Ação só se Yasmin confirmar queda ativa em 2 leituras consecutivas.

- **Não escalar para Kobe sobre dependência estrutural de ADS.** A tese da L01 aponta vulnerabilidade real, mas esta é a primeira leitura com dado disponível — sem série de 3-5 dias confirmando que o ADS share se mantém ≥60% estruturalmente, a discussão com Kobe sobre redirecionamento de verba ou diversificação de catálogo seria prematura. Escalonamento só se o ADS share se mantiver ≥60% por 3 dias consecutivos com GMV acima de R$5.000.

---

### Escalonamento

**observar**

Os dois riscos operacionais imediatos (Canequinhas e Canecas Tulipa) são resolvidos pela Yasmin sem necessidade de Himmel ou Kobe — são questões de estoque no CD do ML, não de ADS nem de decisão estrutural. O risco estrutural principal identificado pela L01 — dependência severa de Mercado Ads — é real, mas esta é a primeira leitura sem histórico confirmado; a L01 explicitamente marca a ausência de weekly/monthly preenchidos. Himmel só entra em cena se o ADS share cair para zona de ineficiência (ROAS <3x ou ACOS >30%), o que não é o caso hoje. Kobe só entra se o ADS share se mantiver ≥60% por 3 dias consecutivos confirmando cronicidade estrutural — nesse ponto, Yasmin abre a discussão sobre dependência de mídia paga e possível diversificação de catálogo. Até lá, a postura correta é coletar evidência sem alterar a operação.