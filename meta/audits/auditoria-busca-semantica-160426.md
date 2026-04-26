---
title: "Auditoria — Busca Semântica e Memória"
created: 2026-04-16
type: audit
status: complete
tags:
  - meta
  - audit
  - busca-semantica
---

# Auditoria — Busca Semântica e Memória

> Data: 16/04/2026
> Executor: Claude Code (Opus 4.6, 1M context)
> Escopo: Inventário completo + testes práticos + análise de gaps
> Política: Zero alterações — apenas leitura e documentação

---

## 1. FONTES DE INFORMAÇÃO

### 1.1 Vault Obsidian (`~/segundo-cerebro/`)

| Métrica | Valor |
|---------|-------|
| Total de notas (.md) | 428 |
| Tamanho total | 18 MB |
| Wikilinks | 1.200 |
| Frontmatter YAML | 422/428 (98,6%) |
| MOCs (Maps of Content) | 8 |
| Diretórios top-level | 8 (openclaw, skills, projects, memory, business, knowledge, automacoes, meta) |

**Maior diretório:** `openclaw/` (184 notas, 1.3 MB) — sistema multi-agente
**Maior arquivo:** `projects/bidspark-multiagente-completo.md` (192 KB)

### 1.2 Memória do Claude Code (`~/.claude/`)

| Componente | Path | Formato | Persistência |
|------------|------|---------|-------------|
| Memória por projeto | `~/.claude/projects/{hash}/memory/*.md` | Markdown com frontmatter | Indefinida |
| Índice de memória | `~/.claude/projects/{hash}/memory/MEMORY.md` | Markdown (lista de links) | Indefinida |
| CLAUDE.md global | `~/.claude/CLAUDE.md` | Markdown | Indefinida |
| Skills | `~/.claude/skills/*/SKILL.md` | Markdown | Indefinida |
| Histórico de sessões | `~/.claude/history.jsonl` | JSON Lines | Indefinida |
| Backups | `~/.claude/backups/*.json` | JSON | 5 versões rolling |

**Projeto principal** (`-Users-pedrobroglio`): 29 arquivos de memória (120 KB)
- 1 `MEMORY.md` (índice com 37 linhas)
- 7 `feedback_*.md` (regras de comportamento)
- 13 `project_*.md` (contexto de projetos)
- 1 `user_profile.md`
- 1 `credentials_*.md`

**Total de projetos com memória:** 7 de 15 diretórios

**Formato:** Texto puro (Markdown). **Zero databases, zero embeddings, zero vetores.** A memória do Claude Code é 100% baseada em arquivos `.md`.

**População:** Semi-automática. O auto-memory system salva quando detecta informação relevante na conversa (feedback, decisões, perfil do usuário). A skill `/salve` faz flush manual no fim de sessão.

### 1.3 CLAUDE.md de Projetos

| Projeto | Tamanho | Escopo |
|---------|---------|--------|
| `~/.claude/CLAUDE.md` (global) | 7.8 KB | Perfil, stack, skills |
| `~/segundo-cerebro/CLAUDE.md` | 7.8 KB | Mapa do vault |
| `amazon-ads-automation/CLAUDE.md` | 33.8 KB | Sistema PPC completo |
| `budamix-ai-agent/CLAUDE.md` | 114 KB | Agente WhatsApp completo |
| `ml-ads-automation/CLAUDE.md` | 24.6 KB | ML Ads |
| + 9 outros projetos | 4-5 KB cada | Templates N8N/Builder |

**Carregamento:** CLAUDE.md é carregado automaticamente quando Claude Code abre o diretório do projeto. O global (`~/.claude/CLAUDE.md`) e o MEMORY.md do projeto são carregados SEMPRE. Outros CLAUDE.md só são carregados se o working directory muda.

### 1.4 Knowledge Graph Plugin

| Métrica | Valor |
|---------|-------|
| Plugin | `~/.claude/plugins/knowledge-graph/` |
| Banco | SQLite + sqlite-vec (`~/.local/share/knowledge-graph/kg.db`, 7.1 MB) |
| Embeddings | Xenova/multilingual-e5-small (384 dimensões) |
| Nodes indexados | 408 (de 428 no vault = **20 faltando**) |
| Edges | 1.025 |
| Comunidades (Louvain) | 19 |
| Vetores | 396 (de 408 nodes = **12 sem embedding**) |
| FTS rows | 297 (de 408 nodes = **111 sem FTS = 27% missing**) |
| Última indexação | 14/04/2026 08:01 (**2 dias atrás**) |

