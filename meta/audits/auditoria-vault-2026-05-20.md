---
title: Auditoria de Saúde do Vault — 2026-05-20
created: 2026-05-20
type: audit
status: active
tags:
  - audit
  - meta
  - knowledge-graph
scope: LOTE A (núcleo editorial humano)
---

# Auditoria de Saúde — Segundo Cérebro · 2026-05-20

> **Escopo (LOTE A):** business/, projects/, knowledge/, automacoes/, memory/context/, memory/projects/, meta/, prompts/, skills/ (exceto `skills/superpowers` que é pacote instalado).
> **Fora do escopo:** openclaw/agents/ (estado operacional do Kobe), memory/sessions/, memory/agent-digests/, reports/ — incluídos só para resolução de wikilinks.
> **Modo:** read-only. Nenhuma edição executada. Relatório gerado por `/tmp/vault-audit/audit.py`.

## Sumário

- **Total notas no vault:** 1299
- **Total notas no LOTE A:** 321
- **Notas órfãs (sem in-link) no LOTE A:** 79
- **Notas ilhas (sem in-link nem out-link) no LOTE A:** 65
- **Sem frontmatter:** 30
- **Sem nenhuma tag (YAML ou body):** 78
- **Wikilinks quebrados (vault inteiro):** 273
- **Wikilinks quebrados em notas LOTE A:** 91
- **Variantes redundantes de tags detectadas:** 3

## 1. Hubs atuais — top 20 no LOTE A

Notas mais referenciadas (potenciais entry points para densificação radial).

| In-links | Nota |
|---:|---|
| 115 | [[memory/context/business-context]] |
| 91 | [[memory/context/decisoes/2026-04]] |
| 48 | [[business/marketplaces/_index]] |
| 32 | [[meta/mocs/MOC - Governanca OpenClaw]] |
| 31 | [[projects/budamix-ecommerce]] |
| 26 | [[projects/budamix-central]] |
| 26 | [[meta/mocs/MOC - Taxas e Precificacao]] |
| 25 | [[knowledge/concepts/stack-tecnico]] |
| 24 | [[meta/mocs/MOC - Supabase Ecosystem]] |
| 22 | [[projects/amazon-ads-automation]] |
| 21 | [[projects/ml-ads-automation]] |
| 19 | [[projects/canggu/canggu]] |
| 16 | [[business/importacao/estrategia-fiscal-gb]] |
| 16 | [[knowledge/concepts/credenciais-map]] |
| 15 | [[skills/spreadsheet-pricing/SKILL]] |
| 13 | [[memory/context/pendencias]] |
| 13 | [[meta/mocs/MOC - Token Management]] |
| 12 | [[projects/gb-import-hub]] |
| 12 | [[projects/canggu/debitos-tecnicos]] |
| 12 | [[meta/mocs/MOC - Design Systems Budamix]] |

## 2. Wikilinks quebrados

Total: 91 links em 23 notas do LOTE A.

### 2.1 Targets mais frequentes (deduzir intenção)

| Quantidade | Target referenciado | Diagnóstico provável |
|---:|---|---|
| 5× | `[[openclaw/agents/spark/IDENTITY\]]` | path correto é `openclaw/agents/spark/IDENTITY` — backslash de escape no `]]` |
| 4× | `[[openclaw/agents/fisco/IDENTITY\]]` | idem — escape `\]]` corrompe o link |
| 4× | `[[openclaw/agents/trader/IDENTITY\]]` | idem |
| 4× | `[[Nome da Nota]]` | placeholder de template não preenchido |
| 3× | `[[skills/planilha-precificacao/SKILL]]` | nota foi renomeada/movida — apontar para path real |
| 2× | `[[memory/sessions/2026-04-10]]` | verificar manualmente |
| 2× | `[[memory/sessions/2026-04-15]]` | verificar manualmente |
| 2× | `[[memory/sessions/2026-04-07]]` | verificar manualmente |
| 2× | `[[skills/n8n/n8n-mcp-tools-expert]]` | skills n8n estão em pasta diferente (verificar) |
| 2× | `[[frontend]]` | termo solto sem path — basename ambíguo |
| 2× | `[[edge-functions\]]` | termo solto — backslash escape |
| 2× | `[[CLAUDE.md]]` | links absolutos com .md — devem virar `[[CLAUDE]]` sem extensão |
| 2× | `[[agents/kobe/IDENTITY]]` | path relativo errado — falta prefixo `openclaw/` |
| 2× | `[[imagem.png]]` | placeholder de template não preenchido |
| 2× | `[[Nota Relacionada 1]]` | placeholder de template não preenchido |

