---
title: "React Rules of Hooks — early return pitfall"
created: 2026-04-17
type: concept
status: active
tags:
  - knowledge
  - dev
  - react
---

# React Rules of Hooks — early return pitfall

Um dos bugs mais sutis em React: **declarar hooks depois de `return` condicionais** viola as Rules of Hooks e crasha o componente na transição entre estados.

## O sintoma

- Componente renderiza tela branca quando algum estado assíncrono (query, fetch) muda.
- Console pode mostrar: `Warning: React has detected a change in the order of Hooks called by [Componente]` ou erro fatal sem mensagem clara no dev overlay.
- Em produção (build minificado) só a tela branca aparece, sem mensagem útil.

## Por que acontece

React trackeia hooks **por ordem de chamada**, não por nome. Se no render 1 você chama `useQuery`, no render 2 você chama `useQuery + useEffect + useEffect + useEffect`, o React não sabe se o 2º hook no render 2 é "novo" ou se é o useQuery "renomeado" — isso viola a garantia de que a lista de hooks é estável.

## Anti-pattern

```tsx
export default function ProductDetail() {
  const { data: product, isLoading } = useQuery(...);  // 1 hook

  if (isLoading) return <Skeleton />;   // early return
  if (!product) return <NotFound />;    // early return

  useEffect(() => { document.title = product.name }, [product]);  // 2º hook (nunca chamado no 1º render)
  useEffect(() => { trackEvent('view', {...}) }, [product.id]);   // 3º hook
  useEffect(() => { /* JSON-LD */ }, [product]);                  // 4º hook

  return <MainContent />;
}
```

Fluxo:
- **Render 1** (`isLoading=true`): chama 1 hook, retorna Skeleton. React registra: `[useQuery]`.
- **Render 2** (`product` loaded): chama 4 hooks. React compara: esperava 1 hook, recebeu 4 → crash.

## Fix correto

Todos os hooks **antes** de qualquer `return` condicional. Guards vão dentro do callback:

```tsx
export default function ProductDetail() {
  const { data: product, isLoading } = useQuery(...);

  useEffect(() => {
    if (!product) return;                        // guard DENTRO
    document.title = `${product.name} | Budamix`;
  }, [product]);

  useEffect(() => {
    if (!product) return;
    trackEvent('view_item', { ... });
  }, [product?.id]);

  useEffect(() => {
    if (!product) return;                        // usar optional chaining para vars derivadas
    const img = product.images?.[0]?.image_url || '';
    // ...
  }, [product]);

  if (isLoading) return <Skeleton />;           // returns POR ÚLTIMO
  if (!product) return <NotFound />;

  return <MainContent product={product} />;
}
```

## Regra prática

1. **Hooks primeiro** — todos os `useState`, `useRef`, `useQuery`, `useEffect`, `useMemo`, `useCallback` no topo da função.
2. **Derivações depois** — variáveis computadas (`const active = items.filter(...)`) usando optional chaining se dependem de estado assíncrono.
3. **Early returns por último** — `if (isLoading)`, `if (!data)`, `if (error)` vão logo antes do JSX principal.
4. **Guards dentro de callbacks** — `useEffect(() => { if (!product) return; ... })` em vez de `if (product) useEffect(...)`.
5. **Para computações que dependem de optional**: calcular dentro do próprio `useEffect` com `product?.x ?? fallback`, ou declarar antes dos returns usando `??` em toda cadeia.

## ESLint / lint rule

O plugin `eslint-plugin-react-hooks` com regra `react-hooks/rules-of-hooks` pega o caso clássico (hook depois de `if`), mas **não pega** hooks depois de `return` em outra coluna/bloco visualmente separado. Sempre vale review manual.

## Caso real

Descoberto em [[projects/budamix-ecommerce]] em 2026-04-17: `src/pages/ProductDetail.tsx` tinha os 3 `useEffect` (document.title, analytics view_item, JSON-LD) após `if (isLoading) return` e `if (!product) return`. PDP ficava em branco ao navegar de `/` para `/produto/{slug}`. Fix no commit `62aa9e1`.

## Notas relacionadas

- [[projects/budamix-ecommerce]]
- [[memory/sessions/2026-04-17]]
