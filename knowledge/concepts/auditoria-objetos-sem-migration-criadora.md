---
title: "Auditoria de objetos sem migration criadora"
created: 2026-04-22
type: concept
status: active
tags:
  - conhecimento
  - auditoria
  - supabase
  - migrations
  - lovable
fonte: "[[projects/canggu/decisoes#ADR-004]]"
---

# Auditoria de objetos sem migration criadora

> Meta-achado da auditoria forense Canggu (22/04/2026). Regra reutilizável
> para auditorias futuras em qualquer projeto Supabase / Postgres.

## Contexto

Ao auditar "drift entre migrations versionadas e estado do banco", é comum
procurar tabelas que existem no banco mas **nenhuma migration local cria**.

O grep ingênuo faz:
```bash
grep -rE "CREATE TABLE" supabase/migrations/ | grep <nome_tabela>
```

Se nada aparece, classifica a tabela como "sem migration criadora" — e
tipicamente a primeira hipótese é **dead code → drop**.

## Por que isso falha

Projetos que usam **AI builders de dashboard** (Lovable, Bolt, Supabase
Studio), ou criação manual via `psql` / painel web, seguem um padrão:

1. Tabela é **criada fora do git** (via UI, via AI builder)
2. Migrations subsequentes versionadas **estendem** o schema com `ALTER
   TABLE ADD COLUMN IF NOT EXISTS` — sem `CREATE TABLE`
3. O grep por `CREATE TABLE` nunca encontra essas tabelas, mas elas
   **têm** referência nas migrations (via ALTER)

Resultado: o grep ingênuo flaga tabela como drift órfão, mas ela é
**legítima parte do schema** — só foi criada fora da disciplina git.

## Caso real — Canggu 22/04/2026

Tabelas `marketplace_chats` e `marketplace_chat_messages`:

- Grep ingênuo: 0 hits em `CREATE TABLE`
- Classificação inicial: dead code, candidato a drop
- Query empírica: 0 rows, `created_at` NULL em ambas — reforçou hipótese
- Preview ROLLBACK: sem dependências físicas em `pg_depend`

**Mas:**
- `supabase/migrations/20260307000000_add_marketplace_integration.sql`
  linha 62: comentário `-- ALTER: marketplace_chats (created by Lovable)`
  + 6 ALTER TABLE ADD COLUMN IF NOT EXISTS + 6 CREATE INDEX IF NOT EXISTS
- `supabase/functions/ml-webhook/index.ts` — 7 INSERT/UPDATE nas tabelas
- `supabase/functions/_shared/ml-types.ts` — types + FK declarada
- `n8n/workflow-ml-messages.json` (ACTIVE no live) — INSERT via REST

Tabelas vazias **porque volume de chat ML ainda não gerou mensagens de
comprador**. Não são dead code — estão esperando dados reais.

**Drop teria quebrado:**
- `ml-webhook` edge function (404 no próximo INSERT)
- Workflow N8N ML Messages (falha no próximo buyer message)
- Staging fresh via `supabase db push` (ALTER em tabela inexistente)

## Regra corrigida

Ao auditar "objetos sem migration criadora", **grep combinado por duas
formas**:

```bash
# Busca 1 — ingênua (CREATE TABLE)
grep -rE "CREATE TABLE.*<nome>" supabase/migrations/

# Busca 2 — incremental (ALTER TABLE)
grep -rE "ALTER TABLE[[:space:]]+(public\.)?<nome>" supabase/migrations/

# Se (1) vazio E (2) tem hits → criação veio fora do git
# Se ambos vazios → drift real, candidato a investigar mais (grep em
# código + workflows antes de drop)
```

## Decisão quando (1) vazio + (2) tem hits

**Resposta correta: migration retroativa idempotente**, não drop.

Padrão:

```sql
-- supabase/migrations/YYYYMMDDHHMMSS_document_<nome>_retroactive.sql
-- Documentação retroativa de tabela criada via Lovable/Bolt/manual.
-- Idempotente: CREATE TABLE IF NOT EXISTS não altera se já existe.

CREATE TABLE IF NOT EXISTS public.<nome> (
  -- DDL extraído do banco via pg_attribute + pg_attrdef
  "id" uuid NOT NULL DEFAULT gen_random_uuid(),
  -- ... resto das colunas exatamente como estão no banco
);

-- Constraints idempotentes via DO block
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_constraint WHERE conname = '<nome>_pkey') THEN
    ALTER TABLE public.<nome> ADD CONSTRAINT <nome>_pkey PRIMARY KEY (id);
  END IF;
  -- FKs idem
END $$;

-- Indexes idempotentes
CREATE INDEX IF NOT EXISTS idx_<nome>_xxx ON public.<nome>(...);

-- RLS + Policies
ALTER TABLE public.<nome> ENABLE ROW LEVEL SECURITY;
CREATE POLICY IF NOT EXISTS <nome_policy> ON public.<nome> ...;
```

Resultado:
- Produção: migration não faz nada (tudo já existe) — seguro
- Staging fresh: migration cria o schema base, migrations subsequentes
  com ALTER IF NOT EXISTS estendem normalmente
- Princípio "tudo que está no banco tem migration" restaurado
- Zero impacto em código ou dados existentes

## Como extrair o DDL correto

Via Management API Supabase ou `mcp__supabase__execute_sql`:

```sql
SELECT
  'CREATE TABLE IF NOT EXISTS public.' || c.relname || ' (' ||
  string_agg(
    '"' || a.attname || '" ' ||
    pg_catalog.format_type(a.atttypid, a.atttypmod) ||
    CASE WHEN a.attnotnull THEN ' NOT NULL' ELSE '' END ||
    CASE WHEN ad.adbin IS NOT NULL
         THEN ' DEFAULT ' || pg_get_expr(ad.adbin, ad.adrelid)
         ELSE '' END,
    ', ' ORDER BY a.attnum
  ) || ');' AS ddl
FROM pg_class c
JOIN pg_attribute a ON a.attrelid = c.oid
LEFT JOIN pg_attrdef ad ON ad.adrelid = c.oid AND ad.adnum = a.attnum
WHERE c.relname = '<nome>'
  AND c.relnamespace = 'public'::regnamespace
  AND a.attnum > 0 AND NOT a.attisdropped
GROUP BY c.relname;
```

Para PKs, FKs, indexes, policies: queries complementares em
`information_schema` e `pg_policies`. Exemplo completo em
`~/audit-canggu-forensics/RAW/C_analysis/_adr004_ddl_extract.sql`.

## Quando drop É a decisão correta

Apenas quando **ambos** os greps retornam zero + **código não referencia**
a tabela (grep em `src/`, `supabase/functions/`, `n8n/`) + **zero rows**
+ **preview ROLLBACK limpo**. Aí sim, dead code.

## Aplicabilidade

Regra vale pra qualquer projeto Supabase / Postgres, especialmente:
- Projetos que começaram no Lovable / Bolt / v0
- Projetos que usam Supabase Studio para criar tabelas visualmente
- Migrações de stacks no-code → code (dashboard manual → migrations git)

## Ver também

- [[projects/canggu/decisoes#ADR-004]] — caso original onde a regra foi descoberta
- [[projects/canggu/debitos-tecnicos#B6-passo-0]] — re-auditoria com regra corrigida antes de drops