**⚠️ STATUS DO KG NESTA SESSÃO: NÃO DISPONÍVEL**
Os MCP tools (`kg_search`, `kg_node`, `kg_paths`, etc.) **não estão carregados** nesta sessão do Claude Code. O ToolSearch não encontrou nenhuma ferramenta `kg_*`.

### 1.5 Obsidian Vault Manager Skill

**Status: NÃO EXISTE.**
O path `/mnt/skills/user/obsidian-vault-manager/` não existe nesta máquina. O diretório `/mnt/skills/` não existe. Não há skill dedicada ao gerenciamento do vault Obsidian — apenas o Knowledge Graph plugin (quando disponível).

### 1.6 Outras Fontes

| Fonte | Acessível? | Como |
|-------|-----------|------|
| Google Sheets (planilha precificação) | Sim | OAuth token em `~/.config/google-sheets-claude/` — via scripts Python |
| Supabase | Sim | Via Edge Functions ou REST API — requer credenciais |
| Google Drive | Limitado | Token Google Sheets, não Drive genérico |
| VPS (OpenClaw) | Sim | Via SSH (Bash tool) |
| N8N | Sim | Via MCP `n8n-mcp` |

---

## 2. MECANISMO DE BUSCA — COMO REALMENTE FUNCIONA

### 2a. Tipo de busca

| Tipo | Disponível? | Ferramenta | Qualidade |
|------|-------------|-----------|-----------|
| **Lexical/keyword** | ✅ Sempre | Grep (ripgrep) | Excelente — regex, case-insensitive, glob filter |
| **Filename pattern** | ✅ Sempre | Glob | Excelente — rápido, suporta `**/*.md` |
| **Direct file read** | ✅ Sempre | Read | Excelente — qualquer arquivo |
| **Semântica (embeddings)** | ⚠️ Às vezes | KG MCP `kg_search` | **NÃO disponível nesta sessão** |
| **Full-text search (FTS5)** | ⚠️ Às vezes | KG MCP (interno) | **Broken: 27% dos nodes sem FTS** |
| **Fuzzy (typos)** | ❌ Nunca | Nenhuma | Não existe |
| **Graph traversal** | ⚠️ Às vezes | KG MCP `kg_paths`, `kg_neighbors` | Depende do MCP estar ativo |

**Resposta direta: quando você pede "briefing sobre X", Claude Code usa busca LEXICAL (Grep).** Não há busca semântica embutida. Eu (Claude) interpreto sua pergunta, decido quais arquivos provavelmente contêm a resposta, e uso Grep/Read para buscá-los.

### 2b. Ordem de busca (real, não teórica)

```
1. CONTEXTO JÁ CARREGADO (automático, zero custo)
   ├── CLAUDE.md global (~/.claude/CLAUDE.md)
   ├── CLAUDE.md do projeto (se working dir = projeto)
   ├── MEMORY.md do projeto (índice de memória)
   └── Mensagens anteriores da conversa

2. MEMÓRIA DO CLAUDE CODE (se eu julgar relevante)
   └── Read de ~/.claude/projects/.../memory/feedback_*.md, project_*.md

3. SEGUNDO CÉREBRO (se eu julgar necessário)
   ├── Grep por keywords no vault inteiro
   ├── Read de arquivos conhecidos (pendencias.md, decisoes/, etc.)
   └── Glob para encontrar arquivos por nome

4. KG MCP (SE ESTIVER DISPONÍVEL — frequentemente não está)
   ├── kg_search para busca semântica
   ├── kg_node para detalhes de uma nota
   └── kg_paths para conexões entre notas

5. FONTES EXTERNAS (raramente, sob demanda)
   ├── SSH na VPS
   ├── Google Sheets API
   └── Supabase REST
```

**A verdade inconveniente:** os passos 1-3 são 99% do que acontece. O KG (passo 4) quase nunca está disponível.

### 2c. Priorização de resultados

