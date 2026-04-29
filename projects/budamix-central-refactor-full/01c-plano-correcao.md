---
title: "Budamix Central Refactor Full — 01C Plano de Correção Shopee"
created: 2026-04-29
type: plan
status: active
tags:
  - project
  - budamix-central
  - refactor
  - shopee
  - correcao
---

# Etapa 1C — Correção do Sync Shopee

## Causa raiz (referência [[projects/budamix-central-refactor-full/01a-diagnostico|01a-diagnostico]])

- Cron `15,45 * * * *` executa wrapper com `timeout 300`.
- `sync-inventory-shopee.py` itera as 3 contas em loop sequencial dentro de UM processo.
- Cada conta leva ~190–202s (3 chamadas item_list + 6 item_base_info + ~120 model_list).
- Total ≈ 585s, excede a janela de 300s.
- Apenas `448649947` (primeira do array) chega a persistir; as outras duas são mortas pelo `timeout`.
- Wrapper reporta `Shopee exit=0` mesmo no falso sucesso (`SIGTERM 124` é tratado como exit limpo).
- Logs não imprimem status por conta — falha silenciosa.

## Caminhos avaliados

| Opção | Prós | Contras | Decisão |
|-------|------|---------|---------|
| **A — Wrapper executa 3x sequencial, 1 conta por processo** | Cada conta tem seu próprio `timeout 300`. Logs naturalmente separados. Patch mínimo. Resiliente: 1 conta travada não derruba outras. | ~600s totais (mas dentro do intervalo de 30min do cron). | ✅ **Escolhida** |
| B — Aumentar timeout pra 900s | 1 linha de código | Continua falso `exit=0`, log silencioso, 1 trava derruba as 3 | ❌ |
| C — 3 processos paralelos | ~200s totais | Risco de rate limit Shopee, logs concorrentes, complexidade | ❌ (overkill por agora) |

## Mudanças necessárias

### Arquivo 1 — `/root/.openclaw/workspace/scripts/sync-inventory-shopee.py`

**Patch 1.1: aceitar variável `TARGET_SHOP` para filtrar conta**

Antes (linha ~325):
```python
for account in ACCOUNTS:
    try:
        count = sync_account(account)
        total += count
```

Depois:
```python
target_shop = os.environ.get("TARGET_SHOP", "").strip()
selected = ACCOUNTS
if target_shop:
    selected = [a for a in ACCOUNTS if str(a["shop_id"]) == target_shop]
    if not selected:
        print(f"[ERROR] TARGET_SHOP={target_shop} não corresponde a nenhuma conta", file=sys.stderr)
        sys.exit(2)

errors = 0
for account in selected:
    try:
        count = sync_account(account)
        total += count
        print(f"[OK] shop_id={account['shop_id']} name={account['name']} rows={count}")
    except Exception as e:
        errors += 1
        print(f"[ERROR] shop_id={account['shop_id']} name={account['name']} error={e}", file=sys.stderr)

# Exit refletindo sucesso real
sys.exit(1 if errors > 0 else 0)
```

**Patch 1.2: corrigir mensagem hardcoded final**

Antes (linha próxima ao fim):
```python
print(f"✅ Total: {total} SKUs synced across 3 stores")
```

Depois:
```python
print(f"Total: {total} SKUs synced across {len(selected)} store(s)")
```

(remove o ✅ falso, ajusta a contagem real)

### Arquivo 2 — `/root/scripts/sync-inventory-cron.sh`

**Patch 2.1: substituir 1 chamada Shopee por 3 chamadas isoladas**

Antes (linha 20):
```bash
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting Shopee inventory sync" >> "$LOG_DIR/inventory-shopee-$DATE.log"
timeout 300 python3 "$SCRIPTS/sync-inventory-shopee.py" >> "$LOG_DIR/inventory-shopee-$DATE.log" 2>&1
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Shopee exit=$?" >> "$LOG_DIR/inventory-shopee-$DATE.log"
```

Depois:
```bash
SHOPEE_LOG="$LOG_DIR/inventory-shopee-$DATE.log"
for SHOP_ID in 448649947 860803675 442066454; do
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Starting Shopee inventory sync shop=$SHOP_ID" >> "$SHOPEE_LOG"
  TARGET_SHOP=$SHOP_ID timeout 300 python3 -u "$SCRIPTS/sync-inventory-shopee.py" >> "$SHOPEE_LOG" 2>&1
  EXIT=$?
  echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Shopee shop=$SHOP_ID exit=$EXIT" >> "$SHOPEE_LOG"
done
```

