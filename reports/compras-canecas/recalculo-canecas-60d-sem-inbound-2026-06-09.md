# Recálculo compras canecas — 60 dias completos SEM inbound (2026-04-10 a 2026-06-08 BRT)

## Diferença vs cálculo anterior

- Correção aplicada: inbound de Reta foi zerado em todas as cores. O bloco “Inbound informado — 2026-06-03” foi totalmente desconsiderado.
- Antes, Reta aparecia como apenas “Monitorar” porque somava 360–480 unidades em trânsito por cor.
- Agora, Reta vira compra imediata nas 6 cores: rosa 324, preto 276, branco 336, azul 204, verde 252, amarelo 252 unidades/semana. Total Reta recomendado: 1.644 unidades.
- O restante da família mantém a mesma base de vendas/estoque do recálculo de 09/06, com cobertura recalculada usando inbound=0 para todos.

## Resumo executivo

- Comprar agora: Tulipa Preto (840), Tulipa Branco (480), Reta Rosa (324), Reta Preto (276), Reta Branco (336), Reta Azul (204), Reta Verde (252), Reta Amarelo (252).
- Comprar/monitorar: Tulipa Azul (108), Tulipa Verde (204), Tulipa Amarelo (360), Canelada Preto (0).
- Monitorar: Tulipa Rosa, Paris Preto.
- Não comprar: 10 combinações com cobertura >=45 dias.
- Fonte: Supabase orders + physical_inventory_items conforme recálculo operacional de 09/06. Pedidos brutos na janela: 18.074; cancelados ignorados: 1.483; pedidos com canecas mapeadas: 2.651; itens/linhas mapeadas: 3.114. Último sync estoque: 2026-06-09T21:18:06Z.

## Tabela consolidada

| Modelo | Cor | ML | Shopee total (Store/C2/C3) | Amazon | Total 60d | Média semanal | Estoque atual | Inbound | Cobertura dias | Compra semanal rec. | Prioridade |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tulipa | Rosa | 170 | 1189 (487/339/363) | 114 | 1473 | 171.8 | 797 | 0 | 32.5 | 0 | Monitorar |
| Tulipa | Preto | 170 | 1189 (487/339/363) | 462 | 1821 | 212.5 | 12 | 0 | 0.4 | 840 | Comprar agora |
| Tulipa | Branco | 170 | 1189 (487/339/363) | 384 | 1743 | 203.3 | 337 | 0 | 11.6 | 480 | Comprar agora |
| Tulipa | Azul | 170 | 1189 (487/339/363) | 66 | 1425 | 166.2 | 567 | 0 | 23.9 | 108 | Comprar/monitorar |
| Tulipa | Verde | 170 | 1189 (487/339/363) | 132 | 1491 | 174.0 | 494 | 0 | 19.9 | 204 | Comprar/monitorar |
| Tulipa | Amarelo | 170 | 1189 (487/339/363) | 156 | 1515 | 176.8 | 357 | 0 | 14.1 | 360 | Comprar/monitorar |
| Paris | Rosa | 93 | 382 (313/63/6) | 203 | 678 | 79.1 | 696 | 0 | 61.6 | 0 | Não comprar |
| Paris | Preto | 93 | 232 (175/51/6) | 203 | 528 | 61.6 | 267 | 0 | 30.3 | 0 | Monitorar |
| Paris | Branco | 93 | 754 (655/93/6) | 107 | 954 | 111.3 | 858 | 0 | 54.0 | 0 | Não comprar |
| Paris | Azul | 93 | 232 (175/51/6) | 47 | 372 | 43.4 | 504 | 0 | 81.3 | 0 | Não comprar |
| Paris | Verde | 93 | 232 (175/51/6) | 47 | 372 | 43.4 | 376 | 0 | 60.6 | 0 | Não comprar |
| Paris | Amarelo | 93 | 232 (175/51/6) | 59 | 384 | 44.8 | 342 | 0 | 53.4 | 0 | Não comprar |
| Canelada | Rosa | 41 | 539 (0/16/523) | 33 | 613 | 71.5 | 766 | 0 | 75.0 | 0 | Não comprar |
| Canelada | Preto | 365 | 17 (0/16/1) | 45 | 427 | 49.8 | 190 | 0 | 26.7 | 0 | Comprar/monitorar |
| Canelada | Branco | 77 | 131 (102/16/13) | 33 | 241 | 28.1 | 770 | 0 | 191.5 | 0 | Não comprar |
| Canelada | Azul | 137 | 17 (0/16/1) | 33 | 187 | 21.8 | 476 | 0 | 152.6 | 0 | Não comprar |
| Canelada | Verde | 209 | 17 (0/16/1) | 33 | 259 | 30.2 | 293 | 0 | 67.8 | 0 | Não comprar |
| Canelada | Amarelo | 29 | 41 (24/16/1) | 33 | 103 | 12.0 | 334 | 0 | 194.2 | 0 | Não comprar |
| Reta | Rosa | 211 | 441 (20/348/73) | 28 | 680 | 79.3 | 0 | 0 | 0.0 | 324 | Comprar agora |
| Reta | Preto | 211 | 441 (20/348/73) | 52 | 704 | 82.1 | 56 | 0 | 4.8 | 276 | Comprar agora |
| Reta | Branco | 211 | 441 (20/348/73) | 46 | 698 | 81.4 | 0 | 0 | 0.0 | 336 | Comprar agora |
| Reta | Azul | 211 | 441 (20/348/73) | 10 | 662 | 77.2 | 114 | 0 | 10.3 | 204 | Comprar agora |
| Reta | Verde | 211 | 441 (20/348/73) | 22 | 674 | 78.6 | 66 | 0 | 5.9 | 252 | Comprar agora |
| Reta | Amarelo | 211 | 441 (20/348/73) | 28 | 680 | 79.3 | 77 | 0 | 6.8 | 252 | Comprar agora |

