---
title: "Amazon Ads Automation — BidSpark-3"
created: 2026-04-20
type: concept
status: active
tags:
  - knowledge
  - amazon
  - ads
  - bidspark-3
  - budamix
---

# Amazon Ads Automation — BidSpark-3

> Knowledge file consolidado do projeto de gestão de campanhas Amazon Ads da Budamix.
> Fonte de verdade das decisões. Para código/scripts, ver `~/Documents/05-Projetos-Codigo/amazon-ads-automation/`.

---

## 1. Identidade do projeto

| Campo | Valor |
|---|---|
| **Path** | `~/Documents/05-Projetos-Codigo/amazon-ads-automation/` |
| **Branch** | `main` (4 commits local-only: `19a6638`, `5489ae0`, `e1d56cd`, `c7b95d9`) |
| **Stack** | Python + FastAPI + Docker |
| **Deploy** | Railway |
| **Supabase** | tabelas `amazon_ads_*` (ver §6) |
| **Orquestração** | N8N (workflow `U8MCTTkNEJnD75aV` — Ciclo Diário 6h BRT) |
| **Skill operacional** | `ANALISE_SEMANAL_SKILL.md` **v4.2** (BidSpark-3) |
| **Estado** | 4/8 grupos migrados para BidSpark-3 (19/04/2026) |

**Modelo operacional (atualizado 19/04):** N8N roda **apenas coletas diárias**. Análise e otimização são **manuais via Claude Code** usando a skill BidSpark-3. Supervisão humana substituiu o fluxo "N8N → Claude API automática → ações" original.

---

## 2. Tese do sistema — funil de 3 campanhas

Cada grupo de produto é um **funil integrado** de 3 campanhas (não 4 — Defesa foi removida em 16/04). Nenhuma campanha opera isolada; cada uma alimenta a próxima.

### Papel de cada campanha

| Campanha | Multiplicador ACoS | Budget nominal | Papel |
|---|:-:|:-:|---|
| **DESCOBERTA** (auto) | ×1.5 | 15% | Mineração de termos novos — aceita ACoS maior |
| **ALCANCE** (broad/phrase) | ×1.2 | 30% | Captura variações de termos conhecidos |
| **PERFORMANCE** (exact) | ×0.72 | 55% | Motor de lucro — winners comprovados |

**Exemplo com target 20%:** Desc 30% | Alc 24% | Perf 14.4%

Budget split 15/30/55 nominal é **ponto de partida obrigatório** em toda migração (skill v4.1 §2). Drift operacional ±5pp tolerável em regime, não como ponto de partida.

### Fluxo do funil

```
Cliente busca "pote hermético vidro tampa bambu 500ml"
  → Performance EXACT "pote hermético vidro tampa bambu" NÃO captura (não é exact match)
  → Alcance BROAD "pote hermético bambu" CAPTURA ✅
  → Se converter 2+ vezes: migrar para Performance + negativar EXACT no Alcance

Cliente busca "pote hermético vidro tampa bambu"
  → Performance EXACT captura ✅
  → Alcance bloqueado por NEGATIVE_EXACT ✅ (roteamento)
  → Descoberta bloqueado por NEGATIVE_EXACT ✅

Cliente busca "pote plástico hermetico"
  → Bloqueado por NEGATIVE_PHRASE "plástico" em todas as campanhas ✅ (filtro de material)
```

### Regras invioláveis do funil

- **NEGATIVE_EXACT = roteamento** (direciona tráfego exact de uma campanha para outra)
- **NEGATIVE_PHRASE = filtro** (bloqueia material/contexto irrelevante, ex: "inox" em porcelana)
- NUNCA usar NEGATIVE_PHRASE em substantivos core (caneca, jarra, pote, xícara)
- Todo termo na Performance DEVE ter NEGATIVE_EXACT correspondente nas origens
- ASINs dos produtos devem estar em TODAS as 3 campanhas do grupo

---

## 3. Guardrails — G1 a G8

Existem porque em Fev/Mar 2026, o sistema antigo negativou termos core ("caneca", "microfibra", "jarra de vidro") como NEGATIVE_PHRASE em nível de campanha → **queda 99% de impressões, ~R$1.270/semana perdidos**.