Mudanças-chave:
- Loop bash, 1 chamada por shop_id
- Cada chamada com seu próprio `timeout 300`
- `python3 -u` (unbuffered) — log em tempo real
- Log line distingue `shop=` e `exit=`

## Sequência de execução

1. **Sync vault na VPS** (Kobe puxa o plano via cron de 15min)
2. **Snapshot tar dos 2 scripts** antes de editar (rollback bruto)
3. **Aplicar Patch 1** no `sync-inventory-shopee.py`
4. **Validar Patch 1 isolado** — rodar `TARGET_SHOP=448649947 python3 sync-inventory-shopee.py` em modo seco (sem mexer no banco precisa? não, agora pode mexer já que estamos resolvendo o problema). Mas pra extra segurança, primeiro rodar com `TARGET_SHOP=999` (inexistente) e confirmar exit=2 + mensagem clara
5. **Aplicar Patch 2** no `sync-inventory-cron.sh`
6. **Validar Patch 2 manual** — executar o wrapper em foreground:
   ```
   bash /root/scripts/sync-inventory-cron.sh
   ```
   Não esperar o cron; rodar agora pra capturar erro imediato se houver
7. **Verificar logs** — `tail -100 /var/log/budamix-sync/inventory-shopee-20260429.log` deve mostrar 3 blocos `Starting ... shop=X` + 3 blocos `exit=0`
8. **SQL de validação:**
   ```sql
   SELECT shop_id, count(*) AS rows, sum(available_qty) AS units, max(last_synced) AS last_sync
   FROM fulfillment_inventory
   WHERE platform = 'shopee'
   GROUP BY shop_id ORDER BY shop_id;
   ```
   Esperado: 3 shop_ids com `last_sync` < 5min atrás
9. **Aguardar próximo ciclo do cron natural** (`:15` ou `:45` mais próximo) e revalidar SQL — confirma que o cron real funciona, não só execução manual

## Versionamento dos scripts

`/root/.openclaw/workspace/scripts/` e `/root/scripts/` **não estão em git**. Mesma situação do app antes da Fase -1.

**Mínimo viável agora:**
- Tar dos 2 arquivos antes de editar: `/root/backups/scripts-pre-shopee-fix-20260429.tar.gz`
- Após validar funcionamento, novo tar com versão fixed: `/root/backups/scripts-post-shopee-fix-20260429.tar.gz`

**Versionamento completo (proposto, fora desta fase):**
- Criar repo `PHPB2025K/budamix-vps-scripts` privado
- `git init` em `/root/scripts/` (ou similar)
- Mover ou linkar `/root/.openclaw/workspace/scripts/`
- Mesmo padrão Fase -1 do app

Deixar para depois — não bloqueia a correção.

## Rollback

Se algo der errado em qualquer passo:
```bash
tar xzf /root/backups/scripts-pre-shopee-fix-20260429.tar.gz -C /
```
Restaura ambos os scripts ao estado anterior. Cron volta a rodar como estava.

Não há mudança no banco que precise reverter — patches só afetam scripts.

## Critério de aceite (Fase 1C → 1D)

| Validação | Como medir |
|-----------|-----------|
| Patch 1 instalado | `grep TARGET_SHOP /root/.openclaw/workspace/scripts/sync-inventory-shopee.py` retorna match |
| Patch 2 instalado | `grep "for SHOP_ID" /root/scripts/sync-inventory-cron.sh` retorna match |
| Execução manual OK | 3 blocos `exit=0` no log do dia |
| Cron natural funciona | Próximo ciclo `:15`/`:45` atualiza 3 last_synced |
| 3 contas frescas | SQL `max(last_synced)` por `shop_id` < 1h em todas as 3 |
| Sem regressão | Conta `448649947` continua atualizando como antes |
| Pedro valida 1 SKU/conta | Comparar painel Shopee × Supabase (Fase 1D) |

## Próximos passos depois da 1C

- **1D — Validação cruzada:** Pedro escolhe 1 SKU por conta, compara estoque Supabase × painel Shopee. Confirma paridade.
- **1E — Monitoramento:** healthcheck cron 6h/6h + alerta Telegram se alguma conta passar de 6h sem sync.
- **Etapa 2 — KPI CUSTO no header:** já mapeada no [[projects/budamix-central-refactor-full/00-mapeamento|00-mapeamento.md]] seção D, ataca a fórmula + match Sheets + bug UX.
