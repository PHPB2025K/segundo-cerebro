<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Patamar em ganho confirmado + ADS excepcionalmente eficiente → não tocar campanha.** A L01 confirma deslocamento de patamar de ticket nas janelas 30d (+27.0%) e 60d (+33.6%), sustentado por campanha com ROAS 11.6x e ACOS 4.64%. A decisão tática correta é registrar ADS share (59.8%) e ticket (R$55.91) como ponto zero da série e observar continuidade por 3-5 dias — qualquer ajuste de campanha introduz variável num sistema sem baseline histórico consolidado.

- **Health penalizada nos dois campeões em categoria → checar direção antes de agir.** Dado que a tese da L01 identifica `MLB4073003575` (health=0.75) e `MLB3288536143` (health=0.71) como risco estrutural central — ADS possivelmente mascarando deterioração orgânica em anúncios `is_catalog=false` — a decisão tática é determinar se o health está caindo, estabilizando ou recuperando nos próximos 2 ciclos. Sem direção, qualquer movimento (ADS ou orgânico) é ruído.

- **Ruptura iminente em Full → ação operacional hoje, sem esperar confirmação.** `MLB4410218897` (Kit 06 Canequinhas Acrílico) com `available_quantity=3` no CD do ML e 3 pedidos ontem configura risco operacional ML imediato — anúncio em Full pausado por ruptura gera cancelamentos automáticos que impactam `cancellations_rate`, independente de qualquer tese estratégica.

- **Memória inaugural → postura conservadora em decisões de prazo médio.** Weekly e monthly estão em template vazio. A tese da L01 é construída sobre janelas operacionais (7d/30d/60d), não sobre hipóteses confirmadas longitudinalmente. Qualquer decisão estrutural — mix de catálogo, dependência de ADS, diversificação de vetor — precisa de mais 2-3 ciclos antes de virar ação.

---

### O que fazer hoje

1. **Yasmin:** verificar `available_quantity` do Kit 06 Canequinhas Acrílico em Full (`MLB4410218897` — 3 unidades no CD do ML, 3 pedidos registrados ontem) e providenciar reposição emergencial ou alinhar com expedição sobre envio ao CD — motivo: ruptura em Full pausa o anúncio automaticamente pelo ML; com 3 unidades e demanda diária de ~3 pedidos, a janela é de 24h; cancelamentos prospectivos impactam `reputation.cancellations_rate` antes que haja tempo de reação — sinal de resultado: `available_quantity` acima de 20 unidades após reposição neutraliza o risco; se anúncio pausar antes da reposição, Yasmin registra data e hora como variável confundidora para a leitura dos próximos dias.

2. **Yasmin:** checar a direção do `health` dos dois campeões em Full com penalização ativa (Kit 4 Potes 1050ml em 0.75 e Conjunto 5 Potes Tampa Vermelha em 0.71) — se o valor de hoje está acima, igual ou abaixo do snapshot atual — motivo: dado que a L01 aponta ADS potencialmente mascarando deterioração orgânica nesses dois anúncios `is_catalog=false`, a direção do health nos próximos 2 ciclos é o dado que define se o risco é gerenciável por observação ou requer alinhamento com Himmel sobre cobertura preventiva — sinal de resultado: health estável ou recuperando em ambos = manter observação; health caindo em um ou ambos por 2 ciclos consecutivos = Yasmin alinha com Himmel.

3. **Yasmin:** registrar como ponto zero formal da série: ADS share (59.8% = R$3.041,56 / R$5.087,71), ticket médio (R$55.91) e ACOS (4.64%) — motivo: esta é a primeira leitura estruturada com pacote completo (weekly/monthly em template vazio); sem baseline registrado, futuras leituras de dependência de ADS ou variação de ticket ficam sem âncora — sinal de resultado: ADS share acima de 60% por 3 dias consecutivos com ticket mantido fornece evidência para discussão com Kobe sobre dependência estrutural; ticket abaixo de R$50 em dia sem variação de spend sinaliza reversão de mix.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel para ajustar, escalar ou revisar ADS.** ROAS 11.6x e ACOS 4.64% configuram campanha eficiente em fase inaugural. Qualquer ajuste — mesmo com intenção positiva — introduz variável num sistema sem histórico consolidado, impossibilitando separar efeito de campanha de comportamento orgânico. A regra é explícita: campanha com ROAS > 5x e ACOS < 10% é para observar, não para mexer.

2. **Não tomar decisão sobre cobertura ADS dos campeões com base na leitura atual de health.** `MLB4073003575` (0.75) e `MLB3288536143` (0.71) são snapshot único sem direção conhecida. Ajustar cobertura de Himmel sobre anúncios com health desconhecida em trajetória — podendo estar em recuperação — seria precipitado e introduziria confundidor antes de 2 ciclos de confirmação.

3. **Não sinalizar dependência estrutural de ADS para Kobe.** ADS share de 59.8% é preocupante do ponto de vista estrutural, mas esta é a primeira leitura consolidada. Sem série de 3-5 dias, qualquer escalonamento para Kobe sobre diversificação ou risco de dependência seria baseado em dado único — o sinal precisa persistir antes de virar pauta estratégica.

---

### Escalonamento

**observar**

Reputação verde-gold (`cancellations_rate=0`, `claims_rate=0.0025`), campanha eficiente (ROAS 11.6x, ACOS 4.64%), patamar de ticket confirmado em múltiplas janelas e pedidos flat vs 60d — nenhum desses sinais justifica acionamento de Himmel ou Kobe hoje. A única ação imediata é operacional (ruptura em Full do Kit 06 Canequinhas Acrílico), que Yasmin resolve diretamente. O risco estrutural principal — health penalizada nos campeões e dependência de ADS sem orgânico testado — precisa de 2-3 ciclos de leitura para revelar direção. Gatilho para mudar classificação: se health dos dois campeões em Full cair por 2 ciclos consecutivos, Yasmin alinha com Himmel sobre cobertura preventiva; se ADS share superar 60% por 3 dias consecutivos com ROAS mantido, Yasmin abre discussão com Kobe sobre dependência estrutural da conta.