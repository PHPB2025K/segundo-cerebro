<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 10/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 8.063,87
- Pedidos: 185
- Ticket médio: R$ 43,59
- Cancelamentos: 8

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 67 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 23 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 22 pedidos
- Kit 4 Potes 1050ml — 12 pedidos
- Kit 6 Canequinhas 100ml — Madeira — 8 pedidos

🔍 ANÁLISE DA CONTA
- O Kit 6 Canecas Lisas 200ml fechou o dia no Catálogo Premium com 5 unidades em Full e 7 pedidos — a pausa antes do próximo snapshot é cenário provável. Como é o único anúncio Premium do topo, pausar significa perder o Buy Box do Catálogo Premium, e recuperar essa posição demora mais do que em qualquer anúncio Clássico.
- Não é só um Catálogo em risco — são três Full que podem pausar numa janela de 72 horas: o Kit 6 Canecas Lisas 200ml, o Kit 6 Canecas Tulipa 250ml (14 un, ~2,8 dias) e o Kit 2 Potes 800ml — Quadrado (12 un, ~3 dias). Essa combinação ainda não aconteceu na série. Ruptura em Full vira cancelamento automático — e é o único vetor que pode tirar a taxa oficial de cancelamento de zero e ameaçar o MercadoLíder Platinum recém-consolidado.
- A composição da modalidade de envio do dia ficou em 61% Full — contra 80% dos últimos 30 dias. Mas não é reversão do canal: os Potes Vidro 5 Peças — Tampa Cinza operam em Cross-Docking, assim como o Kit 6 Canequinhas 100ml — Madeira e o Kit 10 Potes 520ml. Os três juntos explicam toda a diferença — a proporção histórica de Full segue intacta.

🎯 PRIORIDADES DO DIA
- Yasmin: confirmar se há reposição em trânsito ou prazo estimado de chegada ao CD do ML para o Kit 6 Canecas Lisas 200ml (Catálogo Premium em Full, 5 unidades com 7 pedidos/dia). Sem prazo confirmado em 24h, o anúncio pausa, perde o Buy Box do único Catálogo Premium da conta e ativa cancelamento automático — o que pode tirar a taxa oficial de cancelamento de zero e ameaçar o MercadoLíder Platinum. Confirmar/refutar por: prazo confirmado em ≤24h = risco neutralizado; sem prazo ou anúncio pausado no próximo snapshot = ruptura iniciada. Escalar se: anúncio pausar antes da reposição e taxa oficial de cancelamento sair de zero em 2 snapshots consecutivos — Yasmin alinha com Kobe sobre cadenciamento de restock vs ritmo de vendas.
- Yasmin: verificar o prazo estimado de reposição em Full para o Kit 6 Canecas Tulipa 250ml (14 un, ~2,8 dias) e o Kit 2 Potes 800ml — Quadrado (12 un, ~3 dias). O histórico recente mostra reposições chegando insuficientes para o novo ritmo de vendas — e os três Catálogos Full pausando juntos é a situação mais delicada da conta. Confirmar/refutar por: prazo dentro do tempo de cobertura para os dois = risco monitorado; sem prazo para qualquer um = maior chance de pausas concentradas nas próximas 72 horas. Escalar se: não aplicável hoje — sobe junto com a prioridade acima se a taxa oficial de cancelamento sair de zero.
- Yasmin: registrar que o ADS respondeu por 59,7% do faturamento ontem (R$ 4.813,22 de R$ 8.063,87, ACOS 12,1%) — primeiro ponto acima de 55% em dia de faturamento forte. Isso suspende, sem refutar, a série descendente dos últimos 9 dias. Os próximos 2 ciclos vão dizer se foi desvio pontual ou reversão. Confirmar/refutar por: fatia abaixo de 50% em 2 ciclos = desvio pontual e série orgânica retoma; fatia acima de 55% com ACOS acima de 10% por mais 2 ciclos = Yasmin alinha com Himmel sobre composição da campanha. Escalar se: subordinado ao risco de estoque — só acionar Himmel depois que os Catálogos Full estiverem fora de zona crítica.

Dia analisado: 10/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos. `o_que_nao_pode_ir_para_slack` da L05 está vazio. A L04 declarou `bloqueios_para_slack: []` e `risco_identificacao: baixo`. Nenhum item foi omitido ou substituído por agregado.

---

### Decisões de formatação

**Remoção de metadados internos**
- Campos `padrao`, `base` e `classificacao` dos 3 insights da L05 omitidos — são metadados de pipeline, não vão para Slack.

