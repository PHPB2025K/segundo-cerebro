---
tipo: referencia
projeto: Canggu
status: ativo
tags:
  - canggu
  - frontend
  - react
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Frontend

> Monorepo `~/Documents/05-Projetos-Codigo/budamix-ai-agent/src/` — ~7.657 LOC TS/TSX.
> Vite SPA deployada no Vercel.

## Stack

| Camada | Tecnologia |
|---|---|
| Build tool | Vite 6.0.5 |
| UI framework | React 19.0.0 |
| TypeScript | 5.7.2 strict + `noUncheckedIndexedAccess: true` + `noUnusedLocals/Parameters: true` |
| Roteamento | react-router-dom 7.1.1 (BrowserRouter + Routes) |
| Estado | Zustand 5.0.3 (4 stores) |
| UI components | Radix UI + shadcn 3.8.5 |
| Styling | Tailwind CSS 4 + class-variance-authority |
| Realtime | Supabase Realtime via `useRealtimeSubscription` hook |
| Charts | Recharts 2.15 |
| Forms | Hook forms via Radix (sem react-hook-form declarado) |
| Toasts | Sonner 2.0.7 |

## Rotas (14 totais)

| Path | Componente | Proteção | Propósito |
|---|---|---|---|
| `/login` | `LoginPage` | pública | Supabase Auth login |
| `/` | redirect → `/dashboard` | — | — |
| `/dashboard` | `DashboardPage` | ProtectedRoute | KPIs, gráficos, alertas |
| `/conversations` | `ConversationsPage` | ProtectedRoute | Lista + filtros (`ConversationFilters.tsx` com status=escalated) |
| `/conversations/:id` | `ConversationDetailPage` | ProtectedRoute | ChatView + envio via `send-human-message` |
| `/products` | `ProductsPage` | ProtectedRoute | Catálogo CRUD |
| `/products/:id` | `ProductDetailPage` | ProtectedRoute | Edição |
| `/customers` | `CustomersPage` | ProtectedRoute | Lista |
| `/customers/:id` | `CustomerDetailPage` | ProtectedRoute | Perfil |
| `/policies` | `PoliciesPage` | ProtectedRoute | Editor políticas + FAQ |
| `/escalations` | `EscalationsPage` | ProtectedRoute | Fila humana |
| `/analytics` | `AnalyticsPage` | ProtectedRoute | Métricas |
| `/settings` | `SettingsPage` | ProtectedRoute | Configuração do agente |
| `*` | redirect → `/dashboard` | — | Fallback |

Pendência B2: adicionar rota `/operations` com 3 widgets (msgs sem agent_response, embeddings NULL 7d, incidentes de áudio).

## Zustand stores (4)

- `auth-store.ts` — usuário logado, session
- `conversations-store.ts` — lista + selected + subscriptions
- `escalations-store.ts` — fila humana
- `products-store.ts` — catálogo

**Sem React Query / Redux / Jotai.** Fetching é manual via supabase-js client.

## Integração Supabase

- **Cliente instanciado:** `src/integrations/supabase/client.ts` (referenciado no sumário B5 como `src/lib/supabase.ts:13` — conferir path exato no repo)
- **Credentials:** via `import.meta.env.VITE_SUPABASE_URL` + `VITE_SUPABASE_ANON_KEY` (padrão Vite, com guard que lança Error se ausente — **seguro**)
- **Frontend zero refs a `service_role`** (confirmado em [[decisoes#ADR-001]] §21d)

### Tabelas usadas em `.from()`
`agent_config, analytics_daily, conversations, customers, escalations, faq, messages, policies, product_listings, products`

### RPCs
Nenhum `.rpc()` chamado do frontend.

### Realtime subscriptions
`src/hooks/useRealtimeSubscription.ts` — hook genérico com `.channel()` + `.on('postgres_changes', ...)`. Consumido dinamicamente pelos stores (`conversations-store` subscreve em `messages` + `conversations`).

## Chamadas a edge functions (apenas 2 lugares)

| Função | Método | Onde |
|---|---|---|
| `send-human-message` | fetch `POST /functions/v1/send-human-message` | `src/lib/api.ts:238` |
| [[edge-functions\|sync-product-embedding]] | `supabase.functions.invoke()` | `src/lib/api.ts:328` |

⚠️ Bug confirmado em [[debitos-tecnicos]] achado #14: [[edge-functions|send-human-message]] retorna `{success: true, sent: false}` quando Evolution falha — frontend não mostra toast de erro.

## Qualidade

- **Testes: 0** (sem Jest/Vitest/Playwright)
- **Lint:** ESLint v9 + typescript-eslint 8 + eslint-plugin-react-hooks + eslint-plugin-react-refresh. Script `lint` no package.json.
- **Prettier:** nenhum config localizado.
- **TSConfig `include`:** `["src"]` — **edge functions (Deno) ficam fora do tsc**. Abordado em [[debitos-tecnicos#B5]].

## Deploy

- **Target:** Vercel (`vercel.json` com rewrite SPA `/(.*)` → `/index.html`)
- **Dockerfiles:** nenhum
- **docker-compose:** nenhum
- **GitHub Actions:** **ausente** (achado #22 — abordado em B5)

## Componentes de chat

Identificados em `src/components/conversations/`:
- `ConversationFilters.tsx` — filtro status incluindo `escalated`
- `ChatView`, `MessageBubble` — embutidos em `ConversationDetailPage` (não extraídos ainda)

Total componentes (sumário B4 do histórico): 39 + 8 hooks + 4 stores.

## Evidência completa

- Sumário B1–B10 do monorepo: `~/audit-canggu-forensics/RAW/B_monorepo/01_summary.md`
- Seções §B1 (estrutura), §B4 (rotas), §B5 (Supabase), §B6 (edge calls)
