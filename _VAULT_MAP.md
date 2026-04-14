---
title: Mapa do Segundo Cérebro
created: 2026-04-13
modified: 2026-04-13
tags:
  - meta
  - vault-map
type: meta
---

# Mapa Completo — Segundo Cérebro

> **Instruções para Claude Code:** Leia este arquivo PRIMEIRO em
> toda sessão antes de buscar qualquer coisa. Ele contém o mapeamento
> completo de todos os arquivos e pastas. Use-o para navegar
> diretamente ao arquivo correto sem gastar tokens com find, glob
> ou grep exploratórios.
>
> **Última atualização:** 2026-04-14

## Estatísticas
- Total de arquivos: 460
- Total de pastas: 201 (excluindo raiz)
- Breakdown por extensão: .md (359), .py (41), .json (17), .sh (14), .ts (6), .png (4), .yml (2), .pdf (2), .log (2), .js (2), .xlsx (1), .tsx (1), .mjs (1), .lock (1), .html (1), .gitignore (1), .example (1), .dot (1), .cjs (1), .canvas (1), .bak (1)

## Estrutura de Pastas

```
segundo-cerebro/
├── .claude/
│   └── projects/
│       └── -Users-pedrobroglio-segundo-cerebro/
│           └── memory/
├── .playwright-mcp/
├── meta/mocs/
├──openclaw/agents/
│   ├── builder/
│   │   └── memory/
│   │       ├── context/
│   │       └── projects/
│   ├── fisco/
│   ├── kobe/
│   │   └── shared/
│   │       ├── builder/
│   │       │   └── memory/
│   │       │       └── sessions/
│   │       ├── fisco/
│   │       │   ├── memory/
│   │       │   │   ├── context/
│   │       │   │   └── sessions/
│   │       │   ├── reference/
│   │       │   ├── skills/
│   │       │   │   ├── bling-nfe/
│   │       │   │   ├── distribution/
│   │       │   │   ├── nf-internal/
│   │       │   │   ├── nf-transfer/
│   │       │   │   ├── reconciliation/
│   │       │   │   └── simples-monitor/
│   │       │   └── templates/
│   │       ├── lessons/
│   │       │   └── reviews/
│   │       ├── outputs/
│   │       ├── rh/
│   │       │   ├── knowledge/
│   │       │   ├── memory/
│   │       │   │   └── context/
│   │       │   ├── skills/
│   │       │   │   ├── comunicacao-funcionarios/
│   │       │   │   └── monitor-ponto/
│   │       │   └── templates/
│   │       ├── simulimport/
│   │       ├── spark/
│   │       │   ├── memory/
│   │       │   │   ├── campaigns/
│   │       │   │   ├── context/
│   │       │   │   └── sessions/
│   │       │   └── skills/
│   │       │       ├── anomaly-detector/
│   │       │       ├── budget-optimizer/
│   │       │       ├── google-ads/
│   │       │       └── meta-ads/
│   │       └── trader/
│   │           └── memory/
│   │               ├── context/
│   │               └── sessions/
│   ├── rh/
│   ├── spark/
│   │   └── memory/
│   │       └── context/
│   └── trader/
│       └── memory/
│           └── context/
├── memory/
│   ├── context/
│   │   └── decisoes/
│   ├── projects/
│   └── sessions/
├── scripts/
└── skills/
    ├── amazon-listing-creator/
    │   ├── reference/
    │   ├── rules/
    │   └── templates/
    ├── coaching-corrida/
    │   ├── assets/
    │   └── references/
    ├── design/
    │   ├── animated-financial-display/
    │   │   └── .clawhub/
    │   ├── data-visualization-2/
    │   │   └── .clawhub/
    │   ├── financial-design-systems/
    │   │   └── .clawhub/
    │   ├── frontend-design-ultimate/
    │   │   ├── .clawhub/
    │   │   ├── references/
    │   │   ├── scripts/
    │   │   └── templates/
    │   ├── lb-motion-skill/
    │   │   ├── .clawhub/
    │   │   └── docs/
    │   ├── lovable-quality/
    │   ├── report-design-system/
    │   ├── shadcn-ui/
    │   │   └── .clawhub/
    │   └── superdesign/
    │       └── .clawhub/
    ├── dev/
    │   └── fullstack-dev/
    │       ├── assets/
    │       │   └── nextjs-starter/
    │       │       └── src/
    │       │           ├── app/
    │       │           ├── components/
    │       │           │   └── ui/
    │       │           ├── lib/
    │       │           └── types/
    │       ├── references/
    │       └── scripts/
    ├── excel-generation/
    ├── financeiro/
    │   └── stripe-api/
    │       ├── references/
    │       └── scripts/
    ├── gb-import-hub/
    │   └── references/
    ├── integracao/
    │   └── instagram/
    │       └── scripts/
    ├── marketing/
    │   ├── anomaly-detector/
    │   ├── budget-optimizer/
    │   ├── google-ads/
    │   └── meta-ads/
    │       ├── references/
    │       └── scripts/
    ├── marketplace/
    │   ├── amazon-extrato/
    │   │   ├── references/
    │   │   └── scripts/
    │   ├── amazon-fees-rules/
    │   ├── consolidado-financeiro/
    │   │   └── scripts/
    │   ├── marketplace-optimization/
    │   │   └── references/
    │   ├── marketplace-report/
    │   │   ├── assets/
    │   │   ├── references/
    │   │   └── scripts/
    │   │       ├── connectors/
    │   │       └── sections/
    │   ├── ml-ads/
    │   │   └── references/
    │   ├── ml-competitor-analysis/
    │   │   ├── cases/
    │   │   ├── references/
    │   │   └── scripts/
    │   ├── ml-extrato/
    │   │   ├── references/
    │   │   └── scripts/
    │   ├── ml-fees-rules/
    │   ├── ml-report/
    │   │   ├── assets/
    │   │   ├── references/
    │   │   └── scripts/
    │   │       └── sections/
    │   ├── shopee-extrato/
    │   │   ├── references/
    │   │   └── scripts/
    │   └── shopee-fees-rules/
    ├── obsidian-vault-manager/
    ├── operations/
    │   └── inventory-management/
    ├── perplexity/
    │   └── scripts/
    ├── research/
    │   └── deep-research-protocol/
    ├── shopee-listing-creator/
    │   ├── rules/
    │   └── templates/
    ├── spreadsheet-pricing/
    │   ├── maps/
    │   └── rules/
    ├── strategic-planner/
    │   └── references/
    ├── superpowers/
    │   ├── brainstorming/
    │   │   └── scripts/
    │   ├── dispatching-parallelopenclaw/agents/
    │   ├── executing-plans/
    │   ├── finishing-a-development-branch/
    │   ├── receiving-code-review/
    │   ├── requesting-code-review/
    │   ├── subagent-driven-development/
    │   ├── systematic-debugging/
    │   ├── test-driven-development/
    │   ├── using-git-worktrees/
    │   ├── using-superpowers/
    │   │   └── references/
    │   ├── verification-before-completion/
    │   ├── writing-plans/
    │   └── writing-skills/
    │       └── examples/
    ├── update-ml-return-rates/
    └── whatsapp-ultimate/
        └── scripts/
```

## Índice Completo de Arquivos

### 📁 / (raiz)
- _VAULT_MAP.md — Mapa do Segundo Cérebro (este arquivo)
- CLAUDE.md — Pedro Broglio — Contexto para o Claude Code
- PROPAGATION.md — Propagação de Dados — Protocolo Único
- Sem título.canvas — (canvas Obsidian)

### 📁 /.claude/projects/-Users-pedrobroglio-segundo-cerebro/memory/
- feedback_shopee_brand.md — (feedback Claude Code)

### 📁 /.playwright-mcp/
- console-2026-04-07T19-54-48-743Z.log — (log Playwright)
- console-2026-04-07T19-55-25-927Z.log — (log Playwright)
- page-2026-04-07T19-54-54-534Z.yml — (page state Playwright)
- page-2026-04-07T19-55-27-870Z.yml — (page state Playwright)

### 📁 /meta/mocs/
- MOC - Design Systems Budamix.md — MOC — Design Systems Budamix
- MOC - Extratos Financeiros.md — MOC — Extratos Financeiros
- MOC - Governanca OpenClaw.md — MOC — Governanca OpenClaw
- MOC - Listing Pipeline.md — MOC — Listing Pipeline
- MOC - Supabase Ecosystem.md — MOC — Supabase Ecosystem
- MOC - Superpowers Pipeline.md — MOC — Superpowers Pipeline
- MOC - Taxas e Precificacao.md — MOC — Taxas e Precificacao
- MOC - Token Management.md — MOC — Token Management
- auditoria-conexoes-2026-04-10.md — Auditoria de Conexões do Vault — 10/04/2026

### 📁 /agents/builder/
- AGENTS.md — AGENTS.md — Builder
- HEARTBEAT.md — HEARTBEAT.md — Builder
- IDENTITY.md — IDENTITY.md — Builder
- MEMORY.md — MEMORY.md — Builder
- SOUL.md — SOUL.md — Builder
- TOOLS.md — TOOLS.md — Cheat Sheet Rápido
- USER.md — USER.md — Contexto do Operador

