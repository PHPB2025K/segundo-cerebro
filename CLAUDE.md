# segundo-cerebro — Vault Obsidian Unificado

Vault centralizado do Pedro Broglio. Contém: infraestrutura do sistema multi-agente OpenClaw, skills do Claude Code, referências de negócios (Budamix/GB Importadora), projetos de código, automações, e conhecimento pessoal.

## Mapa do Vault

```
segundo-cerebro/
├── openclaw/              ← Sistema multi-agente OpenClaw
│   ├── agents/            ← 6 agentes: kobe, builder, trader, spark, fisco, rh
│   │   └── */IDENTITY.md  ← Quem é, personalidade, regras
│   │   └── */SKILL.md     ← Skills específicas do agente
│   │   └── */memory/      ← Sessões e contexto do agente
│   └── system/            ← Briefings de sistema, configs globais
├── skills/                ← TODAS as skills do Claude Code
│   ├── marketplace/       ← ML, Amazon, Shopee (fees, listing, precificação)
│   ├── financeiro/        ← Stripe, extratos, gestão financeira
│   ├── design/            ← Design system, identidade visual
│   ├── dev/               ← Fullstack, debugging, código
│   ├── superpowers/       ← Skills avançadas (systematic-debugging, etc)
│   ├── marketing/         ← Conteúdo, anúncios, tráfego
│   ├── n8n/               ← 🔗 symlinks → ~/.claude/skills/n8n-*
│   ├── lovable/           ← 🔗 symlinks → ~/.claude/skills/lovable-*
│   ├── pessoal/           ← 🔗 symlinks → ~/.claude/skills/cerebro, salve
│   └── [projeto]/         ← 🔗 symlinks → skills de cada projeto
├── business/              ← Referências operacionais (notas-índice)
│   ├── importacao/        ← 471 arqs em ~/Documents/01-Importacao/
│   ├── marketplaces/      ← 56 arqs em ~/Documents/02-Marketplaces/
│   ├── financeiro/        ← 112 arqs em ~/Documents/03-Financeiro/
│   ├── empresa/           ← 124 arqs em ~/Documents/04-Empresa/
│   └── marketing/         ← 20 arqs em ~/Documents/07-Conteudo-Marketing/
├── projects/              ← Fichas de projeto (1 nota por projeto)
├── memory/                ← Contexto operacional
│   ├── context/           ← Pendências, decisões mensais, pessoas
│   ├── sessions/          ← Logs de sessão
│   └── people/            ← Notas de pessoas
├── knowledge/             ← Conhecimento pessoal e referências
│   ├── pessoal/           ← História, memórias (Trades Up, Tobias)
│   ├── concepts/          ← Conceitos, stack técnico, credenciais
│   └── corrida/           ← Coaching de corrida
├── automacoes/            ← Prompts e fluxos automatizados
│   ├── atendimento/       ← System prompts de atendimento WhatsApp
│   ├── sops/              ← SOPs (deploy, listing Amazon/Shopee, pagamento, senha, importação, OpenClaw agent)
│   ├── workflows/         ← Fichas detalhadas de workflows N8N (Gmail, Running Coach, Ana, Estoque)
│   ├── crons-index.md     ← Índice de todos os crons OpenClaw
│   ├── n8n-workflows/     ← Referências de workflows N8N (legado)
│   └── system-prompts/    ← Prompts de sistema
└── meta/                  ← Infraestrutura do vault
    ├── mocs/              ← Maps of Content (índices temáticos)
    ├── templates/         ← Templates de notas
    ├── audits/            ← Auditorias de saúde do vault
    └── scripts/           ← Scripts de manutenção
```

## Como Achar Coisas

### Por tipo de conteúdo
```bash
# Agente específico
find openclaw/agents/kobe/ -name "*.md"

# Todas as skills de um domínio
find skills/marketplace/ -name "*.md"

# Skills de um projeto específico
find skills/[nome-projeto]/ -name "*.md"

# Decisões
find memory/context/decisoes/ -name "*.md"

# Sessões de um agente
find openclaw/agents/*/memory/sessions/ -name "*.md"

# MOCs
find meta/mocs/ -name "*.md"

# Fichas de projeto
find projects/ -name "*.md"
```

### Por conteúdo (grep)
```bash
# Buscar por conceito em todo o vault
grep -rli "precificação\|pricing" --include="*.md" .

# Buscar por tag no frontmatter
grep -rl "tags:" --include="*.md" . | xargs grep "business/importacao"

# Buscar por tipo de nota
grep -rl "type: skill" --include="*.md" .

# Buscar por domínio
grep -rl "domain: marketplace" --include="*.md" .

# Buscar por agente
grep -rl "agent: trader" --include="*.md" .

# Notas sem backlinks (órfãs)
for f in $(find . -name "*.md" -not -path "./.obsidian/*" -not -type l); do
  bn="$(basename "${f%.md}")"; 
  [ "$(grep -rli "\[\[$bn" --include="*.md" . | grep -v "$f" | wc -l)" -eq 0 ] && echo "$f"
done
```

