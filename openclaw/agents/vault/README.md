---
title: "README — Vault"
created: 2026-05-21
type: readme
agent: vault
status: active
tags:
  - agent/vault
---

# Vault — Diretor Financeiro (CFO) do GB Grupo

Agente top-level do OpenClaw, par do Trader/Spark/Builder/Fisco/RH, reportando ao Kobe.

**Responsabilidade:** saúde de caixa das 8 empresas do GB Grupo, leitura estratégica financeira, governança.

**Não faz:** processamento operacional de extrato (isso é do Ledger), pagamento real, comunicação direta com Pedro/banco/contador.

## Estrutura

```
vault/
├── IDENTITY.md      — quem é, escopo, personalidade
├── SOUL.md          — essência em 1 frase
├── AGENTS.md        — como opera (protocolos)
├── TOOLS.md         — ferramentas e integrações
├── USER.md          — perfil Pedro (estilo de comunicação)
├── MEMORY.md        — índice da memória
├── HEARTBEAT.md     — sinais de vida
├── README.md        — este arquivo
├── memory/
│   ├── sessions/    — registro de sessões (mtime → Mission Control)
│   ├── decisions.md — decisões financeiras
│   ├── lessons.md   — lições aprendidas
│   └── posicao-caixa/ — snapshots mensais
├── knowledge/       — conhecimento permanente (versionado)
│   ├── 01-instrucao-projeto-v2.md
│   ├── 02-knowledge-file-v10.1.md
│   └── 03-tabela-mestra-v2.0.md
├── skills/          — skills próprias (vazio por ora; Ledger usa cash-flow-extract-processor)
└── shared/
    └── ledger/      — sub-agente (Analista Sênior de Fluxo de Caixa)
```

## Sub-agente

[[openclaw/agents/vault/shared/ledger/IDENTITY|Ledger]] — Analista Sênior de Fluxo de Caixa. Executor especializado em processamento de extratos PDF Itaú e preenchimento das planilhas DFC.

## Skills usadas

- [[skills/financeiro/cash-flow-extract-processor/SKILL|cash-flow-extract-processor]] (executada pelo Ledger)
