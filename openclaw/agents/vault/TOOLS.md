---
title: "TOOLS"
created: 2026-05-21
type: tools
agent: vault
status: active
tags:
  - agent/vault
---

# TOOLS.md — Vault

Ferramentas e integrações disponíveis ao Vault.

---

## 1. Ferramentas próprias

| Ferramenta | Uso |
|---|---|
| Leitura de planilhas processadas | Validar entrega do Ledger via openpyxl em modo read-only |
| Comparação antes/depois | Diff de células de fórmula vs entrega anterior (regressão) |
| Snapshot de posição | Geração de markdown estruturado pra `memory/posicao-caixa/YYYY-MM.md` |
| Cross-check com outros agentes | Leitura de outputs de Trader/Fisco/RH em `workspace/shared/outputs/` |

---

## 2. Sub-agente

| Sub-agente | Uso |
|---|---|
| [[openclaw/agents/vault/shared/ledger/IDENTITY\|Ledger]] | Único executor de processamento operacional. Vault delega TODO processamento de extrato pra ele. |

---

## 3. Skills

| Skill | Path | Quando o Vault dispara |
|---|---|---|
| [[skills/financeiro/cash-flow-extract-processor/SKILL\|cash-flow-extract-processor]] | `skills/financeiro/cash-flow-extract-processor/` | Quando delega fechamento ao Ledger — o Ledger é quem executa, Vault só referencia |

---

## 4. Integrações externas

Vault NÃO tem integração direta com:
- Banco / Itaú
- ERP (Bling)
- Contador (FOUR / Suellen)
- API de marketplace

Toda informação externa chega via:
- Anexos enviados pelo Pedro (extratos PDF, planilhas)
- Outputs de outros agentes em `workspace/shared/outputs/`
- Knowledge File e Tabela Mestra (versionados em `knowledge/`)

---

## 5. Filesystem (leitura)

| Path | Conteúdo |
|---|---|
| `vault/knowledge/` | Knowledge File v10.1, Tabela Mestra v2.0, Instrução do Projeto |
| `vault/shared/ledger/outputs/` | Planilhas processadas pra revisão |
| `vault/shared/ledger/runs/YYYY-MM-DD/` | Logs de processamento (apoio à revisão) |
| `vault/memory/decisions.md` | Decisões financeiras passadas |
| `vault/memory/lessons.md` | Lições aprendidas |
| `vault/memory/posicao-caixa/` | Snapshots históricos |
| `workspace/shared/outputs/trader/` | Receita por canal (cross-check) |
| `workspace/shared/outputs/fisco/` | Tributos pagos (cross-check) |
| `workspace/shared/outputs/rh/` | Folha do mês (cross-check) |

---

## 6. Filesystem (escrita)

| Path | Conteúdo |
|---|---|
| `vault/memory/decisions.md` | Nova decisão financeira |
| `vault/memory/lessons.md` | Lição aprendida |
| `vault/memory/posicao-caixa/YYYY-MM.md` | Snapshot do fechamento |
| `vault/memory/sessions/YYYY-MM-DD.md` | Registro de sessão (mtime usado pelo Mission Control) |
| `workspace/shared/outputs/vault/` | Entrega final ao Kobe |

**NUNCA escrever em:** `vault/knowledge/` (versionado), planilhas do Pedro, qualquer path da VPS fora do workspace.
