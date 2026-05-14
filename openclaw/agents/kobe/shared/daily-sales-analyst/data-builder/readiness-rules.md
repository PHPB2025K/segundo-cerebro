# Regras de Data Readiness — Layer 0

## DADOS_OK

Condições (todas devem ser verdadeiras):

- Todas as fontes necessárias sincronizadas nas últimas 4h (quando métrica de sync existir)
- Volume dentro da banda 30d: entre -40% e +40% da média
- Zero divergências críticas detectadas
- Timezone BRT validado (janela 00:00-23:59 America/Sao_Paulo)
- Fonte canônica (orders BRT) disponível para todas as plataformas
- Shopee separada corretamente por `shop_id` (3 contas distintas)
- Amazon com identificação segura por pedido real (ASIN/título) quando produtos forem citados

Resultado: `data_quality = ok`, pipeline pode rodar normalmente.

## DADOS_PARCIAIS

Condição quando uma ou mais ocorrerem:

- Uma fonte com latência entre 4h e 8h
- Volume fora da banda 30d, inclusive spike positivo forte, desde que não indique quebra crítica de extração
- Queda fora da banda 60d, mas ainda acima do piso crítico de 30% da média 30d
- Divergência menor entre fontes (<5%)
- Dado secundário ausente sem comprometer totais principais

Resultado: `data_quality = partial`, pipeline pode rodar com ressalva.

## NOT_READY

Condição quando uma ou mais ocorrerem:

- Fonte canônica indisponível (plataforma ausente do canonical)
- Timezone incorreto ou janela BRT inconsistente
- Divergência crítica >10% entre fontes
- Volume abaixo de 30% da média 30d sem explicação operacional (queda crítica; `pct_change < -70%`)
- Falha na separação Shopee por `shop_id`
- Pacote sem pedido real suficiente para citar produto (Amazon sem ASIN/título)
- Erro sistêmico de sync, banco ou extração

Resultado: `data_quality = not_ready`, bloqueia execução, Trader não chama camadas analíticas.

## Observação

Quando métrica de sync/frescura não existir no banco, o check é registrado como `not_measured`. O readiness é conservador mas não bloqueia por métrica inexistente se o restante do pacote estiver consistente.

## Thresholds

| Parâmetro | Valor | Nota |
|-----------|-------|------|
| Banda 30d | -40% a +40% | |
| Banda 60d | -60% a +60% | Referência contextual; fora dela não bloqueia sozinho se acima do piso crítico |
| Spike positivo | >+40% vs média 30d | DADOS_PARCIAIS; não bloqueia sozinho |
| Volume crítico | <30% da média 30d (`pct_change < -70%`) | NOT_READY |
| Divergência menor | <5% | DADOS_PARCIAIS |
| Divergência crítica | >10% | NOT_READY |
| Sync freshness | 4h (ok), 4-8h (parcial), >8h (fail) | Quando mensurável |

Thresholds podem ser calibrados na Fase 5 com dados reais.
