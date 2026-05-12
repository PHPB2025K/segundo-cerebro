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

A análise deve conter:
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
