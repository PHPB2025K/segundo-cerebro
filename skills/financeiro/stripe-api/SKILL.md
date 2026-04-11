---
name: stripe-api
description: Interface completa com a API REST do Stripe via curl. Cobranças (PaymentIntents), clientes, produtos/preços, assinaturas, faturas, relatórios financeiros (saldo, balance transactions, payouts, refunds, disputes) e webhooks. Use quando Pedro pedir qualquer operação Stripe — pagamentos, clientes, assinaturas, faturas, saldo, reembolsos, disputas ou relatórios financeiros. Também usar para análise financeira de receita SaaS.
---

# Stripe API — Operador Completo

> Usado por [[agents/fisco/IDENTITY|Fisco]]

Interface direta com a API REST do Stripe via curl. Cobre 100% das operações do dia a dia: cobranças, clientes, produtos, assinaturas, faturas, saldo, reembolsos, disputas e webhooks.

## Autenticação

```bash
# Variável obrigatória — NUNCA exibir o valor
export STRIPE_SECRET_KEY="sk_live_..."
```

Toda chamada: `curl -u "$STRIPE_SECRET_KEY:" ...`
Base URL: `https://api.stripe.com/v1/`
Content-Type: `application/x-www-form-urlencoded` (parâmetros via `-d`, NÃO JSON)
Idempotência: TODA operação POST inclui `-H "Idempotency-Key: $(uuidgen)"`

### Check antes de qualquer operação
```bash
[ -z "$STRIPE_SECRET_KEY" ] && echo "ERRO: STRIPE_SECRET_KEY não configurada" && exit 1
```

## Contexto Brasil
- Moeda padrão: **BRL** — sempre `currency=brl`
- Valores em **centavos**: R$ 49,90 = `4990`
- Valor mínimo: R$ 0,50 (`50`)
- Métodos: `card`, `pix`, `boleto`
- Pix: pagamento real-time, `expires_after_seconds`
- Boleto: requer `tax_id` (CPF/CNPJ), `expires_after_days`, não reembolsável nativamente

## Rate Limits
| Contexto | Limite |
|---|---|
| Produção | 100 req/s |
| PaymentIntents update | 1.000/hora por PI |
| Search API | 20 reads/s |
| Create Payout | 15 req/s, 30 concorrentes |
| Subscriptions | 10 novas invoices/min por sub |

HTTP 429 → exponential backoff com jitter. Verificar `Stripe-Should-Retry`.

## Módulos

Detalhes completos de cada módulo: ver `references/`

| # | Módulo | Referência |
|---|---|---|
| 1 | Cobranças (PaymentIntents + PaymentMethods) | `references/m01-pagamentos.md` |
| 2 | Clientes (Customers) | `references/m02-clientes.md` |
| 3 | Produtos e Preços (Products + Prices) | `references/m03-produtos-precos.md` |
| 4 | Assinaturas (Subscriptions) | `references/m04-assinaturas.md` |
| 5 | Faturas (Invoices) | `references/m05-faturas.md` |
| 6 | Relatórios Financeiros (Balance, Payouts, Refunds, Disputes) | `references/m06-financeiro.md` |
| 7 | Webhooks | `references/m07-webhooks.md` |
| 8 | Paginação e Expand | `references/m08-paginacao.md` |
| 9 | Tratamento de Erros | `references/m09-erros.md` |

## Inputs Necessários

| Input | Obrigatório | Descrição |
|---|---|---|
| `STRIPE_SECRET_KEY` | Sim | Chave secreta (env var, nunca hardcoded) |
| Operação | Sim | O que fazer (criar cliente, cobrar, listar, etc) |
| Parâmetros | Depende | IDs, valores, dados específicos da operação |

## Confirmações Obrigatórias (SEMPRE perguntar antes)

- ❌ Deletar cliente (cancela TODAS as assinaturas)
- ❌ Cancelar assinatura imediatamente
- ❌ Aceitar/fechar disputa (irreversível)
- ❌ Criar payout manual em produção
- ❌ Reembolso com `reason=fraudulent` (adiciona a blocklists)
- ❌ Qualquer operação > R$ 1.000,00

## Operações Seguras (executar direto)

- ✅ Qualquer GET (consultas, listagens)
- ✅ Criar cliente
- ✅ Atualizar metadata
- ✅ Preview de fatura
- ✅ Recuperar saldo

## Critérios de Qualidade

- Toda operação POST usa Idempotency-Key
- Valores sempre em centavos BRL
- Erros parseados e apresentados de forma clara (tipo + código + mensagem)
- Nunca exibir API key em logs ou outputs
- Operações destrutivas sempre com confirmação
- Respostas formatadas: status, ID do recurso, dados relevantes

## Aprendizados Incorporados

<!-- MELHORIA 2026-03-16 -->
### Chaves de teste vs produção
- sk_test_: funciona pra testar integração, não processa pagamentos reais
- sk_live_: produção — gerar quando SaaS estiverem prontos
- rk_test_: restricted key — acesso limitado, não é a secret key completa
- Sempre verificar prefixo antes de operar
<!-- /MELHORIA -->
