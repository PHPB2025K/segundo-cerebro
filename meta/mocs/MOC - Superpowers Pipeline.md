---
title: "MOC   Superpowers Pipeline"
created: 2026-04-14
type: moc
status: active
tags:
  - moc
---

# MOC — Superpowers Pipeline

> Mapa das 14 skills de desenvolvimento que formam um pipeline linear completo.

---

## Pipeline principal (sequencial)

```
1. Brainstorming (design antes de codigo)
   ↓
2. Writing Plans (plano bite-sized)
   ↓
3a. Subagent-Driven Development (paralelo, double review)
3b. Executing Plans (sequencial, human-in-loop)
   ↓
4. Requesting Code Review (dispatch reviewer)
   ↓
5. Receiving Code Review (avaliar feedback)
   ↓
6. Finishing a Development Branch (merge/PR)
```

| Etapa | Skill | Entrada | Saida |
|-------|-------|---------|-------|
| 1 | [[skills/superpowers/brainstorming/SKILL|brainstorming]] | Pedido do usuario | Spec aprovada |
| 2 | [[skills/superpowers/writing-plans/SKILL|writing-plans]] | Spec | Plano em docs/superpowers/plans/ |
| 3a | [[skills/superpowers/subagent-driven-development/SKILL|subagent-driven-development]] | Plano | Codigo implementado |
| 3b | [[skills/superpowers/executing-plans/SKILL|executing-plans]] | Plano | Codigo implementado |
| 4 | [[skills/superpowers/requesting-code-review/SKILL|requesting-code-review]] | Codigo | Review dispatch |
| 5 | [[skills/superpowers/receiving-code-review/SKILL|receiving-code-review]] | Feedback | Correcoes aplicadas |
| 6 | [[skills/superpowers/finishing-a-development-branch/SKILL|finishing-a-development-branch]] | Branch pronta | Merge/PR |

## Skills laterais (usadas em qualquer etapa)

| Skill | Quando usar |
|-------|------------|
| [[skills/superpowers/systematic-debugging/SKILL|systematic-debugging]] | Bug encontrado durante implementacao |
| [[skills/superpowers/verification-before-completion/SKILL|verification-before-completion]] | Antes de declarar qualquer tarefa completa |
| [[skills/superpowers/test-driven-development/SKILL|test-driven-development]] | Durante implementacao (Red-Green-Refactor) |
| [[skills/superpowers/dispatching-parallel-agents/SKILL|dispatching-parallel-agents]] | Problemas independentes paralelizaveis |
| [[skills/superpowers/using-git-worktrees/SKILL|using-git-worktrees]] | Antes de iniciar implementacao isolada |

## Meta-skills

| Skill | Proposito |
|-------|----------|
| [[skills/superpowers/using-superpowers/SKILL|using-superpowers]] | Orquestra todos os outros; prioridade maxima |
| [[skills/superpowers/writing-skills/SKILL|writing-skills]] | TDD aplicado a criacao de novas skills |

---

*Criado: 10/04/2026 — Auditoria de conexoes*
