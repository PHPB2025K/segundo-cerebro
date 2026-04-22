---
title: "Mapeamento de Credenciais — 1Password Vault OpenClaw"
type: reference
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - knowledge
  - credenciais
  - seguranca
  - 1password
---

# Mapeamento de Credenciais — 1Password Vault OpenClaw

> Referência de onde cada credencial está armazenada e para que serve.
> **NUNCA incluir valores aqui** — apenas referências ao 1Password.
> Acesso CLI: `op item get "<nome>" --vault "OpenClaw"`

---

## Acesso ao Vault

```bash
# Service Account Token (em ~/.zshrc, ~/.bashrc, ~/.profile)
export OP_SERVICE_ACCOUNT_TOKEN="..."

# Listar todos os itens
op item list --vault "OpenClaw"

# Obter um item específico
op item get "Nome do Item" --vault "OpenClaw" --fields label=password
```

---

## Supabase (6 items)

| Item 1Password | Tipo | Projeto | Usado em |
|----------------|------|---------|----------|
| Supabase Access Token - CLI | API_CREDENTIAL | Todos | CLI (`supabase` commands) |
| Supabase - Budamix Ecommerce - Anon Key | API_CREDENTIAL | `ioujfkrqvporfbvdqyus` | Frontend checkout |
| Supabase - Budamix Ecommerce - Service Role | API_CREDENTIAL | `ioujfkrqvporfbvdqyus` | Edge Functions, admin ops |
| Supabase - Budamix Ecommerce - DB Password | API_CREDENTIAL | `ioujfkrqvporfbvdqyus` | Direct DB connection |
| Supabase - Budamix Central | LOGIN | `sqbkoprcmnznmzbwdrmf` | Dashboard, analytics, produtos, pgvector |
| Supabase - Spark Ads | API_CREDENTIAL | `wzhmrpskiscassbixurr` | Cache Meta/Google Ads ([[openclaw/agents/spark/IDENTITY\|Spark]]) |

---

## Mercado Pago (7 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Mercado Pago - Budamix Ecommerce - Access Token | API_CREDENTIAL | Edge Function `create-mp-payment` |
| Mercado Pago - Budamix Ecommerce - Public Key | API_CREDENTIAL | Frontend Payment Brick |
| Mercado Pago - Budamix Ecommerce - Client ID | API_CREDENTIAL | OAuth integration |
| Mercado Pago - Budamix Ecommerce - Client Secret | API_CREDENTIAL | OAuth integration |
| Mercado Pago - Budamix Ecommerce - Webhook Secret | API_CREDENTIAL | Edge Function `mp-webhook` (HMAC) |
| Mercado Pago - Budamix Ecommerce - Test Access Token | API_CREDENTIAL | Ambiente teste |
| Mercado Pago - Budamix Ecommerce - Test Public Key | API_CREDENTIAL | Ambiente teste |

---

## Bling ERP (3 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Bling API - Matriz (58.151.616/0001-43) | API_CREDENTIAL | [[openclaw/agents/fisco/IDENTITY\|Fisco]], NF-e Matriz |
| Bling API - Filial (58.151.616/0002-24) | API_CREDENTIAL | [[openclaw/agents/fisco/IDENTITY\|Fisco]], NF-e Filial |
| Bling API - Filial | LOGIN | OAuth tokens Filial |

---

## Amazon (3 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Amazon SP-API - Tobias | API_CREDENTIAL | [[openclaw/agents/trader/IDENTITY\|Trader]], listings, orders, FBA |
| Amazon SP-API - Budamix Ads Automation | LOGIN | [[openclaw/agents/spark/IDENTITY\|Spark]], ads automation |
| AWS Console - GB Importadora (root) | LOGIN | Console AWS (SP-API IAM) |
| AWS IAM - sp-api-tobias | LOGIN | IAM user para SP-API |

---

## Mercado Livre (3 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Mercado Livre API - Openclaw.agent | API_CREDENTIAL | [[openclaw/agents/trader/IDENTITY\|Trader]], vendas |
| Mercado Livre API - Financeiro | LOGIN | Agente financeiro, conciliação |
| Mercado Livre API - Métricas | LOGIN | Dashboard métricas |

