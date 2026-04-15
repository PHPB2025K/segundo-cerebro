---
title: Claude Code Skills — Auditoria de Segurança 2026-04-14
created: 2026-04-14
type: reference
status: active
tags: [knowledge, tools, audit, security]
---

# Claude Code Skills — Auditoria de Segurança 2026-04-14

Data da auditoria: **2026-04-14**
Auditor: Pedro Broglio + Claude Code

---

## Tier 1 — ui-skills

**Repositório:** `nichochar/ui-skills`
**Classificação:** SEGURO
**Skills:** baseline-ui, fixing-accessibility, fixing-motion-performance, fixing-metadata

Todas as 4 skills são SKILL.md de markdown puro. Sem execução de código, sem chamadas externas, sem side effects.

**Atenção no instalador:** O método oficial (`npx ui-skills`) usa `curl | sh` com telemetria. **NÃO foi usado.** As skills foram copiadas diretamente dos arquivos SKILL.md do repositório.

---

## Tier 2 — Vercel Labs (agent-skills)

**Repositório:** `vercel-labs/agent-skills`
**Skills:** composition-patterns, react-best-practices, web-design-guidelines

### composition-patterns
**Classificação:** SEGURO — markdown puro, patterns de composição React.

### react-best-practices
**Classificação:** SEGURO — markdown puro, guidelines de performance React/Next.js da Vercel Engineering.

### web-design-guidelines
**Classificação:** ATENCAO — versão original continha instrução de `WebFetch` para buscar guidelines remotas em runtime. **Sanitizado:** referência ao WebFetch removida, conteúdo convertido para local. Sem chamadas externas.

---

## Tier 3 — Medusa (storefront-best-practices)

**Repositório:** `medusajs`
**Classificação:** SEGURO
**Skills:** storefront-best-practices

Markdown puro, sem execução de código. Best practices para storefronts e-commerce baseadas na stack Medusa.

---

## Tier 4 — designer-skills (Owl-Listener)

**Repositório:** `Owl-Listener/designer-skills`
**Classificação:** SEGURO
**Skills:** 63 skills em `~/.claude/skills/designer/`

63 skills especializadas em design. Todas são SKILL.md markdown puro. Sem hooks, sem execução de código, sem side effects.

**Exemplos de skills incluídas:** color-theory, typography, grid-systems, brand-identity, motion-design, icon-design, data-visualization, etc.

---

## Tier 4b — designpowers (Owl-Listener)

**Repositório:** `Owl-Listener/designpowers`
**Classificação:** ATENCAO
**Skills:** 29 skills em `~/.claude/skills/designpowers/`

**Risco identificado:** O repositório original inclui hooks que auto-injetam contexto em TODA sessão do Claude Code via `EXTREMELY_IMPORTANT` no CLAUDE.md. Esse mecanismo forçaria o carregamento automático das skills sem invocação explícita.

**Mitigação aplicada:** Instalado **SEM os hooks**. Apenas as skills individuais foram copiadas. O CLAUDE.md do repositório original não foi incluído. As skills só são ativadas quando explicitamente invocadas com `/skill-name`.

---

## Tier 5 — Stripe (jezweb/claude-skills)

**Repositório:** `jezweb/claude-skills`
**Classificação:** SEGURO
**Skills:** stripe-payments

Skill para integração Stripe (Checkout Sessions, Payment Intents, subscriptions, webhooks). Chaves Stripe gerenciadas via variáveis de ambiente — sem hardcode.

**Atenção no repositório:** O repo original contém `brains-trust.py`, um script que envia arquivos do projeto para Gemini/OpenRouter para análise. **NÃO instalado.** Apenas a skill stripe-payments foi copiada.

---

## Resumo de Riscos

| Item | Risco | Status |
|------|-------|--------|
| ui-skills installer (npx) | curl\|sh + telemetria | Não usado — copiado direto |
| web-design-guidelines WebFetch | Chamada remota em runtime | Sanitizado |
| designpowers hooks EXTREMELY_IMPORTANT | Auto-injeção em toda sessão | Hooks não instalados |
| jezweb brains-trust.py | Exfiltração de arquivos para LLM externo | Não instalado |

---

## Links Relacionados

- [[knowledge/concepts/claude-code-skills-inventario]]
- [[knowledge/concepts/claude-code-skills-guia-uso]]
