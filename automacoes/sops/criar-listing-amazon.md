---
title: "SOP — Criar Listing Amazon BR"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - sop
  - amazon
  - listing
  - sp-api
---

# SOP — Criar Listing Amazon BR via SP-API

> Passo a passo para criar um listing na Amazon Brasil usando a skill amazon-listing-creator.

---

## Pré-requisitos

| Item | Valor |
|------|-------|
| Marketplace ID (BR) | A2Q3Y263D00KWC |
| Seller ID | AVZC2M082DE2P |
| SP-API Base URL | https://sellingpartnerapi-na.amazon.com |
| Fulfillment | FBA (AMAZON_NA) |
| Brand | Budamix (Brand Registry ativo) |
| Credenciais | 1Password → "Amazon SP-API - Tobias" |
| Skill | `skills/amazon-listing-creator/SKILL.md` |

---

## Processo em 10 Fases

### Fase 1 — Coletar dados do produto

- Nome do produto
- Material, dimensões (cm), peso (g)
- Preço (BRL)
- Fotos (mínimo 7, ideal 9, ≥1000px, primeira com fundo branco)
- SKU (padrão Budamix: DPM001, PCM001, etc.)
- CMV (custo)

### Fase 2 — Identificar Product Type

```bash
GET /definitions/2020-09-01/productTypes?marketplaceIds=A2Q3Y263D00KWC&keywords={termo}
```

Exemplos validados:
- Descanso de copos → `DRINK_COASTER`
- Descanso de panela → `TRIVET`

### Fase 3 — Obter campos obrigatórios

```bash
GET /definitions/2020-09-01/productTypes/{PRODUCT_TYPE}?marketplaceIds=A2Q3Y263D00KWC&requirements=REQUIRED&locale=pt_BR
```

### Fase 4 — Montar payload SP-API

Campos críticos (formato exato — errar causa rejeição):

**unit_count** (causa mais erros):
```json
"unit_count": [{"value": 7.0, "type": {"value": "count", "language_tag": "pt_BR"}, "marketplace_id": "A2Q3Y263D00KWC"}]
```

**list_price**:
```json
"list_price": [{"currency": "BRL", "value_with_tax": 39.90, "marketplace_id": "A2Q3Y263D00KWC"}]
```

**GTIN Exemption** (Budamix tem Brand Registry):
```json
"supplier_declared_has_product_identifier_exemption": [{"value": true, "marketplace_id": "A2Q3Y263D00KWC"}]
```

**item_dimensions** (3D):
```json
"item_dimensions": [{"length": {"unit": "centimeters", "value": 8.0}, "width": {"unit": "centimeters", "value": 8.0}, "height": {"unit": "centimeters", "value": 10.0}, "marketplace_id": "A2Q3Y263D00KWC"}]
```

### Fase 5 — Título

Formato (max 200 chars, recomendado ≤150):
```
[Produto] [Material] [Dimensão] - [Diferencial] - [Quantidade] - [Marca]
```

### Fase 6 — Upload de fotos

1. Upload para Supabase Storage (bucket `product-images`, pasta `{SKU}/`)
2. PATCH listing com URLs públicas
3. Amazon baixa e re-hospeda no CDN
4. Campos: `main_product_image_locator` (principal) + `other_product_image_locator_1..8`

### Fase 7 — Validar checklist

Consultar seção 7 da skill `amazon-listing-creator/SKILL.md`.

### Fase 8 — Submeter listing

```bash
PUT /listings/2021-08-01/items/{sellerId}/{sku}?marketplaceIds=A2Q3Y263D00KWC
Body: {"productType": "...", "requirements": "LISTING", "attributes": {...}}
```

### Fase 9 — Verificar resposta

- `ACCEPTED` → ASIN atribuído em 15-30 min
- `INVALID` → corrigir erros e resubmeter

### Fase 10 — Pós-criação

1. Aguardar ASIN (verificar a cada 5 min, até 30 min)
2. Registrar no Supabase (ASIN, SKU, preço, data)
3. Confirmar que sync scripts capturam o item
4. **Enviar estoque ao CD FBA** (inbound shipment via Seller Central)
5. Upload de fotos se não feito na Fase 6

---

## Exemplos Reais

| SKU | ASIN | Product Type | Preço | Data |
|-----|------|-------------|-------|------|
| DPM001 | B0GWS1151L | DRINK_COASTER | R$19,90 | 07/04/2026 |
| DPM002 | B0GX7RN9FS | TRIVET | R$34,90 | 14/04/2026 |

---

## Notas Relacionadas

- [[skills/amazon-listing-creator/SKILL]] — skill completa
- [[knowledge/concepts/credenciais-map]] — credenciais SP-API
- [[meta/mocs/MOC - Listing Pipeline]] — pipeline de listings
