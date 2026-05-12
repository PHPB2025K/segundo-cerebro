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

## Bloqueios de qualidade adicionados em 2026-05-12
Bloquear o envio/preview e devolver para reescrita se houver qualquer um destes sinais:
- produto visível por SKU em vez de nome comercial;
- diagnóstico só descritivo, sem hipótese ou interpretação;
- prioridade genérica sem ação concreta, evidência e critério de acompanhamento;
- ausência de comparação temporal relevante;
- Shopee sem leitura comparativa entre as 3 contas;
- Amazon com cancelamento alto sem investigação operacional;
- títulos fora do padrão emoji + uppercase + bold/underline real no payload Slack.

## Score mínimo de QA
Antes de enviar, atribuir PASS apenas se cada mensagem cumprir:
- **Dados:** fonte oficial e conta correta.
- **Interpretação:** explica o que mudou e por quê importa.
- **Ação:** responsável sabe exatamente o que olhar hoje.
- **Memória:** usa contexto persistente quando disponível.
- **Forma:** títulos e produto-nome no padrão aprovado.
Se qualquer item falhar, status = `BLOQUEADO_QUALIDADE`.

