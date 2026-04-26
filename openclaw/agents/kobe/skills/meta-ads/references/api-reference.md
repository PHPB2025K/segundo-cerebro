---
title: "api-reference"
created: 2026-04-26
type: skill-reference
agent: kobe
status: active
tags:
  - agent/kobe
  - skill
  - skill/openclaw/meta-ads
---
# Meta Marketing API — Referência Completa
**Versão:** v21.0 | **Conta:** act_323534883953033

---

## Setup Rápido

```bash
# Obter token (sempre via 1Password)
TOKEN=$(op read "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/token")
AC="act_323534883953033"
BASE="https://graph.facebook.com/v21.0"

# Verificar token
curl -s "$BASE/me?access_token=$TOKEN" | python3 -m json.tool
```

---

## Endpoints — Ad Account

```bash
# Detalhes da conta
curl -s "$BASE/$AC?fields=name,currency,timezone_name,account_status,spend_cap&access_token=$TOKEN"

# Status: 1=ACTIVE, 2=DISABLED, 3=UNSETTLED, 7=PENDING_RISK_REVIEW, 9=IN_GRACE_PERIOD
```

---

## Endpoints — Campaigns

```bash
# Listar campanhas
curl -s "$BASE/$AC/campaigns?fields=id,name,objective,status,daily_budget,lifetime_budget,bid_strategy&access_token=$TOKEN"

# Criar campanha SALES - CBO
curl -X POST "$BASE/$AC/campaigns" \
  -d "name=BUDAMIX_SALES_POTES_CBO_Mar2026" \
  -d "objective=OUTCOME_SALES" \
  -d "status=PAUSED" \
  -d "special_ad_categories=[]" \
  -d "bid_strategy=LOWEST_COST_WITHOUT_CAP" \
  -d "daily_budget=15000" \
  -d "access_token=$TOKEN"

# Criar campanha AWARENESS - ABO (sem budget)
curl -X POST "$BASE/$AC/campaigns" \
  -d "name=BUDAMIX_AWARENESS_BRAND_Mar2026" \
  -d "objective=OUTCOME_AWARENESS" \
  -d "status=PAUSED" \
  -d "special_ad_categories=[]" \
  -d "access_token=$TOKEN"

# Pausar campanha
curl -X POST "$BASE/{CAMPAIGN_ID}" \
  -d "status=PAUSED" -d "access_token=$TOKEN"

# Ativar campanha
curl -X POST "$BASE/{CAMPAIGN_ID}" \
  -d "status=ACTIVE" -d "access_token=$TOKEN"

# Deletar campanha
curl -X DELETE "$BASE/{CAMPAIGN_ID}?access_token=$TOKEN"

# Atualizar budget
curl -X POST "$BASE/{CAMPAIGN_ID}" \
  -d "daily_budget=20000" \
  -d "access_token=$TOKEN"
```

### Objetivos ODAX (2025)
| Código | Uso |
|---|---|
| `OUTCOME_SALES` | E-commerce, conversão, catálogo |
| `OUTCOME_TRAFFIC` | Visitas ao site/app |
| `OUTCOME_AWARENESS` | Branding, alcance |
| `OUTCOME_ENGAGEMENT` | Curtidas, comentários, mensagens |
| `OUTCOME_LEADS` | Lead forms, captação |
| `OUTCOME_APP_PROMOTION` | Instalações de app |

---

## Endpoints — Ad Sets

```bash
# Criar Ad Set - Sales com Pixel (CBO)
curl -X POST "$BASE/$AC/adsets" \
  -d "name=POTES_BR_25-55_BROAD_PURCHASE" \
  -d "campaign_id={CAMPAIGN_ID}" \
  -d "billing_event=IMPRESSIONS" \
  -d "optimization_goal=OFFSITE_CONVERSIONS" \
  -d "bid_strategy=LOWEST_COST_WITHOUT_CAP" \
  -d "targeting={\"geo_locations\":{\"countries\":[\"BR\"]},\"age_min\":25,\"age_max\":55}" \
  -d "promoted_object={\"pixel_id\":\"{PIXEL_ID}\",\"custom_event_type\":\"PURCHASE\"}" \
  -d "status=PAUSED" \
  -d "access_token=$TOKEN"

# Criar Ad Set - ABO com budget próprio
curl -X POST "$BASE/$AC/adsets" \
  -d "name=POTES_BR_25-55_LAL1PCT_PURCHASE" \
  -d "campaign_id={CAMPAIGN_ID_SEM_BUDGET}" \
  -d "daily_budget=5000" \
  -d "billing_event=IMPRESSIONS" \
  -d "optimization_goal=OFFSITE_CONVERSIONS" \
  -d "bid_strategy=LOWEST_COST_WITHOUT_CAP" \
  -d "targeting={\"geo_locations\":{\"countries\":[\"BR\"]},\"age_min\":25,\"age_max\":55}" \
  -d "promoted_object={\"pixel_id\":\"{PIXEL_ID}\",\"custom_event_type\":\"PURCHASE\"}" \
  -d "status=PAUSED" \
  -d "access_token=$TOKEN"

# Atualizar budget do Ad Set
curl -X POST "$BASE/{ADSET_ID}" \
  -d "daily_budget=8000" \
  -d "access_token=$TOKEN"

# Listar Ad Sets de uma campanha
curl -s "$BASE/{CAMPAIGN_ID}/adsets?fields=id,name,status,daily_budget,optimization_goal&access_token=$TOKEN"
```

