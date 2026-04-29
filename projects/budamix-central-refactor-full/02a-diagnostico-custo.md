---
title: "Budamix Central Refactor Full — 02A Diagnóstico Custo"
created: 2026-04-29
type: reference
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - custo
  - diagnostico
---

# Budamix Central Refactor Full — 02A Diagnóstico Custo

Diagnóstico read-only do match de `cost_price` usado pelo KPI **Valor Custo** no header do módulo Full.

Escopo respeitado:
- Sem `ALTER`, `INSERT`, `UPDATE`, `DELETE`.
- Supabase lido via REST/service role apenas para `SELECT` equivalente.
- Planilha lida via `gog sheets`.
- `sync-costs.py --dry-run` executado sem alteração no banco.

> Nota de fonte: a skill `spreadsheet-pricing` documenta a planilha `PLANILHA DE ESTOQUE` (`1u74a...`), mas o KPI/cost sync real do Budamix Central usa a planilha configurada em `/root/.openclaw/workspace/scripts/sync-costs.py`: `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU`. Para diagnosticar o KPI, usei a planilha que o script realmente lê.

---

## Resumo executivo

A hipótese original estava certa no espírito, mas os números mudaram após a Etapa 1C reativar as 3 Shopees:

- `fulfillment_inventory` agora tem **212 registros**, não 195.
- **153 registros** têm `cost_price > 0`.
- **59 registros** têm `cost_price = 0`.
- Não há `cost_price NULL`.
- Valor de venda parado em registros sem custo: **R$ 67.818,72**.
- Custo atual somado no banco: **R$ 124.591,94**.
- Estimativa usando custo médio por marketplace nos zeros: **R$ 155.518,36** — diferença potencial **+R$ 30.926,42**.

Causa técnica mais grave encontrada:

1. `sync-costs.py` lê **colunas erradas** para parte da planilha atual.
2. Na aba `ESTOQUE`, ele lê `C9:F500` e trata **coluna F como custo**, mas a amostra mostra `C=produto/SKU`, `D=custo`, `E=EAN`, `F=NCM`. Isso explica custos absurdos como `70134290.00` para descrições de produtos.
3. Nas abas `SHOPEE` e `AMAZON`, o SKU real está na **coluna B**, mas o script lê `D7:F...` e usa D como SKU. Resultado: SHOPEE/AMAZON entram praticamente sem SKU útil no `cost_map` atual.
4. O script faz match **exato** (`if sku in cost_map`) — sem lower, sem normalização, sem `sku_mapping`.

Conclusão: o KPI está subestimado e/ou inconsistente porque o pipeline de custo está frágil: parte dos custos existentes não é lida, e parte dos custos lidos vem de coluna errada.

---

## 2A.1 — Diagnóstico SQL

### Q1 — Distribuição global de `cost_price`

```sql
SELECT
 count(*) AS total,
 count(*) FILTER (WHERE cost_price IS NULL) AS null_cost,
 count(*) FILTER (WHERE cost_price = 0) AS zero_cost,
 count(*) FILTER (WHERE cost_price > 0) AS valid_cost
FROM fulfillment_inventory;
```

Resultado:

| total | null_cost | zero_cost | valid_cost |
|---:|---:|---:|---:|
| 212 | 0 | 59 | 153 |

### Q2 — Por marketplace, impacto financeiro do gap

```sql
SELECT
 platform,
 count(*) AS rows,
 count(*) FILTER (WHERE cost_price IS NULL OR cost_price = 0) AS sem_custo,
 sum(available_qty) FILTER (WHERE cost_price IS NULL OR cost_price = 0) AS units_sem_custo,
 sum(available_qty * unit_price) FILTER (WHERE cost_price IS NULL OR cost_price = 0) AS valor_venda_sem_custo
FROM fulfillment_inventory
GROUP BY platform
ORDER BY platform;
```

Resultado:

| platform | rows | sem_custo | units_sem_custo | valor_venda_sem_custo |
|---|---:|---:|---:|---:|
| amazon | 69 | 15 | 529 | R$ 13.798,70 |
| ml | 30 | 5 | 183 | R$ 10.320,91 |
| shopee | 113 | 39 | 883 | R$ 43.699,11 |

### Q3 — Top 20 SKUs sem custo por valor de venda potencial

```sql
SELECT sku, platform, shop_id, available_qty, unit_price,
 available_qty * unit_price AS valor_venda_potencial
FROM fulfillment_inventory
WHERE (cost_price IS NULL OR cost_price = 0)
 AND available_qty > 0
ORDER BY valor_venda_potencial DESC
LIMIT 20;
```