| # | Regra | Detalhe |
|---|---|---|
| **G1** | Termos protegidos | Tabela `amazon_ads_protected_terms` (257 termos). Consultar ANTES de negativar. Aprovação explícita do Pedro para override. |
| **G2** | NEGATIVE_EXACT default | PHRASE só para MATERIAIS/CONTEXTOS irrelevantes. NUNCA em substantivos do produto. |
| **G3** | Limite de bid | Max -30%/ciclo, -50% acumulado em 28d. Mínimo absoluto R$0.30 (keywords) / R$0.15 (targeting). |
| **G4** | Limite de negativações | DESC 30 / ALC 40 / PERF 15 / DEF 5 por campanha |
| **G5** | Nunca negativar com vendas | Qualquer venda 30d → não negativar. Termo core com 0 vendas → problema é listing, não ads. |
| **G6** | Dados mínimos | Reduzir bid: 20+ clicks. Negativar irrelevante: 10+ cliques + R$3+ spend + 0 vendas. Migrar: 2+ vendas. |
| **G7** | Pares de migração | Toda migração → Performance exige NEGATIVE_EXACT na origem (primeiro cria destino, depois negativa origem) |
| **G8** | Nunca migrar ASINs | Regex `^[bB]0[a-zA-Z0-9]{8,}$`. ASINs podem ser negativados, nunca migrados. |

---

## 4. Metodologia — 4 fases sequenciais

### FASE 1 — Coleta (automática, sem perguntar)

Fonte primária: **Supabase** (dados do ciclo N8N). Secundária: **API Amazon ao vivo** enquanto `keyword_snapshots` e `negative_snapshots` não têm 30d de histórico (até ~10/05/2026).

Métricas em 3 janelas (**7d, 15d, 30d**) para evitar decisões por flutuação de curto prazo: impressões, cliques, CTR, CPC médio, spend, sales, ACoS, ROAS, pedidos, budget utilization.

### FASE 2 — Análise (automática, 6 dimensões)

1. **Integridade do funil:** furos de NEGATIVE_EXACT? PHRASE destrutivas? ASINs em todas as campanhas? Competição interna? Bids invertidos (Alcance > Performance no mesmo termo)?
2. **Métricas vs target:** cada campanha vs seu target específico (multiplicador). Budget utilization >90% limita, <30% sobra.
3. **Search terms:** winners (candidatos a migração), waste (spend >R$3 + 0 vendas), ASINs (separar concorrente de product targeting).
4. **Tendência:** 7d vs 15d vs 30d. Ponto de inflexão cruzado com data das ações nossas.
5. **Resultado das ações anteriores:** `result_after_7d` calculado pelo compute-results. MELHOROU/NEUTRO/PIOROU. Se PIOROU: não repetir abordagem. Se MELHOROU: escalar.
6. **Diagnóstico de conversão:** tráfego alto + 0 vendas pode ser listing/preço/Buy Box/estoque, NÃO ads.

### FASE 3 — Recomendações (PARAR e esperar aprovação)

Formato por grupo, dentro de cada grupo **por campanha**, classificação de risco das ações:
- ✅ **SEGURA**: negativar ASIN concorrente, migrar winner comprovado, negativar irrelevante claro
- ⚠️ **REVISAR**: reduzir bid >20%, negativar termo com alguma relação, ajustar budget
- 🔴 **DECISÃO**: pausar keyword com vendas históricas, mudança estrutural

**Nunca executar sem aprovação explícita do Pedro.**

### FASE 4 — Execução (somente após aprovação)

1. Re-verificar G1–G8
2. Executar via SDK `python-amazon-ad-api`
3. Registrar em `amazon_ads_actions_log` (action_type, entity_name, old_value, new_value, reason com dados concretos, status=EXECUTED)
4. Reportar resultado + IDs Amazon
5. Definir efeito esperado para compute-results medir em 7d

---

## 5. Metodologia BidSpark-3 — Blocos de migração (skill v4.2)

Migração de um grupo é dividida em blocos executados em ordem. **Em grupos antigos (pré-01/03/2026) o Bloco 3 precede o Bloco 2** (descoberta no Paris, formalizado na v4.2).

| Bloco | Propósito | Quando |
|---|---|---|
| **Bloco 1** | Housekeeping (pausar Defesa, remover waste óbvio, adicionar negativas de grupo G1) | Sempre primeiro |
| **Bloco 2** | Migrações EXACT (winners Alcance/Descoberta → Performance + pares G7) | Após Bloco 1 (ou após Bloco 3 em grupos antigos) |
| **Bloco 3** | Limpeza de NEG_PHRASE destrutivas herdadas de Fev/Mar 2026 | Antes do Bloco 2 em grupos antigos |
| **M2** | Rebalance budget 15/30/55 sobre total do grupo | Fim, se a migração fechou coerente |

