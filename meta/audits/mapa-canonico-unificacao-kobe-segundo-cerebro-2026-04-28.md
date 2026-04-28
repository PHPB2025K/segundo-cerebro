# Mapa Canônico — Unificação Kobe ↔ Segundo Cérebro

_Gerado em: 2026-04-28 06:32 BRT_

## Objetivo

Definir, antes de qualquer migração, qual será a fonte canônica de cada classe de arquivo quando o repo `PHPB2025K/segundo-cerebro` passar a ser a fonte única de verdade para Claude Code local + OpenClaw/Kobe.

Esta fase NÃO migra conteúdo e NÃO altera runtime. Ela apenas define o mapa e as regras para a Fase 3.

---

## Princípio central

O repo `segundo-cerebro` será o único repositório canônico.

Dentro dele haverá duas camadas distintas:

1. **Camada global do vault** — conhecimento, projetos, contexto e memória acessíveis por Claude Code/Obsidian/qualquer agente.
2. **Camada runtime OpenClaw** — arquivos que o OpenClaw/Kobe precisa carregar para operar como agente.

Regra: nenhum conteúdo durável deve depender exclusivamente de `/root/.openclaw/workspace` depois da virada.

---

## Estrutura canônica final

```text
segundo-cerebro/
├── CLAUDE.md                                  # entrada principal do Claude Code local
├── memory/                                    # memória global do segundo cérebro
│   ├── context/
│   │   ├── pendencias.md                      # pendências globais canônicas
│   │   ├── decisoes/                          # decisões globais por período/tema
│   │   ├── lessons.md                         # lições globais consolidadas
│   │   ├── people.md                          # pessoas/contatos globais
│   │   └── business-context.md                # contexto de negócio global
│   ├── sessions/                              # sessões globais Claude/local/Kobe consolidadas
│   └── projects/                              # projetos globais
├── openclaw/
│   └── agents/
│       ├── kobe/                              # runtime/memória específica do Kobe
│       │   ├── SOUL.md
│       │   ├── AGENTS.md
│       │   ├── IDENTITY.md
│       │   ├── USER.md
│       │   ├── MEMORY.md
│       │   ├── TOOLS.md
│       │   ├── memory/                        # memória operacional específica do Kobe/OpenClaw
│       │   └── shared/                        # workspaces compartilhados sob orquestração do Kobe
│       ├── trader/
│       ├── spark/
│       ├── builder/
│       ├── fisco/
│       └── rh/
├── agents/                                    # camada Obsidian/agent docs se usada por Claude local
├── skills/                                    # skills canônicas
├── automacoes/
├── knowledge/
├── business/
├── projects/
└── meta/
```

---

## Mapa canônico por classe

| Classe | Origem atual Kobe | Destino canônico no `segundo-cerebro` | Regra Fase 3 |
|---|---|---|---|
| Core Kobe | `SOUL.md`, `AGENTS.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`, `TOOLS.md` | `openclaw/agents/kobe/*.md` | Merge semântico. Preservar conteúdo mais recente do Kobe e wikilinks/frontmatter/estrutura do vault. |
| Memória operacional Kobe | `memory/` | `openclaw/agents/kobe/memory/` | Copiar/mergear como memória específica do agente. Não confundir com `memory/` global. |
| Pendências globais | `memory/pending.md` | `memory/context/pendencias.md` | Fundir item a item. Remover resolvidas. Manter origem/data quando possível. |
| Decisões globais | `memory/context/decisions.md` | `memory/context/decisoes/2026-04.md` e/ou arquivos por período | Converter decisões permanentes em formato do vault, mantendo rastreabilidade. |
| Lições | `memory/context/lessons.md` | `memory/context/lessons.md` + `openclaw/agents/kobe/memory/context/lessons.md` se necessário | Lições estratégicas globais no vault; lições operacionais do Kobe no agente. |
| Pessoas | `memory/context/people.md` | `memory/context/people.md` | Merge único, sem duplicar contatos. |
| Contexto de negócio | `memory/context/business-context.md` | `memory/context/business-context.md` | Merge semântico, preservar wikilinks do vault e números atualizados do Kobe. |
| Projetos Kobe | `memory/projects/` | `openclaw/agents/kobe/memory/projects/` e/ou `memory/projects/` | Projetos de negócio vão para global; notas internas do Kobe ficam no agente. |
| Sessões Kobe antigas | `memory/*.md` e `memory/sessions/*.md` | `openclaw/agents/kobe/memory/` + `memory/sessions/` quando relevantes globalmente | Manter histórico bruto no agente; promover só resumo/decisão/pendência para global. |
| Feedbacks | `memory/feedback/` | `openclaw/agents/kobe/memory/feedback/` | Manter como memória operacional do Kobe; só promover padrões globais se necessário. |
| Integrações | `memory/integrations/` | `openclaw/agents/kobe/memory/integrations/` + docs globais em `knowledge/` se necessário | Evitar expor credenciais. Mapas operacionais ficam no agente. |
| Tasks pending | `memory/tasks-pending.md` | `openclaw/agents/kobe/memory/tasks-pending.md` + itens acionáveis em `memory/context/pendencias.md` | Não perder tarefas abertas; separar backlog operacional vs pendência global. |
| Skills | `skills/` | `skills/` | Como só 1 arquivo diverge, resolver diff pontual e manter `segundo-cerebro/skills/` canônico. |
| Shared agents | `shared/` | `openclaw/agents/kobe/shared/` | Merge por agente. Sessões recentes do Kobe entram; índices do vault preservados. |
| Agentes independentes | `shared/{trader,spark,builder,fisco,rh}` e/ou `/root/.openclaw/workspaces/*` | `openclaw/agents/{trader,spark,builder,fisco,rh}/` | Consolidar em `openclaw/agents/*`; evitar duplicar em `shared/` salvo quando for contexto do Kobe. |
| Automação/scripts operacionais | `scripts/`, `integrations/` | NÃO migrar tudo automaticamente | Só scripts documentais/SOPs entram. Tokens, logs e credenciais ficam fora. |
| Logs/tokens/cache | `logs/`, tokens, `.dreams/events.jsonl`, OAuth files | Não canônico no vault | Não migrar para Git. Se houver insight, registrar resumo seguro. |
| Budamix e-commerce repo | `budamix-ecommerce/` | Continua repo/projeto próprio | Não trazer código inteiro para o segundo cérebro. Apenas docs/contexto/links. |
| Backups antigos | `backups/` | Não migrar | Preservar no workspace legado até arquivamento; não poluir vault. |

