---
tipo: debitos
projeto: Canggu
status: ativo
tags:
  - canggu
  - refatoracao
  - roadmap
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Débitos Técnicos e Roadmap

> Matriz de 24 achados priorizados + 6 blocos de refatoração. Input direto do roadmap.
> Detalhes completos em `~/audit-canggu-forensics/AUDIT_REPORT.md`.

## Legenda

- **Impacto 1–5:** 1=cosmético, 5=catastrófico
- **Esforço:** S (<1d), M (1–3d), L (1–2sem), XL (>2sem)
- **Severidade:** 🔴 crítico · 🟡 alto · 🟢 médio/baixo

## Matriz dos 24 achados

| # | Achado | Sev | Imp | Esf | Bloco | Depende de |
|---|---|:-:|:-:|:-:|:-:|:-:|
| 1 | service_role JWT hardcoded em 3 arquivos tracked | 🔴 | 5 | M | B1 | [[decisoes#ADR-001]] |
| 2 | Edge function `test-search` ghost deployed | 🔴 | 4 | S | B1 | [[decisoes#ADR-003]] |
| 3 | Zero alertas/monitoria ativa | 🔴 | 5 | M | B2 | [[decisoes#ADR-005]] |
| 4 | Zero fallback Anthropic/OpenAI/Groq | 🟡 | 4 | M | B3 | B2 ideal |
| 5 | Zero testes num pipeline de 9 etapas | 🟡 | 4 | L | B5 | — |
| 6 | Drift N8N (2 workflows estrutural, 3 active) | 🟡 | 3 | S | B5 | [[decisoes#ADR-005]] |
| 7 | `--no-verify-jwt` global em 14 edge fns | 🟡 | 4 | M | B1 | #1, #2 |
| 8 | Deploy parcial (5/13 functions) | 🟡 | 3 | S | B5 | — |
| 9 | Triggers pg_net falham silenciosas | 🟡 | 4 | M | B2 | — |
| 10 | `whatsapp_message_id` sem UNIQUE | 🟡 | 3 | S | B3 | — |
| 11 | Pipeline WhatsApp duplicado (N8N + edge fn) | 🟡 | 3 | L | B4 | [[decisoes#ADR-007]] ✅ |
| 12 | Divergência searchProducts vs searchProductsEnriched | 🟡 | 3 | M | B4 | [[decisoes#ADR-006]] |
| 13 | `buildSearchText` duplicado | 🟢 | 2 | S | B4 | — |
| 14 | send-human-message `success:true, sent:false` | 🟡 | 3 | S | B3 | — |
| 15 | Áudio sem alerta ao operador | 🟢 | 2 | S | B2 | — |
| 16 | CORS `*` global em edge fns autenticadas | 🟢 | 2 | S | B1 | #7 |
| 17 | `products_backup_20260404` órfã (4 MB) | 🟢 | 1 | S | B6 | — |
| 18 | `LOVABLE_API_KEY` edge secret órfão | 🟢 | 1 | S | B1 | [[decisoes#ADR-002]] |
| 19 | `marketplace_chats*` sem migration criadora | 🟢 | 2 | S | B6 | [[decisoes#ADR-004]] ✅ |
| 20 | `test-semantic-search` órfã funcional | 🟢 | 1 | S | B6 | [[decisoes#ADR-003]] |
| 21 | Working copy dirty em produção | 🟡 | 3 | M | B5 | — |
| 22 | Sem CI/CD (GitHub Actions ausente) | 🟢 | 2 | L | B5 | — |
| 23 | Sem validação de schema (zod) em edge fns | 🟢 | 2 | M | B5/B6 | — |
| 24 | Drift estrutural não auditado (colunas vs ALTER) | 🟢 | 2 | M | B5 | — |

## Blocos

### B1 — Segurança (crítico + primeiro)
**Achados:** #1, #2, #7, #16, #18
**Esforço:** M (5–7 dias)
**Pré-req:** [[decisoes#ADR-001]] ✅, [[decisoes#ADR-002]] ✅, [[decisoes#ADR-003]] ✅
**Objetivo:** Eliminar service_role hardcoded + deletar ghost + verify_jwt interno + CORS restrito + remover secret legado.
**Passos 1–14:** detalhados em `~/audit-canggu-forensics/AUDIT_REPORT.md` §6/B1.
**DoD:**
- [ ] `git grep -nIE 'eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{20,}'` retorna zero linhas
- [ ] `test-search` não existe mais (`curl .../functions | jq` sem ele)
- [ ] Insert produto novo dispara embedding em ≤30s (validação do trigger com key nova)
- [ ] `curl -X POST .../functions/v1/process-message` sem Authorization retorna 401
- [ ] `LOVABLE_API_KEY` não existe em secrets
- [ ] Runbook em `docs/runbooks/rotate-service-role.md`

### B2 — Observabilidade
**Achados:** #3, #9, #15
**Esforço:** M (3–5 dias)
**Pré-req:** [[decisoes#ADR-005]] ✅ (Slack como canal)
**Objetivo:** Sair de zero alertas → detecção ativa em todos os pontos críticos.
**Passos principais:**
1. Redesenhar Health Check N8N (11 nodes originais → nova versão com Slack webhook)
2. Cron job `SELECT count(*) FROM products WHERE embedding IS NULL AND created_at > now() - interval '7 days'` + alert Slack se >0
3. ALTER TABLE [[supabase-canggu|messages]] ADD COLUMN needs_review boolean DEFAULT false
4. webhook-whatsapp: ao falhar transcrição áudio → marcar needs_review=true + Slack alert
5. Rota `/operations` no frontend com 3 widgets
6. Runbooks em `docs/runbooks/on-alert-*.md` (5 runbooks curtos)

**DoD:**
- [ ] Simular disconnect Evolution → alerta Slack em ≤30 min
- [ ] `cron.job` count ≥1
- [ ] Coluna `messages.needs_review` existe
- [ ] 5 runbooks em `docs/runbooks/`

### B3 — Resiliência
**Achados:** #4, #10, #14
**Esforço:** M (3–5 dias)
**Pré-req:** B2 ideal (pra validar via alertas), mas não bloqueia
**Objetivo:** Parar de silenciar falhas upstream.
**Passos principais:**
1. Wrapper `withRetry` em `classifyIntent` + `generateResponse` (max 2 tentativas, backoff exp)
2. Se falha final, process-message retorna success:false + N8N/webhook-whatsapp envia fallback textual ("Recebi sua mensagem! Tive um problema técnico, volto em instantes.")
3. Query de detecção duplicatas: `SELECT whatsapp_message_id, count(*) FROM messages GROUP BY 1 HAVING count(*)>1`
4. Migration: cleanup duplicatas + `CREATE UNIQUE INDEX CONCURRENTLY idx_messages_wa_unique ON messages(whatsapp_message_id) WHERE whatsapp_message_id IS NOT NULL`
5. [[edge-functions|webhook-whatsapp]] e N8N node "Save Message" → `INSERT ... ON CONFLICT DO NOTHING`
6. `send-human-message` retorna `{success:false, error:'evolution_send_failed'}` quando Evolution falha; frontend mostra toast

**DoD:**
- [ ] Mock de Anthropic 500 → process-message tenta 2× e retorna success:false
- [ ] Fallback textual chega ao cliente em caso de falha final
- [ ] Zero duplicatas em messages por whatsapp_message_id
- [ ] UNIQUE index existe
- [ ] Frontend mostra toast de erro em send-human-message fail

### B4 — Arquitetura
**Achados:** #11, #12, #13
**Esforço:** L (1–2 semanas)
**Pré-req:** [[decisoes#ADR-007]] ✅ (edge fn canônica) + [[perguntas-abertas#ADR-006]] (portar ML?)
**Objetivo:** Consolidar pipeline WhatsApp + unificar search layers entre WhatsApp e ML + deduplicar `buildSearchText`.
**Plano (ADR-007 já decidiu (a) edge function canônica):**
1. Confirmar `webhook-whatsapp` no deploy com versão atual
2. Feature-completeness: revisar se edge fn cobre 100% do que N8N faz (debounce, escalation, group filter)
3. Staging: duplicar project em feature branch, apontar Evolution de staging pra webhook-whatsapp → testes manuais
4. Cutover produção: trocar Evolution webhook URL pra `/functions/v1/webhook-whatsapp`; manter N8N em "catch-fallback" 24h
5. Desabilitar workflow N8N Principal após 24h sem issues
6. [Se ADR-006 = portar]: editar [[edge-functions|process-ml-question]]/index.ts pra usar `searchProductsEnriched` em vez de `searchProducts`
7. Unificar `buildSearchText` em `_shared/embeddings.ts` (achado #13)

**DoD:**
- [ ] Evolution aponta pra **único** endpoint
- [ ] N8N Principal `active=false` e/ou workflow removido
- [ ] `process-ml-question` usa `searchProductsEnriched` (se ADR-006=sim)
- [ ] `rg "buildSearchText" supabase/functions/` só mostra definições em `_shared/`
- [ ] ADR em `docs/adr/001-pipeline-whatsapp.md`

### B5 — Governança
**Achados:** #5, #6, #8, #21, #22, #24
**Esforço:** L (1–2 sem, incremental)
**Pré-req:** nenhum — paralelizável
**Objetivo:** Testes + CI + sync dirty + drift audit.
**Passos principais:**
1. Commitar ou stashar working copy dirty ([[_historico#Pendências]] + achado #21)
2. `scripts/sync-n8n-workflows.sh` — baixa os 5 workflows live via API e sobrescreve locais; commitar (#6)
3. Vitest smoke tests em frontend (3 tests mínimos)
4. Deno.test smoke em process-message + webhook-whatsapp + send-human-message
5. GitHub Actions `.github/workflows/ci.yml` (lint + tsc --noEmit + deno check)
6. Reescrever `scripts/deploy-functions.sh` iterando TODAS as 13 functions (split INTERNAL/EXTERNAL do B1) — #8
7. Script `scripts/schema-drift-check.sh` comparando banco vs DDL cumulativo das migrations (#24)

**DoD:**
- [ ] `git status --short` limpo no monorepo
- [ ] Diff `n8n/workflow-*.json` local vs live = zero
- [ ] `pnpm test` ≥3 smoke tests passando
- [ ] CI rodando em PRs
- [ ] deploy-functions.sh cobre 13/13
- [ ] `docs/schema-drift.md` existe (mesmo que zero drift)

### B6 — Cleanup
**Achados:** #17, #19, #20, #23
**Esforço:** S (1–2 dias)
**Pré-req:** B1 completo (#2 test-search já tratado) + [[decisoes#ADR-003]] ✅ + [[decisoes#ADR-004]] ✅

#### B6 passo 0 (novo): Re-auditar "objetos sem migration criadora"
Antes dos drops/migrations (passos seguintes), revisar `~/audit-canggu-forensics/RAW/C_analysis/23_migrations_vs_state.md` seção "Objetos órfãos" com regra **corrigida**: grepar por `ALTER TABLE <nome>` além de `CREATE TABLE <nome>`.

Se encontrar outros objetos no padrão "criado via Lovable + ALTER em migration tracked", aplicar **migration retroativa** (padrão ADR-004) em vez de drop. Ver [[decisoes#ADR-004]] — seção "Meta-achado" — para racional.

Candidatos a re-auditar (da Fase 2): `products_backup_20260404` já foi classificado como órfão puro em grep original, mas vale um duplo-check com a nova regra antes de dropar.

**DoD passo 0:**
- [ ] Lista completa de "objetos sem migration criadora" re-verificada com grep ALTER + CREATE
- [ ] Decisão por objeto: drop vs migration retroativa, documentada num parágrafo curto em `docs/adr/b6-dead-code-review.md`

#### Plano principal (passos 1+)
1. **ADR-004:** criar migration retroativa `supabase/migrations/YYYYMMDDHHMMSS_document_marketplace_chats_retroactive.sql` baseada em `~/audit-canggu-forensics/RAW/C_analysis/_adr004_ddl_extract.sql`. Validar: `supabase db reset` local + aplicar todas migrations → schema idêntico à produção.
2. **ADR-003:** habilitar `verify_jwt=true` em `test-semantic-search` + documentar no README.
3. **`products_backup_20260404`** (achado #17, após passo 0 confirmar drop): DROP com BEGIN/ROLLBACK preview primeiro, depois migration de drop definitiva.
4. **Zod validation** (achado #23) em 3 edge fns principais (process-message, send-human-message, ml-webhook).

**DoD:**
- [ ] `products_backup_20260404` não existe
- [ ] ADR-004 resolvido (migration ou drop executados)
- [ ] `test-semantic-search` com `verify_jwt=true`
- [ ] Zod rodando em ≥3 edge fns

## Sequenciamento sugerido

```
Semana 1-2:  B1 ████████████████ (crítico — Segurança)
             B5 ████████████████ (paralelo — parte 1: CI + sync N8N + commit dirty)

Semana 3:    B2 ████████████ (Observabilidade)
             B5 ████████ (parte 2: smoke tests)

Semana 4:    B3 ████████████ (Resiliência)
             B6 ████ (parte 1: drops + docs)

Semana 5-6:  B4 ████████████████████ (Arquitetura pós-ADR-006)
             B6 ████ (parte 2: zod)
             B5 ████ (drift audit)
```

**Paralelismo confirmado:**
- B1 + B5-1 (semanas 1–2) — zero dependência técnica
- B2 + B3 (semanas 3–4) — B3 se beneficia de B2 mas não depende
- B6 pinga ao longo do trajeto

**Dependências duras:**
- B1 passo 2 (delete test-search) antes do passo 13 (habilitar verify_jwt)
- B4 pode começar assim que [[perguntas-abertas#ADR-006]] for respondida (ADR-007 já ok)
- B2 passo 1 (Slack webhook) depende de [[decisoes#ADR-005]] ✅ já resolvido

## Evidência completa

- Matriz detalhada: `~/audit-canggu-forensics/RAW/C_analysis/28_priority_matrix.md`
- Roadmap completo com DoD e rollback: `~/audit-canggu-forensics/AUDIT_REPORT.md` §6