### Optimization Goals mais usados
| Campo | Quando usar |
|---|---|
| `OFFSITE_CONVERSIONS` | Sales (Purchase/AddToCart via Pixel) |
| `LANDING_PAGE_VIEWS` | Traffic qualificado |
| `LINK_CLICKS` | Traffic básico |
| `IMPRESSIONS` | Awareness puro |
| `REACH` | Cobertura máxima |
| `LEAD_GENERATION` | Lead forms |

### Bid Strategies
| Campo | Quando usar |
|---|---|
| `LOWEST_COST_WITHOUT_CAP` | Padrão, fase inicial |
| `LOWEST_COST_WITH_BID_CAP` | Controle de bid máximo |
| `COST_CAP` | CPA-alvo definido |
| `MINIMUM_ROAS` | Meta de ROAS mínimo |

---

## Endpoints — Ad Creatives

```bash
# Criar creative com imagem (URL pública)
curl -X POST "$BASE/$AC/adcreatives" \
  -d "name=POTES_IMG_OFERTA-01_Mar2026" \
  -d "object_story_spec={
    \"page_id\": \"{PAGE_ID}\",
    \"link_data\": {
      \"picture\": \"https://url-publica-da-imagem.jpg\",
      \"link\": \"https://budamix.com.br/potes\",
      \"message\": \"Potes herméticos premium para organizar sua cozinha.\",
      \"name\": \"Potes Herméticos Budamix\",
      \"call_to_action\": {
        \"type\": \"SHOP_NOW\",
        \"value\": {\"link\": \"https://budamix.com.br/potes\"}
      }
    }
  }" \
  -d "access_token=$TOKEN"

# Upload de imagem (retorna image_hash para usar no creative)
curl -X POST "$BASE/$AC/adimages" \
  -F "filename=@/caminho/para/imagem.jpg" \
  -F "access_token=$TOKEN"
# Retorna: {"images":{"imagem.jpg":{"hash":"XXXXXXXX","url":"..."}}}

# Criar creative com image_hash (após upload)
curl -X POST "$BASE/$AC/adcreatives" \
  -d "name=POTES_IMG_UPLOAD-01_Mar2026" \
  -d "object_story_spec={
    \"page_id\": \"{PAGE_ID}\",
    \"link_data\": {
      \"image_hash\": \"{IMAGE_HASH}\",
      \"link\": \"https://budamix.com.br\",
      \"message\": \"Organize sua cozinha com estilo.\",
      \"name\": \"Budamix — Potes Herméticos\",
      \"call_to_action\": {\"type\": \"SHOP_NOW\", \"value\": {\"link\": \"https://budamix.com.br\"}}
    }
  }" \
  -d "access_token=$TOKEN"
```

### CTAs disponíveis
`SHOP_NOW` | `LEARN_MORE` | `SIGN_UP` | `DOWNLOAD` | `GET_OFFER` | `CONTACT_US` | `WATCH_MORE` | `BOOK_NOW` | `SUBSCRIBE`

---

## Endpoints — Ads

```bash
# Criar Ad
curl -X POST "$BASE/$AC/ads" \
  -d "name=POTES_IMG_OFERTA-01_Mar2026" \
  -d "adset_id={ADSET_ID}" \
  -d "creative={\"creative_id\":\"{CREATIVE_ID}\"}" \
  -d "status=PAUSED" \
  -d "access_token=$TOKEN"

# Listar Ads de um Ad Set
curl -s "$BASE/{ADSET_ID}/ads?fields=id,name,status,creative&access_token=$TOKEN"
```

---

## Insights API — Relatórios

```bash
# Visão geral da conta (últimos 7 dias)
curl -s "$BASE/$AC/insights?\
fields=campaign_name,spend,impressions,clicks,ctr,cpm,cpc,purchase_roas,actions\
&level=campaign&date_preset=last_7d&access_token=$TOKEN"

# Por Ad Set (últimos 30 dias)
curl -s "$BASE/$AC/insights?\
fields=adset_name,campaign_name,spend,impressions,ctr,cpm,cpc,purchase_roas,frequency,actions\
&level=adset&date_preset=last_30d&access_token=$TOKEN"

# Por Criativo/Ad (últimos 14 dias)
curl -s "$BASE/$AC/insights?\
fields=ad_name,adset_name,spend,impressions,ctr,cpm,cpc,purchase_roas,frequency,actions\
&level=ad&date_preset=last_14d&access_token=$TOKEN"

# Breakdown por placement
curl -s "$BASE/{CAMPAIGN_ID}/insights?\
fields=impressions,spend,clicks,cpm,ctr,actions\
&breakdowns=publisher_platform,platform_position\
&date_preset=last_14d&access_token=$TOKEN"

# Breakdown por idade e gênero
curl -s "$BASE/{ADSET_ID}/insights?\
fields=impressions,spend,actions,purchase_roas\
&breakdowns=age,gender\
&date_preset=last_30d&access_token=$TOKEN"

# Breakdown por device
curl -s "$BASE/$AC/insights?\
fields=impressions,spend,ctr,actions\
&breakdowns=device_platform\
&level=campaign&date_preset=last_7d&access_token=$TOKEN"
```

