---
title: "Daily Sales Report — Shopee"
created: 2026-06-02
updated: 2026-06-04
type: project
status: fase1-validada
path: "/root/segundo-cerebro/shared/daily-sales-analyst/"
tags:
  - project
  - daily-sales
  - shopee
  - pipeline
related:
  - "[[projects/budamix-central]]"
  - "[[reports/daily-sales-report-v2/PLANO-IMPLEMENTACAO-DAILY-SALES-ANALYST]]"
---

# Daily Sales Report — Shopee

**Path (VPS):** `/root/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/`
**Path (Mac, sync):** `~/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/`
**Status:** 🟢 Fase 1 validada end-to-end (04/06/2026 — APROVADO COM RESSALVA no smoke real)
**Owner:** Pedro (decisão) + Kobe / Claude Code (execução)

## O que é

Replicação do pipeline diário do Mercado Livre para as 3 contas Shopee da Budamix, com camada estratégica adicional de consolidação para detectar canibalização e validar / refinar teses por conta. Equivalente Shopee do `daily-sales-ml-pipeline.sh`.

## Decisões-chave do escopo (02/06/2026)

- **3 alavancas ADS distintas:** Shopee Ads (Himmel) + Programa de Afiliados Shopee (Lucas + Pedro) + Cashback em Moedas Shopee (Lucas + Pedro). Não consolidar num ROAS único.
- **L06b Consolidadora descobre teses:** começa com tese seed do Pedro (abaixo), refina / refuta diariamente.
- **Slack só pro Pedro, só a consolidadora:** Lucas não recebe nada por enquanto. Mensagens individuais das 3 contas geradas como artefato auditável em `runs/`, sem disparo.
- **Janela de cron:** ML move para `09:00 UTC` (06:00 BRT). Shopee roda `10:00 UTC` (07:00 BRT). Gap de 1h é seguro.
- **Refutação da tese seed** requer ≥5 ciclos consecutivos da L01 com status `refutada` e SÓ Pedro autoriza mudança formal do papel.

## Tese seed Pedro — 02/06/2026 (baseline da L06b)

> Base: Supabase Budamix Central, 03/04 a 01/06 (60 dias), 8.523 pedidos, R$ 424.650,37 GMV, 9.232 itens. Cancelados excluídos.

**Papel proposto por conta:**

| Conta | shop_id | Papel | Métricas 60d | Crescimento 30d vs 30d |
|---|---|---|---|---|
| **Budamix Store (Conta 1)** | 448649947 | **Volume / Giro** | 4.886 ped • R$ 197.640 • ticket R$ 40,45 | +51,6% ped • +57,9% GMV |
| **Budamix Oficial (Conta 2)** | 860803675 | **Kits / Ticket alto** | 2.020 ped • R$ 121.356 • ticket R$ 60,08 | +49,7% ped • +69,7% GMV |
| **Budamix Shop (Conta 3)** | 442066454 | **Cerâmica / Mesa posta / Kits médios** | 1.617 ped • R$ 105.653 • ticket R$ 65,34 | +30,0% ped • +29,9% GMV |

**Concentração top 3 SKUs:** Store 82,2% / Oficial 63,8% / Shop 59,0%. Store é a mais frágil a ruptura nos campeões.

**Catálogo sobreposto:** 39 dos 61 SKUs aparecem em mais de uma conta. SKU mais crítico de potencial canibalização:
- **CTL002 (Kit 6 Canecas Tulipa 250ml)** — Store 564 un / Oficial 393 un / Shop 379 un (60d). Primeiro alvo de auditoria L06b.

## Estado atual da infra (04/06/2026)

