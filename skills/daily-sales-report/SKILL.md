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
- Incluir `Atacado GB Matriz` no bloco geral `🛒 VENDAS POR CANAL` quando Pedro pedir o padrão dos templates de 2026-05-12. O diagnóstico individual continua focado no marketplace do responsável.
- Não usar coleta direta de APIs como total oficial, exceto fallback explícito com aviso.
- Não misturar settlement/extrato financeiro/DRE com venda gerada do dia.

## Scripts canônicos

### v2 — mensagens individuais com memória do Trader
Usar para Lucas/Yasmin/Leonardo quando a rotina v2 estiver em preview/produção:

```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-analyzer.py YYYY-MM-DD --write-memory
python3 /root/segundo-cerebro/scripts/daily-sales-v2-generate-slack.py YYYY-MM-DD --dry-run
python3 /root/segundo-cerebro/scripts/daily-sales-v2-generate-slack.py YYYY-MM-DD --write-preview
```

Envio real somente após QA e aprovação explícita:
```bash
python3 /root/segundo-cerebro/scripts/daily-sales-v2-generate-slack.py YYYY-MM-DD --send-real
```

### v1 — relatório único legado/aprovado
Manter como fallback operacional enquanto v2 não estiver 100% aprovada:

```bash
python3 /root/segundo-cerebro/scripts/send-daily-sales-slack-funcionarios.py [YYYY-MM-DD]
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

## Estrutura obrigatória aprovada — v2 individual (TRAVADA em 2026-05-12)

Para qualquer geração futura do Daily Sales Report individual de funcionários, manter rigorosamente esta ordem:
1. `DAILY SALES REPORT — [PLATAFORMA] — DD/MM/AAAA (Ontem)`
2. `📊 RESUMO GERAL`
3. `🛒 VENDAS POR CANAL`
4. `🛍️ VISÃO [PLATAFORMA]`
5. `🏆 TOP PRODUTOS [PLATAFORMA]`
6. `🔍 ANÁLISE DA CONTA`
7. `🎯 PRIORIDADES DO DIA`
8. `Dia analisado: DD/MM/AAAA — 00:00–23:59 BRT`

Não incluir `Pedro Broglio` no topo. O título começa diretamente com `DAILY SALES REPORT`.
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

No Daily Sales Report v2 individual, o ranking `🏆 TOP PRODUTOS [PLATAFORMA]` deve ser da plataforma da mensagem, não um consolidado das três plataformas.

Obrigatório:
- Usar mapeamento SKU/produto equivalente para consolidar variações/anúncios dentro da própria plataforma/conta analisada.
- Para Shopee, agregar os produtos equivalentes das 3 contas Shopee quando a mensagem for do Lucas.
- Para Mercado Livre e Amazon, consolidar produtos equivalentes dentro da plataforma correspondente.
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
- Repetir números secos já exibidos em `RESUMO GERAL`, `VENDAS POR CANAL`, `VISÃO [PLATAFORMA]` ou `TOP PRODUTOS`.
- Incluir blocos como `Dia granular`, comparativos numéricos 30d/60d/mesma segunda, linha de produto principal, concentração top 3 ou cancelamentos como métrica solta.
- Usar análise rasa, genérica ou óbvia.

Em resumo: fora dados crus; dentro só raciocínio.

## Checklist antes de enviar
1. Confirmar dia analisado em BRT.
2. Confirmar `v_daily_sales` disponível para o dia.
3. Confirmar se o padrão vigente pede Atacado GB Matriz no bloco geral/canais; se sim, incluir apenas no resumo/canais e não no diagnóstico individual.
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
- Padrão de 2026-05-12: o bloco geral/canais pode incluir Atacado GB Matriz quando o template aprovado pedir; diagnósticos individuais seguem por responsável/canal.
- Mensagens serão individuais por funcionário: Lucas/Shopee, Yasmin/Mercado Livre, Leonardo/Amazon.
- Cada mensagem começa obrigatoriamente com dois blocos fixos e separados, iguais para todos os funcionários: `📊 RESUMO GERAL` e `🛒 VENDAS POR CANAL`.
- `📊 RESUMO GERAL` deve conter apenas os totais gerais: faturamento total, pedidos e ticket médio.
- `🛒 VENDAS POR CANAL` deve vir logo depois, separado, com Shopee, Mercado Livre e Amazon em bullets próprios.
- Depois desses dois blocos fixos, entra o diagnóstico específico da plataforma/conta do funcionário.
- Estrutura híbrida: blocos fixos de resumo geral/vendas por canal, visão da plataforma e prioridade do dia; seções variáveis conforme sinais relevantes do dia.
- Usar bullet points em todas as seções de conteúdo; cada ideia deve ser quebrada em um novo bullet, inclusive nas prioridades e seções variáveis.
- Uma linha em branco entre seções.
- Títulos em negrito + sublinhado real do Slack.
- Conteúdo sem formatação especial.
- Sem seção `DESTAQUES DO DIA`.

## Correção obrigatória — profundidade analítica e nomes de produtos (Pedro, 2026-05-12)

- Diagnóstico por conta e prioridades do dia NÃO podem ser rasos, óbvios ou meramente descritivos.
- Cada diagnóstico deve trazer leitura temporal/retroativa: comparação com 30d, 60d, mesmo dia da semana, tendência recente, concentração de mix, horário de venda quando relevante, cancelamentos, fulfillment/estoque e hipótese operacional.
- Prioridades do dia devem ser completas e acionáveis: explicar o porquê, indicar o que verificar, qual sinal confirma/refuta a hipótese e quem deve agir/acompanhá-la.
- Usar memória persistente por conta sempre que existir; nunca gerar análise como se fosse o primeiro dia quando já houver `daily/`, `weekly.md`, `monthly.md` ou `rules.md`.
- Sempre que mencionar produtos no texto visível ao funcionário/Pedro, mostrar o **nome do produto**, nunca o SKU. O SKU pode ser usado apenas internamente para cálculo/mapeamento.
- Títulos de seções devem seguir o padrão visual aprovado no Slack: emoji + título em uppercase, com bold+underline real via rich_text. Ex.: `📊 RESUMO GERAL`, `🛒 VENDAS POR CANAL`, `🏆 TOP PRODUTOS — CONSOLIDADO 3 PLATAFORMAS`, `📈 ANÁLISE DO DIA`. Para seções novas, manter o mesmo padrão: emoji + uppercase + bold+underline.
- No report dos funcionários, se usar os templates aprovados em 2026-05-12, incluir Atacado GB Matriz apenas no bloco geral/canais e preservar o padrão visual dos títulos.
- `📊 RESUMO GERAL` e `🛒 VENDAS POR CANAL` são seções obrigatórias e fixas em todas as mensagens para funcionários; nunca juntar canais dentro do resumo geral.


## Correção obrigatória — template aprovado sem prefixo Pedro (Pedro, 2026-05-12)

- O topo das mensagens NÃO deve incluir `Pedro Broglio`.
- O título deve começar diretamente com `DAILY SALES REPORT — [PLATAFORMA] — DD/MM/AAAA (Ontem)`.
- Manter estrutura próxima aos anexos aprovados: `📊 RESUMO GERAL`, `🛒 VENDAS POR CANAL`, `🛍️ VISÃO [CANAL]`, `🏆 TOP PRODUTOS [CANAL]`, `🔍 ANÁLISE DA CONTA`, `🎯 PRIORIDADES DO DIA`, rodapé `Dia analisado: DD/MM/AAAA — 00:00–23:59 BRT`.


## Padrão obrigatório final — Daily Sales Report v2 individual (Pedro, 2026-05-12)

Pedro aprovou e travou os três templates finais de Amazon, Mercado Livre e Shopee como padrão obrigatório para todas as gerações futuras.

### Estrutura fixa
- `DAILY SALES REPORT — [PLATAFORMA] — DD/MM/AAAA (Ontem)`
- `📊 RESUMO GERAL`
- `🛒 VENDAS POR CANAL`
- `🛍️ VISÃO [PLATAFORMA]`
- `🏆 TOP PRODUTOS [PLATAFORMA]`
- `🔍 ANÁLISE DA CONTA`
- `🎯 PRIORIDADES DO DIA`
- `Dia analisado: DD/MM/AAAA — 00:00–23:59 BRT`

### Separação dados crus vs análise
- Dados crus ficam apenas em `RESUMO GERAL`, `VENDAS POR CANAL`, `VISÃO [PLATAFORMA]`, `TOP PRODUTOS` e, quando necessário, `PRIORIDADES DO DIA`.
- `VISÃO [PLATAFORMA]` não deve conter comparativos 30d/60d/mesmo dia da semana; esses comparativos alimentam o raciocínio, mas não aparecem como linha seca ali.
- `ANÁLISE DA CONTA` nunca repete blocos numéricos secos. Ela usa esses dados apenas como insumo para interpretação.

### Regras por plataforma
- Amazon: não mostrar Fulfillment FBA na visão, pois operação Amazon é 100% FBA por padrão; manter cancelamentos quando forem sinal relevante.
- Mercado Livre: visão contém faturamento, pedidos, ticket médio e cancelamentos; análise interpreta comportamento de demanda, comparação de janelas, saúde de distribuição e risco.
- Shopee: visão contém faturamento, pedidos, ticket médio e cancelamentos consolidados; análise deve manter separação por conta (Budamix Store, Budamix Oficial / Conta 2, Budamix Shop / Conta 3), mas cada subitem deve ser raciocínio denso, sem cabeçalho com números crus.

### Raciocínio obrigatório
- A análise deve partir da análise em background/memória do Trader e condensar padrões dos últimos 30/60 dias, dia equivalente da semana, tendência, mix, exposição/tráfego, cancelamentos, estoque/fulfillment e hipótese operacional.
- Prioridades devem ser acionáveis: o que fazer, por quê, como confirmar/refutar e quando escalar.
- Produto visível deve ser nome comercial, nunca SKU cru.

Esse padrão substitui regras antigas conflitantes sobre `ANÁLISE DO DIA`, blocos genéricos ou análise rasa.

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
- Cron ativo: `Daily Sales v2 — Himmel/Granola Context Sync`, 06:35 BRT, antes do envio das 06:50.
