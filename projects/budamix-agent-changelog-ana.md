---
title: "budamix agent changelog ana"
created: 2026-04-14
type: project
status: active
tags:
  - project
---

# CHANGELOG — Agente Ana (WhatsApp)

## 2026-04-12 — Sprint Auditoria 7d (5 correções sistêmicas)

**Contexto:** Auditoria de 113 mensagens (06-09/abr) revelou taxa de erro de 61%.
3 problemas CRÍTICOS + 4 ALTOS + 2 MÉDIOS + 1 BAIXO.

### Problemas corrigidos: 10/10 da auditoria

| # | Problema | Severidade | Status |
|---|---------|-----------|--------|
| 1 | Loop perguntas repetitivas (Ellen Joyce) | CRITICO | CORRIGIDO |
| 2 | Vazamento "Nenhum produto foi carregado" | CRITICO | CORRIGIDO |
| 3 | Promessas indevidas (Edneuda — troca/reembolso) | CRITICO | CORRIGIDO |
| 4 | Reclamação sem escalação real | ALTO | CORRIGIDO |
| 5 | Loop mensagem vazia (7 tentativas) | ALTO | CORRIGIDO |
| 6 | Áudio não transcrito | ALTO | CORRIGIDO |
| 7 | Cupom BEMVINDO10 para cliente existente | MEDIO | CORRIGIDO |
| 8 | Resposta duplicada (debounce) | MEDIO | CORRIGIDO |
| 9 | "Fita" não abordada (produto fora catálogo) | BAIXO | CORRIGIDO |
| 10 | Produtos nunca carregados (pipeline) | ALTO | CORRIGIDO |

### Arquivos modificados

| Arquivo | Tipo de mudança |
|---------|----------------|
| `supabase/functions/_shared/context-builder.ts` | Carry-over 0.2, regex expandido, fallback legacy |
| `supabase/functions/_shared/response-generator.ts` | Instrução no-products, regra reativa anti-loop |
| `supabase/functions/_shared/response-validator.ts` | 6 novos patterns anti-vazamento |
| `supabase/functions/process-message/index.ts` | Anti-loop, post-response escalation, áudio fallback |
| `n8n/workflow-principal.json` | Debounce 8s → 12s |
| `CLAUDE.md` | Seção 31 documentando todas as correções |
| `agent_config (Supabase DB)` | Regras 16-18 no prompt, debounce 12s |

### Deploy — EXECUTADO 2026-04-13 01:02 UTC

| Componente | Status | Timestamp |
|-----------|--------|-----------|
| `process-message` (Edge Function) | ACTIVE | 2026-04-13 01:02:14 UTC |
| N8N Workflow Principal (KE7YVXayl5ntjwQk) | ACTIVE, debounce=12s | 2026-04-13 01:03:12 UTC |
| `agent_config` (DB) | Regras 16-18 + debounce 12s | 2026-04-12 (sessão anterior) |

### Smoke Tests — 4/4 PASSED

| # | Teste | Resultado |
|---|-------|----------|
| 1 | Busca "potes herméticos" | Resposta com "potes de vidro hermético", sem vazamento |
| 2 | Carry-over "Sim, quero ver os kits" | Ana reconheceu contexto de potes/kits |
| 3 | Anti-vazamento "Ambos" | 3 produtos reais com preços (Kit 5 Potes R$24,90), ZERO debug |
| 4 | Escalação "tampa com borracha diferente" | Ana respondeu sem promessas proibidas, `escalated=true`, registro criado em `escalations` |

### Monitoramento pós-deploy

- Verificar busca semântica: "potes herméticos" deve retornar 5+ produtos
- Verificar escalação: reclamação com nro pedido → `escalations` deve ter registro
- Verificar anti-loop: 2+ "[Mensagem sem texto]" → auto-escalação
- Verificar áudio: arquivo .ogg deve ser transcrito via Groq
- **Próxima auditoria: 19/abr/2026** — meta: taxa de erro < 20%
