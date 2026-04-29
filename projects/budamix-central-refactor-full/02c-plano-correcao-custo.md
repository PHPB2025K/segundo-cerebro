---
title: "Budamix Central Refactor Full — 02C Plano Correção sync-costs.py"
created: 2026-04-29
type: plan
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - custo
  - correcao
---

# Etapa 2C — Correção das Colunas no `sync-costs.py`

## Causa raiz (referência [[projects/budamix-central-refactor-full/02a-diagnostico-custo|02a-diagnostico]])

Script lê colunas erradas das abas da planilha de precificação (`1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU`):

| Aba | Range atual | Lê SKU em | Lê custo em | Realidade |
|-----|-------------|-----------|-------------|-----------|
| ESTOQUE | `C9:F500` | C | F (índice 3) | F = NCM. Custo está em **D** |
| MELI | `D7:F200` | D | F (índice 2) | OK, mas tem `#ERROR!` e vazios |
| SHOPEE | `D7:F200` | D (vazio!) | F | SKU está em **B**, custo em **F** |
| AMAZON | `D7:F200` | D (vazio!) | F | SKU está em **B**, custo em **F** |

Resultado: SHOPEE e AMAZON contribuem **0 SKUs** ao `cost_map`. ESTOQUE pode estar contaminando com NCMs interpretados como custo.

## Patches

### Patch 1 — Corrigir TABS

