---
name: daily-sales-report
description: Gere, valide, ajuste ou dispare o Daily Sales Report da GB Importadora para Slack/Telegram/WhatsApp. Use sempre que Pedro mencionar Daily Sales Report, Sales Report, relatório diário de vendas, resumo diário de vendas, vendas de ontem, envio para Yasmin/Lucas/Leonardo, ou ajustes no cron das 06:50 BRT. Garante fonte canônica, ranking consolidado por SKU cross-plataforma, formatação Slack aprovada e validações antes do envio.
---

# Daily Sales Report — GB Importadora

## Objetivo
Enviar diariamente o relatório de vendas do dia anterior com dados corretos, sem duplicidade de informação, em formato legível para equipe administrativa.

## Fonte de verdade
- Marketplaces: agregação direta de Supabase `orders` em janela BRT (`00:00–23:59 America/Sao_Paulo`), excluindo cancelados.
- `v_daily_sales` pode alimentar dashboard, mas o Daily Sales Report não deve depender cegamente dela se houver risco de truncamento UTC; qualquer view canônica precisa usar `timezone('America/Sao_Paulo', order_date)`.
- Período: dia anterior completo em BRT, 00:00–23:59.
- Canais obrigatórios para o Slack dos funcionários:
  - Shopee
  - Mercado Livre
  - Amazon
- No pipeline v2.5 individual em camadas, não incluir blocos consolidados (`RESUMO GERAL` / `VENDAS POR CANAL`) nem Atacado GB Matriz; cada mensagem é específica da plataforma do responsável.
- Não usar coleta direta de APIs como total oficial, exceto fallback explícito com aviso.
- Não misturar settlement/extrato financeiro/DRE com venda gerada do dia.

## Scripts canônicos

### v2.5 — pipeline em camadas (em implementação/preview)
Usar para Lucas/Yasmin/Leonardo quando a rotina em camadas estiver em preview/produção:

```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-analyzer.py YYYY-MM-DD --write-memory
python3 /root/segundo-cerebro/scripts/daily-sales-v2-generate-slack.py YYYY-MM-DD --write-preview
```

Arquitetura obrigatória do pipeline novo:
1. Estratégica — `prompts/daily-sales/camada-1-estrategica.md`
2. Tática — `prompts/daily-sales/camada-2-tatica.md`
3. Operacional — `prompts/daily-sales/camada-3-operacional.md`
4. Granular — `prompts/daily-sales/camada-4-granular.md`
5. Condensadora — `prompts/daily-sales/camada-5-condensadora.md`
6. Slack Writer — `prompts/daily-sales/camada-6-slack-writer.md`
7. QA Gate — `prompts/daily-sales/camada-7-qa-gate.md`

Envio real somente se QA Gate retornar `APROVADO` ou `APROVADO COM RESSALVA`:
```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-generate-slack.py YYYY-MM-DD --send-real
```

Se QA Gate retornar `BLOQUEADO`, não enviar Slack real; salvar artefatos e alertar Pedro no tópico Telegram `Daily Sales Report - SLACK` (thread 10222).

### v1 — relatório único legado/aprovado
Manter como fallback operacional enquanto v2 não estiver 100% aprovada:

```bash
python3 /root/segundo-cerebro/scripts/send-daily-sales-slack-funcionarios.py [YYYY-MM-DD]
```

## Regra de canal Telegram — funcionários Slack

Decisão Pedro 2026-05-15: qualquer assunto, alerta, aviso, preview, QA, bloqueio, desenvolvimento, cron ou mensagem relacionado ao Daily Sales Report dos funcionários enviado no Slack deve obrigatoriamente ir no tópico Telegram **Daily Sales Report - SLACK** do Kobe Hub.

- Chat: Kobe Hub (`-1003730816228`)
- Thread ID: `10222`
- Delivery para crons relacionados: `-1003730816228:topic:10222`
- Não usar mais Marketplaces/Urgente/Operacional para esta rotina, exceto se Pedro mover explicitamente o assunto.

