---
title: "SOP — Criar Listing na Shopee"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
estimated-time: "20-30 min"
tags:
  - sop
  - shopee
  - listing
  - marketplace
---

# SOP — Criar Listing na Shopee

## Objetivo

Criar um anúncio na Shopee Brasil para a marca Budamix usando a API Open Platform v2 ou a skill `shopee-listing-creator`.

## Pré-requisitos

- [ ] Acesso VPS (187.77.237.231) — API só funciona com IP autorizado
- [ ] Dados do produto (nome, material, dimensões, peso, preço, fotos)
- [ ] 9 fotos do produto (1200×1200px, JPG/PNG, <2MB cada)
- [ ] CMV calculado para validar margem

---

## Dados de Acesso

| Item | Valor |
|------|-------|
| Partner ID | 2031533 |
| API Base | https://partner.shopeemobile.com |
| API Version | v2 |
| Auth | HMAC-SHA256 |
| Brand ID Budamix | 5014011 |
| Skill | `shopee-listing-creator` (VPS: `/root/.openclaw/workspace/skills/`) |

### Lojas

| Loja | Shop ID | Tokens |
|------|---------|--------|
| budamix.store | 448649947 | `.shopee-tokens-budamix-store.json` |
| budamix-store2 | 860803675 | `.shopee-tokens-budamix-store2.json` |
| budamix-shop | 442066454 | `.shopee-tokens-budamix-shop.json` |

OAuth auto-refresh: cada 3h30 via `shopee_oauth.py`.

---

## Estrutura de Taxas Shopee (Abril 2026)

| Faixa | Preço | Comissão | Taxa Fixa | Observação |
|:-----:|-------|:--------:|:---------:|------------|
| 1 | ≤R$7,99 | 50% | R$0 | Inviável — evitar |
| **2** | **R$8–79,99** | **20%** | **R$4** | Faixa principal Budamix |
| 3 | R$80–99,99 | 14% | R$16 | 🔴 **EVITAR** — taxa fixa salta R$12 |
| 4 | R$100–199,99 | 14% | R$20 | Aceitável para kits grandes |
| 5 | R$200–499,99 | 14% | R$26 | — |
| 6 | R$500+ | 14% | R$26 | — |

**Regra de precificação:** NUNCA precificar entre R$80–99,99 (Faixa 3). Ir para R$79,90 ou R$100+.

Taxa de transação (~2%) já está embutida na comissão. NÃO somar separadamente.

---

## Procedimento

### Fase 1 — Coletar dados do produto

- Nome, material, dimensões (cm), peso (kg)
- Preço (validar contra tabela de taxas acima)
- SKU interno (padrão Budamix: PCM001, DPM001, etc.)
- CMV (custo) para cálculo de margem
- 9 fotos (foto 1 = lifestyle em uso, NÃO fundo branco)

### Fase 2 — Descobrir categoria

```
GET /api/v2/product/get_category?language=pt
```

Categorias validadas:
- **101247** — Placemats & Coasters (porta-copos)
- **101220** — Food Storage (potes)

### Fase 3 — Obter e preencher atributos

```
GET /api/v2/product/get_attributes?category_id={id}&language=pt
```

**Preencher 100% dos atributos obrigatórios.** Nunca deixar "Select" ou vazio.

Atributos comuns:
- Features (multi-valor)
- Warranty Type: "Garantia do Vendedor - 90 dias"
- Material, Pattern, Style, Dimensions, Pieces
- Country of Origin: "Brasil"

### Fase 4 — Formatar título e descrição

**Título** (max 120 chars):
```
[Marca] [Produto] [Material] [Spec Principal] [Quantidade]
```
Ex: "Budamix Kit 6 Porta Copos MDF 6mm Com Suporte Corte Laser Design Solaris"

**Descrição** (500-800 chars, texto puro, sem HTML):
```
→ Introdução (benefício principal)
→ Especificações
  ▪ Material: ...
  ▪ Dimensões: ...
→ Ideal para
→ Garantia
```

