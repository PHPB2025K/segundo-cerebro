<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 13/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Total Shopee: R$ 5.964,55 — 119 pedidos — ticket médio R$ 50,12
- Budamix Store: R$ 3.285,11 — 75 pedidos
- Budamix Oficial (Conta 2): R$ 852,36 — 13 pedidos
- Budamix Shop (Conta 3): R$ 1.827,08 — 31 pedidos
- Cancelamentos: 9 no total (Store: 5 / Conta 2: 3 / Conta 3: 1)

🏆 TOP PRODUTOS SHOPEE
- Jarra Medidora de Vidro 500ml com Alça (Store) — 31 pedidos
- Kit 5 Potes de Vidro Redondos — 30 pedidos
- Canecas Tulipa 250ml Porcelana Colorida — 25 pedidos
- Kit 6 Canecas Porcelana 200ml (Conta 3) — 15 pedidos
- Kit 2 Potes Vidro 800ml Quadrado Hermético (Conta 3) — 10 pedidos

🔍 ANÁLISE DA CONTA
- O problema da Conta 2 (Budamix Oficial) não é queda de demanda — é combinação de colapso de volume com cancelamentos que apontam para bloqueio na execução. Investigar só a queda de pedidos não é suficiente: Lucas precisa identificar o que está gerando rejeição nessa conta especificamente. A leitura ainda é limitada porque o dado da Conta 2 está fora da banda de confiança — o diagnóstico é indicado pela combinação de evidências, mas não pode ser tratado como fato confirmado até amanhã.
- A queda de hoje não é de canal — é da Conta 2 especificamente: Store e Conta 3 ficaram dentro de seus padrões de erosão já esperada, enquanto a Conta 2 (que deveria responder por cerca de 28–30% do GMV) contribuiu com apenas 14%. Tratar como "dia fraco na Shopee" distorce a leitura e desvia o foco de onde o sinal está.
- Na Conta 3 (Budamix Shop), o volume segurou — mas o ticket caiu de R$ 71,75 (média do mesmo dia da semana) para R$ 58,94, com mix migrando para itens de valor menor. O GMV parece estável mas a qualidade do faturamento piorou. Se o ticket permanecer comprimido por mais 2 dias, não é variação do ciclo — é deriva de mix em curso.

🎯 PRIORIDADES DO DIA
- Lucas: investigar o que está gerando cancelamentos na Conta 2 (Budamix Oficial) — não apenas o volume baixo; a combinação com cancelamentos aponta para bloqueio na execução, não demanda fraca. Confirmar/refutar amanhã: mais de 20 pedidos com cancelamentos abaixo de 10% = anomalia pontual; menos de 15 pedidos ou cancelamentos acima de 15% novamente = padrão de bloqueio operacional. Escalar se Conta 2 ficar abaixo de 15 pedidos por 2 dias seguidos — Lucas alinha com Himmel para diagnóstico de exposição e ADS antes de qualquer movimentação.
- Lucas: verificar se os produtos campeões da Store (Jarra Medidora 500ml e Kit 5 Potes Redondos) e da Conta 3 (Kit 6 Canecas 200ml e Kit 2 Potes 800ml) estão com listing ativo e estoque disponível. Todos com listing ativo e estoque positivo = GMV atual é dinâmica de demanda, não problema operacional. Qualquer campeão com listing ou estoque comprometido = prioridade imediata antes de qualquer outra ação.
- Lucas: registrar o ticket médio da Conta 3 pelos próximos 3 dias. Ticket abaixo de R$ 62,00 por 3 dias seguidos = erosão de mix em curso, avaliar ajuste de exposição dos produtos de ticket maior. Ticket acima de R$ 65,00 em até 2 dias = variação do ciclo semanal, encerra observação.

Dia analisado: 13/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios de produto recebidos com nome explícito.
- Restrições recebidas da Condensadora foram editoriais (não nominais), tratadas nas Decisões de Formatação abaixo.

---

### Decisões de formatação

- `Remoção de metadados internos ("base: Operacional + Estratégica")` — regra do prompt: nomes de camadas não vão ao Slack; tese e termos analíticos preservados integralmente.
- `Ressalva do flag PARCIAL da Conta 2 preservada na Análise` — Condensadora marcou confiança ajustada; linguagem de indício usada ("a leitura ainda é limitada", "indicado pela combinação de evidências, mas não pode ser tratado como fato confirmado").
- `Taxa exata de cancelamento da Conta 2 omitida como manchete` — incorporada como contexto diagnóstico ("combinação de colapso de volume com cancelamentos"), conforme orientação da Condensadora.
- `Variações históricas percentuais omitidas da Análise e Visão` — Condensadora bloqueou percentuais históricos como dado central; diagnóstico sustentado pela tese, não pelos números.
- `Hipótese de canibalização (CTL002 entre contas) omitida` — Condensadora classificou como hipótese fraca sem dados de exposição por conta; não incluída.
- `Concentração top 3 (90%, 84%) não citada como métrica explícita` — Condensadora orientou usar apenas como enquadramento estrutural; mantida na forma de tese de risco nas prioridades, sem os percentuais.
- `Top Produtos: receita por produto omitida` — pacote de dados não contém faturamento por produto; itens listados por quantidade de pedidos. Nenhum dado inventado.
- `Top Produtos: Jarra Medidora 500ml com indicação (Store)` — vendeu exclusivamente na Store (1 conta); regra de indicação de conta aplicada.
- `Top Produtos: Kit 6 Canecas 200ml com indicação (Conta 3)` — vendeu nas 3 contas (Store: 1, Conta 2: 2, Conta 3: 12), mas Condensadora citou explicitamente como campeão da Conta 3 nas prioridades; indicação de conta aplicada por critério de relevância editorial.
- `Top Produtos: Kit 2 Potes Vidro 800ml com indicação (Conta 3)` — vendeu em 2 contas (Store: 1, Conta 3: 9), Conta 3 dominante e citada explicitamente pela Condensadora como campeão da conta.
- `Top Produtos: Kit 5 Potes Redondos consolidado de Store (IMB501P_T) + Conta 2 (IMB501C_T)` — SKUs ligeiramente distintos (_T vs _C no sufixo) mas produto equivalente (potes redondos vidro); consolidação aplicada; 2 contas, sem indicação de conta por regra.
- `Top Produtos: Canecas Tulipa 250ml sem indicação de conta` — vendeu nas 3 contas; sem indicação necessária por regra.
- `Generalização "Shopee caiu" não utilizada` — Condensadora bloqueou explicitamente; sinal localizado na Conta 2 preservado com especificidade.