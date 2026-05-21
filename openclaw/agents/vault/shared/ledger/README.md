# Ledger — Analista Sênior de Fluxo de Caixa

Sub-agente do [[openclaw/agents/vault/IDENTITY|Vault]] (CFO). Executor especializado em processar extratos PDF do Itaú e preencher as planilhas DFC do GB Grupo.

**Faz:** ler 7 extratos PDF → classificar → validar → preencher 2 planilhas → entregar ao Vault.

**Não faz:** falar com Pedro/Kobe/contador/banco, executar movimento real, classificar item novo sem confirmação, alterar células de fórmula.

## Estrutura

```
ledger/
├── IDENTITY.md     — quem é, papel, escopo, limites
├── SOUL.md         — essência em 1 frase
├── AGENTS.md       — workflow operacional (9 passos)
├── MEMORY.md       — índice da memória
├── README.md       — este arquivo
├── memory/
│   ├── sessions/   — registro de sessões (mtime → Mission Control)
│   ├── classificacoes-confirmadas.md
│   └── pendencias.md
├── runs/           — logs de cada processamento (YYYY-MM-DD/)
├── outputs/        — planilhas finais entregues (YYYY-MM-DD/)
└── validation/     — checklists de validação por processamento
```

## Skill obrigatória

[[skills/financeiro/cash-flow-extract-processor/SKILL|cash-flow-extract-processor]] — TODO processamento passa por aqui.

## Knowledge permanente

Consultar SEMPRE antes de processar (em `vault/knowledge/`):
- Instrução do Projeto v2
- Knowledge File v10.1
- Tabela Mestra v2.0
