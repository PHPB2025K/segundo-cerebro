---
name: fullstack-dev
description: >
  Desenvolvimento full-stack sênior: criar apps web, APIs, SaaS, sistemas internos e automações.
  Use quando: criar app Next.js, criar API REST/tRPC, frontend React, backend Node/FastAPI,
  deploy no VPS ou Vercel, configurar banco de dados PostgreSQL/Supabase, auth/RBAC,
  integração Stripe, multi-tenancy, feature flags, integração AI/LLM (OpenAI, Claude),
  TypeScript avançado, testes (Vitest/Playwright), Docker, CI/CD, monitoramento, Nginx, PM2,
  refatorar código, revisar arquitetura, scaffoldar projeto, bootstrap novo SaaS.
  Cobre projetos SimulImport, Bidspark e Canguu (Pedro Broglio / GB Importadora).
  Triggers: "criar app", "criar API", "novo projeto", "fazer deploy", "Next.js", "React",
  "Supabase", "FastAPI", "TypeScript", "SaaS", "fullstack", "backend", "frontend", "database",
  "auth", "Stripe", "autenticação", "banco de dados", "Docker", "CI/CD", "testes", "AI".
---

# Fullstack Dev — Stack & Workflows

> Usado por [[agents/builder/IDENTITY|Builder]]

## Stack Padrão (Pedro / GB Importadora)

| Camada | Tecnologia |
|--------|-----------|
| Frontend | Next.js 15 (App Router) + TypeScript strict |
| UI | shadcn/ui + Tailwind CSS v4 + cva |
| State | TanStack Query (server) + Zustand (client) |
| Forms | React Hook Form + Zod |
| Auth | Supabase Auth |
| DB | Supabase PostgreSQL + RLS |
| ORM | Drizzle ORM |
| Payments | Stripe |
| Email | Resend |
| Deploy | Vercel (frontend) ou VPS 187.77.237.231 (backend/workers) |
| Monit | Sentry + Uptime Kuma |
| Queue | BullMQ + Redis (workers/jobs assíncronos) |
| AI | Anthropic Claude + OpenAI GPT-4o |

## Decisão de Stack por Projeto

```
Precisa de UI + banco + auth?
  → Next.js 15 + Supabase + shadcn/ui (SimulImport, Bidspark frontend)

Precisa de workers persistentes / cron jobs?
  → BullMQ + Redis no VPS (Bidspark sync, Canguu)

Precisa de processamento Python (ML, scrapers)?
  → FastAPI + SQLAlchemy no VPS

Landing page / marketing site?
  → Astro (máxima performance)

API standalone (sem SSR)?
  → Fastify ou Hono (edge)

Agente de IA com RAG?
  → Claude/OpenAI + pgvector (Supabase) + BullMQ
```

## Infra Pedro

| Recurso | Detalhe |
|---------|---------|
| VPS | Ubuntu 187.77.237.231 — Node.js v22, Python 3.12, Docker, Nginx, PM2 |
| GitHub | PHPB2025K |
| DB | Supabase (PostgreSQL + RLS + Edge Functions) |
| Cloud | AWS (S3, etc.) |
| DNS/SSL | Nginx + Certbot no VPS |

## Quick Start — Iniciar Projeto

### Next.js + Supabase (padrão SaaS)

```bash
# Script automatizado (recomendado)
bash /root/.openclaw/workspace/skills/dev/fullstack-dev/scripts/init-nextjs-project.sh \
  --name meu-saas \
  --dir ~/projects

# Manual
pnpm create next-app@latest meu-saas --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"
cd meu-saas
pnpm add @supabase/supabase-js @supabase/ssr drizzle-orm postgres
pnpm add @tanstack/react-query react-hook-form @hookform/resolvers zod
pnpm add class-variance-authority clsx tailwind-merge lucide-react
pnpm add -D drizzle-kit
pnpm dlx shadcn@latest init
```

### FastAPI + PostgreSQL

```bash
bash /root/.openclaw/workspace/skills/dev/fullstack-dev/scripts/init-fastapi-project.sh \
  --name meu-api \
  --dir ~/projects
```

### Deploy no VPS

```bash
bash /root/.openclaw/workspace/skills/dev/fullstack-dev/scripts/deploy-vps.sh \
  --app meu-saas \
  --host 187.77.237.231 \
  --mode pm2
```

## Estrutura de Pastas (Next.js)

