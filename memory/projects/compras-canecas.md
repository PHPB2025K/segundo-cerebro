---
title: "Compras — Reposição de Canecas"
created: 2026-05-15
type: project
status: active
tags:
  - project/compras
  - gb-importadora
  - canecas
---

# Compras — Reposição de Canecas

## Contexto

Pedro está alinhando com Yasmin, Lucas e Leonardo uma projeção de compras para reposição das canecas Budamix.

Objetivo: cruzar histórico real por marketplace + projeção humana da equipe + análise do Kobe/Trader para definir quanto comprar semanalmente por SKU/cor nos próximos 2 meses.

## Produtos no escopo

Modelos:
- Tulipa
- Paris
- Canelada
- Reta

Cores por modelo:
- Rosa
- Preto
- Branco
- Azul
- Verde
- Amarelo

Granularidade esperada: modelo × cor × marketplace.

Regra operacional confirmada pelo Pedro em 18/05/2026: existe apenas um tipo de kit colorido por modelo de caneca, e todos os kits coloridos usam a mesma combinação das seis cores: rosa, preto, branco, azul, verde e amarelo. Portanto, todo kit colorido vendido deve ser desmembrado em 1 unidade de cada cor do respectivo modelo. Não tratar como hipótese nem como variação incerta.

Responsáveis por plataforma:
- Yasmin: Mercado Livre
- Lucas: Shopee
- Leonardo: Amazon

## Pedido feito à equipe

Cada responsável deve entregar:
1. Histórico de venda dos últimos 3 meses.
2. Quebra por modelo e por cor, se disponível.
3. Projeção de compras para os próximos 2 meses.
4. Recomendação semanal considerando que Pedro faz pedido 1 vez por semana.

## Premissas operacionais

- Pedido pode ser feito semanalmente.
- Lead time fornecedor/entrega: 3 a 8 dias.
- Horizonte de compra: próximos 2 meses.
- A análise precisa considerar histórico, tendência, ruptura, cobertura, sazonalidade e variação entre marketplaces.

## Modelo de decisão recomendado

Para cada SKU/cor/modelo:
- vendas 90 dias;
- média diária e média semanal;
- tendência 30d vs 90d;
- estoque atual;
- cobertura atual em dias;
- estoque em trânsito/pedidos já feitos;
- lead time pessimista de 8 dias;
- estoque de segurança mínimo;
- recomendação de compra por semana;
- prioridade: comprar agora / monitorar / não recomprar.

## Como Kobe deve operar

1. Receber as planilhas/projeções de Yasmin, Lucas e Leonardo.
2. Normalizar nomes de modelo/cor/SKU entre plataformas.
3. Converter todo pedido para cabeças unitárias antes de calcular demanda: kit cor única = 6 unidades da mesma cor/modelo; kit colorido = 1 unidade de cada uma das seis cores do respectivo modelo.
4. Cruzar com dados reais disponíveis de marketplaces e estoque.
5. Produzir uma versão independente do Kobe/Trader.
6. Comparar divergências relevantes entre equipe vs dados.
7. Entregar recomendação consolidada em formato executivo, com tabela final de compra semanal por modelo/cor.

## Agente de Compras

Decisão do Pedro em 2026-05-15 18:56 BRT: o Agente de Compras deve ser criado. A primeira rodada de canecas seria feita diretamente pelo Kobe, sem agente, para validar o método, o formato, os cálculos e o processo.

Atualização 2026-05-25 19:22 BRT: Pedro pediu retomar a criação do agente como Diretor. Fundação criada como **Compras — Diretor de Compras e Planejamento de Reposição**, mantendo o piloto de canecas como primeiro playbook e com guardrail de não executar compras/mensagens externas sem autorização explícita.

Depois da validação da primeira rodada, transformar o playbook em agente/rotina recorrente, porque Pedro pretende usar esse fluxo para vários outros produtos além das canecas.

Sequência aprovada:
1. Rodada 1 — Kobe executa manualmente a análise das canecas.
2. Validar com Pedro o formato final, os campos, os critérios e a recomendação semanal.
3. Documentar o playbook canônico de compras.
4. Criar/finalizar o Agente de Compras com base no processo validado.
5. Ampliar para outras famílias de produto.

## Regra de canal

Todo assunto relacionado a compras deve ser tratado no tópico Telegram **🛍️ Compras** do Kobe Hub, thread 11. Isso inclui o planejamento/projeção das canecas e o futuro Agente de Compras.

## Próximo passo

Aguardar os arquivos/projeções da equipe e montar a primeira rodada consolidada.

## Conectado a

- [[memory/context/people]] — **ref**: 3 focal points (Yasmin/ML, Lucas/Shopee, Leonardo/Amazon)
- [[openclaw/agents/trader/IDENTITY]] — **executor**: Trader cruza dados marketplace para validar projeções da equipe
- [[projects/budamix-central]] — **ref**: estoque consolidado FULL+FÍSICO+TOTAL na home do Central
- [[business/marketplaces/_index]] — **tema**: 3 canais ML/Shopee/Amazon mapeados como contexto
- [[memory/projects/gestao-funcionarios]] — **tema**: mesma equipe acompanhada semanalmente
