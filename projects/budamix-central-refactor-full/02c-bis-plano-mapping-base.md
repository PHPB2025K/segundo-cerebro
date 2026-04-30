---
title: "Budamix Central Refactor Full — 02C bis Plano Mapping Base"
created: 2026-04-30
type: plan
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - custo
  - mapping
  - correcao
---

# Etapa 2C bis — Reescrever sync-costs.py com lógica anuncio→base→custo

## Causa raiz nova (descoberta em 30/04 manhã)

A planilha de precificação `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU` tem estrutura **2 níveis**:

```
ESTOQUE  : 1 SKU_BASE → 1 CUSTO (fonte de verdade)
   ↑ lookup
MARKETPLACES: SKU_BASE (col B) ↔ SKU_ANUNCIO (col D)
              (mapeamento — NÃO tem custo aqui, vem por fórmula de ESTOQUE)
```

**Estrutura confirmada:**

| Aba | A | B | C | D | E | F | G | H |
|-----|---|---|---|---|---|---|---|---|
| ESTOQUE | qty | **SKU BASE** | descrição | **CUSTO** | EAN | NCM | empresa | total |
| MELI | qty | SKU BASE | MLB | **SKU ANUNCIO** | produto | preço custo (vazio) | preço venda | anúncio |
| SHOPEE | qty | SKU BASE | ID anúncio | **SKU ANUNCIO** | produto | preço custo (vazio) | preço venda | comissão |
| AMAZON | qty | SKU BASE | ASIN | **SKU ANUNCIO** | produto | preço custo (vazio) | preço venda | comissão |

**Estado atual da planilha:**
- ESTOQUE: 121 SKUs base com custo ✅
- MELI: 47 mappings ✅
- SHOPEE: 1 mapping ❌
- AMAZON: 1 mapping ❌

## Lógica nova do sync-costs.py

```
1. Carregar cost_map de ESTOQUE: {SKU_BASE → CUSTO}
2. Carregar mappings de cada aba marketplace: {SKU_ANUNCIO → SKU_BASE}
3. Pra cada registro do fulfillment_inventory:
   a. Tenta cost_map[sku] direto (caso seja SKU base)
   b. Senão: mapping[sku] → cost_map[base]
   c. Senão: pula (continua zerado)
4. Aplica updates no Supabase
```

## Patches no script

Reescrita completa de `/root/.openclaw/workspace/scripts/sync-costs.py`. Mantém:
- Parse de custo robusto (`parse_cost`)
- Suporte a `--dry-run`
- Relatório `[COVERAGE]` no final
- Service role key como env var ou fallback hardcoded

Muda:
- `TABS` → `ESTOQUE_RANGE` + `MARKETPLACE_TABS`
- `build_cost_map()` → `load_cost_map_from_estoque()` + `load_mapping_from_marketplace()`
- `build_updates_preview()` → usa `resolve_cost(sku, platform, ...)`
- Adiciona log "resolved direct vs via mapping" no relatório

## Sequência de execução

1. **Snapshot tar antes** (`/root/backups/sync-costs-pre-mapping-fix-20260430.tar.gz`)
2. **Substituir arquivo inteiro** via `tee` ou `cat > file.py <<EOF` (não edição cirúrgica — risco de escape com `\n` em strings)
3. **ast.parse** (sintaxe)
4. **Smoke test runtime — TARGET inválido** (parse_cost de ESTOQUE)
5. **Dry-run** — relatório esperado:
   - ESTOQUE: 121 SKUs base com custo
   - MELI: 47 mappings, X com base válido em ESTOQUE
   - SHOPEE: 1 mapping
   - AMAZON: 1 mapping
   - Total resolved (direct + via mapping): ~95-100 dos ~150 SKUs com cost no inventário
   - Updates pendentes: 0 (porque MELI já tem 47 mappings, mas custo já estava aplicado da execução anterior; só haverá update se algum mapping novo descobrir SKU diferente)
6. **Execução real** — `python3 sync-costs.py`
7. **SQL pós:**
   ```sql
   SELECT count(*) FILTER (WHERE cost_price = 0) AS zero_cost,
          count(*) FILTER (WHERE cost_price > 0) AS valid_cost,
          sum(available_qty * coalesce(cost_price, 0)) AS custo_real
   FROM fulfillment_inventory;
   ```
   Esperado: zero_cost ≤ 50 (vai cair pouco — SHOPEE/AMAZON ainda vazios), valid_cost ≥ 153, custo_real ≥ R$ 130k. Ganho real virá quando analistas preencherem SKU BASE em SHOPEE/AMAZON.

## Critério de aceite

| Validação | Como medir |
|-----------|-----------|
| Sintaxe OK | `ast.parse` passa |
| Dry-run reporta 4 carregamentos (ESTOQUE + 3 marketplaces) | Output mostra contagem de SKUs por aba |
| Sem regressão | zero_cost não sobe; custo_real não cai |
| Pelo menos 1 SKU resolvido via mapping | Logs mostram "resolved via base X" |
| Cron diário 9h amanhã preserva | Próxima execução natural sem regressão |

## Rollback

```bash
tar xzf /root/backups/sync-costs-pre-mapping-fix-20260430.tar.gz -C /
```

## Próximo passo após 2C bis

Mensagem revisada pros analistas (Etapa B): **preencher coluna B (SKU BASE)** nas suas abas para os SKU ANUNCIO listados. Não precisam cadastrar custo — só vincular ao SKU base de ESTOQUE.

Esperado pós-cadastro analistas: zero_cost cai pra ~10-15 (apenas fantasmas reais sem produto Budamix), custo_real sobe pra R$ 145-155k.