### 📁 /agents/builder/memory/context/
- decisions.md — Decisões — Builder
- lessons.md — Lições — Builder
- stack.md — Stack & Padrões — Builder

### 📁 /agents/builder/memory/
- pending.md — Pendências — Builder

### 📁 /agents/builder/memory/projects/
- atlas-finance.md — Projeto: Atlas Finance Suite
- bidspark.md — Projeto: Bidspark
- canguu.md — Projeto: Canguu
- simulimport.md — Projeto: SimulImport

### 📁 /agents/fisco/
- AGENTS.md — AGENT.md — Arquitetura Técnica do Agente Fisco
- HEARTBEAT.md — HEARTBEAT.md
- IDENTITY.md — IDENTITY.md — Fisco v1.0
- MEMORY.md — MEMORY.md - Long-Term Memory
- SOUL.md — SOUL.md — Fisco v2.0
- TOOLS.md — TOOLS.md — Agente Fisco
- USER.md — USER.md — Pedro Broglio

### 📁 /agents/kobe/
- AGENTS.md — AGENTS.md — Regras Operacionais do Kobe
- BOOT.md — BOOT.md — Checklist de Startup
- BOOTSTRAP.md — BOOTSTRAP.md — Bootstrap Operacional + Recuperação de Contexto
- CHANGELOG.md — CHANGELOG — Evolução Contínua do Kobe
- HEARTBEAT.md — HEARTBEAT — Checklist Proativo do Kobe
- IDENTITY.md — IDENTITY.md — Kobe
- MEMORY.md — MEMORY.md — Índice Central de Memória
- SOUL.md — SOUL.md — Quem eu sou
- TOOLS.md — TOOLS.md — Infraestrutura e Dispositivos
- USER.md — USER.md — Pedro Broglio

### 📁 /agents/kobe/shared/
- TEAM.md — TEAM.md — Time Kobe
- rh-agent-briefing.md — BRIEFING COMPLETO — Agente RH

### 📁 /agents/kobe/shared/builder/
- MEMORY.md — MEMORY.md — Índice de Memória do Builder
- SOUL.md — SOUL.md — Builder v1.0

### 📁 /agents/kobe/shared/builder/memory/
- decisions.md — Decisões — Builder
- lessons.md — Lições Aprendidas — Builder
- pending.md — Pendências — Builder

### 📁 /agents/kobe/shared/builder/memory/sessions/
- 2026-03-24.md — Builder — Sessão 2026-03-24
- 2026-03-26.md — Builder — Sessão 2026-03-26
- 2026-03-27.md — Builder — Sessão 2026-03-27
- 2026-03-29.md — Builder Sessions — 2026-03-29
- 2026-03-30.md — Builder Sessions — 2026-03-30
- 2026-04-05.md — Builder — Sessões 2026-04-05
- 2026-04-06.md — Builder — Sessões 2026-04-06
- 2026-04-07.md — Builder — Sessões 2026-04-07
- 2026-04-08.md — Builder — Sessões 2026-04-08
- 2026-04-09.md — Builder — Sessões 2026-04-09

### 📁 /agents/kobe/shared/fisco/
- IDENTITY.md — IDENTITY.md — Fisco v1.0
- MEMORY.md — MEMORY.md — Índice de Memória do Fisco v1.0
- SOUL.md — SOUL.md — Fisco v2.0

### 📁 /agents/kobe/shared/fisco/memory/
- accounts.md — Accounts — Integrações do Fisco
- decisions.md — Decisões — Fisco
- lessons.md — Lições — Fisco
- nfe-log.md — Log de Auditoria Fiscal — NF-e
- pending.md — Pendências — Fisco
- playbook.md — Playbook Fiscal — Fisco

### 📁 /agents/kobe/shared/fisco/memory/context/
- business.md — Contexto Fiscal do Negócio — GB Importadora
- decisions.md — Decisões Fiscais
- lessons.md — Lições do Fisco

### 📁 /agents/kobe/shared/fisco/memory/sessions/
- TEMPLATE.md — Operação Fiscal — YYYY-MM-DD

### 📁 /agents/kobe/shared/fisco/reference/
- session-nf-planning-20260331.md — Session: 2026-04-01 00:19:22 UTC

### 📁 /agents/kobe/shared/fisco/skills/bling-nfe/
- SKILL.md — SKILL — Emissão de NF-e via Bling API v3

### 📁 /agents/kobe/shared/fisco/skills/distribution/
- SKILL.md — Skill: Motor de Distribuição (Módulo A)

### 📁 /agents/kobe/shared/fisco/skills/nf-internal/
- SKILL.md — Skill: NFs Venda Interna Filial→Simples (Módulo C)

### 📁 /agents/kobe/shared/fisco/skills/nf-transfer/
- SKILL.md — Skill: NF Transferência Matriz→Filial (Módulo B)

### 📁 /agents/kobe/shared/fisco/skills/reconciliation/
- SKILL.md — Skill: Conciliação Fisco (Módulo D)

### 📁 /agents/kobe/shared/fisco/skills/simples-monitor/
- SKILL.md — Skill: Monitor de Limites Simples Nacional (Módulo E)

### 📁 /agents/kobe/shared/fisco/templates/
- distribution-report.md — Relatório de Distribuição de Estoque
- reconciliation-report.md — Relatório de Conciliação Fisco

### 📁 /agents/kobe/shared/lessons/reviews/
- builder-2026-03-26.md — Review Semanal — Builder — 2026-03-26
- spark-2026-03-26.md — Review Semanal — Spark — 2026-03-26
- trader-2026-03-26.md — Review Semanal — Trader — 2026-03-26

### 📁 /agents/kobe/shared/outputs/
- trader-AGENTS.md — AGENTS.md — Trader
- trader-IDENTITY-v2.md — IDENTITY.md — Trader
- trader-IDENTITY.md — IDENTITY.md — Trader
- trader-MEMORY.md — MEMORY.md — Trader
- trader-SOUL.md — SOUL.md — Trader v1.0
- trader-decisions.md — Decisões — Trader
- trader-lessons.md — Lições — Trader
- trader-pending.md — Pendências — Trader
- trader-platforms.md — Plataformas — Contexto Operacional

### 📁 /agents/kobe/shared/rh/
- SOUL.md — SOUL.md — Agente RH (GB Importadora / Budamix)

### 📁 /agents/kobe/shared/rh/knowledge/
- regras-ponto-certo.md — Knowledge File — Regras do Sistema Ponto Certo

### 📁 /agents/kobe/shared/rh/memory/
- instructions.md — Instruções Operacionais — Agente RH
- pending.md — Pendências — Agente RH
- people.md — Funcionários GB Importadora

### 📁 /agents/kobe/shared/rh/memory/context/
- decisions.md — Decisões de RH
- lessons.md — Lições — Agente RH

### 📁 /agents/kobe/shared/rh/skills/comunicacao-funcionarios/
- SKILL.md — SKILL — Comunicação Humanizada com Funcionários (Módulo C)

### 📁 /agents/kobe/shared/rh/skills/monitor-ponto/
- SKILL.md — SKILL — Monitor de Ponto (Módulo A)

### 📁 /agents/kobe/shared/rh/templates/
- alerta-risco.md — ALERTA DE RISCO TRABALHISTA
- comunicado-ferias.md — Comunicado de Férias
- relatorio-diario.md — Relatório de Ponto — {DATA}
- relatorio-mensal-contador.md — Relatório Mensal — {MES}/{ANO}
- relatorio-semanal.md — Relatório Semanal de Banco de Horas — Semana {SEMANA}

### 📁 /agents/kobe/shared/simulimport/
- reforma-tributaria-importacao.md — Reforma Tributária Brasileira (EC 132/2023 + LC 214/2025) — Impacto na Importação

### 📁 /agents/kobe/shared/spark/
- BRIEFING-spark-ads-mvp.md — BRIEFING: Spark Ads — MVP (Fase 1)
- CHANGELOG-skills-v2.md — CHANGELOG — Skills do Spark v1.0 → v2.0
- CHANGELOG-v2.md — CHANGELOG — Spark Memory Pack v1.0 → v2.0
- FASE2-CAPACITACAO-SPARK.md — Fase 2 — Capacitação do Agente Spark
- IDENTITY.md — IDENTITY.md — Spark v2.0
- MEMORY.md — MEMORY.md — Índice de Memória do Spark v2.0
- SOUL.md — SOUL.md — Spark v2.0
- SPARK-ADS-MANAGEMENT-PLAN.md — Spark Ads Management System — Plano Completo

### 📁 /agents/kobe/shared/spark/memory/
- accounts.md — Contas de Anúncio — Spark v2.0
- pending.md — Pendências — Spark
- playbook.md — Playbook Operacional — Spark v2.0

### 📁 /agents/kobe/shared/spark/memory/campaigns/
- active.md — Campanhas Ativas — Spark
- history.md — Histórico de Campanhas — Spark

### 📁 /agents/kobe/shared/spark/memory/context/
- business.md — Contexto do Negócio — Spark v2.0
- decisions.md — Decisões Permanentes — Spark v2.0
- lessons.md — Lições Aprendidas — Spark v2.0

