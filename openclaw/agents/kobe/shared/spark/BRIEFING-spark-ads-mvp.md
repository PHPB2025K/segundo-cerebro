---
title: "BRIEFING spark ads mvp"
created: 2026-04-14
type: briefing
agent: kobe
status: active
tags:
  - agent/kobe
---

# BRIEFING: Spark Ads — MVP (Fase 1)

_Para: Builder | De: Kobe | Data: 2026-03-23_

---

## Objetivo

Construir o **Spark Ads** — webapp de gestão de tráfego pago da GB Importadora. Dashboard profissional e moderno que consolida **Google Ads + Meta Ads** em uma única interface.

**Usuário inicial:** Pedro Broglio (único usuário por enquanto).

---

## Escopo Fase 1 — MVP

### 1. Auth
- Login via Supabase Auth (email/password — só Pedro por enquanto)
- Middleware de proteção de rotas
- Seed inicial com usuário Pedro

### 2. Dashboard Principal
- **Design:** Moderno, profissional, dark mode (design system da GB)
- **Separação visual clara** entre Google Ads e Meta Ads:
  - Cada plataforma com seu branding (cores, ícones)
  - Google Ads: azul/verde (`#4285F4`, `#34A853`)
  - Meta Ads: azul Meta (`#0668E1`)
  - Cards/seções claramente identificáveis por plataforma
- **KPIs consolidados** (topo):
  - Total Spend, Total Revenue, ROAS geral, CPA médio
  - Variação % vs período anterior
- **KPIs por plataforma** (lado a lado):
  - Spend, Revenue, ROAS, CPA, CTR, CPC, CPM, Impressões, Cliques, Conversões
- **Filtros:**
  - Período: Hoje, 7d, 30d, Mês atual, Custom range
  - Plataforma: Todas, Google, Meta
- **Gráficos:**
  - Spend over time (line chart, Google vs Meta)
  - ROAS over time (line chart, Google vs Meta)
  - Spend breakdown by platform (donut/pie)
- **Indicador de saúde:** ROAS vs meta (10x)

### 3. Listagem de Campanhas
- Tabela filtrada por plataforma, status, tipo
- Colunas: Nome, Plataforma (ícone), Status, Tipo, Budget, Spend, Impressões, Cliques, CTR, Conversões, CPA, ROAS
- Sorting por qualquer coluna
- Badge de plataforma (Google/Meta) em cada linha
- Status visual: ativo (verde), pausado (amarelo), removido (cinza)
- Click → detalhamento (fase futura, por enquanto read-only)

---

## Stack (já definida — não mudar)

| Camada | Tech |
|---|---|
| Frontend | Next.js 15 + React 19 + App Router |
| Styling | Tailwind CSS + shadcn/ui |
| Charts | Recharts ou Tremor |
| DB | Supabase (Postgres) + Drizzle ORM |
| Auth | Supabase Auth |
| Language | TypeScript (strict) |
| Package manager | pnpm |

---

## APIs — Credenciais e Endpoints

### Google Ads API
- **Versão:** v23 (IMPORTANTE: v19 sunset, não usar)
- **Endpoint:** `https://googleads.googleapis.com/v23/`
- **Customer ID:** 7625801774 (GB Distribuição)
- **Manager Account:** 9656686533 (TrafficAI)
- **Auth:** OAuth 2.0 (refresh token → access token)
- **Query:** POST `customers/{id}/googleAds:searchStream` com GAQL
- **Headers:**
  - `Authorization: Bearer {access_token}`
  - `developer-token: {dev_token}`
  - `login-customer-id: 9656686533`
- **1Password:** "Google Ads API - Spark" (vault OpenClaw)

### Meta Ads API
- **Versão:** v21.0
- **Endpoint:** `https://graph.facebook.com/v21.0/`
- **Ad Account:** act_323534883953033
- **Auth:** Long-lived access token
- **1Password:** "Meta Ads API - KOBE.OPENCLAW" (vault OpenClaw)

### Supabase
- **URL:** https://wzhmrpskiscassbixurr.supabase.co
- **Project Ref:** wzhmrpskiscassbixurr
- **1Password:** "Supabase - Spark Ads" (vault OpenClaw)

---

## Arquitetura