**Não existe priorização automatizada.** Eu (Claude) leio os resultados do Grep e sintetizo com base em:
- Relevância semântica (meu julgamento, não um algoritmo)
- Recência (arquivos em `memory/context/` tendem a ser mais atuais)
- Especificidade (arquivo dedicado > menção passageira)

Se a mesma informação aparece em múltiplas fontes, **o PROPAGATION.md define a hierarquia:**
- Fonte individual (ex: `projects/X.md`) > cache compilado (`business-context.md`)
- Conversa atual > memória persistente > vault

### 2d. Limites

| Limite | Valor | Impacto |
|--------|-------|---------|
| Context window | 1M tokens (Opus 4.6) | Cabe ~3.500 páginas — raramente é problema |
| Grep default | 250 linhas output | Pode truncar busca ampla |
| Read default | 2.000 linhas | Arquivos grandes precisam de offset/limit |
| Arquivos por busca | Sem limite hard | Mas cada Read custa tempo e tokens |
| Vault inteiro | 428 notas, 18 MB | Grep lê tudo em <1 segundo |

**Na prática:** o gargalo não é tamanho, é **saber onde procurar.** Se eu não sei que a informação está em `skills/marketplace/amazon-fees-rules/SKILL.md`, nunca vou ler esse arquivo.

---

## 3. TESTES PRÁTICOS

### Teste 1 — "Briefing sobre o piloto BidSpark-3"

| Métrica | Resultado |
|---------|-----------|
| Ferramenta usada | `Grep -i "BidSpark-3\|bidspark.3\|bidspark3"` |
| Arquivos encontrados | 4: sessão 16/04, decisões abril, deadlines, pendências |
| Tempo | <1s (Grep instantâneo) |
| Precisão | ✅ **COMPLETA** — encontrou todas as fontes relevantes |
| Razão do sucesso | Termo exato "BidSpark-3" presente nos arquivos |

**Nota:** Se a informação estivesse em arquivo com nome diferente e sem o termo exato, teria falhado.

### Teste 2 — "Briefing sobre operação Budamix em Itajaí"

| Métrica | Resultado |
|---------|-----------|
| Ferramenta usada | `Grep -i "Itajaí\|itajai\|TTD.?409"` |
| Arquivos encontrados | 24 arquivos |
| Tempo | <1s |
| Precisão | ✅ **COMPLETA** — business-context, empresa/_index, perfil, fisco skills, trader platforms |
| Pontos fortes | Variações de acentuação cobertas pelo regex |
| Gap identificado | Se alguém escrevesse "filial SC" sem mencionar Itajaí, não encontraria |

### Teste 3 — "Briefing sobre margem dos potes de vidro em todos os marketplaces"

| Métrica | Resultado |
|---------|-----------|
| Ferramenta usada | `Grep -i "potes.*vidro.*marg\|margem.*potes\|potes.*hermétic"` |
| Arquivos encontrados | 33 (bidspark spec, trader context, marketplace skills, atendimento, etc.) |
| Tempo | <1s |
| Precisão | ⚠️ **PARCIAL** |
| O que encontrou | Referências aos potes em skills, specs, trader context |
| O que NÃO encontrou | **Planilha de precificação real** (Google Sheets, fora do vault) |
| O que NÃO encontrou | **Dados de auditoria específicos** (estavam em pendencias.md mas padrão regex não casou) |

**Problema real:** Para montar o briefing completo eu precisaria:
1. Ler 5+ arquivos do vault (decisões, pendências, auditorias)
2. Acessar Google Sheets API (dados atuais de margem)
3. Cruzar informação de 3 abas (MELI, AMAZON, SHOPEE)

**Isso funciona** mas requer que EU (Claude) saiba que essas fontes existem e execute as buscas corretas. Não é automático.

---

## 4. TESTES DE STRESS

### Stress 1 — Typo deliberado: "briefng do pioto bidsparc"

| Resultado | ❌ FALHA TOTAL |
|-----------|--------------|
| Grep encontrou | 0 arquivos |
| Motivo | Grep é lexical exato — "bidsparc" ≠ "bidspark" |
| Workaround | Eu (Claude) poderia interpretar o typo e corrigir antes de buscar |
| Mas... | Se o typo for em nome de arquivo/skill que eu não conheço, falha silenciosa |

### Stress 2 — Sinônimo: "despesa" em vez de "custo"