---

## Decisões canônicas específicas

### 1. `segundo-cerebro/memory/` é memória global

Esse diretório não deve virar cópia literal do `Kobe memory/`.

Ele deve conter o que é útil para qualquer ambiente:

- pendências globais
- decisões
- lições estratégicas
- pessoas
- contexto de negócio
- sessões globais relevantes
- projetos de negócio

### 2. `openclaw/agents/kobe/memory/` é memória operacional do Kobe

Aqui entra o histórico completo e operacional que hoje vive em `/root/.openclaw/workspace/memory/`.

Isso permite que o OpenClaw continue tendo profundidade operacional sem poluir a camada global do vault.

### 3. `openclaw/agents/kobe/*.md` substitui os core files da raiz do workspace

Depois da virada, os arquivos da raiz do workspace atual devem ser derivados/cópia de runtime, não fonte de verdade.

### 4. Skills são simples

Como `skills/` tem 270 arquivos iguais e apenas 1 divergente, a Fase 3 deve resolver somente:

- `skills/marketplace/ml-fees-rules/SKILL.md`

Depois disso, `segundo-cerebro/skills/` vira fonte canônica.

### 5. Shared/agentes exigem merge cuidadoso

`shared/` tem muitas divergências porque carrega sessões e memória dos agentes. A regra é:

- preservar sessões recentes que só existem no Kobe
- preservar índices `_sessions-index.md` do vault
- não sobrescrever `MEMORY.md`, `SOUL.md`, `AGENTS.md` dos agentes sem diff semântico

---

## Ordem recomendada para Fase 3

1. Criar backup/tag antes da migração.
2. Resolver core files do Kobe (`SOUL`, `AGENTS`, `IDENTITY`, `USER`, `MEMORY`, `TOOLS`).
3. Fundir memória de contexto global:
   - pendências
   - decisões
   - lições
   - pessoas
   - business-context
4. Copiar/mergear memória operacional completa do Kobe para `openclaw/agents/kobe/memory/`.
5. Resolver projetos e integrações.
6. Resolver shared/agentes.
7. Resolver única divergência de skills.
8. Validar com diff final.
9. Só depois preparar Fase 4 de runtime.

---

## Regras de merge para Fase 3

- Nunca usar `rsync --delete`.
- Nunca escolher automaticamente pelo arquivo mais novo.
- Nunca sobrescrever arquivos com wikilinks/frontmatter do vault sem preservar a estrutura.
- Arquivo de memória recente do Kobe tem prioridade para conteúdo factual recente.
- Arquivo do segundo cérebro tem prioridade para organização, wikilinks, frontmatter e estrutura de vault.
- Pendência resolvida não deve voltar como aberta.
- Decisão permanente deve ser preservada mesmo que apareça só no Kobe.
- Credenciais, tokens, logs brutos e arquivos OAuth não entram no vault.
- Se o conflito for semântico, gerar seção `CONFLITO_A_RESOLVER` em vez de decidir no escuro.

---

## Checklist de aceite da Fase 2

- [x] Definido que `segundo-cerebro` é repo único canônico.
- [x] Separada camada global do vault vs camada runtime OpenClaw.
- [x] Definido destino de core files do Kobe.
- [x] Definido destino de memória operacional do Kobe.
- [x] Definido destino de pendências/decisões/lições globais.
- [x] Definido destino de skills.
- [x] Definido destino de shared/agentes.
- [x] Definidas regras de merge para Fase 3.

---

## Próximo passo

Executar Fase 3 como migração controlada/consolidação, começando por backup/tag e core files. A Fase 3 deve produzir commits pequenos por bloco, para permitir rollback granular.