**Gatilho `DECISAO_ADIAR_M2`:** se Performance ainda subutilizada (<20%) ou Bloco 2 vazio (zero winners), pular M2 e aguardar ~14d.

**Inspeção de NEG_PHRASE obrigatória (v4.2 §4):** classificar 🟢/🔴/⚠️ por grupo antes de qualquer análise de métrica. Se houver 🔴 → Bloco 3 automático.

**Normalização de acento pela Amazon:** EXACT com e sem acento são duplicatas (confirmado em Paris: `xicaras de café porcelana` ≡ `xicaras de cafe porcelana`). Skill v4.2 §5.3.

**Zombies:** 80 AJUSTAR_BID antigas ficam eternamente no eligible set sem dados para computar. Não bloqueiam mas poluem. Ticket 2 propõe outcome terminal `ENTITY_STALE` após 14d sem dados.

---

## 6. Infraestrutura de dados

### Tabelas Supabase — mapa completo

| Tabela | Tipo | Frequência | Dados |
|---|---|:-:|---|
| `amazon_ads_campaigns` | Relatório | Diário D-2 | Métricas de campanha |
| `amazon_ads_keywords` | Relatório | Diário D-2 | Métricas de keyword + bid |
| `amazon_ads_search_terms` | Relatório | Diário D-2 | Search terms com métricas |
| `amazon_ads_keyword_snapshots` | API live | Diário | Bids atuais + state (ENABLED/PAUSED) |
| `amazon_ads_negative_snapshots` | API live | Diário | Negativas ativas por campanha |
| `amazon_ads_product_ads` | API live | Diário | ASINs por campanha |
| `amazon_ads_catalog` | API Metadata | Diário | Título, preço, BSR, categoria |
| `amazon_ads_product_groups` | Estático | Manual | Metas (acos_target, margin, budget) — FONTE ÚNICA de metas |
| `amazon_ads_campaign_roles` | Estático | Manual | Mapeamento campanha → grupo → role |
| `amazon_ads_protected_terms` | Estático | Manual | 257 termos que nunca negativar |
| `amazon_ads_actions_log` | Evento | Por ação | Histórico + `result_after_7d` |
| `amazon_ads_config` | Estático | Manual | 4 configs globais |

### Pipeline N8N — Ciclo Diário 6h BRT

```
Schedule 6h BRT
  → Health Check
  → Collect Campaigns (D-2)     → amazon_ads_campaigns
  → Collect Targeting (D-2)      → amazon_ads_keywords
  → Collect Search Terms (D-2)   → amazon_ads_search_terms
  → Daily Health Check           → alertas WhatsApp
  → Rolling Collection (D-4, D-9, D-16, D-30) → reapuração
  → Sync Catalog                 → amazon_ads_catalog
  → Collect Product Ads          → amazon_ads_product_ads
  → Compute Action Results       → actions_log.result_after_7d
  → Keyword Snapshots            → amazon_ads_keyword_snapshots
  → Negative Snapshots           → amazon_ads_negative_snapshots
  → Format Summary + Send WhatsApp
```

**Conexão Supabase para análise manual:** `venv/python + psycopg2 + DATABASE_URL` (padrão estabelecido 19/04).

---

## 7. Estado operacional — 20/04/2026

### Grupos migrados para BidSpark-3 (5/12)

| # | Grupo | Data | Ações | Observação |
|---|---|---|:-:|---|
| 0 | Suporte Controle Gamer | 16/04 (piloto) | — | Revisão formal 30/04. Metas: ACoS <15%, 0 bleeders, utilização >30% |
| 1 | Potes Tampa Bambu | 19/04 | 12 | Alcance PAUSED (manter até investigação listing) |
| 2 | Potes Herméticos Vidro | 19/04 | 27 | **Primeiro grupo com M2 efetivamente rodado** (R$30 total). Ticket 3: expandir ASINs Alcance 6/13 → 13/13 |
| 3 | Kit Xícaras Porcelana Paris | 19/04 | 48 | Caso antigo: 34 NEG_PHRASE destrutivas removidas + 5 ASINs → NEG_EXACT. Ordem invertida (Bloco 3 antes do Bloco 2) |
| 4 | Canecas Porcelana Tulipa | 19/04 | 43 | Pior legado: 39 PHRASE destrutivas removidas (Alcance 53→33, Descoberta 26→7). Bloco 2 **vazio**. DECISAO_ADIAR_M2. Revisitar ~03/05 |

### Fila de migração (próximos 5 grupos)

