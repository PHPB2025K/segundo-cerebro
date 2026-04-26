---
title: "backend"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/fullstack-dev
---
# Backend Reference — Node/Fastify, FastAPI, APIs

## Índice
1. [Node.js + Fastify](#1-fastify)
2. [Python FastAPI](#2-fastapi)
3. [REST Design](#3-rest-design)
4. [tRPC (type-safe)](#4-trpc)
5. [WebSockets + Supabase Realtime](#5-websockets--realtime)
6. [Webhooks Seguros](#6-webhooks)
7. [Background Jobs (BullMQ)](#7-bullmq)

---

## 1. Fastify

```ts
// server.ts
import Fastify from 'fastify'
import { TypeBoxTypeProvider } from '@fastify/type-provider-typebox'
import { Type } from '@sinclair/typebox'

const app = Fastify({ logger: { level: 'info' } })
  .withTypeProvider<TypeBoxTypeProvider>()

// Auth hook global
app.addHook('onRequest', async (request, reply) => {
  const token = request.headers.authorization?.split(' ')[1]
  if (!token) return reply.status(401).send({ error: 'Unauthorized' })
  try {
    request.user = await verifyJWT(token)
  } catch {
    reply.status(401).send({ error: 'Invalid token' })
  }
})

// Route tipada
app.post('/campaigns', {
  schema: {
    body: Type.Object({
      name: Type.String(),
      budgetDaily: Type.Number({ minimum: 1 }),
      marketplace: Type.Union([Type.Literal('amazon'), Type.Literal('ml')]),
    }),
    response: {
      201: Type.Object({ id: Type.String(), name: Type.String() }),
    },
  },
}, async (request, reply) => {
  const campaign = await createCampaign({ ...request.body, userId: request.user.id })
  return reply.status(201).send(campaign)
})

// Error handler global
app.setErrorHandler((error, _req, reply) => {
  if (error.validation) return reply.status(400).send({ error: 'Validation', details: error.validation })
  reply.status(500).send({ error: 'Internal server error' })
})

await app.listen({ port: 3001, host: '0.0.0.0' })
```

### Plugins úteis

```bash
pnpm add fastify @fastify/cors @fastify/jwt @fastify/rate-limit @fastify/type-provider-typebox
pnpm add @sinclair/typebox
```

---

## 2. FastAPI (Python)

```python
# main.py
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from typing import Annotated

app = FastAPI(title="Bidspark API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bidspark.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema Pydantic v2
class CampaignCreate(BaseModel):
    name: str
    budget_daily: float
    target_acos: float
    marketplace: str  # "amazon" | "ml"

    @field_validator('budget_daily')
    @classmethod
    def budget_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError('Budget deve ser positivo')
        return v

# Dependency injection
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = await verify_jwt(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user

CurrentUser = Annotated[dict, Depends(get_current_user)]

# Async endpoint
@app.post("/campaigns", status_code=201)
async def create_campaign(data: CampaignCreate, user: CurrentUser):
    campaign = await db.campaigns.create({**data.model_dump(), "user_id": user["id"]})
    return campaign

# Background task (não bloqueia response)
@app.post("/reports/generate")
async def generate_report(background_tasks: BackgroundTasks, user: CurrentUser):
    background_tasks.add_task(generate_heavy_report, user["id"])
    return {"message": "Processando..."}

# Error handlers
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(status_code=400, content={"error": str(exc)})
```

### Estrutura FastAPI

```
project/
├── main.py              # App + routers registration
├── routers/
│   ├── campaigns.py
│   ├── reports.py
│   └── auth.py
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── services/            # Business logic
├── db/
│   ├── database.py      # engine, session
│   └── migrations/      # Alembic migrations
├── core/
│   ├── config.py        # Settings (pydantic-settings)
│   └── security.py      # JWT, password hash
└── requirements.txt
```

```bash
# init projeto
pip install fastapi uvicorn[standard] sqlalchemy asyncpg alembic pydantic-settings python-jose passlib

# rodar dev
uvicorn main:app --reload --port 8000

# gerar migration
alembic revision --autogenerate -m "create_campaigns"
alembic upgrade head
```

---

## 3. REST Design

### Padrão de URLs

```
GET    /api/v1/campaigns          # listar (paginado)
GET    /api/v1/campaigns/:id      # um registro
POST   /api/v1/campaigns          # criar
PATCH  /api/v1/campaigns/:id      # atualizar parcial
DELETE /api/v1/campaigns/:id      # deletar
POST   /api/v1/campaigns/:id/pause  # ação customizada (verbo como sub-resource)

# Paginação + filtros
GET /api/v1/campaigns?page=2&limit=20&status=active&sort=createdAt:desc
```

### Response Padrão

```ts
// Sucesso lista
{ "data": [...], "meta": { "total": 150, "page": 2, "limit": 20, "totalPages": 8 } }

// Sucesso único
{ "data": { id: "...", ... } }

// Erro
{ "error": { "code": "VALIDATION_ERROR", "message": "Invalid input", "details": [{ "field": "email", "message": "Email inválido" }] } }
```

### Paginação genérica (Drizzle)

```ts
async function paginate<T>(query: { items: T[]; total: number }, page: number, limit: number) {
  return {
    data: query.items,
    meta: { total: query.total, page, limit, totalPages: Math.ceil(query.total / limit) }
  }
}

async function getCampaigns(params: { page?: number; limit?: number; userId: string }) {
  const page = Math.max(1, params.page ?? 1)
  const limit = Math.min(100, params.limit ?? 20)
  const offset = (page - 1) * limit

  const [items, [{ total }]] = await Promise.all([
    db.query.campaigns.findMany({
      where: eq(campaigns.userId, params.userId),
      limit, offset,
      orderBy: [desc(campaigns.createdAt)],
    }),
    db.select({ total: count() }).from(campaigns).where(eq(campaigns.userId, params.userId)),
  ])

  return paginate({ items, total }, page, limit)
}
```

---

## 4. tRPC

```ts
// server/trpc.ts
import { initTRPC, TRPCError } from '@trpc/server'
import { z } from 'zod'

const t = initTRPC.context<Context>().create()
export const router = t.router
export const publicProcedure = t.procedure

const protectedProcedure = t.procedure.use(async ({ ctx, next }) => {
  if (!ctx.user) throw new TRPCError({ code: 'UNAUTHORIZED' })
  return next({ ctx: { user: ctx.user } })
})

// Router com procedures
export const appRouter = router({
  simulations: router({
    list: protectedProcedure
      .input(z.object({ page: z.number().default(1) }))
      .query(({ ctx, input }) => getSimulations({ ...input, userId: ctx.user.id })),

    create: protectedProcedure
      .input(SimulationSchema)
      .mutation(({ ctx, input }) => createSimulation({ ...input, userId: ctx.user.id })),

    delete: protectedProcedure
      .input(z.string().uuid())
      .mutation(async ({ ctx, input }) => {
        const sim = await db.query.simulations.findFirst({
          where: and(eq(simulations.id, input), eq(simulations.userId, ctx.user.id))
        })
        if (!sim) throw new TRPCError({ code: 'NOT_FOUND' })
        await db.delete(simulations).where(eq(simulations.id, input))
      }),
  }),
})

export type AppRouter = typeof appRouter

// Client
import { createTRPCReact } from '@trpc/react-query'
export const trpc = createTRPCReact<AppRouter>()

// Uso
const { data } = trpc.simulations.list.useQuery({ page: 1 })
const { mutate } = trpc.simulations.create.useMutation({
  onSuccess: () => utils.simulations.list.invalidate()
})
```

---

## 5. WebSockets + Realtime

### Supabase Realtime (Postgres Changes)

```ts
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(url, key)

// Escuta mudanças em tabela
const channel = supabase
  .channel('campaigns-changes')
  .on('postgres_changes', {
    event: '*', schema: 'public', table: 'campaigns',
    filter: `user_id=eq.${userId}`,
  }, (payload) => {
    if (payload.eventType === 'INSERT') addCampaign(payload.new as Campaign)
    if (payload.eventType === 'UPDATE') updateCampaign(payload.new as Campaign)
    if (payload.eventType === 'DELETE') removeCampaign(payload.old.id)
  })
  .subscribe()

// Cleanup
return () => supabase.removeChannel(channel)

// Broadcast (mensagens em tempo real, sem DB)
const chat = supabase.channel('support-chat')
chat.on('broadcast', { event: 'message' }, ({ payload }) => addMessage(payload))
   .subscribe()

chat.send({ type: 'broadcast', event: 'message', payload: { text: 'Olá!', userId } })
```

---

## 6. Webhooks

```ts
// Verificação de assinatura (crítico!)
import Stripe from 'stripe'
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!)

export async function POST(request: NextRequest) {
  const body = await request.text() // .text(), não .json()!
  const sig = request.headers.get('stripe-signature')!

  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!)
  } catch {
    return NextResponse.json({ error: 'Invalid signature' }, { status: 400 })
  }

  // Idempotência — evitar processar duas vezes
  const processed = await db.query.webhookEvents.findFirst({
    where: eq(webhookEvents.stripeId, event.id)
  })
  if (processed) return NextResponse.json({ received: true })

  await db.insert(webhookEvents).values({ stripeId: event.id, type: event.type })

  // Processar async (não bloquear Stripe)
  processStripeEvent(event).catch(err => logger.error(err))

  return NextResponse.json({ received: true })
}

async function processStripeEvent(event: Stripe.Event) {
  switch (event.type) {
    case 'customer.subscription.created':
    case 'customer.subscription.updated':
      await syncSubscription(event.data.object as Stripe.Subscription)
      break
    case 'customer.subscription.deleted':
      await cancelSubscription(event.data.object as Stripe.Subscription)
      break
    case 'invoice.payment_failed':
      await handlePaymentFailed(event.data.object as Stripe.Invoice)
      break
  }
}
```

---

## 7. BullMQ

```ts
import { Queue, Worker } from 'bullmq'
const connection = { host: 'localhost', port: 6379 }

// Definir filas
export const emailQueue = new Queue('email', { connection })
export const syncQueue = new Queue('marketplace-sync', { connection })

// Adicionar job
await emailQueue.add('welcome', { to: user.email, name: user.name }, {
  attempts: 3,
  backoff: { type: 'exponential', delay: 1000 },
})

// Job com delay (abandoned cart)
await emailQueue.add('cart-reminder', { userId }, {
  delay: 2 * 60 * 60 * 1000 // 2 horas
})

// Cron job
await syncQueue.add('amazon-sync', { marketplace: 'amazon' }, {
  repeat: { pattern: '0 */4 * * *' } // a cada 4h
})

// Worker
const worker = new Worker('email', async (job) => {
  switch (job.name) {
    case 'welcome': await sendWelcomeEmail(job.data); break
    case 'cart-reminder': await sendCartReminderEmail(job.data); break
  }
}, { connection, concurrency: 5 })

worker.on('failed', (job, err) => logger.error({ jobId: job?.id, err }, 'Job failed'))
```
