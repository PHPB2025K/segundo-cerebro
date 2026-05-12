---
name: trader-daily-sales-memory-cycle
description: Ciclo de memoria persistente do Trader para o Daily Sales Report v2. Use sempre que o Trader gerar, revisar, consolidar ou auditar analises diarias por conta do Sales Report; quando criar memoria diaria/semanal/mensal/regras permanentes por conta; ou quando mexer nos reports Slack personalizados de Lucas/Shopee, Yasmin/Mercado Livre e Leonardo/Amazon.
---

# Trader — Ciclo de Memória do Daily Sales Report v2

## Objetivo
Manter uma memória analítica persistente, por conta, para que o Daily Sales Report v2 fique mais inteligente todos os dias sem sobrecarregar o contexto do Trader.

A memória interna **não é o texto enviado aos funcionários**. Ela deve ser mais completa, granular e extensa. O Slack recebe apenas a síntese acionável.

## Unidades operacionais
Tratar cada unidade abaixo como conta independente, com memória própria:

| Unidade | Plataforma | Responsável | ADS |
|---|---|---|---|
| Shopee — Budamix Store | Shopee `shop_id=448649947` | Lucas | Himmel |
| Shopee — Budamix Oficial / Conta 2 | Shopee `shop_id=860803675` | Lucas | Himmel |
| Shopee — Budamix Shop / Conta 3 | Shopee `shop_id=442066454` | Lucas | Himmel |
| Mercado Livre | ML conta única | Yasmin | Himmel |
| Amazon | Amazon conta única | Leonardo | Pedro |

## Fonte de dados obrigatória
- Resumo geral por plataforma: `v_daily_sales` pode ser usado.
- Análise por conta Shopee: consultar `orders` diretamente usando `shop_id`.
- Período sempre em BRT: dia analisado de 00:00 a 23:59.
- Não incluir Atacado/Bling no report dos funcionários.
- Não misturar venda gerada com settlement, extrato financeiro ou DRE.
- Se dados estiverem incompletos, marcar como parcial; nunca estimar número.

## Estrutura de memória
Usar a árvore do Trader:

`shared/trader/memory/projects/daily-sales-report/`

Cada conta deve ter:
- `daily/` — análises brutas diárias.
- `weekly.md` — consolidação semanal vigente.
- `monthly.md` — tese mensal vigente.
- `rules.md` — regras permanentes aprendidas.

Arquivos gerais:
- `himmel-context.md` — decisões/reuniões/contexto da Himmel.
- `marketplace-rules-watch.md` — mudanças de regras, taxas e políticas.
- `sent-reports.md` — histórico do que foi enviado no Slack.
- `OPERATING-RULES.md` — regras aprovadas do processo.

## Pacote de contexto antes da análise diária
Antes de analisar uma conta, carregar somente:
1. A análise diária anterior daquela conta, se existir.
2. `weekly.md` daquela conta.
3. `monthly.md` daquela conta.
4. `rules.md` daquela conta.
5. `himmel-context.md` somente para Shopee e Mercado Livre, quando houver evento recente ou hipótese de ADS.
6. `marketplace-rules-watch.md` somente se houver mudança relevante de plataforma/taxa/regra.

Não carregar histórico diário inteiro. Se precisar investigar padrão antigo, buscar pontualmente.

## Ciclo diário — antes do Slack
Para cada conta, gerar primeiro uma análise interna completa com:

- Data analisada.
- Métricas do dia: faturamento, pedidos, ticket, unidades.
- Comparação contra 30 dias e 60 dias.
- Comparação contra mesmo dia da semana.
- Comportamento por horário.
- SKUs/produtos que explicam o resultado.
- Concentração de venda em poucos produtos.
- Estoque/fulfillment: Shopee Full, Amazon FBA, Full/estoque quando disponível.
- ADS/contexto:
  - Shopee/ML: tratar como ponto para Himmel quando indicar tráfego, exposição, campanha, verba ou ACOS.
  - Amazon: tratar como gestão Pedro; separar o que Leonardo pode acompanhar do que precisa ajuste de campanha.
- Hipóteses antigas lidas.
- Hipóteses confirmadas, refutadas ou ainda abertas.
- Novas hipóteses.
- Riscos para o próximo dia.
- Ação recomendada para o responsável.
- O que observar amanhã.
- Observações para Kobe/Pedro se houver risco estratégico.

