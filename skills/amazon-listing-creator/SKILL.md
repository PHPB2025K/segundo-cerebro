---
name: amazon-listing-creator
description: Criacao de anuncios na Amazon BR via SP-API com todos os campos obrigatorios preenchidos. Evita trial-and-error documentando formatos exatos dos campos problematicos. Inclui GTIN exemption, FBA, browse nodes e simulacao de custos.
triggers:
  - "criar anuncio amazon"
  - "publicar na amazon"
  - "cadastrar produto amazon"
  - "listing amazon"
  - "novo anuncio amazon br"
metadata:
  openclaw:
    emoji: "\U0001F4E6"
    last_updated: "2026-04-07"
    sources:
      - "Amazon SP-API Listings Items API v2021-08-01"
      - "Amazon SP-API Product Type Definitions v2020-09-01"
      - "Cadastro real do Kit Porta-Copos PCM001 (07/04/2026)"
    related_skills:
      - shopee-listing-creator
      - shopee-fees-rules
      - ml-fees-rules
      - amazon-extrato
---

# Skill: Amazon Listing Creator — Budamix

> Cria anuncios na Amazon BR via SP-API com TODOS os campos preenchidos.
> Objetivo: status ACCEPTED na primeira submissao (zero erros, zero warnings).
> Baseado em licoes reais do cadastro PCM001 (9 erros na 1a tentativa -> 0 na 6a).

---

## 1. CREDENCIAIS E INFRAESTRUTURA

| Componente | Valor |
|------------|-------|
| SP-API Credentials | `/root/.openclaw/workspace/integrations/amazon/.sp-api-credentials.json` |
| Marketplace ID (BR) | `A2Q3Y263D00KWC` |
| Seller ID | `AVZC2M082DE2P` |
| SP-API Base | `https://sellingpartnerapi-na.amazon.com` |
| Auth | LWA Token + AWS STS AssumeRole + SigV4 |
| Fulfillment | FBA (`AMAZON_NA`) — padrao para todos os produtos Budamix |
| Brand | Budamix (registrada, Brand Registry ativo) |
| Marca sem GTIN | Exemption funciona (supplier_declared_has_product_identifier_exemption: true) |

Scripts de sync:
- `sync-amazon-orders.py` — orders -> Supabase
- `sync-amazon-prices.py` — precos -> Supabase
- `sync-inventory-amazon.py` — inventario FBA -> Supabase
- `amazon-request-reviews.py` — solicita avaliacoes

---

## 2. FLUXO DE CRIACAO (10 fases)

### Fase 1 — Receber dados do produto
Nome, material, dimensoes, peso, preco, fotos, SKU, CMV.

### Fase 2 — Identificar Product Type
```
GET /definitions/2020-09-01/productTypes?marketplaceIds=A2Q3Y263D00KWC&keywords={termo}
```
Retorna lista de product types possiveis. Usar o mais especifico.

### Fase 3 — Obter campos obrigatorios
```
GET /definitions/2020-09-01/productTypes/{PRODUCT_TYPE}?marketplaceIds=A2Q3Y263D00KWC&requirements=REQUIRED&locale=pt_BR
```
Se retornar schema link: baixar e parsear JSON Schema (propriedades required).
Se nao: usar a tabela de campos conhecidos (secao 4) + testar iterativamente.

### Fase 4 — Mapear dados para formato SP-API
Usar a referencia de formatos exatos (secao 5). NUNCA chutar formato — sempre copiar do que ja funcionou.

### Fase 5 — GTIN
- Se tem EAN/GTIN: usar `externally_assigned_product_identifier`
- Se nao tem: usar `supplier_declared_has_product_identifier_exemption: true`
- Budamix tem Brand Registry = exemption funciona para todos os product types testados

### Fase 6 — Preparar imagens
- Minimo 7, ideal 9 fotos
- Foto 1: fundo branco puro, produto ocupa 85%+ do frame, sem texto, sem logo overlay
- Todas >= 1000px no lado maior (ideal 1200x1200 ou 2000x2000)
- Formato: JPEG ou PNG
- Upload via Seller Central ou SP-API (Images API)
- Imagens sao referenciadas por URL no listing (main_product_image_locator, other_product_image_locator_1..8)

### Fase 7 — Validar contra checklist
Rodar checklist completo (templates/checklist.md) ANTES de submeter.