```
src/
├── app/
│   ├── (auth)/
│   │   └── login/page.tsx
│   ├── (dashboard)/
│   │   ├── layout.tsx          ← Sidebar + header
│   │   ├── page.tsx            ← Dashboard principal
│   │   └── campaigns/
│   │       └── page.tsx        ← Listagem de campanhas
│   └── api/
│       ├── google-ads/         ← Proxy para Google Ads API
│       └── meta-ads/           ← Proxy para Meta Ads API
├── components/
│   ├── ui/                     ← shadcn/ui
│   ├── dashboard/
│   │   ├── kpi-card.tsx
│   │   ├── platform-section.tsx
│   │   ├── spend-chart.tsx
│   │   └── roas-chart.tsx
│   └── campaigns/
│       └── campaign-table.tsx
├── lib/
│   ├── google-ads/
│   │   ├── client.ts           ← Auth + query helper
│   │   └── queries.ts          ← GAQL queries
│   ├── meta-ads/
│   │   ├── client.ts           ← Auth + fetch helper
│   │   └── queries.ts          ← Queries/endpoints
│   ├── supabase/
│   │   ├── client.ts
│   │   └── server.ts
│   └── utils.ts
├── hooks/
│   └── use-date-range.ts
├── types/
│   ├── google-ads.ts
│   ├── meta-ads.ts
│   └── dashboard.ts
└── styles/
    └── globals.css
```

### Fluxo de dados
1. **Frontend** chama API Routes do Next.js
2. **API Routes** fazem chamadas autenticadas pra Google Ads API e Meta Ads API
3. **API Routes** normalizam os dados num formato unificado
4. **Frontend** renderiza com os dados normalizados

### Segurança
- Credenciais ficam em variáveis de ambiente (server-side only)
- Nunca expor tokens no client
- API Routes como proxy — frontend nunca fala direto com Google/Meta

---

## Schema Supabase (mínimo para MVP)

```sql
-- Usuários gerenciados pelo Supabase Auth

-- Cache de métricas (evitar rate limits e acelerar dashboard)
CREATE TABLE daily_metrics (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  platform TEXT NOT NULL CHECK (platform IN ('google_ads', 'meta_ads')),
  campaign_id TEXT NOT NULL,
  campaign_name TEXT,
  campaign_status TEXT,
  campaign_type TEXT,
  date DATE NOT NULL,
  impressions BIGINT DEFAULT 0,
  clicks BIGINT DEFAULT 0,
  cost_micros BIGINT DEFAULT 0,
  conversions NUMERIC(10,2) DEFAULT 0,
  conversions_value NUMERIC(12,2) DEFAULT 0,
  ctr NUMERIC(6,4),
  cpc_micros BIGINT,
  cpm_micros BIGINT,
  synced_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(platform, campaign_id, date)
);

-- Configurações
CREATE TABLE settings (
  key TEXT PRIMARY KEY,
  value JSONB NOT NULL,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- RLS
ALTER TABLE daily_metrics ENABLE ROW LEVEL SECURITY;
ALTER TABLE settings ENABLE ROW LEVEL SECURITY;

-- Policy: authenticated users can read all
CREATE POLICY "Authenticated users can read metrics" ON daily_metrics
  FOR SELECT TO authenticated USING (true);

CREATE POLICY "Authenticated users can read settings" ON settings
  FOR SELECT TO authenticated USING (true);
```

---

## Requisitos de Design

- **Dark mode** por padrão (consistente com design system GB)
- **Profissional e limpo** — não parecer template genérico
- **Separação de plataformas é PRIORIDADE** — Pedro quer ver claramente o que é Google e o que é Meta
- **Responsivo** — funciona no laptop com 2 telas do Pedro
- **Sidebar** com navegação: Dashboard, Campaigns, (futuro: Budget, Reports, Settings)
- **Paleta:**
  - Background: `#0a0a0a` / #111111
  - Cards: `#1a1a1a` com border `#2a2a2a`
  - Google Ads: `#4285F4` (accent)
  - Meta Ads: `#0668E1` (accent)
  - Positive: `#22c55e`
  - Negative: `#ef4444`
  - Neutral text: `#a1a1aa`

---

## Repo

- Criar repo `spark-ads` no GitHub (PHPB2025K)
- Private
- Branch: main
- README com setup instructions

---

## Entregáveis Fase 1

1. ✅ Repo GitHub configurado
2. ✅ Supabase schema aplicado
3. ✅ Auth funcionando (login/logout)
4. ✅ Dashboard com dados reais de Google Ads + Meta Ads
5. ✅ Listagem de campanhas com filtro por plataforma
6. ✅ Deploy funcional (local dev ou Vercel preview)

---

## O que NÃO fazer nesta fase

- Não implementar gestão de campanhas (criar/pausar/editar) — só leitura
- Não implementar alertas/insights proativos
- Não implementar exportação PDF/Excel
- Não implementar gestão de criativos
- Não over-engineer — MVP funcional > arquitetura perfeita

---

## Referências no workspace

- `skills/marketing/google-ads/SKILL.md` — Skill completa com GAQL queries
- `skills/marketing/meta-ads/SKILL.md` — Skill Meta Ads com endpoints
- `skills/design/report-design-system/SKILL.md` — Design system
- `memory/projects/traffic-agent.md` — Plano completo dos 7 módulos
- `shared/spark/SOUL.md` — Identidade do Spark
