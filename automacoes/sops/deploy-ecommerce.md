---
title: "SOP — Deploy E-commerce Budamix"
type: sop
created: 2026-04-15
updated: 2026-04-15
status: active
tags:
  - sop
  - deploy
  - ecommerce
  - vercel
---

# SOP — Deploy E-commerce Budamix

> Como fazer deploy do budamix.com.br (React + Vite + Supabase + Mercado Pago)

---

## Dados do Projeto

| Campo | Valor |
|-------|-------|
| Path local | `~/Documents/05-Projetos-Codigo/budamix-ecommerce/` |
| Repo | `PHPB2025K/budamix-ecommerce` |
| Branch | main |
| Deploy | Vercel (prj_wMl99f4aixldKCwBiJv9xDedL7AR) |
| Domínio | https://budamix.com.br (A record: 76.76.21.21) |
| Supabase | `ioujfkrqvporfbvdqyus` (sa-east-1) |

---

## Passo a Passo

### 1. Navegar até o projeto

```bash
cd ~/Documents/05-Projetos-Codigo/budamix-ecommerce
```

### 2. Verificar env vars

Arquivo `.env` na raiz (NÃO committar):

```
VITE_SUPABASE_URL="https://ioujfkrqvporfbvdqyus.supabase.co"
VITE_SUPABASE_PUBLISHABLE_KEY=<Supabase - Budamix Ecommerce - Anon Key>
VITE_SUPABASE_PROJECT_ID="ioujfkrqvporfbvdqyus"
VITE_MERCADOPAGO_PUBLIC_KEY=<Mercado Pago - Budamix Ecommerce - Public Key>
```

Credenciais no 1Password vault OpenClaw → [[knowledge/concepts/credenciais-map]]

Env vars no Vercel Dashboard também devem estar sincronizadas.

### 3. Build local (verificação)

```bash
npm run build
```

Output: `dist/`. Se falhar, corrigir antes de prosseguir.

### 4. Deploy para Vercel

```bash
vercel --prod
```

Ou via push para `main` (auto-deploy configurado).

### 5. Verificar deploy

- Acessar https://budamix.com.br
- Testar navegação (home → produtos → produto → checkout)
- Verificar console do browser para erros

### 6. Testar checkout (se houve mudanças no pagamento)

- Adicionar produto ao carrinho
- Ir até checkout
- Verificar Payment Brick (Pix + Cartão + Débito)
- Em sandbox: usar cartão de teste MP

---

## Edge Functions (Supabase)

| Function | Rota | O que faz |
|----------|------|-----------|
| `create-mp-payment` | POST | Cria order no Supabase + chama MP /v1/payments |
| `mp-webhook` | POST | Recebe IPN do Mercado Pago (HMAC-SHA256) |
| `get-order-by-token` | GET | Busca order por ID + email |

Deploy de Edge Functions:

```bash
supabase functions deploy create-mp-payment --project-ref ioujfkrqvporfbvdqyus
supabase functions deploy mp-webhook --project-ref ioujfkrqvporfbvdqyus --no-verify-jwt
```

---

## DNS (se precisar reconfigurar)

- Registro.br ou Cloudflare
- A record: `budamix.com.br` → `76.76.21.21`
- A record: `www.budamix.com.br` → `76.76.21.21`

---

## SPA Routing

Arquivo `vercel.json` na raiz:

```json
{ "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }] }
```

---

## Pendente

- ⚠️ Configurar webhook MP manualmente no painel Developers: `https://ioujfkrqvporfbvdqyus.supabase.co/functions/v1/mp-webhook`
- ⚠️ Testar pagamento Pix real (valor baixo) para validar QR code + webhook + order

---

## Notas Relacionadas

- [[projects/budamix-ecommerce]] — ficha do projeto
- [[knowledge/concepts/credenciais-map]] — credenciais
- [[knowledge/concepts/stack-tecnico]] — stack
