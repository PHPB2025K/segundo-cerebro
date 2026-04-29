---
title: "Budamix Central Refactor Full — 01A Diagnóstico Shopee"
created: 2026-04-29
type: reference
status: active
tags:
  - project
  - budamix-central
  - refactor
  - shopee
  - diagnostico
---

# Budamix Central Refactor Full — 01A Diagnóstico Shopee

Diagnóstico read-only por conta do sync de inventário Shopee. Objetivo: descobrir por que `fulfillment_inventory` só estava atualizando a conta `448649947`, enquanto `860803675` e `442066454` ficaram paradas.

Restrições respeitadas:
- Banco em read-only para o diagnóstico: nenhum upsert real foi executado manualmente.
- Script original `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py` não foi alterado.
- Cópia debug usada: `/tmp/sync-shopee-debug.py` com `supabase_upsert()` mockado.
- Não rodei `sync-inventory-cron.sh` manualmente.
- Não houve PM2 restart.
- Nenhum token/segredo foi copiado para o vault.

---

## Logs do cron

### Localização

Logs localizados em:

- `/var/log/budamix-sync/inventory-shopee-YYYYMMDD.log`
- Logs recentes encontrados de `20260421` até `20260429`.

Não há mail root:

- `/var/spool/mail/root` não existe no host (`NO_ROOT_MAIL_FILE`).

Não encontrei logs relevantes em:

- `/root/scripts/logs/`
- `/root/.openclaw/workspace/logs/`

### Últimos ciclos

Cron configurado:

```cron
15,45 * * * * /root/scripts/sync-inventory-cron.sh
```

Wrapper relevante:

- `/root/scripts/sync-inventory-cron.sh:20` executa `timeout 300 python3 "$SCRIPTS/sync-inventory-shopee.py"`.

Trecho do wrapper:

```bash
timeout 300 python3 "$SCRIPTS/sync-inventory-shopee.py" >> "$LOG_DIR/inventory-shopee-$DATE.log" 2>&1
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Shopee exit=$?" >> "$LOG_DIR/inventory-shopee-$DATE.log"
```

### Execuções nas últimas 24h

```bash
grep -h 'Starting Shopee inventory sync' /var/log/budamix-sync/inventory-shopee-2026042*.log
# Resultado resumido: 49 execuções entre 2026-04-28T13:45Z e 2026-04-29T13:45Z.
```

Hoje, até a coleta inicial, havia 27 execuções no arquivo do dia `20260429`.

### Padrão dos logs

Os logs do cron têm apenas wrapper start/exit, sem stdout detalhado por conta:

```text
[2026-04-29T13:15:01Z] Starting Shopee inventory sync
[2026-04-29T13:20:04Z] Shopee exit=0
[2026-04-29T13:45:01Z] Starting Shopee inventory sync
[2026-04-29T13:50:04Z] Shopee exit=0
```

Grep por erros nos logs de inventário Shopee não encontrou ocorrências:

```bash
grep -RIniE 'ERROR|WARN|FAIL|401|403|expired|invalid|error_auth|invalid_token|shop_id|budamix|❌|⚠️' /var/log/budamix-sync/inventory-shopee-*.log
# Resultado: sem linhas relevantes.
```

### Confirmação pós-cron 13:45

Depois do cron das `13:45Z`, o banco mostrou:

```sql
SELECT shop_id, last_synced
FROM fulfillment_inventory
WHERE platform = 'shopee'
ORDER BY last_synced DESC
LIMIT 1;
-- Resultado por shop_id:
-- 448649947 => 2026-04-29T13:48:12Z
-- 860803675 => 2026-04-18T22:18:43Z
-- 442066454 => 2026-04-01T15:26:01Z
```

Leitura: o cron continua atualizando só a primeira conta (`448649947`). As duas contas seguintes não chegam a persistir no banco.

---

## Token files

Arquivos inspecionados sem copiar conteúdo. Só `stat` + keys JSON.

| Conta | shop_id | Arquivo | mtime epoch | mtime humano | size | keys |
|---|---:|---|---:|---|---:|---|
| Budamix Store | `448649947` | `.shopee-tokens-budamix-store.json` | `1777466767` | `2026-04-29 12:46:07 UTC` | `460` bytes | `access_token`, `access_token_expire_in`, `partner_id`, `refresh_token`, `refresh_token_expire_in`, `shop_id`, `token_obtained_at`, `updated_at` |
| Budamix Oficial | `860803675` | `.shopee-tokens-budamix-store2.json` | `1777466770` | `2026-04-29 12:46:10 UTC` | `460` bytes | `access_token`, `access_token_expire_in`, `partner_id`, `refresh_token`, `refresh_token_expire_in`, `shop_id`, `token_obtained_at`, `updated_at` |
| Budamix Shop | `442066454` | `.shopee-tokens-budamix-shop.json` | `1777466773` | `2026-04-29 12:46:13 UTC` | `460` bytes | `access_token`, `access_token_expire_in`, `partner_id`, `refresh_token`, `refresh_token_expire_in`, `shop_id`, `token_obtained_at`, `updated_at` |