Salvar essa análise em `daily/YYYY-MM-DD.md` da conta antes de gerar a mensagem Slack.

## Geração do Slack
Gerar mensagens individuais:

- Lucas: Shopee geral + três contas separadas.
- Yasmin: Mercado Livre.
- Leonardo: Amazon.

Toda mensagem deve ter:
- Resumo geral igual para todos: total marketplaces, Shopee, ML e Amazon.
- Visão da plataforma do responsável.
- Diagnóstico específico da conta ou contas.
- Prioridades do dia.

Formatação:
- Tudo em bullet points.
- Uma ideia por bullet.
- Bullets podem ser parágrafos médios quando necessário para clareza.
- Seções variáveis entram apenas quando agregam: horário, SKU, ADS/Himmel, estoque, tendência, Buy Box/FBA, sazonalidade, regra/taxa.

Depois de enviar, salvar cópia em `sent-reports.md` ou no formato definido pela Fase 2.

## Ciclo semanal
Uma vez por semana, consolidar por conta:

- Padrões confirmados.
- Padrões descartados.
- SKUs ganhando/perdendo força.
- Mudanças de horário de venda.
- Conta saudável, instável ou em alerta.
- Pontos para Himmel/Pedro.
- Hipóteses que seguem abertas.
- Regras candidatas a permanente.
- O que carregar para a semana seguinte.

Após consolidar, manter o diário bruto recente e reduzir a dependência de análises antigas.

## Ciclo mensal
Uma vez por mês, criar ou atualizar a tese da conta:

- Tese atual da conta.
- O que mudou no mês.
- Saúde da conta.
- Dependências e riscos estruturais.
- Oportunidades.
- Hipóteses estratégicas para o próximo mês.
- Regras permanentes novas ou invalidadas.

Kobe deve revisar mudanças estratégicas mensais.

## Regras permanentes
Promover para `rules.md` apenas aprendizados recorrentes ou validados.

Cada regra deve conter:
- Regra.
- Conta/plataforma.
- Evidência que originou.
- Quando aplicar.
- Quando não aplicar.
- Data de criação.
- Revisão/expiração, se aplicável.

Nunca transformar uma hipótese de um único dia em regra permanente.

## Escalonamento para Kobe
Avisar Kobe/Pedro no tópico Marketplaces quando houver:

- Dados incompletos ou divergentes.
- Impossibilidade de separar conta.
- Queda forte recorrente sem explicação.
- Mudança de regra/taxa com impacto comercial.
- Risco de ruptura relevante.
- Hipótese envolvendo decisão estratégica, preço, margem ou cobrança da Himmel.
- Falha no envio Slack.

## Papel dos agentes
- Trader: dono operacional da análise, memória e envio diário.
- Kobe: governança, QA, regras e comunicação com Pedro.
- Spark: apoio em ADS quando necessário.
- Builder: alterações de código, scripts, views, automações e crons.

## Checklist obrigatório
Antes de finalizar qualquer execução diária:

1. Dados do dia anterior em BRT conferidos.
2. Todas as 5 unidades operacionais avaliadas ou marcadas como parcial.
3. Memória diária interna salva por conta antes do Slack.
4. Mensagens individuais geradas para Lucas, Yasmin e Leonardo.
5. Report sem Atacado/Bling.
6. Tudo em bullets.
7. Cópia do enviado registrada.
8. Alertas relevantes escalados para Kobe.

## Correção obrigatória — nível mínimo de análise Slack (Pedro, 2026-05-12)

- A mensagem Slack externa é síntese, mas não pode ser rasa. Deve condensar a análise interna em prioridades realmente úteis.
- Diagnóstico por conta deve explicar causa provável, evidência, comparação temporal e ação; não basta listar pedidos, GMV, ticket, SKU principal e variação.
- Prioridades devem ser mais profundas que “acompanhar volume” ou “verificar anúncios”: precisam dizer o que olhar, por que olhar, qual risco existe e qual responsável/contexto (Lucas/Yasmin/Leonardo/Himmel/Pedro).
- Produto visível deve aparecer por nome comercial, nunca por SKU. SKUs ficam apenas no background.
- Se o dado ainda não permite afirmar causa, escrever como hipótese com evidência e critério de confirmação no próximo dia.
