---
name: obsidian-vault-manager
description: >
  Skill completa para gerenciar, organizar e manter vaults do Obsidian via Claude Code.
  Use SEMPRE que o usuário mencionar Obsidian, vault, cofre, notas, wikilinks, backlinks,
  MOC, Map of Content, daily notes, Zettelkasten, PARA method, frontmatter YAML,
  tags de notas, grafo de conhecimento, knowledge graph, notas órfãs, links quebrados,
  reorganizar notas, segundo cérebro, second brain, PKM, personal knowledge management,
  ou qualquer operação envolvendo arquivos .md num vault Obsidian. Também ative quando
  o usuário pedir para criar templates de notas, auditar estrutura de pastas, gerar
  índices, extrair entidades de daily notes, consolidar tags, fazer bulk rename/move
  de notas, analisar conexões entre notas, ou qualquer variação de organização de
  conhecimento pessoal. Se o usuário mencionar "minhas notas", "meu vault", "meu cofre",
  ou referenciar qualquer estrutura de pastas com arquivos Markdown — use esta skill.
---

# Obsidian Vault Manager — Claude Code Skill

> Usado por [[agents/kobe/IDENTITY|Kobe]]

Skill para operar como assistente especializado em vaults Obsidian. Você tem acesso
direto ao filesystem e deve usar as ferramentas nativas (Read, Write, Edit, Glob, Grep,
Bash) para interagir com o vault. Nunca sugira que o usuário faça manualmente o que
você pode fazer diretamente.

---

## 1. RECONHECIMENTO DO VAULT

Antes de qualquer operação, execute este checklist de reconhecimento:

### 1.1 Localizar e validar o vault

```bash
# Verificar se estamos num vault Obsidian
ls -la .obsidian/ 2>/dev/null && echo "VAULT CONFIRMADO" || echo "NÃO É UM VAULT"

# Se não estiver no vault, procurar
find ~ -maxdepth 4 -name ".obsidian" -type d 2>/dev/null | head -5
```

**REGRA ABSOLUTA:** Nunca modificar, criar ou deletar nada dentro de `.obsidian/`.
Essa pasta contém configurações do app e plugins — é território do Obsidian.

### 1.2 Mapear a estrutura existente

```bash
# Contagem de arquivos por tipo
find . -name "*.md" | wc -l
find . -name "*.canvas" | wc -l
find . -name "*.base" | wc -l

# Estrutura de pastas (2 níveis)
find . -maxdepth 2 -type d | grep -v ".obsidian" | grep -v ".git" | grep -v ".trash" | sort

# Amostra de frontmatter (primeiros 5 arquivos)
for f in $(find . -name "*.md" -not -path "./.obsidian/*" | head -5); do
  echo "=== $f ==="
  head -20 "$f"
  echo ""
done

# Tags mais usadas
grep -roh '#[a-zA-Z0-9_-]\+' --include="*.md" | sort | uniq -c | sort -rn | head -20

# Wikilinks mais referenciados
grep -roh '\[\[[^]]*\]\]' --include="*.md" | sort | uniq -c | sort -rn | head -20
```

### 1.3 Verificar proteções

```bash
# Git está inicializado?
git status 2>/dev/null && echo "GIT OK" || echo "⚠️ SEM GIT — INICIALIZAR ANTES DE EDITAR"

# Se não tem git, PARAR e avisar o usuário
```

**REGRA CRÍTICA:** Se o vault NÃO tem git inicializado, PARE e diga ao usuário:
> "Seu vault não tem controle de versão. Antes de qualquer edição, vou inicializar
> o git para que possamos reverter qualquer mudança. Posso fazer isso agora?"

Então execute:
```bash
git init
echo ".obsidian/workspace.json" >> .gitignore
echo ".obsidian/workspace-mobile.json" >> .gitignore
echo ".trash/" >> .gitignore
echo ".DS_Store" >> .gitignore
git add -A
git commit -m "backup: pre-AI snapshot $(date +%Y%m%d-%H%M%S)"
```

---

## 2. SINTAXE OBSIDIAN FLAVORED MARKDOWN

