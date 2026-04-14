---
title: "TOOLS"
created: 2026-04-14
type: tools-config
agent: trader
status: active
tags:
  - agent/trader
---

# TOOLS.md — Cheat Sheet Rápido

_Consulta rápida para paths e comandos do dia a dia. Detalhes completos em MEMORY.md._

---

## Quick Reference — Tokens

| Plataforma | Refresh | TTL |
|---|---|---|
| ML | `skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh [app]` | 6h |
| Shopee | Automático por conta (script shopee-extrato.py) | 4h |
| Amazon | LWA (Login with Amazon) | Longo |

## Quick Reference — Paths

| O quê | Onde |
|---|---|
| Outputs → Kobe | `shared/outputs/` |
| Lições compartilhadas | `shared/lessons/` |
| Template HTML | `templates/report-base.html` |
| Design system HTML | `skills/design/report-design-system/SKILL.md` |
| Design system Excel | `skills/design/excel-design-system.md` |
| Planilha estoque | Google Sheets `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU` |
| Dados temporários | `/tmp/trader/` |

## Quick Reference — Comandos

```bash
# Refresh token ML (vendas)
skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh vendas

# Extrato Shopee todas as contas
python3 skills/marketplace/shopee-extrato/scripts/shopee-extrato.py --conta todas

# 1Password — buscar credencial
op item get "Amazon SP-API" --vault "OpenClaw"
```

---

_Para integrações completas (endpoints, IDs, multi-conta): MEMORY.md seção 6._
_Para skills disponíveis: MEMORY.md seção 7._
