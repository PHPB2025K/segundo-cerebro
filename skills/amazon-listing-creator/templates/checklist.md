---
title: "checklist"
created: 2026-04-14
type: skill
domain: marketplace
status: active
tags:
  - skill/marketplace
  - amazon
---

# Checklist Pre-Submissao Amazon BR — Budamix

> Verificar TODOS os itens antes de chamar PUT /listings.
> Target: ACCEPTED na primeira tentativa.

## Identificacao
- [ ] SKU definido (padrao Budamix: PCM001, XCP001, SPC001...)
- [ ] Product Type identificado via SP-API (ex: DRINK_COASTER, ITEM_STAND)
- [ ] Browse Node correto para a categoria

## Titulo e Conteudo
- [ ] Titulo: ate 200 chars (ideal 150), keywords nos primeiros 80
- [ ] Titulo contem marca "Budamix"
- [ ] Titulo sem ALL CAPS, sem preco, sem promocao
- [ ] 5 bullet points preenchidos (ate 500 chars cada)
- [ ] Descricao completa (HTML basico permitido: br, b, ul, li)
- [ ] Backend search terms (ate 250 bytes, sem repetir titulo)

## Atributos Obrigatorios
- [ ] brand = "Budamix" (language_tag: pt_BR)
- [ ] manufacturer = "Budamix"
- [ ] condition_type = "new_new"
- [ ] country_of_origin = "BR"
- [ ] list_price com currency BRL e value_with_tax
- [ ] purchasable_offer com our_price.schedule.value_with_tax
- [ ] fulfillment_availability = "AMAZON_NA" (FBA)

## Dimensoes e Peso (3 campos separados!)
- [ ] item_dimensions (length + width + height em cm)
- [ ] item_length_width (length + width em cm) — SEPARADO do item_dimensions!
- [ ] item_package_dimensions (embalagem: length + width + height em cm)
- [ ] item_package_weight (peso em grams)

## Campos Especiais (os que causam INVALID)
- [ ] unit_count: valor float + type como OBJETO {"value": "count", "language_tag": "pt_BR"}
- [ ] number_of_items: valor inteiro
- [ ] power_source_type: "does_not_require_power" (para nao-eletronicos)
- [ ] external_testing_certification: "no_testing_required" (se nao exigir)
- [ ] supplier_declared_dg_hz_regulation: "not_applicable" (para nao-perigosos)
- [ ] recommended_browse_nodes: browse_node_id como string

## GTIN / Identificacao
- [ ] Se tem EAN: usar externally_assigned_product_identifier
- [ ] Se NAO tem EAN: supplier_declared_has_product_identifier_exemption = true
- [ ] NUNCA enviar ambos ao mesmo tempo

## Informacoes Fiscais BR
- [ ] ncm_code: NCM sem pontos (ex: "44111210")
- [ ] import_designation: "2" (Nacional)

## Imagens
- [ ] Minimo 7 fotos (ideal 9)
- [ ] Foto 1: fundo branco puro, produto 85%+ do frame, sem texto
- [ ] Todas >= 1000px no lado maior
- [ ] Formato JPEG ou PNG
- [ ] Upload via Seller Central ou SP-API

## Opcionais mas Recomendados
- [ ] color (language_tag + value)
- [ ] model_number (SKU ou nome do modelo)
- [ ] part_number (SKU)
- [ ] batteries_required = false
- [ ] skip_offer = false
- [ ] condition_note = "Novo"

## Pos-Submissao
- [ ] Resposta = ACCEPTED (0 erros)
- [ ] ASIN atribuido (verificar em 15-30 min)
- [ ] Imagens uploadadas via Seller Central
- [ ] Registrado no Supabase
- [ ] Scripts de sync confirmados
- [ ] Pedro notificado no Telegram (Thread 3)
