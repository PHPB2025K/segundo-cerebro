# Recalculo compras canecas — 60 dias completos (2026-04-10 a 2026-06-08 BRT)

## Resumo executivo

- Comprar agora: Tulipa Preto (840), Tulipa Branco (480).
- Monitorar/comprar se fornecedor for fechar pedido: Tulipa Rosa, Tulipa Azul, Tulipa Verde, Tulipa Amarelo, Paris Preto, Canelada Preto, Reta Rosa, Reta Preto, Reta Branco, Reta Azul, Reta Verde, Reta Amarelo.
- Não comprar agora: 10 combinações com cobertura >=45 dias.
- Fonte: Supabase orders + physical_inventory_items. Pedidos brutos na janela: 18074; cancelados ignorados: 1483; pedidos com canecas mapeadas: 2651; itens/linhas mapeadas: 3114. Último sync estoque: 2026-06-09T21:18:06.210486+00:00.

## Tabela consolidada

| Modelo | Cor | ML | Shopee total (Store/C2/C3) | Amazon | Total 60d | Média diária | Média semanal | Estoque atual | Inbound | Cobertura dias | Compra semanal rec. | Prioridade |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Tulipa | Rosa | 170 | 1189 (487/339/363) | 114 | 1473 | 24.55 | 171.8 | 797 | 0 | 32.5 | 0 | Monitorar |
| Tulipa | Preto | 170 | 1189 (487/339/363) | 462 | 1821 | 30.35 | 212.5 | 12 | 0 | 0.4 | 840 | Comprar agora |
| Tulipa | Branco | 170 | 1189 (487/339/363) | 384 | 1743 | 29.05 | 203.3 | 337 | 0 | 11.6 | 480 | Comprar agora |
| Tulipa | Azul | 170 | 1189 (487/339/363) | 66 | 1425 | 23.75 | 166.2 | 567 | 0 | 23.9 | 108 | Comprar/monitorar |
| Tulipa | Verde | 170 | 1189 (487/339/363) | 132 | 1491 | 24.85 | 174.0 | 494 | 0 | 19.9 | 204 | Comprar/monitorar |
| Tulipa | Amarelo | 170 | 1189 (487/339/363) | 156 | 1515 | 25.25 | 176.8 | 357 | 0 | 14.1 | 360 | Comprar/monitorar |
| Paris | Rosa | 93 | 382 (313/63/6) | 203 | 678 | 11.3 | 79.1 | 696 | 0 | 61.6 | 0 | Não comprar |
| Paris | Preto | 93 | 232 (175/51/6) | 203 | 528 | 8.8 | 61.6 | 267 | 0 | 30.3 | 0 | Monitorar |
| Paris | Branco | 93 | 754 (655/93/6) | 107 | 954 | 15.9 | 111.3 | 858 | 0 | 54.0 | 0 | Não comprar |
| Paris | Azul | 93 | 232 (175/51/6) | 47 | 372 | 6.2 | 43.4 | 504 | 0 | 81.3 | 0 | Não comprar |
| Paris | Verde | 93 | 232 (175/51/6) | 47 | 372 | 6.2 | 43.4 | 376 | 0 | 60.6 | 0 | Não comprar |
| Paris | Amarelo | 93 | 232 (175/51/6) | 59 | 384 | 6.4 | 44.8 | 342 | 0 | 53.4 | 0 | Não comprar |
| Canelada | Rosa | 41 | 539 (0/16/523) | 33 | 613 | 10.22 | 71.5 | 766 | 0 | 75.0 | 0 | Não comprar |
| Canelada | Preto | 365 | 17 (0/16/1) | 45 | 427 | 7.12 | 49.8 | 190 | 0 | 26.7 | 0 | Comprar/monitorar |
| Canelada | Branco | 77 | 131 (102/16/13) | 33 | 241 | 4.02 | 28.1 | 770 | 0 | 191.7 | 0 | Não comprar |
| Canelada | Azul | 137 | 17 (0/16/1) | 33 | 187 | 3.12 | 21.8 | 476 | 0 | 152.7 | 0 | Não comprar |
| Canelada | Verde | 209 | 17 (0/16/1) | 33 | 259 | 4.32 | 30.2 | 293 | 0 | 67.9 | 0 | Não comprar |
| Canelada | Amarelo | 29 | 41 (24/16/1) | 33 | 103 | 1.72 | 12.0 | 334 | 0 | 194.6 | 0 | Não comprar |
| Reta | Rosa | 211 | 441 (20/348/73) | 28 | 680 | 11.33 | 79.3 | 0 | 480 | 42.4 | 0 | Monitorar |
| Reta | Preto | 211 | 441 (20/348/73) | 52 | 704 | 11.73 | 82.1 | 56 | 360 | 35.5 | 0 | Monitorar |
| Reta | Branco | 211 | 441 (20/348/73) | 46 | 698 | 11.63 | 81.4 | 0 | 480 | 41.3 | 0 | Monitorar |
| Reta | Azul | 211 | 441 (20/348/73) | 10 | 662 | 11.03 | 77.2 | 114 | 360 | 43.0 | 0 | Monitorar |
| Reta | Verde | 211 | 441 (20/348/73) | 22 | 674 | 11.23 | 78.6 | 66 | 360 | 37.9 | 0 | Monitorar |
| Reta | Amarelo | 211 | 441 (20/348/73) | 28 | 680 | 11.33 | 79.3 | 77 | 360 | 38.6 | 0 | Monitorar |

## Critério usado

