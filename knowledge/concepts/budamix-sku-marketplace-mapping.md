---
title: "Budamix — mapeamento SKU site × marketplaces (componente-based)"
created: 2026-06-09
type: knowledge
status: active
tags:
  - knowledge/budamix-ecommerce
  - knowledge/marketplace
  - knowledge/skus
---

# Mapeamento SKU site × marketplaces

## Contexto

Pedro está fechando parceria com empresa que puxa contato (WhatsApp/email) via CPF de compradores nos marketplaces. O fluxo de pós-venda precisa decidir: cliente compra X no marketplace → manda mensagem direcionando pra **site Budamix** ou pra **recompra no próprio marketplace**.

## O problema do match

O site Budamix cadastra **kits como produto** (`KIT10YW320` = KIT FAMÍLIA 10 unidades 320ml quadrados), enquanto os marketplaces cadastram o **pote individual** (`YW320` = pote 320ml) e montam os kits via título do anúncio + variação de quantidade.

**Match literal por SKU não funciona** porque os universos usam granularidades diferentes.

## A lógica: componente-based

Um anúncio de marketplace cujo SKU base contém um componente (pote individual) deve ser linkado a TODOS os kits do site que contenham aquele pote — pra permitir upsell ("comprou 4 potes, leva kit de 10").

### Tabela de componentes (YW)

| Pote individual (marketplace) | Aparece nos kits do site |
|-------------------------------|--------------------------|
| `YW320` / `YW320SQ` | `KIT10YW320` (FAMÍLIA), `KIT20YW320` (COZINHA), `KIT9YWSQ_MIX` (PRÁTICO), `KIT6YWSQ_MIX` (SOLO) |
| `YW520` / `YW520SQ` | `KIT10YW520` (FAMÍLIA), `KIT20YW520` (COZINHA), `KIT9YWSQ_MIX`, `KIT6YWSQ_MIX` |
| `YW800` / `YW800SQ_T` / `YW800SQ` | `KIT10YW800` (FAMÍLIA), `KIT20YW800` (COZINHA), `KIT9YWSQ_MIX`, `KIT6YWSQ_MIX` |
| `YW640` / `YW640RC` | `KIT10YW640` (DESPENSA), `KIT20YW640` (LAR), `KIT9YW_MIX` (COMPLETO), `KIT6YW_MIX` (ESSENCIAL) |
| `YW1050` / `YW1050RC` / `YW105` | `KIT10YW1050` (DESPENSA), `KIT20YW1050` (LAR), `KIT9YW_MIX`, `KIT6YW_MIX` |
| `YW1520` / `YW1520RC` / `YW1520AZ` | `KIT10YW1520` (DESPENSA), `KIT20YW1520` (LAR), `KIT9YW_MIX`, `KIT6YW_MIX` |

### Tabela de componentes (IMB501 — potes redondos)

| Marketplace | Site |
|-------------|------|
| `IMB501C_T` (tampa cinza) | Conjunto Cinza, Combo CV, Combo PC, Kit Coleção 3 |
| `IMB501P_T` (tampa preta) | Conjunto Preta, Combo PC, Combo PV, Kit Coleção 3 |
| `IMB501V_T` (tampa vermelha) | Conjunto Vermelha, Combo CV, Combo PV, Kit Coleção 3 |

### SKU base composto (kits com múltiplos potes)

Quando o anúncio é kit composto, o SKU base na planilha de precificação tem múltiplos componentes separados por `/`:
- `YW320/YW520SQ/YW800SQ_T` (kit 3 sizes quadrados)
- `YW640RC/YW1050RC/YW1520RC` (kit 3 sizes retangulares)
- `CK4742_B / YW520SQ` (kit jarra + pote)

Cada componente é avaliado separadamente → o anúncio entra como filho de múltiplos kits do site.

## Snapshot 09/06

- **Total anúncios mapeados:** 358 (3 plataformas × até 3 contas Shopee)
- **SITE BUDAMIX:** 142 (40%) → direcionam pro e-commerce com URL específica
- **RECOMPRA MARKETPLACE:** 216 (60%) → SKUs legados (Tulipa porcelana, Clink jarra/canecas, Suporte gamer MDF, Descanso de panela MDF, Fita adesiva, Caceroletes etc.) que não estão no site

## Fonte da verdade

Planilha de Precificação oficial (Google Sheets):
- ID: `1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI`
- Abas usadas: ESTOQUE (base de SKUs físicos), SHOPEE, MELI, AMAZON
- Critério de "ativo": Pedro confirmou que linhas na planilha = anúncios ativos (inativos saem)
- Acesso via gspread + `~/.config/google-sheets-claude/token.json`

## Entregáveis (em `~/Downloads/`)

1. **`Budamix - Mapeamento SKUs.xlsx`** (interno — 5 abas)
   - Resumo, Produtos Ativos (11 produtos / 23 SKUs filhos), Produtos Inativos (legado), Anúncios Marketplace (678 relações), Pivot por SKU pai
2. **`Budamix - Mapa de Direcionamento Pós-venda.xlsx`** (pro parceiro — 3 abas)
   - Resumo, Instruções, Mapa de Direcionamento (358 linhas com cor SITE verde / MARKETPLACE terracota, hyperlinks pro produto no site, filtros automáticos)

## SKU pai derivado (planilha interna)

Algoritmo: longest common prefix dos SKUs filhos do mesmo produto, trimado de `_` ou `-` à direita. Quando só 1 variante: SKU pai = a própria. Quando sem SKU: `—`.

Colisões legítimas conhecidas no esquema atual:
- `KIT10YW`: compartilhado por KIT FAMÍLIA Quadrados (320/520/800) e KIT DESPENSA Retangulares (640/1050/1520) — mesmo prefixo, capacidades diferentes (a planilha tem o full SKU filho na próxima coluna pra desambiguação)
- `KIT20YW`: compartilhado por KIT COZINHA Quadrados e KIT LAR Retangulares
- `IMB501`: conjunto ativo + 3 listings espelho inativos
- `TL250A`: 7 listings espelho da família Tulipa (Amarela/Azul/Branca/Colorida/Preta/Rosa/Verde — cada cor era um listing próprio com as 7 variantes cruzadas, padrão de SEO antigo)

## Construção dos URLs por plataforma

| Plataforma | Padrão URL |
|------------|-----------|
| Mercado Livre | `https://produto.mercadolivre.com.br/{MLB-prefix}-{rest}` (ex.: `MLB3288536143` → `MLB-3288536143`) |
| Amazon | `https://www.amazon.com.br/dp/{ASIN}` (ex.: `B0GSWLK5F3`) |
| Shopee | usa link original da compra (não dá pra construir só pelo ID — precisa shop_id) |
| Site Budamix | `https://budamix.com.br/produto/{slug}` (slug puxado de `products.slug` no Supabase) |

## Ver também

- [[projects/budamix-ecommerce]]
- [[skills/marketplace/planilha-precificacao]] — skill que documenta as colunas da planilha de precificação
- [[memory/context/decisoes/2026-06]] — decisão de 09/06