---

## Shopee (2 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Shopee Open Platform - Openclaw Agent | LOGIN | [[openclaw/agents/trader/IDENTITY\|Trader]], 3 lojas |
| Shopee Open Platform - Canggu Chat (NÃO USAR) | LOGIN | Legado — não usar |

---

## Comunicação (4 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Evolution API Cloudfy | LOGIN | WhatsApp envio (N8N) |
| Evolution API Cloudfy - WhatsApp Kobe | LOGIN | WhatsApp Kobe (+55 19 99845-8149) |
| Telegram Bot Token | PASSWORD | @TOBIAS_USER_BOT, Kobe Hub |
| Gmail Openclaw | LOGIN | Email agente |

---

## GB Import Hub (5 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| gb-import-hub-resend-api-key | LOGIN | Email transacional (Resend) |
| gb-import-hub-terminal49-api-key | LOGIN | Tracking containers |
| gb-import-hub-terminal49-webhook-secret | LOGIN | Webhook validation |
| gb-import-hub-mapbox-token | LOGIN | Mapas tracking |
| gb-import-hub-notification-email | LOGIN | Destinatário notificações |
| gb-import-hub-supabase-anon | API_CREDENTIAL | Frontend Import Hub |
| gb-import-hub-supabase-service-role | API_CREDENTIAL | Edge Functions Import Hub |

---

## Ads (3 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Meta Ads API - KOBE.OPENCLAW | API_CREDENTIAL | [[openclaw/agents/spark/IDENTITY\|Spark]], campanhas Meta |
| Google Ads API - Spark | API_CREDENTIAL | [[openclaw/agents/spark/IDENTITY\|Spark]], campanhas Google |
| Stripe API Keys (Test) | LOGIN | Legado — Stripe removido, migrado MP |

---

## AI & Search (4 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Anthropic Setup Token | PASSWORD | Claude API (migrando para OpenAI) |
| OpenAI API Key - Whisper | PASSWORD | Transcrição áudio |
| Perplexity API | PASSWORD | Jornal da Manhã |
| Brave | LOGIN | Busca web (agentes) |

---

## Scraping & Data (2 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| Bright Data Web Unlocker | API_CREDENTIAL | Web scraping ML/Amazon |
| Bright Data Scraping Browser | LOGIN | Browser automation |

---

## Outros (5 items)

| Item 1Password | Tipo | Usado em |
|----------------|------|----------|
| GitHub PAT - PHPB2025K | PASSWORD | Git push, GitHub CLI |
| Service Account Auth Token: agent.assistant.openclaw | API_CREDENTIAL | 1Password CLI (OP_SERVICE_ACCOUNT_TOKEN) |
| Mission Control - Kobe | LOGIN | TenacitOS — dashboard de monitoramento OpenClaw, roda como PM2 na VPS, coleta usage data (cron hourly) |
| RapidAPI - Tobias Agent | LOGIN | Instagram API (instagram120) |
| Upseller ERP | LOGIN | Hub multi-marketplace, gestão de SKUs armazém (apelidos), exports para [[openclaw/agents/fisco/IDENTITY\|Fisco]] |
| Google Workspace - Tobias Agent | LOGIN | Calendar, Gmail integrations |
| Apify - API Token | PASSWORD | Web scraping (Apify) |

---

## Resumo

| Categoria | Qtd Items |
|-----------|:---------:|
| Supabase | 6 |
| Mercado Pago | 7 |
| Bling ERP | 3 |
| Amazon | 4 |
| Mercado Livre | 3 |
| Shopee | 2 |
| Comunicação | 4 |
| GB Import Hub | 7 |
| Ads | 3 |
| AI & Search | 4 |
| Scraping | 2 |
| Outros | 7 |
| **Total** | **53** |

---

## Notas Relacionadas

- [[knowledge/concepts/stack-tecnico]] — stack tecnológico completo
- [[memory/context/business-context]] — contexto geral
- [[openclaw/agents/kobe/IDENTITY]] — agente principal
