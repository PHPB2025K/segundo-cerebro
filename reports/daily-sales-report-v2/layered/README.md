# Daily Sales Report v2 — Pipeline em Camadas

## Visão geral

Pipeline de análise diária de vendas por plataforma/destinatário, com 7 camadas de análise
e validação. Atualmente opera em modo **shadow/preview** — envio real de Slack está **bloqueado**.

## Destinatários

| Nome     | Plataforma    | Contas                                              |
|----------|---------------|-----------------------------------------------------|
| Lucas    | Shopee        | Budamix Store, Budamix Oficial/Conta 2, Budamix Shop/Conta 3 |
| Yasmin   | Mercado Livre | Mercado Livre                                       |
| Leonardo | Amazon        | Amazon                                              |

## Camadas

| # | Camada         | Prompt                        | Descrição                                    |
|---|----------------|-------------------------------|----------------------------------------------|
| 1 | Estratégica    | `camada-1-estrategica.md`     | Tese temporal da conta (7d/30d/60d)          |
| 2 | Tática         | `camada-2-tatica.md`          | Decisões práticas para 5–7 dias              |
| 3 | Operacional    | `camada-3-operacional.md`     | Leitura de execução do dia                   |
| 4 | Granular       | `camada-4-granular.md`        | Validação forense de evidências              |
| 5 | Condensadora   | `camada-5-condensadora.md`    | Corte para 20% essencial                     |
| 6 | Slack Writer   | `camada-6-slack-writer.md`    | Tradução fiel para formato Slack             |
| 7 | QA Gate        | `camada-7-qa-gate.md`         | Validação bloqueante antes de envio          |

## Estrutura de arquivos

```
reports/daily-sales-report-v2/layered/
├── packages/
│   └── YYYY-MM-DD/
│       └── package.json          ← Fase 1: dados canônicos validados
├── runs/
│   └── YYYY-MM-DD/
│       ├── manifest.json         ← Metadados da execução
│       ├── lucas/
│       │   ├── camada-3-operacional.md
│       │   ├── camada-4-granular.json
│       │   ├── camada-5-condensadora.json
│       │   ├── camada-6-slack-writer-preview.md
│       │   └── camada-7-qa-gate-preview.json
│       ├── yasmin/
│       │   └── (mesma estrutura)
│       └── leonardo/
│           └── (mesma estrutura)
├── README.md                     ← Este arquivo
└── PLAN.md                       ← Plano para runner LLM
```

## Como rodar

### Fase 1 — Gerar package

```bash
cd /root/segundo-cerebro
python3 scripts/daily-sales-v2-build-package.py 2026-05-13 --write
```

Saída: `reports/daily-sales-report-v2/layered/packages/2026-05-13/package.json`

### Fase 2 — Rodar preview em camadas (determinístico)

```bash
python3 scripts/daily-sales-v2-layered-preview.py 2026-05-13
```

Saída: artefatos por destinatário em `runs/2026-05-13/`

### Fase 2 — Com package customizado

```bash
python3 scripts/daily-sales-v2-layered-preview.py 2026-05-13 --package /caminho/para/package.json
```

## Regras de qualidade (QA Gate endurecido)

O QA Gate bloqueia automaticamente:

- **Seções proibidas**: RESUMO GERAL, VENDAS POR CANAL, DESTAQUES DO DIA, VISÃO CONSOLIDADA
- **Produto sem identidade**: SKU cru ou "Produto sem identidade confiável" no texto final
- **Análise rasa**: prioridades tipo "monitorar", "observar se repete", "checar exposição/ADS/listing" sem evidência
- **Métrica sem tese**: insight que repete números sem interpretação
- **Bloqueio sistêmico**: 3+ padrões genéricos = bloqueio automático por acúmulo
- **send_real_allowed**: deve ser explicitamente `false`

## Segurança

- `send_real_allowed=false` hardcoded no package e no manifest
- Nenhum script envia Slack real nesta fase
- Cron `Daily Sales Report — Slack Funcionários` está **desabilitado**
- Tokens/credenciais nunca expostos em artefatos

## Próximos passos

Ver `PLAN.md` para proposta de runner LLM (Opção A) quando aprovado por Pedro/Kobe.
