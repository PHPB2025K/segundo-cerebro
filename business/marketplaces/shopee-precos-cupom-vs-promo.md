---
title: "Shopee — leitura de preços: cupom vs promoção vs preço cheio"
created: 2026-06-10
type: rule
status: active
tags:
  - marketplace/shopee
  - rule
  - pricing
---

# Shopee — leitura de preços nas saídas Trader/API

> Regra confirmada por Pedro em 10/06/2026 durante análise dos potes herméticos 4 travas na Conta 1 (budamix-store).

Quando o agente **Trader** (ou qualquer script direto na Shopee Open API v2) listar anúncios com a coluna "Promo ativa", os 3 estados possíveis traduzem assim:

| Flag bruto (API) | Tradução para apresentação | Significado |
|---|---|---|
| `PROMOÇÃO` / `Shopee Discount` | **Promoção oficial** | Campanha cadastrada no Seller Center com data início/fim. Aparece em `/discount/get_discount_list`. |
| `price_info` | **Cupom de desconto da loja** | Não tem campanha em `/discount/...` mas `current_price < original_price`. É cupom de loja aplicado em cima do preço base. |
| `sem promo` | **Preço cheio** | Sem desconto nem cupom. |

## Aplicação

- Em qualquer relatório/análise de preços Shopee (qualquer das 3 contas: budamix-store, budamix_store/Oficial, budamix-shop): substituir `price_info` por **"cupom de loja"** na apresentação final pro Pedro.
- Não voltar a apresentar `price_info` como ambíguo (descontinuada a explicação de "preço baixado direto OU cupom OU benefício automático" — Pedro já validou que é cupom).
- Se a planilha/análise tiver lógica diferenciando "PROMOÇÃO" e "cupom" pra cálculo de margem, tratar as duas como descontos efetivos sobre o preço base.

## Por que o Trader marca diferente

Trader usa heurística defensiva: só assume "PROMOÇÃO" quando confirma via endpoint `/discount/get_discount` que existe campanha ativa. Quando não confirma mas o `price_info.current_price` já vem reduzido, ele marca conservadoramente como `price_info promo` em vez de assumir promoção que pode não existir. Pedro confirmou que esse cenário corresponde a cupom de loja.
