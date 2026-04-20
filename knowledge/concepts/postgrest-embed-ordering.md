---
title: "PostgREST — embed ordering"
created: 2026-04-19
type: knowledge
status: active
tags:
  - knowledge
  - supabase
  - postgrest
  - backend
---

# PostgREST — embed sem `.order()` não garante ordem

## Contexto

Supabase-js (via PostgREST) permite embedded selects pra trazer relações numa única chamada:

```ts
supabase
  .from('products')
  .select('id, name, images:product_images(image_url, alt_text)')
```

**Armadilha:** a ordem das linhas dentro do embed (`images`) **não é garantida**. PostgREST devolve na ordem que o plano físico do PostgreSQL entregar — geralmente ordem de inserção ou CTID/PK UUID, mas nada obriga.

Consequência: `data[0].images[0]` pode ser qualquer row do embed. Se o código assume "primeira é a principal" sem explicitar, qualquer mudança de dados (UPDATE, REINDEX, VACUUM) pode alterar a ordem silenciosamente.

## Como ordenar

Duas formas — ambas válidas, escolha depende do embed ser raso ou profundo.

### A) Ordenar no servidor via `foreignTable` (preferido em embeds rasos)

```ts
supabase
  .from('products')
  .select('id, name, images:product_images(image_url, alt_text)')
  .order('sort_order', { foreignTable: 'product_images', ascending: true })
```

Vantagens: single source of truth, menos payload, não depende do consumidor.

Limitação: para embeds **aninhados profundos** (ex: `cart_items → variant → product → images`), o path de `foreignTable` fica frágil — a sintaxe exata varia entre versões do Supabase-js e do PostgREST, e debug é chato.

### B) Incluir coluna de ordenação no select + ordenar client-side

```ts
supabase
  .from('products')
  .select('id, name, images:product_images(image_url, alt_text, sort_order)')
// depois:
products.forEach(p => {
  p.images.sort((a, b) => (a.sort_order ?? 0) - (b.sort_order ?? 0))
})
```

Vantagens: explícito, robusto, funciona em qualquer nível de embed aninhado.

Desvantagens: trafega um campo a mais; duplica a regra em cada consumidor.

## Quando cada um faz sentido

- Embed **raso** (1 nível): prefira **A** — uma linha na query resolve.
- Embed **aninhado profundo** (2+ níveis): prefira **B** — garantido, sem dependência de sintaxe PostgREST.
- Queries que compartilham hook (ex: `useCart` no Budamix): **B** é mais seguro porque o hook é consumido por múltiplos componentes, não dá pra confiar que cada consumidor ordene.

## Como detectar se o bug existe num codebase

Grep por embeds que não pedem o campo de ordenação:

```bash
grep -rn "product_images\s*(" src/ | grep -v "sort_order"
```

Se houver match e o consumidor faz `images[0]`, tem bug latente. Validar com query REST direta pedindo a row específica do banco e confirmando que a "capa esperada" está em `sort_order=0`.

## Caso Budamix (19/04/2026)

- 19 capas regeneradas via Nano Banana, UPDATE em `product_images.image_url` na row `sort_order=0`
- Capas novas só apareciam em `/loja` (que ordenava) — resto do site exibia URLs antigas
- Investigação em [[memory/context/decisoes/2026-04|decisões 19/04]] + fix commit `4ad4937`

## Ver também

- [[projects/budamix-ecommerce]] — projeto onde a regra nasceu
- [[memory/context/decisoes/2026-04|Decisões Abril 2026]] — entrada 19/04 com detalhes do fix
- [Supabase docs — Ordering embedded resources](https://supabase.com/docs/reference/javascript/order) (verificar sintaxe exata de foreignTable antes de usar em aninhados)
