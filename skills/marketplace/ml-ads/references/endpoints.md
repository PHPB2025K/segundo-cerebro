# Endpoints — ML Ads API v2

Base URL: `https://api.mercadolibre.com`
Headers: `Authorization: Bearer $TOKEN` + `Api-Version: 2`
ADV_ID: `172453` | SITE: `MLB`

## Advertisers

```bash
# Obter advertiser ID
GET /advertising/advertisers?product_id=PADS
# Header: Api-Version: 1 (este endpoint usa v1)
```

## Campanhas (Product Ads)

```bash
# Listar campanhas + métricas
GET /marketplace/advertising/$SITE/advertisers/$ADV_ID/product_ads/campaigns/search
  ?metrics=clicks,prints,cost,total_amount,acos,roas
  &date_from=YYYY-MM-DD&date_to=YYYY-MM-DD
  &limit=50&offset=0

# Obter campanha individual
GET /marketplace/advertising/$SITE/product_ads/campaigns/$CAMPAIGN_ID

# Métricas diárias agregadas
GET /advertising/advertisers/$ADV_ID/product_ads/campaigns
  ?aggregation_type=DAILY
  &metrics=clicks,prints,cost,total_amount,acos,roas,cpc,ctr,cvr,sov
  &date_from=YYYY-MM-DD&date_to=YYYY-MM-DD

# Criar campanha (⚠️ CONFIRMAR ANTES)
POST /marketplace/advertising/$SITE/advertisers/$ADV_ID/product_ads/campaigns
  Body: {"name":"...", "status":"active", "budget":100, "strategy":"profitability", "channel":"marketplace", "acos_target":15}

# Atualizar campanha (⚠️ CONFIRMAR ANTES)
PUT /marketplace/advertising/$SITE/product_ads/campaigns/$CAMPAIGN_ID
  Body: {"budget":150, "status":"paused"}
```

**Não existe DELETE** — pausar via PUT com `status: "paused"`.

## Anúncios/Ads

```bash
# Buscar ads + métricas (por campanha ou geral)
GET /advertising/$SITE/advertisers/$ADV_ID/product_ads/ads/search
  ?campaign_id=$CAMP_ID
  &metrics=clicks,prints,cost,total_amount,acos,roas
  &date_from=YYYY-MM-DD&date_to=YYYY-MM-DD
  &limit=50&offset=0

# Obter ad individual
GET /advertising/$SITE/product_ads/ads/$ITEM_ID

# Atualizar ad (⚠️ CONFIRMAR ANTES)
PUT /advertising/$SITE/product_ads/ads/$ITEM_ID?channel=marketplace
  Body: {"campaign_id": CAMP_ID, "status": "active"}

# Bulk update (⚠️ CONFIRMAR ANTES — até 10.000 items)
PUT /marketplace/advertising/$SITE/advertisers/$ADV_ID/product_ads/ads?channel=marketplace
  Body: {"target": [{"item_id":"MLB..."}, ...], "campaign_id": CAMP_ID, "status": "active"}

# Remover ad de campanha → campaign_id: 0 (fica idle)
PUT ... Body: {"campaign_id": 0}
```

## Ad Groups (Catálogo)

```bash
GET /advertising/$SITE/product_ads/ad_groups/$AD_GROUP_ID
GET /advertising/$SITE/product_ads/ad_groups/$AD_GROUP_ID/ads
```

## Métricas por Ad em Campanha

```bash
GET /advertising/$SITE/advertisers/$ADV_ID/product_ads/campaigns/$CAMP_ID/ads/metrics
  ?metrics=clicks,prints,cost,total_amount,acos,roas
  &date_from=YYYY-MM-DD&date_to=YYYY-MM-DD
```

## Brand Ads

```bash
GET /advertising/advertisers/$ADV_ID/brand_ads/campaigns
GET /advertising/advertisers/$ADV_ID/brand_ads/campaigns/$CAMP_ID
GET /advertising/advertisers/$ADV_ID/brand_ads/campaigns/$CAMP_ID/items
GET /advertising/advertisers/$ADV_ID/brand_ads/campaigns/$CAMP_ID/keywords
GET /advertising/advertisers/$ADV_ID/brand_ads/campaigns/$CAMP_ID/keywords/metrics
```

## Bonificações

```bash
GET /advertising/advertisers/bonifications
```

## Status de Ads

| Status | Significado |
|---|---|
| active | Ativo, recebendo tráfego |
| paused | Pausado pelo seller |
| hold | Desabilitado pelo ML (qualidade, policy) |
| idle | Sem campanha (campaign_id = 0) |
| delegated | Gerenciado por automação |
| revoked | Revogado |

## Notas importantes

- Bulk update: primeiros 50 items são síncronos, restante é assíncrono
- `campaign_id: 0` no PUT = remove ad da campanha (fica idle)
- Não pode enviar `status` e `campaign_id: 0` na mesma requisição
- Ads com status `hold` não podem ser movidos entre campanhas
- Items com `deferred_stock` (prazo de fabricação) são despriorizados pelo algoritmo
