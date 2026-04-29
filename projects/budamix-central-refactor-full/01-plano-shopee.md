---
title: "Budamix Central Refactor Full — 01 Plano Shopee"
created: 2026-04-29
type: plan
status: active
tags:
  - project
  - budamix-central
  - refactor
  - full
  - shopee
  - plano
---

# Etapa 1 — Auditoria e Reativação das 3 Contas Shopee

## Contexto

Mapeamento ([[projects/budamix-central-refactor-full/00-mapeamento|00-mapeamento.md]]) revelou que o cron de inventário Shopee (`15,45 * * * *`) está rodando, mas só 1 das 3 contas tem dados recentes:

| Conta | shop_id | Última sync | Idade |
|-------|---------|------------|-------|
| Budamix Store | `448649947` | 29/04 13:18 | ✅ hoje |
| Budamix Oficial | `860803675` | 18/04 22:18 | 🚨 11 dias |
| Budamix Shop | `442066454` | 01/04 15:26 | 🚨 28 dias |

Falha silenciosa: cron executa, exit=0 reportado, mas duas contas não atualizam.

## Objetivo

1. Identificar causa raiz por conta (token? bug? bloqueio?)
2. Reativar sync das 3 contas
3. Validar paridade dos dados pós-fix
4. Adicionar monitoramento defensivo (alerta quando alguma conta passar de X horas sem sync)

Sem mexer em código de aplicação ainda. Refactor de UX (filtro recalcula KPI) fica na Etapa 2.

## Dependências

- ✅ Fase -1 concluída (rollback existe via tag `pre-refactor-full-20260429`)
- ✅ Fase 0 concluída (mapeamento detalhado)
- Acesso SSH VPS, leitura `/root/.openclaw/workspace/scripts/`, leitura `/var/log/`

## Fases

### Fase 1A — Diagnóstico isolado por conta (read-only)

Antes de qualquer mudança, isolar o erro de cada conta. Sem rodar script com escrita no banco.

**1A.1 — Coletar logs do cron**
- Localizar log do `sync-inventory-shopee.py` na VPS (provável: `/var/log/`, `/root/scripts/logs/`, ou stdout do cron via `mail`)
- Listar últimas 50 execuções por conta
- Identificar onde para o fluxo: `get_shopee_token` falha? `get_item_list` retorna erro? upsert falha?

**1A.2 — Inspecionar token files**
- `/root/.openclaw/workspace/integrations/shopee/.shopee-tokens-budamix-store.json` ← funcionando
- `.shopee-tokens-budamix-store2.json` ← parou em 18/04
- `.shopee-tokens-budamix-shop.json` ← parou em 01/04

Para cada arquivo: `mtime` (quando foi escrito por último), tamanho, validade JSON, presença de `access_token` e `refresh_token`. **Não copiar conteúdo** — só estatísticas.

**1A.3 — Rodar script manualmente em modo dry-run/debug**

Modificar temporariamente o invocação do script para rodar UMA conta por vez com verbose. Ideal: variável de ambiente filtrando contas, ou comentar 2 das 3 entradas em `ACCOUNTS` em uma cópia de trabalho. Capturar stdout/stderr completos.

Sequência:
1. Rodar isolado para `448649947` (Store) — baseline funcional
2. Rodar isolado para `860803675` (Oficial)
3. Rodar isolado para `442066454` (Shop)

Capturar:
- Status code de cada chamada Shopee API
- Mensagem de erro completa (Shopee retorna `{error, message, request_id}` em payload)
- Linha do código onde falha
- Timestamp da última requisição bem-sucedida no log da conta

**Output da Fase 1A:** apêndice em `00-mapeamento.md` ou novo arquivo `01a-diagnostico.md` com tabela:

| Conta | Erro detectado | Linha do script | Mensagem Shopee | Hipótese |
|-------|---------------|-----------------|-----------------|----------|
| Store | (sem erro) | — | — | OK |
| Oficial | ? | ? | ? | ? |
| Shop | ? | ? | ? | ? |

### Fase 1B — Hipóteses a validar

Diagnóstico provavelmente cai em uma destas categorias:

