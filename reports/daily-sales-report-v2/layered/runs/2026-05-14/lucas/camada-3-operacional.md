# Camada 3 — Operacional — Lucas / SHOPEE

Data analisada: 2026-05-14 — 00:00–23:59 BRT
Fonte: Supabase `orders` em janela BRT, cancelados excluídos dos totais válidos.

## Visão objetiva da plataforma
- Faturamento: R$ 4.257,66
- Pedidos: 75
- Ticket médio: R$ 56,77
- Cancelamentos: 1

## Raio-X por unidade operacional
- Shopee — Budamix Store: 35 pedidos, R$ 1.225,37, ticket R$ 35,01, 0 cancelamentos; vs 30d: pedidos -60,1%, GMV -64,2%; top3 91,4%.
- Shopee — Budamix Oficial / Conta 2: 17 pedidos, R$ 1.262,98, ticket R$ 74,29, 1 cancelamentos; vs 30d: pedidos -49,3%, GMV -35,6%; top3 58,8%.
- Shopee — Budamix Shop / Conta 3: 23 pedidos, R$ 1.769,31, ticket R$ 76,93, 0 cancelamentos; vs 30d: pedidos -19,0%, GMV -7,5%; top3 78,3%.

## O que precisa ser investigado pela Granular
- Shopee — Budamix Store: validar `high_top3_concentration` — Alta concentracao nos top 3 produtos (>=70%).
- Shopee — Budamix Store: explicar variação forte de pedidos vs 30d (-60,1%).
- Shopee — Budamix Store: avaliar risco de concentração de mix/top produtos.
- Shopee — Budamix Oficial / Conta 2: explicar variação forte de pedidos vs 30d (-49,3%).
- Shopee — Budamix Shop / Conta 3: validar `high_top3_concentration` — Alta concentracao nos top 3 produtos (>=70%).
- Shopee — Budamix Shop / Conta 3: avaliar risco de concentração de mix/top produtos.
