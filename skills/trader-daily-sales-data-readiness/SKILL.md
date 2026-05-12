---
name: trader-daily-sales-data-readiness
description: Valida completude e confiabilidade dos dados antes do Daily Sales Report v2 do Trader. Use no início do cron diário, previews, auditorias ou quando houver suspeita de lacuna/divergência em orders, v_daily_sales, Shopee shop_id, Mercado Livre, Amazon, timezone BRT, status cancelado ou dados parciais.
---

# Trader — Daily Sales Data Readiness

## Objetivo
Garantir que os dados do dia analisado estão completos e confiáveis antes de qualquer análise ou mensagem Slack.

## Ordem obrigatória
1. Definir o dia analisado em BRT: 00:00–23:59.
2. Validar `v_daily_sales` para resumo geral por plataforma.
3. Validar `orders` para análise granular por conta.
4. Confirmar as 5 unidades operacionais:
   - Shopee `shop_id=448649947`
   - Shopee `shop_id=860803675`
   - Shopee `shop_id=442066454`
   - Mercado Livre (`platform=ml`)
   - Amazon (`platform=amazon`)
5. Excluir cancelados; nunca misturar venda gerada com settlement/extrato/DRE.
6. Se qualquer fonte estiver incompleta, marcar parcial e não estimar.

## Checks mínimos
- Contagem de pedidos por plataforma e por conta.
- Receita por plataforma e por conta.
- Presença de `order_date`, `status`, `items`, `total_amount`.
- Conversão correta para BRT.
- Shopee separada por `shop_id`, nunca consolidada para análise por conta.
- Amazon sem pedidos de remoção FBA ativos como venda.
- `v_daily_sales` usado só para resumo geral, não para Shopee por conta.

## Resultado esperado
Produzir um status claro:
- `DADOS_OK`: pode analisar.
- `DADOS_PARCIAIS`: pode analisar com ressalva explícita.
- `BLOQUEADO`: não gerar report; escalar para Kobe.

## Escalonar para Kobe
Escalar se:
- alguma conta ficou sem dados quando historicamente deveria ter;
- `v_daily_sales` diverge muito de `orders`;
- Shopee não separa por conta;
- timezone parece deslocado;
- Amazon tem pedidos suspeitos de FBA removal ativos;
- falta dado suficiente para recomendação acionável.
