---
name: meta-ads
description: >
  Skill de Meta Ads (Facebook/Instagram Ads) para operação profissional via Marketing API.
  Usar quando: criar campanha no Meta, subir anúncio no Facebook ou Instagram, gerar
  relatório de performance de ADS, verificar ROAS de campanhas Meta, checar gasto com
  anúncios, criar regras automatizadas, escalar campanha, pausar campanha com CPA alto,
  configurar targeting ou público, criar Custom Audience, Lookalike Audience, analisar
  métricas de CTR/CPM/CPC/CPA/ROAS, otimizar campanha de vendas, configurar Advantage+
  Shopping Campaign, criar ads para e-commerce, Meta Ads para GB Importadora, Budamix ads,
  campanha de sales no Meta, relatório de ads últimos 7/30/90 dias, automação de anúncios.
---

# Meta Ads — Skill de Operação Profissional

> Usado por [[agents/spark/IDENTITY|Spark]]

Skill de gestão e automação de Meta Ads via Marketing API v21.0.
Contexto: GB Importadora (Budamix), vendas em marketplace.

---

## Contas e IDs

| Item | Valor |
|---|---|
| **Ad Account** | `act_323534883953033` (GB Distribuição) |
| **Business Manager ID** | `7723008527787239` |
| **App** | KOBE.OPENCLAW (`3582660648568553`) |
| **API Version** | `v21.0` |
| **Base URL** | `https://graph.facebook.com/v21.0/` |

---

## Credenciais (1Password)

```bash
# Token de acesso (System User Token — não expira)
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/access_token")

# App Secret
APP_SECRET=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/app_secret")

# Todos os campos disponíveis no item "Meta Ads API - KOBE.OPENCLAW"
# Vault: OpenClaw
```

**Verificar token:**
```bash
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/access_token")
curl "https://graph.facebook.com/v21.0/me?access_token=$TOKEN"
```

---

## Scripts Disponíveis

| Script | O que faz |
|---|---|
| `scripts/meta-ads-report.py` | Relatório de performance (7/30/90 dias), salva JSON |
| `scripts/meta-ads-create.py` | Criar campanha completa (campaign + adset + ad) |
| `scripts/meta-ads-rules.py` | Criar/listar/pausar regras automatizadas |

**Usar scripts:**
```bash
cd /root/.openclaw/workspace/skills/marketing/meta-ads

# Relatório dos últimos 30 dias
python3 scripts/meta-ads-report.py --days 30

# Relatório por nível (campaign/adset/ad)
python3 scripts/meta-ads-report.py --days 7 --level campaign

# Criar campanha de vendas
python3 scripts/meta-ads-create.py --name "BUDAMIX_SALES_POTES_Mar2026" --budget 15000

# Listar regras ativas
python3 scripts/meta-ads-rules.py --list

# Criar conjunto de regras essenciais
python3 scripts/meta-ads-rules.py --create-essentials
```

---

## Workflow Principal

### 1. Verificar performance atual
```bash
python3 scripts/meta-ads-report.py --days 7 --level campaign
```

### 2. Criar nova campanha de vendas
```bash
python3 scripts/meta-ads-create.py \
  --name "BUDAMIX_SALES_POTES_CBO_$(date +%b%Y)" \
  --objective OUTCOME_SALES \
  --budget 15000 \
  --status PAUSED
```

### 3. Ativar regras de proteção
```bash
python3 scripts/meta-ads-rules.py --create-essentials
```

### 4. Monitorar e escalar
- Aguardar Learning Phase (7–14 dias, 50 events/semana)
- Aumentar budget máx 20% por vez a cada 3–5 dias
- Renovar criativos quando frequência > 3.0

---

## Quick Reference — Comandos Diretos via curl

### Verificar conta
```bash
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/access_token")
AC="act_323534883953033"

# Status da conta
curl -s "https://graph.facebook.com/v21.0/$AC?fields=name,currency,account_status,spend_cap&access_token=$TOKEN" | python3 -m json.tool
```

