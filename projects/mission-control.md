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

## Status atual (13/05/2026)

| Camada | Status |
|--------|--------|
| Deploy + HTTPS | ✅ `mission.budamix.com.br`, Let's Encrypt válido até 10/08/2026 |
| Frontend 100% | ✅ Design System Budamix Central aplicado |
| `/` Dashboard | ✅ PRD v2 fechado (KPIs com comparativos 7d, agentes live, atividade SSE, notepad SQLite, ⌘K command palette, telemetria UI_EVENT, WeatherWidget PT-BR) |
| `/system` System Monitor | ✅ PRD v1 fechado (3 tabs: Hardware/Serviços/Rede; CPU correto via /proc/stat; 14/15 serviços reais; sparklines persistentes 24h; ações Start/Stop/Restart com allowlist) |
| `/files` Files | ✅ PRD v1 fechado (8 workspaces; Monaco editor lazy; markdown render; CRUD com lixeira 7d; search nome+conteúdo opcional; path traversal bloqueado) |
| `/agents` Agents | ✅ PRD v1 fechado (3 tabs: Cards/Organograma SVG/Atividade swimlanes 24h; AgentDrawer drill-down com SOUL+stats+5 atividades+4 ações; bot Telegram badge) |
| `/memory` Memory | ✅ PRD v1 fechado (visão temática do vault Obsidian; 5 tabs: Recentes/Buscar/Pendências/Decisões/MOCs; NoteView markdown+edit+Ctrl+S; backlinks; captura rápida em inbox) |
| `/office` Office 3D | ✅ PRD v1 fechado (i18n PT-BR; ControlsPanel colapsável; AgentDrawer reuse; OFFICE_STATUS_COLORS 5 status; workspaceRadius anti-aglomeração; Whiteboard 3D dinâmico com top 3 pendências críticas) |
| `/activity` Activity Log | ✅ PRD v1 fechado 14/05 (i18n PT-BR; UI_EVENT hidden default + toggle; heatmap 12w/26w/52w default 52w; ActivityDrawer desktop + expand mobile; deep-link `?agent=`; custom date range; export CSV) |
| `/cron` Cron Jobs | ✅ PRD v1 fechado 14/05 (API lê `jobs.json` + `jobs-state.json` + `runs/*.jsonl` direto — antes execSync travava 15s; 83 jobs <100ms; filtros agente/status/erros; schedule humanizado em BRT; CronDrawer com 50 runs+payload; toggle escreve no jobs.json + reload) |
| `/sessions` Sessions | ✅ PRD v1 fechado 14/05 (API lê `agents/<id>/sessions/sessions.json` — antes Bad Gateway por CLI quebrado; 82 sessões <400ms; filtros tipo/agente/abortadas; presets período Hoje/7d/30d/Tudo; SessionDrawer paginado 50 msgs com user/assistant/thinking/tool_use/tool_result) |
| `/skills` Skills | ✅ PRD v1 fechado 14/05 (scan automático 4 dirs canônicos — antes dependia de `configured-skills.json` inexistente; 118 skills com dedup +N cópias; filtros tipo + 6 agentes; SkillDrawer com react-markdown + syntax highlight) |
| `/costs` Costs & Analytics | ✅ PRD v1 fechado 14/05 (separa custo real API vs subscription; pricing.ts: Anthropic=API real, GPT=subscription Pro 5x cobre; migration usage-tracking.db com billing_type/real_cost/equivalent_cost recalculou 4628 snapshots; budget só sobre API; 2 cards novos Subscription/Economia; AgentCostDrawer; histórico 6 meses) |
| Backend cron `activity-collector.py` | ✅ `*/5min` populando activities.db |
| Backend cron `system-metrics` | ✅ Snapshot 1/5s persistente em `system-metrics.db` 24h retention |
| n8n usage tracking | ⏳ Em aberto (retomar 15/05) — 3 workflows LLM mapeados em `trottingtuna-n8n.cloudfy.live`, plano 4 passos pronto |
| PRDs futuros | ⏳ 12 módulos: tasks, agents-detail, logs, terminal, git, workflows, search, analytics, reports, settings, calendar, about, actions |
| PRD futuro **"Minhas Aplicações"** | ⏳ cross-host (VPS + Vercel + Supabase + Railway) — unifica visão de todos os sistemas próprios independente de onde hospedados |
| Pendência menor | ⏳ KG sync Mac→VPS via cron rsync 1h (ativa busca semântica no /memory); filtro `/memory?agent=` por workspace; refinement regex `botToken` em auth-profiles.json |

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