### 2.1 Wikilinks (OBRIGATÓRIO)

Obsidian usa wikilinks. NUNCA use markdown links padrão para links internos.

```markdown
# ✅ CORRETO — Sempre usar wikilinks
[[Nome da Nota]]
[[Nome da Nota|texto alternativo]]
[[Nome da Nota#Heading]]
[[Nome da Nota#^block-id]]

# ❌ ERRADO — NUNCA fazer isso para links internos
[texto](Nome%20da%20Nota.md)
[texto](./pasta/nota.md)
```

### 2.2 Embeds

```markdown
![[nota-a-embedar]]           # embed de nota inteira
![[nota#seção]]               # embed de seção
![[imagem.png]]               # embed de imagem
![[imagem.png|300]]           # imagem com largura
![[documento.pdf#page=3]]     # embed de página de PDF
```

### 2.3 Callouts

```markdown
> [!note] Título opcional
> Conteúdo do callout

> [!tip] Dica
> Texto da dica

> [!warning] Atenção
> Texto do aviso

> [!info]- Título (colapsável, fechado por padrão)
> Conteúdo colapsado

> [!question]+ Pergunta (colapsável, aberto por padrão)
> Resposta
```

Tipos disponíveis: `note`, `abstract`, `summary`, `tldr`, `info`, `todo`,
`tip`, `hint`, `important`, `success`, `check`, `done`, `question`, `help`,
`faq`, `warning`, `caution`, `attention`, `failure`, `fail`, `missing`,
`danger`, `error`, `bug`, `example`, `quote`, `cite`.

### 2.4 Tags

```markdown
# Inline
#tag-name              # no corpo da nota
#categoria/subtag      # tags aninhadas (nested tags)

# No frontmatter (formato preferido para tags semânticas)
---
tags:
  - tag-name
  - categoria/subtag
---
```

**Convenção:** tags sempre em lowercase, palavras separadas por hífen.
Nunca usar espaços, camelCase ou underscores em tags.

### 2.5 Propriedades / Frontmatter YAML

```yaml
---
title: Título Legível da Nota
created: 2026-04-11
modified: 2026-04-11
tags:
  - tag-um
  - tag-dois
aliases:
  - nome-alternativo
  - abreviação
status: draft | active | review | archived
type: note | book | person | project | meeting | moc | daily | fleeting
source: https://url-de-origem.com
related:
  - "[[Nota Relacionada 1]]"
  - "[[Nota Relacionada 2]]"
cssclasses:
  - wide-page
publish: false
---
```

**Regras de frontmatter:**
- Sempre usar `tags` (plural, formato lista YAML), nunca `tag`
- Sempre usar `created`, nunca `date` ou `created_at`
- Nunca usar nomes de propriedade capitalizados
- Datas no formato ISO: `YYYY-MM-DD`
- Nunca remover campos existentes — apenas adicionar ou atualizar
- Aliases são úteis para wikilinks: `[[abreviação]]` resolve para a nota

### 2.6 Obsidian Bases (`.base`)

Arquivos `.base` são views tabulares nativas do Obsidian (desde v1.9.10).
Preferir Bases sobre Dataview para novas consultas — são nativas e mais estáveis.

```json
{
  "headings": [
    {"heading": "Nome", "id": "name-field"},
    {"heading": "Status", "id": "status-field"},
    {"heading": "Tags", "id": "tags-field"}
  ],
  "rows": [],
  "source": "folder:01 - Projects"
}
```

### 2.7 JSON Canvas (`.canvas`)

```json
{
  "nodes": [
    {
      "id": "node-1",
      "type": "file",
      "file": "path/to/note.md",
      "x": 0, "y": 0,
      "width": 400, "height": 300
    },
    {
      "id": "node-2",
      "type": "text",
      "text": "Texto livre no canvas",
      "x": 500, "y": 0,
      "width": 300, "height": 200
    }
  ],
  "edges": [
    {
      "id": "edge-1",
      "fromNode": "node-1",
      "toNode": "node-2",
      "label": "relação"
    }
  ]
}
```

---