### 2.2 Notas com 5+ wikilinks quebrados (prioridade de correção)

| Quebras | Nota |
|---:|---|
| 19 | [[skills/obsidian-vault-manager/SKILL]] |
| 12 | [[memory/context/decisoes/2026-04]] |
| 12 | [[business/marketing/marca/_index]] |
| 10 | [[knowledge/concepts/credenciais-map]] |
| 7 | [[projects/n8n-builder]] |
| 6 | [[knowledge/concepts/stack-tecnico]] |
| 4 | [[memory/projects/_index]] |
| 3 | [[knowledge/concepts/kg-wikilinks-auditoria-metodo]] |

## 3. Notas órfãs (sem nenhum in-link) — LOTE A

Total: 79.

### 3.1 Distribuição por pasta

| Pasta | Órfãs |
|---|---:|
| `skills/marketing/` | 14 |
| `automacoes/workflows/` | 11 |
| `memory/projects/` | 9 |
| `prompts/daily-sales/` | 9 |
| `memory/context/` | 6 |
| `business/marketing/` | 5 |
| `automacoes/sops/` | 4 |
| `meta/audits/` | 3 |
| `knowledge/concepts/` | 3 |
| `skills/financeiro/` | 2 |
| `projects/canggu/` | 1 |
| `projects/budamix-central-estoque-modulo/` | 1 |
| `business/financeiro/` | 1 |
| `skills/design/` | 1 |
| `skills/trader-himmel-context-ingestion/` | 1 |
| `skills/trader-daily-sales-qa-escalation/` | 1 |
| `skills/trader-daily-sales-memory-cycle/` | 1 |
| `skills/daily-sales-report/` | 1 |
| `skills/trader-daily-sales-account-analysis/` | 1 |
| `skills/trader-marketplace-rules-watch/` | 1 |
| `skills/trader-daily-sales-data-readiness/` | 1 |
| `skills/trader-daily-sales-cron-orchestrator/` | 1 |
| `skills/trader-daily-sales-slack-writer/` | 1 |

### 3.2 Lista completa (agrupada por pasta)

#### `automacoes/sops/`

- [[automacoes/sops/abrir-nova-importacao]]
- [[automacoes/sops/configurar-novo-agente-openclaw]]
- [[automacoes/sops/criar-listing-shopee]]
- [[automacoes/sops/deploy-ecommerce]]

#### `automacoes/workflows/`

- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.1]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.2]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.3]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.4]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado]]
- [[automacoes/workflows/budamix-whatsapp-ana]]
- [[automacoes/workflows/gmail-agente-inbox]]
- [[automacoes/workflows/pedidos-venda-gb-bling]]
- [[automacoes/workflows/running-coach-nova-atividade]]
- [[automacoes/workflows/vault-sync-mac-launchd]]

#### `business/financeiro/`

- [[business/financeiro/dre-abril-2026-u15-u44-v4]]

#### `business/marketing/`

- [[business/marketing/marca/calendario-semana-04-a-10-maio-2026]]
- [[business/marketing/marca/mapa-editorial]]
- [[business/marketing/marca/planejamento-comunidade-vip]]
- [[business/marketing/marca/proposta-de-valor]]
- [[business/marketing/marca/recomendacao-stories]]

#### `knowledge/concepts/`

- [[knowledge/concepts/bling-api-v3-aprendizados]]
- [[knowledge/concepts/cloudflare-urllib-user-agent]]
- [[knowledge/concepts/nano-banana-mcp-setup]]

#### `memory/context/`

