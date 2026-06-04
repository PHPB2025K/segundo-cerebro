# v4.0 / Shopee — Prompts do Daily Sales Analyst

Pipeline diário Shopee, 1 conta por execução. 3 contas Budamix (Store / Oficial / Shop) processadas em sequência pelo bash `/root/scripts/daily-sales-shopee-pipeline.sh`. A L06b Consolidadora cross-account roda depois, separada.

**Status:** Fase 1 — Slack individual da L06 NÃO é enviado (artefato auditável). Única mensagem do dia é a consolidada da L06b → Pedro.

## Mapa das 9 camadas

| # | Camada | Output | Função | Linhas |
|---|---|---|---|---|
| L00 | Data Builder + Snapshot Fetcher + Merge | `package.json` | Determinístico — sem LLM | scripts |
| L01 | Estratégica | Markdown | Tese da conta + status da tese seed | 587 |
| L02 | Tática | Markdown | Decisão 5-7d + postura sobre tese seed | 372 |
| L03 | Operacional | Markdown | Raio-X execução do dia + perguntas pra L04 | 392 |
| L04 | Granular | JSON | Evidência forense + bloqueios_para_slack | 457 |
| L05 | Condensadora | JSON | Editora-chefe + observacoes_para_consolidadora | 459 |
| L06 | Slack Writer | Markdown | Artefato (não enviado na Fase 1-2) | 502 |
| L07 | QA Gate | JSON | 13 gates (12 = snapshot consistency / 13 = tese seed) | 615 |
| L08 | Weekly | Markdown | Consolidação semanal (segunda 09:00 BRT) | 167 |
| L09 | Monthly | Markdown | Consolidação mensal (dia 1 09:00 BRT) | 157 |

**Total dos 9 prompts:** 3.708 linhas / 246 KB.

## L00 — pré-requisitos determinísticos

A L00 é código, não LLM. Composta por 4 componentes:

1. **Data Builder** (`scripts/daily-sales-data-builder.py`) — gera `package.json` com métricas BRT canônicas das 3 contas Shopee + top_products + histórico 7d/30d/60d + data_readiness checks. **OK em produção.**
2. **Snapshot Fetcher** (`scripts/shopee-snapshot-fetcher.py`) — gera `shopee_snapshot` enriquecido via Open API Shopee + persiste em `public.shopee_account_snapshots`. **OK em produção** (5 de 9 blocos funcionais; 4 com gaps conhecidos abaixo).
3. **Merge** (no bash pipeline) — injeta `shopee_snapshot` em `platforms.shopee-{slug}` no package. **OK em produção.**
4. **Layer 0 contract validation** (no runner) — `validate_layer0_product_contract()` bloqueia pipeline se mapping crítico falhar. **OK em produção.**

### Gaps conhecidos do `shopee_snapshot` (estado em 03/06/2026)

| Bloco | Status | Causa | Resolução pendente |
|---|---|---|---|
| `programs` (Vendedor Indicado / Shopee Mall) | ✅ ok | — | — |
| `account_overview` (totals + mix + Mall pct + FSP pct + out_of_stock) | ✅ ok | — | — |
| `top_items_details` | ✅ ok | — | — |
| `fulfillment_mix_yesterday_top10` | ✅ ok | — | — |
| `shop_performance` (LSR / NFR / RR / Avaliação / Pontos de Penalidade) | ❌ HTTP 404 | Endpoint correto não identificado | Investigar `/api/v2/account_health/shop_performance` ou variantes |
| `ads_summary` (Shopee Ads) | ❌ HTTP 403 | Escopo OAuth `ads` não habilitado | Validar com Pedro / Himmel pra adicionar escopo |
| `fulfillment_mix_30d` / `fulfillment_mix_7d` | ❌ `logistic_type=null` em 100% | `sync-shopee-orders.py` não popula o campo | Backfill no sync de pedidos |
| `affiliate_summary` (Programa de Afiliados) | ❌ gap estrutural permanente | Open API Shopee não expõe (só Seller Center) | Sem resolução via API — só dado humano |
| `coins_summary` (Cashback em Moedas) | ❌ gap estrutural permanente | Mesma razão acima | Sem resolução via API |

Os prompts L01-L07 já tratam cada um desses casos com regras explícitas (declarar `unavailable`, não inventar leitura, gaps permanentes recebem linguagem suave "limitação da Open API"; gaps pendentes recebem "indisponível no ciclo de hoje").

## Glossário PT-BR essencial

Texto narrativo dos outputs nunca usa termos em inglês. Tradução obrigatória:

- `GMV` → **Faturamento** (bloqueio Maior na L07 se escapar)
- `ADS share` solto → **share de Shopee Ads** / **Shopee Ads respondeu por X%**
- `Preferred Seller` / `Star Seller` → **Vendedor Indicado** / **Vendedor Indicado Star**
- `Mall Shop` / `Mall Brand` / `not_mall` → **Loja Oficial** / **Marca Oficial** / **fora do Shopee Mall**
- `FSP` / `Free Shipping Program` → **Programa de Frete Grátis** (+ **Frete Grátis Extra**)
- `Coins Cashback` / `Coins` → **Cashback em Moedas Shopee**
- `Affiliate` → **Programa de Afiliados Shopee**
- `fulfillment` (conceito) → **modalidade de envio**
- `runway` → **fôlego**
- `ETA` → **estimativa** / **prazo estimado**
- `breakdown` → **detalhe** / **abertura**

