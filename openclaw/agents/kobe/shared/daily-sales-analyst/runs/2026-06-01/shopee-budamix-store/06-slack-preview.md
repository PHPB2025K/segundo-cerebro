<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 01/06/2026 (Ontem)

📊 VISÃO SHOPEE
- Total Shopee: 96 pedidos — R$ 4.379,34 — ticket médio R$ 45,62
- Cancelamentos: 16
- Budamix Store: 68 pedidos — R$ 3.092,25
- Budamix Oficial (Conta 2): 17 pedidos
- Budamix Shop (Conta 3): 11 pedidos

🏆 TOP PRODUTOS SHOPEE
- Jarra Medidora de Vidro 500ml (Store) — 19 pedidos
- Kit 6 Canecas Tulipa 250ml (Store) — 15 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 15 pedidos
- Pote de Vidro Hermético 520ml Tampa 4 Travas (Store) — 5 pedidos
- Kit 2 Potes de Vidro 800ml Quadrado (Store) — 4 pedidos
- Kit 2 4 6 10 Potes Herméticos Vidro Quadrado 800ml (Store) — 2 pedidos
- Kit 4 Potes Vidro 520ml Quadrado Hermético Fitness (Store) — 2 pedidos
- Kit 6 Potes de Vidro Hermético (Store) — 1 pedido
- Kit 4 Descanso de Panela Modular MDF 6mm (Store) — 1 pedido
- Kit 2 Potes de Vidro 320ml Retangular (Store) — 1 pedido

🔍 ANÁLISE DA CONTA
- A Budamix Store fez R$ 3.092,25 no dia, mas o resultado veio quase todo de 3 produtos que aparecem sem estoque no mesmo snapshot — o dia parece bom, mas a base que sustentou esse número já estava sinalizando ruptura.
- A ruptura é mais ampla do que só os 3 campeões: 6 dos top 10 do dia estão marcados como sem estoque, cobrindo cerca de 78% dos pedidos. Sobram apenas 4 SKUs com venda hoje, todos da mesma família de potes quadrados — não há cauda nem segundo vetor para amortecer.
- O ticket subiu (R$ 45,47 vs R$ 39,51 do bimestre) e segurou o GMV mesmo com volume menor, mas isso é proteção frágil: depende do mix atual seguir disponível. Se os campeões não voltarem ao estoque em 24–48h, o patamar não se sustenta nos próximos dias.

🎯 PRIORIDADES DO DIA
- Lucas: confirmar no Seller Center o status de estoque dos 6 SKUs que venderam no top do dia e aparecem sem estoque no snapshot — não limitar a checagem aos 3 campeões. Os 6 cobriram cerca de 78% dos pedidos de ontem; recompor só os líderes deixa buraco real. Confirmar/refutar por: snapshot de 06/02 e 06/03 com os SKUs recompostos. Escalar se: OOS nos campeões persistir amanhã — suspender qualquer alinhamento de ADS com Himmel até normalizar.
- Lucas: acompanhar o GMV da Store nas próximas 48h com leitura no fim do dia. O patamar de R$ 3.092,25 depende dos campeões disponíveis; a cauda de 4 SKUs não absorve a queda. Confirmar impacto: GMV abaixo de R$ 2.000,00 em qualquer dos próximos 2 dias. Risco pontual: GMV acima de R$ 2.500,00 com estoque recomposto. Escalar se: GMV cair abaixo de R$ 2.000,00 mesmo com estoque recomposto — alinhar com Himmel sobre exposição.
- Lucas: registrar se o padrão de 68% dos listings ativos sem estoque é pontual ou recorrente na conta. Se recorrente, o problema extrapola a decisão de canal. Confirmar por: comparar snapshots dos próximos 3 dias. Escalar para Kobe se: OOS amplo se confirmar como padrão recorrente.

Dia analisado: 01/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

**Bloqueios recebidos via Condensadora (o_que_nao_pode_ir_para_slack):**

- Item bloqueado: formulação "ruptura só dos 3 campeões"
  - Origem do bloqueio: Condensadora
  - Motivo: Granular demonstrou que são 6 SKUs do top do dia, não apenas 3; subdimensionaria o risco
  - Agregado autorizado: sim — "6 dos top 10 do dia"
  - Tratamento aplicado: substituído por "6 dos top 10 do dia estão marcados como sem estoque, cobrindo cerca de 78% dos pedidos"
  - Aparece na mensagem final: sim, como agregado autorizado

