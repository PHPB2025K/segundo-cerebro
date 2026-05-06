---
title: "Deletar Edge Functions Supabase via REST API (sem CLI)"
created: 2026-05-06
type: concept
status: active
tags:
  - knowledge
  - supabase
  - edge-functions
  - mcp
  - api
---

# Deletar Edge Functions Supabase via REST API (sem CLI)

## Problema

O MCP server do Supabase (`@supabase/mcp-server-supabase`) **não tem `delete_edge_function` no toolset** — só `list`, `get`, e `deploy`. O fluxo padrão é usar o Supabase CLI (`supabase functions delete`), mas isso exige terminal local autenticado, o que nem sempre é viável (Pedro não usa terminal).

## Solução

Usar a **Supabase Management REST API** diretamente via `curl`, autenticando com o **mesmo PAT que o MCP server já usa** (`SUPABASE_ACCESS_TOKEN` em `~/.mcp.json`).

### Endpoint

```
DELETE https://api.supabase.com/v1/projects/{project_ref}/functions/{slug}
Authorization: Bearer {PAT}
```

### Receita prática

Extrair o PAT do MCP config sem expor em transcript/env persistente, e fazer DELETE em loop:

```bash
PAT=$(jq -r '.mcpServers.supabase.env.SUPABASE_ACCESS_TOKEN' ~/.mcp.json) && \
  for fn in fn-1 fn-2 fn-3; do
    echo "=== DELETE $fn ==="
    curl -s -o /tmp/del-$fn.txt -w "HTTP %{http_code}\n" \
      -X DELETE \
      -H "Authorization: Bearer $PAT" \
      "https://api.supabase.com/v1/projects/{PROJECT_REF}/functions/$fn"
    echo "body: $(cat /tmp/del-$fn.txt | head -c 200)"
    rm -f /tmp/del-$fn.txt
  done
unset PAT
```

**Cuidados de segurança:**
- Token nunca aparece literalmente no transcript (vai como `$PAT`)
- `unset PAT` ao fim do bloco
- Body da resposta vem por arquivo temp e é deletado após print
- HTTP 200 = deletado; HTTP 404 = já não existia

### Validar pós-delete

Confirmar via MCP que sumiram:

```
mcp__supabase__list_edge_functions(project_id)
```

## Quando usar

- Pedro pediu pra remover edges em prod e não tem CLI local
- Sessão Claude Code precisa fazer cleanup destrutivo de edges sem ação manual
- Migrações onde várias edges precisam sair de uma vez

## Quando NÃO usar

- Se for substituir a edge por nova versão: usar `mcp__supabase__deploy_edge_function` (versiona, mais limpo)
- Se quiser apenas neutralizar temporariamente: deploy de stub que retorna 410 Gone (mais reversível)

## Caso de uso real

**Social Studio Reborn (06/05/2026):** 5 edge functions legacy (`generate-social-copy`, `social-generate-image`, `social-render-slide`, `social-render-carousel`, `social-export`) deletadas em prod (`ioujfkrqvporfbvdqyus`) durante a Fase A. 5 × HTTP 200. Validação via `list_edge_functions` confirmou: só restaram MP + orders.

Commit registrando: `d6e76d5` (vazio, só doc) na branch `feature/social-studio-reborn`.

## Referências

- Supabase Management API: https://supabase.com/docs/reference/api/v1-delete-a-function
- MCP Supabase: `~/.mcp.json` → `mcpServers.supabase`
- [[projects/social-studio-reborn]]