## Critério usado

- Janela: 10/04/2026 a 08/06/2026 BRT, 60 dias completos, excluindo 09/06 por ser parcial.
- Cancelados excluídos por status contendo cancel.
- Kits coloridos: 1 unidade de cada uma das seis cores do modelo.
- Kits cor única: 6 unidades da mesma cor/modelo. Brasil/Copa Tulipa: 3 verdes + 3 amarelas.
- Estoque: soma por modelo/cor na tabela física, incluindo SKUs equivalentes por fornecedor quando cadastrados separadamente.
- Inbound: 0 para todos os modelos/cores, inclusive Reta.
- Recomendação: alvo 28 dias; compra sugerida = déficit até 28 dias arredondado para múltiplos de 12; déficit menor que 25% da demanda semanal fica zerado.
- Prioridade: comprar agora <14 dias; comprar/monitorar 14–28; monitorar 28–45; não comprar >=45.

## Alertas de qualidade dos dados

- Filtro amplo encontrou falsos positivos de “reta” em potes retangulares; esses itens não foram tratados como canecas sem SKU/título seguro.
- Canelada tem BOM oficial incompleto no banco para algumas cores; foram aplicadas regras explícitas K6CAN250* = 6 unidades da cor e K6CAN250 colorida = 1 por cor.
- Paris usa SKU comercial XCP00* e estoque físico 54171*_B; mapeamento por regra de cor.
- Tulipa direta TL250* e Reta direta CAR200* em Amazon são kits de 6 pelo título; regra aplicada explicitamente.
- Shopee separada por shop_id conhecido: 448649947 Store, 442066454 Conta 2, 860803675 Conta 3.
- Estoque atual inclui SKUs equivalentes por fornecedor alternativo quando cadastrados; se Pedro quiser só LU, a cobertura cai em Tulipa e Canelada.

## Arquivos

- CSV: recalculo-canecas-60d-sem-inbound-2026-06-09.csv
- MD: recalculo-canecas-60d-sem-inbound-2026-06-09.md
