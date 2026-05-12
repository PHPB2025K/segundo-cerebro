---
name: daily-sales-report
description: Gere, valide, ajuste ou dispare o Daily Sales Report da GB Importadora para Slack/Telegram/WhatsApp. Use sempre que Pedro mencionar Daily Sales Report, Sales Report, relatório diário de vendas, resumo diário de vendas, vendas de ontem, envio para Yasmin/Lucas/Leonardo, ou ajustes no cron das 06:50 BRT. Garante fonte canônica, ranking consolidado por SKU cross-plataforma, formatação Slack aprovada e validações antes do envio.
---

# Daily Sales Report — GB Importadora

## Objetivo
Enviar diariamente o relatório de vendas do dia anterior com dados corretos, sem duplicidade de informação, em formato legível para equipe administrativa.

## Fonte de verdade
- Marketplaces: Budamix Central / Supabase `v_daily_sales`.
- Período: dia anterior completo em BRT, 00:00–23:59.
- Canais obrigatórios para o Slack dos funcionários:
  - Shopee
  - Mercado Livre
  - Amazon
- **Não incluir Atacado GB Matriz/Bling no Daily Sales Report enviado para Yasmin, Lucas e Leonardo.** Eles não atuam no atacado; o relatório deles deve refletir somente marketplaces.
- Não usar coleta direta de APIs como total oficial, exceto fallback explícito com aviso.
- Não misturar settlement/extrato financeiro/DRE com venda gerada do dia.

## Script canônico
Usar:

```bash
python3 /root/segundo-cerebro/scripts/send-daily-sales-slack-funcionarios.py [YYYY-MM-DD]
```

Modos úteis:
- Preview sem envio:
  ```bash
  python3 /root/segundo-cerebro/scripts/send-daily-sales-slack-funcionarios.py YYYY-MM-DD --dry-run
  ```
- Enviar teste só para Pedro no Slack:
  ```bash
  python3 /root/segundo-cerebro/scripts/send-daily-sales-slack-funcionarios.py YYYY-MM-DD --to-pedro
  ```
- Envio real para equipe:
  ```bash
  python3 /root/segundo-cerebro/scripts/send-daily-sales-slack-funcionarios.py YYYY-MM-DD
  ```

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
- Se falha: alertar Pedro no Telegram tópico Marketplaces, sem expor tokens, comandos, paths internos ou logs brutos.

## Estrutura aprovada
Manter exatamente estas seções:
1. `DAILY SALES REPORT - DD/MM/AAAA (Ontem)`
2. `📊 RESUMO GERAL`
3. `🛒 VENDAS POR CANAL`
4. `🏆 TOP PRODUTOS — CONSOLIDADO 3 PLATAFORMAS`
5. `📈 ANÁLISE DO DIA`
6. `Dia analisado: DD/MM/AAAA — 00:00–23:59 BRT`

Não incluir a seção `DESTAQUES DO DIA`; ela foi removida por duplicar informação.

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
O ranking deve ser consolidado por produto equivalente nas três plataformas, não por título/anúncio isolado.

Obrigatório:
- Usar mapeamento SKU cross-plataforma existente.
- Somar vendas de SKUs equivalentes em Shopee + Mercado Livre + Amazon.
- Mostrar produto único consolidado e unidades totais.
- Nunca exibir “Produto não identificado” ou similar. Se o nome não for confiável, omitir do Top Produtos e tratar como problema de cadastro interno.

## Análise do dia — regra crítica
A análise deve ser curta e útil para operação.

Deve considerar:
- Faturamento total vs média dos últimos 30 dias.
- Comparação com dias equivalentes da semana quando relevante.
- Mês/data analisada e efeito de calendário.
- Particularidades por canal quando realmente agregarem insight.
- Tendência operacional acionável para o dia atual.

Evitar:
- Repetir números já listados em Resumo/Vendas por Canal.
- Comentário genérico sem base nos dados.
- Frases longas demais.

## Checklist antes de enviar
1. Confirmar dia analisado em BRT.
2. Confirmar `v_daily_sales` disponível para o dia.
3. Confirmar que o relatório dos funcionários está excluindo Atacado GB Matriz/Bling.
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

## Último padrão aprovado
Aprovado por Pedro em 2026-05-11 e ajustado em 2026-05-12:
- Envio via Slack DM para Yasmin, Lucas e Leonardo.
- Escopo do Slack dos funcionários: somente marketplaces (Shopee, Mercado Livre e Amazon), sem Atacado GB Matriz/Bling.
- Mensagens serão individuais por funcionário: Lucas/Shopee, Yasmin/Mercado Livre, Leonardo/Amazon.
- Cada mensagem começa com o mesmo resumo geral da operação e depois traz diagnóstico específico da plataforma/conta do funcionário.
- Estrutura híbrida: blocos fixos de resumo geral, visão da plataforma e prioridade do dia; seções variáveis conforme sinais relevantes do dia.
- Usar bullet points em todas as seções de conteúdo; cada ideia deve ser quebrada em um novo bullet, inclusive nas prioridades e seções variáveis.
- Uma linha em branco entre seções.
- Títulos em negrito + sublinhado real do Slack.
- Conteúdo sem formatação especial.
- Sem seção `DESTAQUES DO DIA`.