| Hipótese | Sinal | Correção |
|----------|-------|----------|
| **H1: Refresh token expirou** | Endpoint `refresh_token` retorna `error_auth` ou `invalid_token` | Reautorizar OAuth da conta — gera novo `access_token + refresh_token` |
| **H2: Conta foi suspensa/bloqueada na Shopee** | Endpoint `get_item_list` retorna `error_permission` ou `shop_not_active` | Pedro investiga no admin Shopee da conta; pode envolver suporte Shopee |
| **H3: Rate limit** | HTTP 429 ou `error_too_many_requests` | Adicionar backoff entre contas, espaçar timing |
| **H4: Edge case no script** | Erro Python (KeyError, IndexError, JSONDecodeError) com stack trace | Patch no script, testar isolado, redeploy |
| **H5: Token file corrompido/removido** | mtime antigo, JSON inválido, ou arquivo ausente | Restaurar do backup ou reautorizar |
| **H6: Mudança no payload Shopee** | Campo esperado vira `null` ou estrutura mudou | Adaptar parser, validar contra docs Shopee atual |

H1 é a mais provável — Shopee tem refresh token com expiração de 30 dias. A conta `442066454` parou em **01/04**, exatos 28 dias atrás. Coincide com expiração natural.

### Fase 1C — Correção (executar depois de 1A+1B)

Plano específico depende do diagnóstico. Cenário mais provável (H1, refresh expirou):

**Para cada conta com refresh expirado:**
1. Pedro abre Shopee Open Platform → Reautoriza app → gera nova URL OAuth
2. Pedro completa fluxo OAuth → callback recebe novo `access_token + refresh_token`
3. Kobe atualiza arquivo `.shopee-tokens-{nome-conta}.json` com novos tokens
4. Kobe roda script isolado para a conta — confirma que pega itens

Se diagnóstico apontar outra coisa, plano é adaptado nessa fase.

### Fase 1D — Validação pós-fix

Depois que 3 contas estiverem rodando:

```sql
SELECT shop_id, count(*) AS rows, count(DISTINCT sku) AS skus,
       sum(available_qty) AS units,
       sum(available_qty * coalesce(cost_price, 0)) AS estimated_cost,
       max(last_synced) AS last_sync
FROM fulfillment_inventory
WHERE platform = 'shopee'
GROUP BY shop_id
ORDER BY shop_id;
```

Critério de aceite:
- 3 `last_synced` < 1h
- Total Shopee unitário coerente com painéis das 3 contas (Pedro valida manualmente)
- Sem regressão em `448649947` (Store que já funcionava)

### Fase 1E — Monitoramento defensivo

Sem isso, o problema volta silencioso na próxima expiração de token.

**Adicionar:**
1. Cron de healthcheck que roda 1x/dia: query `last_synced` por conta. Se alguma > 6h, alerta.
2. Canal de alerta: Telegram do Kobe (já existe), ou Telegram pessoal Pedro
3. Log estruturado no `sync-inventory-shopee.py`: por conta, status final (success/error), com motivo

**Mínimo viável (MVP do monitoramento):**
- Script bash em `/root/scripts/healthcheck-shopee.sh` rodando cron `0 */6 * * *`
- Query rápida via `curl` no Supabase REST
- Mensagem Telegram via API se alguma conta > 6h

## Definição de "feito"

A Etapa 1 está completa quando:
- ✅ 3 contas Shopee com `last_synced` < 1h
- ✅ Causa raiz documentada em `01a-diagnostico.md`
- ✅ Correção aplicada e versionada (commit no repo `budamix-central` ou no repo de scripts da VPS, dependendo de onde mora `sync-inventory-shopee.py`)
- ✅ Healthcheck rodando + 1 alerta de teste validado
- ✅ Pedro confirmou que números batem com painel da Shopee em pelo menos 1 SKU por conta

## Riscos

- **Reativar OAuth:** processo manual no painel Shopee, depende do Pedro estar logado nas 3 contas
- **`sync-inventory-shopee.py` não está versionado:** mora em `/root/.openclaw/workspace/scripts/` na VPS, fora do repo `budamix-central`. Mudanças no script precisam de versionamento próprio (ou snapshot tar antes de editar)
- **Possível inconsistência histórica:** se alguma conta ficou 28 dias sem sync, vendas que aconteceram nesse período podem ter mexido em estoque sem refletir. Reposição/recomendações dos últimos 28d podem estar erradas — fora do escopo dessa etapa, mas vale anotar

## Próximo passo

Mensagem pro Kobe executar Fase 1A (diagnóstico read-only).
