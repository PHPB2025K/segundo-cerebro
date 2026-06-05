<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Proteger MLB6232315532 (Catálogo gold_pro Full) antes de qualquer outra ação.** Dado que a tese da L01 é ganho de patamar sustentado por campeões em Full, e esse é o único anúncio `is_catalog=true` da conta com `listing_type=gold_pro`, a cobertura de 11 unidades contra ritmo de 16 pedidos/dia configura ruptura sub-dia iminente — ruptura em Catálogo derruba Buy Box e a recuperação de posição é mais lenta do que em Clássico, comprometendo diretamente o patamar atual.

- **Proteger MLB6167272090 (Tulipa, Full) para blindar a elegibilidade Platinum.** A L01 identifica esse anúncio como vetor direto de risco ao `cancellations_rate` no momento de threshold (gap R$3.810, ETA 0,8 dias). Com 5 unidades e 18 pedidos no dia (sub-day runway), é o 7º ciclo do padrão de ruptura recorrente: cada cancelamento automático que entrar na janela oficial ML antes do threshold ser cruzado ameaça os critérios de qualidade obrigatórios para Platinum.

- **Não acionar Himmel sobre ADS.** ADS share em 56,5% (R$4.886,83 / R$8.647,61) com ROAS 14,27x e ACOS 10,64% — campanha eficiente. A lente ADS indica não mexer enquanto ROAS > 5x: qualquer ajuste introduz variável num momento em que a conta está a menos de 1 dia do threshold Platinum e sem histórico longo o suficiente para separar efeito de campanha de comportamento orgânico.

- **Registrar direção do health de MLB5402326666 (0,66) como sinal a confirmar no próximo ciclo.** A L01 documenta esse como o menor health do snapshot, 2º ciclo consecutivo abaixo do threshold 0,85 (documentado na weekly de 02/06 como "primeira aparição em zona crítica"). O 3º ponto define recorrente vs pontual e desbloqueia ou não o alinhamento com Himmel sobre cobertura preventiva.

---

### O que fazer hoje

**1. Yasmin:** verificar `available_quantity` atual do Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo gold_pro Full, 11 unidades no snapshot, ritmo de 16 pedidos/dia = cobertura <1 dia) e confirmar se há reposição em trânsito ao CD do ML — motivo: único `is_catalog=true` da conta; ruptura nesse anúncio derruba o Buy Box ML em Catálogo, e a recuperação de posição persiste por dias após restock, deteriorando diretamente o patamar atual confirmado pela L01 — sinal de resultado: reposição confirmada em trânsito com ETA ≤ 24h = risco neutralizado nos próximos 2-3 dias; `available_quantity ≤ 5` sem reposição confirmada = alerta de ruptura iminente, checagem novamente em 4-6h.

**2. Yasmin:** verificar `status` e `available_quantity` do Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full, 5 unidades no snapshot, 18 pedidos ontem, 7º ciclo do padrão de ruptura recorrente) e confirmar se há reposição em trânsito — motivo: com sub-day runway, o anúncio pode pausar ainda neste ciclo; cancelamentos automáticos por ruptura entram no `cancellations_rate` da janela oficial ML precisamente no momento em que a conta está a R$3.810 do threshold Platinum — qualquer saída de zero no `cancellations_rate` antes da promoção ameaça os critérios de qualidade para a medalha — sinal de resultado: anúncio ativo com reposição confirmada = risco blindado; `status=paused` = Yasmin registra data/hora da ruptura como variável confundidora para as métricas de reputação dos próximos 3-5 snapshots e monitora `cancellations_rate` no próximo ciclo.

**3. Yasmin:** registrar o `health` do Kit 4 Potes 640ml Tampa Azul-petróleo (MLB5402326666, Full, 0,66 no snapshot) como 2º ponto confirmado da série — motivo: menor health do snapshot atual, abaixo de 0,85 pelo 2º ciclo (documentado na weekly de 02/06 como aparição inaugural em zona crítica); o 3º ponto no próximo ciclo classifica o padrão como recorrente ou pontual e define se há ação tática pendente — sinal de resultado: health ≥ 0,68 no próximo ciclo = manter observação sem ação; health ≤ 0,65 ou 3º ciclo abaixo de 0,70 = Yasmin alinha com Himmel sobre cobertura ADS preventiva nesse anúncio.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel para ajustar ou revisar campanhas.** ROAS 14,27x e ACOS 10,64% — eficiente. O gatilho para revisão de campanha com Himmel (ROAS < 3x ou ACOS > 30%) está muito distante. A série de ADS share está em estabilização (50–57% nos últimos 5 ciclos), não em tendência de ineficiência. Qualquer ajuste agora introduz variável num sistema sem histórico longo o suficiente para separar efeito de ADS de comportamento orgânico, e num momento de threshold Platinum iminente.

2. **Não tomar nenhuma ação sobre MLB3288536143 (Potes de Vidro Tampa Cinza+Vermelha, Full, health=0,71) além de observação.** A L01 documenta 13 ciclos idênticos no mesmo valor — padrão confirmado como estável, sem direção de piora observável. `available_quantity=88` é robusto. Pausar ou alterar o principal anúncio da conta (39% do volume diário) sem conhecer o driver da health degradada (atrasos, claims, completude de listing — pendência estrutural do pacote desde 22/05) seria agir sobre hipótese sem confirmação.

3. **Não escalar para Kobe hoje.** Os dois riscos operacionais ativos (Tulipa em sub-day, Catálogo com cobertura crítica) têm solução dentro do nível tático: verificar estoque, confirmar reposição. Nenhuma decisão estrutural está madura agora. O gatilho de Kobe é: ruptura confirmada em MLB6232315532 (Buy Box perdida em Catálogo) *somada* a `cancellations_rate > 0` antes da promoção Platinum — esse cenário cria dilema entre proteger reputação e sustentar patamar que extrapola decisão tática.

---

### Escalonamento

**observar**

A conta está em ganho de patamar confirmado pela L01 em múltiplas janelas, com campanha eficiente, reputação verde e MercadoLíder Platinum iminente. Os dois riscos operacionais ativos têm solução no nível tático — Yasmin verifica estoque e confirma reposição sem precisar de Himmel ou Kobe. O escalonamento muda para **alinhar com Himmel** se: (a) MLB5402326666 chegar ao 3º ciclo com health abaixo de 0,70, confirmando erosão orgânica recorrente em Full que justifica cobertura preventiva de ADS; ou (b) ADS share ultrapassar 60% por 2 ciclos consecutivos com ACOS acima de 20%, sinalizando ineficiência que precisa de revisão de segmentação. O escalonamento muda para **Kobe** se MLB6232315532 entrar em ruptura com perda de Buy Box *e* `cancellations_rate` sair de zero antes da promoção Platinum — combinação que cria dilema estrutural entre proteger reputação e sustentar o patamar atual, extrapolando o nível tático.