### Listar campanhas
```bash
curl -s "https://graph.facebook.com/v21.0/$AC/campaigns?fields=id,name,objective,status,daily_budget,lifetime_budget&access_token=$TOKEN" | python3 -m json.tool
```

### Pausar/ativar campanha
```bash
CAMPAIGN_ID="120xxxxxxxxxx"

# Pausar
curl -X POST "https://graph.facebook.com/v21.0/$CAMPAIGN_ID" \
  -d "status=PAUSED" -d "access_token=$TOKEN"

# Ativar
curl -X POST "https://graph.facebook.com/v21.0/$CAMPAIGN_ID" \
  -d "status=ACTIVE" -d "access_token=$TOKEN"
```

### Insights rápidos (últimos 7 dias)
```bash
curl -s "https://graph.facebook.com/v21.0/$AC/insights?\
fields=campaign_name,spend,impressions,clicks,ctr,cpm,cpc,purchase_roas,actions\
&level=campaign&date_preset=last_7d&access_token=$TOKEN" | python3 -m json.tool
```

### Ajustar orçamento de Ad Set
```bash
ADSET_ID="23xxxxxxxxxx"
curl -X POST "https://graph.facebook.com/v21.0/$ADSET_ID" \
  -d "daily_budget=20000" \  # R$200/dia em centavos
  -d "access_token=$TOKEN"
```

---

## Naming Convention (GB Importadora)

```
Campaign:   [MARCA]_[OBJETIVO]_[PRODUTO]_[TIPO]_[MêsAno]
AdSet:      [PRODUTO]_[REGIÃO]_[IDADE]_[PÚBLICO]_[EVENTO]
Ad:         [PRODUTO]_[FORMATO]_[VARIAÇÃO]_[MêsAno]

Exemplos:
  BUDAMIX_SALES_POTES-HERMETICOS_CBO_Mar2026
  POTES_BR_25-55_BROAD_PURCHASE
  POTES_IMG_OFERTA-01_Mar2026
```

---

## KPIs de Referência — E-commerce BR (2025)

| KPI | Benchmark | Meta GB |
|---|---|---|
| ROAS | Mediana 2.2x | >3x |
| CTR | 0.8–1.5% | >1% |
| CPM | R$15–40 | <R$25 |
| CPC | R$0.50–2.00 | <R$1.50 |
| Frequência | 1.5–2.5 | <3.0 |
| ROAS Retargeting | 4–8x | >4x |

**ROAS Breakeven:** `1 / Margem Bruta`
→ Margem 40% = ROAS mínimo 2.5x

---

## Referências Detalhadas

| Arquivo | Conteúdo |
|---|---|
| `references/api-reference.md` | Endpoints completos, parâmetros, exemplos curl |
| `references/campaign-guide.md` | Criação de campanhas por objetivo, estrutura ODAX |
| `references/audience-targeting.md` | Custom Audiences, Lookalike, Advantage+ |
| `references/creative-specs.md` | Specs técnicas, formatos, copy framework |
| `references/optimization-guide.md` | Bidding, Learning Phase, escala, regras |
| `references/ecommerce-strategy.md` | Estratégia específica GB/Budamix/marketplace |

---

## Instalação de Dependências

```bash
pip install facebook-python-business-sdk requests tabulate
# ou
pip3 install facebook-business requests tabulate
```

---

## Alertas Importantes

⚠️ **Meta Ads → Mercado Livre:** Evitar. Sem Pixel, sem ROAS mensurável. Ver `references/ecommerce-strategy.md`.

⚠️ **Learning Phase:** Não mexer em nada por 7 dias após criar/modificar Ad Set. Qualquer mudança reseta.

⚠️ **Budget changes:** Aumentar máx 20% de uma vez. Acima disso reseta Learning Phase.

⚠️ **API v21.0:** Checar sunset dates. Meta deprecia versões a cada ~2 anos.