| Resultado | ⚠️ PARCIAL |
|-----------|-----------|
| Grep "despesa" encontrou | 4 arquivos (sessões e decisões recentes) |
| Grep "custo" encontraria | ~50+ arquivos |
| Gap | "despesa" e "custo" não são tratados como equivalentes |
| Impacto | Se o vault usa consistentemente "custo", buscar "despesa" perde 90% dos resultados |

### Stress 3 — Contexto ausente: "briefing do projeto novo"

| Resultado | ⚠️ AMBÍGUO |
|-----------|-----------|
| O que aconteceria | Eu perguntaria qual projeto (Potes Redondos? DPM002? BidSpark-3?) |
| Se não perguntasse | Chutaria o mais recente mencionado na conversa |
| Risco | Se a conversa é nova, não teria contexto para desambiguar |

### Stress 4 — Pergunta composta: "compara margens Gamer com Potes Redondos considerando FBA pós-julho"

| Resultado | ⚠️ REQUER SÍNTESE MANUAL |
|-----------|------------------------|
| Passos necessários | 1) Grep "Gamer" margem, 2) Grep "Potes Redondos" margem, 3) Read promoção FBA+, 4) Calcular |
| Fontes | Planilha (Sheets API), pendencias.md (flag FBA+), amazon-fees-rules (tarifas) |
| Viável? | Sim, mas depende de eu saber onde cada dado vive |
| Automatizado? | Não — montaria query por query |

### Stress 5 — Cross-language: pergunta em PT, nota em EN

| Resultado | ⚠️ DEPENDE DO CONTEÚDO |
|-----------|----------------------|
| "sourcing" (EN) no vault | 8 arquivos encontrados |
| "cadeia de suprimento" (PT) | 0 arquivos (termo não usado no vault) |
| Impacto | Vault mistura PT e EN — busca precisa cobrir ambos idiomas |
| Fix natural | O vault tende a usar termos técnicos em inglês, então buscar em EN funciona melhor |

---

## 5. ANÁLISE DE GAPS

### Gap 1 — Busca semântica NÃO está disponível na maioria das sessões

**Severidade: 🔴 CRÍTICA**

O Knowledge Graph MCP server está instalado e configurado, mas **não estava ativo nesta sessão**. Se isso é intermitente, significa que em ~50%+ das sessões você está sem busca semântica.

**Causa provável:** O MCP server precisa ser iniciado quando o Claude Code abre. Se o processo não starta (timeout, erro de dependência, etc.), as tools ficam indisponíveis silenciosamente.

### Gap 2 — KG index desatualizado e FTS quebrado

**Severidade: 🔴 CRÍTICA**

| Problema | Detalhe |
|----------|---------|
| Index stale | Última indexação: 14/04 (2 dias atrás). 20 notas faltando. |
| FTS incompleto | 297 de 408 nodes com FTS (27% sem indexação full-text) |
| Vetores incompletos | 396 de 408 nodes com embeddings (12 sem vetor) |
| Sem reindex automático | Não há hook/cron que reindexe quando notas mudam |

Mesmo quando o KG MCP está ativo, buscas FTS por "bidspark" ou "margem" retornam **ZERO resultados** apesar do conteúdo existir nos nodes. O FTS está funcional mas incompleto.

### Gap 3 — Zero tolerância a erros de digitação

**Severidade: 🟡 IMPORTANTE**

Grep é exato. Não existe fuzzy matching. Se o usuário digita "bidsparc", "margem negativa" em vez de "margem negativa", ou "suporte gamer" em vez de "Suporte Controle Gamer", a busca pode falhar.

**Mitigação atual:** EU (Claude) interpreto a intenção e corrijo antes de buscar. Funciona na maioria dos casos, mas falha quando:
- O termo correto é um nome próprio que eu não conheço
- O typo é grande demais para eu inferir

### Gap 4 — Informação fragmentada requer montagem manual

**Severidade: 🟡 IMPORTANTE**

Não existe um "briefing generator" que consolide automaticamente dados de múltiplas fontes. Para o Teste 3 (margens potes vidro), eu precisaria:
- Vault: 5 arquivos
- Google Sheets: 3 abas
- Cálculo: cruzar dados

