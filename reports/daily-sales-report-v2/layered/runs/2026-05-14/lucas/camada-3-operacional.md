# Camada 3 — Operacional — Lucas / SHOPEE

Data analisada: 2026-05-14 — 00:00–23:59 BRT
Fonte: Supabase `orders` em janela BRT, cancelados excluídos dos totais válidos.

## Visão objetiva da plataforma
- Faturamento: R$ 4.217,42
- Pedidos: 74
- Ticket médio: R$ 56,99
- Cancelamentos: 2

## Raio-X por unidade operacional
- Shopee — Budamix Store: 35 pedidos, R$ 1.225,37, ticket R$ 35,01, 0 cancelamentos; vs 30d: pedidos -59,9%, GMV -64,2%; top3 91,4%.
- Shopee — Budamix Oficial / Conta 2: 16 pedidos, R$ 1.222,74, ticket R$ 76,42, 2 cancelamentos; vs 30d: pedidos -52,2%, GMV -37,6%; top3 62,5%.
- Shopee — Budamix Shop / Conta 3: 23 pedidos, R$ 1.769,31, ticket R$ 76,93, 0 cancelamentos; vs 30d: pedidos -19,0%, GMV -7,5%; top3 78,3%.

## O que precisa ser investigado pela Granular
- Shopee — Budamix Store: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Store: explicar variação forte de pedidos vs 30d (-59,9%).
- Shopee — Budamix Store: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Oficial / Conta 2: explicar variação forte de pedidos vs 30d (-52,2%).
- Shopee — Budamix Oficial / Conta 2: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Shop / Conta 3: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Shop / Conta 3: avaliar risco de concentração de mix/top produtos.