1. **Canequinhas Café** — hipótese: criado 01/03 pode ter escapado do legado destrutivo
2. **Potes Redondos Plástico**
3. **Kits Microfibra Carro** — edge: campanha órfã
4. **Canecas Canelada** — edge: split 81/10/8
5. **Jarra Medidora** — edge: Defesa-ASIN (única exceção com Defesa real)

Ritmo: **um grupo por dia**.

### Amazon Ads — snapshot 60 dias (baseline 15/04)

- 139 campanhas (48 ativas, 91 pausadas — Era 1: 2022-2025, lixo histórico)
- 12 grupos × 4 camps (pré-migração); BidSpark-3 converge para 3 camps × 12 grupos
- ACoS geral: 22,9%
- Spend 60d: R$4.884 | Sales 60d: R$21.317

### Ações cirúrgicas executadas 15/04 (83 ações em `amazon_ads_actions_log`)

- **AÇÃO 1:** Canequinhas Café bids -50%/-50%/-40% (58 keywords Desc/Alc/Exact)
- **AÇÃO 2:** 16 negativas campaign-level (caneca, xicara, xícara, marmita, marmita de vidro) em 8 campanhas — override G1 autorizado (termos com R$270 gasto e zero vendas)
- **AÇÃO 3:** Potes Tampa Bambu Alcance PAUSED (ACoS 62,8%)
- **AÇÃO 4:** Abraçadeiras Nylon + Redinha Frutas (8 camps) PAUSED (zero vendas/tráfego 60d)
- Campanhas ativas: 48 → 39. Budget diário: R$315 → ~R$274

### Revisões marcadas

| Data | Item |
|---|---|
| 20/04 6h BRT | Validar N8N Ciclo Diário rodou limpo pós-fix `continueOnFail` (19/04) |
| 29/04 | Impacto ações 1–3 de 15/04 (meta ACoS ≤19%) |
| 30/04 | BidSpark-3 Piloto Gamer — revisão formal |
| ~03/05 | Tulipa pós-Bloco 3 — Descoberta voltou a converter? ACoS consolidado <20%? |
| 15/06 | Reavaliar Abraçadeiras/Redinha (Ação 4) |

---

## 8. Alertas ativos (SKUs em atenção)

- **KIT2YW520SQ:** ACoS 64,8%, R$244 gasto / 7 vendas em 60d → **pausar urgente**
- **5 SKUs Amazon com margem negativa pós-ACoS real:** 914C_BB, K6CAN250, KIT2CK4742_B, KIT4YW520SQ, KIT4YW800SQ → revisar preço ou pausar ads
- **26/46 SKUs sem ASIN na planilha** → preencher pra diferenciar com/sem ads
- **157 keywords PHRASE legacy** remanescentes — possível resquício Fev/Mar
- **91 campanhas pausadas (Era 1: 2022–2025)** — considerar arquivamento

---

## 9. Decisões-chave (cronológico)

| Data | Decisão |
|---|---|
| 13/04 | Amazon Request Review migrado para Opus 4.6 exclusivo + `delivered_at` + timeout 600s + batch 35 |
| 13/04 | Backfill de ~4866 pedidos executado |
| 15/04 | Auditoria ACoS real: ML 11,4% (345 ads) / Amazon 20,4% (47 ASINs) / Shopee sem API Ads |
| 15/04 | Ads flats atualizados na planilha (MELI 6→11%/0%, AMAZON 8,9→20%/0%, SHOPEE 5→7%) |
| 16/04 | **BidSpark-4 → BidSpark-3** — Defesa removida como role. 3 campanhas canônicas (Desc/Alc/Perf) |
| 16/04 | Piloto BidSpark-3 em Suporte Controle Gamer |
| 19/04 | Budget split 15/30/55 nominal obrigatório em migração (multiplicadores ×1.5/×1.2/×0.72) |
| 19/04 | N8N apenas para coletas — análise/otimização é manual via Claude Code |
| 19/04 | compute-results fix: `continueOnFail=true` + `onError=continueRegularOutput` no node WhatsApp Alert |
| 19/04 | Inspeção de NEG_PHRASE obrigatória em análise (v4.2 §4) |
| 19/04 | Normalização de acento pela Amazon → EXACT c/ e s/ acento são duplicatas (v4.2 §5.3) |

---

## 10. Incidentes críticos — memória institucional

### Fev/Mar 2026 — Negativações PHRASE destrutivas
Sistema antigo negativou "caneca", "microfibra", "jarra de vidro" como NEGATIVE_PHRASE em nível de campanha. **-99% impressões, ~R$1.270/semana perdidos.**
→ G1 + G2. Skill v4.2 §4 inspeção obrigatória.

