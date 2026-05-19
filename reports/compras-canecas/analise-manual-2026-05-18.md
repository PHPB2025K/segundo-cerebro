# Análise manual — Reposição de Canecas Budamix

Data: 2026-05-18
Status: primeira rodada manual executada antes da criação do Agente de Compras

## Fontes consultadas

- Projeto canônico de compras de canecas.
- Memória recente: pedido do Agente de Compras + contexto Amazon Ads de Tulipa/Canelada.
- Supabase Budamix Central:
  - pedidos reais 18/02–18/05/2026;
  - estoque físico sincronizado em 18/05 20:30 BRT;
  - fulfillment/FBA/Full/listing stock sincronizado em 14–18/05;
  - raw Shopee para capturar model_sku e cor real das variações.
- Planilha/export de precificação 01/05 para validar nomenclatura/SKUs.

## Achados executivos

- A análise não tinha sido rodada antes; esta é a primeira versão manual.
- Foram analisados 27.727 pedidos; 3.433 pedidos tinham itens das famílias de canecas; 3.646 itens normalizados.
- Recomendações estão em unidades de caneca, não kits.
- Regra usada: kit cor única = 6 unidades daquela cor; kit colorido = 1 unidade por cor do respectivo modelo.
- Regra confirmada pelo Pedro: existe apenas um tipo de kit colorido por modelo, sempre com a mesma combinação das seis cores: rosa, preto, branco, azul, verde e amarelo.
- Compra semanal sugerida conservadora pelos dados atuais:
  - Tulipa: comprar rosa, preto e branco.
  - Paris: só preto aparece como compra agora, mas depende de validar se o estoque Shopee/Full não está duplicado.
  - Canelada: crítico em branco, rosa e amarelo.
  - Reta: crítico em branco e rosa; preto leve.
- Total sugerido: 423 unidades/semana no cenário atual.

## Tabela — compra semanal sugerida

| Modelo | Cor | V30 un | Média sem | Estoque total un | Cobertura | Comprar/sem |
|---|---:|---:|---:|---:|---:|---:|
| Tulipa | Rosa | 814 | 190 | 869 | 32d | 109 |
| Tulipa | Preto | 712 | 166 | 1.051 | 44d | 59 |
| Tulipa | Branco | 934 | 218 | 1.712 | 55d | 36 |
| Tulipa | Azul | 388 | 91 | 1.540 | 119d | 0 |
| Tulipa | Verde | 544 | 127 | 1.491 | 82d | 0 |
| Tulipa | Amarelo | 388 | 91 | 948 | 73d | 0 |
| Paris | Rosa | 465 | 109 | 1.876 | 121d | 0 |
| Paris | Preto | 165 | 39 | 285 | 52d | 9 |
| Paris | Branco | 321 | 75 | 4.730 | 442d | 0 |
| Paris | Azul | 129 | 30 | 3.368 | 783d | 0 |
| Paris | Verde | 123 | 29 | 3.063 | 747d | 0 |
| Paris | Amarelo | 141 | 33 | 3.170 | 675d | 0 |
| Canelada | Rosa | 172 | 40 | 168 | 29d | 25 |
| Canelada | Preto | 106 | 25 | 239 | 68d | 0 |
| Canelada | Branco | 166 | 39 | 5 | 1d | 44 |
| Canelada | Azul | 58 | 14 | 133 | 69d | 0 |
| Canelada | Verde | 58 | 14 | 281 | 145d | 0 |
| Canelada | Amarelo | 64 | 15 | 5 | 2d | 17 |
| Reta | Rosa | 273 | 64 | 165 | 18d | 53 |
| Reta | Preto | 303 | 71 | 581 | 58d | 9 |
| Reta | Branco | 345 | 81 | 243 | 21d | 62 |
| Reta | Azul | 183 | 43 | 505 | 83d | 0 |
| Reta | Verde | 159 | 37 | 431 | 81d | 0 |
| Reta | Amarelo | 117 | 27 | 537 | 138d | 0 |

## Lacunas para fechar 100%

- Faltam projeções humanas de Yasmin, Lucas e Leonardo.
- Precisa validar se linhas de Shopee/Full são estoque físico separado ou stock virtual espelhado entre contas; isso afeta principalmente Paris e Tulipa.
- Não foi localizado registro confiável de pedidos já feitos ao fornecedor fora de inbound_qty.
- ADS Amazon foi usado apenas como contexto, não como substituto de venda real.

## Próximo passo para o Agente de Compras

Transformar este método em playbook:
1. normalização SKU → modelo/cor;
2. venda real 90/30 dias;
3. conversão kit → unidade, usando a regra fixa: colorido = 1 unidade de cada uma das seis cores do modelo;
4. estoque físico + Full/FBA separado;
5. recomendação semanal com lead time pessimista de 8 dias;
6. comparação contra projeção humana por marketplace.
