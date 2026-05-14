<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 13/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 2.258,49
- Pedidos: 46
- Ticket médio: R$ 49,10
- Cancelamentos: 2
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Jarra Medidora de Vidro 500ml Resistente com Alça para Receitas — 13 unidades
- Conjunto de 5 Potes de Vidro Redondos (vermelho) — 12 unidades
- Jogo 6 Canequinha 100ml Caneca Café Suporte Madeira Alumínio — 8 unidades
- Kit 6 Canecas de Porcelana Tulipa 250ml Preto — 6 unidades
- Suporte de Controle PS5/PS4/Xbox Organizador de Mesa Gamer 2 em 1 — 6 unidades

🔍 ANÁLISE DA CONTA
- O dia foi genuinamente forte em volume e GMV, mas a leitura positiva é condicionada — a causa do spike não foi identificada e Buy Box e cobertura FBA dos ASINs líderes não foram validados; tratar hoje como novo patamar antes dessas checagens é o risco exato que as regras da conta buscam evitar.
- O mix não ficou mais distribuído do que o ranking de ASINs sugere — duas famílias de produto (Jarra Medidora e família Potes em quatro variações de cor) sustentam 53% do volume de itens do dia; a cauda existe mas é composta majoritariamente por variações da família líder, não por expansão real de base.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box e cobertura de estoque FBA da Jarra Medidora e da família Potes de Vidro, que juntos respondem por mais da metade do volume do dia. Sem essa validação, qualquer decisão sobre ADS fica bloqueada pelas regras da conta — escalar tráfego pago sem Buy Box estável nos líderes amplifica risco em vez de oportunidade. Confirmar por: Buy Box ≥ 85% nos dois produtos líderes com FBA sem alerta de estoque = pré-requisitos atendidos e conversa sobre ADS pode avançar após confirmação de volume por 2 ciclos. Abaixo disso, ADS pausa independentemente do resultado de hoje. Escalar se: Buy Box instável ou FBA com risco de ruptura nos líderes → sinalizar para Pedro antes de qualquer decisão de tráfego pago.
- Leonardo: identificar e registrar a causa do spike de ontem — promoção ativa, campanha ADS, mudança de listing ou boost algorítmico. Sem causa identificada, qualquer normalização de volume nos próximos dias fica sem âncora interpretativa — retorno ao baseline pode ser lido erroneamente como queda se hoje for tomado como nova referência. Confirmar por: causa documentada com data de início e escopo. Se promoção pontual: normalização esperada, não é alerta. Se orgânico ou boost de listing: acompanhar por 2 ciclos para classificar.

Dia analisado: 13/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios formais recebidos da Granular/Condensadora (bloqueios_para_slack vazio; risco de identificação classificado como baixo).
- Tratamento aplicado ao item "Hipótese sobre Suporte Gamer": produto aparece no Top Produtos com título real (ranking seguro, sem bloqueio), mas qualquer afirmação analítica sobre ele foi omitida da seção ANÁLISE DA CONTA conforme instrução explícita da Condensadora (confiança insuficiente por ausência de histórico).
- ASINs específicos não aparecem na mensagem final (instrução da Condensadora: "desnecessariamente granulares"; risco de identificação baixo, títulos suficientemente discriminantes).
- SKUs crus não aparecem.

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Tática + Granular`, `— base: Granular + Estratégica`) dos insights, mantendo a tese intacta.
- Confiança média preservada: insights escritos em tom condicionado, sem transformar hipótese em fato — "mas a leitura positiva é condicionada" e "a cauda existe mas é composta majoritariamente por variações da família líder" preservados integralmente.
- Top Produtos: exibidos individualmente por título real (fonte primária: pedido real com ASIN confirmado). Suporte Gamer incluído no ranking por ter pedidos reais identificados com risco baixo; sem análise sobre ele na seção ANÁLISE DA CONTA conforme Condensadora.
- ASIN omitido em todos os produtos — títulos são suficientemente discriminantes e risco de identificação é baixo; nenhum caso de ambiguidade de título para o mesmo produto.
- Métrica usada em Top Produtos: "unidades" em vez de "pedidos" — o campo quantity do pacote representa unidades vendidas por SKU, não contagem de pedidos; usar "pedidos" seria impreciso.
- Prioridades: texto preservado da Condensadora com remoção mínima de redundâncias de formato e substituição de "ASINs líderes" por "produtos líderes" onde o contexto já tornava claro quais produtos eram — mantendo a regra de não usar ASINs brutos no Slack.
- Sem seção DESTAQUES DO DIA, RESUMO GERAL, VENDAS POR CANAL — proibições estruturais respeitadas.
- Sem nome de Pedro Broglio no cabeçalho.
- Data confirmada em BRT: 13/05/2026.