### 📁 /agents/kobe/shared/spark/memory/sessions/
- 2026-03-21.md — Spark — Sessão 2026-03-21
- 2026-03-22.md — Spark — Sessão 2026-03-22
- 2026-03-23.md — Spark — Sessão 2026-03-23
- 2026-03-24.md — Spark — Sessão 2026-03-24
- 2026-03-26.md — Spark — Sessão 2026-03-26
- 2026-03-27.md — Spark — Sessão 2026-03-27
- 2026-04-05.md — Spark — Sessões 2026-04-05
- 2026-04-06.md — Spark — Sessões 2026-04-06
- 2026-04-07.md — Spark — Sessões 2026-04-07
- 2026-04-08.md — Spark — Sessões 2026-04-08
- 2026-04-09.md — Spark — Sessões 2026-04-09
- TEMPLATE.md — Sessão — YYYY-MM-DD

### 📁 /agents/kobe/shared/spark/skills/anomaly-detector/
- SKILL.md — Skill: Anomaly Detector — Spark v2.0

### 📁 /agents/kobe/shared/spark/skills/budget-optimizer/
- SKILL.md — Skill: Budget Optimizer — Spark v2.0

### 📁 /agents/kobe/shared/spark/skills/google-ads/
- SKILL.md — Skill: Google Ads — Spark v2.0

### 📁 /agents/kobe/shared/spark/skills/meta-ads/
- SKILL.md — Skill: Meta Ads — Spark v2.0

### 📁 /agents/kobe/shared/trader/
- SOUL.md — SOUL.md — Trader v1.0
- etapa2-identity.md — IDENTITY.md — Trader
- etapa3-decisions.md — Decisões — Trader
- etapa3-lessons.md — Lições — Trader
- etapa3-memory.md — MEMORY.md — Trader
- etapa3-pending.md — Pendências — Trader
- etapa3-platforms.md — Plataformas — Contexto Operacional
- etapa5-agents.md — AGENTS.md — Trader

### 📁 /agents/kobe/shared/trader/memory/context/
- decisions.md — Decisões — Trader
- lessons.md — Lições Aprendidas — Trader

### 📁 /agents/kobe/shared/trader/memory/
- pending.md — Pendências — Trader

### 📁 /agents/kobe/shared/trader/memory/sessions/
- 2026-03-24.md — Trader — Sessão 2026-03-24
- 2026-03-26.md — Trader — Sessão 2026-03-26
- 2026-03-27.md — Trader — Sessão 2026-03-27
- 2026-04-05.md — Trader — Sessões 2026-04-05
- 2026-04-06.md — Trader — Sessões 2026-04-06
- 2026-04-07.md — Trader — Sessões 2026-04-07
- 2026-04-08.md — Trader — Sessões 2026-04-08
- 2026-04-09.md — Trader — Sessões 2026-04-09

### 📁 /agents/rh/
- AGENTS.md — AGENTS.md — Agente RH (GB Importadora / Budamix)
- HEARTBEAT.md — HEARTBEAT.md
- IDENTITY.md — IDENTITY.md — Agente RH
- SOUL.md — SOUL.md — Agente RH
- TOOLS.md — TOOLS.md — Agente RH
- USER.md — USER.md — Pedro Broglio

### 📁 /agents/spark/
- AGENTS.md — AGENTS.md — Spark
- HEARTBEAT.md — HEARTBEAT.md — Spark
- IDENTITY.md — IDENTITY.md — Spark
- MEMORY.md — MEMORY.md — Spark
- SOUL.md — SOUL.md — Spark
- TOOLS.md — TOOLS.md — Cheat Sheet Rápido
- USER.md — USER.md — Contexto do Operador

### 📁 /agents/spark/memory/context/
- accounts.md — Contas de Anúncio — Spark
- decisions.md — Decisões — Spark
- lessons.md — Lições — Spark

### 📁 /agents/spark/memory/
- pending.md — Pendências — Spark

### 📁 /agents/trader/
- AGENTS.md — AGENTS.md — Trader
- HEARTBEAT.md — HEARTBEAT.md — Trader
- IDENTITY.md — IDENTITY.md — Trader
- MEMORY.md — MEMORY.md — Trader
- SOUL.md — SOUL.md — Trader
- TOOLS.md — TOOLS.md — Cheat Sheet Rápido
- USER.md — USER.md — Contexto do Operador

### 📁 /agents/trader/memory/context/
- decisions.md — Decisões — Trader
- lessons.md — Lições — Trader
- marketplace-algorithms.md — Algoritmos de Ranking — Mercado Livre, Shopee e Amazon BR
- platforms.md — Plataformas — Contexto Operacional

### 📁 /agents/trader/memory/
- pending.md — Pendências — Trader

### 📁 /memory/context/
- business-context.md — Contexto Geral — Pedro Broglio
- deadlines.md — Deadlines — Fonte de Verdade
- dev-projects-local.md — Projetos de Código — Máquina Local (~/Documents/05-Projetos-Codigo/)
- pendencias.md — Pendências Ativas
- people.md — Pessoas — Equipe e Contatos

### 📁 /memory/context/decisoes/
- 2026-04.md — Decisões — Abril 2026

### 📁 /memory/projects/
- _index.md — Projetos — Índice Geral
- gb-import-hub-edge-functions-map.md — GB Import Hub — Edge Functions Map
- gb-import-hub-reconnection-plan.md — GB Import Hub — Plano de Reconexao do Frontend
- gb-import-hub-schema.md — GB Import Hub — Schema Completo do Banco de Dados
- shopee-porta-copos-analise.md — Análise Shopee — Kit 6 Porta-Copos MDF Design Solaris Budamix

### 📁 /memory/sessions/
- 2026-04-06.md — Sessão — 2026-04-06
- 2026-04-07.md — Sessão — 2026-04-07
- 2026-04-08.md — Sessão — 2026-04-08
- 2026-04-09.md — Sessão — 2026-04-09
- 2026-04-10.md — Sessão — 2026-04-10
- 2026-04-13.md — Sessão — 2026-04-13
- 2026-04-14.md — Sessão — 2026-04-14

### 📁 /scripts/
- brain-boot.sh — (script de boot do segundo cérebro)

### 📁 /skills/amazon-listing-creator/
- SKILL.md — (skill definition)

### 📁 /skills/amazon-listing-creator/reference/
- known-product-types.md — Product Types Conhecidos — Amazon BR

### 📁 /skills/amazon-listing-creator/rules/
- field-formats.md — Formatos Exatos de Campos SP-API — Amazon BR
- validation-rules.md — Regras de Validacao — Amazon Listing Creator

### 📁 /skills/amazon-listing-creator/templates/
- bullet-points-template.md — Template de Bullet Points Amazon BR — Budamix
- checklist.md — Checklist Pre-Submissao Amazon BR — Budamix
- description-template.md — Template de Descricao Amazon BR — Budamix

### 📁 /skills/coaching-corrida/
- SKILL.md — Coach de Corrida — Skill do Kobe

### 📁 /skills/coaching-corrida/assets/
- plano-unificado.xlsx — (planilha de treino)

### 📁 /skills/coaching-corrida/references/
- knowledge-base.md — Expert em Coaching de Corrida — Knowledge File

### 📁 /skills/design/animated-financial-display/
- README.md — Animated Financial Display
- SKILL.md — Animated Financial Display
- _meta.json — (metadata)

### 📁 /skills/design/animated-financial-display/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/design/data-visualization-2/
- SKILL.md — Data Visualization
- _meta.json — (metadata)

### 📁 /skills/design/data-visualization-2/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/design/
- excel-design-system.md — Excel Design System — GB Importadora

### 📁 /skills/design/financial-design-systems/
- README.md — Financial Data Visualization
- SKILL.md — Financial Data Visualization
- _meta.json — (metadata)

### 📁 /skills/design/financial-design-systems/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/design/frontend-design-ultimate/
- README.md — Frontend Design Ultimate
- REVIEW.md — Skill Review: frontend-design-ultimate
- SKILL.md — (skill definition)
- _meta.json — (metadata)

### 📁 /skills/design/frontend-design-ultimate/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/design/frontend-design-ultimate/references/
- design-philosophy.md — Design Philosophy — Anti-AI-Slop Manifesto
- mobile-patterns.md — Mobile-First Patterns
- shadcn-components.md — shadcn/ui Component Reference

### 📁 /skills/design/frontend-design-ultimate/scripts/
- bundle-artifact.sh — (bundle script)
- init-nextjs.sh — (init Next.js project)
- init-vite.sh — (init Vite project)

### 📁 /skills/design/frontend-design-ultimate/templates/
- site-config.ts — (site config template)

### 📁 /skills/design/lb-motion-skill/
- README.md — Motion.dev Documentation Skill
- SKILL.md — (skill definition)
- _meta.json — (metadata)

### 📁 /skills/design/lb-motion-skill/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/design/lb-motion-skill/docs/
- quick-start.md — Get started with Motion

### 📁 /skills/design/lovable-quality/
- SKILL.md — (skill definition)

### 📁 /skills/design/report-design-system/
- SKILL.md — Design System — Relatórios OpenClaw (Curso)