### Mar 2026 — Migração de ASINs
ASINs de concorrentes foram migrados como EXACT para Performance. Gastou dinheiro biddando em produtos alheios.
→ G8. Regex `^[bB]0[a-zA-Z0-9]{8,}$`.

### Mar 2026 — Bid crushing
Mesma keyword recebeu -30% por 3 ciclos (total -66%). Keyword morreu.
→ G3. Limite acumulado 50% em 28d.

### 11/04 → 19/04 — compute-results stale 9 dias
Node `Send Health Alert WhatsApp` do N8N Ciclo Diário falhou com 500 da Evolution API desde 11/04, derrubando toda cadeia downstream. `result_after_7d` travado. Causa NÃO era bug no código — era falha upstream bloqueando branch.
→ Fix `continueOnFail=true` aplicado via N8N API em 19/04 22h. Ticket 1: refactor para desacoplar notificação de coleta em branches paralelos.

---

## 11. Tickets abertos

Todos em `docs/TICKETS.md` do projeto.

- **Ticket 1:** Refactor Ciclo Diário N8N — desacoplar WhatsApp de coleta em branches paralelos
- **Ticket 2:** compute-results zombies — outcome terminal `ENTITY_STALE` após 14d sem dados
- **Ticket 3:** Potes Herméticos Vidro — expandir ASINs Alcance 6/13 → 13/13

---

## 12. Pendências operacionais

- 🔴 [20/04 6h BRT] Validar N8N Ciclo Diário rodou limpo pós-fix `continueOnFail`. Se falhar → **PARAR migração BidSpark-3** e diagnosticar. Comando: `curl -s -H "X-N8N-API-KEY: $KEY" "$URL/api/v1/executions?workflowId=U8MCTTkNEJnD75aV&limit=3"`
- ⏭️ Migração 5 grupos restantes (Canequinhas → Redondos → Microfibra → Canelada → Jarra) — um por dia
- ⏭️ Investigação listing Tampa Bambu (7 ASINs: B0F2GHQHRN, B0F2GKSHYW, B0F2GQNT81, B0F2GKZZ43, B0F2GM9HMW, B0FN4PGK4M, B0FN4PW4SS) — Pedro manual no Seller Central. Pergunta: por que buscas "bambu" específico (`potes hermeticos bambu`, `pote hermetico bambu`, `potes de vidro com tampa de bambu`, `porta temperos bambu`) geram clique mas zero venda? Verificar preço vs concorrentes, Buy Box, ranking, fotos, reviews, título contém "bambu"?, estoque.
- ⏭️ Push dos 4 commits local-only (`19a6638`, `5489ae0`, `e1d56cd`, `c7b95d9`)
- ⏭️ SKUs duplicados: `IMB501*_T` e `IMB501T-{cor}` apontam mesmos ASINs — investigar/consolidar
- ⏭️ Coleta diária falhando em 2 dias (12/04, 15/04) — investigar cron N8N

---

## 13. Scripts de referência (repo)

Sessão 19/04 gerou template consolidado:

- `scripts/bidspark3_tampa_bambu_bloco1.py` + `bloco2.py`
- `scripts/bidspark3_potes_vidro.py`
- `scripts/bidspark3_paris.py`
- `scripts/bidspark3_tulipa.py`

Padrão: script idempotente que executa 1 bloco de 1 grupo, lê metas via `amazon_ads_product_groups`, re-checa G1–G8 em runtime, registra cada ação em `amazon_ads_actions_log` com `reason` populado por dados concretos, gera `bidspark3_{grupo}_results.json` com outcome.

---

## Ver também

- [[projects/amazon-ads-automation]] — índice do projeto
- [[projects/analise-semanal-skill-amazon]] — skill operacional (v4.2)
- [[projects/bidspark-multiagente-completo]] — design multi-agente original (pausado)
- [[openclaw/agents/spark/IDENTITY]] — agente Spark (marketplaces)
- [[memory/sessions/2026-04-19]] — sessão densa com as 4 migrações
- [[memory/sessions/2026-04-15]] — auditoria ACoS real + 83 ações cirúrgicas
- [[memory/sessions/2026-04-16]] — piloto BidSpark-3 Gamer + Fase 1 escalação
- [[memory/context/pendencias]] — lista ativa
- [[memory/context/decisoes/2026-04]] — decisões de abril

---

*Criado: 20/04/2026 — consolidação das sessões 13/04 → 19/04 (Request Review fix, BidSpark-4→3, 83 ações cirúrgicas, 4 migrações, compute-results fix, skill v4.0→v4.2).*
