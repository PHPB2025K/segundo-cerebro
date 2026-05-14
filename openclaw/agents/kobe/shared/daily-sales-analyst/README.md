# Daily Sales Analyst

Executor especializado do Daily Sales Report v2.5 — pipeline em Layer 0 + 7 camadas analíticas.

## Hierarquia

| Papel | Agente | Responsabilidade |
|-------|--------|-----------------|
| Decisor humano | Pedro | Decisão final |
| Governança/QA | Kobe | Validação de rollout, bloqueios, mudanças estratégicas |
| Dono/Orquestrador | Trader | Aciona DSA, recebe retorno, envia Slack |
| Executor | **Daily Sales Analyst** | Executa pipeline analítico, devolve artefatos ao Trader |

O cron aciona o Trader, não o DSA diretamente.

## Pipeline

```
Layer 0 — Data Builder (determinístico, sem LLM)
    ↓
Camada 1 — Estratégica
Camada 2 — Tática
Camada 3 — Operacional
Camada 4 — Granular
Camada 5 — Condensadora
Camada 6 — Slack Writer
Camada 7 — QA Gate
    ↓
Retorno ao Trader → envio Slack
```

## Estrutura do Workspace

```
shared/daily-sales-analyst/
├── README.md          ← este arquivo
├── IDENTITY.md        ← identidade, escopo e limites
├── SOUL.md            ← postura analítica e princípios
├── AGENTS.md          ← regras operacionais e relação com Trader/Kobe
├── MEMORY.md          ← índice da memória
├── config/            ← configurações operacionais (Fase 2+)
├── prompts/           ← prompts versionados das 7 camadas (Fase 2+)
├── data-builder/      ← docs/schema/changelog do Layer 0 (Fase 0 ✓)
├── memory/            ← memória por conta/plataforma (Fase 2+)
├── runs/              ← logs de execução
├── handoff/           ← contrato de integração com Trader (Fase 3+)
└── validation/        ← casos de validação e baseline (Fase 4+)
```

## Relação com Fase 0

O Data Builder é componente do pipeline DSA:
- **Executável:** `scripts/daily-sales-data-builder.py`
- **Docs/schema/changelog:** `shared/daily-sales-analyst/data-builder/`
- **Status Fase 0:** APROVADO_COM_RESSALVA (checkpoint Kobe) — calibragem futura de thresholds e freshness prevista na Fase 5.

## Limites

O DSA **não tem autonomia de canal**. Não fala com Pedro, não fala com funcionários, não envia Slack, não reativa cron, não muda regra permanente sem governança, não altera prompt estrutural sem versionamento/aprovação, não usa LLM no Layer 0.

Ver detalhes completos em `IDENTITY.md`.
