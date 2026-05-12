---
name: trader-daily-sales-qa-escalation
description: QA e escalonamento do Daily Sales Report v2 do Trader. Use antes de finalizar preview/envio, quando houver dado incompleto, análise genérica, divergência, falha de Slack, risco operacional, queda recorrente, mudança de regra/taxa, hipótese estratégica ou necessidade de avisar Kobe/Pedro.
---

# Trader — Daily Sales QA & Escalation

## Objetivo
Impedir que relatórios ruins, incompletos ou perigosamente confiantes sejam enviados. Escalar para Kobe quando houver risco, divergência ou decisão estratégica.

## QA obrigatório
Antes de considerar o ciclo diário concluído:

1. Dados validados por `trader-daily-sales-data-readiness`.
2. Todas as 5 contas analisadas ou marcadas como parcial.
3. Análise interna salva antes do Slack.
4. Mensagens individuais geradas para Lucas/Yasmin/Leonardo.
5. Resumo geral igual e consistente nas 3 mensagens.
6. Sem Atacado/Bling.
7. Tudo em bullets.
8. Hipóteses claramente marcadas como hipóteses.
9. Ações recomendadas são específicas e executáveis.
10. Cópia do enviado/preview registrada.

## Sinais de baixa qualidade
Revisar ou bloquear se houver:
- “acompanhar” sem dizer o quê;
- análise que poderia valer para qualquer plataforma;
- Shopee consolidada sem conta;
- recomendação de ADS sem indicar Himmel/Pedro;
- recomendação de preço/margem sem custo confiável;
- números sem fonte;
- conclusão causal sem evidência;
- mensagem longa, mas sem ação.

## Quando marcar parcial
- Uma conta ou plataforma sem dados confiáveis.
- API/tabela com lacuna.
- Timezone suspeito.
- Status de pedidos inconsistente.
- Separação Shopee por `shop_id` falhou.

Mensagem parcial deve dizer o que falta e não estimar.

## Escalonar para Kobe/Pedro
Escalar quando:
- falha de envio Slack;
- dados incompletos relevantes;
- divergência grande entre `v_daily_sales` e `orders`;
- queda forte recorrente sem explicação;
- risco de ruptura relevante;
- mudança de regra/taxa com impacto comercial;
- hipótese que envolve cobrança da Himmel;
- recomendação exige decisão estratégica;
- Amazon requer ação de ADS do Pedro.

## Formato do alerta para Kobe
- O que aconteceu.
- Conta/plataforma afetada.
- Evidência numérica.
- Impacto provável.
- O que já foi feito.
- Decisão/ação necessária.

## Nunca fazer
- Não enviar report “normal” se o status é bloqueado.
- Não esconder lacuna de dados.
- Não prometer conclusão onde há hipótese.
- Não mandar funcionário agir com base em dado suspeito.
