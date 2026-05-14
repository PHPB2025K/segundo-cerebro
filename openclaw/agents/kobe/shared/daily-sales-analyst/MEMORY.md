# MEMORY — Daily Sales Analyst

Índice da memória operacional do DSA.

## Status

Estrutura de memória implementada na **Fase 2** (2026-05-14). Conteúdo será populado a partir da primeira execução do pipeline.

## Estrutura

```
memory/
├── accounts/
│   ├── shopee-budamix-store/
│   │   ├── daily/              ← memória diária por data
│   │   ├── weekly.md           ← consolidação semanal
│   │   ├── monthly.md          ← tese mensal
│   │   └── rules.md            ← regras permanentes (shop_id: 448649947)
│   ├── shopee-budamix-oficial-2/
│   │   ├── daily/
│   │   ├── weekly.md
│   │   ├── monthly.md
│   │   └── rules.md            ← (shop_id: 860803675)
│   ├── shopee-budamix-shop-3/
│   │   ├── daily/
│   │   ├── weekly.md
│   │   ├── monthly.md
│   │   └── rules.md            ← (shop_id: 442066454)
│   ├── mercado-livre/
│   │   ├── daily/
│   │   ├── weekly.md
│   │   ├── monthly.md
│   │   └── rules.md
│   └── amazon/
│       ├── daily/
│       ├── weekly.md
│       ├── monthly.md
│       └── rules.md
├── context/
│   ├── responsaveis.md         ← mapa de responsáveis por canal
│   ├── contas-shopee.md        ← shop_ids e regras das 3 contas Shopee
│   ├── himmel.md               ← contexto ADS/Himmel como input
│   ├── marketplace-rules.md    ← regras críticas por marketplace
│   ├── slack-format.md         ← template Slack e proibições
│   └── qa-standards.md         ← critérios de bloqueio/ressalva
├── MAINTENANCE.md              ← política de manutenção da memória
└── audit-ressalvas.md          ← registro e triggers de ressalvas
```

## Prompts

```
prompts/
├── CHANGELOG.md                ← histórico de versões
├── current                     ← marcador de versão ativa (→ v3.0)
└── versions/
    └── v3.0/
        ├── 01-estrategica.md
        ├── 02-tatica.md
        ├── 03-operacional.md
        ├── 04-granular.md
        ├── 05-condensadora.md
        ├── 06-slack-writer.md
        └── 07-qa-gate.md
```

## Handoff — Contrato Trader ↔ DSA (Fase 3)

```
handoff/
├── TRADER-CONTRACT.md            ← contrato formal de delegação
├── input-schema.json             ← schema do payload de entrada
├── output-schema.json            ← schema do payload de saída
├── escalation-rules.md           ← regras de escalonamento
├── TRADER-INTEGRATION-SCOPE.md   ← escopo de integração futura
└── examples/
    ├── input-example.json        ← exemplo de input válido
    └── output-example.json       ← exemplo de output completo
```

## Config

```
config/
└── daily-sales-analyst.json    ← configuração operacional
```

## Regras

- DSA sugere atualizações de memória; Trader decide se aplica.
- Memória não conflita com domínio do Trader.
- Toda memória aplicada é registrada e auditável.
- Ver `memory/MAINTENANCE.md` para política completa de manutenção.
- Ver `memory/audit-ressalvas.md` para triggers de escalonamento.
