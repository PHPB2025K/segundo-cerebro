---
name: ml-ads
description: Consultar e gerenciar campanhas de Product Ads do Mercado Livre via API. Use quando Pedro pedir dados de Ads ML, métricas de campanhas, ACOS, ROAS, cliques, impressões, performance de anúncios, listar campanhas ativas, ou qualquer análise de publicidade do Mercado Livre. Também usar para criar/editar campanhas e mover ads entre campanhas.
---

# ML Ads — Product Ads Mercado Livre

Acessa a API de Advertising do Mercado Livre (v2) para Product Ads, Brand Ads e métricas.

## Autenticação

```bash
# Refresh token antes de qualquer operação
bash /root/.openclaw/workspace/skills/marketplace/ml-extrato/scripts/ml-refresh-token.sh vendas

# Token
ACCESS_TOKEN=$(python3 -c "import json; print(json.load(open('/root/.openclaw/.ml-tokens.json'))['access_token'])")
```

Headers obrigatórios:
```
Authorization: Bearer $ACCESS_TOKEN
Api-Version: 2
```

## Dados da conta

| Campo | Valor |
|---|---|
| Advertiser ID | 172453 |
| Site ID | MLB |
| Nome | GAMMAOFICIAL |
| Moeda | BRL |
| Produto principal | Product Ads (PADS) |

## Quando usar

- Pedro pedir "como estão os Ads do ML"
- Relatório de performance de campanhas
- Análise de ROAS, ACOS, CPC, CTR
- Listar campanhas ativas/pausadas
- Métricas por anúncio
- Comparativo entre campanhas
- Dados pra seção 5 do marketplace-report

## Inputs necessários

| Input | Obrigatório | Descrição |
|---|---|---|
| Período | Sim | date_from e date_to (YYYY-MM-DD) |
| Escopo | Não | Todas campanhas, campanha específica, ou ad específico |
| Métricas | Não | Default: clicks,prints,cost,total_amount,acos,roas |

## Endpoints principais

Ver `references/endpoints.md` para lista completa com exemplos.

### Quick reference

```bash
# Listar campanhas com métricas
curl -s "https://api.mercadolibre.com/marketplace/advertising/MLB/advertisers/172453/product_ads/campaigns/search?metrics=clicks,prints,cost,total_amount,acos,roas&date_from=YYYY-MM-DD&date_to=YYYY-MM-DD&limit=50" \
  -H "Authorization: Bearer $ACCESS_TOKEN" -H "Api-Version: 2"

# Métricas diárias agregadas
curl -s "https://api.mercadolibre.com/advertising/advertisers/172453/product_ads/campaigns?aggregation_type=DAILY&metrics=clicks,prints,cost,total_amount,acos,roas,cpc,ctr,cvr,sov&date_from=YYYY-MM-DD&date_to=YYYY-MM-DD" \
  -H "Authorization: Bearer $ACCESS_TOKEN" -H "Api-Version: 2"

# Ads de uma campanha com métricas
curl -s "https://api.mercadolibre.com/advertising/MLB/advertisers/172453/product_ads/ads/search?campaign_id=CAMP_ID&metrics=clicks,prints,cost,total_amount,acos,roas&date_from=YYYY-MM-DD&date_to=YYYY-MM-DD&limit=50" \
  -H "Authorization: Bearer $ACCESS_TOKEN" -H "Api-Version: 2"
```

## Passo a passo de execução

1. Refresh token: `ml-refresh-token.sh vendas`
2. Carregar token do arquivo `.ml-tokens.json`
3. Chamar endpoint com `Authorization: Bearer` + `Api-Version: 2`
4. Parsear resposta JSON
5. Apresentar dados formatados

## Métricas disponíveis

| Métrica | Descrição |
|---|---|
| clicks | Cliques no anúncio |
| prints | Impressões (vezes que apareceu) |
| ctr | Click-through rate (clicks/prints) |
| cost | Investimento em R$ |
| cpc | Custo por clique médio |
| acos | Advertising Cost of Sales (cost/sales %) |
| roas | Return on Ad Spend (sales/cost) |
| cvr | Conversion rate |
| sov | Share of Voice |
| total_amount | Vendas totais (diretas + indiretas) |
| direct_amount | Vendas diretas (clicou e comprou) |
| indirect_amount | Vendas indiretas (viu e comprou depois) |
| units_quantity | Unidades vendidas |
| direct_units_quantity | Unidades vendidas diretas |
| indirect_units_quantity | Unidades vendidas indiretas |

## Estratégias de campanha

| Strategy | Uso | Comportamento |
|---|---|---|
| profitability | Best-sellers, foco em conversão | Menos impressões, maior ROAS |
| increase (growth) | Produtos de giro médio | Equilíbrio visibilidade/rentabilidade |
| visibility | Lançamentos, categorias competitivas | Máximo de impressões |

## Critérios de qualidade

- Sempre incluir período analisado nos dados
- ROAS e ACOS devem ser calculados corretamente (ROAS = sales/cost, ACOS = cost/sales × 100)
- Campanhas pausadas devem ser indicadas visualmente
- Comparativo com período anterior quando disponível
- Insights acionáveis: quais campanhas escalar, quais pausar, quais otimizar
- Consultar feedbacks em `memory/feedback/content.json` antes de formatar

## Regras operacionais

### Sem confirmação (executar direto)
- ✅ Qualquer GET (consultas, métricas, listagens)

### Com confirmação (perguntar antes)
- ❌ Criar campanha
- ❌ Atualizar budget
- ❌ Pausar/ativar campanha
- ❌ Mover ads entre campanhas
- ❌ Qualquer PUT/POST

<!-- MELHORIA 2026-03-18 -->
## Integração com marketplace-report

A seção 5 (`s05_ads.py`) do marketplace-report consome esta skill diretamente.
Dados confirmados com dados reais em 2026-03-17:
- ROAS global: 8.76x
- 21 campanhas analisadas
- Advertiser ID: 172453

Referência: `skills/marketplace/marketplace-report/scripts/sections/s05_ads.py`
<!-- FIM MELHORIA 2026-03-18 -->
