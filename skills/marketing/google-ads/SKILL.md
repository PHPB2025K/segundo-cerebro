---
name: google-ads
description: >
  Gestão de Google Ads via API para e-commerce (Search, Shopping, Performance Max, Display).
  Usar quando: criar ou gerenciar campanha Google Ads, relatório de performance Google Ads,
  otimizar bidding, verificar ROAS/CPA de Google Ads, configurar Shopping campaign,
  Performance Max, Search ads, Display ads, analisar métricas Google Ads, pausar/ativar
  campanhas, ajustar budgets Google Ads, keywords research, negative keywords, asset groups,
  Smart Bidding (Target CPA, Target ROAS, Maximize Conversions), relatório GAQL, Google Ads
  para GB Importadora, Budamix Google Ads, integração Google Ads API.
---

# Google Ads — Skill de Operação Profissional

> Usado por [[openclaw/agents/spark/IDENTITY|Spark]]

Gestão e automação de Google Ads via API (REST/gRPC). API v23.
Contexto: GB Importadora (Budamix), vendas em marketplace + e-commerce próprio.

---

## Status de Integração

| Item | Valor |
|---|---|
| **API Version** | v23 (latest stable — v19 sunset fev/2026) |
| **Developer Token** | ✅ Basic Access |
| **Customer ID** | 7625801774 (GB Distribuição) |
| **Manager Account** | 9656686533 (TrafficAI) |
| **Auth** | OAuth 2.0 (refresh token ativo) |
| **1Password** | "Google Ads API - Spark" (vault OpenClaw) |
| **Cloud Project** | Spark Ads (billing ativo, free trial até 22/06/2026) |

✅ **INTEGRAÇÃO COMPLETA** (2026-03-23). API testada e funcionando.

---

## Quando Usar Esta Skill

1. Pedro ou Kobe pede relatório de Google Ads
2. Análise de performance de campanhas Search/Shopping/PMax
3. Criação ou otimização de campanhas
4. Ajuste de bidding strategies
5. Gestão de keywords e negative keywords
6. Configuração de asset groups (Performance Max)
7. Comparativo Google Ads vs Meta Ads

---

## Tipos de Campanha — Referência

### Search
- Anúncios de texto na busca do Google
- Keywords + match types (broad, phrase, exact)
- Bidding: Manual CPC, Target CPA, Target ROAS, Maximize Conversions
- Ideal para: captura de demanda (quem já está buscando o produto)

### Shopping
- Anúncios com foto, preço e nome do produto
- Requer Google Merchant Center com feed de produtos
- Bidding: Manual CPC, Target ROAS, Maximize Conversion Value
- Ideal para: e-commerce com catálogo visual (Budamix)

### Performance Max (PMax)
- Automação total — Google decide onde, quando e como exibir
- Roda em Search, Display, YouTube, Gmail, Maps, Discover
- Asset groups (textos, imagens, vídeos) + audience signals
- Bidding: Maximize Conversions ou Maximize Conversion Value (com Target ROAS opcional)
- Ideal para: escala com automação, quando há dados de conversão suficientes

### Display
- Anúncios visuais na rede de display (milhões de sites parceiros)
- Targeting: tópicos, placements, audiências, remarketing
- Bidding: Target CPA, Maximize Conversions, Manual CPC
- Ideal para: awareness, remarketing, top of funnel

---

## Bidding Strategies — Referência Rápida

### Smart Bidding (automatizado, recomendado)

| Estratégia | Objetivo | Quando usar |
|---|---|---|
| **Maximize Conversions** | Máximo de conversões no budget | Quando volume importa mais que custo |
| **Maximize Conversion Value** | Máximo valor de conversão | Quando valor (receita) importa mais que volume |
| **Target CPA** | Conversões a custo-alvo | Quando CPA máximo é definido |
| **Target ROAS** | Valor de conversão com ROAS-alvo | Quando ROAS mínimo é definido |

### Manual

| Estratégia | Controle | Quando usar |
|---|---|---|
| **Manual CPC** | CPC máximo por keyword | Fase inicial com pouco dado de conversão |
| **Enhanced CPC** | CPC manual + ajuste automático | Transição para Smart Bidding |

### Para a GB (contexto)
- **ROAS mínimo:** 10x (decisão Pedro)
- **Ticket médio:** R$100-300
- **Margem bruta:** ~70%
- **Recomendação:** Target ROAS ou Maximize Conversion Value com Target ROAS em Shopping/PMax

---

## Métricas Principais