## 3. ESTRUTURA DE VAULT RECOMENDADA

### 3.1 Híbrido PARA + Zettelkasten + MOCs

Esta é a estrutura mais eficaz para vaults assistidos por IA:

```
vault/
├── 00 - Inbox/                    # Captura rápida, notas não processadas
├── 01 - Projects/                 # Projetos com prazo definido
│   ├── projeto-alpha/
│   └── projeto-beta/
├── 02 - Areas/                    # Responsabilidades contínuas (saúde, finanças)
│   ├── saude/
│   └── financas/
├── 03 - Resources/                # Material de referência
│   ├── books/
│   ├── people/
│   ├── tools/
│   └── concepts/
├── 04 - Permanent/                # Notas atômicas refinadas (Zettelkasten)
├── 05 - Daily/                    # Daily notes
│   └── 2026/
│       ├── 01-jan/
│       └── 02-fev/
├── 06 - Maps of Content/          # MOCs — índices temáticos
├── 07 - Templates/                # Templates de notas
├── 08 - Archives/                 # Projetos/notas inativos
├── 99 - Meta/                     # Assets, scripts, CLAUDE.md
│   └── assets/
├── CLAUDE.md                      # Instruções para Claude Code
└── .obsidian/                     # ⛔ NÃO TOCAR
```

### 3.2 Regras de nomenclatura

| Tipo de nota       | Formato do nome              | Exemplo                         |
|---------------------|-------------------------------|----------------------------------|
| Daily note         | `YYYY-MM-DD.md`              | `2026-04-11.md`                 |
| Zettelkasten       | `YYYYMMDDHHmm.md`            | `202604111430.md`               |
| Nota normal        | `titulo-descritivo.md`       | `como-funciona-webassembly.md`  |
| MOC                | `MOC - Tópico.md`            | `MOC - Machine Learning.md`    |
| Pessoa             | `Nome Completo.md`           | `Andrej Karpathy.md`           |
| Livro              | `Título do Livro.md`         | `Thinking Fast and Slow.md`    |
| Projeto            | `PRJ - Nome do Projeto.md`  | `PRJ - Redesign do Site.md`    |

**Princípio fundamental:** Nomeie arquivos como frases descritivas. O nome do arquivo
é contexto gratuito — `CAN-bus-traffic-without-DBC.md` diz muito antes de ler o conteúdo.
`untitled-48.md` não diz nada. Cada nome de arquivo economiza tokens de leitura.

### 3.3 Profundidade máxima

Mantenha no máximo **2-3 níveis de pasta**. Mais que isso aumenta consumo de tokens
e dificulta navegação. Se o path parece com `Projects/Active/Q1/Research/Sources/topic.md`,
são quatro pastas de indireção desnecessárias.

---

## 4. OPERAÇÕES COMUNS

### 4.1 Criar nota nova

Sempre incluir frontmatter YAML completo:

```bash
# Template mínimo para nota nova
cat > "03 - Resources/concepts/nome-do-conceito.md" << 'EOF'
---
title: Nome do Conceito
created: 2026-04-11
modified: 2026-04-11
tags:
  - conceito
  - area-relevante
type: note
status: draft
---

# Nome do Conceito

Conteúdo da nota aqui.

## Notas relacionadas

- [[Nota Relacionada 1]]
- [[Nota Relacionada 2]]
EOF
```

### 4.2 Mover notas com segurança

**PREFERIR Obsidian CLI** se disponível (v1.12+):

```bash
# Move e atualiza automaticamente todos os wikilinks
obsidian move file="Nota Antiga" to="01 - Projects/nome-projeto.md"
```

**Se CLI não disponível**, atualizar wikilinks manualmente:

```bash
# 1. Identificar todas as referências à nota
grep -rl '\[\[Nome Antigo\]\]' --include="*.md" .

# 2. Mover o arquivo
mv "path/antigo/Nome Antigo.md" "path/novo/Nome Novo.md"

# 3. Atualizar referências em todas as notas
find . -name "*.md" -not -path "./.obsidian/*" -exec \
  sed -i 's/\[\[Nome Antigo\]\]/\[\[Nome Novo\]\]/g' {} +

# 4. Atualizar referências com alias
find . -name "*.md" -not -path "./.obsidian/*" -exec \
  sed -i 's/\[\[Nome Antigo|/\[\[Nome Novo|/g' {} +
```

