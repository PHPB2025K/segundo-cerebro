<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Dado que a L01 identificou ruptura técnica em andamento no Kit 06 Canequinhas Acrílico** (`available_quantity = 2`, 3 pedidos registrados ontem, anúncio `status: active` em fulfillment), a decisão correta é ação imediata da Yasmin — não é cenário de "aguardar 2-3 dias". Cada novo pedido gerado sem estoque disponível configura cancelamento prospectivo que impacta `reputation.cancellations_rate` antes de aparecer na métrica oficial.

- **Dado que a L01 identifica ADS share de 75,5% com ROAS implícito ~13,4x e ACOS 4,71%, e que esta é a primeira leitura estruturada sem histórico acumulado (`weekly.md` e `monthly.md` vazios)**, a decisão correta é não acionar Himmel e registrar os parâmetros de hoje como ponto zero da série. Qualquer ajuste neste momento introduz uma variável externa que impede separar o comportamento natural da conta do efeito da intervenção.

- **Dado que a L01 identificou o Kit 6 Canecas Porcelana (`available_quantity = 19`, 5 pedidos/dia, fulfillment) como segundo anúncio Full em zona de ruptura iminente**, a decisão é checar cobertura ainda hoje — não como urgência igual ao Canequinhas, mas como proteção preventiva antes que o ritmo de vendas consuma o estoque nos próximos 3–4 dias.

- **Dado que a L01 sinaliza health = 0,75 no Kit 4 Potes 1050ml Retangular (abaixo do limiar de penalização 0,85, anúncio em fulfillment com 8 pedidos ontem)**, a decisão é observar a direção do health ao longo de 2–3 dias antes de qualquer movimento — a ação relevante é checar tendência, não intervir sem confirmação de trajetória.

---

### O que fazer hoje

1. **Yasmin:** verificar `available_quantity` e status dos pedidos abertos do anúncio de canequinhas acrílico (top 10, `logistic_type: fulfillment`, 2 unidades disponíveis, 3 pedidos gerados ontem) e tomar decisão binária — reposição em <24h (aciona fluxo de ressuprimento Full) ou cancelamento controlado dos pedidos em aberto antes que o ML cancele automaticamente — motivo: ruptura técnica em andamento; qualquer pedido aceito sem estoque disponível resulta em cancelamento ML-originado que afeta `reputation.cancellations_rate` antes de aparecer na métrica oficial da API, e a L01 já sinalizou esse anúncio como risco operacional iminente — **sinal de resultado:** se reposição for confirmada em <24h, risco neutralizado e anúncio preservado; se cancelamentos aparecerem em `metrics.cancelamentos` acima de 5/dia nos próximos 2 ciclos, confirma que o impacto já vazou para a reputação e Yasmin precisa monitorar a cor da reputação nas próximas 72h.

2. **Yasmin:** registrar os parâmetros de hoje como ponto zero da série de observação de ADS — ADS share 75,5% (R$4.593,66 / R$6.082,82), ticket médio R$60,83, ACOS 4,71% (`ml_snapshot.ads_summary`) — motivo: a L01 identifica dependência estrutural de ADS como risco principal da conta, mas esta é a primeira leitura com share calculável; sem série histórica, qualquer decisão sobre campanhas seria especulação — **sinal de resultado:** ADS share acima de 70% por 3 dos próximos 5 dias confirma a tese de dependência estrutural da L01 e abre a discussão de escalonamento para Kobe; ticket abaixo de R$50 em dia com spend similar ao de hoje (~R$340) indicaria que o ticket atual reflete mix ADS-induzido, não preferência orgânica consolidada.

3. **Yasmin:** checar o ritmo de saída vs cobertura do anúncio de canecas porcelana em fulfillment (top 10, 19 unidades disponíveis, 5 pedidos registrados ontem) — motivo: a L01 sinalizou como segundo anúncio Full em zona de ruptura iminente com cobertura de ~3–4 dias no ritmo atual; diferente do Canequinhas, não há evidência de ruptura hoje, mas a janela para reposição é estreita — **sinal de resultado:** se ritmo de vendas cair para ≤2 pedidos/dia nos próximos 2 dias, urgência reduzida; se mantiver ≥5 pedidos/dia, Yasmin aciona ressuprimento Full imediatamente para preservar o anúncio sem interrupção.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajuste de campanhas.** ROAS implícito de ~13,4x e ACOS 4,71% (`ml_snapshot.ads_summary`) configuram eficiência excepcional, e a L01 é explícita: esta é a primeira leitura estruturada da conta sem histórico acumulado. A regra tática é clara para ADS share ≥50% com ROAS >5x e ACOS <10%: não mexer. Qualquer ajuste introduz variável que contamina os próximos 3–5 dias de leitura e impede isolar o comportamento natural da conta — o dado relevante que Himmel precisaria para uma decisão bem-informada ainda está sendo gerado.

- **Não tratar a queda de volume vs 7d (-15,9%) como sinal de perda de patamar ou justificativa para intensificação de campanhas.** A L01 identifica explicitamente isso como normalização sobre base elevada da semana passada, não reversão estrutural: volume está em linha com 30d (+0,7%) e acima de 60d (+8,2%). Agir sobre essa variação seria responder a ruído, não a sinal — e potencialmente quebrar a eficiência das campanhas atuais ao forçar escalada desnecessária.

- **Não pausar ou redirecionar o anúncio do Kit 4 Potes 1050ml Retangular (health = 0,75) sem antes confirmar a direção do health ao longo de 2–3 dias.** A L01 sinaliza o anúncio como penalizado (`health < 0,85`, fulfillment, 8 pedidos ontem), mas a direção — estável, caindo ou recuperando — é desconhecida sem série de leitura. Intervenção prematura em anúncio com volume ativo pode piorar ranking e introduzir variável confundidora justamente quando a conta está em fase de mapeamento de baseline.

---

### Escalonamento

**observar** — com exceção do risco operacional do anúncio de canequinhas acrílico, que sai do modo observação e exige ação da Yasmin ainda hoje.

A conta está em modo de coleta de baseline em todos os vetores estratégicos relevantes: ADS share sem série histórica, health sem direção confirmada, ticket sem confirmação se orgânico ou ADS-induzido. O risco operacional do anúncio Full com 2 unidades é a única situação que justifica ação imediata — e ela é resolvível no nível da Yasmin sem envolver Himmel ou Kobe. Se ADS share permanecer acima de 70% por 3 dias consecutivos mantendo ROAS atual, Yasmin abre discussão com Kobe sobre dependência estrutural de mídia paga — essa seria a condição de transição de "observar" para "escalar para Kobe". Se health do Kit 4 Potes continuar caindo nos próximos 2 ciclos, Yasmin alinha com Himmel sobre cobertura preventiva — transição de "observar" para "alinhar com Himmel".