### 📁 /skills/design/shadcn-ui/
- SKILL.md — (skill definition)
- _meta.json — (metadata)

### 📁 /skills/design/shadcn-ui/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/design/superdesign/
- SKILL.md — Frontend Design Skill
- _meta.json — (metadata)

### 📁 /skills/design/superdesign/.clawhub/
- origin.json — (clawhub origin)

### 📁 /skills/dev/fullstack-dev/
- SKILL.md — (skill definition)

### 📁 /skills/dev/fullstack-dev/assets/nextjs-starter/
- .env.example — (env example)
- next.config.ts — (Next.js config)
- package.json — (package.json)
- tsconfig.json — (TypeScript config)

### 📁 /skills/dev/fullstack-dev/assets/nextjs-starter/src/app/
- layout.tsx — (Next.js root layout)

### 📁 /skills/dev/fullstack-dev/assets/nextjs-starter/src/lib/
- utils.ts — (utility functions)

### 📁 /skills/dev/fullstack-dev/references/
- ai-integration.md — AI Integration Reference — OpenAI, Claude, Streaming, RAG, pgvector
- auth-security.md — Auth & Security Reference — Supabase Auth, RBAC, RLS, OWASP
- backend.md — Backend Reference — Node/Fastify, FastAPI, APIs
- database.md — Database Reference — PostgreSQL, Supabase, Drizzle, Redis
- frontend.md — Frontend Reference — React 19, Next.js 15, shadcn/ui, State
- infrastructure.md — Infrastructure Reference — Docker, Nginx, PM2, Vercel, CI/CD
- saas-patterns.md — SaaS Patterns — Stripe, Multi-Tenancy, Feature Flags, Onboarding
- testing.md — Testing Reference — Vitest, Playwright, E2E, Mocking
- typescript-patterns.md — TypeScript Patterns — Avançado, Generics, Zod, Strict Mode

### 📁 /skills/dev/fullstack-dev/scripts/
- deploy-vps.sh — (deploy to VPS script)
- init-fastapi-project.sh — (init FastAPI project)
- init-nextjs-project.sh — (init Next.js project)

### 📁 /skills/excel-generation/
- SKILL.md — Skill: Programmatic Excel Generation (Professional/Corporate Grade)

### 📁 /skills/financeiro/stripe-api/
- SKILL.md — Stripe API — Operador Completo

### 📁 /skills/financeiro/stripe-api/references/
- m01-pagamentos.md — Módulo 1 — Cobranças e Pagamentos
- m02-clientes.md — Módulo 2 — Gestão de Clientes
- m03-produtos-precos.md — Módulo 3 — Produtos e Preços
- m04-assinaturas.md — Módulo 4 — Assinaturas Recorrentes
- m05-faturas.md — Módulo 5 — Faturas
- m06-financeiro.md — Módulo 6 — Relatórios Financeiros
- m07-webhooks.md — Módulo 7 — Webhooks
- m08-paginacao.md — Módulo 8 — Paginação e Expand
- m09-erros.md — Módulo 9 — Tratamento de Erros

### 📁 /skills/gb-import-hub/
- SKILL.md — GB Import Hub - Skill de Acesso ao Sistema de Importacoes
- SKILL.md.bak — (backup)

### 📁 /skills/gb-import-hub/references/
- schema-tables.md — GB Import Hub — Schema Completo do Banco de Dados

### 📁 /skills/integracao/instagram/
- SKILL.md — Instagram — Consulta de Perfis e Posts

### 📁 /skills/integracao/instagram/scripts/
- instagram.sh — (script Instagram)

### 📁 /skills/marketing/anomaly-detector/
- SKILL.md — (skill definition)

### 📁 /skills/marketing/budget-optimizer/
- SKILL.md — (skill definition)

### 📁 /skills/marketing/google-ads/
- SKILL.md — (skill definition)

### 📁 /skills/marketing/meta-ads/
- SKILL.md — (skill definition)

### 📁 /skills/marketing/meta-ads/references/
- api-reference.md — Meta Marketing API — Referência Completa
- audience-targeting.md — Segmentação e Públicos — Meta Ads
- campaign-guide.md — Guia de Criação de Campanhas — Meta Ads
- creative-specs.md — Especificações de Criativos — Meta Ads
- ecommerce-strategy.md — Meta Ads para E-commerce — Estratégia GB Importadora
- optimization-guide.md — Otimização e Bidding — Meta Ads

### 📁 /skills/marketing/meta-ads/scripts/
- meta-ads-create.py — (criação de anúncios Meta)
- meta-ads-report.py — (relatório Meta Ads)
- meta-ads-rules.py — (regras Meta Ads)

### 📁 /skills/marketplace/amazon-extrato/
- SKILL.md — Extrato Financeiro — Amazon BR (SP-API)

### 📁 /skills/marketplace/amazon-extrato/references/
- classificacoes.md — Classificações de Transação — Extrato Amazon BR
- colunas.md — Referência de Colunas — Extrato Amazon BR
- nomenclatura-unificada.md — Nomenclatura Unificada — Mercado Livre ↔ Shopee ↔ Amazon

### 📁 /skills/marketplace/amazon-extrato/scripts/
- amazon-extrato.py — (extrato Amazon script)

### 📁 /skills/marketplace/amazon-fees-rules/
- SKILL.md — (skill definition)

### 📁 /skills/marketplace/consolidado-financeiro/
- SKILL.md — Consolidado Financeiro — Marketplaces

### 📁 /skills/marketplace/consolidado-financeiro/scripts/
- enhance-consolidado.py — (enhance consolidado script)

### 📁 /skills/marketplace/marketplace-optimization/
- SKILL.md — Marketplace Optimization — Playbook Operacional GB Importadora

### 📁 /skills/marketplace/marketplace-optimization/references/
- amazon-ranking.md — Amazon Brasil — Algoritmo A10, Buy Box e Estratégias
- cross-platform-matrix.md — Análise Cruzada — Matriz Comparativa e Estratégia Multi-Plataforma
- ml-ranking.md — Mercado Livre — Algoritmo, Fatores e Estratégias
- optimization-playbook.md — Optimization Playbook — Framework Unificado GB Importadora
- shopee-ranking.md — Shopee — Algoritmo, Fatores e Estratégias

### 📁 /skills/marketplace/marketplace-report/
- SKILL.md — Relatório de Performance — Marketplaces

### 📁 /skills/marketplace/marketplace-report/assets/
- budamix-logo-teal.png — (logo Budamix teal)
- budamix-logo-white.png — (logo Budamix white)

### 📁 /skills/marketplace/marketplace-report/references/
- estrutura-relatorio.md — Estrutura do Relatório — 9 Seções
- paleta-cores.md — Paleta de Cores — Budamix / GB Importadora

### 📁 /skills/marketplace/marketplace-report/scripts/
- charts.py — (geração de gráficos)
- report-engine.py — (engine principal do relatório)

### 📁 /skills/marketplace/marketplace-report/scripts/connectors/
- __init__.py — (init connectors)
- amazon.py — (conector Amazon)
- mercadolivre.py — (conector Mercado Livre)
- shopee.py — (conector Shopee)

### 📁 /skills/marketplace/marketplace-report/scripts/sections/
- __init__.py — (init sections)
- helpers.py — (helpers para seções)
- icons.py — (ícones para seções)
- s01_capa.py — (seção 1: capa)
- s02_faturamento.py — (seção 2: faturamento)
- s03_vendas.py — (seção 3: vendas)
- s04_trafego.py — (seção 4: tráfego)
- s05_ads.py — (seção 5: ads)
- s06_reputacao.py — (seção 6: reputação)
- s07_logistica.py — (seção 7: logística)
- s08_catalogo.py — (seção 8: catálogo)
- s09_estrategia.py — (seção 9: estratégia)

### 📁 /skills/marketplace/
- ml-ads-api-reference.pdf — (PDF referência ML Ads API)
- shopee-api-reference.pdf — (PDF referência Shopee API)

### 📁 /skills/marketplace/ml-ads/
- SKILL.md — ML Ads — Product Ads Mercado Livre

### 📁 /skills/marketplace/ml-ads/references/
- endpoints.md — Endpoints — ML Ads API v2

### 📁 /skills/marketplace/ml-competitor-analysis/
- SKILL.md — (skill definition)

### 📁 /skills/marketplace/ml-competitor-analysis/cases/
- pote-1520ml-kit2-2026-03-18.md — Case: Kit 2 Potes Vidro 1520ml Retangular — 2026-03-18

### 📁 /skills/marketplace/ml-competitor-analysis/scripts/
- fetch_ml_search.py — (fetch ML search results)
- parse_ml_search.py — (parse ML search results)

### 📁 /skills/marketplace/ml-extrato/
- SKILL.md — Extrato Financeiro — Mercado Livre / Mercado Pago

### 📁 /skills/marketplace/ml-extrato/references/
- colunas.md — Referência de Colunas — Extrato ML

### 📁 /skills/marketplace/ml-extrato/scripts/
- ml-extrato.py — (extrato ML script)
- ml-refresh-token.sh — (refresh token ML)

