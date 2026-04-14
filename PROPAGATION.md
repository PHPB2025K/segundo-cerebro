---
title: "Propagação de Dados — Protocolo Único"
created: 2026-04-06
modified: 2026-04-14
type: meta
status: active
tags:
  - meta
  - protocolo
---

# Propagação de Dados — Protocolo Único

> Fonte de verdade sobre o que atualizar quando algo muda no vault.
> Lido pelo Claude Code durante sessões e pelo /salve no fim de cada sessão.
> Quando a regra mudar, mude AQUI.

---

## Regra geral

**Toda ação que mude o estado de algo deve atualizar o arquivo correspondente no momento em que acontecer.** O /salve é o safety net — não o método principal.

---

## Tabela de Propagação

| Evento | Atualizar | O que escrever |
|--------|-----------|----------------|
| **Pendência criada ou resolvida** | `memory/context/pendencias.md` | Adicionar ou mover pra ✅ Resolvidas |
| **Decisão tomada** | `memory/context/decisoes/YYYY-MM.md` | Data, contexto, owner, status |
| | `memory/context/business-context.md` | SE mudou deal, equipe ou foco |
| **Pessoa nova ou role mudou** | `memory/context/people.md` | Adicionar ou atualizar entry |
| | `memory/context/business-context.md` | SE é equipe principal |
| **Projeto novo** | `projects/{nome}.md` | Criar com template (ver abaixo) |
| | `projects/_index.md` | Adicionar na tabela |
| | `memory/context/business-context.md` | SE é negócio principal |
| **Projeto mudou de status** | `projects/{nome}.md` | Atualizar status no frontmatter + corpo |
| | `projects/_index.md` | Atualizar status na tabela |
| **Métrica atualizada** | `projects/{nome}.md` | Atualizar tabela de métricas |
| | `memory/context/business-context.md` | SE é métrica-chave |
| **Deadline novo ou concluído** | `memory/context/deadlines.md` | Adicionar ou mover pra concluídos |
| **Skill criada ou alterada** | `skills/[domínio]/[nome]/SKILL.md` | Atualizar conteúdo |
| | CLAUDE.md do projeto (se aplicável) | Referenciar a skill |
| **Mudança em agente OpenClaw** | `openclaw/agents/[agente]/IDENTITY.md` | Atualizar config/regras |
| | `memory/context/business-context.md` | SE mudou infra AI |
| **Arquivo de Documents/ mudou** | `business/[área]/_index.md` | Atualizar tabela de arquivos-chave |
| **Nota de conhecimento criada** | `knowledge/[subpasta]/[nota].md` | Criar com frontmatter |
| **Automação criada ou alterada** | `automacoes/[subpasta]/[nota].md` | Atualizar conteúdo |
| **Ideia registrada** | arquivo adequado (knowledge/, memory/) | Adicionar com data |

---

## Fontes de Verdade

| Dado | Fonte principal | Cache/overview |
|------|-----------------|----------------|
| Status de projeto | `projects/{nome}.md` | `projects/_index.md`, `business-context.md` |
| Decisões | `memory/context/decisoes/YYYY-MM.md` | `business-context.md` |
| Pessoas/equipe | `memory/context/people.md` | `business-context.md` |
| Pendências | `memory/context/pendencias.md` | — |
| Deadlines | `memory/context/deadlines.md` | — |
| Skills | `skills/[domínio]/[nome]/SKILL.md` | CLAUDE.md (mapa geral) |
| Agentes OpenClaw | `openclaw/agents/[agente]/IDENTITY.md` | CLAUDE.md (aliases) |
| Arquivos Documents/ | `business/[área]/_index.md` | — |
| Panorama geral | `memory/context/business-context.md` | (cache compilado) |

`business-context.md` é um **cache compilado**. Em caso de conflito, as fontes individuais prevalecem.

---

## Template — Nova Ficha de Projeto

```markdown
---
title: "[Nome do Projeto]"
created: YYYY-MM-DD
type: project
status: active
path: "~/Documents/05-Projetos-Codigo/[nome]/"
tags:
  - project
  - dev
---

# [Nome do Projeto]

**Path:** `~/Documents/05-Projetos-Codigo/[nome]/`
**Branch:** main
**Stack:** [Next.js/Python/etc]
**Deploy:** [Vercel/VPS/etc]

## O que é

[1-2 frases]

## Decisões-chave

- [YYYY-MM-DD] [decisão]

## Pendências

- [ ] [próxima ação]

## Notas relacionadas

- [[links relevantes]]
```

---

## Índices do Vault

### MOCs (Maps of Content)
- [[meta/mocs/MOC - Token Management|Token Management]]
- [[meta/mocs/MOC - Extratos Financeiros|Extratos Financeiros]]
- [[meta/mocs/MOC - Superpowers Pipeline|Superpowers Pipeline]]
- [[meta/mocs/MOC - Taxas e Precificacao|Taxas e Precificação]]
- [[meta/mocs/MOC - Design Systems Budamix|Design Systems]]
- [[meta/mocs/MOC - Supabase Ecosystem|Supabase Ecosystem]]
- [[meta/mocs/MOC - Governanca OpenClaw|Governança OpenClaw]]
- [[meta/mocs/MOC - Listing Pipeline|Listing Pipeline]]

### Índices de Negócio (Documents/)
- [[business/importacao/_index|Importação]] — 471 arquivos
- [[business/marketplaces/_index|Marketplaces]] — 56 arquivos
- [[business/financeiro/_index|Financeiro]] — 112 arquivos
- [[business/empresa/_index|Empresa]] — 124 arquivos
- [[business/marketing/_index|Marketing]] — 20 arquivos

### Projetos
- [[projects/_index|Índice de Projetos]] — todas as fichas

### Auditorias
- [[meta/audits/auditoria-conexoes-2026-04-10]]

---

*Atualizado: 2026-04-14*
