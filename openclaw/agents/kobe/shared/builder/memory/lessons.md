---
title: "lessons"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Lições Aprendidas — [[openclaw/agents/builder/IDENTITY|Builder]]

_Erros e aprendizados. [ESTRATÉGICA] = permanente | [TÁTICA] = expira em 30 dias._

---

### [ESTRATÉGICA] Briefing sem design system = output amador (2026-03-24)
**Lição:** Todo briefing de frontend DEVE referenciar BRIEFING-TEMPLATE.md + 4 skills de design (lovable-quality, superdesign, frontend-design-ultimate, shadcn-ui).

### [ESTRATÉGICA] Job "failed" pode ter entregado — verificar RESULT.md (2026-03-24)
**Lição:** Exit code ≠ resultado. SEMPRE verificar workspace/RESULT.md mesmo em jobs "failed".

### [ESTRATÉGICA] Bugs complexos de estado React → resolver direto, não via Builder (2026-03-27)
**Lição:** Builder via `claude -p` não debuga bugs de estado React com múltiplas interações. Resolver no Claude Code interativo.

### [ESTRATÉGICA] Deploy/preview: SEMPRE via Traefik HTTPS (2026-04-01)
**Lição:** Subdomínio `*.srv1480018.hstgr.cloud` via Traefik. Nunca portas custom. Nunca HTTP puro.

### [ESTRATÉGICA] Máximo 2 Builder jobs simultâneos no VPS (2026-03-30)
**Lição:** VPS 3.8GB RAM. 4 jobs = OOM killer. Disparar em lotes de 2.

### [ESTRATÉGICA] Supabase upsert on_conflict: parâmetro condicional por tabela (2026-04-02)
**Lição:** Tabelas com unique constraints (`products`) precisam de `on_conflict`. Tabelas de log (`price_history`) NÃO usam on_conflict. Tornar parâmetro opcional em funções genéricas de upsert.

### [TÁTICA] NODE_OPTIONS obrigatório para Next.js build no VPS (2026-03-25)
**Lição:** Sempre usar `NODE_OPTIONS="--max-old-space-size=2048"` antes de build.
**Expira:** 2026-04-25

---

_Atualizado na Consolidação Profunda 2026-04-04._

### [ESTRATÉGICA] UI longa deve acompanhar job/status persistido, não webhook síncrono (2026-04-28)
**Lição:** Para Admin Blog/Social Studio e qualquer geração assíncrona, criar job, persistir status e reconciliar pelo banco. Timeout HTTP não é prova de falha.

### [TÁTICA] Preview Vercel CLI precisa envs públicas explícitas (2026-04-28)
**Lição:** Deploy preview do Budamix E-commerce pela CLI pode buildar sem `VITE_SUPABASE_URL`/`VITE_SUPABASE_PUBLISHABLE_KEY`; passar envs ou configurar Preview Environment.
**Expira:** 2026-05-28

### [ESTRATÉGICA] Supabase db push amplo é perigoso com histórico remoto desalinhado (2026-04-28)
**Lição:** Aplicar migrations específicas com backup/smoke quando o histórico remoto não está marcado; não empurrar migrations antigas sem auditoria.

### [ESTRATÉGICA] Confirmar repo/deploy real antes de corrigir UI (2026-04-30)
**Lição:** Antes de corrigir bug visual/admin, confirmar qual repo está ligado ao domínio/projeto Vercel/Lovable real. Em Canggu, editar `budamix-ai-agent` não alterava o admin visto pela Yasmin porque o deploy real vinha de `canguu`.

### [TÁTICA] Parser BR em sync financeiro/estoque exige validação de somatório (2026-04-30)
**Lição:** Em planilhas brasileiras, ponto costuma ser milhar. Validar parse contra colunas calculadas antes de publicar KPI financeiro.
**Expira:** 2026-05-30