### 📁 /skills/marketplace/ml-fees-rules/
- SKILL.md — (skill definition)

### 📁 /skills/marketplace/ml-report/
- DEPRECATED.md — DEPRECATED — migrado para marketplace-report
- SKILL.md — ml-report — Relatório de Performance ML

### 📁 /skills/marketplace/ml-report/assets/
- budamix-logo-teal.png — (logo Budamix teal)
- budamix-logo-white.png — (logo Budamix white)

### 📁 /skills/marketplace/ml-report/references/
- estrutura-relatorio.md — Estrutura do Relatório — 9 Seções
- paleta-cores.md — Paleta de Cores — Budamix / GB Importadora

### 📁 /skills/marketplace/ml-report/scripts/
- ml-charts.py — (gráficos ML)
- ml-report.py — (relatório ML)

### 📁 /skills/marketplace/ml-report/scripts/sections/
- __init__.py — (init sections)
- helpers.py — (helpers para seções)
- s01_capa.py — (seção 1: capa)
- s02_faturamento.py — (seção 2: faturamento)
- s03_vendas.py — (seção 3: vendas)
- s04_trafego.py — (seção 4: tráfego)
- s05_ads.py — (seção 5: ads)
- s06_reputacao.py — (seção 6: reputação)
- s07_logistica.py — (seção 7: logística)
- s08_catalogo.py — (seção 8: catálogo)
- s09_estrategia.py — (seção 9: estratégia)

### 📁 /skills/marketplace/shopee-extrato/
- SKILL.md — Extrato Financeiro — Shopee / Budamix (Multi-Conta)

### 📁 /skills/marketplace/shopee-extrato/references/
- classificacoes.md — Classificações de Transação — Extrato Shopee
- colunas.md — Referência de Colunas — Extrato Shopee
- nomenclatura-unificada.md — Nomenclatura Unificada — Mercado Livre ↔ Shopee

### 📁 /skills/marketplace/shopee-extrato/scripts/
- shopee-extrato.py — (extrato Shopee script)

### 📁 /skills/marketplace/shopee-fees-rules/
- SKILL.md — (skill definition)

### 📁 /skills/obsidian-vault-manager/
- SKILL.md — (skill definition)

### 📁 /skills/operations/inventory-management/
- SKILL.md — Gestão de Estoque — GB Importadora

### 📁 /skills/perplexity/scripts/
- search.mjs — (Perplexity search script)

### 📁 /skills/research/deep-research-protocol/
- SKILL.md — (skill definition)

### 📁 /skills/shopee-listing-creator/
- SKILL.md — (skill definition)

### 📁 /skills/shopee-listing-creator/rules/
- validation-rules.md — Regras de Validacao — Shopee Listing Creator

### 📁 /skills/shopee-listing-creator/templates/
- checklist.md — Checklist Pre-Publicacao Shopee — Budamix
- description-template.md — Template de Descricao Shopee — Budamix

### 📁 /skills/spreadsheet-pricing/
- SKILL.md — (skill definition)

### 📁 /skills/spreadsheet-pricing/maps/
- amazon-columns.md — Mapeamento de Colunas — ABA AMAZON
- estoque-columns.md — Mapeamento de Colunas — ABA ESTOQUE
- meli-columns.md — Mapeamento de Colunas — ABA MELI
- shopee-columns.md — Mapeamento de Colunas — ABA SHOPEE

### 📁 /skills/spreadsheet-pricing/rules/
- format-rules.md — Regras de Formato — Spreadsheet Pricing
- formula-protection.md — Protecao de Formulas — Spreadsheet Pricing

### 📁 /skills/strategic-planner/
- SKILL.md — Skill: Strategic Planner

### 📁 /skills/strategic-planner/references/
- template-deep.md — Template Deep — Planejamento Estratégico Completo
- template-lite.md — Template Lite — Planejamento Rápido
- template-standard.md — Template Standard — Planejamento Estruturado

### 📁 /skills/superpowers/brainstorming/
- SKILL.md — Brainstorming Ideas Into Designs
- spec-document-reviewer-prompt.md — Spec Document Reviewer Prompt Template
- visual-companion.md — Visual Companion Guide

### 📁 /skills/superpowers/brainstorming/scripts/
- frame-template.html — (frame template HTML)
- helper.js — (helper JS)
- server.cjs — (server CommonJS)
- start-server.sh — (start server script)
- stop-server.sh — (stop server script)

### 📁 /skills/superpowers/dispatching-parallelopenclaw/agents/
- SKILL.md — Dispatching Parallel Agents

### 📁 /skills/superpowers/executing-plans/
- SKILL.md — Executing Plans

### 📁 /skills/superpowers/finishing-a-development-branch/
- SKILL.md — Finishing a Development Branch

### 📁 /skills/superpowers/receiving-code-review/
- SKILL.md — Code Review Reception

### 📁 /skills/superpowers/requesting-code-review/
- SKILL.md — Requesting Code Review
- code-reviewer.md — Code Review Agent

### 📁 /skills/superpowers/subagent-driven-development/
- SKILL.md — Subagent-Driven Development
- code-quality-reviewer-prompt.md — Code Quality Reviewer Prompt Template
- implementer-prompt.md — Implementer Subagent Prompt Template
- spec-reviewer-prompt.md — Spec Compliance Reviewer Prompt Template

### 📁 /skills/superpowers/systematic-debugging/
- CREATION-LOG.md — Creation Log: Systematic Debugging Skill
- SKILL.md — Systematic Debugging
- condition-based-waiting-example.ts — (TypeScript example)
- condition-based-waiting.md — Condition-Based Waiting
- defense-in-depth.md — Defense-in-Depth Validation
- find-polluter.sh — (find test polluter script)
- root-cause-tracing.md — Root Cause Tracing
- test-academic.md — Academic Test: Systematic Debugging Skill
- test-pressure-1.md — Pressure Test 1: Emergency Production Fix
- test-pressure-2.md — Pressure Test 2: Sunk Cost + Exhaustion
- test-pressure-3.md — Pressure Test 3: Authority + Social Pressure

### 📁 /skills/superpowers/test-driven-development/
- SKILL.md — Test-Driven Development (TDD)
- testing-anti-patterns.md — Testing Anti-Patterns

### 📁 /skills/superpowers/using-git-worktrees/
- SKILL.md — Using Git Worktrees

### 📁 /skills/superpowers/using-superpowers/
- SKILL.md — (skill definition)

### 📁 /skills/superpowers/using-superpowers/references/
- codex-tools.md — Codex Tool Mapping
- gemini-tools.md — Gemini CLI Tool Mapping

### 📁 /skills/superpowers/verification-before-completion/
- SKILL.md — Verification Before Completion

### 📁 /skills/superpowers/writing-plans/
- SKILL.md — Writing Plans
- plan-document-reviewer-prompt.md — Plan Document Reviewer Prompt Template

### 📁 /skills/superpowers/writing-skills/
- SKILL.md — Writing Skills
- anthropic-best-practices.md — Skill authoring best practices
- graphviz-conventions.dot — (Graphviz conventions)
- persuasion-principles.md — Persuasion Principles for Skill Design
- render-graphs.js — (render graphs script)
- testing-skills-with-subagents.md — Testing Skills With Subagents

### 📁 /skills/superpowers/writing-skills/examples/
- CLAUDE_MD_TESTING.md — Testing CLAUDE.md Skills Documentation

### 📁 /skills/update-ml-return-rates/
- SKILL.md — Skill: update-ml-return-rates
- update-return-rates.py — (update return rates script)

### 📁 /skills/whatsapp-ultimate/
- SKILL.md — (skill definition)
- _meta.json — (metadata)
- description.md — (descrição da skill)

### 📁 /skills/whatsapp-ultimate/scripts/
- apply-history-fix.sh — (apply history fix)
- apply-model-prefix.sh — (apply model prefix)
- wa-create-group.ts — (create WhatsApp group)
- wa-fetch-contacts.ts — (fetch WhatsApp contacts)

### 📁 / (raiz — arquivos ocultos/config)
- .gitignore — (git ignore rules)
- scheduled_tasks.lock — (lock de tarefas agendadas)

## Índice por Tipo

