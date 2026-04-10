# Frontend Reference — React 19, Next.js 15, shadcn/ui, State

## Índice
1. [React 19 — Hooks Essenciais](#1-react-19)
2. [Next.js 15 App Router](#2-nextjs-15)
3. [shadcn/ui + Tailwind](#3-shadcnui--tailwind)
4. [State Management](#4-state-management)
5. [Forms com Zod](#5-forms--validação)
6. [Performance](#6-performance)

---

## 1. React 19

### Hooks Novos

```tsx
// useTransition — não bloqueia a UI durante updates pesados
const [isPending, startTransition] = useTransition()
startTransition(() => setSearchResults(filter(query)))

// useOptimistic — UI atualiza imediatamente, sincroniza depois
const [optimisticItems, addOptimistic] = useOptimistic(
  items,
  (state, newItem) => [...state, { ...newItem, pending: true }]
)
async function handleAdd(item) {
  addOptimistic(item) // UI mostra imediatamente
  await saveToDb(item)
}

// useActionState — estado de form action
const [error, submitAction, isPending] = useActionState(
  async (prevState, formData) => {
    const result = await serverAction(formData)
    if (!result.ok) return result.error
    redirect('/success')
  },
  null
)
```

### Patterns de Composição

```tsx
// Custom Hook — extrai lógica reutilizável
function useDebounce<T>(value: T, delay = 300): T {
  const [debounced, setDebounced] = useState(value)
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(t)
  }, [value, delay])
  return debounced
}

// Compound Component — estado implícito compartilhado
const Tabs = ({ children, defaultValue }: TabsProps) => {
  const [active, setActive] = useState(defaultValue)
  return <TabsContext.Provider value={{ active, setActive }}>{children}</TabsContext.Provider>
}
Tabs.List = TabsList
Tabs.Trigger = TabsTrigger
Tabs.Content = TabsContent

// HOC com TypeScript genérico
function withAuth<T extends object>(Component: React.ComponentType<T>) {
  return function AuthGuard(props: T) {
    const { user } = useAuth()
    if (!user) return <Redirect to="/login" />
    return <Component {...props} />
  }
}
```

---

## 2. Next.js 15

### Server vs Client Components

```tsx
// SERVER (padrão, sem 'use client')
// ✅ async/await direto, acesso ao DB, env vars secretas
// ❌ useState, useEffect, event handlers

export default async function Page() {
  const user = await getCurrentUser() // acessa auth diretamente
  const orders = await db.query.orders.findMany({
    where: eq(orders.userId, user.id)
  })
  return <OrdersList orders={orders} /> // pode ser Client
}

// CLIENT ('use client')
// ✅ useState, eventos, browser APIs
// ❌ async no corpo, acesso direto ao DB
'use client'
export function OrdersList({ orders }: { orders: Order[] }) {
  const [selected, setSelected] = useState<string | null>(null)
  return <ul>{orders.map(o => <li key={o.id} onClick={() => setSelected(o.id)}>{o.id}</li>)}</ul>
}
```

### App Router — Arquivos Especiais

```
app/
├── layout.tsx       # HTML + body + providers — obrigatório
├── page.tsx         # rota /
├── loading.tsx      # Suspense fallback automático
├── error.tsx        # Error boundary — deve ser 'use client'
├── not-found.tsx    # 404
├── middleware.ts    # edge middleware (raiz do projeto)
├── (auth)/          # route group — sem impacto na URL
├── [slug]/          # segmento dinâmico
└── [...slug]/       # catch-all
```

### Rendering Modes

```tsx
// ISR — cache + revalida a cada N segundos
export const revalidate = 60

// ISR por tag — invalida sob demanda
export default async function Page({ params }) {
  const data = await fetch(url, { next: { tags: [`product-${params.id}`] } })
  return <View data={await data.json()} />
}
// Em action/route handler:
import { revalidateTag } from 'next/cache'
revalidateTag(`product-${id}`)

// SSR (dinâmico por request)
export const dynamic = 'force-dynamic'

// SSG (estático na build)
export async function generateStaticParams() {
  const items = await db.query.products.findMany()
  return items.map(i => ({ id: i.id }))
}
```

### Server Actions (padrão para mutações)

```tsx
// actions.ts
'use server'
import { revalidatePath } from 'next/cache'

export async function createSimulation(formData: FormData) {
  const user = await requireAuth()
  const parsed = SimulationSchema.safeParse(Object.fromEntries(formData))
  if (!parsed.success) return { error: parsed.error.flatten() }

  const sim = await db.insert(simulations).values({
    ...parsed.data,
    userId: user.id,
  }).returning()

  revalidatePath('/dashboard/simulations')
  return { success: true, id: sim[0].id }
}

// Formulário usando a action
'use client'
import { createSimulation } from './actions'
import { useActionState } from 'react'

export function SimulationForm() {
  const [state, action, isPending] = useActionState(createSimulation, null)
  return (
    <form action={action}>
      <input name="productName" required />
      {state?.error && <p className="text-red-500">{JSON.stringify(state.error)}</p>}
      <button disabled={isPending}>{isPending ? 'Salvando...' : 'Criar'}</button>
    </form>
  )
}
```

### Route Handlers (API)

```tsx
// app/api/orders/route.ts
import { NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url)
  const page = Number(searchParams.get('page') ?? '1')
  const data = await getOrders({ page })
  return NextResponse.json(data)
}

// app/api/orders/[id]/route.ts
export async function GET(
  _request: NextRequest,
  { params }: { params: Promise<{ id: string }> } // Next.js 15: params é Promise!
) {
  const { id } = await params
  const order = await db.query.orders.findFirst({ where: eq(orders.id, id) })
  if (!order) return NextResponse.json({ error: 'Not found' }, { status: 404 })
  return NextResponse.json(order)
}
```

### Middleware (auth + redirects)

```tsx
// middleware.ts (raiz do projeto)
import { NextRequest, NextResponse } from 'next/server'
import { createServerClient } from '@supabase/ssr'

export async function middleware(request: NextRequest) {
  const response = NextResponse.next()
  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    { cookies: { getAll: () => request.cookies.getAll(), setAll: (c) => c.forEach(({ name, value, options }) => response.cookies.set(name, value, options)) } }
  )
  const { data: { session } } = await supabase.auth.getSession()

  if (request.nextUrl.pathname.startsWith('/dashboard') && !session) {
    return NextResponse.redirect(new URL('/login', request.url))
  }
  if (request.nextUrl.pathname === '/login' && session) {
    return NextResponse.redirect(new URL('/dashboard', request.url))
  }
  return response
}

export const config = {
  matcher: ['/dashboard/:path*', '/settings/:path*', '/login'],
}
```

---

## 3. shadcn/ui + Tailwind

### Setup e Uso

```bash
pnpm dlx shadcn@latest init
pnpm dlx shadcn@latest add button dialog form input select table
```

```tsx
// Button com variantes (cva)
import { cva, type VariantProps } from 'class-variance-authority'
import { cn } from '@/lib/utils'

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        outline: 'border border-input bg-background hover:bg-accent',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        destructive: 'bg-destructive text-destructive-foreground',
      },
      size: {
        sm: 'h-8 px-3 text-xs',
        md: 'h-10 px-4 py-2',
        lg: 'h-11 px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: { variant: 'default', size: 'md' },
  }
)

// cn() — merges tailwind classes corretamente
// lib/utils.ts
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'
export function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)) }
```

### Dark Mode

```tsx
// providers.tsx — ThemeProvider
import { ThemeProvider } from 'next-themes'
export function Providers({ children }: { children: React.ReactNode }) {
  return <ThemeProvider attribute="class" defaultTheme="system" enableSystem>{children}</ThemeProvider>
}

// Toggle
import { useTheme } from 'next-themes'
const { theme, setTheme } = useTheme()
<button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}>Toggle</button>
```

### Data Table (shadcn + TanStack Table)

```tsx
import { useReactTable, getCoreRowModel, flexRender } from '@tanstack/react-table'

const columns = [
  { accessorKey: 'name', header: 'Nome' },
  { accessorKey: 'status', header: 'Status' },
  {
    id: 'actions',
    cell: ({ row }) => <ActionMenu item={row.original} />,
  },
]

export function DataTable<T>({ data, columns }: { data: T[]; columns: ColumnDef<T>[] }) {
  const table = useReactTable({ data, columns, getCoreRowModel: getCoreRowModel() })
  return (
    <table>
      <thead>
        {table.getHeaderGroups().map(hg => (
          <tr key={hg.id}>{hg.headers.map(h => <th key={h.id}>{flexRender(h.column.columnDef.header, h.getContext())}</th>)}</tr>
        ))}
      </thead>
      <tbody>
        {table.getRowModel().rows.map(row => (
          <tr key={row.id}>{row.getVisibleCells().map(cell => <td key={cell.id}>{flexRender(cell.column.columnDef.cell, cell.getContext())}</td>)}</tr>
        ))}
      </tbody>
    </table>
  )
}
```

---

## 4. State Management

### Regra de Decisão

```
Dados do servidor (fetch/cache) → TanStack Query (SEMPRE)
State local simples (toggle, form) → useState
State global de UI → Zustand
State atômico granular → Jotai
State de forms → React Hook Form
```

### TanStack Query

```tsx
// Setup
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
const queryClient = new QueryClient({
  defaultOptions: { queries: { staleTime: 60_000, retry: 2 } }
})

// Hook de query
function useSimulations(filters: Filters) {
  return useQuery({
    queryKey: ['simulations', filters],
    queryFn: () => api.getSimulations(filters),
    enabled: !!filters.userId,
  })
}

// Mutation com invalidação
function useCreateSimulation() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (data: CreateSimInput) => api.createSimulation(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['simulations'] })
      toast.success('Simulação criada!')
    },
  })
}

// Prefetch no Server (App Router)
import { dehydrate, HydrationBoundary } from '@tanstack/react-query'
export default async function Page() {
  const qc = new QueryClient()
  await qc.prefetchQuery({ queryKey: ['simulations'], queryFn: fetchSimulations })
  return (
    <HydrationBoundary state={dehydrate(qc)}>
      <SimulationsList /> {/* Client Component com useQuery */}
    </HydrationBoundary>
  )
}
```

### Zustand

```tsx
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

interface UIState {
  sidebarOpen: boolean
  activeOrgId: string | null
  setSidebarOpen: (open: boolean) => void
  setActiveOrg: (id: string) => void
}

export const useUIStore = create<UIState>()(
  persist(
    (set) => ({
      sidebarOpen: true,
      activeOrgId: null,
      setSidebarOpen: (open) => set({ sidebarOpen: open }),
      setActiveOrg: (id) => set({ activeOrgId: id }),
    }),
    { name: 'ui-storage' }
  )
)

// Uso granular — evita re-renders desnecessários
const sidebarOpen = useUIStore(s => s.sidebarOpen)
const setSidebarOpen = useUIStore(s => s.setSidebarOpen)
```

---

## 5. Forms + Validação

```tsx
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'

const SimSchema = z.object({
  productName: z.string().min(1, 'Obrigatório'),
  fobValue: z.number({ coerce: true }).positive('Deve ser positivo'),
  quantity: z.number({ coerce: true }).int().positive(),
  ncm: z.string().regex(/^\d{8}$/, 'NCM: 8 dígitos'),
  incoterm: z.enum(['FOB', 'CIF', 'EXW']),
})
type SimForm = z.infer<typeof SimSchema>

export function SimulationForm({ onSubmit }: { onSubmit: (d: SimForm) => Promise<void> }) {
  const form = useForm<SimForm>({
    resolver: zodResolver(SimSchema),
    defaultValues: { incoterm: 'FOB' },
  })

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        <FormField control={form.control} name="productName" render={({ field }) => (
          <FormItem>
            <FormLabel>Nome do Produto</FormLabel>
            <FormControl><input {...field} /></FormControl>
            <FormMessage />
          </FormItem>
        )} />
        <button type="submit" disabled={form.formState.isSubmitting}>
          {form.formState.isSubmitting ? 'Enviando...' : 'Simular'}
        </button>
      </form>
    </Form>
  )
}
```

---

## 6. Performance

```tsx
// Code splitting
const HeavyChart = lazy(() => import('./HeavyChart'))
<Suspense fallback={<Skeleton className="h-64" />}><HeavyChart /></Suspense>

// Images otimizadas
import Image from 'next/image'
<Image src="/hero.jpg" alt="" width={1200} height={630} priority quality={85} />

// Fonts sem FOUT
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'], variable: '--font-inter' })

// Bundle analyzer
// package.json: "analyze": "ANALYZE=true next build"
```

### Erros Comuns Next.js 15

```
❌ useState em Server Component → mover para Client Component
❌ params sem await → const { id } = await params (Next 15: params é Promise)
❌ Fetch em loop (N+1) → usar Promise.all() ou query com include/join
❌ revalidatePath('/') para um dado específico → usar revalidateTag
❌ Passar função de Server para Client Component → usar Server Actions
```
