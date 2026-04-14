---
title: "typescript patterns"
created: 2026-04-14
type: skill
domain: dev
status: active
tags:
  - skill/dev
---

# TypeScript Patterns — Avançado, Generics, Zod, Strict Mode

## Índice
1. [Utility Types](#1-utility-types)
2. [Generics](#2-generics)
3. [Conditional & Mapped Types](#3-conditional--mapped-types)
4. [Discriminated Unions](#4-discriminated-unions)
5. [Zod — Schema as Source of Truth](#5-zod)
6. [Strict Mode Config](#6-strict-mode)
7. [Patterns Práticos](#7-patterns-práticos)

---

## 1. Utility Types

```ts
// Built-in utilities com exemplos reais
type User = {
  id: string; name: string; email: string
  passwordHash: string; createdAt: Date
}

type UserPreview = Pick<User, 'id' | 'name' | 'email'>
type UpdateUser = Partial<Omit<User, 'id' | 'createdAt' | 'passwordHash'>>
type ReadonlyUser = Readonly<User>
type UserRecord = Record<string, User>
type NonNullUser = NonNullable<User | null | undefined>

// Required (todos campos obrigatórios)
type RequiredConfig = Required<Partial<Config>>

// ReturnType e Parameters
async function createSimulation(data: SimInput): Promise<Simulation> { /* ... */ }
type SimResult = Awaited<ReturnType<typeof createSimulation>> // Simulation
type SimParams = Parameters<typeof createSimulation>[0]       // SimInput
```

---

## 2. Generics

```ts
// Generic simples
function getFirst<T>(arr: T[]): T | undefined {
  return arr[0]
}

// Generic com constraint
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key]
}
const name = getProperty(user, 'name') // string — tipado!

// Generic API response
interface ApiResponse<T> {
  data: T
  meta?: { total: number; page: number }
  error?: string
}

async function fetchApi<T>(url: string): Promise<ApiResponse<T>> {
  const res = await fetch(url)
  return res.json()
}

const { data: orders } = await fetchApi<Order[]>('/api/orders')
// orders: Order[] ✅

// Generic com default
interface PaginatedResult<T, M = DefaultMeta> {
  data: T[]
  meta: M
}

// Generic repository
interface Repository<T, ID = string> {
  findById(id: ID): Promise<T | null>
  findMany(filters: Partial<T>): Promise<T[]>
  create(data: Omit<T, 'id' | 'createdAt'>): Promise<T>
  update(id: ID, data: Partial<T>): Promise<T>
  delete(id: ID): Promise<void>
}

// Generic hook de data fetching
function useData<T>(key: string, fetcher: () => Promise<T>) {
  return useQuery<T>({ queryKey: [key], queryFn: fetcher })
}

const { data: simulations } = useData<Simulation[]>('simulations', fetchSimulations)
```

---

## 3. Conditional & Mapped Types

```ts
// Conditional Types
type IsArray<T> = T extends any[] ? true : false
type Unwrap<T> = T extends Promise<infer U> ? U : T
type ElementType<T> = T extends (infer U)[] ? U : never

type Resolved = Unwrap<Promise<Simulation>> // Simulation
type SimItem = ElementType<Simulation[]>    // Simulation

// infer — extrair tipos internos
type UnpackPromise<T> = T extends Promise<infer R> ? R : T
type FirstArg<T extends (...args: any) => any> = T extends (first: infer A, ...rest: any) => any ? A : never

// Mapped Types
type Optional<T> = { [K in keyof T]?: T[K] }
type Nullable<T> = { [K in keyof T]: T[K] | null }
type Mutable<T> = { -readonly [K in keyof T]: T[K] } // remove readonly

// Template Literal Types
type Route = `/api/${string}`
type EventHandler = `on${Capitalize<string>}`
type DbColumn = `${string}_id` | `${string}_at` | `${string}_count`

// Combinação prática
type ApiEndpoints = {
  [K in 'simulations' | 'campaigns' | 'users']: {
    list: `/api/${K}`
    get: `/api/${K}/${string}`
    create: `/api/${K}`
  }
}
```

---

## 4. Discriminated Unions

```ts
// Result type (sem throw/catch)
type Result<T, E = string> =
  | { success: true; data: T }
  | { success: false; error: E }

function divideImportCost(fob: number, items: number): Result<number> {
  if (items === 0) return { success: false, error: 'Cannot divide by zero' }
  return { success: true, data: fob / items }
}

const result = divideImportCost(1000, 5)
if (result.success) {
  console.log(result.data)   // number ✅ — TypeScript sabe
} else {
  console.log(result.error)  // string ✅
}

// Action states (React forms)
type ActionState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: Simulation }
  | { status: 'error'; message: string; code?: string }

// Payment status
type PaymentEvent =
  | { type: 'initiated'; amount: number; currency: string }
  | { type: 'completed'; transactionId: string; timestamp: Date }
  | { type: 'failed'; reason: string; retryable: boolean }
  | { type: 'refunded'; amount: number; reason: string }

function handlePayment(event: PaymentEvent) {
  switch (event.type) {
    case 'completed':
      activateSubscription(event.transactionId) // transactionId só existe aqui
      break
    case 'failed':
      if (event.retryable) scheduleRetry()
      break
  }
}

// Narrowing manual
function processEvent(event: unknown): void {
  if (typeof event !== 'object' || event === null) return
  if (!('type' in event)) return
  // event.type existe agora
}
```

---

## 5. Zod

### Schema como Source of Truth

```ts
import { z } from 'zod'

// Define schema uma vez → type inferido automaticamente
const ImportSimSchema = z.object({
  productName: z.string().min(1, 'Obrigatório').max(200),
  fobValue: z.number({ coerce: true }).positive('Deve ser positivo'),
  freightCost: z.number({ coerce: true }).min(0),
  quantity: z.number({ coerce: true }).int().positive(),
  ncm: z.string().regex(/^\d{8}$/, 'NCM deve ter 8 dígitos'),
  country: z.enum(['CN', 'US', 'DE', 'BR', 'IN']).default('CN'),
  incoterm: z.enum(['FOB', 'CIF', 'EXW']).default('FOB'),
  weight: z.number().positive().optional(),
})

type ImportSimInput = z.infer<typeof ImportSimSchema> // type automático!

// Validação server-side
export async function POST(request: NextRequest) {
  const body = await request.json()
  const parsed = ImportSimSchema.safeParse(body)

  if (!parsed.success) {
    return NextResponse.json(
      { error: parsed.error.flatten() }, // { fieldErrors, formErrors }
      { status: 400 }
    )
  }

  const sim = await createSimulation(parsed.data) // totalmente tipado!
  return NextResponse.json(sim, { status: 201 })
}

// Schemas avançados
const PasswordSchema = z
  .object({ password: z.string().min(8), confirm: z.string() })
  .refine(d => d.password === d.confirm, {
    message: 'Senhas não coincidem',
    path: ['confirm'],
  })

const PlanLimitsSchema = z.object({
  simulations: z.number().or(z.literal('unlimited')),
  users: z.number(),
  apiCalls: z.number().optional(),
})

// Transform
const MoneySchema = z
  .string()
  .transform(v => parseFloat(v.replace(',', '.')))
  .pipe(z.number().positive())

// Preprocess (antes da validação)
const StringToNumber = z.preprocess(val => {
  if (typeof val === 'string') return parseFloat(val)
  return val
}, z.number())

// Discriminated union com Zod
const CampaignActionSchema = z.discriminatedUnion('action', [
  z.object({ action: z.literal('pause'), campaignId: z.string().uuid() }),
  z.object({ action: z.literal('setBudget'), campaignId: z.string().uuid(), budget: z.number() }),
  z.object({ action: z.literal('delete'), campaignId: z.string().uuid() }),
])

// Reutilizar schemas
const BaseEntitySchema = z.object({
  id: z.string().uuid(),
  createdAt: z.coerce.date(),
  updatedAt: z.coerce.date().optional(),
})

const SimulationSchema = BaseEntitySchema.extend({
  productName: z.string(),
  fobValue: z.number(),
})

type Simulation = z.infer<typeof SimulationSchema>

// Validar variáveis de ambiente
const EnvSchema = z.object({
  DATABASE_URL: z.string().url(),
  SUPABASE_URL: z.string().url(),
  STRIPE_SECRET_KEY: z.string().startsWith('sk_'),
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
})

// lib/env.ts
export const env = EnvSchema.parse(process.env) // erro claro se faltando
```

---

## 6. Strict Mode

```json
// tsconfig.json — configuração recomendada
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,                          // habilita todas as verificações
    "noUncheckedIndexedAccess": true,        // arr[0] pode ser undefined
    "exactOptionalPropertyTypes": true,       // undefined ≠ ausente
    "noImplicitReturns": true,               // toda branch deve retornar
    "noFallthroughCasesInSwitch": true,      // switch sem fallthrough
    "noImplicitOverride": true,              // override explícito
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": { "@/*": ["./src/*"] }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

### Como lidar com strict

```ts
// noUncheckedIndexedAccess
const items: string[] = ['a', 'b']
const first = items[0] // string | undefined (não só string!)
if (first) console.log(first.toUpperCase()) // OK

// non-null assertion (só quando TEM certeza)
const element = document.getElementById('app')! // ! = você garante que não é null

// Type narrowing preferido ao assertion
function processOrder(order: Order | null) {
  if (!order) throw new Error('Order required')
  // Aqui order é Order (narrowed)
  return order.total
}

// Evitar any — usar unknown + narrowing
function processData(data: unknown) {
  if (typeof data !== 'object' || data === null) return
  if (!('id' in data) || typeof data.id !== 'string') return
  // data.id: string ✅
}
```

---

## 7. Patterns Práticos

### Builder Pattern para queries

```ts
class SimulationQueryBuilder {
  private filters: SQL[] = []
  private limitValue = 20
  private offsetValue = 0

  where(condition: SQL): this {
    this.filters.push(condition)
    return this
  }

  forUser(userId: string): this {
    return this.where(eq(simulations.userId, userId))
  }

  forOrg(orgId: string): this {
    return this.where(eq(simulations.orgId, orgId))
  }

  paginate(page: number, limit = 20): this {
    this.limitValue = limit
    this.offsetValue = (page - 1) * limit
    return this
  }

  async execute() {
    return db.query.simulations.findMany({
      where: and(...this.filters),
      limit: this.limitValue,
      offset: this.offsetValue,
      orderBy: [desc(simulations.createdAt)],
    })
  }
}

// Uso fluente
const sims = await new SimulationQueryBuilder()
  .forOrg(orgId)
  .forUser(userId)
  .paginate(2, 10)
  .execute()
```

### Type-safe event emitter

```ts
type EventMap = {
  'simulation.created': { simId: string; userId: string }
  'simulation.completed': { simId: string; result: SimResult }
  'payment.succeeded': { userId: string; amount: number }
}

class TypedEventEmitter<T extends Record<string, unknown>> {
  private handlers = new Map<string, Set<Function>>()

  on<K extends keyof T>(event: K, handler: (data: T[K]) => void) {
    if (!this.handlers.has(event as string)) {
      this.handlers.set(event as string, new Set())
    }
    this.handlers.get(event as string)!.add(handler)
  }

  emit<K extends keyof T>(event: K, data: T[K]) {
    this.handlers.get(event as string)?.forEach(h => h(data))
  }
}

const events = new TypedEventEmitter<EventMap>()
events.on('simulation.created', ({ simId, userId }) => {
  // simId: string, userId: string ✅
})
```

### Satisfies operator (TypeScript 4.9+)

```ts
// Garante que o valor satisfaz o tipo sem perder informação específica
const PLAN_CONFIG = {
  free: { limit: 5, price: 0 },
  starter: { limit: 50, price: 49 },
  pro: { limit: 500, price: 149 },
} satisfies Record<string, { limit: number; price: number }>

// Agora TypeScript conhece as chaves exatas!
PLAN_CONFIG.pro.limit   // number ✅
PLAN_CONFIG.unknown     // ❌ Error (sem satisfies, seria any)
```