- [[memory/context/business-context-kobe-import]]
- [[memory/context/decisions]]
- [[memory/context/decisoes/kobe-permanentes]]
- [[memory/context/lessons]]
- [[memory/context/people-kobe-import]]
- [[memory/context/writing-as-pedro]]

#### `memory/projects/`

- [[memory/projects/compras-canecas]]
- [[memory/projects/gb-whatsapp-areas/README]]
- [[memory/projects/gb-whatsapp-areas/compras]]
- [[memory/projects/gb-whatsapp-areas/expedicao]]
- [[memory/projects/gb-whatsapp-areas/financeiro]]
- [[memory/projects/gb-whatsapp-areas/socios]]
- [[memory/projects/gb-whatsapp-areas/vendas-atacado]]
- [[memory/projects/gestao-funcionarios]]
- [[memory/projects/mission-control]]

#### `meta/audits/`

- [[meta/audits/auditoria-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[meta/audits/mapa-canonico-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[meta/audits/quarentena-migracao-kobe-memory-2026-04-28]]

#### `projects/budamix-central-estoque-modulo/`

- [[projects/budamix-central-estoque-modulo/sync-physical-inventory-v3-with-items.py.patch]]

#### `projects/canggu/`

- [[projects/canggu/frontend]]

#### `prompts/daily-sales/`

- [[prompts/daily-sales/camada-1-estrategica]]
- [[prompts/daily-sales/camada-2-tatica]]
- [[prompts/daily-sales/camada-3-operacional]]
- [[prompts/daily-sales/camada-4-granular]]
- [[prompts/daily-sales/camada-5-condensadora]]
- [[prompts/daily-sales/camada-6-slack-writer]]
- [[prompts/daily-sales/camada-6b-shopee-consolidadora]]
- [[prompts/daily-sales/camada-7-qa-gate]]
- [[prompts/daily-sales/obsolete/camada-6-qa-obsoleta]]

#### `skills/daily-sales-report/`

- [[skills/daily-sales-report/SKILL]]

#### `skills/design/`

- [[skills/design/epic-paper/SKILL]]

#### `skills/financeiro/`

- [[skills/financeiro/dre-profissional-marketplace/SKILL]]
- [[skills/financeiro/dre-profissional-marketplace/references/checklist-dre]]

#### `skills/marketing/`

- [[skills/marketing/image-prompt-generator/SKILL]]
- [[skills/marketing/image-prompt-generator/references/additional-use-cases]]
- [[skills/marketing/image-prompt-generator/references/ads]]
- [[skills/marketing/image-prompt-generator/references/comic]]
- [[skills/marketing/image-prompt-generator/references/editing]]
- [[skills/marketing/image-prompt-generator/references/educational]]
- [[skills/marketing/image-prompt-generator/references/fundamentals]]
- [[skills/marketing/image-prompt-generator/references/infographic]]
- [[skills/marketing/image-prompt-generator/references/logo]]
- [[skills/marketing/image-prompt-generator/references/models]]
- [[skills/marketing/image-prompt-generator/references/photorealism]]
- [[skills/marketing/image-prompt-generator/references/product]]
- [[skills/marketing/image-prompt-generator/references/translation]]
- [[skills/marketing/image-prompt-generator/references/ui-mockup]]

#### `skills/trader-daily-sales-account-analysis/`

- [[skills/trader-daily-sales-account-analysis/SKILL]]

#### `skills/trader-daily-sales-cron-orchestrator/`

- [[skills/trader-daily-sales-cron-orchestrator/SKILL]]

#### `skills/trader-daily-sales-data-readiness/`

- [[skills/trader-daily-sales-data-readiness/SKILL]]

#### `skills/trader-daily-sales-memory-cycle/`

- [[skills/trader-daily-sales-memory-cycle/SKILL]]

#### `skills/trader-daily-sales-qa-escalation/`

- [[skills/trader-daily-sales-qa-escalation/SKILL]]

#### `skills/trader-daily-sales-slack-writer/`

- [[skills/trader-daily-sales-slack-writer/SKILL]]

#### `skills/trader-himmel-context-ingestion/`

- [[skills/trader-himmel-context-ingestion/SKILL]]

#### `skills/trader-marketplace-rules-watch/`

- [[skills/trader-marketplace-rules-watch/SKILL]]

## 4. Notas ilha (sem in-link nem out-link) — LOTE A

Total: 65. **Estas são as prioridades absolutas de densificação** — nem entram nem saem do grafo.

| Pasta | Ilhas |
|---|---:|
| `skills/marketing/` | 14 |
| `prompts/daily-sales/` | 9 |
| `memory/projects/` | 8 |
| `automacoes/workflows/` | 7 |
| `memory/context/` | 5 |
| `business/marketing/` | 5 |
| `meta/audits/` | 3 |
| `skills/financeiro/` | 2 |
| `projects/budamix-central-estoque-modulo/` | 1 |
| `business/financeiro/` | 1 |
| `skills/design/` | 1 |
| `skills/trader-himmel-context-ingestion/` | 1 |
| `skills/trader-daily-sales-qa-escalation/` | 1 |
| `skills/trader-daily-sales-memory-cycle/` | 1 |
| `skills/daily-sales-report/` | 1 |
| `skills/trader-daily-sales-account-analysis/` | 1 |
| `skills/trader-marketplace-rules-watch/` | 1 |
| `skills/trader-daily-sales-data-readiness/` | 1 |
| `skills/trader-daily-sales-cron-orchestrator/` | 1 |
| `skills/trader-daily-sales-slack-writer/` | 1 |

Lista completa:

- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.2]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.3]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.4]]
- [[automacoes/workflows/pedidos-venda-gb-bling]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2.1]]
- [[automacoes/workflows/briefing-pipeline-pedidos-atacado-v2]]
- [[memory/context/people-kobe-import]]
- [[memory/context/business-context-kobe-import]]
- [[memory/context/writing-as-pedro]]
- [[memory/context/decisions]]
- [[memory/context/decisoes/kobe-permanentes]]
- [[memory/projects/compras-canecas]]
- [[memory/projects/mission-control]]
- [[memory/projects/gb-whatsapp-areas/financeiro]]
- [[memory/projects/gb-whatsapp-areas/expedicao]]
- [[memory/projects/gb-whatsapp-areas/vendas-atacado]]
- [[memory/projects/gb-whatsapp-areas/compras]]
- [[memory/projects/gb-whatsapp-areas/README]]
- [[memory/projects/gb-whatsapp-areas/socios]]
- [[projects/budamix-central-estoque-modulo/sync-physical-inventory-v3-with-items.py.patch]]
- [[business/financeiro/dre-abril-2026-u15-u44-v4]]
- [[business/marketing/marca/proposta-de-valor]]
- [[business/marketing/marca/planejamento-comunidade-vip]]
- [[business/marketing/marca/calendario-semana-04-a-10-maio-2026]]
- [[business/marketing/marca/recomendacao-stories]]
- [[business/marketing/marca/mapa-editorial]]
- [[meta/audits/auditoria-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[meta/audits/quarentena-migracao-kobe-memory-2026-04-28]]
- [[meta/audits/mapa-canonico-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[prompts/daily-sales/camada-2-tatica]]
- [[prompts/daily-sales/camada-3-operacional]]
- [[prompts/daily-sales/camada-6b-shopee-consolidadora]]
- [[prompts/daily-sales/camada-4-granular]]
- [[prompts/daily-sales/camada-6-slack-writer]]
- [[prompts/daily-sales/camada-1-estrategica]]
- [[prompts/daily-sales/camada-7-qa-gate]]
- [[prompts/daily-sales/camada-5-condensadora]]
- [[prompts/daily-sales/obsolete/camada-6-qa-obsoleta]]
- [[skills/design/epic-paper/SKILL]]
- [[skills/trader-himmel-context-ingestion/SKILL]]
- [[skills/trader-daily-sales-qa-escalation/SKILL]]
- [[skills/trader-daily-sales-memory-cycle/SKILL]]
- [[skills/daily-sales-report/SKILL]]
- [[skills/trader-daily-sales-account-analysis/SKILL]]
- [[skills/financeiro/dre-profissional-marketplace/SKILL]]
- [[skills/financeiro/dre-profissional-marketplace/references/checklist-dre]]
- [[skills/trader-marketplace-rules-watch/SKILL]]
- [[skills/trader-daily-sales-data-readiness/SKILL]]
- [[skills/trader-daily-sales-cron-orchestrator/SKILL]]
- [[skills/marketing/image-prompt-generator/SKILL]]
- [[skills/marketing/image-prompt-generator/references/translation]]
- [[skills/marketing/image-prompt-generator/references/product]]
- [[skills/marketing/image-prompt-generator/references/logo]]
- [[skills/marketing/image-prompt-generator/references/comic]]
- [[skills/marketing/image-prompt-generator/references/educational]]
- [[skills/marketing/image-prompt-generator/references/infographic]]
- [[skills/marketing/image-prompt-generator/references/editing]]
- [[skills/marketing/image-prompt-generator/references/photorealism]]
- [[skills/marketing/image-prompt-generator/references/fundamentals]]
- [[skills/marketing/image-prompt-generator/references/models]]
- [[skills/marketing/image-prompt-generator/references/additional-use-cases]]
- [[skills/marketing/image-prompt-generator/references/ui-mockup]]
- [[skills/marketing/image-prompt-generator/references/ads]]
- [[skills/trader-daily-sales-slack-writer/SKILL]]

## 5. Notas sem frontmatter

Total: 30.

- [[projects/budamix-central-estoque-modulo/sync-physical-inventory-v3-with-items.py.patch]]
- [[meta/audits/auditoria-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[meta/audits/quarentena-migracao-kobe-memory-2026-04-28]]
- [[meta/audits/mapa-canonico-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[prompts/daily-sales/camada-2-tatica]]
- [[prompts/daily-sales/camada-3-operacional]]
- [[prompts/daily-sales/camada-6b-shopee-consolidadora]]
- [[prompts/daily-sales/camada-4-granular]]
- [[prompts/daily-sales/camada-6-slack-writer]]
- [[prompts/daily-sales/camada-1-estrategica]]
- [[prompts/daily-sales/camada-7-qa-gate]]
- [[prompts/daily-sales/camada-5-condensadora]]
- [[prompts/daily-sales/obsolete/camada-6-qa-obsoleta]]
- [[skills/financeiro/dre-profissional-marketplace/references/checklist-dre]]
- [[skills/lovable/lovable-github-sync]]
- [[skills/lovable/lovable-design-system]]
- [[skills/lovable/lovable-compatibility]]
- [[skills/marketing/image-prompt-generator/references/translation]]
- [[skills/marketing/image-prompt-generator/references/product]]
- [[skills/marketing/image-prompt-generator/references/logo]]
- [[skills/marketing/image-prompt-generator/references/comic]]
- [[skills/marketing/image-prompt-generator/references/educational]]
- [[skills/marketing/image-prompt-generator/references/infographic]]
- [[skills/marketing/image-prompt-generator/references/editing]]
- [[skills/marketing/image-prompt-generator/references/photorealism]]
- [[skills/marketing/image-prompt-generator/references/fundamentals]]
- [[skills/marketing/image-prompt-generator/references/models]]
- [[skills/marketing/image-prompt-generator/references/additional-use-cases]]
- [[skills/marketing/image-prompt-generator/references/ui-mockup]]
- [[skills/marketing/image-prompt-generator/references/ads]]

## 6. Notas sem nenhuma tag (YAML ou inline body)

Total: 78.

- [[memory/projects/gb-whatsapp-areas/financeiro]]
- [[memory/projects/gb-whatsapp-areas/expedicao]]
- [[memory/projects/gb-whatsapp-areas/vendas-atacado]]
- [[memory/projects/gb-whatsapp-areas/compras]]
- [[memory/projects/gb-whatsapp-areas/README]]
- [[memory/projects/gb-whatsapp-areas/socios]]
- [[projects/budamix-central-estoque-modulo/sync-physical-inventory-v3-with-items.py.patch]]
- [[meta/audits/auditoria-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[meta/audits/quarentena-migracao-kobe-memory-2026-04-28]]
- [[meta/audits/mapa-canonico-unificacao-kobe-segundo-cerebro-2026-04-28]]
- [[prompts/daily-sales/camada-2-tatica]]
- [[prompts/daily-sales/camada-3-operacional]]
- [[prompts/daily-sales/camada-6b-shopee-consolidadora]]
- [[prompts/daily-sales/camada-4-granular]]
- [[prompts/daily-sales/camada-6-slack-writer]]
- [[prompts/daily-sales/camada-1-estrategica]]
- [[prompts/daily-sales/camada-7-qa-gate]]
- [[prompts/daily-sales/camada-5-condensadora]]
- [[prompts/daily-sales/obsolete/camada-6-qa-obsoleta]]
- [[skills/research/deep-research-protocol/SKILL]]
- [[skills/design/shadcn-ui/SKILL]]
- [[skills/design/epic-paper/SKILL]]
- [[skills/design/animated-financial-display/SKILL]]
- [[skills/design/superdesign/SKILL]]
- [[skills/trader-himmel-context-ingestion/SKILL]]
- [[skills/trader-daily-sales-qa-escalation/SKILL]]
- [[skills/trader-daily-sales-memory-cycle/SKILL]]
- [[skills/daily-sales-report/SKILL]]
- [[skills/trader-daily-sales-account-analysis/SKILL]]
- [[skills/marketplace/marketplace-report/SKILL]]
- [[skills/marketplace/ml-extrato/SKILL]]
- [[skills/marketplace/amazon-extrato/SKILL]]
- [[skills/marketplace/amazon-fees-rules/SKILL]]
- [[skills/marketplace/ml-ads/SKILL]]
- [[skills/marketplace/ml-competitor-analysis/SKILL]]
- [[skills/marketplace/shopee-extrato/SKILL]]
- [[skills/marketplace/shopee-fees-rules/SKILL]]
- [[skills/marketplace/consolidado-financeiro/SKILL]]
- [[skills/marketplace/ml-fees-rules/SKILL]]
- [[skills/marketplace/ml-report/SKILL]]
- [[skills/marketplace/marketplace-optimization/SKILL]]
- [[skills/amazon-listing-creator/SKILL]]
- [[skills/spreadsheet-pricing/SKILL]]
- [[skills/operations/inventory-management/SKILL]]
- [[skills/financeiro/dre-profissional-marketplace/SKILL]]
- [[skills/financeiro/dre-profissional-marketplace/references/checklist-dre]]
- [[skills/financeiro/stripe-api/SKILL]]
- [[skills/trader-marketplace-rules-watch/SKILL]]
- [[skills/trader-daily-sales-data-readiness/SKILL]]
- [[skills/integracao/instagram/SKILL]]
- [[skills/trader-daily-sales-cron-orchestrator/SKILL]]
- [[skills/lovable/lovable-github-sync]]
- [[skills/lovable/lovable-design-system]]
- [[skills/lovable/lovable-compatibility]]
- [[skills/marketing/image-prompt-generator/SKILL]]
- [[skills/marketing/image-prompt-generator/references/translation]]
- [[skills/marketing/image-prompt-generator/references/product]]
- [[skills/marketing/image-prompt-generator/references/logo]]
- [[skills/marketing/image-prompt-generator/references/comic]]
- [[skills/marketing/image-prompt-generator/references/educational]]
- [[skills/marketing/image-prompt-generator/references/infographic]]
- [[skills/marketing/image-prompt-generator/references/editing]]
- [[skills/marketing/image-prompt-generator/references/photorealism]]
- [[skills/marketing/image-prompt-generator/references/fundamentals]]
- [[skills/marketing/image-prompt-generator/references/models]]
- [[skills/marketing/image-prompt-generator/references/additional-use-cases]]
- [[skills/marketing/image-prompt-generator/references/ui-mockup]]
- [[skills/marketing/image-prompt-generator/references/ads]]
- [[skills/marketing/google-ads/SKILL]]
- [[skills/marketing/budget-optimizer/SKILL]]
- [[skills/marketing/anomaly-detector/SKILL]]
- [[skills/marketing/meta-ads/SKILL]]
- [[skills/dev/fullstack-dev/SKILL]]
- [[skills/gb-import-hub/SKILL]]
- [[skills/whatsapp-ultimate/SKILL]]
- [[skills/shopee-listing-creator/SKILL]]
- [[skills/coaching-corrida/SKILL]]
- [[skills/trader-daily-sales-slack-writer/SKILL]]

## 7. Conectividade por pasta — zonas pouco conectadas

Média de in-links por nota dentro do LOTE A. Pastas com média baixa = candidatas a densificação.

| Avg in-links | Total in-links | Notas | Pasta |
|---:|---:|---:|---|
| 0.00 | 0 | 9 | `prompts/daily-sales/` |
| 0.00 | 0 | 1 | `skills/trader-himmel-context-ingestion/` |
| 0.00 | 0 | 1 | `skills/trader-daily-sales-qa-escalation/` |
| 0.00 | 0 | 1 | `skills/trader-daily-sales-memory-cycle/` |
| 0.00 | 0 | 1 | `skills/daily-sales-report/` |
| 0.00 | 0 | 1 | `skills/trader-daily-sales-account-analysis/` |
| 0.00 | 0 | 1 | `skills/trader-marketplace-rules-watch/` |
| 0.00 | 0 | 1 | `skills/trader-daily-sales-data-readiness/` |
| 0.00 | 0 | 1 | `skills/trader-daily-sales-cron-orchestrator/` |
| 0.00 | 0 | 1 | `skills/trader-daily-sales-slack-writer/` |
| 0.15 | 2 | 13 | `automacoes/workflows/` |
| 0.40 | 2 | 5 | `meta/audits/` |
| 0.42 | 10 | 24 | `skills/marketing/` |
| 0.50 | 1 | 2 | `projects/budamix-central-estoque-modulo/` |
| 0.78 | 7 | 9 | `automacoes/sops/` |
| 0.83 | 15 | 18 | `memory/projects/` |
| 0.83 | 10 | 12 | `skills/financeiro/` |
| 1.00 | 1 | 1 | `automacoes/crons-index.md/` |
| 1.00 | 1 | 1 | `projects/budamix-central-inventory-card/` |
| 1.00 | 1 | 1 | `skills/video/` |
| 1.00 | 1 | 1 | `skills/operations/` |
| 1.00 | 1 | 1 | `skills/obsidian-vault-manager/` |
| 1.00 | 1 | 1 | `skills/integracao/` |
| 1.00 | 2 | 2 | `skills/coaching-corrida/` |
| 1.20 | 12 | 10 | `skills/dev/` |

## 8. Tags inconsistentes / redundantes

Variantes detectadas por normalização (lower + sem `s` final + `_`→`-`).

| Forma normalizada | Variantes no vault |
|---|---|
| `cron` | `cron`, `crons` |
| `workflow` | `workflow`, `workflows` |
| `checklist` | `checklist`, `checklists` |

**Recomendação:** padronizar singular ou plural consistentemente. Ação fora do escopo da densificação de links — pode ser tratada na Fase 4 ou em uma rodada separada.

## 9. Próximos passos (Fase 2)

- **Fase 2** vai cruzar conceitos/entidades das 321 notas do LOTE A para sugerir **wikilinks transversais entre áreas diferentes** (ex: business ↔ projects ↔ skills, knowledge ↔ memory/context).
- Prioridades de densificação:
  - **65 ilhas** (devem ganhar pelo menos 1 link de entrada cada)
  - **79 órfãs** (devem ganhar in-link de hub temático ou MOC)
  - **Pastas com avg < 0.5 in-links**: skills/marketing, automacoes/workflows, automacoes/sops, prompts/daily-sales
- **Não tratar nesta fase de densificação** (separar):
  - 91 wikilinks quebrados (correção mecânica, fazer em rodada própria)
  - 30 notas sem frontmatter (formatação, não conexão)
  - 78 notas sem tags (taxonomia, não conexão)
  - 3 grupos de tag-variants (padronização lexical)

---

_Auditoria gerada por `/tmp/vault-audit/audit.py` em 2026-05-20._