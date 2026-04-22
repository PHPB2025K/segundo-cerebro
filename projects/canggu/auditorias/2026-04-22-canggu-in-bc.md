---
tipo: auditoria
projeto: Canggu
status: concluida
resultado: nulo
tags:
  - canggu
  - auditoria
  - 2026-04
data: 2026-04-22
auditor: Claude Code (Opus 4.7 1M)
---

# Auditoria Canggu-in-BC — 2026-04-22

## Contexto

Auditoria anterior à [[2026-04-22-forense]], **pivotada a meio caminho**.

**Hipótese original:** "O Canggu criou objetos no Supabase do Budamix
Central (BC, project `sqbkoprcmnznmzbwdrmf`) por conveniência operacional
— mapear esses objetos pra eventual separação."

## Resultado

**Nulo.** Zero sinais de Canggu no Supabase do BC.

Todas as **11 heurísticas** de detecção retornaram vazio:
- Tabelas com nome Canggu-ish (`conversations`, `messages`, `contacts`, etc.)
- Tabelas com colunas Canggu-style (`whatsapp_number`, `wa_id`, `ai_generated`, etc.)
- Functions PL/pgSQL com nome/corpo mencionando Evolution/OpenAI/Anthropic/n8n/whatsapp/webhook
- Edge functions Canggu
- Edge secrets Canggu-related
- Auth metadata com hints WhatsApp
- DB webhooks (`supabase_functions.hooks` — schema nem existe no BC)
- Cron jobs
- Referência ao project ref Canggu (`jpacmloqsfiebvagfomt`) no código BC
- Strings Evolution/WhatsApp/conversation/message no código BC
- Rotas de chat no app BC

**Conclusão:** os dois sistemas já estavam 100% separados. Não havia nada
para migrar ou remover. Hipótese original descartada.

## Pivot

Com o resultado nulo, pivotamos para a auditoria forense do próprio
Canggu — [[2026-04-22-forense]] — que passou a ser a auditoria de verdade.

## Achado lateral (fora de escopo, registrado)

O Supabase do BC (`sqbkoprcmnznmzbwdrmf`) tem **0 foreign keys** em 11
tabelas com ~2.4 GB de dados (vs 11 FKs no Canggu — [[supabase-canggu]]).
Débito estrutural do BC, não relacionado ao Canggu. Endereçável em
refactoring futuro do Budamix Central, não deste projeto.

## Artefatos

- **Dumps:** `~/audit-canggu-in-bc/RAW/` — 29 arquivos, 456 KB
- **Context file:** `~/audit-canggu-in-bc/00_context.md`
- (Nenhum `NOTE.md` commitado no repo BC — regra read-only mantida)

## Stack das heurísticas

Para referência (caso hipótese similar apareça no futuro em outro projeto):

| # | Heurística | Implementação |
|---|---|---|
| 1 | Tabela com nome Canggu-ish | grep em `information_schema.tables` com regex |
| 2 | Coluna Canggu-style | grep em `information_schema.columns` |
| 3 | PL/pgSQL body com WhatsApp/Evolution/LLM refs | `pg_get_functiondef` + ILIKE |
| 4 | Edge functions com nome Canggu | Management API `/functions` |
| 5 | Edge secrets Canggu | `supabase secrets list` |
| 6 | auth.users metadata keys | `jsonb_object_keys(raw_user_meta_data)` |
| 7 | DB webhooks (`supabase_functions.hooks`) | check if schema/table existe |
| 8 | Cron jobs Canggu-like | `cron.job` se pg_cron instalado |
| 9 | Project ref cross-reference no código | `grep` no monorepo BC |
| 10 | Strings Canggu no código | `grep -E "evolution|whatsapp|conversation|message"` |
| 11 | Rotas de chat no app | `find src/app` por pattern |

Todas verificáveis em ~5 queries SQL + 2 SSH greps.

## Relação com auditoria principal

Este resultado desbloqueou o pivô para [[2026-04-22-forense]], que é a
auditoria operacional do Canggu propriamente dito.
