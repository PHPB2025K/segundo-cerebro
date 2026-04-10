# Lições Aprendidas — Builder

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