### Markdown (.md)
- _VAULT_MAP.md
- .claude/projects/-Users-pedrobroglio-segundo-cerebro/memory/feedback_shopee_brand.md
- meta/mocs/MOC - Design Systems Budamix.md
- meta/mocs/MOC - Extratos Financeiros.md
- meta/mocs/MOC - Governanca OpenClaw.md
- meta/mocs/MOC - Listing Pipeline.md
- meta/mocs/MOC - Supabase Ecosystem.md
- meta/mocs/MOC - Superpowers Pipeline.md
- meta/mocs/MOC - Taxas e Precificacao.md
- meta/mocs/MOC - Token Management.md
- meta/mocs/auditoria-conexoes-2026-04-10.md
- CLAUDE.md
- PROPAGATION.md
-openclaw/agents/builder/AGENTS.md
-openclaw/agents/builder/HEARTBEAT.md
-openclaw/agents/builder/IDENTITY.md
-openclaw/agents/builder/MEMORY.md
-openclaw/agents/builder/SOUL.md
-openclaw/agents/builder/TOOLS.md
-openclaw/agents/builder/USER.md
-openclaw/agents/builder/memory/context/decisions.md
-openclaw/agents/builder/memory/context/lessons.md
-openclaw/agents/builder/memory/context/stack.md
-openclaw/agents/builder/memory/pending.md
-openclaw/agents/builder/memory/projects/atlas-finance.md
-openclaw/agents/builder/memory/projects/bidspark.md
-openclaw/agents/builder/memory/projects/canguu.md
-openclaw/agents/builder/memory/projects/simulimport.md
-openclaw/agents/fisco/AGENTS.md
-openclaw/agents/fisco/HEARTBEAT.md
-openclaw/agents/fisco/IDENTITY.md
-openclaw/agents/fisco/MEMORY.md
-openclaw/agents/fisco/SOUL.md
-openclaw/agents/fisco/TOOLS.md
-openclaw/agents/fisco/USER.md
-openclaw/agents/kobe/AGENTS.md
-openclaw/agents/kobe/BOOT.md
-openclaw/agents/kobe/BOOTSTRAP.md
-openclaw/agents/kobe/CHANGELOG.md
-openclaw/agents/kobe/HEARTBEAT.md
-openclaw/agents/kobe/IDENTITY.md
-openclaw/agents/kobe/MEMORY.md
-openclaw/agents/kobe/SOUL.md
-openclaw/agents/kobe/TOOLS.md
-openclaw/agents/kobe/USER.md
-openclaw/agents/kobe/shared/TEAM.md
-openclaw/agents/kobe/shared/builder/MEMORY.md
-openclaw/agents/kobe/shared/builder/SOUL.md
-openclaw/agents/kobe/shared/builder/memory/decisions.md
-openclaw/agents/kobe/shared/builder/memory/lessons.md
-openclaw/agents/kobe/shared/builder/memory/pending.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-24.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-26.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-27.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-29.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-03-30.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-05.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-06.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-07.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-08.md
-openclaw/agents/kobe/shared/builder/memory/sessions/2026-04-09.md
-openclaw/agents/kobe/shared/fisco/IDENTITY.md
-openclaw/agents/kobe/shared/fisco/MEMORY.md
-openclaw/agents/kobe/shared/fisco/SOUL.md
-openclaw/agents/kobe/shared/fisco/memory/accounts.md
-openclaw/agents/kobe/shared/fisco/memory/context/business.md
-openclaw/agents/kobe/shared/fisco/memory/context/decisions.md
-openclaw/agents/kobe/shared/fisco/memory/context/lessons.md
-openclaw/agents/kobe/shared/fisco/memory/decisions.md
-openclaw/agents/kobe/shared/fisco/memory/lessons.md
-openclaw/agents/kobe/shared/fisco/memory/nfe-log.md
-openclaw/agents/kobe/shared/fisco/memory/pending.md
-openclaw/agents/kobe/shared/fisco/memory/playbook.md
-openclaw/agents/kobe/shared/fisco/memory/sessions/TEMPLATE.md
-openclaw/agents/kobe/shared/fisco/reference/session-nf-planning-20260331.md
-openclaw/agents/kobe/shared/fisco/skills/bling-nfe/SKILL.md
-openclaw/agents/kobe/shared/fisco/skills/distribution/SKILL.md
-openclaw/agents/kobe/shared/fisco/skills/nf-internal/SKILL.md
-openclaw/agents/kobe/shared/fisco/skills/nf-transfer/SKILL.md
-openclaw/agents/kobe/shared/fisco/skills/reconciliation/SKILL.md
-openclaw/agents/kobe/shared/fisco/skills/simples-monitor/SKILL.md
-openclaw/agents/kobe/shared/fisco/templates/distribution-report.md
-openclaw/agents/kobe/shared/fisco/templates/reconciliation-report.md
-openclaw/agents/kobe/shared/lessons/reviews/builder-2026-03-26.md
-openclaw/agents/kobe/shared/lessons/reviews/spark-2026-03-26.md
-openclaw/agents/kobe/shared/lessons/reviews/trader-2026-03-26.md
-openclaw/agents/kobe/shared/outputs/trader-AGENTS.md
-openclaw/agents/kobe/shared/outputs/trader-IDENTITY-v2.md
-openclaw/agents/kobe/shared/outputs/trader-IDENTITY.md
-openclaw/agents/kobe/shared/outputs/trader-MEMORY.md
-openclaw/agents/kobe/shared/outputs/trader-SOUL.md
-openclaw/agents/kobe/shared/outputs/trader-decisions.md
-openclaw/agents/kobe/shared/outputs/trader-lessons.md
-openclaw/agents/kobe/shared/outputs/trader-pending.md
-openclaw/agents/kobe/shared/outputs/trader-platforms.md
-openclaw/agents/kobe/shared/rh-agent-briefing.md
-openclaw/agents/kobe/shared/rh/SOUL.md
-openclaw/agents/kobe/shared/rh/knowledge/regras-ponto-certo.md
-openclaw/agents/kobe/shared/rh/memory/context/decisions.md
-openclaw/agents/kobe/shared/rh/memory/context/lessons.md
-openclaw/agents/kobe/shared/rh/memory/instructions.md
-openclaw/agents/kobe/shared/rh/memory/pending.md
-openclaw/agents/kobe/shared/rh/memory/people.md
-openclaw/agents/kobe/shared/rh/skills/comunicacao-funcionarios/SKILL.md
-openclaw/agents/kobe/shared/rh/skills/monitor-ponto/SKILL.md
-openclaw/agents/kobe/shared/rh/templates/alerta-risco.md
-openclaw/agents/kobe/shared/rh/templates/comunicado-ferias.md
-openclaw/agents/kobe/shared/rh/templates/relatorio-diario.md
-openclaw/agents/kobe/shared/rh/templates/relatorio-mensal-contador.md
-openclaw/agents/kobe/shared/rh/templates/relatorio-semanal.md
-openclaw/agents/kobe/shared/simulimport/reforma-tributaria-importacao.md
-openclaw/agents/kobe/shared/spark/BRIEFING-spark-ads-mvp.md
-openclaw/agents/kobe/shared/spark/CHANGELOG-skills-v2.md
-openclaw/agents/kobe/shared/spark/CHANGELOG-v2.md
-openclaw/agents/kobe/shared/spark/FASE2-CAPACITACAO-SPARK.md
-openclaw/agents/kobe/shared/spark/IDENTITY.md
-openclaw/agents/kobe/shared/spark/MEMORY.md
-openclaw/agents/kobe/shared/spark/SOUL.md
-openclaw/agents/kobe/shared/spark/SPARK-ADS-MANAGEMENT-PLAN.md
-openclaw/agents/kobe/shared/spark/memory/accounts.md
-openclaw/agents/kobe/shared/spark/memory/campaigns/active.md
-openclaw/agents/kobe/shared/spark/memory/campaigns/history.md
-openclaw/agents/kobe/shared/spark/memory/context/business.md
-openclaw/agents/kobe/shared/spark/memory/context/decisions.md
-openclaw/agents/kobe/shared/spark/memory/context/lessons.md
-openclaw/agents/kobe/shared/spark/memory/pending.md
-openclaw/agents/kobe/shared/spark/memory/playbook.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-21.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-22.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-23.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-24.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-26.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-03-27.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-05.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-06.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-07.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-08.md
-openclaw/agents/kobe/shared/spark/memory/sessions/2026-04-09.md
-openclaw/agents/kobe/shared/spark/memory/sessions/TEMPLATE.md
-openclaw/agents/kobe/shared/spark/skills/anomaly-detector/SKILL.md
-openclaw/agents/kobe/shared/spark/skills/budget-optimizer/SKILL.md
-openclaw/agents/kobe/shared/spark/skills/google-ads/SKILL.md
-openclaw/agents/kobe/shared/spark/skills/meta-ads/SKILL.md
-openclaw/agents/kobe/shared/trader/SOUL.md
-openclaw/agents/kobe/shared/trader/etapa2-identity.md
-openclaw/agents/kobe/shared/trader/etapa3-decisions.md
-openclaw/agents/kobe/shared/trader/etapa3-lessons.md
-openclaw/agents/kobe/shared/trader/etapa3-memory.md
-openclaw/agents/kobe/shared/trader/etapa3-pending.md
-openclaw/agents/kobe/shared/trader/etapa3-platforms.md
-openclaw/agents/kobe/shared/trader/etapa5-agents.md
-openclaw/agents/kobe/shared/trader/memory/context/decisions.md
-openclaw/agents/kobe/shared/trader/memory/context/lessons.md
-openclaw/agents/kobe/shared/trader/memory/pending.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-03-24.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-03-26.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-03-27.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-05.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-06.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-07.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-08.md
-openclaw/agents/kobe/shared/trader/memory/sessions/2026-04-09.md
-openclaw/agents/rh/AGENTS.md
-openclaw/agents/rh/HEARTBEAT.md
-openclaw/agents/rh/IDENTITY.md
-openclaw/agents/rh/SOUL.md
-openclaw/agents/rh/TOOLS.md
-openclaw/agents/rh/USER.md
-openclaw/agents/spark/AGENTS.md
-openclaw/agents/spark/HEARTBEAT.md
-openclaw/agents/spark/IDENTITY.md
-openclaw/agents/spark/MEMORY.md
-openclaw/agents/spark/SOUL.md
-openclaw/agents/spark/TOOLS.md
-openclaw/agents/spark/USER.md
-openclaw/agents/spark/memory/context/accounts.md
-openclaw/agents/spark/memory/context/decisions.md
-openclaw/agents/spark/memory/context/lessons.md
-openclaw/agents/spark/memory/pending.md
-openclaw/agents/trader/AGENTS.md
-openclaw/agents/trader/HEARTBEAT.md
-openclaw/agents/trader/IDENTITY.md
-openclaw/agents/trader/MEMORY.md
-openclaw/agents/trader/SOUL.md
-openclaw/agents/trader/TOOLS.md
-openclaw/agents/trader/USER.md
-openclaw/agents/trader/memory/context/decisions.md
-openclaw/agents/trader/memory/context/lessons.md
-openclaw/agents/trader/memory/context/marketplace-algorithms.md
-openclaw/agents/trader/memory/context/platforms.md
-openclaw/agents/trader/memory/pending.md
- memory/context/business-context.md
- memory/context/deadlines.md
- memory/context/dev-projects-local.md
- memory/context/decisoes/2026-04.md
- memory/context/pendencias.md
- memory/context/people.md
- memory/projects/_index.md
- memory/projects/gb-import-hub-edge-functions-map.md
- memory/projects/gb-import-hub-reconnection-plan.md
- memory/projects/gb-import-hub-schema.md
- memory/projects/shopee-porta-copos-analise.md
- memory/sessions/2026-04-06.md
- memory/sessions/2026-04-07.md
- memory/sessions/2026-04-08.md
- memory/sessions/2026-04-09.md
- memory/sessions/2026-04-10.md
- memory/sessions/2026-04-13.md
- skills/amazon-listing-creator/SKILL.md
- skills/amazon-listing-creator/reference/known-product-types.md
- skills/amazon-listing-creator/rules/field-formats.md
- skills/amazon-listing-creator/rules/validation-rules.md
- skills/amazon-listing-creator/templates/bullet-points-template.md
- skills/amazon-listing-creator/templates/checklist.md
- skills/amazon-listing-creator/templates/description-template.md
- skills/coaching-corrida/SKILL.md
- skills/coaching-corrida/references/knowledge-base.md
- skills/design/animated-financial-display/README.md
- skills/design/animated-financial-display/SKILL.md
- skills/design/data-visualization-2/SKILL.md
- skills/design/excel-design-system.md
- skills/design/financial-design-systems/README.md
- skills/design/financial-design-systems/SKILL.md
- skills/design/frontend-design-ultimate/README.md
- skills/design/frontend-design-ultimate/REVIEW.md
- skills/design/frontend-design-ultimate/SKILL.md
- skills/design/frontend-design-ultimate/references/design-philosophy.md
- skills/design/frontend-design-ultimate/references/mobile-patterns.md
- skills/design/frontend-design-ultimate/references/shadcn-components.md
- skills/design/lb-motion-skill/README.md
- skills/design/lb-motion-skill/SKILL.md
- skills/design/lb-motion-skill/docs/quick-start.md
- skills/design/lovable-quality/SKILL.md
- skills/design/report-design-system/SKILL.md
- skills/design/shadcn-ui/SKILL.md
- skills/design/superdesign/SKILL.md
- skills/dev/fullstack-dev/SKILL.md
- skills/dev/fullstack-dev/references/ai-integration.md
- skills/dev/fullstack-dev/references/auth-security.md
- skills/dev/fullstack-dev/references/backend.md
- skills/dev/fullstack-dev/references/database.md
- skills/dev/fullstack-dev/references/frontend.md
- skills/dev/fullstack-dev/references/infrastructure.md
- skills/dev/fullstack-dev/references/saas-patterns.md
- skills/dev/fullstack-dev/references/testing.md
- skills/dev/fullstack-dev/references/typescript-patterns.md
- skills/excel-generation/SKILL.md
- skills/financeiro/stripe-api/SKILL.md
- skills/financeiro/stripe-api/references/m01-pagamentos.md
- skills/financeiro/stripe-api/references/m02-clientes.md
- skills/financeiro/stripe-api/references/m03-produtos-precos.md
- skills/financeiro/stripe-api/references/m04-assinaturas.md
- skills/financeiro/stripe-api/references/m05-faturas.md
- skills/financeiro/stripe-api/references/m06-financeiro.md
- skills/financeiro/stripe-api/references/m07-webhooks.md
- skills/financeiro/stripe-api/references/m08-paginacao.md
- skills/financeiro/stripe-api/references/m09-erros.md
- skills/gb-import-hub/SKILL.md
- skills/integracao/instagram/SKILL.md
- skills/marketing/anomaly-detector/SKILL.md
- skills/marketing/budget-optimizer/SKILL.md
- skills/marketing/google-ads/SKILL.md
- skills/marketing/meta-ads/SKILL.md
- skills/marketing/meta-ads/references/api-reference.md
- skills/marketing/meta-ads/references/audience-targeting.md
- skills/marketing/meta-ads/references/campaign-guide.md
- skills/marketing/meta-ads/references/creative-specs.md
- skills/marketing/meta-ads/references/ecommerce-strategy.md
- skills/marketing/meta-ads/references/optimization-guide.md
- skills/marketplace/amazon-extrato/SKILL.md
- skills/marketplace/amazon-extrato/references/classificacoes.md
- skills/marketplace/amazon-extrato/references/colunas.md
- skills/marketplace/amazon-extrato/references/nomenclatura-unificada.md
- skills/marketplace/amazon-fees-rules/SKILL.md
- skills/marketplace/consolidado-financeiro/SKILL.md
- skills/marketplace/marketplace-optimization/SKILL.md
- skills/marketplace/marketplace-optimization/references/amazon-ranking.md
- skills/marketplace/marketplace-optimization/references/cross-platform-matrix.md
- skills/marketplace/marketplace-optimization/references/ml-ranking.md
- skills/marketplace/marketplace-optimization/references/optimization-playbook.md
- skills/marketplace/marketplace-optimization/references/shopee-ranking.md
- skills/marketplace/marketplace-report/SKILL.md
- skills/marketplace/marketplace-report/references/estrutura-relatorio.md
- skills/marketplace/marketplace-report/references/paleta-cores.md
- skills/marketplace/ml-ads/SKILL.md
- skills/marketplace/ml-ads/references/endpoints.md
- skills/marketplace/ml-competitor-analysis/SKILL.md
- skills/marketplace/ml-competitor-analysis/cases/pote-1520ml-kit2-2026-03-18.md
- skills/marketplace/ml-extrato/SKILL.md
- skills/marketplace/ml-extrato/references/colunas.md
- skills/marketplace/ml-fees-rules/SKILL.md
- skills/marketplace/ml-report/DEPRECATED.md
- skills/marketplace/ml-report/SKILL.md
- skills/marketplace/ml-report/references/estrutura-relatorio.md
- skills/marketplace/ml-report/references/paleta-cores.md
- skills/marketplace/shopee-extrato/SKILL.md
- skills/marketplace/shopee-extrato/references/classificacoes.md
- skills/marketplace/shopee-extrato/references/colunas.md
- skills/marketplace/shopee-extrato/references/nomenclatura-unificada.md
- skills/marketplace/shopee-fees-rules/SKILL.md
- skills/obsidian-vault-manager/SKILL.md
- skills/operations/inventory-management/SKILL.md
- skills/research/deep-research-protocol/SKILL.md
- skills/shopee-listing-creator/SKILL.md
- skills/shopee-listing-creator/rules/validation-rules.md
- skills/shopee-listing-creator/templates/checklist.md
- skills/shopee-listing-creator/templates/description-template.md
- skills/spreadsheet-pricing/SKILL.md
- skills/spreadsheet-pricing/maps/amazon-columns.md
- skills/spreadsheet-pricing/maps/estoque-columns.md
- skills/spreadsheet-pricing/maps/meli-columns.md
- skills/spreadsheet-pricing/maps/shopee-columns.md
- skills/spreadsheet-pricing/rules/format-rules.md
- skills/spreadsheet-pricing/rules/formula-protection.md
- skills/strategic-planner/SKILL.md
- skills/strategic-planner/references/template-deep.md
- skills/strategic-planner/references/template-lite.md
- skills/strategic-planner/references/template-standard.md
- skills/superpowers/brainstorming/SKILL.md
- skills/superpowers/brainstorming/spec-document-reviewer-prompt.md
- skills/superpowers/brainstorming/visual-companion.md
- skills/superpowers/dispatching-parallelopenclaw/agents/SKILL.md
- skills/superpowers/executing-plans/SKILL.md
- skills/superpowers/finishing-a-development-branch/SKILL.md
- skills/superpowers/receiving-code-review/SKILL.md
- skills/superpowers/requesting-code-review/SKILL.md
- skills/superpowers/requesting-code-review/code-reviewer.md
- skills/superpowers/subagent-driven-development/SKILL.md
- skills/superpowers/subagent-driven-development/code-quality-reviewer-prompt.md
- skills/superpowers/subagent-driven-development/implementer-prompt.md
- skills/superpowers/subagent-driven-development/spec-reviewer-prompt.md
- skills/superpowers/systematic-debugging/CREATION-LOG.md
- skills/superpowers/systematic-debugging/SKILL.md
- skills/superpowers/systematic-debugging/condition-based-waiting.md
- skills/superpowers/systematic-debugging/defense-in-depth.md
- skills/superpowers/systematic-debugging/root-cause-tracing.md
- skills/superpowers/systematic-debugging/test-academic.md
- skills/superpowers/systematic-debugging/test-pressure-1.md
- skills/superpowers/systematic-debugging/test-pressure-2.md
- skills/superpowers/systematic-debugging/test-pressure-3.md
- skills/superpowers/test-driven-development/SKILL.md
- skills/superpowers/test-driven-development/testing-anti-patterns.md
- skills/superpowers/using-git-worktrees/SKILL.md
- skills/superpowers/using-superpowers/SKILL.md
- skills/superpowers/using-superpowers/references/codex-tools.md
- skills/superpowers/using-superpowers/references/gemini-tools.md
- skills/superpowers/verification-before-completion/SKILL.md
- skills/superpowers/writing-plans/SKILL.md
- skills/superpowers/writing-plans/plan-document-reviewer-prompt.md
- skills/superpowers/writing-skills/SKILL.md
- skills/superpowers/writing-skills/anthropic-best-practices.md
- skills/superpowers/writing-skills/examples/CLAUDE_MD_TESTING.md
- skills/superpowers/writing-skills/persuasion-principles.md
- skills/superpowers/writing-skills/testing-skills-with-subagents.md
- skills/update-ml-return-rates/SKILL.md
- skills/whatsapp-ultimate/SKILL.md
- skills/whatsapp-ultimate/description.md