## Destinatários Slack
Envio por DM no Slack para:
- Yasmin — usar o perfil `yasminoscarlino7@gmail.com` (`U09AX9SETDM`). Não usar o perfil antigo `yasmin.oscarlino@gbimportadora.com`.
- Lucas — `U08TCL5A8U9`.
- Leonardo — `U0AUUQ5MP6C`.

## Cron
- Nome: `Daily Sales Report — Slack Funcionários`.
- Horário: diariamente às 06:50 BRT.
- Deve rodar depois do Sales Report do Trader/rotinas de vendas e antes do Daily Briefing.
- Se sucesso: responder `HEARTBEAT_OK`.
- Se falha: alertar Pedro no Telegram tópico `Daily Sales Report - SLACK` (thread 10222), sem expor tokens, comandos, paths internos ou logs brutos.

## Estrutura obrigatória aprovada — v2.5 individual em camadas (TRAVADA em 2026-05-14)

Para qualquer geração futura do Daily Sales Report individual de funcionários no pipeline em camadas, manter rigorosamente esta ordem de 6 seções:
1. `DAILY SALES REPORT — [PLATAFORMA] — DD/MM/AAAA (Ontem)`
2. `📊 VISÃO [PLATAFORMA]`
3. `🏆 TOP PRODUTOS [PLATAFORMA]`
4. `🔍 ANÁLISE DA CONTA`
5. `🎯 PRIORIDADES DO DIA`
6. `Dia analisado: DD/MM/AAAA — 00:00–23:59 BRT`

Não incluir `Pedro Broglio` no topo. O título começa diretamente com `DAILY SALES REPORT`.
Não incluir a seção `DESTAQUES DO DIA`.
Não incluir `📊 RESUMO GERAL` consolidado.
Não incluir `🛒 VENDAS POR CANAL` consolidado.
Mensagem individual é da plataforma do destinatário: Lucas/Shopee, Yasmin/Mercado Livre, Leonardo/Amazon.

## Formatação Slack aprovada
- Títulos das seções: negrito + sublinhado real do Slack via `rich_text blocks` (`style: {bold: true, underline: true}`).
- Não usar underline Unicode, linha separadora fake ou `────────────`.
- Conteúdo interno: texto normal, sem negrito, sem itálico e sem sublinhado.
- Usar bullet points em todas as seções de conteúdo, inclusive seções variáveis, prioridades e ações recomendadas.
- Cada bullet deve transmitir uma ideia completa; bullets de análise podem ser parágrafos médios quando isso deixar o insight mais claro e acionável.
- Bullets sem linhas em branco entre eles.
- Espaçamento entre seções: uma linha em branco.
- A análise deve ser em bullets; cada bullet é um chunk de ideia. Não duplicar informações já presentes nas seções anteriores.

## Top Produtos — regra crítica

No Daily Sales Report v2 individual, o ranking `🏆 TOP PRODUTOS [PLATAFORMA]` deve ser da plataforma da mensagem, não um consolidado das três plataformas.

Obrigatório:
- Usar mapeamento SKU/produto equivalente para consolidar variações/anúncios dentro da própria plataforma/conta analisada.
- Para Shopee, agregar os produtos equivalentes das 3 contas Shopee quando a mensagem for do Lucas.
- Para Mercado Livre, consolidar produtos equivalentes dentro da plataforma correspondente.
- Para Amazon, priorizar identidade real do pedido (`platform_item_id`/ASIN + título vindo de `orderItems`) antes de qualquer alias manual de SKU. Alias manual só pode ser fallback quando ASIN/título não existir.
- Nunca inferir que um ASIN vendeu a partir de memória, planilha, Ads, catálogo ou nome parecido; Top Produtos Amazon só pode sair de pedidos reais em `orders.items`.
- Mostrar produto único consolidado e unidades totais.
- Nunca exibir “Produto não identificado” ou similar. Se o nome não for confiável, omitir do Top Produtos e tratar como problema de cadastro interno.

## Análise da Conta — regra crítica inviolável

