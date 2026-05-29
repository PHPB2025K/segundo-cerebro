---
title: "Daily Marketplace Baixa — cron 07h BRT (passo c)"
created: 2026-05-29
type: project-status
status: producao
project: estoque-gb-fase2
tags:
  - estoque
  - marketplaces
  - cron
  - producao
---

# Daily Marketplace Baixa — Passo (c) finalizado

> Implementado 29/05/2026. Processa vendas pagas do dia anterior nas 3 plataformas; **só baixa Seller** (Full/FBA/FBS já foi baixado pelo cron ENVIOS FULL).

## Princípio crítico: evitar dupla baixa

O motor de baixa **NUNCA** decrementa galpão para vendas Full/FBA/FBS, porque a baixa já aconteceu no momento do envio para o CD da plataforma. Decisão Pedro 29/05.

## Classificação por plataforma

| Plataforma | Como classifica | Volume típico/dia | % Seller (baixa galpão) |
|---|---|---|---|
| **Amazon** | hardcoded `full` (Pedro: 100% FBA) | ~39 | 0% |
| **ML** | `orders.logistic_type` → `fulfillment`=full ; `cross_docking`+demais=seller | ~108 | ~23% |
| **Shopee** | `raw_payload.shipping_carrier` → `Full`=full ; `Shopee Xpress`/`Retirada`=seller | ~120 | ~33% |

**Função SQL:** `public.classify_fulfillment(platform, logistic_type, raw_payload)` retorna `'full'|'seller'|'unknown'`.

Validação com 7 dias reais: **0 unknown** em 1.732 pedidos. 100% classificável.

## Schema

### `public.marketplace_sales_log`
- Log de TODOS os pedidos processados (Full + Seller + Unknown)
- UNIQUE (platform, platform_order_id, platform_item_id, sku_raw) garante idempotência
- `applied_to_stock` boolean — true só para Seller que conseguiu baixar
- `apply_skip_reason` text — `fulfillment_full` / `fulfillment_unknown` / motivo erro
- `stock_movement_id` referência ao ledger quando applied_to_stock=true
- `raw_payload` jsonb com prev/new qty e resoluções

## Pipeline

```
crons existentes (sync-orders-fast.sh + sync-amazon-orders-fast.sh)
   │ a cada 2-5min
   ↓
orders (Supabase) — populada continuamente
   │
   │ (cron 07h BRT)
   ↓
daily-marketplace-baixa.py — processa dia ANTERIOR (BRT)
   ├─ classify_fulfillment por item
   ├─ Full/Unknown → log only (marketplace_sales_log)
   └─ Seller → POST ingest-safe-outbound (sourceType='marketplace', apply=true)
         ↓
       stock_movements (ledger) + planilha ESTOQUE (decremento real)
```

## Resultado primeira execução (28/05/2026)

- 246 orders processados
- 195 itens Full (logados sem baixa)
- 52 itens Seller:
  - **12 aplicados** (baixa real)
  - **40 divergentes** (SKUs não cadastrados — Telegram alertou)
  - 0 erros

**Top SKUs divergentes** que precisam alias/kit_bom:
- `CTL002`, `KIT6CAR200`, `IMB501PT`, `IMB501V`, `KIT6YW320`, `SPC0111`, `KIT10YW320`, `XCP002`, `IMB501CT`, `KIT10YW520`, `KITYW320`, `KITYW640`

Maioria parece ser:
- Kits novos (KIT6CAR200, KIT6YW320, KIT10YW320, KIT10YW520) — cadastrar em `kit_bom`
- SKUs com sufixo errado (IMB501PT/IMB501V/IMB501CT vs IMB501P_T/IMB501V_T/IMB501C_T) — cadastrar em `sku_aliases`
- Códigos numéricos (098, 096, 101) — Pedro decide

## Arquivos / Localizações

| Item | Path |
|---|---|
| Script | `/var/www/mission-control/scripts/daily-marketplace-baixa.py` |
| Log | `/var/www/mission-control/data/daily-marketplace-baixa.log` |
| Lockfile | `/var/run/daily-marketplace-baixa.lock` (fcntl LOCK_EX) |
| Cron | `0 10 * * *` UTC (= 07h BRT), 1h após cron ENVIOS FULL |
| Tabela | `public.marketplace_sales_log` |
| Função | `public.classify_fulfillment(text, text, jsonb)` |

## Telegram digest diário (tópico Estoque) — formato Pedro aprovou 29/05

Separa explicitamente "VENDA FULL" (não baixou galpão) de "VENDA DIÁRIA" (baixou ou tentou baixar do galpão), com totais em unidades + pedidos por plataforma.

```
📊 Vendas marketplaces — DD/MM/YYYY

📦 VENDA FULL (não baixou galpão):
  • Amazon: N unidades (M pedidos)
  • Mercado Livre: N unidades (M pedidos)
  • Shopee: N unidades (M pedidos)
  Total: N unidades

🛒 VENDA DIÁRIA (baixou ou tentou baixar do galpão):
  • Amazon: N unidades (M pedidos)
  • Mercado Livre: N unidades (M pedidos)
  • Shopee: N unidades (M pedidos)
  Total: N unidades

✅ N unidades baixaram certinho
⚠️ N unidades ficaram pendentes (SKU não cadastrado)

🚨 SKUs sem cadastro (N distintos):
  • SKU1 (Mercado Livre)
  ...
Cadastrar em sku_aliases (alias) ou kit_bom (kit)
```

Nomenclatura segue regra Pedro: nunca usar "Seller/Full/FBA/FBS" na comunicação visível — só os termos "venda diária" e "venda Full" em português.

## Idempotência (3 camadas)

1. `marketplace_sales_log` UNIQUE — mesmo item nunca processado 2x
2. `stock_movements.external_event_id` UNIQUE — motor descarta dupla baixa
3. Lockfile fcntl — não roda em paralelo

## Edge cases tratados

- ✅ Pedido com kit (resolver_sku expande)
- ✅ Múltiplos items no mesmo pedido (cada item classificado/processado independentemente)
- ✅ Pedido pago tarde da noite (cron 07h pega completo)
- ✅ Race com sync orders (UNIQUE garante)
- ✅ unknown fulfillment → log com apply_skip_reason, não baixa (segurança)
- ⏳ Pedido cancelado APÓS baixa aplicada → atual: só log status mudou; reversão automática = Fase futura

## Status final do plano arquitetura v2

| Frente | Status |
|---|---|
| (a) Renomeação + aba Físico tempo real | ✅ |
| (b) WhatsApp Estoque + Atacado parser | ✅ |
| (c) Cron marketplaces tempo real | ✅ (este doc) |

## Próximos passos sugeridos

1. **Cadastrar aliases dos 12 SKUs divergentes** (lista acima) → próxima rodada cron baixa mais
2. **Dashboard de conciliação Full**: comparar `marketplace_sales_log` (Full) com cron ENVIOS FULL pra detectar discrepância
3. **Reversão automática de pedidos cancelados** após baixa (Fase futura)
4. **Webhooks marketplaces** (push real-time em vez de polling) — só se latência de 24h se tornar problema
