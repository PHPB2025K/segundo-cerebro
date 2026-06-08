---
title: "accounts"
created: 2026-04-14
modified: 2026-06-08
type: agent
agent: spark
status: active
tags:
  - agent/spark
---

# Contas de Anúncio — Spark

_Status e detalhes de cada conta. Atualizado 2026-06-08._

---

## Meta Ads

### 🟢 Budamix (PRIMÁRIA ATIVA)

| Campo | Valor |
|---|---|
| **Account ID** | `act_1140258596603533` |
| **Status** | 🟢 ATIVA — Strategy 2026 |
| **Campanhas ativas** | Camp 1 ASC R$20/dia (rodando desde 08/06) |
| **Camps PAUSED** | Camp 2 Teste 3:2:2 (R$11/dia) + Camp 3 Retarget WCA (R$9/dia) |
| **Business Manager** | `836285430695962` (Budamix) |
| **Page** | `106066888942641` (Budamix) |
| **Instagram** | `17841466202361418` (budamix.br) — 2.934 seguidores |
| **Catálogo** | `1973158136897277` (Budamix Catálogo) — 23 produtos via feed XML |
| **Pixel + CAPI** | `460889899401645` — operacional com event_id dedup |
| **Moeda** | BRL |
| **Feed XML** | `https://budamix.com.br/feeds/meta-catalog.xml` |

**HERO atual:** IMB501 (Conjunto 5 Potes Redondos de Vidro), R$24,90, 5,0⭐/18 reviews.

**⚠️ Freeze period:** Camp 1 em fase de aprendizado 08/06 → ~22/06. NÃO tocar (mudança >20% reseta).

### 🔴 GB Distribuição (LEGACY — PARADA)

| Campo | Valor |
|---|---|
| **Account ID** | `act_323534883953033` |
| **Status** | 🔴 PARADA em 06/2026 — NÃO operar |
| **Campanhas** | 16 (todas pausadas em Mar/2026, conta inativa desde) |
| **Gasto total histórico** | R$27.432,69 |
| **Business Manager** | `7723008527787239` |
| **App vinculado** | `3582660648568553` (KOBE.OPENCLAW velho) |

**Atenção:** scripts Meta Ads têm guardrail desde 08/06 — refusam executar sem `META_AD_ACCOUNT` explícito, e essa conta NÃO está na whitelist (só Budamix está). Ver `/root/segundo-cerebro/skills/marketing/meta-ads/scripts/`.

**Lookalikes herdadas (INACTIVE):**
- `120220400359220456` — LAL 1% Visitantes Site (~1M pessoas) — operation_status_code 433, não reativável
- `120219003397950456` — LAL 3% Engajados Página (~3M pessoas) — operation_status_code 433, não reativável

### ⚪ Broglio Brinquedos

| Campo | Valor |
|---|---|
| **Account ID** | `act_599689043839914` |
| **Status** | ⚪ Sem campanhas ativas |
| **Notas** | Mapear quando Pedro reativar |

### ⚪ Trades Up

| Campo | Valor |
|---|---|
| **Account ID** | `act_851375860374263` |
| **Status** | ⚪ Sem campanhas ativas |
| **Notas** | Mapear quando Pedro reativar |

---

## App e Token (atualizado 2026-06-08)

| Item | Valor |
|---|---|
| **App ativo** | KOBE.OPENCLAW (`1486886096369858`) — Live mode desde 08/06 |
| **Token tipo** | SYSTEM_USER (permanente, NEVER expira) |
| **System User** | Fat_User_CRM (`61581773210100`) |
| **Token storage** | 1P "OpenClaw" → item "Meta System User Token - Budamix Ads" (id `hxvgwjrdluw4yblo4lbktatoyy`) |
| **Campo no item** | `notesPlain` (CUIDADO: vem com aspas/newline, requer cleanup `sed 's/^"//; s/"$//' \| tr -d '\n'`) |
| **API version** | `v25.0` |

**Token velho** (`Meta Ads API - KOBE.OPENCLAW`, app `3582660648568553`): descontinuado — era long-lived 60 dias, expirou 18/05/2026.

---

## Google Ads

| Campo | Valor |
|---|---|
| **Status** | ❌ Não integrada |
| **Blocker** | Developer Token pendente + OAuth invalid_grant em 26/04 |
| **Customer ID** | A definir |

---

## Notas operacionais

- **Conta primária ativa:** Budamix. Todas análises e recomendações Meta partem dela.
- **GB Distribuição:** legacy, não operar. Histórico preservado pra benchmarks.
- **Demais contas (Broglio, Trades Up):** sem operação no momento.
- **Strategy 2026:** estrutura ativa Budamix substitui playbook antigo de 4 campanhas. Detalhes em `~/segundo-cerebro/projects/budamix-meta-ads.md`.
