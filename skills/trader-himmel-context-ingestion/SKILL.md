---
name: trader-himmel-context-ingestion
description: Ingestão de contexto da Himmel e transcrições Granola para análises do Trader. Use quando houver reunião, transcrição, resumo, decisão, plano ou cobrança da Himmel sobre ADS de Shopee ou Mercado Livre, e para registrar contexto que deve influenciar o Daily Sales Report v2.
---

# Trader — Himmel Context Ingestion

## Objetivo
Transformar reuniões/transcrições Granola e alinhamentos com a Himmel em contexto útil para as análises diárias de Shopee e Mercado Livre.

## Quando usar
- Chegou transcrição Granola de reunião com Himmel.
- Houve alinhamento manual sobre campanhas, verba, produto priorizado ou estratégia.
- Funcionário trouxe retorno da Himmel.
- Daily Sales Report identificou hipótese que precisa ser cruzada com decisão de ADS.

## O que extrair
Para cada reunião/contexto:
- Data da reunião.
- Participantes.
- Plataformas/contas discutidas.
- Campanhas citadas.
- SKUs/produtos priorizados.
- Mudanças de verba, bid, ACOS, ROAS ou estratégia.
- Testes combinados.
- Prazos.
- Responsáveis.
- Cobranças pendentes.
- Hipóteses levantadas pela Himmel.
- Pontos que devem ser verificados nos próximos reports.

## Onde registrar
Registrar em:
`shared/trader/memory/projects/daily-sales-report/himmel-context.md`

Se uma decisão for específica de conta, também referenciar na análise diária/weekly da conta correspondente.

## Como usar no Daily Sales Report
- Usar como contexto causal, não como dado bruto.
- Cruzar decisão da Himmel com resultado real de vendas.
- Se uma queda pode estar ligada a campanha/verba/exposição, formular como hipótese e ponto de checagem.
- Não culpar a Himmel sem evidência.

## Formato recomendado de registro
- Data.
- Conta/plataforma.
- Decisão ou contexto.
- Evidência/transcrição resumida.
- Impacto esperado.
- Janela de observação.
- Como validar nos dados.
- Status: aberto / confirmado / refutado / encerrado.

## Escalonar para Kobe
Escalar se:
- Himmel prometeu ação e os dados contradizem;
- há queda recorrente possivelmente ligada a ADS;
- há conflito entre orientação da Himmel e dados reais;
- há decisão que afeta orçamento, preço, margem ou estratégia.

## Nunca fazer
- Não colar transcrição inteira na análise diária.
- Não transformar fala de reunião em fato sem validação.
- Não misturar contexto Himmel com Amazon, salvo comparação estratégica; Amazon ADS é Pedro.

## Frequência e classificação Granola — decisão Pedro 2026-05-12
- O sync Granola deve rodar **uma vez por dia no fim do dia**, não a cada 30 minutos.
- Reuniões com Himmel e outras empresas são esporádicas; processamento diário é suficiente.
- Cron canônico: `Granola Daily Sync → classificação de reuniões`, 20:30 BRT.
- O agente deve classificar a reunião pelo conteúdo da transcrição/resumo, não apenas pelo título.
- Se for Himmel/ADS Shopee ou Mercado Livre, distribuir pontos cabíveis para as contas do Daily Sales Report v2.
- Se for outro tema, registrar no destino correto conforme conteúdo: Spark, Trader, Kobe ou projeto específico.
- Nunca copiar transcrição integral; salvar só interpretação útil, decisões, pendências e hipóteses validáveis.
