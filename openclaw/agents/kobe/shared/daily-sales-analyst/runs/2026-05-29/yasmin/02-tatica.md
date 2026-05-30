<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a tese da L01 é de ganho de patamar sustentado por portfólio 100% Full + ADS 60.9% eficiente**, a decisão central é **proteger o que permitiu o rompimento** — não testar, não expandir, não mexer em campanha. O patamar é frágil não por causa do ADS, mas porque os anúncios que geraram o resultado estão em risco de ruptura simultânea.

- **Dado que o risco estrutural principal identificado pela L01 é cadeia de rupturas Full**, a prioridade tática é conter o dano antes que `cancellations_rate` saia de 0: os 19 pedidos sobre MLB6167272090 (`status=paused`, `available_quantity=0`) são cancelamentos prospectivos garantidos que ainda não entraram na métrica oficial de reputação — e o ETA para Platinum é 5,9 dias. Yasmin precisa tratar isso como risco operacional imediato, não como observação.

- **Dado que MLB4676726433, MLB4676751119 e MLB6754669844 estão com cobertura de 1–2 ciclos em modalidade de envio Full**, a decisão é acionar urgência de reposição ao CD do ML via quem tiver alçada operacional para isso — essa é uma decisão de abastecimento, não de ADS. Yasmin opera como focal point de alerta; migração ou reclassificação de modalidade de envio é pauta para Trader/Kobe, não ação tática de hoje.

- **Dado que ADS share está em 60.9% com ROAS 12.2x e ACOS 5.74%**, a decisão é explicitamente **não acionar Himmel** — campanha eficiente. O que muda esse julgamento é o share cruzar 3 ciclos consecutivos acima de 55% com ROAS mantido, que ativa uma conversa estrutural com Kobe sobre dependência de mídia paga — não ajuste de campanha.

---

### O que fazer hoje

1. **Yasmin:** verificar se os pedidos gerados sobre o anúncio do Kit 6 Canecas Tulipa 250ml (paused, estoque zero) já geraram cancelamentos automáticos ou ainda estão pendentes — risco operacional imediato: se ML cancelar automaticamente esses pedidos antes de Yasmin agir, os registros entram em `cancellations_rate` que hoje é 0, colocando em risco a exigência de qualidade do MercadoLíder Gold na janela dos próximos 5,9 dias de ETA para Platinum — sinal de resultado: se `cancellations_rate` permanecer em 0 no próximo snapshot, risco neutralizado ou absorvido pelo sistema; se sair de 0, confirma que o evento entrou na janela oficial e Yasmin precisa registrar como variável confundidora para leitura dos próximos ciclos.

2. **Yasmin:** acionar urgência de reposição Full ao CD do ML para os três anúncios com cobertura crítica (potes 1050ml — 10 un com ~1 dia de cobertura, potes 1050ml — 6 un com 1 unidade restante, potes 640ml — 6 un com 2 unidades restantes) — motivo: em modalidade de envio Full, reposição não é imediata; ruptura simultânea desses três reduz o portfólio operacional ativo exatamente na semana do ETA para Platinum, e sem volume para sustentar o ritmo de R$4.491/dia o gap de R$26.538 deixa de fechar no prazo estimado — sinal de resultado: se ETA no próximo snapshot mantiver-se abaixo de 7 dias com pelo menos um dos três anúncios com reposição confirmada em trânsito, risco operacional sob controle; se ETA subir acima de 8 dias sem reposição em vista, o patamar de hoje não se sustenta até a promoção.

3. **Yasmin:** checar direção do `health` dos dois campeões em Full com penalização (Jogo Potes 5 Peças em 0.71 e Kit 4 Potes 1050ml em 0.75) — oitavo ciclo idêntico, sem direção observável até agora — motivo: se health começar a cair a partir deste ciclo (gatilho L01: abaixo de 0.68 em qualquer dos dois), hipótese de erosão de ranking orgânico se confirma num momento em que ADS está sustentando 60.9% do GMV, ou seja, qualquer queda de exposição orgânica não compensada pela campanha afeta o patamar diretamente — sinal de resultado: health estável ou em recuperação = manter observação sem ação; health caindo em ambos por 2 ciclos consecutivos = Yasmin alinha com Himmel sobre cobertura preventiva antes que o 9º ciclo confirme tendência.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para qualquer ajuste de campanha ADS.** ROAS 12.2x e ACOS 5.74% indicam campanha eficiente — qualquer toque agora introduz variável num sistema que está gerando o maior GMV da série recente. O share de 60.9% é elevado, mas é *estruturalmente* elevado há 4 ciclos consecutivos; isso é insumo para discussão futura com Kobe sobre dependência, não sinal de ineficiência que justifique intervenção tática imediata.

- **Não recomendar pausar ou redirecionar anúncios com health baixo** (MLB3288536143: 0.71; MLB4073003575: 0.75). Oito ciclos idênticos sem variação de direção indicam estabilidade no patamar atual — não deterioração ativa. Pausar anúncio com health baixo mas estável remove volume de portfólio exatamente quando o resultado do dia dependeu de poucos anúncios em Full. Ação só se health cair abaixo de 0.68.

- **Não tratar o ganho de patamar como base para escalar verba ou testar segundo vetor de anúncio.** A tese da L01 é de ganho com vulnerabilidade — não ganho consolidado. Enquanto 3–4 anúncios em Full estiverem em ruptura iminente e `cancellations_rate` estiver prestes a sair de 0, qualquer experimento de expansão contamina a leitura e pode comprometer a elegibilidade para Platinum.

---

### Escalonamento

**observar** — com gatilho explícito para alinhar com Himmel e, em paralelo, sinalizar Kobe.

A conta não precisa de intervenção de ADS hoje: campanha eficiente, ROAS 12.2x, ACOS 5.74% — critério da Lente Tática 5 é inequívoco no sentido de não mexer. O risco real é operacional (rupturas Full + cancellations_rate), não de mídia paga, e é resolvido por Yasmin via abastecimento, não via Himmel. O gatilho para **alinhar com Himmel** é: health dos dois campeões com penalização cair abaixo de 0.68 em qualquer ciclo dos próximos 5 dias — aí Yasmin abre conversa sobre cobertura preventiva de ADS para compensar perda de exposição orgânica. O gatilho para **escalar para Kobe** é dual: (a) ADS share permanecer acima de 55% por 3 ciclos consecutivos adicionais com ROAS sustentado — dependência estrutural de mídia paga merece discussão de tese com Kobe; (b) `cancellations_rate` sair de 0 antes do fechamento do ciclo de elegibilidade para Platinum — risco que extrapola a decisão tática diária de Yasmin.