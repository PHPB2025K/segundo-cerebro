---
title: "known product types"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
  - amazon
---

# Product Types Conhecidos — Amazon BR

> Atualizar sempre que cadastrar produto em categoria nova.
> Cada entry inclui: product type, display name, browse node, campos especificos.

---

## DRINK_COASTER — Descanso de Copos

| Dado | Valor |
|------|-------|
| Product Type | DRINK_COASTER |
| Display Name | Descanso de Copos |
| Browse Node BR | 17836821011 |
| Referral Fee | 15% (Home & Kitchen) |
| GTIN Exemption | Funciona (testado 07/04/2026) |
| Primeiro SKU | PCM001 |
| Campos obrigatorios | 26 (ver SKILL.md secao 4) |

**Campos especificos desta categoria:**
- unit_count obrigatorio com type object
- item_length_width obrigatorio (alem de item_dimensions)
- external_testing_certification obrigatorio ("no_testing_required")
- power_source_type obrigatorio ("does_not_require_power")
- supplier_declared_dg_hz_regulation obrigatorio ("not_applicable")

**NCM:** 44111210 (paineis de fibra de madeira MDF)

---

## ITEM_STAND — Suporte/Organizador

| Dado | Valor |
|------|-------|
| Product Type | ITEM_STAND |
| Display Name | Suporte |
| Browse Node BR | 23575039011 |
| Referral Fee | 15% |
| GTIN Exemption | Funciona (SPC013 sem GTIN, ativo) |
| SKUs ativos | SPC001-SPC015 |
| Campos obrigatorios | ~35 (baseado em SPC013) |

**Campos especificos desta categoria:**
- variation_theme: COLOR (variantes por cor)
- child_parent_sku_relationship (se tiver variantes)
- parentage_level: "child" ou "parent"

**NCM:** 95045000 (jogos e brinquedos)

---

## A MAPEAR (quando cadastrar)

| Product Type | Produto Budamix | Status |
|---|---|---|
| CERAMIC_CUP ou similar | Xicara Paris XCP | A descobrir |
| GLASS_STORAGE_JAR ou similar | Potes Hermeticos | A descobrir |
| TULIP_CUP ou similar | Caneca Tulipa CTL | A descobrir |

> Para descobrir: GET /definitions/2020-09-01/productTypes?keywords={termo}&marketplaceIds=A2Q3Y263D00KWC