### Date Presets disponíveis
`today` | `yesterday` | `this_week_sun_today` | `last_7d` | `last_14d` | `last_28d` | `last_30d` | `last_90d` | `this_month` | `last_month`

### Principais campos de métricas
| Campo | Descrição |
|---|---|
| `spend` | Gasto em reais |
| `impressions` | Total de impressões |
| `reach` | Alcance único |
| `frequency` | Impressões/Reach |
| `clicks` | Cliques totais |
| `ctr` | Click-Through Rate % |
| `cpc` | Custo por Clique |
| `cpm` | Custo por Mil Impressões |
| `actions` | Array: conversões, likes, etc. |
| `action_values` | Valores das ações (receita) |
| `purchase_roas` | ROAS de compras |
| `cost_per_action_type` | CPA por tipo de evento |
| `video_p25_watched_actions` | 25% do vídeo assistido |
| `video_thruplay_watched_actions` | Vídeo assistido até o fim (ou 15s) |

---

## Regras Automatizadas

```bash
# Listar regras
curl -s "$BASE/$AC/adrules_library?fields=id,name,status,evaluation_spec,execution_spec&access_token=$TOKEN"

# Pausar regra
curl -X POST "$BASE/{RULE_ID}" -d "status=PAUSED" -d "access_token=$TOKEN"

# Deletar regra
curl -X DELETE "$BASE/{RULE_ID}?access_token=$TOKEN"
```

---

## Custom Audiences

```bash
# Criar audience de compradores (Pixel - 180 dias)
curl -X POST "$BASE/$AC/customaudiences" \
  -d "name=Compradores - 180d" \
  -d "rule={
    \"inclusions\":{\"operator\":\"or\",\"rules\":[{
      \"event_sources\":[{\"id\":\"{PIXEL_ID}\",\"type\":\"pixel\"}],
      \"retention_seconds\":15552000,
      \"filter\":{\"operator\":\"and\",\"filters\":[
        {\"field\":\"event\",\"operator\":\"eq\",\"value\":\"Purchase\"}
      ]}
    }]}
  }" \
  -d "access_token=$TOKEN"

# Criar Lookalike 1%
curl -X POST "$BASE/$AC/customaudiences" \
  -d "name=LAL 1% - Compradores - BR" \
  -d "subtype=LOOKALIKE" \
  -d "origin_audience_id={CUSTOM_AUDIENCE_ID}" \
  -d "lookalike_spec={\"type\":\"similarity\",\"starting_ratio\":0.0,\"ratio\":0.01,\"country\":\"BR\"}" \
  -d "access_token=$TOKEN"

# Listar audiences
curl -s "$BASE/$AC/customaudiences?fields=id,name,subtype,approximate_count&access_token=$TOKEN"
```

---

## Códigos de Erro Comuns

| Código | Causa | Solução |
|---|---|---|
| 190 | Token inválido/expirado | Renovar token no 1Password |
| 200 | Permissão faltando | Adicionar scope necessário |
| 100 | Parâmetro inválido | Verificar sintaxe |
| 613 | Rate limit | Aguardar + backoff |
| 368 | Conta restrita | Verificar policy violations |
| 1487394 | Ad Set sem criativos suficientes | Adicionar mais criativos |

---

## Paginação

```bash
# Seguir cursor para próxima página
NEXT=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('paging',{}).get('next',''))")
if [ -n "$NEXT" ]; then
  curl -s "$NEXT"
fi
```

## Batch Requests (até 50 chamadas por batch)

```bash
curl -X POST "$BASE" \
  -d "access_token=$TOKEN" \
  -d "batch=[
    {\"method\":\"GET\",\"relative_url\":\"$AC/campaigns?fields=id,name,status\"},
    {\"method\":\"GET\",\"relative_url\":\"$AC/insights?fields=spend,purchase_roas&date_preset=last_7d&level=campaign\"}
  ]"
```

---

## SDK Python — Setup

```python
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import subprocess

# Token via 1Password
token = subprocess.run(
    ["op", "read", "op://OpenClaw/Meta Ads API - KOBE.OPENCLAW/token"],
    capture_output=True, text=True
).stdout.strip()

FacebookAdsApi.init(access_token=token)
account = AdAccount("act_323534883953033")

# Listar campanhas
campaigns = account.get_campaigns(fields=["id", "name", "status"])
for c in campaigns:
    print(c["id"], c["name"], c.get("status"))
```
