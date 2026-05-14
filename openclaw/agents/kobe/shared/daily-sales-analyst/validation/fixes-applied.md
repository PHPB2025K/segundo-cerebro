# Fixes Applied — Phase 5

**Data:** 2026-05-14

---

## Fix 1: Regeneracao do package 2026-05-12

**Issue:** Package em schema antigo sem `data_readiness`.
**Acao:** Regenerado via `python3 scripts/daily-sales-data-builder.py 2026-05-12 --write`.
**Resultado:** Package agora em schema v1.0 com data_readiness=DADOS_OK.
**Risco:** Nenhum — Data Builder e deterministico e idempotente.

---

## Fix 2: Geracao do package 2026-05-11

**Issue:** Package nao existia para 2026-05-11.
**Acao:** Gerado via `python3 scripts/daily-sales-data-builder.py 2026-05-11 --write`.
**Resultado:** Package gerado com data_readiness=DADOS_OK.
**Risco:** Nenhum.

---

## Fix 3: Script auxiliar de comparacao de packages

**Issue:** Briefing solicita validacao 06:50 vs 09:00.
**Acao:** Criado `scripts/daily-sales-compare-packages.py` para comparar dois packages da mesma data.
**Resultado:** Script validado com `py_compile`. Compara totais, cancelamentos, e top produtos.
**Risco:** Nenhum — script read-only, nao modifica dados.

---

## Fixes NAO aplicados (fora do escopo)

Os seguintes ajustes foram identificados mas NAO aplicados nesta fase por serem mudancas estruturais:

1. **Separar bloqueio per-recipient** — Requer mudanca no Data Builder e no runner. Fase 6.
2. **Ajustar threshold de volume_band** — Requer decisao de Pedro. Fase 6.
3. **Implementar sync_freshness** — Requer mudanca na infraestrutura de sync. Fora do escopo DSA.
4. **Integrar LLM** — Fase 6.