```
src/
├── app/
│   ├── (auth)/           # login, signup, callback
│   ├── (marketing)/      # landing, pricing, about
│   ├── (app)/            # dashboard autenticado
│   │   ├── layout.tsx    # sidebar + navbar
│   │   ├── dashboard/
│   │   └── settings/
│   └── api/
│       └── webhooks/
├── components/
│   ├── ui/               # shadcn/ui (não editar diretamente)
│   └── [feature]/        # componentes por feature
├── features/             # feature slices (componentes + hooks + actions)
│   ├── auth/
│   ├── billing/
│   └── [domain]/
├── lib/
│   ├── db/               # Drizzle schema + connection
│   ├── auth.ts           # helpers de auth
│   ├── stripe.ts
│   └── utils.ts          # cn(), formatters
└── types/                # types globais
```

## Patterns Essenciais

### Server Component (buscar dados)
```tsx
// app/dashboard/page.tsx
export default async function DashboardPage() {
  const user = await requireAuth() // redirect se não autenticado
  const data = await db.query.orders.findMany({
    where: eq(orders.userId, user.id),
    limit: 10,
    orderBy: [desc(orders.createdAt)]
  })
  return <OrdersList orders={data} /> // pode ser Client Component
}
```

### Server Action (mutações)
```tsx
'use server'
export async function createItem(formData: FormData) {
  const user = await requireAuth()
  const parsed = Schema.safeParse(Object.fromEntries(formData))
  if (!parsed.success) return { error: parsed.error.flatten() }
  await db.insert(items).values({ ...parsed.data, userId: user.id })
  revalidatePath('/dashboard')
  return { success: true }
}
```

### Middleware (proteção de rotas)
```tsx
// middleware.ts
export async function middleware(request: NextRequest) {
  const session = await getSupabaseSession(request)
  if (request.nextUrl.pathname.startsWith('/dashboard') && !session) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  return NextResponse.next()
}
export const config = { matcher: ['/dashboard/:path*', '/settings/:path*'] }
```

### RLS no Supabase (segurança)
```sql
ALTER TABLE minha_tabela ENABLE ROW LEVEL SECURITY;
CREATE POLICY "users_own_data" ON minha_tabela
  FOR ALL USING (user_id = auth.uid());
```

## Regras de Ouro

1. **RLS obrigatório** em toda tabela no Supabase — nunca expor dado sem policy
2. **Validar com Zod** no server — nunca confiar no client
3. **service_role key** apenas no server — nunca expor no client
4. **Webhook Stripe** = única fonte de verdade para status de assinatura
5. **Idempotência** em webhooks — salvar event.id antes de processar
6. **Índice em foreign keys** — sempre criar index em colunas de join
7. **Monolito primeiro** — escalar horizontal antes de microservices
8. **Conventional commits** — feat/fix/chore/refactor/test

## Referências Detalhadas

Ler conforme necessidade:

| Tópico | Arquivo |
|--------|---------|
| React 19, Next.js 15, shadcn/ui, state management | `references/frontend.md` |
| Fastify, FastAPI, REST, tRPC, WebSockets | `references/backend.md` |
| PostgreSQL, Supabase, Drizzle, Redis | `references/database.md` |
| Supabase Auth, NextAuth, RBAC, RLS, OWASP | `references/auth-security.md` |
| Docker, Nginx, PM2, Vercel, CI/CD, monitoramento | `references/infrastructure.md` |
| TypeScript avançado, generics, Zod | `references/typescript-patterns.md` |
| Stripe, multi-tenancy, feature flags, onboarding | `references/saas-patterns.md` |
| OpenAI, Claude, streaming, RAG, pgvector | `references/ai-integration.md` |
| Vitest, Playwright, E2E, mocking | `references/testing.md` |

## Template Base

Assets em `assets/nextjs-starter/` — package.json, tsconfig, tailwind config, next.config, .env.example, estrutura inicial.

Copiar como base: `cp -r assets/nextjs-starter/ ~/projects/meu-projeto`

---
## Referências
- [[skills/dev/fullstack-dev/references/ai-integration|AI Integration]]
- [[skills/dev/fullstack-dev/references/auth-security|Auth & Security]]
- [[skills/dev/fullstack-dev/references/backend|Backend]]
- [[skills/dev/fullstack-dev/references/database|Database]]
- [[skills/dev/fullstack-dev/references/frontend|Frontend]]
- [[skills/dev/fullstack-dev/references/infrastructure|Infrastructure]]
- [[skills/dev/fullstack-dev/references/saas-patterns|SaaS Patterns]]
- [[skills/dev/fullstack-dev/references/testing|Testing]]
- [[skills/dev/fullstack-dev/references/typescript-patterns|TypeScript Patterns]]
