---
title: "MEMORY"
created: 2026-04-14
type: memory-config
agent: builder
status: active
tags:
  - agent/builder
---
# MEMORY.md — Índice de Memória do Builder

_Último update: 2026-05-01 04:00 BRT (Consolidação Profunda)._

---

## Índice de arquivos

- [[openclaw/agents/kobe/shared/builder/SOUL|SOUL]]
- [[openclaw/agents/kobe/shared/builder/IDENTITY|IDENTITY]]
- [[openclaw/agents/kobe/shared/builder/memory/decisions|Decisões]]
- [[openclaw/agents/kobe/shared/builder/memory/lessons|Lições]]
- [[openclaw/agents/kobe/shared/builder/memory/pending|Pendências]]

### Sessões preservadas
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-05|Sessão 2026-04-05]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-06|Sessão 2026-04-06]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-07|Sessão 2026-04-07]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-08|Sessão 2026-04-08]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-09|Sessão 2026-04-09]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-10|Sessão 2026-04-10]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-11|Sessão 2026-04-11]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-12|Sessão 2026-04-12]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-13|Sessão 2026-04-13]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-14|Sessão 2026-04-14]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-15|Sessão 2026-04-15]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-16|Sessão 2026-04-16]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-17|Sessão 2026-04-17]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-18|Sessão 2026-04-18]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-19|Sessão 2026-04-19]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-20|Sessão 2026-04-20]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-22|Sessão 2026-04-22]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-23|Sessão 2026-04-23]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-24|Sessão 2026-04-24]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-25|Sessão 2026-04-25]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-26|Sessão 2026-04-26]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-27|Sessão 2026-04-27]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-28|Sessão 2026-04-28]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-29|Sessão 2026-04-29]]
- [[openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-30|Sessão 2026-04-30]]

---

## Skills de Design/Frontend — obrigatórias em UI

1. `lovable-quality`
2. `superdesign`
3. `frontend-design-ultimate`
4. `shadcn-ui`

Briefing de frontend sem design system e sem essas skills não deve ser disparado.

## Stack padrão

| Camada | Tecnologia |
|---|---|
| Frontend | Next.js/Vite conforme repo existente |
| UI | shadcn/ui + Tailwind + tokens semânticos |
| DB/Auth | Supabase |
| Deploy | Vercel com GitHub App quando disponível; VPS/PM2/Traefik quando app já roda na VPS |
| Package manager | pnpm |
| Node | v22.x |

## Projetos ativos — estado real

| Projeto | Estado |
|---|---|
| Budamix Central | Repo GitHub + tag rollback; Full fechado com `zero_cost=0`; Estoque Fase 1.5 deployado; Fase 2/3/4 pendentes. |
| Budamix E-commerce / Blog | GitHub→Vercel auto-deploy ativo; Blog Pipeline v2 em produção; Social Studio em preview/branch, pendente QA/merge. |
| Canggu | Repo único `canguu`; edge functions + admin em Vercel; B1 segurança e B3 resiliência pendentes. |
| Ponto Certo / RH | Conversas RH implementado; confirmar/deploy produção se ainda estiver local; monitor real em 04/05 10h BRT. |
| SimulImport / Bidspark / Atlas | Fora da frente imediata. |

## Regras de qualidade

- Confirmar repo/deploy real antes de mexer em UI/admin.
- App de produção sem Git precisa baseline + tag rollback antes de refactor.
- Build OK não basta: smoke renderizado da rota e superfícies relacionadas.
- Geração longa precisa job/status persistido; não confiar em webhook HTTP síncrono.
- Secrets nunca em Code node/export/workflow tracked.

---
_Consolidação Profunda 2026-05-01: sessões brutas de março removidas; índice atualizado para o estado real pós-30/04._
