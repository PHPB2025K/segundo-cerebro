---
tipo: decisao
projeto: Canggu
status: ativo
tags:
  - canggu
  - decisoes
  - adr
criado: 2026-04-22
atualizado: 2026-04-22
fonte-auditoria: "[[auditorias/2026-04-22-forense]]"
---

# Decisões — Canggu

Registro cronológico de decisões operacionais e arquiteturais. Período
06/04 a 22/04/2026. Continuidade em nova seção a cada marco.

## Índice

### Pré-auditoria (06–17/04/2026)
Fonte integral: [[_historico]]. Contexto: pipeline vetorial inicial +
downtime de 8 dias pós-deploy quebrado + restauração + refactor do Health
Check + padrões de credentials.

- [[#DP-01]] — [06/04] Pipeline vetorial (embedding → pgvector → contexto)
- [[#DP-02]] — [06/04] Bug envio WhatsApp humano→cliente corrigido
- [[#DP-03]] — [17/04] Ana restaurada após 8 dias — placeholders hardcoded substituídos
- [[#DP-04]] — [17/04] ML Questions destravado (placeholders YOUR_*)
- [[#DP-05]] — [17/04] Feedback loop ativo (search_corrections RPC)
- [[#DP-06]] — [17/04] Trigger pg_net trg_base_product_embedding_sync criado
- [[#DP-07]] — [17/04] Health Check refatorado com 4 checks reais
- [[#DP-08]] — [17/04] N8N Credentials Opção A no principal
- [[#DP-09]] — [17/04] linkPreview: false no Send WhatsApp Response
- [[#DP-10]] — [17/04] Auditoria 48 threads / 151 respostas concluída

### ADRs da auditoria (22/04/2026)
- [[#ADR-001]] — Armazenamento do service_role_key via `ALTER DATABASE SET` ✅
- [[#ADR-002]] — Remover `LOVABLE_API_KEY` direto ✅
- [[#ADR-003]] — Manter `test-semantic-search` com `verify_jwt=true`; deletar `test-search` ✅
- [[#ADR-004]] — Documentação retroativa de `marketplace_chats*` (CREATE TABLE IF NOT EXISTS) ✅
- [[#ADR-005]] — Canal de alerting: Slack ✅
- [[#ADR-006]] — Portar pipeline ML pra base_products em B4 — ⏳ **Pendente** ([[perguntas-abertas#ADR-006]])
- [[#ADR-007]] — Pipeline WhatsApp canônico: edge function ✅

---

## Decisões pré-auditoria (06–17/04/2026)

> Fonte integral: [[_historico]].
> Período: construção do pipeline vetorial → downtime 09–17/04 → restauração → estabilização pré-auditoria.

### DP-01
**Data:** 06/04/2026
**Decisão:** Pipeline vetorial: embedding pergunta → busca vetorial (pgvector) → SQL → contexto enriquecido.
**Impacto atual:** arquitetura ainda vigente; ver [[supabase-canggu#Triggers críticos]] e [[edge-functions]] (sync-*-embedding functions).

### DP-02
**Data:** 06/04/2026
**Decisão:** Bug envio WhatsApp humano→cliente CORRIGIDO (feature do dashboard Budamix Central).
**Impacto atual:** [[edge-functions#Tabela de referência]] — `send-human-message`. Achado novo #14 na auditoria (retorna `success:true, sent:false` sob falha) é um refinamento desse caso, endereçado em [[debitos-tecnicos#B3]].

### DP-03
**Data:** 17/04/2026
**Decisão:** Ana restaurada após 8 dias de downtime (09–17/04). Placeholders hardcoded `SUPABASE_SERVICE_ROLE_KEY_PLACEHOLDER` e `WHATSAPP_API_KEY_PLACEHOLDER` em 8 Code nodes do workflow `KE7YVXayl5ntjwQk` substituídos por chaves reais. Deploy de 12–13/04 havia reintroduzido o problema via import de workflow stub.
**Motivação:** evitar recidiva → adoção do padrão "Setup Credentials" (ver DP-08).
**Impacto atual:** [[n8n-workflows]].

### DP-04
**Data:** 17/04/2026
**Decisão:** ML Questions workflow `g4JxNpC2sP9K8c71` destravado — 8 placeholders `YOUR_*` substituídos. Refresh OAuth ML automático via `marketplace_tokens` intacto.
**Impacto atual:** [[n8n-workflows]] — ML Questions é hoje 100% sincronizado entre local e live.

### DP-05
**Data:** 17/04/2026
**Decisão:** Feedback loop ativo no WhatsApp — `search_corrections` RPC criada no Supabase, `process-message` integrado com as correções via `searchCorrections()` (threshold 0.85, bloco "CORREÇÕES APRENDIDAS" no prompt).
**Impacto atual:** [[supabase-canggu#Functions PL/pgSQL críticas (schema public, 7 total)]] e feature em dirty working copy (working copy tem +237 LOC em `process-message`). Ver [[debitos-tecnicos#B5]] achado #21.

### DP-06
**Data:** 17/04/2026
**Decisão:** Trigger pg_net `trg_base_product_embedding_sync` criado — re-embedding automático de `base_products` para qualquer origem de UPDATE (não só UI do Budamix Central).
**Impacto atual:** [[supabase-canggu#Triggers críticos]]. A migration criadora (`20260417120000_auto_embed_trigger_base_products.sql`) está **UNTRACKED** no working copy — commit pendente em B5.

### DP-07
**Data:** 17/04/2026
**Decisão:** Health Check refatorado com 4 checks reais (Supabase auth, Ana responsividade, Evolution state, erros do principal <30min). Alerta via WhatsApp para 5519993040768 (pessoal, não o da Ana).
**Impacto atual:** [[n8n-workflows]] — este workflow sofreu drift massivo pós-17/04 (live hoje tem apenas 2 nodes). Redesenho em B2 com canal Slack ([[#ADR-005]]).

### DP-08
**Data:** 17/04/2026
**Decisão:** N8N Credentials Opção A no workflow principal — `Process Message (AI)` usa credential httpHeaderAuth; 7 Code nodes + Send WhatsApp Response leem chaves de um único `Setup Credentials` node com guard clauses. SRK: 9→1 ocorrências, WAK: 2→1 no JSON.
**Motivação:** evitar nova cascata como os 8 dias de downtime (DP-03). Guard clauses detectam placeholders acidentais em tempo de execução.
**Impacto atual:** [[n8n-workflows#Padrão de credenciais (Setup Credentials, Opção A)]] documenta o padrão completo. O workflow principal é depreciado em [[#ADR-007]] — padrão segue relevante para os demais workflows N8N ativos.

### DP-09
**Data:** 17/04/2026
**Decisão:** `linkPreview: false` no node "Send WhatsApp Response" — elimina bolha de loading que aparecia em msgs com URL.
**Impacto atual:** ajuste UX no Evolution API; persiste no workflow mesmo após depreciação do N8N principal (será replicado na edge function canônica).

### DP-10
**Data:** 17/04/2026
**Decisão:** Auditoria 48 threads / 151 respostas concluída — 60% ✅ / 18% ⚠️ / 18% ❌ / 4% 🔄. 4/5 padrões top já corrigidos pelos fixes de 04/04 + 12/04. Único residual: loop de qualificação de canal (Rec 4.1). Artefato: `auditoria-ana-whatsapp-abril2026.md`.
**Pendência não resolvida:** aplicar Rec 4.1 — regra ANTI-LOOP DE CANAL no Passo 4a do BLOCO 4 do `system_prompt` (bloqueia repetir "site/ML/Shopee?" quando cliente já respondeu).
**Impacto atual:** [[_historico#Pendências]] mantém a Rec 4.1 em aberto; não foi endereçada na auditoria forense 22/04 (escopo diferente — comportamento de prompt vs estado técnico do sistema).

---

## ADRs da auditoria (22/04/2026)

### ADR-001
**Título:** Armazenamento do service_role_key via `ALTER DATABASE SET`
**Status:** ✅ Decidido (22/04)
**Contexto:** 3 arquivos tracked no repo contêm o service_role JWT literal como fallback de `current_setting('app.settings.service_role_key', true)`, e `ALTER DATABASE` nunca foi executado — o fallback está sempre ativo. Histórico git exposto desde 2026-03-06.
**Decisão:** Adotar opção (a) do relatório — `ALTER DATABASE postgres SET app.settings.service_role_key = '<key_nova>';` como config permanente do banco. Triggers leem via `current_setting` sem fallback.
**Consequências:**
- Key fora do git, fora do runtime memory dos edge functions.
- Rotação = 1 comando SQL (não requer nova migration).
- Acessível apenas a admins do Postgres (quem tem credenciais db.<ref>.supabase.co).
**Implementação:** [[debitos-tecnicos#B1]] passo 7.

### ADR-002
**Título:** Remoção do `LOVABLE_API_KEY`
**Status:** ✅ Decidido (22/04)
**Contexto:** Secret declarado em Edge Secrets do Supabase, zero referências em `supabase/functions/**/*.ts`. Legado do tempo em que o projeto era Lovable-first.
**Decisão:** Remover direto via `supabase secrets unset LOVABLE_API_KEY`, sem verificação adicional no dashboard Lovable (Pedro confirmou que Lovable atual é espelho passivo, sem webhook externo).
**Consequências:** reduz surface de exposição. Se alguma integração desconhecida usava, vai falhar explicitamente — mais fácil de descobrir do que silêncio.
**Implementação:** [[debitos-tecnicos#B1]] passo 12.

### ADR-003
**Título:** Destino das funções de debug (`test-search`, `test-semantic-search`)
**Status:** ✅ Decidido (22/04)
**Contexto:** `test-search` é ghost (deployed sem código no repo, comentário `// DELETE after testing`, `verify_jwt=false`, 8 calls OpenAI por invocação). `test-semantic-search` está no repo, `verify_jwt=false`, zero chamadores.
**Decisão:**
- **`test-search`:** deletar via `supabase functions delete test-search`.
- **`test-semantic-search`:** manter com `verify_jwt=true` + documentar no README do monorepo como ferramenta de debug que requer JWT.
**Consequências:** elimina vetor de abuso público; mantém ferramenta de debug manual para casos de triage semântica.
**Implementação:** [[debitos-tecnicos#B1]] passo 2 (delete test-search) + [[debitos-tecnicos#B6]] (restringir test-semantic-search).

### ADR-004
**Título:** Documentação retroativa de `marketplace_chats` e `marketplace_chat_messages`
**Data decisão:** 2026-04-22 (revisada no mesmo dia após descoberta)
**Status:** ✅ Decidido — Migration retroativa `CREATE TABLE IF NOT EXISTS` (executar em B6)
**Bloco afetado:** B6 (Cleanup)

#### Contexto original (pré-descoberta)
Duas tabelas no schema public classificadas pela Fase 2 da auditoria como "sem migration criadora" e "não referenciadas em código ativo". Hipótese inicial: drop seguro.

#### Descoberta que mudou a decisão
Query de investigação e preview ROLLBACK revelaram que:

1. **Tabelas estão vazias** (0 rows, `created_at` NULL em ambas) — fato que sustentava a hipótese original.

2. **Mas são usadas por código ATIVO** — refs em:
   - `supabase/functions/ml-webhook/index.ts` linhas 290, 372, 397, 409, 428, 439, 465 (7 INSERTs/UPDATEs)
   - `supabase/functions/_shared/ml-types.ts` linhas 141, 229 (types + FK)
   - `n8n/workflow-ml-messages.json` linhas 23, 71 (INSERTs via REST) — workflow `sg2yU46R9EQq3a2v` está `active=true` no live

3. **Migration tracked EXISTE** — `supabase/migrations/20260307000000_add_marketplace_integration.sql` linhas 62–111 reconhece as tabelas explicitamente:
   - Comentário `-- ALTER: marketplace_chats (created by Lovable)`
   - 6 `ALTER TABLE marketplace_chats ADD COLUMN IF NOT EXISTS`
   - 2 `ALTER TABLE marketplace_chat_messages ADD COLUMN IF NOT EXISTS`
   - 6 `CREATE INDEX IF NOT EXISTS`

   Ou seja: tabelas foram criadas via Lovable (AI editor do dashboard Supabase), e a migration versionada estende o schema com ALTERs idempotentes. Foi design consciente, não drift.

4. **Vazias porque ML não gerou mensagens de comprador no período** — workflow ML Messages só insere quando detecta mensagem em pedido ativo dos últimos 7 dias. Baixo volume de ML explica 0 rows.

#### Por que drop quebraria produção
- `ml-webhook` quebra em 404 no próximo INSERT
- Workflow N8N ML Messages quebra no próximo buyer message
- Staging fresh via `supabase db push` falha (ALTER TABLE em tabela inexistente)

#### Opções revisadas após descoberta
- (a) ~~Drop~~ — descartada, quebra produção
- (b) Migration retroativa com `CREATE TABLE IF NOT EXISTS` — **escolhida**
- (c) Manter como está, aceitar o desvio — rejeitada (staging quebra)

#### Decisão
Opção (b). Criar migration retroativa em B6 com DDL idêntico ao estado atual do banco.

#### Plano de execução (B6)
1. DDL já extraído e salvo em `~/audit-canggu-forensics/RAW/C_analysis/_adr004_ddl_extract.sql` (DDL gerado via `pg_attribute` + `pg_attrdef` + `pg_constraint` + `pg_indexes` + `pg_policies` do estado atual).
2. Criar migration `supabase/migrations/YYYYMMDDHHMMSS_document_marketplace_chats_retroactive.sql` baseada no extract — incluindo `CREATE TABLE IF NOT EXISTS`, `ALTER TABLE ADD CONSTRAINT` (PK + 3 FKs) em DO block idempotente, `CREATE INDEX IF NOT EXISTS` (6 indexes), `ENABLE ROW LEVEL SECURITY`, `CREATE POLICY IF NOT EXISTS` (1 policy por tabela).
3. Validar localmente: `supabase db reset` + aplicar todas as migrations em ordem → schema final deve ser idêntico à produção.
4. Aplicar em produção: `supabase db push` (seguro — tudo `IF NOT EXISTS` / DO block idempotente, nada altera se objeto já existe).

#### Rollback
Migration é idempotente — aplicar em produção não faz nada (tabelas já existem). Se algo der errado em staging/local, rollback é DROP das duas tabelas (seguro em fresh environment, sem dados a preservar).

#### Consequências
- Schema Canggu passa a ser 100% reproduzível via migrations versionadas
- Clone fresh de ambiente deixa de quebrar
- Princípio "tudo que está no banco tem migration" restaurado
- Zero impacto em produção (migration idempotente)

#### Meta-achado (lição da auditoria)
A Fase 2 da auditoria classificou essas tabelas como "sem migration criadora" porque o grep só olhava por `CREATE TABLE` em migrations. Quando o Lovable cria tabelas via dashboard, a migration tracked frequentemente referencia apenas com `ALTER TABLE ADD COLUMN IF NOT EXISTS`, sem o `CREATE` — isso é drift invisível para o grep ingênuo.

**Regra adicionada para auditorias futuras:** ao auditar "objetos sem migration criadora", grep combinado por `CREATE TABLE <nome>` **E** `ALTER TABLE <nome>` — se só aparecer ALTER, é provável que a criação original veio fora do git (Lovable, dashboard manual, psql direto). Nesses casos, migration retroativa restaura a disciplina.

#### Auditoria de escopo derivada
Outras tabelas classificadas na Fase 2 como "sem migration criadora" podem estar no mesmo cenário. Antes de B6 executar, re-auditar aquela lista aplicando a regra acima — tarefa virou [[debitos-tecnicos#B6 passo 0 (novo): Re-auditar "objetos sem migration criadora"]]. Fonte: seção "Objetos órfãos" em `~/audit-canggu-forensics/RAW/C_analysis/23_migrations_vs_state.md`.

### ADR-005
**Título:** Canal de alerting do Health Check
**Status:** ✅ Decidido (22/04)
**Contexto:** Workflow "Health Check" tinha 11 nodes no export local e foi simplificado para 2 nodes no live (SMTP removido). Canal de alerta efetivamente morto. Recomendação original do relatório era Telegram (para alinhar com OpenClaw no VPS); decisão foi Slack.
**Decisão:** **Slack** como canal de alerta dedicado. Novo Health Check em B2 usa node "Slack Incoming Webhook" em vez do node SMTP original.
**Consequências:** alinha com eventual uso corporativo (distinto do canal pessoal WhatsApp 5519993040768 do DP-07, que era alerta de emergência). Requer criar webhook Slack e armazenar URL em Credentials do N8N.
**Implementação:** [[debitos-tecnicos#B2]] passos 1–2.

### ADR-006
**Título:** Portar pipeline ML (`process-ml-question`) pra `searchProductsEnriched` em B4
**Status:** ⏳ **Pendente** — Pedro decide antes de iniciar B4
**Contexto:** Pipeline WhatsApp usa `searchProductsEnriched` ([[supabase-canggu|base_products]]). Pipeline ML usa `searchProducts` legacy ([[supabase-canggu|products]]). Divergência de qualidade entre canais.
**Decisão:** não tomada. Default se não decidir até início de B4 = **não portar** (adiar como dívida conhecida).
**Implementação:** [[debitos-tecnicos#B4]] passo 6 (condicional).

### ADR-007
**Título:** Pipeline WhatsApp canônico — edge function `webhook-whatsapp`
**Status:** ✅ Decidido (22/04)
**Contexto:** N8N workflow "Principal" (17 nodes live) e edge function `webhook-whatsapp` (490 LOC) implementam o mesmo fluxo. Evolution aponta para um dos dois; ambos estão ativos. Manutenção dupla, cada mudança precisa ser feita em 2 lugares.
**Decisão:** **Edge function canônica.** N8N workflow "Principal" será depreciado em B4.
**Racional:**
- Alinha com resto da stack (tudo em TS no monorepo)
- Simplifica testabilidade (Deno.test)
- Reduz número de peças móveis
- Padrão Setup Credentials (DP-08) fica desnecessário para este fluxo — edge function lê via `Deno.env.get`, zero JS embutido em JSON de workflow
**Consequências:**
- Padrão Setup Credentials segue relevante para os outros workflows N8N (ML Questions, ML Messages, Relatório Diário, Health Check).
- Perde observabilidade visual do fluxo via N8N UI — mitigada via logging estruturado + rota `/operations` no frontend (B2).
- Dashboard Budamix Central tem integração direta com edge fn via `fetch` — não afetado.
**Implementação:** [[debitos-tecnicos#B4]] passos 1–5 + ADR em `docs/adr/001-pipeline-whatsapp.md` (a criar).
