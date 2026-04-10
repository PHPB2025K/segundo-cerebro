# TOOLS.md — Cheat Sheet Rápido

_Consulta rápida para IDs, tokens e comandos. Detalhes completos em MEMORY.md._

---

## Meta Ads — Quick Reference

```bash
# Buscar token
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/access_token")

# Verificar token
curl "https://graph.facebook.com/v21.0/me?access_token=$TOKEN"

# Listar campanhas da GB Distribuição
curl "https://graph.facebook.com/v21.0/act_323534883953033/campaigns?fields=name,status,objective&access_token=$TOKEN"
```

## IDs Importantes

| Item | ID |
|---|---|
| App KOBE.OPENCLAW | `3582660648568553` |
| Business Manager | `7723008527787239` |
| GB Distribuição | `act_323534883953033` |
| Budamix | `act_1140258596603533` |
| Broglio Brinquedos | `act_599689043839914` |
| Trades Up | `act_851375860374263` |

## Metas de Referência

| Métrica | Meta |
|---|---|
| ROAS mínimo | 10x |
| CPA máximo | ~R$100 |
| Ticket médio | R$100-300 |
| Margem bruta | ~70% |

## Quick Reference — Paths

| O quê | Onde |
|---|---|
| Outputs → Kobe | `shared/outputs/` |
| Lições compartilhadas | `shared/lessons/` |
| Dados temporários | `/tmp/spark/` |

## Token Meta Ads

| Campo | Valor |
|---|---|
| Tipo | System User Token (long-lived) |
| TTL | ~60 dias |
| Expira | ~2026-05-18 |
| Vault | 1Password → "Meta Ads API - KOBE.OPENCLAW" |
| Cron renovação | Agendado |

---

_Para integrações completas: MEMORY.md seção 6._
_Para skills: MEMORY.md seção 7._
