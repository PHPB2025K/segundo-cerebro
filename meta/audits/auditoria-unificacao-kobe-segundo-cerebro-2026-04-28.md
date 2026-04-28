# Auditoria Fase 1 — Unificação Kobe ↔ Segundo Cérebro
_Gerado em: 2026-04-28 06:29 BRT_
## Escopo
Auditoria read-only da divergência entre o workspace atual do Kobe/OpenClaw e o repo `segundo-cerebro`. Nenhuma configuração de runtime foi alterada e nenhuma migração foi aplicada.
## Estado dos repositórios
- Kobe workspace HEAD: `494979c 2026-04-28 05:01:25 +0000 org: manutenção noturna 2026-04-28 🌙`
- Segundo cérebro HEAD: `7670fb7 2026-04-27 05:07:03 +0000 kobe-auto: sync memory 2026-04-27T05:07Z`
- Status Kobe workspace:
```
M integrations/shopee/.shopee-tokens-budamix-shop.json
 M integrations/shopee/.shopee-tokens-budamix-store.json
 M integrations/shopee/.shopee-tokens-budamix-store2.json
 M integrations/shopee/.shopee-tokens.json
 M integrations/shopee/shopee_oauth.log
 M memory/.dreams/events.jsonl
 M memory/.dreams/short-term-recall.json
 M memory/core-audit-snapshot.tsv
 M scripts/bling-oauth/failures.json
 M scripts/bling-oauth/tokens-matriz.json
?? memory/2026-04-28-blog-fix.md
```
- Status segundo cérebro antes deste relatório: limpo.
## Arquivos core
| Arquivo | Kobe existe | Segundo cérebro existe | Hash Kobe | Hash cérebro | Linhas Kobe | Linhas cérebro | Estado |
|---|---:|---:|---|---|---:|---:|---|
| `SOUL.md` | True | True | `fd5b5f52bfa3` | `e424ec56da45` | 193 | 202 | **diferente** |
| `AGENTS.md` | True | True | `d966fcbd7ca4` | `b5a9feeefd4e` | 443 | 453 | **diferente** |
| `IDENTITY.md` | True | True | `5dd5afe55f38` | `3611a5b708c5` | 110 | 118 | **diferente** |
| `USER.md` | True | True | `3d151974cc33` | `160d00c6273f` | 155 | 165 | **diferente** |
| `MEMORY.md` | True | True | `a15547314b5b` | `664957d62fa5` | 198 | 205 | **diferente** |
| `TOOLS.md` | True | True | `323532ac51ca` | `4c0c82a76478` | 64 | 74 | **diferente** |

## Diretórios críticos
### Kobe `memory/` vs `openclaw/agents/kobe/memory/`
- Total Kobe: 136
- Total cérebro: 123
- Iguais: 5
- Diferentes: 116
- Só no Kobe: 15
- Só no cérebro: 2

Diferentes — amostra:
- `.dreams/short-term-recall.json`
- `2026-03-18.md`
- `2026-03-20.md`
- `2026-03-23-ads-webapp-status.md`
- `2026-03-23-bidspark-status.md`
- `2026-03-23-billing-decision.md`
- `2026-03-23-builder-ads-status.md`
- `2026-03-23-builder-workspace.md`
- `2026-03-23-import-audit.md`
- `2026-03-23-relatorio-lembrete.md`
- `2026-03-23-rodonaves-whatsapp.md`
- `2026-03-23-session-greeting.md`
- `2026-03-23-session-startup.md`
- `2026-03-23-spark-builder.md`
- `2026-03-23-whatsapp-test.md`
- `2026-03-23.md`
- `2026-03-24-financial-cron.md`
- `2026-03-24-session-greeting.md`
- `2026-03-24-spark-ads-builder.md`
- `2026-03-24-spark-ads-review.md`

Só no Kobe — amostra:
- `.dreams/events.jsonl`
- `2026-03-31-rh-whatsapp-dup.md`
- `2026-04-02-bling-credentials.md`
- `2026-04-07-context-restore.md`
- `2026-04-26.md`
- `2026-04-27-blog-automation.md`
- `2026-04-27-job-monitor.md`
- `2026-04-27-wf4-images.md`
- `2026-04-27.md`
- `2026-04-28-blog-fix.md`
- `core-audit-snapshot.tsv`
- `integrations/slack-integration.md`
- `projects/budamix-blog-editorial.md`
- `sessions/2026-04-28.md`
- `tasks-pending.md`

Só no segundo cérebro — amostra:
- `sessions/2026-03-27.md`
- `sessions/2026-03-28.md`

### Kobe `skills/` vs `segundo-cerebro/skills/`
- Total Kobe: 271
- Total cérebro: 271
- Iguais: 270
- Diferentes: 1
- Só no Kobe: 0
- Só no cérebro: 0

Diferentes — amostra:
- `marketplace/ml-fees-rules/SKILL.md`

### Kobe `shared/` vs `openclaw/agents/kobe/shared/`
- Total Kobe: 186
- Total cérebro: 183
- Iguais: 17
- Diferentes: 162
- Só no Kobe: 7
- Só no cérebro: 4

