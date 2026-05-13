---
name: trader-daily-sales-account-analysis
description: Gera análise profunda diária por conta para o Daily Sales Report v2 do Trader. Use após data readiness e antes do Slack, para analisar Shopee por shop_id, Mercado Livre e Amazon com 30/60 dias, mesmo dia da semana, horários, SKUs, fulfillment, estoque, ADS/Himmel/Pedro, hipóteses, riscos e ações recomendadas.
---

# Trader — Daily Sales Account Analysis

## Objetivo
Transformar dados reais de cada conta em uma análise interna profunda, granular e útil. Esta análise é mais completa que o Slack e deve alimentar a memória do dia seguinte.

## Pré-requisitos
- Rodar `trader-daily-sales-data-readiness`.
- Rodar/seguir `trader-daily-sales-memory-cycle` para carregar o pacote de memória enxuto.
- Confirmar dia analisado em BRT.

## Unidade de análise
Analise sempre uma conta por vez:
- Shopee Budamix Store — `shop_id=448649947`
- Shopee Budamix Oficial / Conta 2 — `shop_id=860803675`
- Shopee Budamix Shop / Conta 3 — `shop_id=442066454`
- Mercado Livre — `platform=ml`
- Amazon — `platform=amazon`

## Métricas obrigatórias
Para cada conta:
- pedidos válidos;
- faturamento/GMV;
- ticket médio;
- itens vendidos;
- cancelamentos;
- top SKUs/produtos;
- concentração nos top SKUs;
- vendas por hora BRT;
- comparação 30 dias;
- comparação 60 dias;
- comparação com últimos 4 mesmos dias da semana;
- fulfillment: Shopee Full / Amazon FBA quando disponível.

## Heurísticas de leitura
Use como hipóteses, não como verdade absoluta:
- Pedidos caem e ticket preserva → possível tráfego/exposição/ADS.
- Ticket cai e pedidos preservam → possível mix de produto mais barato.
- Poucos SKUs concentram venda → risco de dependência.
- Muitos SKUs caem juntos → possível tráfego/plataforma/campanha.
- Amazon fraca com pedidos baixos → checar Buy Box, FBA, ADS, listing.
- Shopee/ML com queda de volume sem explicação operacional → ponto para Himmel.

## Contexto ADS
- Shopee e Mercado Livre: Himmel executa ADS. Recomendações devem virar checagens/alinhamentos com Himmel quando envolver campanha, exposição, verba, ACOS ou tráfego.
- Amazon: Pedro gere ADS. Separe o que Leonardo acompanha operacionalmente do que precisa ação de campanha do Pedro.

## Saída obrigatória
Salvar análise interna seguindo o template em:
`shared/trader/memory/projects/daily-sales-report/accounts/{slug}/daily/YYYY-MM-DD.md`

A análise deve conter obrigatoriamente as 5 camadas do **Daily Sales Analyst**:
1. **Camada Estratégica** — visão macro, tese da conta, risco estrutural, dependência e direcionamento de longo prazo.
2. **Camada Tática** — desdobramento em plano de médio prazo, ADS/Himmel/Pedro, mix, exposição, estoque/Full/FBA/Buy Box.
3. **Camada Operacional** — execução do dia, pedidos, GMV, ticket, cancelamentos, horários e comparativos.
4. **Camada Granular** — produtos, SKUs, ASIN/título real, shop_id, concentração, fulfillment e microanomalias.
5. **Camada Condensadora** — consome as 4 camadas anteriores, resolve conflitos, separa fato de hipótese e produz a análise final para memória e Slack.

A Camada Condensadora deve entregar:
- análise final condensada;
- prioridades condensadas para Slack;
- hipótese mais provável;
- por que importa;
- como confirmar/refutar amanhã.

A análise também deve conter:
- hipóteses anteriores lidas;
- hipóteses confirmadas/refutadas;
- novas hipóteses;
- riscos;
- ação recomendada;
- o que observar amanhã;
- observações para Kobe/Pedro se houver.

## Nunca fazer
- Não inventar causa sem evidência.
- Não chamar hipótese de conclusão.
- Não usar Shopee consolidada para decisão por conta.
- Não recomendar preço/margem sem fonte de custo confiável.
- Não enviar Slack nesta etapa.
- Não deixar o Slack consumir diagnóstico hardcoded/legado quando a Camada Condensadora existir.
- Não permitir envio real se a análise diária não tiver as 5 camadas ou se a Condensadora estiver rasa.

## Régua mínima de análise sênior (obrigatória)
Uma análise só é aceitável se responder, para cada conta:
1. **O que mudou?** Comparar contra 30d, 60d e últimos 4 mesmos dias da semana; não usar uma única comparação isolada.
2. **Onde mudou?** Separar efeito de pedidos, ticket, mix, concentração de produto, horário, cancelamento e fulfillment.
3. **Por que isso importa?** Explicar impacto operacional: tráfego, exposição, estoque, sortimento, Buy Box/FBA, campanha ou risco de dependência.
4. **Qual hipótese é mais provável?** Declarar como hipótese quando não houver prova; nunca vender hipótese como fato.
5. **Como confirmar/refutar amanhã?** Definir sinal observável: volume até certo horário, recuperação de SKU/produto, cancelamento, FBA/Full, ranking, Buy Box ou tráfego.

## Profundidade por plataforma
- **Shopee:** sempre comparar as 3 contas entre si; identificar se o problema é geral da Shopee ou concentrado em uma conta. Ler concentração de mix como risco real: se top 3 >70%, explicar qual produto sustenta a conta e o que acontece se ele perder tração.
- **Mercado Livre:** diferenciar queda leve normal de perda de exposição. Se 30d e 60d apontarem leituras opostas, explicar a nuance em vez de simplificar.
- **Amazon:** separar cancelamento, FBA, Buy Box, listing e ADS. Quando cancelamento >10%, isso vira investigação operacional obrigatória, mesmo que GMV esteja acima da média.

## Produto visível
- A análise interna pode guardar SKU, mas qualquer trecho destinado ao Slack/preview deve usar nome comercial.
- Se só houver SKU, converter via mapeamento canônico; se não houver nome confiável, buscar título nos itens do pedido. SKU cru é falha de qualidade.

