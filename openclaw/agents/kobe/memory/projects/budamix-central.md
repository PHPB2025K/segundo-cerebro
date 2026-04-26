---
title: "budamix-central"
created: 2026-04-26
type: memory-project
agent: kobe
status: active
tags:
  - agent/kobe
  - memory
  - project
---
# Projeto: Budamix Central

## Status: 🟡 Em produção — Sprint de polish necessário

## O que é
Dashboard operacional da GB Importadora. Consolida dados de vendas, estoque, preços e performance das 3 plataformas (ML, Shopee, Amazon) em tempo real.

## Stack
- Frontend: Next.js + shadcn/ui + Tailwind
- Backend: Supabase (Auth + DB + Views)
- Hosting: VPS (central.gbformulario.com via Traefik)
- Repo: github.com/PHPB2025K/budamix-central
- PM2: `pm2 restart budamix-central`
- Build: `NODE_OPTIONS=--max-old-space-size=1024 npx next build`

## Módulos
| Módulo | Score | Status |
|--------|-------|--------|
| Home (KPIs + HealthStatus) | 6/10 | KPIs com bug timezone, HealthStatus fake |
| Vendas | 8/10 | Funcional, dados reais |
| Live Sales | 8/10 | Funcional, fullscreen, dados reais (R$10.974) |
| Estoque Full | 7/10 | Funcional, seletor SKU limitado |
| Preços v2 | 8/10 | Cross-channel, cache 0.009s |
| Envios v2 | 7/10 | Funcional |
| Curva ABC | 5/10 | Período fake, movimento fake |
| Settings | 0/10 | Não existe (404) |

## Auditoria Pedro (30/03/2026) — Média 7.3/10

### 6 Problemas Críticos
1. **Layout duplicado** — `src/app/dashboard/layout.tsx` e `src/app/(dashboard)/layout.tsx` idênticos. Sidebar renderiza DUAS vezes nas páginas Estoque e Live. Fix: deletar `src/app/dashboard/layout.tsx`, mover rotas pra `(dashboard)/`.
2. **API routes sem auth** — Middleware marca `/api/*` como público. Endpoints `/api/kpis`, `/api/live-sales`, `/api/prices/cross-channel` expostos sem autenticação. Dados de faturamento visíveis pra qualquer pessoa.
3. **Settings page não existe** — Link na sidebar dá 404. Precisa: meta diária (goal), config de sync, status integrações.
4. **HealthStatus fake** — Semáforo de canais (ML, Shopee, Amazon) usa `toHealthData()` hardcoded. Nunca consulta status real. Deveria usar `sync_log`.
5. **Curva ABC ignora período** — API `/api/abc` não filtra por `order_date`. Botões 7d/30d/90d decorativos.
6. **Movimento na Curva ABC fake** — Campo `movimento` hardcoded como "same". Nunca compara curva atual vs anterior.

### Problemas Médios
- Botão "Sync" na sidebar fake (setTimeout, não chama API)
- "Last sync: agora mesmo" hardcoded
- LiveClock duplicado no header desktop do Live Sales
- CSS vars `--ml`, `--shopee`, `--amazon` não existem (deveria ser `--ml-brand`)
- Font `@import` duplicado com `next/font`
- Seletor SKU no histórico Estoque: só 8 primeiros, sem scroll/busca
- API legacy `/api/prices/route.ts` não usada
- Zustand e Drizzle ORM no package.json sem uso
- Nenhum módulo tem ErrorBoundary React

### Sprint de Polish (Prioridade)
1. Layout duplicado (cirúrgico — 15min)
2. Auth das APIs (segurança — 1 Builder job)
3. Settings page (1 Builder job)
4. Curva ABC real — período + movimento (1 Builder job)
5. HealthStatus real com sync_log (1 Builder job)
6. Cleanup: CSS vars, font duplicada, deps mortas, ErrorBoundary

## Dados
- Supabase: 40.000+ orders, 950 products, 1.028 price_history
- Faturamento real no dashboard: R$10.974 (Live Sales validado)
- 57 SKUs sem cost_price na fulfillment_inventory
- KPIs com bug timezone (UTC vs BRT, diferença R$1.677)

## Histórico de entregas
- 24/03: MVP (57 arquivos, Builder)
- 25/03: Live Sales no ar com dados reais
- 26/03: 10 entregas (sync Shopee, Amazon paginação, SKU mapping, Envios v2, Preços v2)
- 27/03: 11 entregas (Preços cross-channel, cache, Curva ABC sub-abas, React keys fix)
- 30/03: Auditoria completa Pedro (média 7.3/10, 6 críticos, 9 médios)