## Aliases e Referências Rápidas

| Referência | Path |
|------------|------|
| Kobe / orquestrador | `openclaw/agents/kobe/IDENTITY.md` |
| Builder | `openclaw/agents/builder/IDENTITY.md` |
| Trader | `openclaw/agents/trader/IDENTITY.md` |
| Spark | `openclaw/agents/spark/IDENTITY.md` |
| Fisco | `openclaw/agents/fisco/IDENTITY.md` |
| RH | `openclaw/agents/rh/IDENTITY.md` |
| GB Importadora | `business/importacao/_index.md` |
| **Estratégia fiscal GB (v2.0 — 90/10)** | **`business/importacao/estrategia-fiscal-gb.md`** |
| Budamix | `business/empresa/_index.md` |
| Precificação | `skills/marketplace/` (ML, Amazon, Shopee) |
| Pendências | `memory/context/pendencias.md` |
| Decisões do mês | `memory/context/decisoes/2026-04.md` |
| MOCs | `meta/mocs/` |

## Regra fiscal — GB Importadora (modelo 90/10)

Fonte única da verdade fiscal da GB: [[business/importacao/estrategia-fiscal-gb]].

- Transferência Matriz(SC)→Filial(SP) = **90% fixo** (CFOP 6.152)
- 10% retido contábil na Matriz SC → B2B com TTD 409 (ICMS efetivo 2,6%)
- Estoque físico 100% em Pedreira-SP
- Margem interna fixa = 5% (preço = custo × 1,05)
- Proporções entre os 3 CNPJs Simples (GB Comércio, Trades, Broglio) são dinâmicas, recalculadas a cada importação com base nos últimos 3 meses
- PDF oficial assinável: `business/importacao/estrategia-fiscal-gb-v2.0.pdf`

Vigente desde 29/03/2026 (decisão validada com Suellen/FOUR). Substitui o modelo anterior (transferência 100%).

## Convenções

- **Wikilinks:** Sempre `[[wikilink]]`, nunca `[text](url)` para links internos
- **Frontmatter:** YAML obrigatório em toda nota. Campos: title, created, type, status, tags
- **Tags:** Hierárquicas com `/` — `#agent/kobe`, `#skill/marketplace`, `#business/importacao`
- **Naming:** kebab-case para notas, UPPERCASE para arquivos de identidade (IDENTITY, SKILL, SOUL)
- **Notas-índice:** Arquivos `_index.md` são índices de referência que apontam para ~/Documents/
- **Symlinks:** Pastas em `skills/n8n/`, `skills/lovable/`, `skills/pessoal/`, `skills/[projeto]/` são symlinks
- **Business:** Vault guarda referências (notas MD), não arquivos brutos (PDFs, planilhas ficam em ~/Documents/)
- **Projetos:** Código fica em `~/Documents/05-Projetos-Codigo/`. Vault tem fichas em `projects/`

## Contexto do Pedro

- **Empresas:** Budamix (produtos para casa/decoração) + GB Importadora (importação China)
- **Marketplaces:** Mercado Livre, Amazon, Shopee — venda direta e B2B
- **Stack:** Next.js, Python, N8N, Supabase, Vercel
- **VPS:** 187.77.237.231 — roda OpenClaw (sistema multi-agente)
- **Background:** Ex-Trades Up (assessoria importação), experiência com sourcing Alibaba

## Knowledge Graph

Plugin de busca semântica e análise de grafo instalado.

### Operações disponíveis (via MCP ou CLI)

| Comando | O que faz |
|---------|-----------|
| `kg_search` | Busca semântica por significado (embeddings 384d) |
| `kg_node` | Lookup de nota com metadata + conexões |
| `kg_paths` | Caminhos entre duas notas no grafo |
| `kg_common` | Conexões compartilhadas entre duas notas |
| `kg_neighbors` | Vizinhança N-hops de uma nota |
| `kg_subgraph` | Extrair subgrafo local |
| `kg_communities` | Detectar clusters temáticos (Louvain) |
| `kg_bridges` | Nós ponte entre clusters (betweenness centrality) |
| `kg_central` | Nós mais centrais (PageRank) |

### Quando usar

- **Buscar por significado:** `kg_search("importação China custo")` — encontra notas relacionadas mesmo sem keyword match
- **Descobrir conexões:** `kg_paths("nota-A", "nota-B")` — como duas notas se conectam
- **Encontrar clusters:** `kg_communities` — quais grupos temáticos existem
- **Identificar hubs:** `kg_central` — notas mais importantes do grafo
- **Reindexar:** Após mudanças grandes, rodar `kg-index` no terminal
