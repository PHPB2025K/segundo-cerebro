# Shadow Runs Summary — Phase 5

**Executado em:** 2026-05-14
**Modo:** --shadow (fallback deterministico, sem LLM)
**Runner:** `scripts/daily-sales-analyst-runner.py`

---

## Resumo Executivo

| Data | Package | Data Readiness | Global Status | Failure | send_real | Artefatos |
|------|---------|----------------|---------------|---------|-----------|-----------|
| 2026-05-11 | Gerado nesta fase | DADOS_OK | APPROVED_WITH_REMARKS | false | false | 24 (8x3) |
| 2026-05-12 | Regenerado nesta fase* | DADOS_OK | APPROVED_WITH_REMARKS | false | false | 24 (8x3) |
| 2026-05-13 | Pre-existente | NOT_READY | BLOCKED | layer0 | false | 24 (8x3) |

*O package de 2026-05-12 existia em schema antigo (sem `data_readiness`). Foi regenerado pelo Data Builder v1.0 nesta fase.

---

## Detalhes por Data

### 2026-05-11 (Domingo)

**Status:** APPROVED_WITH_REMARKS — Pipeline executou completamente.

| Recipient | Plataforma | Status | send_allowed | QA Verdict |
|-----------|------------|--------|--------------|------------|
| lucas | shopee | APPROVED_WITH_REMARKS | false | APPROVED_WITH_REMARKS |
| yasmin | mercado_livre | APPROVED_WITH_REMARKS | false | APPROVED_WITH_REMARKS |
| leonardo | amazon | APPROVED_WITH_REMARKS | false | APPROVED_WITH_REMARKS |

**Metricas chave:**
- Lucas (Shopee): 135 pedidos, R$ 6.506,57 GMV, 21 cancelamentos
- Yasmin (ML): 92 pedidos, R$ 3.664,91 GMV, 3 cancelamentos
- Leonardo (Amazon): 30 pedidos, R$ 1.152,80 GMV, 8 cancelamentos

**Package gerado por:** Data Builder v1.0 (gerado nesta fase, nao existia previamente)

### 2026-05-12 (Segunda-feira)

**Status:** APPROVED_WITH_REMARKS — Pipeline executou completamente.

| Recipient | Plataforma | Status | send_allowed | QA Verdict |
|-----------|------------|--------|--------------|------------|
| lucas | shopee | APPROVED_WITH_REMARKS | false | APPROVED_WITH_REMARKS |
| yasmin | mercado_livre | APPROVED_WITH_REMARKS | false | APPROVED_WITH_REMARKS |
| leonardo | amazon | APPROVED_WITH_REMARKS | false | APPROVED_WITH_REMARKS |

**Metricas chave:**
- Lucas (Shopee): 118 pedidos, R$ 5.378,44 GMV, 13 cancelamentos
- Yasmin (ML): 91 pedidos, R$ 4.081,49 GMV, 4 cancelamentos
- Leonardo (Amazon): 30 pedidos, R$ 1.157,57 GMV, 1 cancelamento

**Observacao:** Package original (schema antigo) nao tinha `data_readiness` → runner tratava como NOT_READY por default. Regenerado com Data Builder v1.0 → DADOS_OK. Documentado em `issues-found.md`.

### 2026-05-13 (Terca-feira)

**Status:** BLOCKED — Pipeline bloqueada por Data Readiness NOT_READY.

| Recipient | Plataforma | Status | send_allowed | QA Verdict |
|-----------|------------|--------|--------------|------------|
| lucas | shopee | BLOCKED | false | BLOCKED |
| yasmin | mercado_livre | BLOCKED | false | BLOCKED |
| leonardo | amazon | BLOCKED | false | BLOCKED |

**Motivos do bloqueio:**
1. `volume_band_shopee-budamix-oficial-2`: Orders 14 vs avg30 35.0 = -60.0%
2. `volume_band_amazon`: Orders 46 vs avg30 27.3 = +68.5%

**Comportamento:** Correto. O runner bloqueou a pipeline e gerou artefatos BLOCKED como placeholders para auditoria. Nenhum envio real.

---

## Validacoes Globais

- [x] `send_real_allowed=false` em TODOS os manifests (3/3)
- [x] Nenhum Slack enviado
- [x] Nenhum cron alterado
- [x] Todos os manifests sao JSON validos
- [x] Artefatos gerados por recipient (8 por recipient x 3 recipients x 3 datas = 72 total)
- [x] Bloqueio correto em 2026-05-13 (NOT_READY)
- [x] Aprovacao correta em 2026-05-11 e 2026-05-12 (DADOS_OK)

---

## Comandos Executados

```bash
# Gerar package faltante
python3 scripts/daily-sales-data-builder.py 2026-05-11 --write
python3 scripts/daily-sales-data-builder.py 2026-05-12 --write  # regenerado

# Shadow runs
python3 scripts/daily-sales-analyst-runner.py 2026-05-11 --shadow
python3 scripts/daily-sales-analyst-runner.py 2026-05-12 --shadow
python3 scripts/daily-sales-analyst-runner.py 2026-05-13 --shadow
```