Campos técnicos em backticks são permitidos (`is_preferred_seller`, `mall_status`, `is_fulfillment_by_shopee`).

## Decisões arquiteturais críticas (não esquecer)

1. **1 conta por execução** — o pipeline analisa Budamix Store OU Oficial OU Shop por vez. Comparação cross-account é função da L06b Consolidadora, que roda depois.
2. **Tese seed Pedro v1 (02/06/2026)** é input crítico. A Lente 6 de cada camada valida / refina / refuta o papel hipotetizado. Refutação requer ≥5 ciclos consecutivos e SÓ Pedro autoriza.
3. **3 alavancas ADS separadas** — Shopee Ads (Himmel), Programa de Afiliados Shopee (Lucas + Pedro), Cashback em Moedas Shopee (Lucas + Pedro). Não consolidar num ROAS único.
4. **L06 individual não é enviada** durante Fase 1-2 — fica como artefato auditável em `runs/`. Slack único do dia será a L06b consolidada (Fase 3).
5. **`available_quantity` é POST-baixa** — estoque do snapshot é após os pedidos do dia. Risco de ruptura é sempre **prospectivo** (próximos pedidos), nunca retrospectivo (pedidos do dia já atendidos). L03/L04/L05/L06/L07 têm regras duras sobre isso.
6. **Status da tese seed** — campo formal entregue pela L01 e validado pela L05, com 5 valores: confirmada / refinada / em observação / enfraquecida / refutada. Gate 13 da L07 valida coerência L01 → L05 → L06.

## Como rodar

### Pipeline bash completo (3 contas em sequência)
```bash
/root/scripts/daily-sales-shopee-pipeline.sh [YYYY-MM-DD]
```

### Runner por conta (uma de cada vez)
```bash
python3 /root/segundo-cerebro/scripts/daily-sales-runner-shopee.py YYYY-MM-DD \
    --shop-slug budamix-store \
    --account-context /tmp/shopee-pipeline/YYYY-MM-DD/account-context-budamix-store.md \
    --preview-to-kobe --llm
```

`--shop-slug`: `budamix-store` | `budamix-oficial-2` | `budamix-shop-3`
`--account-context`: path do `.md` montado pelo bash (tese seed + baseline 60d + papel hipotetizado)

### Artefatos gerados
`/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/runs/YYYY-MM-DD/shopee-{slug}/`
- `00-data-package.json` (cópia auditável)
- `01-estrategica.input.txt` + `01-estrategica.md`
- ... (até 07)
- `manifest.json`

## Como evoluir os prompts (versionamento)

- **Esta pasta (`v4.0/shopee/`)** é a versão ativa do pipeline Shopee.
- Fixes pequenos / correção de typo → editar direto e commitar.
- Mudanças de tese / lentes / status → considerar bump pra `v4.1/shopee/` (cópia + edit) pra permitir rollback.
- O runner aceita `--prompt-version v4.1/shopee` quando houver.
- O fallback do runner é `v3.0/` (genérico antigo) se a camada não existir na versão pedida — não confiar nisso pra produção.

## Pendências de fetcher (passo 4 da Fase 1)

1. Identificar endpoint correto de Shop Performance Shopee (atualmente HTTP 404)
2. Habilitar escopo `ads` no app OAuth Shopee (atualmente HTTP 403)
3. Backfill de `orders.logistic_type` no `sync-shopee-orders.py` (atualmente 100% null)

Esses 3 destravam Lente 2 (Saúde da Loja) + Lente 5a (Shopee Ads) + comparativo de mix de modalidade de envio em janela longa. Não bloqueiam a Fase 1 — prompts já lidam com `unavailable` graciosamente.

## Histórico

- **02/06/2026** — Tese seed Pedro v1 das 3 contas registrada (baseline 60d: 03/04 a 01/06).
- **02-03/06/2026** — Snapshot fetcher implementado + tabela `shopee_account_snapshots` criada + smoke test em 3 contas OK.
- **03/06/2026** — DSA Runner Shopee adaptado do Runner ML. Smoke test rodou em fallback v3.0 (descoberta: prompts v4.0/shopee originais não persistiram).
- **04/06/2026** — Reescrita completa dos 9 prompts v4.0/shopee. Commit `281bbc06` no git remote + scp na VPS pra blindagem tripla.

## Referências

- Ficha do projeto: `~/segundo-cerebro/projects/daily-sales-shopee.md`
- Mapeamento canônico de nomes curtos: `../../../config/slack-short-names-shopee.json` (61 SKUs)
- Pipeline ML como referência arquitetural: `../mercado-livre/`
- Runner: `/root/segundo-cerebro/scripts/daily-sales-runner-shopee.py`
- Snapshot fetcher: `/root/segundo-cerebro/scripts/shopee-snapshot-fetcher.py`
- Bash pipeline: `/root/scripts/daily-sales-shopee-pipeline.sh`
- Tabela Supabase: `public.shopee_account_snapshots` (projeto Budamix Central `sqbkoprcmnznmzbwdrmf`)