A seção `🔍 ANÁLISE DA CONTA` é a seção mais importante do relatório.
Ela deve conter exclusivamente raciocínio denso, conclusões, insights e reflexões relevantes construídas a partir da análise inteligente feita em background.

Obrigatório:
- Condensar e interpretar dados do dia anterior, últimos 30 dias, últimos 60 dias e dias equivalentes da semana.
- Identificar padrões de comportamento de vendas, mudança de patamar, risco, dependência, sazonalidade, exposição/tráfego, mix, cancelamentos, estoque/fulfillment e hipóteses operacionais.
- Separar leitura por conta quando a plataforma tiver múltiplas contas, especialmente Shopee: Budamix Store, Budamix Oficial / Conta 2 e Budamix Shop / Conta 3.
- Escrever como conclusão analítica, não como tabela narrativa.

Proibido dentro de `🔍 ANÁLISE DA CONTA`:
- Repetir números secos já exibidos em `VISÃO [PLATAFORMA]` ou `TOP PRODUTOS`.
- Incluir blocos como `Dia granular`, comparativos numéricos 30d/60d/mesma segunda, linha de produto principal, concentração top 3 ou cancelamentos como métrica solta.
- Usar análise rasa, genérica ou óbvia.

Em resumo: fora dados crus; dentro só raciocínio.

## Checklist antes de enviar
1. Confirmar dia analisado em BRT.
2. Confirmar `v_daily_sales` disponível para o dia.
3. Confirmar que o pipeline v2.5 não inclui Atacado GB Matriz, `RESUMO GERAL` nem `VENDAS POR CANAL` nas mensagens individuais.
4. Confirmar Top Produtos consolidado por SKU equivalente.
5. Confirmar destinatários Slack corretos.
6. Confirmar formatação rich text: títulos bold+underline, conteúdo normal.
7. Em caso de ajuste de formato, testar primeiro com `--to-pedro`.

## Memória em camadas do Trader — Daily Sales Report v2
- Fonte operacional: `shared/trader/memory/projects/daily-sales-report/`.
- Skill específica do ciclo de memória: `skills/trader-daily-sales-memory-cycle/SKILL.md`.
- Antes de gerar análise diária por conta, o Trader deve ler apenas o pacote relevante: análise diária anterior, `weekly.md`, `monthly.md`, `rules.md`, regras operacionais e contexto Himmel quando aplicável.
- Camadas obrigatórias: diária (`daily/YYYY-MM-DD.md`), semanal (`weekly.md`), mensal (`monthly.md`) e regras permanentes (`rules.md`).
- Unidades operacionais independentes: Shopee Budamix Store (`shop_id=448649947`), Shopee Budamix Oficial/Conta 2 (`shop_id=860803675`), Shopee Budamix Shop/Conta 3 (`shop_id=442066454`), Mercado Livre e Amazon.
- `v_daily_sales` serve para resumo geral por plataforma; análise granular Shopee deve consultar `orders` por `shop_id`.
- A análise interna por conta deve ser salva antes da mensagem Slack externa.

## Padrão obrigatório final — Daily Sales Report v2.5 individual em camadas (Pedro, 2026-05-14)

Pedro aprovou a arquitetura em 7 etapas para substituir a geração rasa/monolítica do Daily Sales Report dos funcionários.

### Arquitetura
- Camadas analíticas internas: Estratégica, Tática, Operacional, Granular e Condensadora.
- Slack Writer: única etapa que escreve a mensagem ao funcionário.
- QA Gate: valida o pacote inteiro e bloqueia envio quando houver erro crítico.
- Orchestrator deve continuar determinístico/script; QA Gate também é bloqueante e determinístico na decisão final.

### Estrutura fixa da mensagem Slack
- `DAILY SALES REPORT — [PLATAFORMA] — DD/MM/AAAA (Ontem)`
- `📊 VISÃO [PLATAFORMA]`
- `🏆 TOP PRODUTOS [PLATAFORMA]`
- `🔍 ANÁLISE DA CONTA`
- `🎯 PRIORIDADES DO DIA`
- `Dia analisado: DD/MM/AAAA — 00:00–23:59 BRT`

