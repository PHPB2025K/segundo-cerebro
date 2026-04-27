---
title: "database"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/fullstack-dev
---
# Database Reference — PostgreSQL, Supabase, Drizzle, Redis

## Índice
1. [PostgreSQL Avançado](#1-postgresql-avançado)
2. [Supabase — Padrões Práticos](#2-supabase)
3. [Drizzle ORM](#3-drizzle-orm)
4. [Prisma (alternativa)](#4-prisma)
5. [Redis — Cache e Rate Limiting](#5-redis)

---

## 1. PostgreSQL Avançado

### Tipos e Índices

```sql
-- Tipos úteis
CREATE TABLE products (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  price NUMERIC(10, 2) NOT NULL,          -- monetário
  metadata JSONB,                          -- JSON indexável
  tags TEXT[],                             -- arrays nativos
  embedding vector(1536),                  -- pgvector para AI
  created_at TIMESTAMPTZ DEFAULT NOW(),
  deleted_at TIMESTAMPTZ                   -- soft delete
);

-- Índices essenciais
CREATE INDEX idx_products_user ON products(user_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_products_created ON products(created_at DESC);
CREATE INDEX idx_products_tags ON products USING GIN(tags);
CREATE INDEX idx_products_metadata ON products USING GIN(metadata);
CREATE INDEX idx_products_fts ON products USING GIN(to_tsvector('portuguese', name));
-- SEMPRE criar índice em foreign keys:
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_org_id ON orders(org_id);
```

### Queries Avançadas

```sql
-- JSONB queries
SELECT * FROM products WHERE metadata->>'category' = 'electronics'
  AND (metadata->>'stock')::int > 10;

-- JSONB update parcial (não substituir o objeto inteiro)
UPDATE products SET metadata = metadata || '{"featured": true}'::jsonb WHERE id = '...';

-- Array queries
SELECT * FROM products WHERE 'premium' = ANY(tags);
SELECT * FROM products WHERE tags @> ARRAY['premium', 'sale']; -- contém todos

-- CTEs para queries complexas
WITH monthly_stats AS (
  SELECT DATE_TRUNC('month', created_at) AS month,
         SUM(total) AS revenue, COUNT(*) AS orders
  FROM orders WHERE status = 'completed' GROUP BY 1
),
growth AS (
  SELECT month, revenue,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month) * 100, 2) AS pct
  FROM monthly_stats
)
SELECT * FROM growth ORDER BY month DESC;

-- Window Functions
SELECT o.*,
  SUM(total) OVER (PARTITION BY user_id ORDER BY created_at) AS running_total,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY total DESC) AS rank_by_value
FROM orders o;

-- Full-text search em português
SELECT *, ts_rank(to_tsvector('portuguese', name), query) AS rank
FROM products, plainto_tsquery('portuguese', 'pote hermético vidro') query
WHERE to_tsvector('portuguese', name) @@ query
ORDER BY rank DESC;

-- Upsert
INSERT INTO user_stats(user_id, count) VALUES ('uuid', 1)
ON CONFLICT (user_id) DO UPDATE SET count = user_stats.count + 1, updated_at = NOW();

-- Diagnosticar queries lentas
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = '...' AND status = 'pending';

-- Índices não utilizados (candidatos a remoção)
SELECT schemaname, tablename, indexname FROM pg_stat_user_indexes WHERE idx_scan = 0;
```

### Triggers Essenciais

```sql
-- updated_at automático
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = NOW(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER products_updated_at
  BEFORE UPDATE ON products
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- Criar profile após signup (Supabase)
CREATE OR REPLACE FUNCTION handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO public.profiles(id, email, full_name, avatar_url)
  VALUES (NEW.id, NEW.email, NEW.raw_user_meta_data->>'full_name', NEW.raw_user_meta_data->>'avatar_url');
  RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

CREATE TRIGGER on_auth_user_created
  AFTER INSERT ON auth.users
  FOR EACH ROW EXECUTE FUNCTION handle_new_user();
```

---

## 2. Supabase

### Client Setup

```ts
// lib/supabase/server.ts — para Server Components e Route Handlers
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'

export function createClient() {
  const cookieStore = cookies()
  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll: () => cookieStore.getAll(),
        setAll: (cs) => cs.forEach(({ name, value, options }) => cookieStore.set(name, value, options)),
      },
    }
  )
}

// lib/supabase/client.ts — para Client Components
import { createBrowserClient } from '@supabase/ssr'
export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}

// Para operações admin (bypass RLS) — SERVER ONLY!
import { createClient } from '@supabase/supabase-js'
export const adminClient = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY! // NUNCA expor no client!
)
```

### RLS Policies

```sql
ALTER TABLE simulations ENABLE ROW LEVEL SECURITY;

-- Policy básica: usuário vê apenas seus dados
CREATE POLICY "users_own_simulations" ON simulations
  FOR ALL USING (user_id = auth.uid());

-- Policy multi-tenant: membros da org veem dados da org
CREATE POLICY "org_members_see_simulations" ON simulations
  FOR SELECT USING (
    org_id IN (SELECT org_id FROM organization_members WHERE user_id = auth.uid())
  );

-- Só owner pode criar
CREATE POLICY "org_members_create_simulations" ON simulations
  FOR INSERT WITH CHECK (
    org_id IN (SELECT org_id FROM organization_members WHERE user_id = auth.uid())
  );

-- Função helper para checar role
CREATE OR REPLACE FUNCTION get_user_org_role(p_org_id UUID)
RETURNS TEXT AS $$
  SELECT role FROM organization_members WHERE org_id = p_org_id AND user_id = auth.uid();
$$ LANGUAGE sql SECURITY DEFINER;

-- Policy baseada em role
CREATE POLICY "admins_can_delete" ON simulations
  FOR DELETE USING (get_user_org_role(org_id) IN ('owner', 'admin'));
```

### Edge Functions

```ts
// supabase/functions/process-webhook/index.ts
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

serve(async (req) => {
  const payload = await req.json()

  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')! // service role para bypass RLS
  )

  const { data: user } = await supabase.from('profiles')
    .select('email, full_name').eq('id', payload.userId).single()

  await sendEmail({ to: user.email, subject: 'Evento processado' })

  return new Response(JSON.stringify({ ok: true }), {
    headers: { 'Content-Type': 'application/json' }
  })
})
```

```bash
# CLI Supabase
supabase login
supabase init && supabase start          # dev local (Docker)
supabase gen types typescript --linked > src/types/supabase.ts
supabase migration new create_orders
supabase db push
supabase functions new send-email
supabase functions deploy send-email
```

### Verificar limite de uso (SaaS)

```sql
CREATE OR REPLACE FUNCTION check_simulation_limit(p_org_id UUID)
RETURNS BOOLEAN AS $$
DECLARE org_plan TEXT; sim_count INT; plan_limit INT;
BEGIN
  SELECT plan INTO org_plan FROM organizations WHERE id = p_org_id;
  SELECT COUNT(*) INTO sim_count FROM simulations
    WHERE org_id = p_org_id AND created_at > DATE_TRUNC('month', NOW());

  plan_limit := CASE org_plan
    WHEN 'starter' THEN 50
    WHEN 'pro' THEN 500
    WHEN 'enterprise' THEN 999999
    ELSE 5 END;

  RETURN sim_count < plan_limit;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
```

---

## 3. Drizzle ORM

### Schema Definition

```ts
// db/schema.ts
import { pgTable, uuid, text, numeric, timestamp, boolean, pgEnum } from 'drizzle-orm/pg-core'
import { relations } from 'drizzle-orm'

export const planEnum = pgEnum('plan', ['free', 'starter', 'pro', 'enterprise'])

export const organizations = pgTable('organizations', {
  id: uuid('id').primaryKey().defaultRandom(),
  name: text('name').notNull(),
  slug: text('slug').notNull().unique(),
  plan: planEnum('plan').default('free').notNull(),
  stripeCustomerId: text('stripe_customer_id'),
  stripeSubscriptionId: text('stripe_subscription_id'),
  createdAt: timestamp('created_at', { withTimezone: true }).defaultNow(),
})

export const simulations = pgTable('simulations', {
  id: uuid('id').primaryKey().defaultRandom(),
  orgId: uuid('org_id').notNull().references(() => organizations.id, { onDelete: 'cascade' }),
  userId: uuid('user_id').notNull(),
  productName: text('product_name').notNull(),
  fobValue: numeric('fob_value', { precision: 10, scale: 2 }).notNull(),
  result: text('result'), // JSON string
  createdAt: timestamp('created_at', { withTimezone: true }).defaultNow(),
})

// Relations
export const organizationsRelations = relations(organizations, ({ many }) => ({
  simulations: many(simulations),
}))
export const simulationsRelations = relations(simulations, ({ one }) => ({
  organization: one(organizations, { fields: [simulations.orgId], references: [organizations.id] }),
}))
```

### Queries

```ts
// db/index.ts
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'
import * as schema from './schema'

const client = postgres(process.env.DATABASE_URL!)
export const db = drizzle(client, { schema })
export * from './schema' // re-export para usar em qualquer lugar

// Queries tipadas
import { db, simulations, organizations } from '@/lib/db'
import { eq, and, desc, gte, lte, count } from 'drizzle-orm'

// Buscar com relação
const sims = await db.query.simulations.findMany({
  where: and(eq(simulations.orgId, orgId), gte(simulations.createdAt, startDate)),
  with: { organization: { columns: { name: true, plan: true } } },
  orderBy: [desc(simulations.createdAt)],
  limit: 20,
})

// Insert e retornar
const [sim] = await db.insert(simulations).values({
  orgId, userId, productName, fobValue: '2.50',
}).returning()

// Update
await db.update(simulations)
  .set({ result: JSON.stringify(calcResult) })
  .where(eq(simulations.id, simId))

// Delete
await db.delete(simulations).where(eq(simulations.id, simId))

// Aggregação
const [stats] = await db.select({
  total: count(),
  sumFob: sum(simulations.fobValue),
}).from(simulations).where(eq(simulations.orgId, orgId))

// Transaction
await db.transaction(async (tx) => {
  const [org] = await tx.insert(organizations).values(orgData).returning()
  await tx.insert(orgMembers).values({ orgId: org.id, userId, role: 'owner' })
})
```

### Drizzle Config + Migrations

```ts
// drizzle.config.ts
import { defineConfig } from 'drizzle-kit'
export default defineConfig({
  schema: './src/db/schema.ts',
  out: './drizzle',
  dialect: 'postgresql',
  dbCredentials: { url: process.env.DATABASE_URL! },
})
```

```bash
pnpm drizzle-kit generate   # gera migration SQL
pnpm drizzle-kit migrate    # aplica migrations
pnpm drizzle-kit push       # push direto (dev sem migration file)
pnpm drizzle-kit studio     # UI visual do banco
pnpm drizzle-kit check      # diff schema vs DB
```

---

## 4. Prisma

```prisma
// schema.prisma
datasource db { provider = "postgresql"; url = env("DATABASE_URL") }
generator client { provider = "prisma-client-js" }

model Organization {
  id          String   @id @default(uuid())
  name        String
  slug        String   @unique
  plan        String   @default("free")
  simulations Simulation[]
  createdAt   DateTime @default(now())
}

model Simulation {
  id          String   @id @default(uuid())
  orgId       String
  org         Organization @relation(fields: [orgId], references: [id])
  productName String
  fobValue    Decimal  @db.Decimal(10, 2)
  createdAt   DateTime @default(now())
  @@index([orgId])
}
```

```ts
// Queries
const sims = await prisma.simulation.findMany({
  where: { orgId, createdAt: { gte: startDate } },
  include: { org: { select: { name: true, plan: true } } },
  orderBy: { createdAt: 'desc' },
  take: 20, skip: (page - 1) * 20,
})

// Transaction
await prisma.$transaction(async (tx) => {
  const org = await tx.organization.create({ data: orgData })
  await tx.orgMember.create({ data: { orgId: org.id, userId, role: 'owner' } })
})
```

**Drizzle vs Prisma:**
- Drizzle: melhor type-safety, mais próximo do SQL, menor overhead, sem Rust dependency
- Prisma: mais fácil de aprender, melhor DX para schemas complexos, mais maduro
- **Recomendação para Pedro: Drizzle** (melhor performance, type-safety superior)

---

## 5. Redis

```ts
import Redis from 'ioredis'
const redis = new Redis(process.env.REDIS_URL!)

// Cache simples
async function getCachedUser(userId: string) {
  const cached = await redis.get(`user:${userId}`)
  if (cached) return JSON.parse(cached) as User

  const user = await db.query.users.findFirst({ where: eq(users.id, userId) })
  await redis.setex(`user:${userId}`, 300, JSON.stringify(user)) // 5 min TTL
  return user
}

// Invalidar
await redis.del(`user:${userId}`)
await redis.del(...await redis.keys(`org:${orgId}:*`)) // wildcard

// Rate limiting (sliding window)
async function checkRateLimit(key: string, limit: number, windowMs: number) {
  const now = Date.now()
  const window = Math.floor(now / windowMs)
  const redisKey = `rate:${key}:${window}`

  const current = await redis.incr(redisKey)
  if (current === 1) await redis.expire(redisKey, Math.ceil(windowMs / 1000))

  return {
    allowed: current <= limit,
    remaining: Math.max(0, limit - current),
    reset: (window + 1) * windowMs,
  }
}

// Uso no API
const { allowed, remaining } = await checkRateLimit(`auth:${ip}`, 5, 60_000)
if (!allowed) {
  return NextResponse.json({ error: 'Too many requests' }, {
    status: 429,
    headers: { 'Retry-After': '60' }
  })
}

// Session storage (alternativa a JWT stateless)
await redis.setex(`session:${sessionId}`, 86400, JSON.stringify(userData))
const session = JSON.parse(await redis.get(`session:${sessionId}`) ?? 'null')
```

### Redis com Upstash (serverless)

```ts
import { Redis } from '@upstash/redis'
import { Ratelimit } from '@upstash/ratelimit'

const redis = Redis.fromEnv()

const ratelimit = new Ratelimit({
  redis,
  limiter: Ratelimit.slidingWindow(10, '10 s'), // 10 req por 10s
  analytics: true,
})

const { success, limit, remaining } = await ratelimit.limit(identifier)
```


## Ver também

- [[openclaw/agents/kobe/IDENTITY]] — agente proprietário desta skill
- [[openclaw/agents/kobe/SOUL]] — princípios estáveis do agente
- [[openclaw/agents/kobe/AGENTS]] — orquestração com sub-agentes
- [[meta/mocs/MOC - Governanca OpenClaw]] — governança da plataforma
- [[meta/mocs/MOC - Supabase Ecosystem]] — referência canônica detectada no conteúdo
