---
name: trader-daily-sales-slack-writer
description: Converte análises profundas do Daily Sales Report v2 em mensagens Slack individuais para Lucas/Shopee, Yasmin/Mercado Livre e Leonardo/Amazon. Use depois das análises internas por conta e antes do envio Slack, garantindo resumo geral igual, blocos específicos, bullets, concisão acionável e sem Atacado/Bling.
---

# Trader — Daily Sales Slack Writer

## Objetivo
Transformar a análise interna profunda em mensagens individuais úteis, claras e acionáveis para cada funcionário.

## Regra principal
O Slack não é a análise bruta. O Slack é a síntese operacional do que cada responsável precisa entender e fazer hoje.

## Destinatários
- Lucas: Shopee, com 3 contas separadas.
- Yasmin: Mercado Livre.
- Leonardo: Amazon.

## Estrutura fixa de cada mensagem
1. Título: `DAILY SALES REPORT — {PLATAFORMA}`.
2. Dia analisado: `DD/MM/YYYY — 00:00–23:59 BRT`.
3. Visão geral da plataforma do responsável.
4. Top Produtos da plataforma.
5. Diagnóstico específico da(s) conta(s).
6. Prioridades do dia.

Não incluir `RESUMO GERAL` nem `VENDAS POR CANAL` nas mensagens individuais dos funcionários. Cada DM deve ser especializada somente no marketplace do responsável.

## Formatação
- Tudo em bullet points.
- Uma ideia por bullet.
- Bullets podem ser parágrafos médios se aumentarem clareza.
- Uma linha em branco entre seções.
- Sem seção “Destaques do dia”.
- Sem Atacado/Bling.
- Conteúdo interno sem negrito/itálico/subscrito; títulos podem usar formatação Slack aprovada.

## Como condensar
Para cada conta, priorize o que muda ação hoje:
- variação relevante vs histórico;
- SKU/produto que explica o dia;
- horário fora do padrão;
- risco de estoque/fulfillment;
- hipótese ADS/Himmel/Pedro;
- ação recomendada.

Se algo não muda ação, não entra no Slack.

## Regras por responsável
### Lucas — Shopee
- A Shopee tem três contas: Budamix Store, Budamix Oficial e Budamix Shop.
- Na seção `📊 VISÃO SHOPEE`: mostrar primeiro o consolidado das três contas em negrito; logo abaixo, mostrar os números individuais das três contas em texto normal.
- Na seção `🏆 TOP PRODUTOS SHOPEE`: mostrar primeiro o ranking consolidado das três contas, somando pedidos da mesma variação entre contas; depois mostrar rankings independentes de Budamix Store, Budamix Oficial e Budamix Shop. Usar nomes curtos de produto e ranking por pedidos.
- Na seção `🔍 ANÁLISE DAS CONTAS`: inverter a ordem — primeiro análise individual das três contas, depois análise consolidada em negrito. A análise consolidada deve avaliar complementaridade entre contas, aumento de faturamento total, escala e risco de canibalização.
- Na seção `🎯 PRIORIDADES DO DIA`: mostrar apenas ações consolidadas, derivadas das análises individuais + consolidada.
- Não concluir “Shopee caiu/subiu” sem dizer qual conta explica.
- Se o sinal for ADS/tráfego, formular como ponto para alinhar com Himmel.

### Yasmin — Mercado Livre
- Focar conta ML, produtos que carregaram/caíram, exposição, Full/reputação/preço quando houver sinal.
- Se queda parecer tráfego/ADS, apontar checagem com Himmel.

### Leonardo — Amazon
- Focar ASIN/SKU, FBA, Buy Box, estoque e listing.
- Separar ações operacionais do Leonardo de ajustes de ADS do Pedro.

## QA antes de enviar
- A mensagem está individualizada?
- O resumo geral bate com os dados canônicos?
- Existe pelo menos uma ação/prioridade clara?
- Algum bullet ficou genérico demais?
- Há hipótese apresentada como fato? Corrigir.
- Está tudo em bullets?
- Sem Atacado/Bling?

## Régua mínima de mensagem aceitável
Bloquear e reescrever se a mensagem parecer resumo automático. Cada mensagem precisa conter:
- diagnóstico que explique **causa provável + evidência + risco**;
- prioridades com **ação + motivo + critério de acompanhamento**;
- produtos por **nome comercial**, nunca SKU;
- título de seção com emoji + uppercase e rich_text bold+underline;
- pelo menos uma leitura temporal útil, não apenas métrica do dia.

## Proibido por baixa qualidade
- “Monitorar operação normal” sozinho.
- “Acompanhar volume” sem dizer qual produto/conta/horário e qual gatilho de escalonamento.
- “Verificar anúncios” sem indicar evidência de tráfego/exposição e responsável/contexto.
- Listar SKU cru no texto visível.
- Repetir pedidos/GMV/ticket sem interpretação.

## Modelo de prioridade boa
Uma prioridade boa segue este formato mental:
`Ação concreta` + `evidência numérica/temporal` + `risco` + `critério de decisão amanhã`.

Exemplo:
- Checar visibilidade dos anúncios dos potes de vidro redondos Tampa Preta na Budamix Store, porque a conta caiu em pedidos e GMV vs 30d com ticket preservado; se até 12h BRT o ritmo seguir abaixo da média horária, alinhar com Himmel revisão de tráfego/campanha.
