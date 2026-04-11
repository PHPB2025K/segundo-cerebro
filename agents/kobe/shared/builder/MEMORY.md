# MEMORY.md — Índice de Memória do Builder

> Agente: [[agents/builder/IDENTITY|Builder]] | Orquestrador: [[agents/kobe/AGENTS|Kobe Team]]

_Último update: 2026-03-24._

---

## Índice de arquivos

- [[agents/kobe/shared/builder/SOUL|SOUL]]
- [[agents/kobe/shared/builder/memory/decisions|Decisões]]
- [[agents/kobe/shared/builder/memory/lessons|Lições]]
- [[agents/kobe/shared/builder/memory/pending|Pendências]]

### Sessões
- [[agents/kobe/shared/builder/memory/sessions/2026-03-24|Sessão 2026-03-24]]
- [[agents/kobe/shared/builder/memory/sessions/2026-03-26|Sessão 2026-03-26]]
- [[agents/kobe/shared/builder/memory/sessions/2026-03-27|Sessão 2026-03-27]]
- [[agents/kobe/shared/builder/memory/sessions/2026-03-29|Sessão 2026-03-29]]
- [[agents/kobe/shared/builder/memory/sessions/2026-03-30|Sessão 2026-03-30]]
- [[agents/kobe/shared/builder/memory/sessions/2026-04-05|Sessão 2026-04-05]]
- [[agents/kobe/shared/builder/memory/sessions/2026-04-06|Sessão 2026-04-06]]
- [[agents/kobe/shared/builder/memory/sessions/2026-04-07|Sessão 2026-04-07]]
- [[agents/kobe/shared/builder/memory/sessions/2026-04-08|Sessão 2026-04-08]]
- [[agents/kobe/shared/builder/memory/sessions/2026-04-09|Sessão 2026-04-09]]

---

## Estrutura

```
shared/builder/
├── MEMORY.md                  ← Este arquivo (índice + skills + stack)
├── decisions.md               ← Decisões permanentes
├── lessons.md                 ← Erros e aprendizados
└── stack.md                   ← Stack técnico e padrões
```

---

## Skills de Design/Frontend (OBRIGATÓRIO em todo projeto com UI)

| Skill | Path | Quando usar |
|-------|------|-------------|
| **lovable-quality** ⭐ | `skills/design/lovable-quality/SKILL.md` | Regras obrigatórias de qualidade visual. Design system first (globals.css + tailwind.config.ts com tokens semânticos). Sem cores hardcoded. CVA obrigatório. A MAIS IMPORTANTE. |
| **superdesign** | `skills/design/superdesign/SKILL.md` | Workflow de design moderno: layout, tema, animações, implementação. |
| **frontend-design-ultimate** | `skills/design/frontend-design-ultimate/SKILL.md` | Estéticas anti-genéricas. Next.js + shadcn + Framer Motion. Mobile-first. |
| **shadcn-ui** | `skills/design/shadcn-ui/SKILL.md` | Patterns avançados shadcn/ui: forms com zod, theming, dark mode, sidebar, data tables, command palette. |
| **report-design-system** | `skills/design/report-design-system/SKILL.md` | Design system dark mode para relatórios HTML (não para webapps). |
| **excel-design-system** | `skills/design/excel-design-system.md` | Paleta dark mode para planilhas Excel. |

### Regras obrigatórias para briefings de frontend:
1. Usar `templates/BRIEFING-TEMPLATE.md` como base estrutural
2. Referenciar as 4 skills de design como leitura obrigatória (lovable-quality + superdesign + frontend-design-ultimate + shadcn-ui)
3. Incluir dados mock realistas (nunca "Lorem ipsum" ou "Campanha 1")
4. Especificar tom visual, paleta como tokens semânticos e referências visuais
5. Incluir checklist de qualidade do lovable-quality na seção de entregáveis
6. Design system first: globals.css + tailwind.config.ts com tokens ANTES de componentes

---

## Skills de Marketplace (referência, não executa diretamente)

| Skill | Path |
|-------|------|
| marketplace-report | `skills/marketplace/marketplace-report/SKILL.md` |
| consolidado-financeiro | `skills/marketplace/consolidado-financeiro/SKILL.md` |
| ml-ads | `skills/marketplace/ml-ads/SKILL.md` |

---

## Stack Padrão

| Camada | Tecnologia |
|--------|-----------|
| Framework | Next.js 15 (App Router) |
| UI | shadcn/ui + Tailwind CSS |
| Animações | Framer Motion |
| Auth | Supabase Auth |
| DB | Supabase (Postgres) + Drizzle ORM |
| Deploy | Vercel (preferido) ou VPS |
| Package manager | pnpm |
| Node | v22.x |
| Python | 3.12 (quando necessário) |

---

## Projetos Ativos

| Projeto | Repo | Status |
|---------|------|--------|
| Spark Ads | PHPB2025K/spark-ads | v2.0 + API integration entregue 24/03, Edge Function deployada, pendente pg_cron + repo GitHub |
| Budamix Central | — (pendente criar repo) | MVP completo 24/03, 57 arquivos, PM2 + Traefik online, pendente DNS + pg_cron |
| Marketplace Report Connectors | — | Amazon + Shopee connectors reescritos 24/03, Seções 4-5 multi-plataforma |
| SimulImport | PHPB2025K/simulimport | Em pausa |
| Bidspark | PHPB2025K/amazon-ads-automation + ml-ads-automation | Em pausa, validação pendente |
| Canguu | — | Em pausa |
| Atlas Finance | — | Em pausa |

---

## Regras de Qualidade

1. Output visual deve ter qualidade de produção, não de template genérico
2. Sempre consultar skills de design antes de implementar UI
3. Mobile-first obrigatório
4. Dark mode como padrão
5. Sem dependências desnecessárias
6. Testes mínimos antes de entregar
7. Tratar erros gracefully — nunca crashar
