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
3. Cruzar com dados reais disponíveis de marketplaces e estoque.
4. Produzir uma versão independente do Kobe/Trader.
5. Comparar divergências relevantes entre equipe vs dados.
6. Entregar recomendação consolidada em formato executivo, com tabela final de compra semanal por modelo/cor.

## Agente de Compras

Ideia do Pedro: criar um agente específico de compras.

Recomendação inicial: rodar primeiro este ciclo como playbook supervisionado por Kobe/Trader. Depois de validar a lógica e o formato final, transformar em agente/rotina recorrente de compras para canecas e, depois, ampliar para outros SKUs.

## Próximo passo

Aguardar os arquivos/projeções da equipe e montar a primeira rodada consolidada.
