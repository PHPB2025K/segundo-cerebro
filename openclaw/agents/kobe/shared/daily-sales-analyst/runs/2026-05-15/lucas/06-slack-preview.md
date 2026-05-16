<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 15/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Consolidado Shopee: 110 pedidos — R$ 5.976,19 — ticket médio R$ 54,33 — 6 cancelamentos
- Budamix Store: 66 pedidos — R$ 3.171,67
- Budamix Oficial / Conta 2: 17 pedidos — R$ 1.248,10
- Budamix Shop / Conta 3: 27 pedidos — R$ 1.556,42

🏆 TOP PRODUTOS SHOPEE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta (Budamix Store) — 30 pedidos
- Jarra Medidora de Vidro 500ml (Budamix Store) — 23 pedidos
- Kit 6 Canecas Tulipa 250ml — 20 pedidos
- Kit 6 Canecas Retas 200ml (Conta 3) — 8 pedidos
- Kit 2 Potes de Vidro 800ml Quadrado — 6 pedidos
- Kit 4 Potes de Vidro 800ml Quadrado — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 4 pedidos
- Kit 3 Potes de Vidro Hermético — 4 pedidos
- Kit 6 Potes de Vidro Hermético (Budamix Store) — 3 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee do dia não é uma plataforma — são três dinâmicas opostas que somam R$ 5.976,19 sem revelar os riscos individuais: a Store sustenta o GMV via ticket elevado com cauda inexistente, a Oficial-2 está com tráfego ausente apesar dos listings ativos, e a Shop-3 entrega volume estável enquanto o valor por pedido erode silenciosamente por drift de mix; tratar o consolidado como sinal de saúde seria o erro do dia.

🟠 *Budamix Store (Shopee 1):* A conta carregou R$ 3.171,67 com 66 pedidos porque o ticket subiu (+24% vs 30d), não porque vendeu mais — os dois campeões, Conjunto 5 Potes de Vidro Redondos Tampa Preta (30 pedidos, 45,5%) e Jarra Medidora de Vidro 500ml (23 pedidos, 34,8%), responderam por 80,3% da conta e o top 5 cobriu literalmente 100% dos pedidos do dia, confirmando que a cauda não existe operacionalmente; qualquer interrupção nesses dois produtos por estoque, ranking ou ADS não encontra absorção nenhuma no restante da conta.

🟠 *Budamix Oficial (Shopee 2):* Com 17 pedidos — piso absoluto de todas as quintas-feiras registradas (série: 26→33→43→39→17) — foi confirmado que os listings dos principais produtos estavam ativos e convertendo por pedido real, descartando bloqueio operacional como causa; o que o dia descreveu foi ausência de tráfego: zero cancelamentos e distribuição horária rarefeita ao longo de todo o dia apontam que visitantes simplesmente não chegaram, e a ação correta não é checar listing — é alinhar com Himmel sobre exposição e configuração de campanha.

🟠 *Budamix Shop (Shopee 3):* Os 27 pedidos — exatamente na média de 30d — mascaram a deterioração real: o dia foi dominado por Kit 6 Canecas Tulipa 250ml e Kit 6 Canecas Retas 200ml empatados em 8 pedidos cada (59% da conta), enquanto potes herméticos caíram para a cauda, produzindo GMV -15,2% vs série de mesmos dias sem queda de volume; o comprador chegou e converteu, mas converteu na categoria de menor valor — o número de pedidos parece saudável enquanto a receita por pedido erode progressivamente.

