---
title: "estoque columns"
created: 2026-04-14
type: skill
domain: financeiro
status: active
tags:
  - skill/financeiro
  - pricing
---

# Mapeamento de Colunas — ABA ESTOQUE

> Headers: row 8 | Dados: row 9+
> INPUT: A, B, C, D, E, F, G
> FORMULA (NUNCA TOCAR): H
> ESTA ABA É A FONTE DE VERDADE — preencher SEMPRE PRIMEIRO

## Estrutura correta atual — 2026-06-09

A aba ESTOQUE da planilha oficial está em **8 colunas (A:H)**, nesta ordem exata:

| Col | Campo | Tipo | Observação |
|-----|-------|------|------------|
| A | ESTOQUE | INPUT | Quantidade em estoque |
| B | SKU BASE | INPUT | Código interno Budamix / fornecedor |
| C | DESCRIÇÃO | INPUT | Título resumido do produto |
| D | CUSTO | INPUT | Custo unitário |
| E | EAN | INPUT | Código de barras como texto |
| F | NCM | INPUT | Código fiscal |
| G | MARCA | INPUT | Marca/fornecedor |
| H | CUSTO ESTOQUE TOTAL | FORMULA | Estoque × custo |

## Regra operacional crítica

- Nunca usar o mapeamento antigo com B vazio, C=SKU, D=STATUS, E=PRODUTO, F=CUSTO, G=EAN, H=NCM, I=MARCA, J/K fórmulas.
- Esse mapeamento antigo desloca todas as colunas e causa cadastro errado.
- Ao adicionar linhas novas, preencher somente A:G e preservar a fórmula/formatação de H copiando linha modelo equivalente.
- Não escrever nada em I:K; essas colunas não fazem parte da estrutura atual da aba ESTOQUE.

## Importância da aba ESTOQUE

Esta aba alimenta as abas de marketplace por lookup:
- MELI/SHOPEE usam principalmente EAN para puxar dados fiscais/marca.
- AMAZON usa principalmente SKU BASE para puxar dados fiscais/marca.

Se o produto não estiver correto na aba ESTOQUE, as abas de marketplace ficam com lookup quebrado ou dados fiscais/marca errados.