### Fase 8 — Submeter
```
PUT /listings/2021-08-01/items/{sellerId}/{sku}?marketplaceIds=A2Q3Y263D00KWC
```
Body: `{"productType": "...", "requirements": "LISTING", "attributes": {...}}`

### Fase 9 — Verificar resposta
- `ACCEPTED` = sucesso, ASIN sera atribuido em 15-30 min
- `INVALID` = erros nos campos, corrigir e resubmeter
- Erros comuns e solucoes na secao 7

### Fase 10 — Pos-criacao
- Aguardar ASIN (verificar a cada 5 min por 30 min)
- Registrar no Supabase (ASIN, SKU, preco, custos)
- Confirmar que scripts de sync capturam o item
- Upload de imagens via Seller Central (se nao feito via API)
- Notificar Pedro no Telegram (Thread 3)

---

## 3. TEMPLATE DE TITULO AMAZON BR

**Formato:** ate 200 chars (recomendado ate 150)
```
[Produto] [Material] [Dimensao/Spec] - [Diferencial] - [Quantidade] - [Marca]
```

**Regras:**
- Primeira letra de cada palavra relevante em maiuscula
- Sem ALL CAPS (exceto siglas: MDF, PS5)
- Sem precos, promocoes, "melhor", "gratis"
- Sem caracteres especiais: (R), (TM), !, #
- Marca no final ou inicio dependendo da categoria
- Keywords mais importantes nos primeiros 80 chars (indexacao prioritaria)

**Exemplo real (PCM001):**
```
Kit 6 Porta-Copos de MDF 6mm com Suporte Organizador - Design Solaris Corte a Laser - Descanso de Copo com Gravacao Decorativa - 7 Pecas - Budamix
```
(148 chars)

---

## 4. CAMPOS OBRIGATORIOS POR PRODUCT TYPE

### DRINK_COASTER (Descanso de Copos) — Validado 07/04/2026

| Campo API | Obrigatorio | Formato | Exemplo real |
|-----------|-------------|---------|--------------|
| item_name | SIM | language_tag + value + marketplace_id | Ver titulo acima |
| brand | SIM | language_tag + value + marketplace_id | "Budamix" |
| manufacturer | SIM | language_tag + value + marketplace_id | "Budamix" |
| bullet_point | SIM (5) | array de 5 objetos com language_tag + value | Ver template |
| product_description | SIM | language_tag + value (texto puro ou HTML basico) | Ver template |
| generic_keyword | SIM | language_tag + value (ate 250 bytes) | Keywords separadas por espaco |
| country_of_origin | SIM | value: "BR" | "BR" |
| condition_type | SIM | value: "new_new" | "new_new" |
| fulfillment_availability | SIM | fulfillment_channel_code: "AMAZON_NA" | FBA |
| purchasable_offer | SIM | currency + our_price.schedule.value_with_tax | R$39.90 |
| list_price | SIM | currency + value_with_tax + marketplace_id | R$39.90 |
| item_dimensions | SIM | length/width/height com unit + value | cm |
| item_length_width | SIM | length/width separados (alem de item_dimensions!) | cm |
| item_package_dimensions | SIM | length/width/height da embalagem | cm |
| item_package_weight | SIM | unit + value | grams |
| unit_count | SIM | **ATENCAO: formato especial** — ver secao 5 | 7.0 + type object |
| number_of_items | SIM | value (integer) | 7 |
| power_source_type | SIM | value: "does_not_require_power" | Para nao-eletronicos |
| external_testing_certification | SIM | value: "no_testing_required" | Para itens sem certificacao |
| supplier_declared_dg_hz_regulation | SIM | value: "not_applicable" | Para itens nao-perigosos |
| supplier_declared_has_product_identifier_exemption | SIM (se sem GTIN) | value: true | Para marca propria sem EAN |
| recommended_browse_nodes | SIM | value: browse_node_id | "17836821011" |
| ncm_code | REC | value: NCM sem pontos | "44111210" |
| import_designation | REC | language_tag + value: "2" | Nacional |
| batteries_required | REC | value: false | Para itens sem bateria |
| skip_offer | REC | value: false | Sempre false |
| color | REC | language_tag + value | "Marrom Natural" |
| model_number | REC | value: SKU ou modelo | "PCM001" |
| part_number | REC | value: SKU | "PCM001" |

> Quando cadastrar produto em categoria NOVA: rodar Fase 3, documentar campos aqui.