**Antes** ([sync-costs.py:32](sync-costs.py#L32)):
```python
TABS = [
    ("ESTOQUE", "ESTOQUE!C9:F500", 0, 3),
    ("MELI",    "MELI!D7:F200",    0, 2),
    ("SHOPEE",  "SHOPEE!D7:F200",  0, 2),
    ("AMAZON",  "AMAZON!D7:F200",  0, 2),
]
```

**Depois:**
```python
TABS = [
    # (nome, range, sku_idx, cost_idx)
    # Índices são relativos ao início do range.
    ("ESTOQUE", "ESTOQUE!A9:K500", 2, 3),   # C=SKU/produto, D=custo (era F=NCM)
    ("MELI",    "MELI!A7:F200",    3, 5),   # D=SKU, F=custo
    ("SHOPEE",  "SHOPEE!A7:F200",  1, 5),   # B=SKU (era D vazio), F=custo
    ("AMAZON",  "AMAZON!A7:F200",  1, 5),   # B=SKU (era D vazio), F=custo
]
```

Nota: o range agora começa em A para todas as abas, e os índices apontam para a coluna correta dentro do array retornado pela API Sheets.

### Patch 2 — Robustez no parse de custo

A coluna de custo na planilha tem strings tipo `R$ 8,39`, `R$ 17.69`, valores vazios e `#ERROR!`. Garantir que o parse trata todos esses casos.

**Adicionar função helper** (no topo do arquivo, depois dos imports):

```python
def parse_cost(value):
    """Parse cost cell: handles R$ prefix, BR/US decimals, errors, blanks."""
    if value is None:
        return None
    s = str(value).strip()
    if not s or s.startswith("#"):  # célula vazia ou #ERROR!, #N/A, etc
        return None
    s = s.replace("R$", "").strip()
    # Aceita BR (1.234,56) e US (1234.56)
    if "," in s and "." in s:
        # 1.234,56 → 1234.56
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        v = float(s)
        return v if v > 0 else None  # custo zero não é custo válido
    except ValueError:
        return None
```

**Substituir o parse atual** (procurar onde lê `row[cost_idx]` e converte pra float):
```python
# Antes:
cost = float(row[cost_idx]) if row[cost_idx] else None

# Depois:
cost = parse_cost(row[cost_idx]) if cost_idx < len(row) else None
```

### Patch 3 — Relatório de cobertura inverso

Adicionar ao final do script, antes do exit, um relatório dos registros do inventário que ficaram sem custo após o sync. Quebra a invisibilidade do `coalesce(0)`.

**Adicionar bloco antes do print final:**
```python
# Cobertura inversa: SKUs do inventário sem custo após sync
inv_unmatched = []
for inv_row in inventory:
    sku = inv_row["sku"]
    cost = inv_row.get("cost_price")
    if not cost or cost <= 0:
        inv_unmatched.append({
            "sku": sku,
            "platform": inv_row["platform"],
            "shop_id": inv_row.get("shop_id"),
            "available_qty": inv_row.get("available_qty", 0),
            "unit_price": inv_row.get("unit_price") or 0,
        })

# Ordena por valor de venda potencial perdido
for u in inv_unmatched:
    u["potential_value"] = u["available_qty"] * u["unit_price"]
inv_unmatched.sort(key=lambda x: x["potential_value"], reverse=True)

print(f"\n[COVERAGE] {len(inventory)} registros no inventário, "
      f"{len(inventory) - len(inv_unmatched)} com custo, "
      f"{len(inv_unmatched)} sem custo.")
print(f"[COVERAGE] Valor venda potencial sem custo: "
      f"R$ {sum(u['potential_value'] for u in inv_unmatched):.2f}")
print(f"[COVERAGE] Top 20 SKUs sem custo por valor potencial:")
for u in inv_unmatched[:20]:
    print(f"  {u['sku']:25s} {u['platform']:8s} {str(u['shop_id']):12s} "
          f"qty={u['available_qty']:5d}  R$ {u['potential_value']:>10.2f}")
```

## Sequência de execução

1. **Sync vault na VPS** (puxa este plano)
2. **Snapshot tar antes** dos scripts de sync (incluindo `sync-costs.py`):
   ```bash
   tar czf /root/backups/sync-costs-pre-fix-20260429.tar.gz \
     /root/.openclaw/workspace/scripts/sync-costs.py \
     /root/scripts/sync-costs-cron.sh
   ```
3. **Aplicar Patches 1, 2, 3** no `sync-costs.py`
4. **Validar sintaxe**: `python3 -c "import ast; ast.parse(open(...).read())"`
5. **Smoke test runtime**: rodar com flag dry-run e capturar output. Verificar:
   - Sem `NameError`, `KeyError`, `IndexError`
   - Cada aba reporta `rows read` e `new SKUs with cost` > 0 (ESTOQUE, MELI, SHOPEE, AMAZON)
   - Bloco `[COVERAGE]` aparece no final com lista
6. **Comparação dry-run vs estado atual**:
   ```sql
   -- Antes da execução real
   SELECT count(*) FILTER (WHERE cost_price = 0) AS zero_cost,
          sum(available_qty * coalesce(cost_price, 0)) AS custo_atual
   FROM fulfillment_inventory;
   ```
7. **Executar de verdade** (sem dry-run): `python3 sync-costs.py`
8. **Validar SQL pós-execução**:
   ```sql
   SELECT count(*) AS total,
          count(*) FILTER (WHERE cost_price = 0) AS zero_cost,
          count(*) FILTER (WHERE cost_price > 0) AS valid_cost,
          sum(available_qty * cost_price) FILTER (WHERE cost_price > 0) AS custo_real
   FROM fulfillment_inventory;
   -- Esperado:
   --   zero_cost: 59 → significativamente menor (alvo < 30)
   --   valid_cost: 153 → > 180
   --   custo_real: R$ 124k → próximo de R$ 145-155k
   ```
9. **Snapshot tar pós-fix**:
   ```bash
   tar czf /root/backups/sync-costs-post-fix-20260429.tar.gz \
     /root/.openclaw/workspace/scripts/sync-costs.py \
     /root/scripts/sync-costs-cron.sh
   ```
10. **Validar próximo cron natural** (cron `0 9 * * *` é diário às 9h, então hoje já rodou — para validar com cron, esperar amanhã ou rodar manualmente o wrapper `/root/scripts/sync-costs-cron.sh`)

## Critério de aceite

| Validação | Como medir |
|-----------|-----------|
| Patches sintaticamente OK | `ast.parse` passa, `bash -n` passa |
| Dry-run cobre 4 abas | output mostra rows e SKUs > 0 em todas |
| Relatório [COVERAGE] presente | bloco com top 20 SKUs sem custo aparece |
| `zero_cost` cai | de 59 para < 30 |
| `custo_real` sobe | de R$ 124k para próximo de R$ 145-155k |
| Sem regressão | `valid_cost` não diminui (registros com custo válido continuam OK) |

## Rollback

Se algo der errado:
```bash
tar xzf /root/backups/sync-costs-pre-fix-20260429.tar.gz -C /
```

Restaura script. Banco fica com os custos atualizados — mas como custos do dry-run anterior estavam abaixo do correto, voltar ao banco anterior também é possível com snapshot Supabase (não previsto pra essa operação, banco está numa janela aceitável).

## Riscos identificados

- **Custos absurdos podem entrar:** se o `parse_cost` ou o range corrigido pegar uma linha mal formatada, custo pode entrar errado. Mitigação: `parse_cost` retorna `None` para qualquer string inválida; log de erro deve aparecer mas não derruba execução.
- **Múltiplas linhas com mesmo SKU em uma aba:** prioridade ESTOQUE > MELI > SHOPEE > AMAZON já existe no script. Confirmar que a lógica de "primeiro a inserir vence" continua. Não muda com o patch.
- **Planilha pode ter SKU duplicado:** se uma aba tem SKU "099" duas vezes com custos diferentes, o segundo sobrescreve o primeiro silenciosamente. Confirmar isso no dry-run (o relatório vai mostrar).

## Próximos passos depois da 2C

- **2D:** Avaliar se vale a pena adicionar `sku_mapping` como fallback (cobre +31 SKUs, mas exige tratar `quantity_multiplier`)
- **2E:** Corrigir bug UX do filtro KPI no frontend (`inventory-overview.tsx` recalcular `kpis` baseado em `filtered`)
- **2F:** Pedro valida 1-2 SKUs campeões manualmente

Decisão sobre 2D depende de: (a) se 2C já cobriu o suficiente, (b) se o `quantity_multiplier` da `sku_mapping` é confiável.