Resultado:

| sku | platform | shop_id | qty | unit_price | valor_venda_potencial |
|---|---|---|---:|---:|---:|
| 098 | shopee | 442066454 | 40 | 128.47 | 5138.80 |
| DPM001 | shopee | 442066454 | 150 | 30.51 | 4576.50 |
| IMB501T-cinza | amazon | A2Q3Y263D00KWC | 145 | 29.90 | 4335.50 |
| IMB501T-vermelho | amazon | A2Q3Y263D00KWC | 163 | 25.90 | 4221.70 |
| KIT2YW800SQ_T | ml | 532562281 | 100 | 41.90 | 4190.00 |
| KIT4YW800SQ | ml | 532562281 | 50 | 79.90 | 3995.00 |
| IMB501T-preto | amazon | A2Q3Y263D00KWC | 135 | 25.90 | 3496.50 |
| KIT2YW520SQ | shopee | 448649947 | 70 | 38.69 | 2708.30 |
| KIT4YW800SQ_T | shopee | 442066454 | 30 | 71.33 | 2139.90 |
| KIT4YW800SQ_T | shopee | 448649947 | 30 | 71.32 | 2139.60 |
| CK5168_B | shopee | 442066454 | 26 | 76.90 | 1999.40 |
| CK5168_B | shopee | 860803675 | 26 | 76.90 | 1999.40 |
| CK5168_B | shopee | 448649947 | 26 | 76.90 | 1999.40 |
| CLR002 | ml | 532562281 | 30 | 64.90 | 1947.00 |
| KIT4YW800SQ_T | shopee | 860803675 | 27 | 71.33 | 1925.91 |
| DPM002 | amazon | A2Q3Y263D00KWC | 50 | 34.90 | 1745.00 |
| 098 | shopee | 860803675 | 12 | 128.47 | 1541.64 |
| DPM002 | shopee | 442066454 | 50 | 30.51 | 1525.50 |
| 096 | shopee | 442066454 | 31 | 47.86 | 1483.66 |
| KIT2YW800SQ_T | shopee | 442066454 | 30 | 41.73 | 1251.90 |

### Q4 — `sku_mapping` cobre algum caso?

SQL fornecido no briefing:

```sql
SELECT count(DISTINCT fi.sku) AS skus_inventory_com_mapping_match
FROM fulfillment_inventory fi
JOIN sku_mapping sm ON sm.child_sku = fi.sku OR sm.parent_sku = fi.sku;
```

A tabela real usa colunas `sku_child` e `sku_parent`, não `child_sku`/`parent_sku`. Query equivalente corrigida:

```sql
SELECT count(DISTINCT fi.sku) AS skus_inventory_com_mapping_match
FROM fulfillment_inventory fi
JOIN sku_mapping sm ON sm.sku_child = fi.sku OR sm.sku_parent = fi.sku;
```

Resultado:

| métrica | valor |
|---|---:|
| rows em `sku_mapping` | 68 |
| SKUs únicos do inventário com match direto em `sku_mapping` | 62 |

Impacto potencial se `sync-costs.py` usasse `sku_mapping` como fallback:

| base de custo | rows com match direto | rows adicionais via mapping | total potencial |
|---|---:|---:|---:|
| `cost_map` atual do script | 44 | 31 | 75 |
| leitura corrigida da planilha | 84 | 31 | 115 |

Exemplos reais de fallback via mapping:

| SKU inventário | plataforma | mapping encontrado | custo |
|---|---|---|---:|
| 099 | shopee | KIT3S099 | 25.33 |
| KIT4YW1520AZ | shopee | KIT4YW1520 | 44.39 |
| CTL002 | shopee | TL6250 | 19.80 |
| CTL003 | shopee | TL6250 | 19.80 |
| XCP001 | shopee | XCP004/XCP002 | 21.00 |
| 003 | amazon | KIT9S098 | 50.22 |
| 102 | amazon | KIT9S101 | 75.99 |
| 097 | amazon | KIT6S097 | 33.48 |

### Q5 — Estimativa por custo médio do marketplace