**Preservação de nuance por classificação**
- Insights 1 e 2 classificados como `risco latente` — redigidos com linguagem prospectiva e condicional: "cenário provável", "podem pausar", "pode tirar", "pode ameaçar". Não convertidos para afirmações categóricas.
- Insight 3 classificado como `fato` — redigido em afirmação direta, sem hedge.

**Alerta de confiança**
- `alertas_de_confianca.nivel == "alta"` — sem restrições adicionais de tom ou corte de insight. Todos os 3 insights e 3 prioridades incluídos.

**Tradução de nomes de produto — Top Produtos (5 primeiros)**
- IMB501P → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- IMB501C → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- IMB501V → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- KIT4YW1050 → usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico)
- 914C → usado `slack_short_name` "Kit 6 Canequinhas 100ml — Madeira" (mapeamento canônico)

**Tradução de nomes de produto — Análise da Conta e Prioridades do Dia**
- CLR002: L05 escreveu "Kit 6 Canecas de Porcelana Lisa Reta para Chá e Café Colorida 200ml" → L06 usou "Kit 6 Canecas Lisas 200ml" (`slack_short_name`, mapeamento canônico). Divergência de denominação cross-layer registrada.
- TL6250: L05 escreveu "Kit 6 Canecas Tulipa Coloridas de Porcelana 250ml" → L06 usou "Kit 6 Canecas Tulipa 250ml" (`slack_short_name`, mapeamento canônico). Divergência registrada.
- KIT2YW800SQ: L05 escreveu "2 Potes Vidro Marmita Tampa Hermética 800ml Verde" → L06 usou "Kit 2 Potes 800ml — Quadrado" (`slack_short_name`, mapeamento canônico). Divergência registrada.
- IMB501C: L05 escreveu "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças Cinza" → L06 usou "Potes Vidro 5 Peças — Tampa Cinza" (`slack_short_name`, mapeamento canônico). Divergência registrada.
- 914C: L05 escreveu "Canequinhas em Madeira" → L06 usou "Kit 6 Canequinhas 100ml — Madeira" (`slack_short_name`, mapeamento canônico). Divergência registrada.
- KIT10YW520: L05 escreveu "Kit 10 Potes 520ml" → L06 usou "Kit 10 Potes 520ml" (`slack_short_name`, mapeamento canônico). Sem divergência.

**Produto KIT4YW640 (Kit 4 Potes 640ml, slack_short_name=null)**
- Não aparece no Top 5 visível (é o 7º) nem é citado nos insights ou prioridades da L05. Fallback para `display_short` não foi necessário. Item sem tratamento ativo na mensagem.

**Consolidação de variações no Top Produtos**
- Cluster IMB501 exibido por variação (Tampa Preta / Tampa Cinza / Tampa Vermelha) em anúncios distintos — Tampa Preta e Tampa Vermelha compartilham MLB3288536143 (Full), Tampa Cinza opera em MLB4535865311 separado (Cross-Docking). Cada variação com seu volume próprio; não consolidado em família.

**Modalidade de envio omitida da VISÃO**
- `fulfillment_mix_yesterday_top10` cobre apenas os top 10 (93 de 185 pedidos = ~50%). A L05 não autorizou exibição com cobertura explícita na VISÃO. Omitido — modalidade de envio tratada somente na ANÁLISE DA CONTA (insight 3), onde a L05 trouxe o dado com contexto analítico.

**Substituições de glossário aplicadas**
- "ADS share" → "ADS respondeu por 59,7% do faturamento" (regra: nunca "ADS share" no Slack)
- "ETA" → "prazo estimado de chegada" / "prazo estimado de reposição"
- "runway" → "tempo de cobertura" / "prazo dentro do tempo de cobertura"
- "mix (fulfillment)" → "composição da modalidade de envio"
- "GMV" → "faturamento" (regra absoluta)
- "ACOS 12,12%" → "ACOS 12,1%" (regra de 1 casa decimal para percentuais)

**Atribuição de responsável**
- Yasmin atribuída como responsável nas 3 prioridades — L05 não atribui responsável; L06 aplica regra fixa (Mercado Livre é de Yasmin).

**Estrutura da mensagem**
- 6 seções obrigatórias presentes na ordem correta.
- Linha em branco entre seções; bullets sem linha em branco entre si.
- Sem Pedro Broglio no topo, sem DESTAQUES DO DIA, sem RESUMO GERAL, sem VENDAS POR CANAL, sem referência a outras plataformas.
- Nenhum MLB, SKU ou ID técnico visível na mensagem.