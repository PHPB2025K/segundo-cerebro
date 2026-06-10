---
title: "Estoque Pipeline — refatoração jun/26 (6 fixes + CMV Full)"
created: 2026-06-10
type: automation
status: active
tags:
  - automacao/estoque
  - estoque/budamix
  - openclaw/kobe
---

# Estoque Pipeline — Refatoração 10/06/2026

> Auditoria dos processamentos 06-08/06 + execução completa de 6 fixes estruturais + religação do CMV Full Backfill.

## Crons ativos pós-refatoração

| Cron | Horário BRT | Script | Função |
|---|---|---|---|
| Envios Full Daily | 06:00 (09 UTC) | `/var/www/mission-control/scripts/envios-full-daily-cron.py` | Baixa XLSX ENVIOS FULL via gog drive, parser snapshot-diff por cursor de linha, ingere movimentos novos no motor |
| Daily Marketplace Baixa | 07:00 (10 UTC) | `/var/www/mission-control/scripts/daily-marketplace-baixa.py` | Processa orders ML/Shopee/Amazon do dia anterior, distingue seller (baixa estoque) vs full (CMV-only), digest 7 seções |
| WhatsApp Estoque Healthcheck | 15/45 min | `/var/www/mission-control/scripts/whatsapp-estoque-healthcheck.py` | Alerta Telegram se houver msg pendente >30min OU sem ingest >6h |
| SKU Unresolved Escalator | 10:30 (13:30 UTC) | `/var/www/mission-control/scripts/sku-unresolved-escalator.py` | Detecta SKUs divergentes ≥2 dias dos últimos 7d e sugere mapeamento |
| CMV Full Backfill | 10:10 (13:10 UTC) | `/root/scripts/cmv-full-daily.sh` → `cmv-full-backfill.py` | Cria snapshots CMV para vendas Full/FBA (D-7 → D+1, idempotente) |
| CMV Revenue Backfill | 10:20 (13:20 UTC) | `/var/www/mission-control/scripts/cmv-revenue-backfill.py` | Preenche `gross_revenue_brl` nos snapshots existentes (range D-7) |

## Bugs corrigidos

### #1 Duplicação de logs
- **Sintoma:** cada linha de log aparecia 2x em `envios-full-daily-cron.log` e `daily-marketplace-baixa.log`.
- **Causa raiz:** função `log()` fazia `print()` (capturado pelo redirect do cron `>> file 2>&1`) E `f.write()` direto no mesmo arquivo.
- **Fix:** removido `print()` em ambos os scripts. Cron continua escrevendo stdout no arquivo, log()` mantém f.write() único.

### #2 WhatsApp Estoque Processor — diagnóstico falso de "parado"
- **Sintoma:** zero atividade no log 07-08/06.
- **Causa raiz:** simplesmente não houve mensagens nos grupos. Processor + poller ambos OK.
- **Fix:** criado healthcheck que distingue "sem dados" de "travado" (verifica msgs pendentes não processadas + tempo desde último INGEST + status PM2).

### #3 CMV revenue backfill com range estreito
- **Sintoma:** dias 03/06 e 05/06 ficaram com snapshots sem receita preenchida.
- **Causa raiz:** default `--from=ontem --to=hoje` (range de 1 dia). Quando `cmv-full-backfill` cria snapshots tardiamente, eles passam fora da janela do revenue backfill.
- **Fix:** default ampliado para D-7 → D no `cmv-revenue-backfill.py`.

### #4 Sem alerta proativo de ruptura
- **Sintoma:** mesmos SKUs em saldo zero geravam dezenas de divergências dia após dia (YW1520RC, YW1050RC, CAR200R, CAR200B). Pedro não recebia destaque.
- **Fix:** nova função `fetch_critical_ruptures(target_date)` em `daily-marketplace-baixa.py`. Filtra divergentes por motivo `Estoque insuficiente em X (atual: N, ...)` com `N ≤ 5`. Agrega por SKU pai e adiciona seção `🔴 RUPTURA CRÍTICA` no digest.

### #5 SKUs unresolved recorrentes não escalavam
- **Sintoma:** `KITIMB501P_T`, `914C_B2` apareciam como divergente em 3 dias seguidos sem ninguém cadastrar alias.
- **Fix:** `sku-unresolved-escalator.py` agendado 10:30. Query divergências últimos 7d, filtra recorrentes (≥2 dias distintos), sugere matches via `difflib.get_close_matches` contra `_catalog_estoque`. Telegram thread Estoque.

### #6 Clink/Microfibra ainda gerando divergente
- **Sintoma:** envio `AM333B` com 100 un `CK4742_B` gerou divergência em 06/06 (Clink descontinuado 28/05).
- **Fix:** `SKU_DISCONTINUED_PREFIXES = ("CK", "PANO", "MICROFIBRA")` no parser. Items com prefix são pulados como `skipped` (não geram movimento nem divergência).

## CMV Full Backfill — religado

### Bug encontrado
Pedidos com **itens duplicados internos** (API marketplace retorna mesmo `item_id+sku+qty` repetidos no mesmo pedido) → script gerava `external_event_id` idêntico no batch → constraint `ux_stock_movements_source_event` (partial UNIQUE INDEX `WHERE external_event_id IS NOT NULL`) rejeitava com HTTP 409.

PostgREST **não aceita** `resolution=ignore-duplicates` em partial unique indexes (precisa de constraint UNIQUE explícita).

### Fix em 2 camadas
```python
# Camada 1: dedupe contra banco — set carregado sem filtro de data
existing = {row["external_event_id"] for row in fetch_all(
    "/stock_movements?select=external_event_id"
    "&source_type=eq.marketplace&source_channel=eq.full_cmv"
    "&external_event_id=like.cmvfull:*"
)}

# Camada 2: dedupe intra-batch
seen_in_batch = set()
for m in movements_to_create:
    eid = m["external_event_id"]
    if eid in existing or eid in seen_in_batch:
        continue
    seen_in_batch.add(eid)
    deduped_movements.append(m)
```

### Recuperação 4 dias

| Dia | Snapshots | Receita | CMV |
|---|---|---|---|
| 04/06 | 416 | R$ 9.602 | R$ 3.829 |
| 06/06 | 299 | R$ 8.918 | R$ 2.769 |
| 07/06 | 227 | R$ 8.389 | R$ 2.822 |
| 08/06 (parcial) | 68 | R$ 2.217 | R$ 768 |

Total: ~R$ 29k receita + R$ 10k CMV que estavam zerados no DRE Full.

## Em aberto

- 4 SKUs componentes em ruptura (saldo 0): CAR200R, CAR200B, YW1520RC, YW1050RC. CAC250P=1, CAC250AZ=5. Precisa repor ou desativar kits dependentes.
- Unresolved continuando: `KITIMB501P_T` (mapear → IMB501P_T), `914C_B2` (ignorar — Clink antigo, já coberto pelo denylist mas como `914C_B2` começa com `9` e não `CK`, precisa add `EXACT` se quiser eliminar do escalator).