### ✅ Funcional em produção
- **Data Builder v1.3** separando 3 contas Shopee por shop_id no `package.json`
- **`shopee-snapshot-fetcher.py`** — 5 de 9 blocos do `shopee_snapshot` populados em produção
- **Tabela `shopee_account_snapshots`** no Budamix Central (31 colunas, PK composta, 3 índices)
- **Bash pipeline** `/root/scripts/daily-sales-shopee-pipeline.sh` (loop sequencial nas 3 contas)
- **DSA Runner Shopee** `/root/segundo-cerebro/scripts/daily-sales-runner-shopee.py` (adaptado do Runner ML)
- **9 prompts v4.0/shopee** (L01-L09) — 3.708 linhas / 246 KB — em Mac + GitHub `281bbc06` + VPS (triplo backup)
- **Mapeamento canônico** `slack-short-names-shopee.json` (61 SKUs)
- **README** de referência em `prompts/versions/v4.0/shopee/` (132 linhas)
- **Memory folders** das 3 contas com stubs (rules.md / weekly.md / monthly.md)

### Gaps conhecidos do `shopee_snapshot`

| Bloco | Status | Causa | Resolução |
|---|---|---|---|
| `programs` (Vendedor Indicado / Shopee Mall) | ✅ ok | — | — |
| `account_overview` (totals + mix + out_of_stock) | ✅ ok | — | — |
| `top_items_details` | ✅ ok (com `--top-items-from`) | — | — |
| `fulfillment_mix_yesterday_top10` | ✅ ok | — | — |
| `shop_performance` (LSR / NFR / RR / Avaliação / Pontos de Penalidade) | ❌ HTTP 404 | Endpoint correto não identificado | Investigar variantes da API |
| `ads_summary` (Shopee Ads) | ❌ HTTP 403 | Escopo OAuth `ads` não habilitado | Validar com Pedro / Himmel |
| `fulfillment_mix_30d` / `fulfillment_mix_7d` | ❌ `logistic_type=null` em 100% | `sync-shopee-orders.py` não popula | Backfill no sync de pedidos |
| `affiliate_summary` (Programa de Afiliados) | ❌ gap estrutural permanente | Open API Shopee não expõe | Sem resolução via API |
| `coins_summary` (Cashback em Moedas) | ❌ gap estrutural permanente | Mesma razão | Sem resolução via API |

Os prompts L01-L07 já tratam cada um desses casos com regras explícitas.

## Validação Fase 1 — smoke test v4.0/shopee REAL (04/06/2026)

Smoke contra Budamix Store, data 2026-06-01:

| Aspecto | Resultado |
|---|---|
| Tempo total | 18:51 min |
| Veredito L07 | APROVADO COM RESSALVA |
| Críticos | 0 |
| Maiores | 0 |
| Menores | 3 |
| Gates 1-9, 12, 13 | OK |
| Gates 10, 11 | RESSALVA |

### Principais validações
- ✅ Cabeçalho com nome da conta: `DAILY SALES REPORT — SHOPEE BUDAMIX STORE — 01/06/2026 (Ontem)`
- ✅ VISÃO/TOP só dessa conta (não consolidado)
- ✅ Zero "GMV" no texto, "Faturamento" sempre
- ✅ Status da tese seed: **"em observação"** + justificativa
- ✅ 4 `observacoes_para_consolidadora` alimentando L06b (CTL002 + IMB501P + padrão ticket/volume + config de boosters)
- ✅ Gate_12 (consistência `shopee_snapshot`) ativo
- ✅ Gate_13 (coerência status tese seed L01→L05→L06) ativo
- ✅ Bloqueio cross-account respeitado
- ✅ POST-baixa respeitado ("encerraram em estoque zero", não retroativo)

### 3 menores apontados pela QA (sinais para próxima rodada de refinamento)
1. **Gate 11** — Percentuais sem 1 casa decimal: "72%" deveria ser "72,1%" (4 ocorrências)
2. **Gate 10** — Anglicismo "booster" nas Prioridades (inconsistência com "amortecedor" usado na Análise)
3. **Gate 10** — Anglicismo "baseline" na Análise (deveria ser "média 60d" ou "referência 60d")

Os 3 menores indicam refinamento futuro do glossário PT-BR proibido (incluir "booster" e "baseline" explicitamente).

## Plano em fases