🎯 PRIORIDADES DO DIA
- Lucas: alinhar com Himmel sobre exposição e configuração de campanha da Budamix Oficial / Conta 2. Os listings dos produtos principais estavam ativos — a causa da queda não é operacional. Confirmar/refutar: Oficial-2 acima de 25 pedidos amanhã com distribuição horária normalizada indica problema pontual; abaixo de 20 pelo segundo dia consecutivo com listings ativos confirma deterioração estrutural de tráfego. Escalar se: Oficial-2 fechar abaixo de 20 pedidos amanhã com listings confirmados ativos.
- Lucas: observar composição de mix da Budamix Shop / Conta 3 nos próximos 3 dias. Kit 6 Canecas Tulipa 250ml e Kit 6 Canecas Retas 200ml dominaram o dia com 59% dos pedidos, explicando a erosão de GMV por pedido. Confirmar/refutar: canecas no topo por mais 2 dias consecutivos confirma drift estrutural de mix e vira intervenção de exposição; potes herméticos retornando ao topo reverte a hipótese.
- Lucas: verificar posição e visibilidade de Conjunto 5 Potes de Vidro Redondos Tampa Preta e Jarra Medidora de Vidro 500ml na Budamix Store nos horários de pico noturno (19h–23h). Os dois carregam 80,3% da conta sem cauda de absorção. Confirmar/refutar: posição estável e pedidos chegando no turno noturno indica risco monitorado; posição degradada requer alinhamento com Himmel antes da próxima sessão.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKU 098 — Oficial-2 (display_name "Pote de Vidro Hermético 800ml")
- Origem do bloqueio: Granular + Condensadora
- Motivo: mismatch material entre raw_title ("Kit 9 Potes Vidro Quadrados Hermético Vedação Tampa 4 Travas Marmita") e display_name — produtos incompatíveis na descrição; risco real de identificação errada
- Agregado autorizado: não
- Tratamento aplicado: omitido; produto com 1 pedido, na cauda da Oficial-2; nenhum agregado inventado
- Aparece na mensagem final: não

---

- Item bloqueado: SKU 096 — Shop-3
- Origem do bloqueio: Granular + Condensadora
- Motivo: confidence medium por mapping_reason "raw_sku_normalized_with_short_title_fallback"; SKU numérico genérico sem informação semântica
- Agregado autorizado: não
- Tratamento aplicado: omitido; 1 pedido, cauda da Shop-3
- Aparece na mensagem final: não

---

- Item bloqueado: ITEM:28044349447 — Shop-3
- Origem do bloqueio: Granular + Condensadora
- Motivo: raw_sku ausente; mapeado exclusivamente por platform_item_id estável; confidence medium
- Agregado autorizado: não
- Tratamento aplicado: omitido; 1 pedido, cauda da Shop-3
- Aparece na mensagem final: não

---

### Decisões de formatação

- Substituição de SKUs crus na análise por display_names — IMB501P → "Conjunto 5 Potes de Vidro Redondos Tampa Preta", CK4742 → "Jarra Medidora de Vidro 500ml", CTL002 → "Kit 6 Canecas Tulipa 250ml", KIT6CAR200 → "Kit 6 Canecas Retas 200ml"; regra proíbe SKU cru visível no Slack
- Correção de formatação numérica — "R$5.976" → "R$ 5.976,19" e "R$3.172" → "R$ 3.171,67" conforme padrão obrigatório (ponto milhar, vírgula decimal, 2 casas)
- Título da seção de análise definido como "🔍 ANÁLISE DAS CONTAS" — presença do 06b-shopee-consolidator ativa o título expandido conforme addendum v3.1
- Faturamento por produto omitido no TOP PRODUTOS — campo de receita individual ausente no pacote de dados (top_products contém apenas orders e quantity); não inventado
- Conta indicada nos produtos com venda em menos de 2 contas: "Budamix Store" para IMB501P e CK4742; "Conta 3" para KIT6CAR200; "Conta 2" para IMB501C
- KIT3S099 (Kit 3 Potes de Vidro Hermético) — vendeu em Oficial-2 (2) e Shop-3 (2), 4 pedidos consolidados em 2 contas; sem indicação de conta específica
- Hipótese de canibalização CTL002 cross-conta — documentada internamente pela Condensadora como "não confirmada como impacto real"; não incluída no Slack
- Agrupamento de 4 pedidos às 23h na Oficial-2 — não citado; Condensadora marcou como bloqueado por ausência de histórico horário para confirmar recorrência
- Taxa de cancelamento da Shop-3 (~11%) — não citada; Condensadora bloqueou por ausência de breakdown granular por produto; citar taxa sem base seria especulação
- Prioridades da 06b preservadas com estrutura ação + evidência + sinal de confirmação/refutação + gatilho de escalonamento quando presentes na fonte