- Item bloqueado: formulação "cauda saudável" ou "segundo vetor disponível"
  - Origem do bloqueio: Condensadora
  - Motivo: Granular confirmou que a cauda viva é estreita (4 SKUs, mesma família); afirmar segundo vetor seria inverter a tese
  - Agregado autorizado: sim — "não há cauda nem segundo vetor para amortecer"
  - Tratamento aplicado: incorporado literalmente na análise
  - Aparece na mensagem final: sim, como formulação negativa autorizada

- Item bloqueado: canibalização nominal do Kit 6 Canecas Tulipa (CTL002) com Budamix Oficial e Budamix Shop
  - Origem do bloqueio: Condensadora
  - Motivo: cruzamento entre contas é função exclusiva da L06b Consolidadora; citar na análise isolada da Store seria antecipar diagnóstico de canal errado
  - Agregado autorizado: não
  - Tratamento aplicado: omitido integralmente da mensagem
  - Aparece na mensagem final: não

- Item bloqueado: interpretação do GMV de R$ 3.092,25 como recuperação de tendência
  - Origem do bloqueio: Condensadora
  - Motivo: base de 30d deprimida, memória com lacuna de 12 dias, base de comparação fraca — leitura positiva não sustentada
  - Agregado autorizado: não
  - Tratamento aplicado: omitido; análise posiciona o GMV como resultado dependente de campeões OOS, não como reversão
  - Aparece na mensagem final: não

- Item bloqueado: acionamento de Himmel/ADS sem confirmação de estoque
  - Origem do bloqueio: Condensadora + Tática
  - Motivo: tráfego pago sobre produto indisponível queima verba e prejudica ranking
  - Agregado autorizado: sim — condição explícita nas prioridades
  - Tratamento aplicado: prioridade 1 condiciona alinhamento com Himmel à normalização do estoque
  - Aparece na mensagem final: sim, como condição de escalonamento

**Bloqueios de identificação de produto (Granular):**
- Sem bloqueios de produto recebidos. Granular declarou risco de identificação "baixo" e ausência de BLOQUEIO PARA SLACK.

---

### Decisões de formatação

- Remoção de metadados "— base: Estratégica + Operacional + Granular" e variantes de todos os insights da Condensadora — metadados internos de pipeline; não pertencem ao Slack
- Valores monetários dos insights substituídos pelas versões precisas do pacote validado: R$45 → R$ 45,47 (ticket do dia); R$40 → R$ 39,51 (avg_60d ticket / "bimestre") — aplicação do padrão numérico obrigatório sem alterar a comparação nem a tese da Condensadora
- Conta indicada em todos os 10 produtos do TOP PRODUTOS como "(Store)" — todos venderam em menos de 2 contas confirmadas no pacote; dados de Conta 2 e Conta 3 por produto não estavam disponíveis
- Faturamento de Budamix Oficial (Conta 2) e Budamix Shop (Conta 3) omitido na seção VISÃO SHOPEE — não disponível no pacote do dia; apenas pedidos derivados do volume_band check constam; omissão registrada para QA
- Layout de 4 blocos da 6B (⚫ Consolidado + 🟠 por conta) não aplicado — 06b-shopee-consolidator não foi entregue neste pacote; usado formato padrão de análise com os 3 insights da 05-condensadora (Store isolada)
- Título da seção mantido como "🔍 ANÁLISE DA CONTA" (singular) — uso de "ANÁLISE DAS CONTAS" e bloco consolidado é exclusivo quando a 6B existe
- Todos os 10 itens do top_products incluídos no ranking em ordem decrescente — pacote entrega ranking validado completo; itens com confidence medium (KITYW800, KIT4YW520SQ, DPM002) incluídos pois Granular declarou risco "baixo" e sem BLOQUEIO PARA SLACK; presença da cauda OOS é analiticamente relevante no contexto da ruptura
- Display name de DPM002 encurtado para "Kit 4 Descanso de Panela Modular MDF 6mm" — nome completo no pacote excede 60 caracteres com termos redundantes para Slack; encurtamento não altera identidade do produto
- Faturamento por produto não incluído no TOP PRODUTOS — pacote não entrega campo de receita validado por variação; proibido calcular ou estimar por ticket médio