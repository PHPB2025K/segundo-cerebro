---
title: "Stack Tecnológico — OpenClaw / Budamix"
type: reference
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - knowledge
  - stack
  - infraestrutura
  - dev
---

# Stack Tecnológico — OpenClaw / Budamix

> Fonte de verdade sobre todas as tecnologias, serviços e integrações usados.
> Credenciais: todas no 1Password vault OpenClaw → [[knowledge/concepts/credenciais-map]]

---

## Infraestrutura

| Componente | Detalhes |
|------------|----------|
| **VPS** | Hostinger Ubuntu 24.04, IP 187.77.237.231 |
| **Supabase** | 5 projetos (ver tabela abaixo) |
| **Vercel** | budamix-ecommerce (prj_wMl99f4aixldKCwBiJv9xDedL7AR) |
| **GitHub** | Org PHPB2025K (23 repos ativos, 7 arquivados) |
| **1Password** | Vault OpenClaw, Service Account: agent.assistant.openclaw |
| **DNS** | Cloudflare (budamix.com.br) |

### Projetos Supabase

| Project Ref | Projeto | Região | Uso |
|-------------|---------|--------|-----|
| `ioujfkrqvporfbvdqyus` | Budamix E-commerce | sa-east-1 | Auth, DB, Storage, Edge Functions, checkout MP |
| `iriqmqxuppfyrnselswk` | Budamix Central / OpenClaw | — | Produtos, orders, analytics, storage buckets |
| `dgldsmhbeosjgfrbegyv` | Ponto Certo | — | RH, ponto, salários, compliance |
| `nvramnisawnwrbvadcmg` | Staging / N8N | — | Testes, workflows N8N |
| A PREENCHER | GB Import Hub | — | Importações, containers, documentos |

---

## Linguagens & Runtimes

| Linguagem | Versão | Uso |
|-----------|--------|-----|
| Node.js | v22 | Backend automações, OpenClaw |
| Python | 3.x | Scripts (sync, backfill, ads) |
| TypeScript | — | React apps, type safety |
| Bash | — | Scripting, DevOps, crons |
| Deno | — | Supabase Edge Functions |

---

## Frontend

| Tecnologia | Uso |
|------------|-----|
| React | v18.3.1 — apps web, dashboards |
| Vite | v5.4.19 — build tool |
| Next.js | SSR/SSG (estoque, import hub) |
| Tailwind CSS | Utility-first styling |
| shadcn/ui | Component library |
| React Router DOM | v6 — client-side routing |
| Lovable | AI-assisted design (legado, migrando) |

---

## Backend & Banco

| Tecnologia | Uso |
|------------|-----|
| Supabase | Auth, PostgreSQL 17, Storage, Edge Functions, Realtime, RLS |
| pgvector | Busca vetorial (embeddings 384d) — Budamix Central |
| Edge Functions | Deno runtime — checkout, webhooks, APIs |
| N8N | Workflow automation (trottingtuna-n8n.cloudfy.live) |
| FastAPI | Amazon Ads Automation (Python) |

---

## Agentes AI

| Agente | Modelo | Função |
|--------|--------|--------|
| [[openclaw/agents/kobe/IDENTITY\|Kobe]] | GPT 5.4 | Orquestrador principal, Telegram |
| [[openclaw/agents/trader/IDENTITY\|Trader]] | GPT 5.4 | Marketplace (ML, Shopee, Amazon) |
| [[openclaw/agents/spark/IDENTITY\|Spark]] | GPT 5.4 | Ads (ML, Amazon, Meta, Google) |
| [[openclaw/agents/builder/IDENTITY\|Builder]] | GPT 5.4 | Dev, MicroSaaS, APIs |
| [[openclaw/agents/fisco/IDENTITY\|Fisco]] | GPT 5.4 | NF-e, Bling ERP, fiscal |
| [[openclaw/agents/rh/IDENTITY\|RH]] | GPT 5.1-mini | Ponto, salários, compliance |
| Ana/Giovana | N8N + Evolution API | Atendimento WhatsApp clientes |
| Claude Code | Opus 4.6 (1M context) | Desenvolvimento, VS Code |

**OpenClaw**: v2026.4.5, Gateway 127.0.0.1:18789 (loopback only)
**Custo AI**: ~$120/mês (migrando de Anthropic para OpenAI)

---

## APIs & Integrações

### Marketplaces

| API | Uso | Sync |
|-----|-----|------|
| Amazon SP-API | Listings, orders, FBA, request review | ≤5min |
| Amazon Ads API | Campanhas, bids, métricas | Cron |
| Mercado Livre API | 3 apps (Vendas, Financeiro, Métricas) | ≤2min |
| ML Ads API | Gestão automatizada de bids | Cron |
| Shopee Open API v2 | 3 contas OAuth, listings, logistics | ≤2min |

### Pagamentos

| API | Uso |
|-----|-----|
| Mercado Pago | Checkout e-commerce (Pix + Cartão + Débito), Payment Brick, webhook HMAC-SHA256 |

### ERP & Fiscal

| API | Uso |
|-----|-----|
| Bling ERP | NF-e, distribuição fiscal, conciliação. Plano Mercúrio. Matriz + Filial |

### Comunicação

| API | Uso |
|-----|-----|
| Evolution API | WhatsApp envio/recebimento (Cloudfy) |
| Baileys | WhatsApp leitura passiva |
| Telegram Bot API | @TOBIAS_USER_BOT, Kobe Hub 11 tópicos |
| Resend | Email transacional (GB Import Hub) |

### Logística & Dados

| API | Uso |
|-----|-----|
| Terminal49 | Tracking de containers, webhooks |
| Bright Data | Web scraping (web_unlocker1) |
| Mapbox | Mapas no GB Import Hub |
| Brave Search | Pesquisa web (agentes) |
| Perplexity API | Jornal da Manhã (digest diário) |

### Ads

| API | Uso |
|-----|-----|
| Meta Ads API | Campanhas Facebook/Instagram |
| Google Ads API | Campanhas Google (Spark) |

---

## DevTools

| Ferramenta | Uso |
|------------|-----|
| VS Code | Editor + Claude Code plugin + MCPs (Supabase, Context7, Playwright, Frontend Design, n8n) |
| Git | v2.43.0, GitHub CLI (gh) |
| Supabase CLI | Migrations, edge functions, DB management |
| Vercel CLI | Deploy frontend (`vercel --prod`) |
| 1Password CLI | Credenciais (`op item get`, Service Account Token) |
| SSH | Acesso VPS 187.77.237.231 |
| Docker | Containers (uso limitado, OpenClaw roda no host) |

---

## Segurança

| Camada | Implementação |
|--------|---------------|
| Credenciais | 1Password vault OpenClaw (53 items) |
| Auth | Supabase Auth (role-based: admin/viewer) |
| RLS | Row-Level Security em todas as tabelas Supabase |
| Webhooks | HMAC-SHA256 (MP), webhook secrets (Terminal49) |
| VPS | UFW firewall (porta 8084 sob revisão) |
| Env vars | .env.local (local), Supabase Secrets (edge), Vercel env (frontend) |

---

## Notas Relacionadas

- [[knowledge/concepts/credenciais-map]] — mapeamento de credenciais 1Password
- [[memory/context/business-context]] — contexto geral
- [[openclaw/agents/kobe/IDENTITY]] — agente principal
- [[projects/_index]] — projetos que usam este stack
- [[knowledge/pessoal/perfil-pedro-broglio]] — perfil do Pedro