| Fase | Foco | Esforço | Status |
|---|---|---|---|
| **1** | Pipeline standalone Conta 1 (Store) — snapshot + prompts v4.0/shopee + bash `--shop-id` + runner adaptado | — | ✅ **Validado 04/06/2026** |
| **2** | Extensão Contas 2 e 3 + cron `10:00 UTC` + janela ML movida pra `09:00 UTC` | 2-3 dias | Próximo |
| **3** | L06b Consolidadora-Estrategista ativada: descobre teses + detecta canibalização + alimenta `cross-account-memory.md`. **Única mensagem Slack do dia (consolidada, pro Pedro)** | 4-5 dias | — |
| **4** | Mission Control (tile Shopee 3 sub-blocos + consolidado), QA Gate Shopee-aware, health checks, audit trail | 2-3 dias | — |
| **Futuro (opcional)** | Liberar mensagem individual pro Lucas | — | Decisão de Pedro |

## Próximos passos lógicos

1. **Smoke contra Contas 2 e 3** (15-20 min cada) — validar que o pipeline funciona simetricamente
2. **Ativar bash pipeline com loop 3 contas** + cron `10:00 UTC` (não ativar produção até validar)
3. **Refinamento v4.0/shopee** opcional — incluir "booster" e "baseline" nas proibições da L05 + força formatação 1 casa decimal em Gate 11
4. **Resolver 3 gaps de fetcher** (endpoint Shop Performance, escopo Ads, backfill `logistic_type`) — destravam Lente 2 / 5a / mix histórico

## Referências

- Pasta v4.0/shopee: `~/segundo-cerebro/openclaw/agents/kobe/shared/daily-sales-analyst/prompts/versions/v4.0/shopee/`
- README de referência: `prompts/versions/v4.0/shopee/README.md`
- Mapeamento canônico: `config/slack-short-names-shopee.json`
- Runner: `/root/segundo-cerebro/scripts/daily-sales-runner-shopee.py`
- Snapshot fetcher: `/root/segundo-cerebro/scripts/shopee-snapshot-fetcher.py`
- Bash pipeline: `/root/scripts/daily-sales-shopee-pipeline.sh`
- Tabela Supabase: `public.shopee_account_snapshots` (projeto `sqbkoprcmnznmzbwdrmf`)
- Logs: `/var/log/daily-sales/shopee-runner-v4real-YYYY-MM-DD.log`

## Histórico

- **04/06/2026 12:00** — **Smoke test v4.0/shopee REAL contra Budamix Store APROVADO COM RESSALVA.** 7 camadas LLM, 18:51 min, 0 críticos / 0 maiores / 3 menores. Gate_12 e Gate_13 ativos. Bug do v3.0 (cabeçalho sem conta, "GMV" escapado, VISÃO consolidada) completamente corrigido.
- **04/06/2026 09:00-11:00** — **9 prompts v4.0/shopee reescritos do zero.** Versão original nunca foi persistida no disco (descoberta forense via input.txt do smoke v3.0 + grep por strings únicas). Reescrita completa (3.708 linhas / 246 KB) + triplo backup (Mac + GitHub `281bbc06` + VPS). README de referência (132 linhas) adicional. Ficha do projeto reconstruída.
- **03/06/2026** — DSA Runner Shopee adaptado do Runner ML. Smoke v3.0 fallback aprovou COM RESSALVA mas com bugs óbvios (cabeçalho sem conta, "GMV" escapado, VISÃO consolidada).
- **02/06/2026 noite** — **Snapshot fetcher Shopee implementado e validado nas 3 contas.** Tabela `shopee_account_snapshots` criada. 3 linhas persistidas.
- **02/06/2026 noite** — Vocabulário PT-BR oficial recebido do Pedro. Glossário ancorado.
- **02/06/2026** — Auditoria do pipeline ML confirma saúde 100%. Pedro aprova replicação pra Shopee. Plano em 4 fases definido. Tese seed das 3 contas registrada (base 60d).
