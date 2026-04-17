---
title: "Edge Function verify_jwt = false para webhooks externos"
created: 2026-04-17
type: concept
status: active
tags:
  - knowledge
  - dev
  - supabase
---

# Edge Function `verify_jwt = false` para webhooks externos

## TL;DR

Por default, toda Edge Function do Supabase tem `verify_jwt = true` — o gateway do Supabase rejeita qualquer request sem JWT válido no `Authorization` header, **antes** da sua função rodar. Webhooks externos (Mercado Pago, Stripe, n8n, GitHub, etc.) não enviam JWT. **Se você não desabilitar `verify_jwt`, todos os webhooks são rejeitados com 401 `UNAUTHORIZED_NO_AUTH_HEADER` sem sequer executar a função.**

Sintoma: webhooks aparecem como "entregues" no dashboard do provedor externo (MP Developers mostra 401, mas é retry) e a sua função tem **zero execuções** no log do Supabase. Orders travam em `pending_payment` / similar porque a atualização assíncrona nunca chega.

## Como detectar

Listar as funções via Management API:

```bash
ACCESS_TOKEN="..." # op://OpenClaw/.../credential (Supabase Access Token CLI)
curl -s "https://api.supabase.com/v1/projects/{ref}/functions" \
  -H "Authorization: Bearer $ACCESS_TOKEN" | jq '.[] | {slug, verify_jwt}'
```

Output esperado:

```
{"slug": "create-mp-payment",  "verify_jwt": true}   ← OK (frontend envia anon key)
{"slug": "mp-webhook",         "verify_jwt": false}  ← obrigatório (MP externo)
{"slug": "get-order-by-token", "verify_jwt": true}   ← OK (frontend envia anon key)
```

## Como corrigir

Redeploy com flag:

```bash
supabase functions deploy mp-webhook --no-verify-jwt --project-ref {ref}
```

Alternativa via `config.toml` (não testei, mas documentado):

```toml
[functions.mp-webhook]
verify_jwt = false
```

## Contrapeso obrigatório — HMAC dentro da função

Desligar `verify_jwt` expõe a URL publicamente. Proteção tem que vir do código da função:

1. Exigir `MP_WEBHOOK_SECRET` como env var. Se não tiver → 500.
2. Exigir headers `x-signature` e `x-request-id`. Se ausentes → 401.
3. Computar HMAC-SHA256 do manifest `id:{data.id};request-id:{x-request-id};ts:{ts};`. Comparar com `v1` dentro de `x-signature`. Mismatch → 401.
4. Nunca confiar no body do webhook — fazer `GET /v1/payments/{id}` na API do MP usando `MP_ACCESS_TOKEN` e usar o payload do provider como source of truth.

Exemplo do padrão (mp-webhook/index.ts no projeto Budamix):

```ts
const mpWebhookSecret = Deno.env.get('MP_WEBHOOK_SECRET');
if (!mpWebhookSecret) return new Response(JSON.stringify({error:'...'}), {status:500})

const xSignature = req.headers.get('x-signature');
const xRequestId = req.headers.get('x-request-id');
if (!xSignature || !xRequestId) return new Response(..., {status:401});

const parts = xSignature.split(',').reduce(...);
const manifest = `id:${body.data?.id};request-id:${xRequestId};ts:${parts.ts};`;
const computed = await hmacSha256(mpWebhookSecret, manifest);
if (computed !== parts.v1) return new Response(..., {status:401});
```

## Teste de spoofing (smoke)

Depois do redeploy, 3 curls pra validar:

```bash
URL="https://{ref}.supabase.co/functions/v1/mp-webhook"

# Teste 1: sem headers — esperado 401 "Missing signature headers"
curl -s -w "\n%{http_code}" -X POST "$URL" \
  -H "Content-Type: application/json" \
  -d '{"type":"payment","data":{"id":"999"}}'

# Teste 2: signature malformado — esperado 401 "Malformed signature"
curl -s -w "\n%{http_code}" -X POST "$URL" \
  -H "Content-Type: application/json" \
  -H "x-signature: garbage" -H "x-request-id: fake" \
  -d '{...}'

# Teste 3: HMAC fake — esperado 401 "Invalid signature"
curl -s -w "\n%{http_code}" -X POST "$URL" \
  -H "Content-Type: application/json" \
  -H "x-signature: ts=1234,v1=aaa..." -H "x-request-id: fake" \
  -d '{...}'
```

Se retornar 200 em qualquer teste → HMAC validation está furada.

## Caso real

Descoberto em [[projects/budamix-ecommerce]] em 2026-04-17 durante o deploy #MP04:
- `mp-webhook` estava deployed desde o início com `verify_jwt=true` (default).
- Nenhum webhook real do MP chegou a processar. Orders com cartão ficavam OK (via sync response), mas PIX/boleto ficavam travados em `pending_payment`.
- Fix: `supabase functions deploy mp-webhook --no-verify-jwt` (v5 → v6).
- Depois o #MP03 tornou HMAC obrigatório no código (antes era opcional `if (secret)`).

## Outras funções que precisam do mesmo fix

Qualquer Edge Function chamada por **provider externo**:
- Mercado Pago (webhooks de pagamento)
- Stripe webhooks
- Evolution API callback
- GitHub webhooks
- n8n → Supabase integrations sem header auth

Edge Functions chamadas pelo **seu próprio frontend** podem manter `verify_jwt=true` (frontend envia anon key no header).

## Notas relacionadas

- [[projects/budamix-ecommerce]]
- [[memory/sessions/2026-04-17]]