### 4.3 Auditar saúde do vault

```bash
# Notas órfãs (sem nenhum link de entrada)
echo "=== NOTAS ÓRFÃS ==="
for f in $(find . -name "*.md" -not -path "./.obsidian/*" -not -path "./.trash/*"); do
  basename="${f%.md}"
  basename="$(basename "$basename")"
  count=$(grep -rl "\[\[$basename" --include="*.md" . 2>/dev/null | grep -v "$f" | wc -l)
  if [ "$count" -eq 0 ]; then
    echo "  $f"
  fi
done

# Wikilinks quebrados (referenciando notas que não existem)
echo "=== WIKILINKS QUEBRADOS ==="
grep -roh '\[\[[^]|#]*' --include="*.md" . | sed 's/\[\[//' | sort -u | while read link; do
  found=$(find . -name "$link.md" -not -path "./.obsidian/*" 2>/dev/null | head -1)
  if [ -z "$found" ]; then
    echo "  [[${link}]] — nota não encontrada"
  fi
done

# Notas sem frontmatter
echo "=== NOTAS SEM FRONTMATTER ==="
for f in $(find . -name "*.md" -not -path "./.obsidian/*" -not -path "./.trash/*"); do
  first_line=$(head -1 "$f")
  if [ "$first_line" != "---" ]; then
    echo "  $f"
  fi
done

# Notas sem tags
echo "=== NOTAS SEM TAGS ==="
for f in $(find . -name "*.md" -not -path "./.obsidian/*" -not -path "./.trash/*"); do
  has_yaml_tags=$(head -30 "$f" | grep -c "^tags:")
  has_inline_tags=$(grep -c '#[a-zA-Z]' "$f")
  if [ "$has_yaml_tags" -eq 0 ] && [ "$has_inline_tags" -eq 0 ]; then
    echo "  $f"
  fi
done
```

### 4.4 Gerar Map of Content (MOC)

Workflow para criar um MOC sobre um tópico:

1. **Glob** para encontrar notas relevantes por pasta ou nome
2. **Grep** para encontrar notas que mencionam o tópico
3. **Read** uma amostra representativa para entender os temas
4. Agrupar notas em subcategorias semânticas
5. **Write** o MOC com wikilinks organizados por subtópico

### 4.5 Processar daily notes

```bash
# Extrair tarefas incompletas da semana
grep -rn "- \[ \]" "05 - Daily/2026/" --include="*.md" | tail -30

# Extrair tarefas completadas
grep -rn "- \[x\]" "05 - Daily/2026/" --include="*.md" | tail -30

# Encontrar menções a pessoas nas daily notes
grep -roh '\[\[.*\]\]' "05 - Daily/" --include="*.md" | sort | uniq -c | sort -rn | head -20
```

### 4.6 Bulk frontmatter update

Para operações em massa (100+ arquivos), gerar e executar um script Python é
dramaticamente mais rápido e seguro que editar arquivo por arquivo.

**Antes de executar qualquer script de bulk:** sempre fazer commit do git.

```bash
git add -A && git commit -m "backup: pre-bulk-update $(date +%Y%m%d-%H%M%S)"
python3 bulk_frontmatter.py
git diff --stat  # verificar mudanças
```

---

## 5. OBSIDIAN CLI (v1.12+)

Se o Obsidian estiver aberto e o CLI instalado, preferir estes comandos sobre
manipulação direta — eles respeitam os mecanismos internos do Obsidian.