- Janela: últimos 60 dias completos em BRT, de 10/04/2026 a 08/06/2026, excluindo 09/06 por dia parcial.
- Cancelados excluídos por status contendo cancel.
- Kits coloridos: 1 unidade de cada uma das seis cores do modelo. Kits cor única: 6 unidades da mesma cor/modelo. Brasil/Copa Tulipa: 3 verdes + 3 amarelas.
- Estoque: soma por modelo/cor na tabela física, incluindo SKUs equivalentes por fornecedor quando cadastrados separadamente; inbound só para Reta conforme memória do projeto.
- Recomendação: cobertura-alvo de 28 dias por causa de pedido semanal + lead time pessimista de 8 dias + colchão operacional. Compra sugerida = déficit até 28 dias, arredondado para múltiplos de 12 unidades; se déficit menor que 25% da demanda semanal, recomendação zerada.
- Prioridade: comprar agora <14 dias; comprar/monitorar 14–28; monitorar 28–45; não comprar >45.

## Alertas de qualidade dos dados

- 959 unidades/linhas caíram no filtro amplo de auditoria por conter termos ambíguos como “reta” dentro de “retangular”; a amostra principal é de potes, não de canecas. Não tratei como demanda de canecas sem SKU/título seguro. Top 10: 211× KIT2YW1520 | Conjunto 2 Potes Vidro 1520ml Retangular Hermético 4 Travas Vedação Marmita; 193× KIT2YW1520AZ | Kit 2 Potes Vidro 1520ml Retangular Hermético 4 Travas Vedação Mantimentos Marmi; 94× KIT3S099 | Kit 3 Potes Vidro Retangulares Hermético Vedação Tampa 4 Travas Marmita; 89× KIT2YW1520 | 2 Potes de Vidro 1520ml Retangular Hermético Marmita Mantimentos 4 Travas; 56× KIT4YW1520 | 4 Potes de Vidro 1520ml Retangular Hermético Marmita Mantimentos 4 Travas; 50× KIT3S099 | Conjunto 3 Potes Vidro Retangulares Hermético: Tampa 4 Travas e Vedação para Mar; 47× IMB501P_T | Kit Conjunto de 5 Potes de Vidro Redondo, Tampa Preta - Conjunto de Tigelas Redo; 24× KIT6S100 | Kit 6 Potes de Vidro Hermético Retangular 4 Travas Marmita de Vidro com Tampa; 24× KIT4YW1050 | Conjunto 4 Potes Vidro 1050ml Retangular Hermético Vedação 4 Travas BPA Free; 23× KIT4YW1520 | Conjunto 4 Potes Vidro 1520ml Retangular Hermético Vedação 4 Travas Marmita
- Canelada possui BOM oficial incompleto no banco para algumas cores; neste recálculo foram aplicadas regras explícitas K6CAN250* = 6 unidades da cor e K6CAN250 colorida = 1 por cor.
- Paris usa SKU comercial XCP00* e estoque físico 54171*_B; mapeamento foi feito por regra de cor, não por BOM nativo completo.
- Tulipa direta TL250* e Reta direta CAR200* em Amazon são kits de 6 pelo título; regra aplicada explicitamente.
- Shopee foi separada por shop_id conhecido: 448649947 Store, 442066454 Conta 2, 860803675 Conta 3. Qualquer shop_id novo apareceria em alerta/fora das colunas principais.
- Estoque atual inclui SKUs por fornecedor alternativo (HR/RR/Guinho) quando equivalentes por modelo/cor; se Pedro quiser só LU, a cobertura cai em Tulipa e Canelada.

## SKUs brutos mapeados mais relevantes

- CTL002: 1189 linhas/unidades de pedido antes do desmembramento
- KIT6CAR200: 441 linhas/unidades de pedido antes do desmembramento
- XCP002: 366 linhas/unidades de pedido antes do desmembramento
- TL6250: 224 linhas/unidades de pedido antes do desmembramento
- CLR002: 211 linhas/unidades de pedido antes do desmembramento
- XCP001: 98 linhas/unidades de pedido antes do desmembramento
- K6CAN250R: 91 linhas/unidades de pedido antes do desmembramento
- TL250P: 68 linhas/unidades de pedido antes do desmembramento
- K6CAN250: 67 linhas/unidades de pedido antes do desmembramento
- K6CAN250P: 60 linhas/unidades de pedido antes do desmembramento
- TL250B: 55 linhas/unidades de pedido antes do desmembramento
- XCP003: 52 linhas/unidades de pedido antes do desmembramento
- K6CAN250VD: 32 linhas/unidades de pedido antes do desmembramento
- K6CAN250B: 29 linhas/unidades de pedido antes do desmembramento
- XCP004: 27 linhas/unidades de pedido antes do desmembramento
- K6CAN250AZ: 20 linhas/unidades de pedido antes do desmembramento
- TL250A: 17 linhas/unidades de pedido antes do desmembramento
- TL250V: 13 linhas/unidades de pedido antes do desmembramento
- CAR200-Colorida: 10 linhas/unidades de pedido antes do desmembramento
- TL250R: 10 linhas/unidades de pedido antes do desmembramento
- CAR200P: 7 linhas/unidades de pedido antes do desmembramento
- CAR200B: 6 linhas/unidades de pedido antes do desmembramento
- K6CAN250AM: 6 linhas/unidades de pedido antes do desmembramento
- XCP007: 3 linhas/unidades de pedido antes do desmembramento
- CAR200AM: 3 linhas/unidades de pedido antes do desmembramento
- CAR200R: 3 linhas/unidades de pedido antes do desmembramento
- CAR200VD: 2 linhas/unidades de pedido antes do desmembramento
- TL250Z: 2 linhas/unidades de pedido antes do desmembramento
- XCP006: 1 linhas/unidades de pedido antes do desmembramento
- XCP005: 1 linhas/unidades de pedido antes do desmembramento