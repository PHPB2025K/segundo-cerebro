# Relatório — Preenchimento Fase 2

Data: 15/04/2026

## Fichas Preenchidas

| Projeto | Status | Fonte dos dados |
|---------|--------|-----------------|
| carousel-factory | **completo** | README.md, docs/ARCHITECTURE.md, docs/COSTS.md, frontend/package.json |
| gmail-organizer | **completo** | CLAUDE.md local (workflow ID, credenciais, categorias, 22 nodes) |
| google-calendar-config | **completo** | Diretório local (contém apenas gcp-oauth.keys.json) |
| running-coach-ai | **completo** | PROJECT.md (168L) — coach Antonieta, 2 workflows N8N, 50 notas memória, integrações Strava/WhatsApp/Sheets |
| openclaw-config | **completo** | Diretório local (2 .docx), vault (2 MDs convertidos em openclaw/system/) |

## Itens "A PREENCHER" Resolvidos

| Item | Valor encontrado | Arquivo atualizado |
|------|------------------|--------------------|
| Supabase GB Import Hub | `ocxvwwaaqqxecmzhfxhb` | stack-tecnico.md |
| Supabase Spark Ads | `wzhmrpskiscassbixurr` | stack-tecnico.md, credenciais-map.md |
| Supabase Amazon Ads / BudaAds | `skntaotevvxblxhpccuy` | stack-tecnico.md |
| Supabase ML Ads | `cckfkvqblvundnyphole` | stack-tecnico.md |
| Supabase Running Coach / Carousel | `xxbsjbgipmtzojhtsrve` | stack-tecnico.md |
| Supabase Budamix AI Agent | `jpacmloqsfiebvagfomt` | stack-tecnico.md |
| Supabase Estoque Budamix | `sqbkoprcmnznmzbwdrmf` | stack-tecnico.md |
| Mission Control - Kobe | TenacitOS — dashboard monitoramento, PM2 na VPS, cron hourly | credenciais-map.md |
| Upseller ERP | Hub multi-marketplace, gestão SKUs armazém, apelidos | credenciais-map.md |
| Total Supabase projects | 5 → 11 (10 ativos + 1 legado migrado) | stack-tecnico.md |

## Pendências que dependem do Pedro

| Item | Arquivo | Pergunta |
|------|---------|----------|
| GB26001 — valores e datas | sops/atualizar-pagamento-importacao.md, projects/gb-import-hub.md | Qual o valor do numerário e 70% balanço? Quais as datas de vencimento? |
| GB26002 — valores e datas | sops/atualizar-pagamento-importacao.md, projects/gb-import-hub.md | Mesmo que acima — nenhum dado registrado no sistema |
| google-calendar-config — destino | projects/google-calendar-config.md | Manter como projeto ou mover para knowledge/concepts/? É só um JSON de OAuth |

## Métricas

| Métrica | Fase 1 (pré) | Fase 2 (pós) | Delta |
|---------|:------------:|:------------:|:-----:|
| Notas total | 413 | 413 | 0 (atualizações, não criações) |
| Wikilinks | 1.165 | ~1.200 | +35 |
| Projetos Supabase mapeados | 5 | 11 | +6 |
| Fichas stub restantes | 5 | 0 | -5 |
| Itens "A PREENCHER" | 8 | 3 | -5 resolvidos |
| Cobertura estimada | **~85%** | **~92%** | +7pp |

## O que falta para 100%

1. **GB26001/GB26002** — Pedro precisa informar valores e datas de pagamento
2. **SOPs adicionais** — faltam: "criar listing Shopee", "abrir nova importação", "configurar novo agente OpenClaw"
3. **Fichas individuais de containers** — GB25007 a GB26002 sem fichas dedicadas
4. **Automações N8N detalhadas** — 4 workflows listados no crons-index sem fichas individuais
5. **knowledge/corrida/** — pasta vazia, dados vivem no PROJECT.md do running-coach-ai

## Commits

1. `7f4e7af` — checkpoint: pre-preenchimento-fase2
2. `a9c5ff5` — feat(preenchimento): fase 2 — fichas stub + itens pendentes
