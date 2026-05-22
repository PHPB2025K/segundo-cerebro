---
title: "Budamix — SKUs compartilhados entre product_variants (anúncios espelho)"
created: 2026-05-22
type: concept
status: active
tags:
  - knowledge/architecture
  - knowledge/ecommerce
  - dominio/budamix
---

# Budamix — SKUs compartilhados entre `product_variants`

## Contexto

Catálogo Budamix tem famílias onde **cada cor do produto vira um anúncio separado** (Tampa Preta / Cinza / Vermelha = 3 produtos distintos), mas dentro de cada anúncio o seletor mostra **todas as cores** pra cross-sell. Cada uma dessas opções é uma `product_variants` row.

Exemplo concreto: Conjunto 5 Potes Redondos
- Produto "Tampa Preta" → 3 variantes (Tampa Preta, Tampa Cinza, Tampa Vermelha)
- Produto "Tampa Cinza" → 3 variantes (mesmas 3 cores)
- Produto "Tampa Vermelha" → 3 variantes (mesmas 3 cores)
- Total: 9 variantes, 3 SKUs únicos (`IMB501P_T`, `IMB501C_T`, `IMB501V_T`)

## Padrão correto

**Cada variant carrega o SKU oficial da sua cor**, mesmo que isso signifique o mesmo SKU aparecer em 3 variants distintas (uma em cada produto).

| product_variants.id | product (anúncio) | attributes.tampa | sku |
|---|---|---|---|
| 079567ea… | Tampa Preta | Preta | IMB501P_T |
| 2d290195… | Tampa Preta | Cinza | IMB501C_T |
| a1dcf19e… | Tampa Preta | Vermelha | IMB501V_T |
| b0a934c8… | Tampa Cinza | Preta | IMB501P_T |
| 3f51408d… | Tampa Cinza | Cinza | IMB501C_T |
| 4e52e29f… | Tampa Cinza | Vermelha | IMB501V_T |
| 1f2bd168… | Tampa Vermelha | Preta | IMB501P_T |
| af1f4399… | Tampa Vermelha | Cinza | IMB501C_T |
| ccefe202… | Tampa Vermelha | Vermelha | IMB501V_T |

## Por que funciona

`product_variants.sku` **não tem constraint UNIQUE** no schema do projeto `ioujfkrqvporfbvdqyus`:

```sql
SELECT con.conname, pg_get_constraintdef(con.oid)
FROM pg_constraint con
JOIN pg_class rel ON rel.oid = con.conrelid
WHERE rel.relname = 'product_variants' AND con.contype IN ('u', 'p');
-- só product_variants_pkey PRIMARY KEY (id)
```

Sem UNIQUE, posso ter o mesmo SKU em N variants — e a sincronia ainda funciona porque o sync usa PostgREST:

```python
# /opt/budamix-stock-sync/sync.py
url = f"{SUPABASE_URL}/rest/v1/product_variants?sku=eq.{urllib.parse.quote(sku)}"
# PATCH com {"stock": stock}
# PostgREST aplica em TODAS as linhas que casam, sem LIMIT
```

Resultado: 1 venda decrementa a planilha → próximo ciclo do sync atualiza as 3 variants daquele SKU simultaneamente.

## Anti-padrão (não fazer)

❌ Variants "espelho" com `sku IS NULL` e `stock=0` (estado anterior do catálogo): o seletor de cor mostra "esgotado" pra cliente que tenta escolher uma cor diferente da do anúncio principal, mata cross-sell.

❌ Variants "espelho" replicando o stock da variant principal do mesmo produto (em vez de buscar o SKU real): introduz drift entre o estoque mostrado e o estoque real do SKU, e o sync.py não consegue corrigir porque ele indexa por SKU.

❌ Adicionar UNIQUE(sku) em product_variants: quebraria o padrão.

## Custos do padrão

- Relatórios analíticos por SKU: precisam de `SELECT DISTINCT sku` ou `GROUP BY sku`, não count direto de rows.
- Edição manual de SKU pelo admin: cuidado, mudar SKU numa variant não muda nas espelho — precisa update SQL no banco ou bulk no admin.
- Decrement-side: `decrement-planilha.py` decrementa a PLANILHA (não o Supabase). A propagação vem depois via sync.py. Janela de inconsistência ≤7min (decrement 2min + sync 5min).

## Pipeline de estoque completo

```
[Cliente compra no site]
        ↓
orders.status = 'paid', orders.planilha_decremented = false
        ↓ (≤2min)
decrement-planilha.py (cron */2):
  lê order_items + product_variants.sku
  lookup aba SITE → (SKU BASE, UND POR KIT)
  decrementa aba ESTOQUE col A do SKU BASE
  marca orders.planilha_decremented = true
        ↓ (≤5min)
sync.py (cron */5):
  lê aba SITE da planilha (col D SKU ANUNCIO, col A qty em kits)
  PATCH /product_variants?sku=eq.X { stock: novo }
  → atualiza TODAS as N variants com aquele SKU
```

Latência total worst-case: ≤7min entre venda e refletir nas 3+ variants. Aceitável pro volume atual da Budamix; trigger AFTER UPDATE no banco resolve no zero, mas é nice-to-have.

## Fontes de verdade

- **Estoque físico do depósito**: Planilha de Precificação aba ESTOQUE (`1u74aCdH8VrQ2eK01YUQ8fUMwwb6ZPZXvrTTHoexWtnI`), coluna A.
- **Estoque por SKU ANUNCIO (kit)**: aba SITE da mesma planilha (fórmula que divide ESTOQUE/UND).
- **Espelho no app**: `product_variants.stock` no Supabase budamix-ecommerce, sincronizado a cada 5min.

## Caso real onde isto foi aplicado

- **22/05/2026**: reparo dos 3 anúncios Conjunto 5 Potes Redondos (IMB501). 6 variants espelho (sem SKU, stock 0) → receberam SKU + stock real. Validação: as 9 variants agora batem com a planilha. Pipeline `decrement-planilha.py` + `sync.py` propaga corretamente sem alteração.
- Ver: [[memory/context/decisoes/2026-05#[22/05 noite] Budamix E-commerce — polimentos visuais + reparo dos Conjuntos IMB501]]

## Ver também

- [[projects/budamix-ecommerce]]
- [[skills/marketplace/planilha-precificacao]] (se existir referência no vault)
- [[automacoes/workflows/stock-sync-planilha-supabase]] (se existir)
