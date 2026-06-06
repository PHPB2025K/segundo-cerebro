<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a tese da L01 é "vulnerável" com risco estrutural principal de ruptura iminente do líder Full:** a decisão central de hoje é proteger o `MLB3288536143` (Conjunto 5 Potes Vidro Tampa Cinza, Full, 25,6% dos pedidos do dia) antes que `available_quantity=58` se esgote ao ritmo de 42 pedidos/dia — cobertura de ~1,4 dias não tolera 1 ciclo sem ação de restock.

- **Dado que a L01 identifica coincidência de timing entre cancelamentos prospectivos acumulados (Tulipa pausada, 7º+ ciclo, 11 pedidos hoje) e threshold Platinum cruzado com promoção formal ainda pendente:** a prioridade tática de hoje é monitorar `cancellations_rate` no próximo snapshot — qualquer saída de zero é o sinal mais sensível da conta e invalida a janela de elegibilidade formal antes que ela se feche.

- **Dado que a L01 classifica ADS share em 55,1% com ROAS 14x e ACOS 7,27% como zona de eficiência dominante:** Himmel não é acionado. Os problemas que ameaçam o patamar hoje são de estoque e cancelamento, não de cobertura de campanha. Introduzir variável numa campanha eficiente no pior momento operacional da conta seria precipitado.

- **Dado que MLB5402326666 (Kit 4 Potes 640ml, Full) aparece no 2º ciclo consecutivo com health=0,66 e que MLB3288536143 carrega health=0,71 há ~15 ciclos sem reversão observada:** a direção interna do health nesses dois Clássicos Full precisa de mais um ciclo para classificar como deterioração ativa vs estagnação — checar direção, não agir ainda.

---

### O que fazer hoje

1. **Yasmin:** verificar ETA de reposição do Conjunto 5 Potes Vidro Tampa Cinza (Full, `available_quantity=58` após 42 pedidos hoje, cobertura ~1,4 dias ao ritmo do dia) junto à cadeia de suprimentos/Trader — a cobertura não fecha o fim de semana ao ritmo atual; ruptura deste anúncio no momento em que a conta aguarda reconhecimento formal do Platinum interrompe o maior gerador de pedidos da conta (25,6% do volume) via modalidade Full, onde reativação demora dias — **sinal de resultado:** ETA confirmado dentro de 24h com quantidade suficiente = risco neutralizado para o ciclo imediato; ETA acima de 48h ou sem resposta = Yasmin escala para Kobe sobre priorização de restock Full urgente.

2. **Yasmin:** monitorar `cancellations_rate` da reputação (`ml_snapshot.reputation.cancellations_rate`) no próximo snapshot ML — os 11 pedidos gerados hoje no anúncio pausado da Tulipa (MLB6167272090, `status=paused`, `available_quantity=0`) são cancelamentos prospectivos garantidos no 7º+ ciclo consecutivo do padrão; com `gap_revenue_brl=0` e `progress_pct=100%`, qualquer entrada desses cancelamentos na janela oficial antes do reconhecimento formal da medalha é o risco mais sensível da conta — **sinal de resultado:** `cancellations_rate=0` no próximo snapshot = série ainda não entrou na janela oficial, observar por mais 1-2 ciclos; `cancellations_rate > 0` = Yasmin aciona Kobe sobre impacto na elegibilidade Platinum formal antes de qualquer outra ação.

3. **Yasmin:** checar `available_quantity` do Kit 6 Canecas Lisas 200ml (MLB6232315532, único `is_catalog=true` + `listing_type=gold_pro` do top 10, Full, 30 unidades após 13 pedidos hoje) — cobertura de ~2,3 dias; ruptura em Catálogo perde Buy Box e recuperação de posição é lenta; restock foi confirmado entre 04/06 e 05/06 mas margem é estreita — **sinal de resultado:** `available_quantity` ≥ 20 após baixa do dia = zona segura por mais 1-2 ciclos sem ação; `available_quantity` < 15 = Yasmin aciona providência de restock imediata via cadeia de suprimentos (não Himmel).

---

### O que NÃO fazer ainda

1. **Não acionar Himmel sobre ADS ML.** ROAS 14x com ACOS 7,27% e share 55,1% é a configuração que a regra tática proíbe de tocar. Os riscos que ameaçam o patamar hoje são ruptura de estoque Full e acumulação de cancelamentos — nenhum deles é resolvível por ajuste de campanha. Mexer em campanha eficiente sem risco de ADS introduz variável numa conta em momento operacional crítico e impede separar efeito de comportamento natural.

2. **Não pausar, redirecionar nem tomar qualquer ação sobre MLB3288536143 por causa do health=0,71.** O anúncio está ativo, lidera volume há ~15 ciclos e o health está estagnado — não em queda confirmada. A ação correta é verificar a direção do health no próximo ciclo (estável/caindo/subindo), não intervir. Pausar ou redirecionar artificialmente o maior vetor da conta sem driver confirmado de deterioração ativa criaria ruptura desnecessária muito mais danosa que o health degradado.

3. **Não escalar para Kobe hoje sobre a transição Platinum.** O lag entre `gap_revenue_brl=0` / `progress_pct=100%` e atualização da medalha (`power_seller_status` ainda `gold`) é comportamento esperado no sistema ML. Escalar agora seria precipitado — Kobe só entra se `cancellations_rate` sair de zero (acionando o vetor de risco à elegibilidade) ou se `power_seller_status` permanecer `gold` por mais 2 ciclos com critérios 100% atendidos, sinalizando possível barreira não visível no pacote.

---

### Escalonamento

**observar** — com dois gatilhos de escalonamento imediato definidos.

A conta opera no patamar mais alto da série histórica observada, ADS roda com eficiência máxima (ROAS 14x, ACOS 7,27%) e reputação está sólida (`color=5_green`, `cancellations_rate=0` oficial, `claims_rate` em 36% do threshold). Yasmin resolve os dois itens críticos de hoje (ETA de restock do líder Full + monitoramento de `cancellations_rate`) sem precisar de Himmel ou Kobe. Dois gatilhos de mudança imediata: **(1)** se `cancellations_rate` sair de zero no próximo snapshot → Yasmin aciona Kobe sobre impacto direto na elegibilidade Platinum formal antes de qualquer outra decisão; **(2)** se ETA de reposição do Conjunto 5 Potes Vidro Tampa Cinza for acima de 48h ou indisponível → Yasmin escala para Kobe sobre priorização de restock Full urgente. Se ambos se mantiverem sob controle, escalonamento permanece em observação pelos próximos 2-3 ciclos, com foco em confirmar reconhecimento formal da medalha e direção do health dos dois Clássicos Full degradados.