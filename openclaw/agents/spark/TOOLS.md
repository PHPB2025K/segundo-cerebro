---
title: "TOOLS"
created: 2026-04-14
modified: 2026-06-08
type: tools-config
agent: spark
status: active
tags:
  - agent/spark
---

# TOOLS.md — Cheat Sheet Rápido

_Consulta rápida para IDs, tokens e comandos. Detalhes completos em MEMORY.md._
_Atualizado 2026-06-08 — Budamix promovida a conta primária, API bump v21→v25._

---

## Meta Ads — Quick Reference (Budamix)

```bash
# Setup obrigatório de conta (guardrail nos scripts desde 08/06)
export META_AD_ACCOUNT=act_1140258596603533

# Buscar token (com cleanup do encoding do op)
TOKEN=$(op item get hxvgwjrdluw4yblo4lbktatoyy --vault=OpenClaw \
  --fields notesPlain --reveal | sed 's/^"//; s/"$//' | tr -d '\n')

# Verificar token
curl "https://graph.facebook.com/v25.0/me?access_token=$TOKEN"

# Listar campanhas Budamix
curl "https://graph.facebook.com/v25.0/act_1140258596603533/campaigns?fields=id,name,status,objective,daily_budget,bid_strategy&access_token=$TOKEN"

# Insights últimos 7d
curl -s "https://graph.facebook.com/v25.0/act_1140258596603533/insights?fields=campaign_name,spend,impressions,clicks,ctr,cpm,cpc,purchase_roas,actions&level=campaign&date_preset=last_7d&access_token=$TOKEN" | python3 -m json.tool
```

**Receita do token via VPS (alternativa):**
```bash
# Pra rodar de qualquer lugar com SSH access
ssh root@187.77.237.231 'source /root/.openclaw/secrets/op-token && \
  op item get hxvgwjrdluw4yblo4lbktatoyy --vault=OpenClaw \
    --fields notesPlain --reveal </dev/null \
  | sed "s/^\"//; s/\"$//" | tr -d "\n"'
```

---

## IDs Importantes (Budamix — PRIMÁRIA)

| Item | ID |
|---|---|
| Ad Account | `act_1140258596603533` |
| Business Manager | `836285430695962` |
| App KOBE.OPENCLAW | `1486886096369858` (Live mode) |
| Page Budamix | `106066888942641` |
| Instagram budamix.br | `17841466202361418` |
| Catálogo Budamix | `1973158136897277` |
| Pixel + CAPI | `460889899401645` |
| API Version | `v25.0` |

### Contas legacy / inativas
| Item | ID | Status |
|---|---|---|
| GB Distribuição | `act_323534883953033` | 🔴 PARADA (06/2026) — não operar |
| Broglio Brinquedos | `act_599689043839914` | ⚪ Sem campanhas |
| Trades Up | `act_851375860374263` | ⚪ Sem campanhas |
| App KOBE.OPENCLAW velho | `3582660648568553` | descontinuado em 08/06 |

---

## Metas de Referência (Budamix Strategy 2026)

| Métrica | Mês 1 | Mês 2 | Mês 3+ |
|---|---|---|---|
| ROAS | 1.0-1.3 (exploração) | 1.5-2.0 (transição Purchase) | 2.0-3.0+ (escala) |
| CPA alvo (ATC) | ~R$2 | ~R$1.5 | <R$1 |
| Ticket médio | R$24,90 (IMB501 unitário) | R$24,90 a R$67,90 (com kits) | — |
| Margem bruta | (calcular por SKU) | — | — |

**Budget atual:** R$20/dia Camp 1 ASC (R$600/mês). Camps 2 e 3 PAUSED.

---

## Strategy 2026 Budamix — campanhas

| Camp | Tipo | Budget | Status | Obs |
|---|---|---|---|---|
| 1 | ASC (Advantage+ Sales) | R$20/dia CBO | 🟢 ATIVA | Cold, mulheres BR sem Norte |
| 2 | Teste 3:2:2 (ABO) | R$11/dia | 🟡 PAUSED | Aguardando vídeos 2 e 3 |
| 3 | Retargeting WCA (ABO) | R$9/dia | 🟡 PAUSED | Aguardando WCAs criadas |

**Freeze period Camp 1:** 08/06 → ~22/06. NÃO tocar.

---

## Comandos diretos via curl (Budamix)

```bash
# Variáveis base
TOKEN=$(op item get hxvgwjrdluw4yblo4lbktatoyy --vault=OpenClaw --fields notesPlain --reveal | sed 's/^"//; s/"$//' | tr -d '\n')
AC="act_1140258596603533"

# Pausar/ativar campanha
curl -X POST "https://graph.facebook.com/v25.0/CAMPAIGN_ID" -d "status=PAUSED" -d "access_token=$TOKEN"

# Ajustar budget Ad Set (em centavos: 2000 = R$20)
curl -X POST "https://graph.facebook.com/v25.0/ADSET_ID" -d "daily_budget=2000" -d "access_token=$TOKEN"

# Trocar creative do ad
curl -X POST "https://graph.facebook.com/v25.0/AD_ID" \
  --data-urlencode 'creative={"creative_id":"NEW_CREATIVE_ID"}' \
  -d "access_token=$TOKEN"

# Ad preview
curl -G "https://graph.facebook.com/v25.0/AD_ID/previews" \
  --data-urlencode "ad_format=INSTAGRAM_REELS" \
  --data-urlencode "access_token=$TOKEN"
```

---

## Quick Reference — Paths

| Recurso | Path |
|---|---|
| Skill global meta-ads | `/root/segundo-cerebro/skills/marketing/meta-ads/` |
| Skill Spark meta-ads (legacy) | `/root/segundo-cerebro/openclaw/agents/kobe/shared/spark/skills/meta-ads/` |
| Scripts | `/root/segundo-cerebro/skills/marketing/meta-ads/scripts/` |
| References | `/root/segundo-cerebro/skills/marketing/meta-ads/references/` |
| Spark workspace | `/root/segundo-cerebro/openclaw/agents/spark/` |
| Spark memory | `/root/segundo-cerebro/openclaw/agents/spark/memory/` |
| Playbook 2026 | `/root/segundo-cerebro/knowledge/concepts/meta-ads-paid-social-2026.md` |
| Projeto Budamix Meta Ads | `/root/segundo-cerebro/projects/budamix-meta-ads.md` |
| Supabase Spark | project `wzhmrpskiscassbixurr` (https://wzhmrpskiscassbixurr.supabase.co) — schema `meta` |
