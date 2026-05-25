---
title: "ChunkErrorBoundary — fix obrigatório em SPA com lazy() + deploy contínuo"
created: 2026-05-25
type: concept
status: active
tags:
  - knowledge
  - frontend
  - react
  - vercel
  - pattern
---

# ChunkErrorBoundary — fix obrigatório em SPA com lazy() + deploy contínuo

## Sintoma

Usuário clica em um link da SPA → tela fica em branco (sem erro visível, sem redirect). Mais comum em desktop com sessão aberta há horas, depois de o time fazer deploy. Refresh manual (F5) resolve.

## Causa raiz

Apps React com `React.lazy()` carregam chunks JS sob demanda (`Shop.[hash].js`). Cada deploy do Vercel/Netlify gera novos hashes e remove os antigos. Se o usuário tem o app aberto desde antes do deploy:

1. Browser tem `Shop.[hash-v1].js` no cache do bundle inicial
2. Deploy publica `Shop.[hash-v2].js`, deleta v1 do CDN
3. Usuário clica em LOJA → React tenta `import('./Shop.[hash-v1].js')` → 404
4. `lazy()` rejeita silenciosamente → Suspense não tem fallback de erro → **tela branca**

## Solução

`ErrorBoundary` envolvendo o `<Suspense>` que:

1. Detecta `ChunkLoadError` (várias mensagens conhecidas — ver implementação)
2. Faz `window.location.reload()` automático pra pegar `index.html` novo com hashes atualizados
3. Limita reload a 1× por sessão via `sessionStorage` flag pra não entrar em loop em caso de falha real de rede

## Implementação de referência

`budamix-ecommerce/src/components/ChunkErrorBoundary.tsx` (commit `77c7d50` em 25/05/2026).

Detecta:
- `Loading chunk \d+ failed`
- `Failed to fetch dynamically imported module`
- `Importing a module script failed`
- `ChunkLoadError`
- `error.name === 'ChunkLoadError'`

Estrutura:
```tsx
<BrowserRouter>
  <ScrollToTop />
  <ChunkErrorBoundary>
    <Suspense fallback={<Loading />}>
      <Routes>...</Routes>
    </Suspense>
  </ChunkErrorBoundary>
</BrowserRouter>
```

## Quando aplicar

**Obrigatório em qualquer SPA do Pedro com `React.lazy()` + deploy automático:**
- ✅ budamix-ecommerce (implementado 25/05)
- ⚠️ estoque.budamix.com.br — verificar se tem lazy()
- ⚠️ central.budamix.com.br (Budamix Central) — verificar
- ⚠️ qualquer projeto Lovable/Next.js futuro com code splitting

## Por que não confiar só em "Hard refresh"

Pedir pra usuário dar Cmd+Shift+R é UX ruim — Pedro mesmo reportou o bug achando que era do código. ErrorBoundary com reload automático é invisível pro usuário final.

## Ver também

- [[memory/context/decisoes/2026-05|Decisão 25/05 ChunkErrorBoundary]]
- [[projects/budamix-ecommerce]]