### Separação dados crus vs análise
- `VISÃO [PLATAFORMA]` contém apenas dados objetivos da plataforma do destinatário, sem comparação temporal e sem interpretação.
- `TOP PRODUTOS [PLATAFORMA]` contém apenas ranking seguro da plataforma do destinatário.
- `ANÁLISE DA CONTA` vem da Condensadora, com no máximo 3 insights e pode ter menos; não preencher por preencher.
- `PRIORIDADES DO DIA` vem das prioridades filtradas pela Condensadora e não pode criar ação nova.
- Sem `RESUMO GERAL`, sem `VENDAS POR CANAL`, sem `DESTAQUES DO DIA` no pipeline v2.5.

### Regras por plataforma
- Shopee/Lucas: `VISÃO` deve mostrar consolidado Shopee e separar Budamix Store, Budamix Oficial / Conta 2 e Budamix Shop / Conta 3 quando o pacote permitir. Análise consolida em até 3 insights totais, não 3 por conta.
- Mercado Livre/Yasmin: `VISÃO` contém faturamento, pedidos, ticket médio, cancelamentos/Full quando disponíveis/relevantes. Análise foca ritmo, exposição, competitividade, reputação, mix e Full quando houver sinal.
- Amazon/Leonardo: produto visível prioriza título real do pedido; ASIN só aparece quando necessário por ambiguidade/risco médio. Alias manual nunca aparece na mensagem. Não interpretar crescimento como positivo quando há fragilidade operacional de FBA/Buy Box/listing.

### QA Gate
- Envio real só pode acontecer se QA Gate retornar `APROVADO` ou `APROVADO COM RESSALVA`.
- Qualquer `BLOQUEADO` impede envio real, salva artefatos e alerta Pedro.
- QA Gate valida: data/período/fonte, destinatário/plataforma/responsável, estrutura Slack, visão, top produtos, análise, prioridades, bloqueios/confiança/logs, consistência entre camadas, tom/utilidade e padrão numérico.

## Fase 7 — Contexto Himmel/Granola
- Antes do Daily Sales Report v2, rodar a sincronização de contexto Himmel/Granola para Shopee e Mercado Livre.
- Script canônico:
```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-himmel-granola-context.py --days 30 --sync-granola --write
```
- A rotina nunca copia transcrição integral; usa apenas resumos/contextos já tratados.
- O contexto global fica em `himmel-context.md`; o contexto específico por conta fica em `accounts/*/himmel-context.md`.
- O analyzer deve carregar `account-himmel-context.md` e `global-himmel-context.md` como insumo de hipótese.
- Usar falas/decisões da Himmel como contexto causal a validar nos dados, nunca como culpa ou fato isolado.
- Amazon Ads não usa Himmel; Amazon continua com Pedro.
- Cron ativo: `Granola Daily Sync → classificação de reuniões`, 20:37 BRT. Classifica reuniões pelo conteúdo e atualiza os contextos cabíveis; não roda mais a cada 30min nem às 06:35.


## Fase 8 — Marketplace Rules Watch
- Antes dos reports matinais, atualizar `marketplace-rules-watch.md` com o estado das regras/taxas/políticas documentadas nas skills de ML, Shopee e Amazon.
- Script canônico:
```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-marketplace-rules-watch.py
```
- Cron ativo: `Daily Sales v2 — Marketplace Rules Watch Refresh`, 06:23 BRT, antes do Sales Report Trader das 06:30 e do Slack Funcionários das 06:50.
- O arquivo é contexto para hipótese, não prova automática. Só mencionar regra/taxa no report quando afetar o dia ou uma prioridade prática.
- Revisão vencida é alerta interno de qualidade de contexto, não mudança confirmada.
- Revisões profundas por plataforma continuam em crons próprios: ML segunda 10h, Shopee quarta 10h, Amazon quarta 10:17 BRT.
