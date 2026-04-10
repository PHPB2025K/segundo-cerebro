# SaaS Patterns — Stripe, Multi-Tenancy, Feature Flags, Onboarding

## Índice
1. [Stripe — Assinaturas Completas](#1-stripe)
2. [Multi-Tenancy com Supabase RLS](#2-multi-tenancy)
3. [Feature Flags](#3-feature-flags)
4. [Onboarding Flow](#4-onboarding)
5. [Email Transacional (Resend)](#5-email)
6. [Métricas SaaS](#6-métricas)

---

## 1. Stripe

### Setup e Planos

```ts
// lib/stripe.ts
import Stripe from 'stripe'

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2024-12-18.acacia',
  typescript: true,
})

export const PLANS = {
  free:       { name: 'Free',       priceId: null,                          limits: { simulations: 5,   users: 1 } },
  starter:    { name: 'Starter',    priceId: process.env.STRIPE_PRICE_STARTER!,    limits: { simulations: 50,  users: 1 } },
  pro:        { name: 'Pro',        priceId: process.env.STRIPE_PRICE_PRO!,        limits: { simulations: 500, users: 5 } },
  enterprise: { name: 'Enterprise', priceId: process.env.STRIPE_PRICE_ENTERPRISE!, limits: { simulations: Infinity, users: Infinity } },
} as const

export type PlanId = keyof typeof PLANS

export function getPlanFromPriceId(priceId: string): PlanId {
  const entry = Object.entries(PLANS).find(([, p]) => p.priceId === priceId)
  return (entry?.[0] as PlanId) ?? 'free'
}
```

### Checkout Session

```ts
export async function createCheckoutSession({
  userId, email, priceId, returnUrl,
}: {
  userId: string; email: string; priceId: string; returnUrl: string
}) {
  // Recuperar ou criar customer
  const user = await db.query.users.findFirst({ where: eq(users.id, userId) })
  let customerId = user?.stripeCustomerId

  if (!customerId) {
    const customer = await stripe.customers.create({
      email,
      metadata: { userId },
    })
    customerId = customer.id
    await db.update(users).set({ stripeCustomerId: customerId }).where(eq(users.id, userId))
  }

  const session = await stripe.checkout.sessions.create({
    customer: customerId,
    mode: 'subscription',
    line_items: [{ price: priceId, quantity: 1 }],
    success_url: `${returnUrl}/billing/success?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${returnUrl}/billing`,
    subscription_data: {
      metadata: { userId },
      trial_period_days: 14,
    },
    allow_promotion_codes: true,
    billing_address_collection: 'auto',
  })

  return session
}

// Portal do cliente
export async function createPortalSession(customerId: string, returnUrl: string) {
  return stripe.billingPortal.sessions.create({
    customer: customerId,
    return_url: returnUrl,
  })
}
```

### Webhook Handler

```ts
// app/api/webhooks/stripe/route.ts
import { NextRequest, NextResponse } from 'next/server'
import Stripe from 'stripe'
import { stripe } from '@/lib/stripe'

export async function POST(request: NextRequest) {
  const body = await request.text()
  const sig = request.headers.get('stripe-signature')!

  let event: Stripe.Event
  try {
    event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!)
  } catch {
    return NextResponse.json({ error: 'Invalid signature' }, { status: 400 })
  }

  // Idempotência
  const existing = await db.query.processedWebhooks.findFirst({
    where: eq(processedWebhooks.stripeEventId, event.id)
  })
  if (existing) return NextResponse.json({ received: true })

  await db.insert(processedWebhooks).values({
    stripeEventId: event.id,
    type: event.type,
    processedAt: new Date(),
  })

  // Processar assincronamente (não bloquear Stripe)
  handleStripeEvent(event).catch(err => logger.error({ err, eventId: event.id }, 'Webhook failed'))

  return NextResponse.json({ received: true })
}

async function handleStripeEvent(event: Stripe.Event) {
  switch (event.type) {
    case 'checkout.session.completed': {
      const session = event.data.object as Stripe.CheckoutSession
      const sub = await stripe.subscriptions.retrieve(session.subscription as string)
      const userId = session.metadata?.userId ?? sub.metadata.userId

      await db.update(users).set({
        stripeSubscriptionId: sub.id,
        stripePriceId: sub.items.data[0].price.id,
        stripeCurrentPeriodEnd: new Date(sub.current_period_end * 1000),
        plan: getPlanFromPriceId(sub.items.data[0].price.id),
      }).where(eq(users.id, userId))
      break
    }

    case 'customer.subscription.updated': {
      const sub = event.data.object as Stripe.Subscription
      await db.update(users).set({
        stripePriceId: sub.items.data[0].price.id,
        stripeCurrentPeriodEnd: new Date(sub.current_period_end * 1000),
        plan: getPlanFromPriceId(sub.items.data[0].price.id),
        stripeStatus: sub.status,
      }).where(eq(users.stripeSubscriptionId, sub.id))
      break
    }

    case 'customer.subscription.deleted': {
      const sub = event.data.object as Stripe.Subscription
      await db.update(users).set({
        plan: 'free',
        stripeSubscriptionId: null,
        stripePriceId: null,
        stripeStatus: 'canceled',
      }).where(eq(users.stripeSubscriptionId, sub.id))
      break
    }

    case 'invoice.payment_failed': {
      const invoice = event.data.object as Stripe.Invoice
      // Notificar usuário sobre falha de pagamento
      const user = await db.query.users.findFirst({
        where: eq(users.stripeSubscriptionId, invoice.subscription as string)
      })
      if (user) await sendPaymentFailedEmail(user.email)
      break
    }
  }
}
```

### Checklist Stripe (não esquecer)

```
□ Criar produtos/preços no Stripe Dashboard
□ Configurar webhook endpoint no Stripe (produção + dev com stripe listen)
□ Verificar assinatura do webhook (constructEvent)
□ Idempotência: salvar event.id antes de processar
□ NUNCA confiar no success_url — sempre processar via webhook
□ Implementar customer portal (alterar plano, cancelar)
□ Trial period (14 dias = conversão maior)
□ Testar todos os eventos com stripe trigger
□ Adicionar allow_promotion_codes: true
□ Guardar stripeCustomerId no usuário (não criar customer duplicado)
```

---

## 2. Multi-Tenancy

### Schema Completo

```sql
-- Ver database.md para RLS completo
-- Estrutura essencial:
CREATE TABLE organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  plan TEXT NOT NULL DEFAULT 'free',
  stripe_customer_id TEXT,
  stripe_subscription_id TEXT,
  stripe_period_end TIMESTAMPTZ,
  settings JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Toda tabela de dados referencia org
CREATE TABLE simulations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  -- ... outros campos
  INDEX (org_id) -- SEMPRE indexar org_id
);
```

### Resolver org ativa (middleware)

```ts
// middleware.ts — injetar org no contexto
export async function middleware(request: NextRequest) {
  const response = NextResponse.next()

  // Resolução de org por subdomain ou slug
  const hostname = request.headers.get('host') ?? ''
  const subdomain = hostname.split('.')[0]

  if (subdomain && subdomain !== 'www' && subdomain !== 'app') {
    response.headers.set('x-org-slug', subdomain)
  }

  return response
}

// Em Server Components/Actions
async function getActiveOrg(orgSlug?: string) {
  if (!orgSlug) redirect('/select-org')
  const org = await db.query.organizations.findFirst({
    where: eq(organizations.slug, orgSlug)
  })
  if (!org) notFound()
  return org
}
```

---

## 3. Feature Flags

```ts
// lib/features.ts
type Plan = 'free' | 'starter' | 'pro' | 'enterprise'

interface PlanFeatures {
  maxSimulationsPerMonth: number
  maxUsers: number
  aiAnalysis: boolean
  exportPDF: boolean
  apiAccess: boolean
  customBranding: boolean
  prioritySupport: boolean
}

export const PLAN_FEATURES: Record<Plan, PlanFeatures> = {
  free:       { maxSimulationsPerMonth: 5,   maxUsers: 1, aiAnalysis: false, exportPDF: false, apiAccess: false, customBranding: false, prioritySupport: false },
  starter:    { maxSimulationsPerMonth: 50,  maxUsers: 1, aiAnalysis: false, exportPDF: true,  apiAccess: false, customBranding: false, prioritySupport: false },
  pro:        { maxSimulationsPerMonth: 500, maxUsers: 5, aiAnalysis: true,  exportPDF: true,  apiAccess: true,  customBranding: false, prioritySupport: true  },
  enterprise: { maxSimulationsPerMonth: Infinity, maxUsers: Infinity, aiAnalysis: true, exportPDF: true, apiAccess: true, customBranding: true, prioritySupport: true },
}

export function getFeatures(plan: Plan): PlanFeatures {
  return PLAN_FEATURES[plan] ?? PLAN_FEATURES.free
}

export function checkFeature(plan: Plan, feature: keyof PlanFeatures): boolean {
  const features = getFeatures(plan)
  return Boolean(features[feature])
}

// Uso em Server Action
export async function exportSimulationToPDF(simId: string) {
  const user = await requireAuth()
  const org = await getActiveOrg(user)

  if (!checkFeature(org.plan as Plan, 'exportPDF')) {
    return { error: 'Upgrade para o plano Starter para exportar PDFs', upgrade: true }
  }
  // ...
}

// Componente de gate
export function FeatureGate({
  feature,
  plan,
  children,
  fallback,
}: {
  feature: keyof PlanFeatures
  plan: Plan
  children: React.ReactNode
  fallback?: React.ReactNode
}) {
  if (!checkFeature(plan, feature)) {
    return fallback ?? <UpgradeCTA feature={feature} />
  }
  return children
}

// Uso
<FeatureGate feature="aiAnalysis" plan={user.plan}>
  <AIAnalysisButton />
</FeatureGate>
```

### Usage Limits

```ts
export async function checkUsageLimit(orgId: string, feature: 'simulations') {
  const org = await db.query.organizations.findFirst({ where: eq(organizations.id, orgId) })
  const plan = org?.plan as Plan ?? 'free'
  const features = getFeatures(plan)

  if (feature === 'simulations') {
    const count = await db.select({ count: count() }).from(simulations)
      .where(and(
        eq(simulations.orgId, orgId),
        gte(simulations.createdAt, startOfMonth(new Date()))
      ))
      .then(r => r[0].count)

    const limit = features.maxSimulationsPerMonth
    return {
      used: count,
      limit,
      remaining: limit === Infinity ? Infinity : Math.max(0, limit - count),
      exceeded: limit !== Infinity && count >= limit,
    }
  }
}
```

---

## 4. Onboarding

```ts
// Onboarding steps como state machine
type OnboardingStep =
  | 'create_org'
  | 'invite_team'
  | 'first_simulation'
  | 'connect_marketplace'
  | 'complete'

interface OnboardingState {
  currentStep: OnboardingStep
  completedSteps: OnboardingStep[]
  skippedSteps: OnboardingStep[]
}

async function getOnboardingState(userId: string): Promise<OnboardingState> {
  const profile = await db.query.profiles.findFirst({ where: eq(profiles.id, userId) })
  return profile?.onboardingState as OnboardingState ?? {
    currentStep: 'create_org',
    completedSteps: [],
    skippedSteps: [],
  }
}

export async function completeOnboardingStep(userId: string, step: OnboardingStep) {
  const state = await getOnboardingState(userId)
  const STEPS_ORDER: OnboardingStep[] = ['create_org', 'invite_team', 'first_simulation', 'connect_marketplace', 'complete']
  const nextIndex = STEPS_ORDER.indexOf(step) + 1
  const nextStep = STEPS_ORDER[nextIndex] ?? 'complete'

  const newState: OnboardingState = {
    ...state,
    completedSteps: [...state.completedSteps, step],
    currentStep: nextStep,
  }

  await db.update(profiles).set({ onboardingState: newState }).where(eq(profiles.id, userId))
  return newState
}
```

---

## 5. Email (Resend)

```ts
// lib/email.ts
import { Resend } from 'resend'
const resend = new Resend(process.env.RESEND_API_KEY!)

export async function sendWelcomeEmail(to: string, { name, orgSlug }: { name: string; orgSlug: string }) {
  await resend.emails.send({
    from: 'SimulImport <noreply@simulimport.com>',
    to,
    subject: `Bem-vindo ao SimulImport, ${name}!`,
    react: WelcomeEmailTemplate({ name, loginUrl: `https://app.simulimport.com/${orgSlug}` }),
  })
}

export async function sendPaymentFailedEmail(to: string) {
  await resend.emails.send({
    from: 'SimulImport <billing@simulimport.com>',
    to,
    subject: 'Falha no pagamento — ação necessária',
    react: PaymentFailedTemplate({ updateUrl: 'https://app.simulimport.com/billing' }),
  })
}

export async function sendInviteEmail(to: string, { inviterName, orgName, token }: {
  inviterName: string; orgName: string; token: string
}) {
  const acceptUrl = `https://app.simulimport.com/invite/${token}`
  await resend.emails.send({
    from: 'SimulImport <noreply@simulimport.com>',
    to,
    subject: `${inviterName} te convidou para ${orgName}`,
    react: InviteEmailTemplate({ inviterName, orgName, acceptUrl }),
  })
}

// Template de email (React Email)
import { Html, Button, Text, Section } from '@react-email/components'

function WelcomeEmailTemplate({ name, loginUrl }: { name: string; loginUrl: string }) {
  return (
    <Html>
      <Section>
        <Text>Olá, {name}!</Text>
        <Text>Sua conta no SimulImport está pronta. Comece a simular suas importações agora.</Text>
        <Button href={loginUrl}>Acessar minha conta</Button>
      </Section>
    </Html>
  )
}
```

---

## 6. Métricas SaaS

```ts
// Métricas essenciais de SaaS
interface SaasMetrics {
  mrr: number              // Monthly Recurring Revenue
  arr: number              // Annual Run Rate
  churnRate: number        // % cancelamentos no mês
  trialConversionRate: number // % trials que viram pago
  avgRevenuePerUser: number
  activeUsers: number
}

async function getSaasMetrics(): Promise<SaasMetrics> {
  const [revenueData, churnData, conversionData] = await Promise.all([
    // MRR: soma das assinaturas ativas
    db.execute(sql`
      SELECT SUM(price) as mrr FROM subscriptions
      WHERE status = 'active' AND billing_period = 'monthly'
    `),

    // Churn: cancelamentos / total inicio do mês
    db.execute(sql`
      SELECT
        COUNT(*) FILTER (WHERE status = 'canceled' AND canceled_at > DATE_TRUNC('month', NOW())) as churned,
        COUNT(*) FILTER (WHERE created_at < DATE_TRUNC('month', NOW())) as total_start
      FROM subscriptions
    `),

    // Trial conversion
    db.execute(sql`
      SELECT
        COUNT(*) FILTER (WHERE converted_at IS NOT NULL) as converted,
        COUNT(*) FILTER (WHERE trial_started_at < NOW() - INTERVAL '14 days') as expired_trials
      FROM trials
      WHERE trial_started_at > NOW() - INTERVAL '30 days'
    `),
  ])

  const mrr = revenueData[0].mrr ?? 0
  const churned = churnData[0].churned ?? 0
  const totalStart = churnData[0].total_start ?? 1
  const converted = conversionData[0].converted ?? 0
  const expiredTrials = conversionData[0].expired_trials ?? 1

  return {
    mrr,
    arr: mrr * 12,
    churnRate: (churned / totalStart) * 100,
    trialConversionRate: (converted / expiredTrials) * 100,
    avgRevenuePerUser: mrr / (totalStart || 1),
    activeUsers: totalStart - churned,
  }
}
```