| Métrica | O que mede | Alerta quando |
|---|---|---|
| **ROAS** | Revenue / Ad Spend | < 10x (meta GB) |
| **CPA** | Cost / Conversions | > ticket médio × (1 - margem alvo) |
| **CTR** | Clicks / Impressions | < 1% em Search, < 0.5% em Display |
| **Conv. Rate** | Conversions / Clicks | < 1% |
| **Impression Share** | Impressões obtidas / total elegível | < 50% em keywords core |
| **Quality Score** | 1-10 por keyword | < 5 |
| **CPC** | Cost / Clicks | Aumento > 30% vs período anterior |
| **Search Lost IS (Budget)** | Impressões perdidas por budget | > 20% |
| **Search Lost IS (Rank)** | Impressões perdidas por rank | > 30% |

---

## Estrutura de Relatório

### GAQL (Google Ads Query Language)

Quando API estiver ativa, usar GAQL para queries:

```sql
-- Performance por campanha (últimos 30 dias)
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign_budget.amount_micros,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_per_conversion
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
```

```sql
-- Performance por produto (Shopping/PMax)
SELECT
  segments.product_title,
  segments.product_item_id,
  metrics.impressions,
  metrics.clicks,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.conversions_value DESC
```

### Formato de Relatório

Seguir design system: `skills/design/report-design-system/SKILL.md`

Estrutura:
1. **KPIs consolidados** — Spend, Revenue, ROAS, CPA, CTR
2. **Por tipo de campanha** — Search vs Shopping vs PMax vs Display
3. **Top performers** — Campanhas/produtos com melhor ROAS
4. **Underperformers** — Campanhas/produtos com ROAS abaixo da meta
5. **Budget analysis** — Impression share lost, pacing
6. **Recomendações** — Ações priorizadas com impacto estimado

---

## Workflow: Criar Campanha

### Search

1. Definir objetivo (conversões, tráfego)
2. Selecionar keywords (broad, phrase, exact)
3. Criar negative keyword list
4. Configurar bidding (Target CPA ou Target ROAS)
5. Definir budget diário
6. Criar ad groups com 2-3 Responsive Search Ads cada
7. Configurar extensions (sitelinks, callouts, structured snippets)
8. Definir targeting (geo, idioma, device, schedule)

### Shopping

1. Vincular Google Merchant Center
2. Verificar feed de produtos (títulos, preços, imagens, GTINs)
3. Criar campanha Shopping com Target ROAS
4. Definir budget diário
5. Configurar negative keywords por product group
6. Monitorar Search Terms Report para refinamento

### Performance Max

1. Definir conversion goal
2. Criar asset group (headlines, descriptions, images, videos, logos)
3. Configurar audience signals (custom segments, remarketing, in-market)
4. Definir bidding (Maximize Conversion Value + Target ROAS)
5. Definir budget diário
6. Adicionar negative keywords (nível campanha — disponível desde 2024)
7. Monitorar insights e placement reports

---

## Workflow: Otimização

### Diário
- Verificar pacing de budget (spend vs budget)
- Checar se alguma campanha parou de gastar
- Verificar conversões (tracking funcionando?)

### Semanal
- Análise de Search Terms → adicionar negative keywords
- Review de Quality Score por keyword
- Ajuste de bids/targets em campanhas manuais
- Análise de Impression Share (budget vs rank)

### Mensal
- Relatório completo de performance
- Comparativo período anterior
- Rebalanceamento de budget entre campanhas
- Review de bidding strategies (Manual → Smart quando houver dados)
- Análise de novos keywords/oportunidades

---

## Integração Ativa

### Credenciais (1Password: "Google Ads API - Spark", vault OpenClaw)
```
Developer Token (credential field)
Client ID (Google Ads section)
Client Secret (Google Ads section)
Refresh Token (Google Ads section)
Manager Account ID: 965-668-6533
Login Customer ID: 762-580-1774
```

### Como autenticar (refresh → access token)
```bash
curl -s -X POST https://oauth2.googleapis.com/token \
  -d "refresh_token=<REFRESH_TOKEN>" \
  -d "client_id=<CLIENT_ID>" \
  -d "client_secret=<CLIENT_SECRET>" \
  -d "grant_type=refresh_token"
```

### Endpoint REST
- Base: `https://googleads.googleapis.com/v23/`
- Headers obrigatórios:
  - `Authorization: Bearer <access_token>`
  - `developer-token: <dev_token>`
  - `login-customer-id: 9656686533` (quando acessando via manager account)
- Query endpoint: `POST /v23/customers/<CUSTOMER_ID>/googleAds:searchStream`
  - Body: `{"query": "<GAQL>"}`

---

## Referências

- API docs: `references/api-overview.md` (a criar quando integração ativa)
- Detalhes de bidding: na seção Bidding Strategies acima
- Design system relatórios: `skills/design/report-design-system/SKILL.md`
