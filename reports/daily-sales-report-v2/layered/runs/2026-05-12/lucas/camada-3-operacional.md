# Camada 3 — Operacional — Lucas / SHOPEE

Data analisada: 2026-05-12 — 00:00–23:59 BRT
Fonte: Supabase `orders` em janela BRT, cancelados excluídos dos totais válidos.

## Visão objetiva da plataforma
- Faturamento: R$ 5.446,35
- Pedidos: 119
- Ticket médio: R$ 45,77
- Cancelamentos: 12

## Raio-X por unidade operacional
- Shopee — Budamix Store: 76 pedidos, R$ 2.813,88, ticket R$ 37,02, 10 cancelamentos; vs 30d: pedidos -17,7%, GMV -21,9%; top3 84,8%.
- Shopee — Budamix Oficial / Conta 2: 23 pedidos, R$ 1.296,64, ticket R$ 56,38, 2 cancelamentos; vs 30d: pedidos -37,2%, GMV -38,6%; top3 79,2%.
- Shopee — Budamix Shop / Conta 3: 20 pedidos, R$ 1.335,83, ticket R$ 66,79, 0 cancelamentos; vs 30d: pedidos -32,9%, GMV -32,9%; top3 86,4%.

## O que precisa ser investigado pela Granular
- Shopee — Budamix Store: validar `reconciliation_mismatch` — Orders granular divergem da fonte canônica BRT.
- Shopee — Budamix Store: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Store: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Oficial / Conta 2: validar `reconciliation_mismatch` — Orders granular divergem da fonte canônica BRT.
- Shopee — Budamix Oficial / Conta 2: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Oficial / Conta 2: explicar variação forte de pedidos vs 30d (-37,2%).
- Shopee — Budamix Oficial / Conta 2: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Shop / Conta 3: validar `reconciliation_mismatch` — Orders granular divergem da fonte canônica BRT.
- Shopee — Budamix Shop / Conta 3: validar `high_top3_concentration` — Alta concentração nos top 3 produtos.
- Shopee — Budamix Shop / Conta 3: explicar variação forte de pedidos vs 30d (-32,9%).
- Shopee — Budamix Shop / Conta 3: avaliar risco de concentração de mix/top produtos.