Diferentes — amostra:
- `TEAM.md`
- `builder/MEMORY.md`
- `builder/SOUL.md`
- `builder/memory/decisions.md`
- `builder/memory/lessons.md`
- `builder/memory/pending.md`
- `builder/memory/sessions/2026-03-24.md`
- `builder/memory/sessions/2026-03-26.md`
- `builder/memory/sessions/2026-03-27.md`
- `builder/memory/sessions/2026-03-29.md`
- `builder/memory/sessions/2026-03-30.md`
- `builder/memory/sessions/2026-04-05.md`
- `builder/memory/sessions/2026-04-06.md`
- `builder/memory/sessions/2026-04-07.md`
- `builder/memory/sessions/2026-04-08.md`
- `builder/memory/sessions/2026-04-09.md`
- `builder/memory/sessions/2026-04-10.md`
- `builder/memory/sessions/2026-04-11.md`
- `builder/memory/sessions/2026-04-12.md`
- `builder/memory/sessions/2026-04-13.md`

Só no Kobe — amostra:
- `builder/memory/sessions/2026-04-26.md`
- `builder/memory/sessions/2026-04-27.md`
- `rh/memory/sessions/2026-04-26.md`
- `spark/memory/sessions/2026-04-26.md`
- `spark/memory/sessions/2026-04-27.md`
- `trader/memory/sessions/2026-04-26.md`
- `trader/memory/sessions/2026-04-27.md`

Só no segundo cérebro — amostra:
- `builder/memory/sessions/_sessions-index.md`
- `outputs/_outputs-index.md`
- `spark/memory/sessions/_sessions-index.md`
- `trader/memory/sessions/_sessions-index.md`

### Kobe `memory/*.md` vs `segundo-cerebro/memory/` global
- Total Kobe: 127
- Total cérebro: 32
- Iguais: 0
- Diferentes: 20
- Só no Kobe: 107
- Só no cérebro: 12

Diferentes — amostra:
- `context/business-context.md`
- `context/people.md`
- `sessions/2026-04-06.md`
- `sessions/2026-04-07.md`
- `sessions/2026-04-08.md`
- `sessions/2026-04-09.md`
- `sessions/2026-04-10.md`
- `sessions/2026-04-13.md`
- `sessions/2026-04-14.md`
- `sessions/2026-04-15.md`
- `sessions/2026-04-16.md`
- `sessions/2026-04-17.md`
- `sessions/2026-04-19.md`
- `sessions/2026-04-20.md`
- `sessions/2026-04-21.md`
- `sessions/2026-04-22.md`
- `sessions/2026-04-23.md`
- `sessions/2026-04-24.md`
- `sessions/2026-04-25.md`
- `sessions/2026-04-26.md`

Só no Kobe — amostra:
- `2026-03-18.md`
- `2026-03-20.md`
- `2026-03-23-ads-webapp-status.md`
- `2026-03-23-bidspark-status.md`
- `2026-03-23-billing-decision.md`
- `2026-03-23-builder-ads-status.md`
- `2026-03-23-builder-workspace.md`
- `2026-03-23-import-audit.md`
- `2026-03-23-relatorio-lembrete.md`
- `2026-03-23-rodonaves-whatsapp.md`
- `2026-03-23-session-greeting.md`
- `2026-03-23-session-startup.md`
- `2026-03-23-spark-builder.md`
- `2026-03-23-whatsapp-test.md`
- `2026-03-23.md`
- `2026-03-24-financial-cron.md`
- `2026-03-24-session-greeting.md`
- `2026-03-24-spark-ads-builder.md`
- `2026-03-24-spark-ads-review.md`
- `2026-03-25-1735.md`

Só no segundo cérebro — amostra:
- `context/deadlines.md`
- `context/decisoes/2026-04.md`
- `context/dev-projects-local.md`
- `context/fornecedores/yiwu-lotus.md`
- `context/pendencias.md`
- `projects/_index.md`
- `projects/estoque-budamix.md`
- `projects/gb-import-hub-edge-functions-map.md`
- `projects/gb-import-hub-reconnection-plan.md`
- `projects/gb-import-hub-schema.md`
- `projects/shopee-porta-copos-analise.md`
- `sessions/2026-04-15-shopee-audit.md`

## Achados principais
1. Os arquivos core existem nos dois lados, mas todos estão diferentes. Isso indica que já houve enriquecimento/edição no segundo cérebro ou drift entre estruturas.
2. `skills/` está praticamente sincronizado: 270 arquivos iguais e apenas 1 divergência detectada (`marketplace/ml-fees-rules/SKILL.md`).
3. A memória do Kobe está bastante divergente: muitos arquivos existem nos dois lados com conteúdo diferente, e há arquivos recentes só no workspace do Kobe.
4. O diretório `shared/` dos agentes também divergiu bastante; sessões recentes de 26/04 e 27/04 existem só no Kobe, enquanto o segundo cérebro tem alguns índices próprios.
5. O repo `segundo-cerebro` estava limpo antes desta auditoria; o workspace Kobe tem mudanças locais operacionais não relacionadas à migração, incluindo tokens/logs e `memory/2026-04-28-blog-fix.md`.
## Riscos para a Fase 2
- Não escolher automaticamente “arquivo mais novo” sem diff semântico; pode apagar wikilinks/frontmatter do vault ou memória recente do Kobe.
- Atenção especial a `pending.md` vs `pendencias.md`, `decisions.md` vs `decisoes/2026-04.md`, e sessões diárias duplicadas.
- Não usar `rsync --delete` em diretórios canônicos enquanto houver divergência.
- Antes da migração, separar arquivos operacionais sensíveis/logs/tokens de memória durável.
## Recomendação para próxima fase
Executar Fase 2 como mapeamento canônico arquivo-a-arquivo, começando por arquivos core e memória de contexto. Skills podem ser tratadas no final porque estão quase idênticas.
