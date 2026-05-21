---
title: "decisions — Vault"
created: 2026-05-21
type: decisions-log
agent: vault
status: active
tags:
  - agent/vault
  - memory
---

# Decisões Financeiras — Vault

Registro de decisões financeiras tomadas pelo Vault (em conjunto com Kobe e Pedro).

## Formato

```
## YYYY-MM-DD — [Título curto]
**Contexto:** [o que estava em jogo]
**Decisão:** [o que foi decidido]
**Owner:** [Pedro / Kobe / Vault / Ledger]
**Status:** ativa | revisar em DD/MM | superada
**Cross-refs:** [[link relevante]]
```

---

## 2026-05-21 — Criação do agente Vault + sub-agente Ledger
**Contexto:** GB Grupo precisava de área financeira AI dedicada. Pedro fazia processamento de extratos e fechamento de caixa manualmente. Sem agente que segurasse esse domínio.
**Decisão:** Criar Vault (CFO top-level) + Ledger (Analista Sênior sub-agente). Vault revisa e interpreta; Ledger processa. Os 2 rodam Opus 4.7 como padrão (Ledger com GPT 5.5 como fallback). Backup completo da config OpenClaw feito antes da ativação.
**Owner:** Pedro (briefing) + Kobe (implementação via Claude Code)
**Status:** ativa, aguardando ativação na VPS
**Cross-refs:** [[memory/sessions/2026-05-21]], briefing original do Pedro