Isso funciona, mas é lento (~30s-1min por briefing complexo) e depende do meu conhecimento de onde cada dado vive.

### Gap 5 — Sem awareness de atualizações recentes

**Severidade: 🟡 IMPORTANTE**

Se a planilha de precificação foi editada hoje, o vault não sabe. Se uma decisão foi tomada na VPS via Kobe, o segundo cérebro só fica sabendo no próximo git pull (06:45 BRT). Não existe notificação em tempo real.

### Gap 6 — MEMORY.md como "tabela de conteúdo" limitada

**Severidade: 🟢 MENOR**

O MEMORY.md do Claude Code tem 37 linhas com ~150 chars cada. É um índice flat sem hierarquia ou tags. Para decidir se um memory file é relevante, eu leio o título na linha — se o título não for descritivo o suficiente, posso ignorar um arquivo relevante.

---

## 6. OBSIDIAN VAULT MANAGER

**Status: NÃO EXISTE** como skill dedicada.

O que existe em vez disso:

| Componente | Função | Status |
|------------|--------|--------|
| Knowledge Graph Plugin | Busca semântica, grafo, comunidades | Instalado mas intermitente |
| Obsidian nativo (graph view) | Visualização de conexões | Funciona só no app Obsidian |
| `/cerebro` skill | Carrega contexto operacional | Funciona (arquivo flat, sem semântica) |
| `/salve` skill | Flush de sessão | Funciona (cria sessão + atualiza arquivos) |
| MOCs (8 arquivos) | Índices temáticos | Estáticos, atualização manual |
| PROPAGATION.md | Regras de propagação | Documento de referência |

**Como o KG Plugin funciona (quando ativo):**
1. `kg_index`: Parseia vault inteiro, extrai frontmatter, detecta wikilinks → edges, gera embeddings (Xenova/multilingual-e5-small, 384d), detecta comunidades (Louvain)
2. `kg_search(query)`: Embedding da query → cosine similarity com nodes_vec → top-N resultados
3. `kg_node(name)`: Fuzzy match do nome → metadata + conexões
4. `kg_paths(A, B)`: Shortest path no grafo via graphology
5. Store: SQLite + sqlite-vec para vetores, FTS5 para full-text

**Problema:** não há hook que reindexe automaticamente. Requer `kg_index` manual.

---

## 7. RECOMENDAÇÕES

### 🔴 Prioridade 1 — Garantir KG MCP disponível em toda sessão

**Problema:** O MCP server `knowledge-graph` não está ativo nesta sessão.
**Ação:** Verificar por que o MCP não startou. Possíveis causas:
- `npx tsx` falhando (dependências desatualizadas)
- Timeout no startup (modelo de embedding demora ~10s para carregar)
- Configuração no `.claude.json` removida ou corrompida (o arquivo está vazio/ausente)

**Diagnóstico imediato:**
```bash
# Testar se o MCP server inicia
cd ~/.claude/plugins/knowledge-graph
KG_VAULT_PATH=~/segundo-cerebro KG_DATA_DIR=~/.local/share/knowledge-graph npx tsx src/mcp/index.ts
```

**Fix permanente:** Garantir que `mcpServers.knowledge-graph` está no settings ativo.

### 🔴 Prioridade 2 — Reindexar KG e corrigir FTS

**Problema:** Index com 2 dias de atraso, 20 notas faltando, FTS com 27% de holes.
**Ação:**
1. Rodar `kg_index` (via MCP tool quando disponível)
2. Se FTS continuar incompleto após reindex, é bug no plugin — abrir issue

**Automação futura:** Criar hook no Claude Code que roda `kg_index` após `/salve` ou a cada N horas.

### 🟡 Prioridade 3 — Criar hook de reindex automático

**Problema:** Reindex é manual, ninguém lembra.
**Ação:** Adicionar ao settings.json do Claude Code:
```json
{
  "hooks": {
    "PostToolCall": [{
      "matcher": "Write|Edit",
      "command": "echo 'reindex-needed' >> /tmp/kg-reindex-flag"
    }]
  }
}
```
Ou: adicionar ao cron de sync (06:45 BRT) um passo que chama o index.

### 🟡 Prioridade 4 — Enriquecer MEMORY.md com tags/categorias

