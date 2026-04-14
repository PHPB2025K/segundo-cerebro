---
title: "decisions"
created: 2026-04-14
type: agent
agent: builder
status: active
tags:
  - agent/builder
---

# Decisões — Builder

_Registro de decisões permanentes. NUNCA contradizer._

## Stack

### Stack padrão definido (2026-03-19)
- **Frontend:** Next.js 15 + React 19 + Tailwind + shadcn/ui
- **Backend full-stack:** Next.js API Routes + Server Actions
- **Backend standalone:** FastAPI (Python) — para APIs independentes, ML, data
- **DB:** Supabase (Postgres) + Drizzle ORM
- **Auth:** Supabase Auth
- **Deploy SaaS:** Vercel
- **Deploy interno:** VPS com Docker
- **Pagamentos:** Stripe
- **Versionamento:** Git + GitHub (PHPB2025K)
- **Package manager:** pnpm
- **TypeScript:** Strict mode sempre

### Commits convencionais (2026-03-19)
- Formato: `feat:`, `fix:`, `refactor:`, `chore:`, `docs:`
- Nunca commitar direto em main (L1)

## Segurança

### Credenciais — NUNCA em código (2026-03-17)
- Credenciais vão para 1Password vault "OpenClaw" ou variáveis de ambiente
- Nunca em código, commits, CLAUDE.md, ou arquivos de contexto de IA
- **Case real:** Auditoria Bidspark encontrou Client ID + Secret em plain text no CLAUDE.md do Amazon Ads

### Bidspark — Ambiente sandbox (2026-03-17)
- Amazon Ads está em sandbox. Antes de ativar otimizações reais: confirmar `AMAZON_ADS_ENVIRONMENT=production` no `.env`
- Não ir pra produção sem trocar

## Projetos

### Bidspark — Validação antes de test users (2026-03-17)
- Pedro quer acumular semanas de dados de otimização real (Amazon Ads) antes de abrir para test users
- Comprovar redução de ACOS e melhoria de ROAS com case próprio primeiro
- Bloqueio atual: zero testes unitários — precisa de suite mínima antes de produção
- Status: ~90% pronto tecnicamente. Bloqueio = validação de resultados, não código

## Operacional

### Team Agents (2026-03-19)
- Builder é agente especializado dev/MicroSaaS
- Coordenado pelo Kobe — nunca fala direto com Pedro
- Resultados sempre entregues ao Kobe para validação
