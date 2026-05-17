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

_Último update: 2026-05-16_

## Estado operacional recente
- 2026-05-16: Refresh OAuth do Bling repetiu o padrão crítico em todas as execuções observadas: Matriz OK, Filial com HTTP 403 por empresa vinculada ao token inativa, e alerta WhatsApp também com HTTP 403. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- 2026-05-15: Refresh OAuth do Bling apresentou falha recorrente na Filial (HTTP 403, empresa vinculada ao token inativa). Matriz renovou/conectou nas execuções completas. Sem NF-e emitida, sem drafts, sem distribuição, sem conciliação e sem novo monitor Simples.
- Bloqueio atual: qualquer fluxo dependente da Filial no Bling deve aguardar correção do token/status da empresa e validação de conectividade.

## Estrutura de memória
- `memory/sessions/YYYY-MM-DD.md` — diário operacional do Fisco.
- `memory/context/decisions.md` — decisões fiscais vigentes registradas pelo Fisco.
- `memory/context/lessons.md` — aprendizados e riscos operacionais.
- `memory/pending.md` — pendências próprias do Fisco.

## 2026-03-31
- Primeira conversa. Workspace "fisco". Escolhi o nome **Fisco**.
- Idioma preferido do usuário: português (BR).