### Fase 5 — Gerar 20 tags

Extrair do título + sinônimos + palavras-chave de busca. Mínimo 15, ideal 20.

### Fase 6 — Comprimir e upload de fotos

```bash
# Comprimir se >2MB
sips -s format jpeg -s formatOptions 85 input.png --out output.jpg

# Upload via API
POST /api/v2/media_space/upload_image
```

Salvar `image_ids` retornados na ordem correta.

### Fase 7 — Criar item via API

```
POST /api/v2/product/add_item
```

Payload:
- `item_name`, `description`, `category_id`
- `original_price`, `normal_stock`
- `image.image_id_list` (9 IDs)
- `weight` (kg), `dimension` (L×W×H cm)
- `condition`: "NEW"
- `item_sku`
- `brand`: `{brand_id: 5014011, original_brand_name: "Budamix"}`
- `attribute_list` (100% preenchido)
- `logistic_info`: `[{logistic_id: 91003, enabled: true}]` (Shopee Xpress)
- `seller_stock`: `[{stock: N}]`

### Fase 8 — Verificar diagnóstico

Seller Center → Diagnóstico do produto. Score deve mostrar "Qualificado" (barra verde).

Se não verde: identificar campos faltantes, atualizar via `update_item`.

### Fase 9 — Replicar nas 3 lojas

Repetir criação para budamix-store2 e budamix-shop com mesmos dados.

### Fase 10 — Registrar e confirmar

- Registrar no Supabase (`iriqmqxuppfyrnselswk`) com platform=shopee
- Confirmar que `sync-shopee-prices.py` captura o novo item
- Notificar via Telegram

---

## Fórmula de Margem

```
Lucro = Preço - CMV - Comissão(%) - Taxa_Fixa - Imposto(7%) - Devoluções(4%) - Ads(5%) - R$1,75
Margem = (Lucro / Preço) × 100
```

**Custos fixos/un:** Caixa R$1,20 + Embalagem R$0,50 + Bilhete R$0,05 = R$1,75

**Meta margem mínima:** >15% sem afiliado, >5% com afiliado (10% adicional)

---

## Verificação

- [ ] Título ≤120 chars com marca Budamix
- [ ] 9 fotos ≤2MB, foto 1 = lifestyle
- [ ] Brand ID = 5014011 (NUNCA "Sem marca")
- [ ] 100% atributos obrigatórios preenchidos
- [ ] Tags: mínimo 15 de 20
- [ ] Preço NÃO está na faixa R$80–99,99
- [ ] Margem >15% calculada
- [ ] Logistics: Shopee Xpress (91003) habilitado
- [ ] Diagnóstico verde no Seller Center
- [ ] Replicado nas 3 lojas

## Troubleshooting

| Problema | Causa | Solução |
|----------|-------|---------|
| Diagnóstico não fica verde | Campos faltantes nos atributos | Usar método iterativo: submit um attr por vez via `update_item` |
| `api_suspended` em `get_attributes` | Partner account sem permissão | Fallback: método iterativo ou Seller Center manual |
| Imagem >2MB rejeitada | Resolução alta demais | Comprimir: `sips -s format jpeg -s formatOptions 85` |
| `error_invalid_logistic_info` | Payload de logística malformado | Usar: `logistic_info: [{logistic_id: 91003, enabled: true}]` |
| Margem negativa | Preço na Faixa 3 (R$80-99,99) | Mover para R$79,90 (Faixa 2) ou R$100+ (Faixa 4) |

## Referências

- [[skills/shopee-listing-creator/SKILL]] — skill completa
- [[knowledge/concepts/credenciais-map]] — credenciais
- [[meta/mocs/MOC - Listing Pipeline]] — pipeline de listings
- [[meta/mocs/MOC - Taxas e Precificacao]] — taxas e precificação
- [[automacoes/sops/criar-listing-amazon]] — SOP equivalente Amazon