```bash
# Verificar disponibilidade
which obsidian 2>/dev/null && echo "CLI disponível" || echo "CLI não instalado"

# Operações de arquivo (atualizam wikilinks automaticamente)
obsidian move file="Nome" to="pasta/novo-nome.md"
obsidian create file="pasta/nova-nota.md" content="# Título"

# Consultas de grafo
obsidian orphans                           # notas sem links
obsidian unresolved                        # wikilinks que não apontam para nota existente
obsidian backlinks file="Nome da Nota"     # links de entrada
obsidian outlinks file="Nome da Nota"      # links de saída

# Propriedades
obsidian property:set file="Nome" name="status" value="active"
obsidian property:get file="Nome" name="tags"

# Tags
obsidian tags                              # listar todas
obsidian tags counts sort=count            # ordenar por frequência

# Busca (mais rápida que grep — usa índice interno)
obsidian search query="machine learning"
```

**Nota:** O CLI requer o Obsidian desktop aberto (opera via IPC).
Se o Obsidian não estiver rodando, use as ferramentas nativas do filesystem.

---

## 6. PROTOCOLOS DE SEGURANÇA

### 6.1 Antes de qualquer edição em massa

```bash
# 1. SEMPRE commit antes
git add -A && git commit -m "checkpoint: $(date +%Y%m%d-%H%M%S)"

# 2. Para operações de risco (bulk move, rename, delete):
#    - Mostrar o plano ao usuário ANTES de executar
#    - Executar em batch pequeno (10 arquivos) como teste
#    - Verificar resultado do batch
#    - Só então executar no vault inteiro
```

### 6.2 Regras invioláveis

1. **NUNCA deletar notas** sem confirmação explícita do usuário
2. **NUNCA sobrescrever conteúdo** — sempre fazer append ou edit cirúrgico
3. **NUNCA modificar `.obsidian/`** — configurações do app
4. **NUNCA remover campos de frontmatter** existentes — apenas adicionar/atualizar
5. **NUNCA usar markdown links** `[text](url)` para links internos — sempre `[[wikilinks]]`
6. **NUNCA inventar conexões** — só linkar notas que genuinamente se relacionam
7. **SEMPRE preservar wikilinks** ao editar conteúdo
8. **SEMPRE validar** que arquivos referenciados existem antes de criar wikilinks
9. **SEMPRE usar UTF-8** para leitura/escrita de arquivos
10. **Em macOS:** normalizar nomes de arquivo Unicode com `NFC`

### 6.3 Quando pausar e perguntar

- Operação afeta mais de 50 arquivos
- Detectou possível conflito de naming (duas notas com nomes similares)
- Frontmatter existente tem formato inesperado
- Nota contém conteúdo que parece pessoal/sensível (diário, emails)
- Qualquer operação de delete ou replace destrutivo

---

## 7. CHECKLIST DE VALIDAÇÃO PÓS-OPERAÇÃO

Após qualquer operação significativa:

```bash
# 1. Verificar que não quebrou nada
git diff --stat

# 2. Contar links quebrados (deve ser 0 ou menor que antes)
grep -roh '\[\[[^]|#]*' --include="*.md" . | sed 's/\[\[//' | sort -u | while read link; do
  found=$(find . -name "$link.md" -not -path "./.obsidian/*" 2>/dev/null | head -1)
  [ -z "$found" ] && echo "QUEBRADO: [[$link]]"
done | wc -l

# 3. Verificar que frontmatter é válido (sem YAML malformado)
for f in $(find . -name "*.md" -not -path "./.obsidian/*" | head -50); do
  first=$(head -1 "$f")
  if [ "$first" = "---" ]; then
    # Verificar se fecha
    close=$(awk 'NR>1 && /^---$/{print NR; exit}' "$f")
    [ -z "$close" ] && echo "YAML NÃO FECHA: $f"
  fi
done

# 4. Commit se tudo OK
git add -A && git commit -m "resultado: [descrição da operação]"
```

---

## CHANGELOG

| Data | Alteração |
|------|-----------|
| 11/04/2026 | v1.0 — Criação da skill. Reconhecimento de vault, sintaxe OFM completa (wikilinks, embeds, callouts, tags, frontmatter, bases, canvas), estrutura PARA+Zettelkasten+MOC, operações comuns (criar, mover, auditar, MOC, daily notes, bulk update), Obsidian CLI v1.12+, protocolos de segurança, checklist pós-operação. |