---

## 5. FORMATOS EXATOS DOS CAMPOS PROBLEMATICOS

### unit_count (CRITICO — causou 5 tentativas)
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
**ERRADO (nao funciona):**
- `"type": "count"` (string simples — rejeitado)
- `"type": "Count"` (case diferente — rejeitado)
- `{"value": 7}` (sem type — campo obrigatorio)
- `{"value": 7, "type": "count"}` (type como string — rejeitado)

**O `type` e um OBJETO com `value` + `language_tag`, nao uma string.**

### list_price / MSRP
```json
"list_price": [{
    "currency": "BRL",
    "value_with_tax": 39.90,
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

### GTIN Exemption (quando nao tem EAN)
```json
"supplier_declared_has_product_identifier_exemption": [{
    "value": true,
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```
**NAO usar** `externally_assigned_product_identifier` com `"type": "gtin_exemption"` — este formato e rejeitado.

### item_dimensions (3D)
```json
"item_dimensions": [{
    "length": {"unit": "centimeters", "value": 8.0},
    "width": {"unit": "centimeters", "value": 8.0},
    "height": {"unit": "centimeters", "value": 10.0},
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

### item_length_width (SEPARADO do item_dimensions!)
```json
"item_length_width": [{
    "length": {"unit": "centimeters", "value": 8.0},
    "width": {"unit": "centimeters", "value": 8.0},
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```
**A Amazon exige AMBOS: item_dimensions (3D) E item_length_width (2D).**

### Browse Node
```json
"recommended_browse_nodes": [{
    "value": "17836821011",
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

### Produto nao-perigoso
```json
"supplier_declared_dg_hz_regulation": [{
    "value": "not_applicable",
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

### Fonte de energia (nao-eletronico)
```json
"power_source_type": [{
    "value": "does_not_require_power",
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

### Certificacao (sem necessidade)
```json
"external_testing_certification": [{
    "value": "no_testing_required",
    "marketplace_id": "A2Q3Y263D00KWC"
}]
```

---

## 6. TEMPLATE DE BULLET POINTS

5 bullets obrigatorios, cada um ate 500 chars. Formato:

```
Bullet 1: KIT/COMPOSICAO — O que vem, quantidades, materiais, dimensoes
Bullet 2: DIFERENCIAL — Design exclusivo, tecnologia, o que so Budamix tem
Bullet 3: FABRICACAO/QUALIDADE — Origem, processo, acabamento, durabilidade
Bullet 4: USO/APLICACAO — Para que serve, onde usar, beneficios praticos
Bullet 5: EXTRAS — Suporte/acessorio incluso, presente, garantia
```

**Regras:**
- Primeira palavra em CAPS (keyword principal do bullet)
- Sem HTML nos bullets
- Sem precos ou promocoes
- Sem referencia a outras plataformas
- Keywords relevantes naturalmente distribuidas

---

## 7. ERROS COMUNS E SOLUCOES

| Erro | Causa | Solucao |
|------|-------|---------|
| 90220 "campo obrigatorio nao inserido" | Campo faltando no payload | Adicionar campo — ver secao 4 |
| 99022 "type nao tem valores suficientes" | unit_count com type como string | Usar type como objeto: {"value": "count", "language_tag": "pt_BR"} |
| 90220 "Dimensoes C x L" | item_length_width faltando | Adicionar ALEM de item_dimensions |
| 90220 "ASIN Sugerido" | merchant_suggested_asin faltando | Omitir o campo (Amazon atribui automaticamente para produtos novos) |
| 90220 "ID externa de produto" | GTIN faltando sem exemption | Usar supplier_declared_has_product_identifier_exemption: true |
| 90220 "Certificacao de teste externa" | Campo obrigatorio na categoria | Usar "no_testing_required" se nao exigir certificacao |
| 4000001 "valor invalido" | Formato do campo errado | Consultar secao 5 para formato exato |
| 90000900 "atributo nao pertence" | Campo de outra categoria | Remover o campo |

---

## 8. SIMULACAO DE CUSTOS AMAZON BR

### Referral Fee (comissao)
| Categoria | Fee |
|-----------|-----|
| Casa e Cozinha (Home & Kitchen) | **15%** |
| Eletronicos | 12-15% |
| Beleza | 15% |
| Brinquedos | 15% |

### FBA Fees (fulfillment)
Depende do tamanho e peso. Para itens pequenos/leves (~200g, 25x16x5cm):
- Picking & Packing: ~R$5-7
- Armazenagem: ~R$0.50/mes/unidade (varia por epoca)

### Simulacao Kit Porta-Copos a R$39,90
| Item | Valor |
|------|-------|
| Preco de venda | R$39,90 |
| (-) Referral Fee 15% | R$5,99 |
| (-) FBA Fee estimado | ~R$6,00 |
| (=) Receita liquida | ~R$27,91 |
| (-) CMV | R$5,04 |
| (=) Lucro | ~R$22,87 |
| Margem | ~57,3% |

### Comparacao entre plataformas (a R$39,90)
| | ML | Shopee | Amazon |
|---|---|---|---|
| Custos totais | R$11,45 | R$12,78 | ~R$11,99 |
| Frete vendedor | R$6,85 | R$0 | R$0 (FBA) |
| Custo real total | R$18,30 | R$12,78 | ~R$11,99 |
| Receita liquida | R$21,60 | R$27,12 | ~R$27,91 |
| **Margem** | **41,4%** | **55,3%** | **~57,3%** |

> Amazon e Shopee sao mais vantajosas que ML para este produto.

---

## 9. INTEGRACAO COM STACK

| Componente | Path/Config | Funcao |
|------------|-------------|--------|
| SP-API Credentials | integrations/amazon/.sp-api-credentials.json | Auth AWS SigV4 |
| sync-amazon-orders.py | scripts/ | Orders -> Supabase |
| sync-amazon-prices.py | scripts/ | Precos -> Supabase |
| sync-inventory-amazon.py | scripts/ | Inventario FBA -> Supabase |
| amazon-request-reviews.py | scripts/ | Solicita avaliacoes |
| Amazon Ads | Spark agent | Campanhas PPC |
| Supabase | Budamix Central | Registro de ASIN, SKU, custos |

---

## 10. LICOES APRENDIDAS (atualizar sempre)

1. `unit_count` e um objeto com `value` (float) + `type` (objeto com `value` + `language_tag`). NAO e string.
2. GTIN exemption usa `supplier_declared_has_product_identifier_exemption: true`, nao o campo `externally_assigned_product_identifier`.
3. Amazon exige AMBOS `item_dimensions` (3D) E `item_length_width` (2D) separadamente.
4. `merchant_suggested_asin` e obrigatorio MAS pode ser omitido para produtos novos (Amazon atribui).
5. Browse node para porta-copos BR: `17836821011`.
6. Product type DRINK_COASTER aceita GTIN exemption para Budamix.
7. Submissao ACCEPTED = ASIN pendente, normal. Demora 15-30 min.
8. Campos como `cpsia_cautionary_statement` e `unit_count_type` NAO pertencem a DRINK_COASTER — a API retorna warning e ignora.
9. O `import_designation` com value "2" = Nacional (fabricacao brasileira).
10. NCM deve ser enviado SEM pontos (ex: "44111210" nao "4411.12.10").
11. `list_price` e obrigatorio alem de `purchasable_offer` — sao campos diferentes.
12. SPC013 (ITEM_STAND) tem 35 atributos — usar como referencia de estrutura para novos product types.

---

## Changelog

| Data | Mudanca |
|------|---------|
| 2026-04-07 | Criacao da skill baseada no cadastro real do PCM001 (DRINK_COASTER) |
| 2026-04-07 | Documentados 9 erros da 1a tentativa e solucoes que funcionaram |
| 2026-04-07 | Mapeamento completo de campos para DRINK_COASTER (26 campos) |

---

## Notas relacionadas

- [[skills/shopee-listing-creator/SKILL|Shopee Listing Creator]]
- [[skills/spreadsheet-pricing/SKILL|Planilha de Precificação]]

---
## Referências
- [[skills/amazon-listing-creator/reference/known-product-types|Product Types Conhecidos]]
- [[skills/amazon-listing-creator/rules/field-formats|Formatos de Campo]]
- [[skills/amazon-listing-creator/rules/validation-rules|Regras de Validação]]
- [[skills/amazon-listing-creator/templates/bullet-points-template|Template Bullet Points]]
- [[skills/amazon-listing-creator/templates/checklist|Checklist]]
- [[skills/amazon-listing-creator/templates/description-template|Template Descrição]]