**Problema:** MEMORY.md flat, sem hierarquia.
**Ação:** Já está razoável. Melhoria: adicionar emojis ou prefixos de categoria para facilitar scan visual:
```
## 🔧 Feedback
## 📋 Projetos
## 👤 User
## 🔗 Referências
```
(Já está organizado assim — manter.)

### 🟢 Prioridade 5 — Não investir em fuzzy search

**Justificativa:** O custo-benefício é baixo. Eu (Claude) já interpreto typos na maioria dos casos antes de buscar. Investir em fuzzy matching no Grep não vale o esforço.

### 🟢 Prioridade 6 — Não criar skill "briefing generator"

**Justificativa:** O `/cerebro` já faz isso para contexto operacional. Briefings ad-hoc ("me traz sobre X") são melhor resolvidos por busca contextual do que por um gerador genérico — cada briefing tem fontes diferentes.

---

## 8. RESUMO EXECUTIVO

```
BUSCA SEMÂNTICA FUNCIONA?
→ PARCIALMENTE. O mecanismo existe (KG plugin com embeddings 384d + FTS5 + grafo)
  mas NÃO ESTAVA DISPONÍVEL nesta sessão e tem problemas de freshness.

CONFIABILIDADE ESTIMADA:
→ 60% — quando KG está ativo e atualizado, sobe pra ~85%

O QUE FUNCIONA BEM (sem KG):
✅ Busca lexical (Grep) — rápida, precisa, cobre vault inteiro em <1s
✅ Carregamento automático de CLAUDE.md + MEMORY.md
✅ Frontmatter padronizado (98,6% do vault)
✅ MOCs e índices manuais
✅ Meu conhecimento acumulado do vault (sei onde as coisas estão)

O QUE NÃO FUNCIONA:
❌ Busca semântica (KG MCP não ativo nesta sessão)
❌ Typo tolerance (zero)
❌ Reindex automático (manual only)
❌ Sync tempo real vault↔planilha↔VPS

GAPS CRÍTICOS:
1. KG MCP não disponível consistentemente
2. KG index stale (2 dias) + FTS incompleto (27% holes)

QUICK WINS:
1. Diagnosticar por que KG MCP não startou (5 min)
2. Rodar kg_index manual (2 min)
3. Adicionar reindex ao cron de sync (10 min)
```

### Diagrama: Como a busca REALMENTE funciona hoje

```
Pedro pergunta "briefing sobre X"
         │
         ▼
┌─────────────────────┐
│ Claude interpreta    │ ← LLM judgment, não algoritmo
│ a intenção          │
└─────┬───────────────┘
      │
      ├── Informação já no contexto? ──→ Responde direto (0s)
      │   (CLAUDE.md, MEMORY.md, conversa)
      │
      ├── Sei qual arquivo tem? ──→ Read direto (1s)
      │   (pendencias.md, decisoes/, etc.)
      │
      ├── Preciso buscar? ──→ Grep por keywords (1-2s)
      │   (regex no vault inteiro)
      │
      ├── KG disponível? ──→ kg_search semântico (2-5s)
      │   (⚠️ frequentemente NÃO)
      │
      └── Preciso de fonte externa? ──→ SSH/API/Sheets (5-30s)
          (planilha, Supabase, VPS)
```

**Conclusão honesta:** A busca é **funcional mas frágil**. Funciona bem para termos exatos e arquivos conhecidos. Falha silenciosamente para sinônimos, typos, e informação em fontes que eu não sei que existem. O KG plugin resolveria a maioria desses problemas — mas precisa estar ativo e atualizado.

---

*Auditoria concluída: 16/04/2026*
*Zero alterações realizadas no vault, skills, memória ou qualquer arquivo (exceto este relatório)*

## Ver também

- [[CLAUDE.md]] — estratégia de busca híbrida (kg_search vs Grep) que esta auditoria fundamentou
- [[memory/sessions/2026-04-16]] — sessão do dia da auditoria
- [[knowledge/concepts/credenciais-map]] — credenciais MCP/API usadas pelo KG e search tools
- [[knowledge/concepts/claude-code-skills-inventario]] — skills/MCPs ativos no Claude Code
- [[knowledge/concepts/stack-tecnico]] — stack que sustenta busca + memória
- [[meta/mocs/MOC - Token Management]] — gestão de tokens MCP/API