```sql
WITH avg_cost_by_platform AS (
 SELECT platform, avg(cost_price) AS avg_cost
 FROM fulfillment_inventory
 WHERE cost_price > 0
 GROUP BY platform
)
SELECT
 fi.platform,
 sum(fi.available_qty * coalesce(fi.cost_price, 0)) AS custo_atual,
 sum(fi.available_qty * coalesce(NULLIF(fi.cost_price, 0), avg.avg_cost)) AS custo_estimado_com_media
FROM fulfillment_inventory fi
JOIN avg_cost_by_platform avg ON avg.platform = fi.platform
GROUP BY fi.platform;
```

Resultado:

| platform | avg_cost usado | custo_atual | custo_estimado_com_media | delta |
|---|---:|---:|---:|---:|
| amazon | 24.2702 | R$ 23.348,17 | R$ 36.187,10 | +R$ 12.838,93 |
| ml | 16.8688 | R$ 17.695,98 | R$ 20.782,97 | +R$ 3.086,99 |
| shopee | 16.9881 | R$ 83.547,79 | R$ 98.548,29 | +R$ 15.000,50 |
| **Total** | — | **R$ 124.591,94** | **R$ 155.518,36** | **+R$ 30.926,42** |

### Q6 — Distribuição de SKU por aparições

```sql
SELECT sku, count(*) AS apparitions
FROM fulfillment_inventory
GROUP BY sku
HAVING count(*) > 1
ORDER BY apparitions DESC
LIMIT 20;
```

Resultado:

| sku | aparições |
|---|---:|
| KIT2YW520SQ | 5 |
| RED01B | 5 |
| KIT2CK4742_B | 4 |
| KIT2YW800SQ_T | 4 |
| CK4742_B | 4 |
| KIT4YW520SQ | 4 |
| DPM001 | 4 |
| 914C_B | 4 |
| PCM001 | 4 |
| DPM002 | 4 |
| IMB501C_T | 3 |
| KIT4YW1520 | 3 |
| KIT2YW1520 | 3 |
| CTL002 | 3 |
| CTL003 | 3 |
| XCP001 | 3 |
| XCP003 | 3 |
| XCP018 | 3 |
| ER2806_T | 3 |
| IMB501P_T | 3 |

---

## 2A.2 — Análise da planilha de precificação

### Fonte real usada pelo sync

`sync-costs.py` usa:

```python
SPREADSHEET_ID = "1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU"
```

Referência: `/root/.openclaw/workspace/scripts/sync-costs.py:25`.

### Leitura atual do script

O script define:

```python
TABS = [
    ("ESTOQUE", "ESTOQUE!C9:F500", 0, 3),
    ("MELI",    "MELI!D7:F200",    0, 2),
    ("SHOPEE",  "SHOPEE!D7:F200",  0, 2),
    ("AMAZON",  "AMAZON!D7:F200",  0, 2),
]
```

Referência: `/root/.openclaw/workspace/scripts/sync-costs.py:32`.

Dry-run do script atual:

```text
ESTOQUE: 121 rows read, 97 new SKUs with cost
MELI: 43 rows read, 31 new SKUs with cost
SHOPEE: 87 rows read, 0 new SKUs with cost
AMAZON: 59 rows read, 0 new SKUs with cost
Total: 128 SKUs com custo mapeado
212 registros no fulfillment_inventory
44 registros com SKU encontrado na planilha
[DRY RUN] 4 SKUs seriam atualizados
107 SKUs na planilha sem match no inventário
```

### Estrutura real observada da planilha

Amostras lidas via `gog sheets` mostram que as colunas esperadas pelo script estão desalinhadas:

#### ESTOQUE

Range `ESTOQUE!C9:F18` retornou:

```text
C = descrição/produto/SKU textual
D = custo (ex: R$ 8,39)
E = EAN
F = NCM (ex: 7013.42.90)
```

Mas o script usa índice `cost_idx=3` dentro de `C:F`, ou seja, **coluna F/NCM como custo**. Por isso aparecem custos absurdos como `70134290.00`.

#### SHOPEE

Range `SHOPEE!A7:Z15` mostrou SKU na **coluna B**:

```text
A = estoque/status
B = SKU (ex: IMB501C_T, 914C_B, KIT3S096)
F = custo (ex: R$ 7,00, R$ 17,69)
```

Mas o script lê `SHOPEE!D7:F200` e usa D como SKU; D está vazio. Resultado: **0 SKUs úteis** para SHOPEE no script atual.

#### AMAZON

Range `AMAZON!A7:V15` mostrou SKU na **coluna B**:

```text
A = estoque/status
B = SKU (ex: 001, 002, 003)
F = custo (ex: R$ 36,54, R$ 45,21)
```