### Scripts (.py, .ts, .js, .sh, .mjs, .cjs)
- scripts/brain-boot.sh
- skills/design/frontend-design-ultimate/scripts/bundle-artifact.sh
- skills/design/frontend-design-ultimate/scripts/init-nextjs.sh
- skills/design/frontend-design-ultimate/scripts/init-vite.sh
- skills/dev/fullstack-dev/assets/nextjs-starter/src/app/layout.tsx
- skills/dev/fullstack-dev/assets/nextjs-starter/src/lib/utils.ts
- skills/dev/fullstack-dev/scripts/deploy-vps.sh
- skills/dev/fullstack-dev/scripts/init-fastapi-project.sh
- skills/dev/fullstack-dev/scripts/init-nextjs-project.sh
- skills/design/frontend-design-ultimate/templates/site-config.ts
- skills/integracao/instagram/scripts/instagram.sh
- skills/marketing/meta-ads/scripts/meta-ads-create.py
- skills/marketing/meta-ads/scripts/meta-ads-report.py
- skills/marketing/meta-ads/scripts/meta-ads-rules.py
- skills/marketplace/amazon-extrato/scripts/amazon-extrato.py
- skills/marketplace/consolidado-financeiro/scripts/enhance-consolidado.py
- skills/marketplace/marketplace-report/scripts/charts.py
- skills/marketplace/marketplace-report/scripts/connectors/__init__.py
- skills/marketplace/marketplace-report/scripts/connectors/amazon.py
- skills/marketplace/marketplace-report/scripts/connectors/mercadolivre.py
- skills/marketplace/marketplace-report/scripts/connectors/shopee.py
- skills/marketplace/marketplace-report/scripts/report-engine.py
- skills/marketplace/marketplace-report/scripts/sections/__init__.py
- skills/marketplace/marketplace-report/scripts/sections/helpers.py
- skills/marketplace/marketplace-report/scripts/sections/icons.py
- skills/marketplace/marketplace-report/scripts/sections/s01_capa.py
- skills/marketplace/marketplace-report/scripts/sections/s02_faturamento.py
- skills/marketplace/marketplace-report/scripts/sections/s03_vendas.py
- skills/marketplace/marketplace-report/scripts/sections/s04_trafego.py
- skills/marketplace/marketplace-report/scripts/sections/s05_ads.py
- skills/marketplace/marketplace-report/scripts/sections/s06_reputacao.py
- skills/marketplace/marketplace-report/scripts/sections/s07_logistica.py
- skills/marketplace/marketplace-report/scripts/sections/s08_catalogo.py
- skills/marketplace/marketplace-report/scripts/sections/s09_estrategia.py
- skills/marketplace/ml-competitor-analysis/scripts/fetch_ml_search.py
- skills/marketplace/ml-competitor-analysis/scripts/parse_ml_search.py
- skills/marketplace/ml-extrato/scripts/ml-extrato.py
- skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh
- skills/marketplace/ml-report/scripts/ml-charts.py
- skills/marketplace/ml-report/scripts/ml-report.py
- skills/marketplace/ml-report/scripts/sections/__init__.py
- skills/marketplace/ml-report/scripts/sections/helpers.py
- skills/marketplace/ml-report/scripts/sections/s01_capa.py
- skills/marketplace/ml-report/scripts/sections/s02_faturamento.py
- skills/marketplace/ml-report/scripts/sections/s03_vendas.py
- skills/marketplace/ml-report/scripts/sections/s04_trafego.py
- skills/marketplace/ml-report/scripts/sections/s05_ads.py
- skills/marketplace/ml-report/scripts/sections/s06_reputacao.py
- skills/marketplace/ml-report/scripts/sections/s07_logistica.py
- skills/marketplace/ml-report/scripts/sections/s08_catalogo.py
- skills/marketplace/ml-report/scripts/sections/s09_estrategia.py
- skills/marketplace/shopee-extrato/scripts/shopee-extrato.py
- skills/perplexity/scripts/search.mjs
- skills/superpowers/brainstorming/scripts/frame-template.html
- skills/superpowers/brainstorming/scripts/helper.js
- skills/superpowers/brainstorming/scripts/server.cjs
- skills/superpowers/brainstorming/scripts/start-server.sh
- skills/superpowers/brainstorming/scripts/stop-server.sh
- skills/superpowers/systematic-debugging/condition-based-waiting-example.ts
- skills/superpowers/systematic-debugging/find-polluter.sh
- skills/superpowers/writing-skills/graphviz-conventions.dot
- skills/superpowers/writing-skills/render-graphs.js
- skills/update-ml-return-rates/update-return-rates.py
- skills/whatsapp-ultimate/scripts/apply-history-fix.sh
- skills/whatsapp-ultimate/scripts/apply-model-prefix.sh
- skills/whatsapp-ultimate/scripts/wa-create-group.ts
- skills/whatsapp-ultimate/scripts/wa-fetch-contacts.ts

