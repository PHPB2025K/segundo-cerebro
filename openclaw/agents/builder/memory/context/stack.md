---
title: "stack"
created: 2026-04-14
type: agent
agent: builder
status: active
tags:
  - agent/builder
---

# Stack & Padrões — Builder

_Padrões de tecnologia definidos para os projetos da GB._
_Atualizado: 2026-03-23_

---

## Stack Padrão

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Frontend | Next.js 15 + React 19 | SSR, API Routes, ecosystem |
| Styling | Tailwind CSS + shadcn/ui | Rápido, consistente, componentizado |
| Backend (full-stack) | Next.js API Routes + Server Actions | Sem necessidade de backend separado |
| Backend (standalone) | FastAPI (Python) | Performance, typing, ML ecosystem |
| ORM | Drizzle | Type-safe, lightweight, Postgres-first |
| DB | Supabase (Postgres) | Auth + DB + Storage + Realtime integrados |
| Auth | Supabase Auth | Integrado com DB, social login, RLS |
| Deploy (SaaS) | Vercel | Zero config para Next.js, preview deploys |
| Deploy (interno) | Docker + VPS | Controle total, custo fixo |
| Pagamentos | Stripe | Padrão de mercado, SDK robusto |
| Package manager | pnpm | Rápido, disk efficient |
| Linguagem | TypeScript (strict) | Type safety obrigatório |

## Conventions

### Estrutura de projeto Next.js
```
src/
├── app/              ← App Router (pages, layouts, API routes)
├── components/       ← Componentes reutilizáveis
│   └── ui/           ← shadcn/ui components
├── lib/              ← Utilities, helpers, configurações
├── hooks/            ← Custom hooks
├── types/            ← TypeScript types/interfaces
└── styles/           ← Global styles (se necessário)
```

### Estrutura de projeto FastAPI
```
src/
├── api/              ← Routes/endpoints
├── core/             ← Config, security, dependencies
├── models/           ← Pydantic models
├── services/         ← Business logic
├── db/               ← Database connection, queries
└── utils/            ← Helpers
```

### Naming conventions
- **Arquivos:** kebab-case (`user-profile.tsx`)
- **Componentes:** PascalCase (`UserProfile`)
- **Funções:** camelCase (`getUserProfile`)
- **Env vars:** UPPER_SNAKE (`DATABASE_URL`)
- **DB tables:** snake_case (`user_profiles`)

### Git
- **Branches:** `feat/[descrição]`, `fix/[descrição]`, `refactor/[descrição]`
- **Commits:** Convencionais (`feat:`, `fix:`, `refactor:`, `chore:`, `docs:`)
- **Nunca** commitar direto em main (L1)
- **PR** para merge em main (quando possível)

---

## Libs Aprovadas (uso livre)

| Categoria | Lib | Versão |
|---|---|---|
| Forms | react-hook-form + zod | Latest |
| Data fetching | TanStack Query (React Query) | v5 |
| Tables | TanStack Table | v8 |
| Charts | recharts | Latest |
| Date | date-fns | Latest |
| Icons | lucide-react | Latest |
| Toast | sonner | Latest |
| State | zustand (se necessário) | Latest |

## Libs que Precisam de Aprovação

| Categoria | Motivo |
|---|---|
| Qualquer lib de auth que não seja Supabase | Decisão de stack |
| ORMs que não sejam Drizzle | Decisão de stack |
| Libs de pagamento que não sejam Stripe | Decisão de stack |
| Qualquer lib > 100kb bundle size | Performance |
