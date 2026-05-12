---
title: "Mission Control"
created: 2026-05-12
type: project
status: active
path: "/var/www/mission-control/ (VPS, deploy in-place)"
tags:
  - project
  - openclaw
---

# Mission Control

Painel visual da operação OpenClaw/Kobe — dashboard único com crons, agentes, custos, health, memory browser, terminal e Office 3D.

**URL:** [https://mission.budamix.com.br](https://mission.budamix.com.br) — autenticação via senha (1Password OpenClaw)

**Origem:** fork customizado do [TenacitOS](https://github.com/carlosazaustre/tenacitOS) — projeto open-source de Carlos Azaustre, adaptado para a operação GB Importadora.

---

## Stack

- Next.js 16.1 + React 19 + Tailwind v4 + TypeScript
- PM2 (porta 3092 loopback) atrás de Traefik
- Better-sqlite3 para `activities.db` + `usage-tracking.db` em `data/`
- Service Worker (PWA) com cache versionado (network-first pra HTML)
- Three.js + React Three Fiber para Office 3D

---

## Status atual (12/05/2026)

| Camada | Status |
|--------|--------|
| Deploy + HTTPS | ✅ `mission.budamix.com.br`, Let's Encrypt válido até 10/08/2026 |
| Frontend 100% | ✅ Design System Budamix Central aplicado, sem hardcodes, PT-BR completo, sem crashes residuais (sweep de 34 defensive checks) |
| Dashboard `/` | ✅ PRD completo implementado — stats reais, agentes com status live, activity feed populado, logo removido a pedido do Pedro |
| Backend: `/api/agents` | ✅ Status detection real via vault sessions, thresholds 2h/24h, botToken detection |
| Backend: `activities.db` | ✅ Popula via `scripts/activity-collector.py` + crontab `*/5min` parseando headings `## titulo — HH:MM BRT` |
| PRDs por módulo restantes | ⏳ Cron, Tasks, Sessions, Skills (precisa `configured-skills.json`), Agents detail, Office 3D, Activity, Analytics, Reports, System, Git, Files, Memory, Search, Logs, Terminal, Calendar, Reports, About |

---

## Arquitetura

```
/var/www/mission-control/
├── src/app/(dashboard)/     ← 24 páginas
├── src/components/ui/       ← Button, Card, Badge, Skeleton (do Budamix Central)
├── src/lib/utils.ts         ← cn() helper
├── data/
│   ├── activities.db        ← populada por activity-collector
│   └── usage-tracking.db    ← populada por collect-usage-cron
├── scripts/
│   ├── activity-collector.py  ← lê vault sessions, popula activities.db
│   └── collect-usage-cron.sh  ← usage de tokens (já existia)
└── public/
    └── sw.js                ← network-first HTML, cache-first assets
```

---

## Componentes / decisões importantes

- **Domínio:** `mission.budamix.com.br` (Registro.br, mesmo padrão de `estoque.` e `ponto.`) — abandonado o `mission.gbformulario.com` original do PRD (Squarespace + Google Cloud DNS, gestão dupla desnecessária).
- **Design System:** copiado do [[projects/budamix-central|Budamix Central]] — globals.css completo + 4 componentes UI + Google Fonts (Space Grotesk + Plus Jakarta Sans + JetBrains Mono).
- **Status dos agentes:** detectado por mtime do session file mais recente no vault (`~/segundo-cerebro/memory/sessions/` p/ main, `~/segundo-cerebro/openclaw/agents/<id>/memory/sessions/` p/ sub-agentes). Online <2h, idle <24h, offline >24h.
- **Activity feed:** parser regex `## Descrição — HH:MM BRT` extrai eventos das sessions do vault. Type heurístico (cron/build/message/search/file/security). Idempotente via UUID = md5(timestamp|description).
- **Service Worker:** versão `mc-v5` (bumpada a cada deploy visual relevante). Network-first pra HTML evita ficar preso em build antigo no browser do Pedro.

---

## Caminho do PRD por módulo

Plano definido em 12/05: depois do Dashboard fechado, vamos abrindo **1 PRD por página** garantindo backend 100% sincronizado com frontend antes de seguir pro próximo.

Próximos sugeridos por valor diário:
1. ✅ Dashboard `/`
2. ⏳ Cron Jobs `/cron` — 31 crons OpenClaw consultados diariamente
3. ⏳ Tasks `/tasks` — parser de `pendencias.md` já existe e funciona, 54 tasks reais
4. ⏳ Sessions `/sessions` — usage SQLite + mensagens
5. ⏳ Agents `/agents` (detail view, separado do dashboard)
6. ⏳ Skills `/skills` — backend depende de `configured-skills.json` ausente

---

## Ver também

- [[openclaw/agents/kobe/docs/prd-mission-control|PRD original Mission Control (30/03)]] — TenacitOS upstream + visão original
- [[openclaw/agents/kobe/IDENTITY|Kobe]] — agente principal cuja operação o painel reflete
- [[projects/budamix-central]] — origem do Design System
- [[memory/context/decisoes/2026-05]] — decisões da retomada
- [[knowledge/concepts/stack-tecnico]] — Traefik, PM2, Let's Encrypt