Conclusão dos token files:

- Os 3 arquivos existem.
- Os 3 são JSON válido.
- Os 3 têm `access_token` e `refresh_token`.
- Os 3 foram regravados hoje às ~12:46 UTC.
- **H1 refresh token expirado não confirmou no estado atual**, porque as 3 contas autenticaram e retornaram dados no debug isolado.

---

## Execução isolada

Cópia debug criada em `/tmp/sync-shopee-debug.py`.

Alterações feitas apenas na cópia:

- `supabase_upsert()` substituído por `DRY_RUN upsert skipped`, imprimindo contagem e sample de até 3 rows.
- `TARGET_SHOP` usado para filtrar uma conta por execução.
- Logs adicionais de chamadas Shopee com path, HTTP 200, `error`, `message`, `request_id`.
- Segredos Supabase redigidos na cópia debug para evitar escrita acidental.

Arquivos de log gerados:

- `/tmp/shopee-debug-448649947.log`
- `/tmp/shopee-debug-860803675.log`
- `/tmp/shopee-debug-442066454.log`

### Conta `448649947` — Budamix Store

Comando:

```bash
TARGET_SHOP=448649947 python3 /tmp/sync-shopee-debug.py > /tmp/shopee-debug-448649947.log 2>&1
```

Resultado:

| Etapa | Status |
|---|---|
| Token refresh | Não precisou refresh; token file recente. Sem erro. |
| `get_item_list` | OK, HTTP 200, 3 chamadas, `278 active items`. |
| `get_item_base_info` | OK, HTTP 200, 6 chamadas. |
| `get_model_list` | OK, HTTP 200, 122 chamadas. |
| Payload DB | `DRY_RUN`, escreveria 32 rows. |
| Linha onde para | Não para; execução completa. |
| Mensagem Shopee | Sem `error`; `message` vazio; request_ids presentes. |

Resumo do log:

```text
TARGET_SHOP=448649947 accounts=[448649947]
budamix-store: 278 active items
budamix-store: 122 items with models fetched, 32 SKUs with stock
DRY_RUN upsert skipped: would_upsert=32 rows
✅ Total: 32 SKUs synced across 3 stores
```

Duração isolada:

```text
2026-04-29T13:38:09Z → 2026-04-29T13:41:21Z = 192.5s
```

### Conta `860803675` — Budamix Oficial / Store2

Comando:

```bash
TARGET_SHOP=860803675 python3 /tmp/sync-shopee-debug.py > /tmp/shopee-debug-860803675.log 2>&1
```

Resultado:

| Etapa | Status |
|---|---|
| Token refresh | Não precisou refresh; token file recente. Sem erro. |
| `get_item_list` | OK, HTTP 200, 3 chamadas, `296 active items`. |
| `get_item_base_info` | OK, HTTP 200, 6 chamadas. |
| `get_model_list` | OK, HTTP 200, 121 chamadas. |
| Payload DB | `DRY_RUN`, escreveria 27 rows. |
| Linha onde para | Não para; execução completa. |
| Mensagem Shopee | Sem `error`; `message` vazio; request_ids presentes. |

Resumo do log:

```text
TARGET_SHOP=860803675 accounts=[860803675]
budamix-store2: 296 active items
budamix-store2: 121 items with models fetched, 27 SKUs with stock
DRY_RUN upsert skipped: would_upsert=27 rows
✅ Total: 27 SKUs synced across 3 stores
```

Duração isolada:

```text
2026-04-29T13:41:21Z → 2026-04-29T13:44:31Z = 189.7s
```

### Conta `442066454` — Budamix Shop

Comando:

```bash
TARGET_SHOP=442066454 python3 /tmp/sync-shopee-debug.py > /tmp/shopee-debug-442066454.log 2>&1
```

Resultado:

| Etapa | Status |
|---|---|
| Token refresh | Não precisou refresh; token file recente. Sem erro. |
| `get_item_list` | OK, HTTP 200, 3 chamadas, `300 active items`. |
| `get_item_base_info` | OK, HTTP 200, 6 chamadas. |
| `get_model_list` | OK, HTTP 200, 129 chamadas. |
| Payload DB | `DRY_RUN`, escreveria 27 rows. |
| Linha onde para | Não para; execução completa. |
| Mensagem Shopee | Sem `error`; `message` vazio; request_ids presentes. |

Resumo do log:

```text
TARGET_SHOP=442066454 accounts=[442066454]
budamix-shop: 300 active items
budamix-shop: 129 items with models fetched, 27 SKUs with stock
DRY_RUN upsert skipped: would_upsert=27 rows
✅ Total: 27 SKUs synced across 3 stores
```

Duração isolada:

```text
2026-04-29T13:44:31Z → 2026-04-29T13:47:54Z = 202.4s
```

### Comparativo de chamadas