### Configuração (.json, .yaml, .yml, .toml, .env, .lock, .gitignore, .example, .bak)
- .gitignore
- scheduled_tasks.lock
- skills/design/animated-financial-display/.clawhub/origin.json
- skills/design/animated-financial-display/_meta.json
- skills/design/data-visualization-2/.clawhub/origin.json
- skills/design/data-visualization-2/_meta.json
- skills/design/financial-design-systems/.clawhub/origin.json
- skills/design/financial-design-systems/_meta.json
- skills/design/frontend-design-ultimate/.clawhub/origin.json
- skills/design/frontend-design-ultimate/_meta.json
- skills/design/lb-motion-skill/.clawhub/origin.json
- skills/design/lb-motion-skill/_meta.json
- skills/design/shadcn-ui/.clawhub/origin.json
- skills/design/shadcn-ui/_meta.json
- skills/design/superdesign/.clawhub/origin.json
- skills/design/superdesign/_meta.json
- skills/dev/fullstack-dev/assets/nextjs-starter/.env.example
- skills/dev/fullstack-dev/assets/nextjs-starter/next.config.ts
- skills/dev/fullstack-dev/assets/nextjs-starter/package.json
- skills/dev/fullstack-dev/assets/nextjs-starter/tsconfig.json
- skills/gb-import-hub/SKILL.md.bak
- skills/whatsapp-ultimate/_meta.json
- .playwright-mcp/page-2026-04-07T19-54-54-534Z.yml
- .playwright-mcp/page-2026-04-07T19-55-27-870Z.yml

### Outros
- Sem título.canvas — (canvas Obsidian)
- .playwright-mcp/console-2026-04-07T19-54-48-743Z.log — (log Playwright)
- .playwright-mcp/console-2026-04-07T19-55-25-927Z.log — (log Playwright)
- skills/coaching-corrida/assets/plano-unificado.xlsx — (planilha de treino)
- skills/marketplace/marketplace-report/assets/budamix-logo-teal.png — (logo)
- skills/marketplace/marketplace-report/assets/budamix-logo-white.png — (logo)
- skills/marketplace/ml-report/assets/budamix-logo-teal.png — (logo)
- skills/marketplace/ml-report/assets/budamix-logo-white.png — (logo)
- skills/marketplace/ml-ads-api-reference.pdf — (PDF referência ML Ads API)
- skills/marketplace/shopee-api-reference.pdf — (PDF referência Shopee API)
