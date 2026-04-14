# TOOLS.md — Cheat Sheet Rápido

_Consulta rápida para paths, comandos e versões. Detalhes completos em MEMORY.md._

---

## Ambiente

| Tool | Versão | Path/Config |
|---|---|---|
| Node.js | v22.22.1 | `nvm` |
| Python | 3.12.3 | System |
| pnpm | 10.32.1 | Package manager padrão |
| Docker | 29.2.1 | `docker` / `docker-compose` |
| Git | 2.43.0 | GitHub: PHPB2025K |
| Nginx | ❌ Não instalado | Instalar quando necessário |

## VPS

| Campo | Valor |
|---|---|
| IP | 187.77.237.231 |
| DNS | `api.importadoragb.com.br` |
| OS | Ubuntu 24.04 |

## Quick Reference — Commands

```bash
# Scaffold Next.js
skills/dev/fullstack-dev/scripts/init-nextjs-project.sh [nome]

# Scaffold FastAPI
skills/dev/fullstack-dev/scripts/init-fastapi-project.sh [nome]

# Deploy VPS
skills/dev/fullstack-dev/scripts/deploy-vps.sh [projeto]

# 1Password — buscar credencial
op item get "[item]" --vault "OpenClaw"
```

## Quick Reference — Paths

| O quê | Onde |
|---|---|
| Outputs → Kobe | `shared/outputs/` |
| Lições compartilhadas | `shared/lessons/` |
| Repos | `github.com/PHPB2025K/[repo]` |
| Dados temporários | `/tmp/builder/` |

## Stack Padrão (decisão vigente)

| Camada | Default |
|---|---|
| Frontend | Next.js 15 + React 19 + Tailwind + shadcn/ui |
| Backend full-stack | Next.js API Routes |
| Backend standalone | FastAPI |
| DB | Supabase (Postgres) + Drizzle ORM |
| Auth | Supabase Auth |
| Deploy SaaS | Vercel |
| Deploy interno | VPS + Docker |
| Pagamentos | Stripe |

---

_Para infraestrutura completa e repos: MEMORY.md seção 6._
_Para skills de dev: MEMORY.md seção 7._
