# Auth & Security Reference — Supabase Auth, RBAC, RLS, OWASP

## Índice
1. [Supabase Auth — Implementação Completa](#1-supabase-auth)
2. [RBAC + Multi-Tenant](#2-rbac--multi-tenant)
3. [JWT vs Sessions](#3-jwt-vs-sessions)
4. [OWASP Top 10 — Aplicado](#4-owasp-top-10)
5. [Headers de Segurança](#5-headers-de-segurança)

---

## 1. Supabase Auth

### Setup Completo

```ts
// lib/supabase/server.ts
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'
import type { Database } from '@/types/supabase'

export function createClient() {
  const cookieStore = cookies()
  return createServerClient<Database>(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll: () => cookieStore.getAll(),
        setAll: (cs) => cs.forEach(({ name, value, options }) =>
          cookieStore.set(name, value, options)
        ),
      },
    }
  )
}

// lib/auth.ts — helpers para Server Components
import { redirect } from 'next/navigation'

export async function getSession() {
  const supabase = createClient()
  const { data: { session } } = await supabase.auth.getSession()
  return session
}

export async function getUser() {
  const supabase = createClient()
  const { data: { user } } = await supabase.auth.getUser()
  return user
}

export async function requireAuth() {
  const user = await getUser()
  if (!user) redirect('/login')
  return user
}

// lib/supabase/client.ts — Client Components
import { createBrowserClient } from '@supabase/ssr'
export function createClient() {
  return createBrowserClient<Database>(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  )
}
```

### Auth Flows

```ts
// Email/Password
const supabase = createClient()

// Signup
const { data, error } = await supabase.auth.signUp({
  email, password,
  options: {
    emailRedirectTo: `${origin}/auth/callback`,
    data: { full_name: name }, // metadata
  }
})

// Login
const { data, error } = await supabase.auth.signInWithPassword({ email, password })

// OAuth (Google, GitHub)
await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: { redirectTo: `${origin}/auth/callback?next=/dashboard` }
})

// Logout
await supabase.auth.signOut()

// Reset de senha
await supabase.auth.resetPasswordForEmail(email, {
  redirectTo: `${origin}/auth/reset-password`
})

// Atualizar senha (após reset)
await supabase.auth.updateUser({ password: newPassword })

// app/auth/callback/route.ts — obrigatório para OAuth
import { NextRequest, NextResponse } from 'next/server'
import { createClient } from '@/lib/supabase/server'

export async function GET(request: NextRequest) {
  const { searchParams, origin } = new URL(request.url)
  const code = searchParams.get('code')
  const next = searchParams.get('next') ?? '/dashboard'

  if (code) {
    const supabase = createClient()
    const { error } = await supabase.auth.exchangeCodeForSession(code)
    if (!error) return NextResponse.redirect(`${origin}${next}`)
  }

  return NextResponse.redirect(`${origin}/login?error=auth_failed`)
}
```

### Client Component Auth

```tsx
'use client'
import { createClient } from '@/lib/supabase/client'
import { useRouter } from 'next/navigation'

export function LoginForm() {
  const supabase = createClient()
  const router = useRouter()

  async function handleLogin(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    const form = new FormData(e.currentTarget)
    const { error } = await supabase.auth.signInWithPassword({
      email: form.get('email') as string,
      password: form.get('password') as string,
    })
    if (error) { setError(error.message); return }
    router.push('/dashboard')
    router.refresh() // importante: atualiza o Server Component
  }
  // ...
}

// Hook para sessão do usuário
import { useEffect, useState } from 'react'
import type { User } from '@supabase/supabase-js'

export function useUser() {
  const [user, setUser] = useState<User | null>(null)
  const supabase = createClient()

  useEffect(() => {
    supabase.auth.getUser().then(({ data }) => setUser(data.user))
    const { data: { subscription } } = supabase.auth.onAuthStateChange((_, session) => {
      setUser(session?.user ?? null)
    })
    return () => subscription.unsubscribe()
  }, [])

  return user
}
```

---

## 2. RBAC + Multi-Tenant

### Schema

```sql
CREATE TYPE user_role AS ENUM ('owner', 'admin', 'member', 'viewer');

CREATE TABLE organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  plan TEXT NOT NULL DEFAULT 'free',
  stripe_customer_id TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE organization_members (
  org_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  role user_role NOT NULL DEFAULT 'member',
  joined_at TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY (org_id, user_id)
);

-- Função helper de role
CREATE OR REPLACE FUNCTION get_user_role(p_org_id UUID)
RETURNS user_role AS $$
  SELECT role FROM organization_members WHERE org_id = p_org_id AND user_id = auth.uid();
$$ LANGUAGE sql SECURITY DEFINER;

-- Policies
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE organization_members ENABLE ROW LEVEL SECURITY;

CREATE POLICY "members_see_org" ON organizations FOR SELECT
  USING (id IN (SELECT org_id FROM organization_members WHERE user_id = auth.uid()));

CREATE POLICY "owner_updates_org" ON organizations FOR UPDATE
  USING (get_user_role(id) = 'owner');

CREATE POLICY "member_sees_members" ON organization_members FOR SELECT
  USING (org_id IN (SELECT org_id FROM organization_members WHERE user_id = auth.uid()));

CREATE POLICY "admin_manages_members" ON organization_members FOR ALL
  USING (get_user_role(org_id) IN ('owner', 'admin'));
```

### RBAC no Next.js

```ts
// lib/rbac.ts
type Role = 'owner' | 'admin' | 'member' | 'viewer'
const ROLE_HIERARCHY: Record<Role, number> = { owner: 4, admin: 3, member: 2, viewer: 1 }

export async function getUserOrgRole(userId: string, orgId: string): Promise<Role | null> {
  const member = await db.query.orgMembers.findFirst({
    where: and(eq(orgMembers.userId, userId), eq(orgMembers.orgId, orgId)),
    columns: { role: true },
  })
  return (member?.role as Role) ?? null
}

export function hasPermission(userRole: Role, requiredRole: Role): boolean {
  return ROLE_HIERARCHY[userRole] >= ROLE_HIERARCHY[requiredRole]
}

// Uso em Server Action
export async function deleteSimulation(simId: string) {
  const user = await requireAuth()
  const sim = await db.query.simulations.findFirst({ where: eq(simulations.id, simId) })
  if (!sim) throw new Error('Not found')

  const role = await getUserOrgRole(user.id, sim.orgId)
  if (!role || !hasPermission(role, 'admin')) {
    throw new Error('Insufficient permissions')
  }

  await db.delete(simulations).where(eq(simulations.id, simId))
  revalidatePath('/dashboard/simulations')
}
```

### Team Invites

```ts
export async function inviteTeamMember(orgId: string, email: string, role: Role) {
  const user = await requireAuth()
  const userRole = await getUserOrgRole(user.id, orgId)
  if (!userRole || !hasPermission(userRole, 'admin')) throw new Error('Not allowed')

  const token = crypto.randomUUID()
  const expiresAt = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000) // 7 dias

  await db.insert(invitations).values({ orgId, email, role, token, expiresAt })
  await sendInviteEmail(email, { token, orgId })
}

export async function acceptInvite(token: string) {
  const user = await requireAuth()
  const invite = await db.query.invitations.findFirst({
    where: and(eq(invitations.token, token), eq(invitations.status, 'pending'))
  })

  if (!invite || invite.expiresAt < new Date()) throw new Error('Convite inválido ou expirado')

  await db.transaction(async (tx) => {
    await tx.insert(orgMembers).values({ orgId: invite.orgId, userId: user.id, role: invite.role })
    await tx.update(invitations).set({ status: 'accepted' }).where(eq(invitations.token, token))
  })
}
```

---

## 3. JWT vs Sessions

```
JWT (stateless):
✅ Escala horizontal sem shared storage
✅ Cross-domain fácil
✅ Performance (sem DB lookup por request)
❌ Não pode ser revogado antes de expirar
❌ Payload aumenta tamanho do header
❌ localStorage = vulnerável a XSS

Sessions (stateful):
✅ Revogação imediata
✅ Cookie HttpOnly = protegido de XSS
✅ Simples de invalidar (logout de todos devices)
❌ Precisa de Redis/DB compartilhado
❌ Lookup a cada request

Supabase Auth = melhor dos dois mundos:
- Access token curto (1h) → JWT
- Refresh token longo (30 dias) → rotacionado a cada uso
- Armazenado em cookies HttpOnly
- Revogação via refresh token invalidation
```

---

## 4. OWASP Top 10

### Broken Access Control (mais comum)

```ts
// ❌ ERRADO: não verifica ownership
async function deleteOrder(orderId: string) {
  await db.delete(orders).where(eq(orders.id, orderId))
}

// ✅ CORRETO: verifica sempre
async function deleteOrder(orderId: string, userId: string) {
  const order = await db.query.orders.findFirst({
    where: and(eq(orders.id, orderId), eq(orders.userId, userId))
  })
  if (!order) throw new Error('Not found or unauthorized')
  await db.delete(orders).where(eq(orders.id, orderId))
}
```

### Injection

```ts
// ❌ NUNCA: string interpolation em queries
const result = await db.execute(sql`SELECT * FROM users WHERE email = '${email}'`)

// ✅ SEMPRE: Drizzle/Prisma usam prepared statements automaticamente
const user = await db.query.users.findFirst({ where: eq(users.email, email) })
```

### Cryptographic Failures

```ts
import { hash, compare } from 'bcrypt'

// ❌ NUNCA: MD5, SHA1, armazenar plain text
// ✅ SEMPRE: bcrypt/argon2 com salt
const passwordHash = await hash(plainPassword, 12) // 12 rounds
const isValid = await compare(plainPassword, passwordHash)
```

### Rate Limiting (Auth endpoints)

```ts
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(5, '1 m'), // 5 tentativas/min
})

export async function POST(request: NextRequest) {
  const ip = request.headers.get('x-forwarded-for') ?? '127.0.0.1'
  const { success } = await ratelimit.limit(`auth:${ip}`)

  if (!success) {
    return NextResponse.json({ error: 'Too many requests' }, {
      status: 429,
      headers: { 'Retry-After': '60' }
    })
  }
  // ... handler
}
```

### XSS

```tsx
// Next.js escapa HTML automaticamente nos JSX expressions
// ❌ Nunca usar dangerouslySetInnerHTML sem sanitizar
// ✅ Se precisar renderizar HTML do usuário:
import DOMPurify from 'isomorphic-dompurify'
<div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(userHtml) }} />
```

### Sanitizar respostas (não vazar dados sensíveis)

```ts
function sanitizeUser(user: User) {
  const { passwordHash, resetToken, stripeSecretKey, ...safeUser } = user
  return safeUser
}

// Ou com Zod (define o que expor, não o que esconder)
const PublicUserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string(),
  plan: z.string(),
})
// Em responses:
return NextResponse.json(PublicUserSchema.parse(user))
```

### SSRF — Validar URLs externas

```ts
function validateExternalUrl(url: string): boolean {
  const parsed = new URL(url)
  const blockedHosts = ['localhost', '127.0.0.1', '169.254.169.254', '10.0.0.0/8']
  return !blockedHosts.some(h => parsed.hostname === h || parsed.hostname.startsWith(h))
}
```

### Environment Secrets

```bash
# NUNCA commitar no Git
# .env.local (desenvolvimento) — no .gitignore
DATABASE_URL=postgres://...
STRIPE_SECRET_KEY=sk_live_...
SUPABASE_SERVICE_ROLE_KEY=eyJ...
JWT_SECRET=...

# Produção: Vercel env vars, Doppler, ou 1Password Secrets Automation
# VPS: /etc/environment ou .env com chmod 600
```

---

## 5. Headers de Segurança

```ts
// next.config.ts
const securityHeaders = [
  { key: 'X-DNS-Prefetch-Control', value: 'on' },
  { key: 'Strict-Transport-Security', value: 'max-age=63072000; includeSubDomains; preload' },
  { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'Referrer-Policy', value: 'origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
]

const ContentSecurityPolicy = `
  default-src 'self';
  script-src 'self' 'unsafe-eval' 'unsafe-inline';
  style-src 'self' 'unsafe-inline';
  img-src 'self' data: blob: https:;
  connect-src 'self' https://*.supabase.co https://api.stripe.com;
  frame-src 'none';
  object-src 'none';
`.replace(/\s{2,}/g, ' ').trim()

export default {
  headers: async () => [{
    source: '/(.*)',
    headers: [
      ...securityHeaders,
      { key: 'Content-Security-Policy', value: ContentSecurityPolicy },
    ],
  }],
}
```

### Audit Logs

```ts
interface AuditLog {
  userId: string; orgId: string; action: string
  resource: string; resourceId: string
  metadata: Record<string, unknown>
  ip: string; userAgent: string
}

export async function audit(log: AuditLog) {
  await db.insert(auditLogs).values({ ...log, createdAt: new Date() })
}

// Uso em actions
await audit({
  userId: user.id, orgId: sim.orgId,
  action: 'simulation.deleted', resource: 'simulation', resourceId: sim.id,
  metadata: { productName: sim.productName },
  ip: request.headers.get('x-forwarded-for') ?? 'unknown',
  userAgent: request.headers.get('user-agent') ?? 'unknown',
})
```