| shop_id | `get_item_list` HTTP 200 | `get_item_base_info` HTTP 200 | `get_model_list` HTTP 200 | erros HTTP/Shopee |
|---:|---:|---:|---:|---:|
| `448649947` | 3 | 6 | 122 | 0 |
| `860803675` | 3 | 6 | 121 | 0 |
| `442066454` | 3 | 6 | 129 | 0 |

---

## Causa raiz por conta

| Conta | Erro | Linha | Mensagem | Hipótese |
|---|---|---:|---|---|
| Budamix Store (`448649947`) | Sem erro; atualiza no cron e no debug | — | Shopee API 200 em todas as etapas | OK |
| Budamix Oficial (`860803675`) | Não é erro Shopee; debug isolado OK, mas cron monolítico não chega a persistir esta conta | `/root/scripts/sync-inventory-cron.sh:20` + loop em `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:325` | Sem `{error,message}` da Shopee; APIs retornaram 200 no debug | **H4 — desenho operacional/script monolítico lento + janela `timeout 300` insuficiente** |
| Budamix Shop (`442066454`) | Não é erro Shopee; debug isolado OK, mas cron monolítico não chega a persistir esta conta | `/root/scripts/sync-inventory-cron.sh:20` + loop em `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:325` | Sem `{error,message}` da Shopee; APIs retornaram 200 no debug | **H4 — desenho operacional/script monolítico lento + janela `timeout 300` insuficiente** |

### Evidência principal

O cron roda todas as contas em um único processo sequencial:

```python
for account in ACCOUNTS:
    try:
        count = sync_account(account)
        total += count
```

Referência: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:325`.

Ordem das contas:

```python
ACCOUNTS = [
    {"name": "budamix-store",  "shop_id": 448649947, ...},
    {"name": "budamix-store2", "shop_id": 860803675, ...},
    {"name": "budamix-shop",   "shop_id": 442066454, ...},
]
```

Referência: `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py:27`.

Cada conta isolada levou ~190–202s. As 3 somadas dão ~584s. O wrapper atual limita o processo inteiro a 300s:

```bash
timeout 300 python3 "$SCRIPTS/sync-inventory-shopee.py"
```

Referência: `/root/scripts/sync-inventory-cron.sh:20`.

O cron das 13:45 confirmou o comportamento: após a execução, só `448649947` avançou para `2026-04-29T13:48:12Z`; as outras duas permaneceram em `18/04` e `01/04`.

### Observação sobre `exit=0`

O wrapper registra `Shopee exit=0` mesmo quando só a primeira conta chega ao banco. Isso torna o problema silencioso. A causa provável é que o processo termina “limpo” do ponto de vista do wrapper, mas o desenho sequencial + tempo efetivo impede que as contas 2 e 3 sejam persistidas dentro da janela atual. Além disso, o log atual não imprime status por conta, então o falso sucesso passa despercebido.

---

## Recomendação

### Hipótese confirmada

**Confirmada: H4 — problema operacional/script, não token expirado.**

A hipótese inicial H1 (`refresh_token` expirado) **não confirmou** no estado atual:

- 3 token files existem e são JSON válido.
- 3 token files têm `access_token` e `refresh_token`.
- 3 contas autenticaram contra Shopee.
- 3 contas retornaram `get_item_list`, `get_item_base_info` e `get_model_list` com HTTP 200.
- Nenhuma mensagem Shopee `{error, message, request_id}` indicou token expirado, permissão, 401 ou 403.

### Próximo passo recomendado para 1C

Correção mínima e segura:

1. **Versionar/snapshotar os scripts antes de alterar** (`sync-inventory-shopee.py` e `sync-inventory-cron.sh` ficam fora do repo app).
2. Alterar o cron/wrapper para rodar **uma conta por processo**, com `TARGET_SHOP`, ou aumentar timeout para algo realista.
3. Melhor opção: patchar o script original para aceitar `TARGET_SHOP` e manter compatibilidade com modo all.
4. Criar wrapper com 3 chamadas separadas:
   - `TARGET_SHOP=448649947 timeout 300 python3 sync-inventory-shopee.py`
   - `TARGET_SHOP=860803675 timeout 300 python3 sync-inventory-shopee.py`
   - `TARGET_SHOP=442066454 timeout 300 python3 sync-inventory-shopee.py`
5. Usar `python3 -u` ou `PYTHONUNBUFFERED=1` para log por conta aparecer em tempo real.
6. Logar status final por shop_id: success/error, active_items, rows_upserted, duration_seconds.
7. Só depois rodar validação SQL da Fase 1D.

Critério de aceite pós-1C:

```sql
SELECT shop_id, count(*) AS rows, count(DISTINCT sku) AS skus,
       sum(available_qty) AS units,
       max(last_synced) AS last_sync
FROM fulfillment_inventory
WHERE platform = 'shopee'
GROUP BY shop_id
ORDER BY shop_id;
-- Esperado: 3 shop_ids com last_sync < 1h.
```
