---
title: "Auditoria de wikilinks no Knowledge Graph — método e armadilhas"
created: 2026-04-27
type: concept
status: active
tags:
  - knowledge
  - knowledge-graph
  - obsidian
  - vault-manutencao
  - auditoria
---

# Auditoria de wikilinks no Knowledge Graph — método e armadilhas

> Método consolidado a partir da auditoria de 27/04/2026 que zerou os nodes isolados do segundo cérebro (182 → 0). Inclui erros que cometi e como evitá-los.

## Objetivo

Garantir que todo node do vault esteja conectado semanticamente — sem ilhas isoladas. Princípio operacional do Pedro: "qualquer node sem conexões está errado".

## Conceitos do KG (sqlite plugin)

| Conceito | Definição |
|----------|-----------|
| **Node** | Arquivo `.md` real do vault, indexado em `nodes` |
| **Stub** | Placeholder em `_stub/...` criado automaticamente pelo KG quando wikilink aponta pra arquivo/heading inexistente |
| **Edge** | Wikilink resolvido entre source_id e target_id |
| **Isolado** | Node com zero edges in/out — não cita ninguém E não é citado |
| **Stub zumbi** | Stub que nenhum node real referencia mais (descontinuado mas ainda no banco — só sai com rebuild) |

## Queries SQL essenciais

```sql
-- Total isolados
SELECT COUNT(*) FROM nodes
WHERE id NOT IN (SELECT source_id FROM edges)
  AND id NOT IN (SELECT target_id FROM edges);

-- Stubs criados por wikilinks órfãos
SELECT target_id, COUNT(*) refs FROM edges
WHERE target_id LIKE '_stub/%'
GROUP BY target_id ORDER BY refs DESC;

-- Stubs zumbis (sem ninguém referenciando)
SELECT id FROM nodes WHERE id LIKE '_stub/%'
  AND id NOT IN (SELECT target_id FROM edges);

-- Wikilinks meus que viraram stub (validar pós-edição em massa)
SELECT source_id, target_id FROM edges
WHERE target_id LIKE '_stub/%' AND source_id LIKE '<padrão dos arquivos editados>';
```

## Método em 5 passos

### 1. Mapear (auditoria de leitura)
- Query SQL → lista de isolados
- Categorizar por subpasta (`openclaw/`, `knowledge/`, `memory/`, etc.)
- Distinguir tipos: notas humanas canônicas vs logs de agentes vs stubs estruturais

### 2. Decidir escopo
- **Notas humanas isoladas** → defeito, corrigir
- **Logs cronológicos de agentes** → pode pular (Opção A) ou conectar com âncoras leves (Opção B)
- **Stubs `_stub/...#Heading`** → não-editáveis (são fragments); só some criando o heading no arquivo alvo
- **Artefatos descartáveis** (relatórios temporários, drafts antigos) → considerar deletar ao invés de conectar

### 3. Construir set de targets VÁLIDOS antes de qualquer edição

**ARMADILHA #1:** templates de wikilinks (ex: `[[memory/sessions/{data}]]`) podem gerar paths que não existem. **Sempre validar contra o KG ANTES de inserir.**

```python
import sqlite3
con = sqlite3.connect(DB)
real_ids = {row[0] for row in con.execute("SELECT id FROM nodes WHERE id NOT LIKE '_stub/%'")}
real_basenames = {rid[:-3] if rid.endswith('.md') else rid for rid in real_ids}

def exists(target):
    return target in real_basenames or target + '.md' in real_ids
```

Cada candidato a wikilink passa por `exists()` antes de virar linha no arquivo.

### 4. Aplicar (manual + script híbrido)

**Manual** para nodes do vault público (poucos, alta importância): ler conteúdo, identificar 3-7 wikilinks semânticos coerentes, inserir inline + "Ver também" no fim.

**Script** para conectar lotes grandes (memórias de agentes, skills internas):
- Classificar por padrão de path (regex no path)
- Gerar âncoras estruturais por categoria (IDENTITY/SOUL/AGENTS do agente proprietário, decisões do mês, business-context)
- Detectar conceitos canônicos no conteúdo via regex (`shopee`, `bidspark`, `canggu`, etc.) e adicionar wikilink se o target existir
- Skipar arquivos que já têm seção "Ver também"
- Filtrar candidatos via `exists()` antes da inserção

### 5. Validar e limpar

- Reindexar KG (incremental: `kg_index` MCP / completo: deletar `kg.db` + CLI rebuild)
- Comparar contagem de stubs antes/depois
- Se subiram stubs **e os novos vieram dos arquivos editados** → tem broken wikilinks
- Rodar script de limpeza: ler o set de IDs reais e remover linhas de "Ver também" cujo alvo não existe

## Armadilhas conhecidas

| Erro | Sintoma | Prevenção |
|------|---------|-----------|
| Wikilinks pra `memory/sessions/{data}` ou `decisoes/{mês}` que não existem | Stubs de mês passado aparecem após edição | Validar com `exists()` antes do append |
| Editar arquivos enquanto o agente (Kobe) cria novos no VPS em paralelo | Conflito no `git push` + arquivos novos isolados | Após rebase, re-rodar query de isolados e processar os novos |
| Reindex incremental não remove stubs zumbis | Contagem de stubs nunca baixa | Rebuild completo: `rm kg.db && CLI index` |
| Path do KG diferente do path real (encoding, sinal `\`) | Stubs `_stub/.../IDENTITY\.md` aparecem | Padronizar paths no script (sem escape de `.`) |
| Symlinks fora do vault | Edits no symlink modificam o canônico mas git do vault não vê diff | Lembrar: KG resolve symlinks; git registra só o link. Mudança canônica vive no destino |
| Conteúdo enorme com 1700+ linhas (ex: README do gogcli) | Edit grande pode falhar | Inserir Ver também no fim sem reescrever o corpo |

## Output mensurável

Auditoria 27/04/2026:
- Edges: 1.757 → 2.755 (+998, +57%)
- Isolados: 182 → 0
- Stubs criados pela operação: 91 (introduzidos pelo erro de templates) → 0 (após cleanup com `exists()`)
- Tempo total: ~3h (1h mapeamento, 1h scripts + execução, 1h validação + cleanup)

## Ver também

- [[CLAUDE.md]] — estratégia de busca híbrida (kg_search vs Grep)
- [[meta/audits/auditoria-busca-semantica-160426]] — auditoria anterior do KG (16/04)
- [[knowledge/concepts/credenciais-map]] — credenciais do MCP knowledge-graph
- [[memory/sessions/2026-04-27]] — sessão dessa auditoria
- [[memory/context/decisoes/2026-04]] — decisão registrada
- [[PROPAGATION.md]] — protocolo de propagação que mantém wikilinks consistentes a cada mudança
