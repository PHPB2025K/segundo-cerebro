# Camada 3 — Operacional — Lucas / SHOPEE

Data analisada: 2026-05-13 — 00:00–23:59 BRT
Fonte: Supabase `orders` em janela BRT, cancelados excluídos dos totais válidos.

## Visão objetiva da plataforma
- Faturamento: R$ 6.265,18
- Pedidos: 124
- Ticket médio: R$ 50,53
- Cancelamentos: 4

## Raio-X por unidade operacional
- Shopee — Budamix Store: 78 pedidos, R$ 3.423,89, ticket R$ 43,90, 2 cancelamentos; vs 30d: pedidos -14,2%, GMV -3,2%; top3 90,4%.
- Shopee — Budamix Oficial / Conta 2: 14 pedidos, R$ 973,32, ticket R$ 69,52, 2 cancelamentos; vs 30d: pedidos -60,0%, GMV -51,8%; top3 61,1%.
- Shopee — Budamix Shop / Conta 3: 32 pedidos, R$ 1.867,97, ticket R$ 58,37, 0 cancelamentos; vs 30d: pedidos +10,7%, GMV -3,9%; top3 84,4%.

## O que precisa ser investigado pela Granular
- Shopee — Budamix Store: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Store: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Oficial / Conta 2: explicar variação forte de pedidos vs 30d (-60,0%).
- Shopee — Budamix Oficial / Conta 2: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Shop / Conta 3: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Shop / Conta 3: avaliar risco de concentração de mix/top produtos.
