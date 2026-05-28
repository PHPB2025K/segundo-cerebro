---
title: "MEMORY"
created: 2026-04-14
type: memory-config
agent: fisco
status: active
tags:
  - agent/fisco
---

# MEMORY.md - Long-Term Memory

_Último update: 2026-05-27_

## Estado operacional recente
- 2026-05-27: Refresh OAuth do Bling manteve o padrão crítico pelo décimo terceiro dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada abortada por SIGTERM após bloqueio inicial e uma rodada bloqueada por política/allowlist sem validação útil. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-24: Refresh OAuth do Bling manteve o padrão crítico pelo décimo dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada bloqueada por allowlist/política de aprovação. Uma execução pós-consolidação anterior foi absorvida neste ciclo para não deixar lacuna. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-23: Refresh OAuth do Bling manteve o padrão crítico pelo nono dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de uma rodada bloqueada por allowlist/política de aprovação e sessão abortada após captura parcial do resultado. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-22: Refresh OAuth do Bling manteve o padrão crítico pelo oitavo dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de rodadas abortadas por timeout e bloqueadas por allowlist/política de execução. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-21: Refresh OAuth do Bling manteve o padrão crítico pelo sétimo dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de bloqueios iniciais por allowlist e sessões abortadas antes de resposta consolidada. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-20: Refresh OAuth do Bling manteve o padrão crítico pelo sexto dia: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403 e uma rodada abortada antes de resultado fiscal útil. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-19: Refresh OAuth do Bling manteve o padrão crítico: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa, alerta WhatsApp também com HTTP 403, além de bloqueios/abortos de automação. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- Bloqueio atual: qualquer fluxo dependente da Filial no Bling deve aguardar correção do token/status da empresa, validação de conectividade e estabilização da execução automática.

## Estrutura de memória
- `memory/sessions/YYYY-MM-DD.md` — diário operacional do Fisco.
- `memory/context/decisions.md` — decisões fiscais vigentes registradas pelo Fisco.
- `memory/context/lessons.md` — aprendizados e riscos operacionais.
- `memory/pending.md` — pendências próprias do Fisco.

## 2026-03-31
- Primeira conversa. Workspace "fisco". Escolhi o nome **Fisco**.
- Idioma preferido do usuário: português (BR).
