---
title: "field formats"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
  - amazon
---

# Formatos Exatos de Campos SP-API — Amazon BR

> Referencia rapida dos formatos que FUNCIONAM.
> Cada campo foi validado com submissao real.
> NUNCA chutar formato — copiar daqui.

## Campos de Texto (language_tag obrigatorio)

```json
"campo": [{
    "language_tag": "pt_BR",
    "value": "texto aqui",
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```
Aplica-se a: item_name, brand, manufacturer, bullet_point, product_description,
generic_keyword, color, condition_note, import_designation

## Campos de Valor Simples

```json
"campo": [{
    "value": "valor_aqui",
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```
Aplica-se a: country_of_origin, condition_type, model_number, part_number,
ncm_code, recommended_browse_nodes, power_source_type,
external_testing_certification, supplier_declared_dg_hz_regulation

## Campos Booleanos

```json
"campo": [{
    "value": true,
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```
Aplica-se a: batteries_required, skip_offer,
supplier_declared_has_product_identifier_exemption

## unit_count (FORMATO ESPECIAL)

```json
"unit_count": [{
    "value": 7.0,
    "type": {
        "value": "count",
        "language_tag": "pt_BR"
    },
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```
**value**: float (numero de unidades)
**type**: OBJETO (nao string!) com value + language_tag

## number_of_items

```json
"number_of_items": [{
    "value": 7,
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

## Preco (purchasable_offer)

```json
"purchasable_offer": [{
    "currency": "BRL",
    "our_price": [{
        "schedule": [{
            "value_with_tax": 39.90
        }]
    }],
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

## Preco Sugerido (list_price)

```json
"list_price": [{
    "currency": "BRL",
    "value_with_tax": 39.90,
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

## Dimensoes 3D (item_dimensions)

```json
"item_dimensions": [{
    "length": {"unit": "centimeters", "value": 8.0},
    "width": {"unit": "centimeters", "value": 8.0},
    "height": {"unit": "centimeters", "value": 10.0},
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

## Dimensoes 2D (item_length_width) — OBRIGATORIO ALEM DO 3D

```json
"item_length_width": [{
    "length": {"unit": "centimeters", "value": 8.0},
    "width": {"unit": "centimeters", "value": 8.0},
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

## Peso

```json
"item_package_weight": [{
    "unit": "grams",
    "value": 194.0,
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

## Fulfillment (FBA)

```json
"fulfillment_availability": [{
    "fulfillment_channel_code": "AMAZON_NA"
}]
```
Nota: SEM marketplace_id neste campo.

## Bullet Points (array de 5)

```json
"bullet_point": [
    {"language_tag": "pt_BR", "value": "Bullet 1...", "marketplace_id": "A2Q3Y263D00KWC"},
    {"language_tag": "pt_BR", "value": "Bullet 2...", "marketplace_id": "A2Q3Y263D00KWC"},
    {"language_tag": "pt_BR", "value": "Bullet 3...", "marketplace_id": "A2Q3Y263D00KWC"},
    {"language_tag": "pt_BR", "value": "Bullet 4...", "marketplace_id": "A2Q3Y263D00KWC"},
    {"language_tag": "pt_BR", "value": "Bullet 5...", "marketplace_id": "A2Q3Y263D00KWC"}
]
```