Mas o script lê `AMAZON!D7:F200` e usa D como SKU; D está vazio. Resultado: **0 SKUs úteis** para AMAZON no script atual.

#### MELI

`MELI!D7:F15` está mais alinhado:

```text
D = SKU
F = custo
```

Mas há linhas com `#ERROR!` ou custo vazio, então só 31 das 43 linhas lidas entram com custo.

### Contagem de SKUs — script atual

| aba | rows lidas | SKUs não vazios conforme script | SKUs únicos | novos custos no `cost_map` |
|---|---:|---:|---:|---:|
| ESTOQUE | 121 | 121 | 121 | 97 |
| MELI | 43 | 43 | 43 | 31 |
| SHOPEE | 87 | 0 | 0 | 0 |
| AMAZON | 59 | 0 | 0 | 0 |
| **Total cost_map atual** | — | — | — | **128** |

### Contagem de SKUs — leitura corrigida pela estrutura real

Leitura corrigida usada apenas para diagnóstico:

- ESTOQUE: `A9:K500`, SKU/descrição em C, custo em D.
- MELI: `A7:AA200`, SKU em D, custo em F.
- SHOPEE: `A7:Z200`, SKU em B, custo em F.
- AMAZON: `A7:V200`, SKU em B, custo em F.

| aba | rows lidas | SKU não vazio | SKUs únicos | rows com custo | novos custos no mapa por prioridade |
|---|---:|---:|---:|---:|---:|
| ESTOQUE | 121 | 121 | 121 | 121 | 121 |
| MELI | 115 | 43 | 43 | 31 | 31 |
| SHOPEE | 87 | 87 | 86 | 40 | 19 |
| AMAZON | 114 | 59 | 59 | 56 | 33 |
| **Total corrigido** | — | — | — | — | **204 SKUs com custo** |

### Comparação inventário × planilha

#### Com `cost_map` atual do script

| métrica | valor |
|---|---:|
| SKUs únicos no inventário | 119 |
| SKUs únicos no cost_map atual | 128 |
| Match exato por SKU único | 21 |
| Match exato por registro | 44 de 212 |
| Case-insensitive/pontuação | 0 |
| Match por prefix strip simples | 2 |
| Sem match único | 96 |

Amostras de match exato atual:

```text
DPM001, EMB01T, K6CAN250, KIT2YW1050, KIT2YW1520, KIT2YW320, KIT2YW640, KIT3S096, KIT3S099, KIT4YW1050
```

Amostras de match parcial por prefixo simples:

```text
KIT2YW520SQ → KIT4YW520SQ
KIT4YW800SQ → KIT2YW800SQ
```

Amostras sem match atual:

```text
001, 002, 003, 004, 006, 0063_, 008, 012, 022, 023,
024, 025, 027, 028, 096, 097, 098, 099, 102, 107,
108, 1888M, CK4742_B, CK5168_B, DPM002, IMB501T-cinza
```

#### Com leitura corrigida da planilha

| métrica | valor |
|---|---:|
| SKUs únicos no inventário | 119 |
| SKUs únicos com custo na leitura corrigida | 204 |
| Match exato por SKU único | 47 |
| Match exato por registro | 84 de 212 |
| Registros zerados que passariam a ter custo por match exato | 8 de 59 |
| Sem match único após leitura corrigida | 72 |

Registros hoje zerados que seriam corrigidos só ajustando as colunas de leitura:

| sku | platform | shop_id | custo planilha |
|---|---|---|---:|
| DPM001 | shopee | 442066454 | 2.39 |
| KIT4YW520SQ | shopee | 442066454 | 16.35 |
| KIT2YW520SQ | shopee | 442066454 | 11.23 |
| PCM001 | shopee | 442066454 | 1.04 |
| KIT4YW800SQ | ml | 532562281 | 27.11 |
| KIT2YW520SQ | shopee | 448649947 | 11.23 |
| KIT2YW520SQ | shopee | 860803675 | 11.23 |
| KIT4YW520SQ | shopee | 860803675 | 16.35 |

Custo adicional exato só nesses zeros mapeáveis:

| mapa | custo adicional em rows zeradas |
|---|---:|
| `cost_map` atual | R$ 477,40 |
| leitura corrigida | R$ 3.292,80 |

---

## 2A.3 — `sync-costs.py`: comportamento detalhado

Arquivo lido: `/root/.openclaw/workspace/scripts/sync-costs.py`.

### Função de comparação SKU

Match é **exato**:

```python
sku = str(row[sku_idx]).strip()
...
if sku in cost_map:
    new_cost = cost_map[sku]
```

Referências:

- `sku.strip()`: `/root/.openclaw/workspace/scripts/sync-costs.py:82`
- match exato: `/root/.openclaw/workspace/scripts/sync-costs.py:117`

Não faz:

- `.lower()`
- normalização de pontuação
- remoção de sufixo/cor
- fallback por `sku_mapping`
- comparação por `sku_parent`/`sku_child`

### Como trata SKU na planilha mas não no inventário

Ele apenas reporta no final como unmatched:

```python
inv_skus = set(r["sku"] for r in inventory)
unmatched = [sku for sku in cost_map if sku not in inv_skus]
```

Referências: `/root/.openclaw/workspace/scripts/sync-costs.py:183`.

Dry-run atual reportou:

```text
107 SKUs na planilha sem match no inventário
```

Mas esse número está poluído porque ESTOQUE está lendo NCM como custo e descrições de produto como SKU.

### Como trata SKU no inventário mas não na planilha

Não faz nada e não reporta diretamente. O registro fica com `cost_price` atual — se for `0`, continua contribuindo R$ 0 no KPI.

Trecho:

```python
if sku in cost_map:
    ... append update
```

Se não está no `cost_map`, simplesmente pula.

### Qual coluna lê para `cost_price`

Segundo o código atual:

| aba | range | sku_idx | cost_idx | interpretação real observada |
|---|---|---:|---:|---|
| ESTOQUE | `ESTOQUE!C9:F500` | 0 → C | 3 → F | F é NCM, não custo |
| MELI | `MELI!D7:F200` | 0 → D | 2 → F | correto para SKU/custo, mas há `#ERROR`/vazios |
| SHOPEE | `SHOPEE!D7:F200` | 0 → D | 2 → F | D vazio; SKU real está em B |
| AMAZON | `AMAZON!D7:F200` | 0 → D | 2 → F | D vazio; SKU real está em B |

### Dry-run manual

Comando executado:

```bash
python3 /root/.openclaw/workspace/scripts/sync-costs.py --dry-run
```

Resultado relevante:

```text
Total: 128 SKUs com custo mapeado
212 registros no fulfillment_inventory
44 registros com SKU encontrado na planilha
[DRY RUN] 4 SKUs seriam atualizados:
  DPM001 (shopee/442066454): → R$ 2.39
  KIT4YW520SQ (shopee/442066454): → R$ 16.35
  PCM001 (shopee/442066454): → R$ 1.04
  KIT4YW520SQ (shopee/860803675): → R$ 16.35
107 SKUs na planilha sem match no inventário
```

Dry-run não altera o banco; ele só lista updates potenciais.

---

## Recomendação para 2C

Prioridade das correções:

1. **Corrigir as colunas em `sync-costs.py` antes de mexer no KPI.**
   - ESTOQUE: custo deveria vir de D, não F.
   - SHOPEE: SKU deveria vir de B, custo de F.
   - AMAZON: SKU deveria vir de B, custo de F.
   - MELI pode permanecer D/F, mas precisa tratar `#ERROR`/vazios explicitamente.

2. **Adicionar relatório de cobertura inverso no `sync-costs.py`:**
   - SKUs do inventário sem custo e sem match na planilha.
   - Top por `available_qty * unit_price`.
   - Isso evita o erro silencioso do KPI.

3. **Só depois avaliar `sku_mapping` como fallback.**
   - Ele cobre 31 registros adicionais, mas pode ser perigoso se parent/child tiverem multiplicador ou custo diferente.
   - Como a própria tabela tem `quantity_multiplier`, fallback precisa respeitar multiplicador quando existir.

4. **KPI front-end continua problema separado.**
   - Mesmo com custo corrigido, o KPI ainda não respeita filtro visual da Visão Geral.
   - Isso fica para 2B/2C UX.

Critério de aceite para uma futura 2D:

```sql
SELECT
 count(*) AS total,
 count(*) FILTER (WHERE cost_price IS NULL) AS null_cost,
 count(*) FILTER (WHERE cost_price = 0) AS zero_cost,
 count(*) FILTER (WHERE cost_price > 0) AS valid_cost
FROM fulfillment_inventory;
-- Esperado após fix mínimo: zero_cost cair de 59 para pelo menos 51 ou menos.
-- Esperado após fix + sku_mapping consciente: queda maior, alvo preliminar < 20.
```
