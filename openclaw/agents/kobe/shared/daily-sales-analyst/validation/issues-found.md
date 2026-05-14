# Issues Found — Phase 5

**Data:** 2026-05-14

---

## Issue 1: Package 2026-05-12 em schema antigo (sem data_readiness)

**Severidade:** Media
**Tipo:** Incompatibilidade de schema

O package de 2026-05-12 existia em schema antigo (pre-Data Builder v1.0) sem o campo `data_readiness`. O runner interpreta ausencia desse campo como `NOT_READY` por default, bloqueando a pipeline mesmo quando os dados eram validos.

**Impacto:** Shadow run inicial de 2026-05-12 retornou BLOCKED indevidamente.
**Resolucao:** Regenerado o package com `daily-sales-data-builder.py 2026-05-12 --write`. Resultado: DADOS_OK.
**Status:** RESOLVIDO nesta fase.

---

## Issue 2: Fallback deterministico — limitacao estrutural

**Severidade:** Alta (para rollout)
**Tipo:** Limitacao de design

O runner opera sem LLM. Camadas 1-6 sao placeholders que extraem dados do package sem analise. Isso significa:
- Profundidade: 2/5
- Utilidade para destinatario: 2/5
- Sem prioridades acionaveis
- Sem insight estrategico
- Sem formatacao Slack final

**Impacto:** Runner nao pode ser usado para envio real sem integracao LLM.
**Status:** ESPERADO — fallback deterministico e by design para Fase 4. Sera resolvido na Fase 6 com integracao LLM.

---

## Issue 3: Sync freshness nao mensuravel

**Severidade:** Baixa
**Tipo:** Metrica ausente

O check `sync_freshness` retorna `not_measured` em todas as datas. O schema do banco nao expoe timestamp de ultima sincronizacao por plataforma.

**Impacto:** Nao e possivel validar se os dados sao "frescos" (ex: sync das 06:00 vs 09:00). Isso afeta a validacao 06:50 vs 09:00 planejada.
**Status:** ABERTO — requer mudanca na infraestrutura de sync (fora do escopo DSA).

---

## Issue 4: Threshold volume_band pode ser muito sensivel

**Severidade:** Media
**Tipo:** Calibracao

2026-05-13 foi bloqueado por:
- shopee-budamix-oficial-2: -60% (14 vs 35 avg30)
- amazon: +68.5% (46 vs 27.3 avg30)

O bloqueio de Amazon com +68.5% pode ser um dia legitimamente bom (nao anomalia). A decisao de bloquear toda a pipeline por volume anomalo em UMA conta afeta TODOS os recipients.

**Questao:** O threshold atual e adequado? Um spike positivo em Amazon deveria bloquear a analise de Shopee para Lucas?

**Status:** ABERTO — requer decisao de Pedro/Kobe sobre:
1. Separar bloqueio por recipient (nao global)?
2. Ajustar threshold para spikes positivos?
3. Tratar spike positivo como "DADOS_PARCIAIS" em vez de NOT_READY?

---

## Issue 5: Bloqueio global vs per-recipient

**Severidade:** Media
**Tipo:** Arquitetura

Atualmente, se ANY volume_band falha, TODA a pipeline e bloqueada para TODOS os recipients. Isso significa que uma anomalia em Amazon bloqueia o report de Shopee para Lucas, mesmo que os dados de Shopee estejam perfeitos.

O TRADER-CONTRACT.md define status per-recipient, mas o Layer 0 decide globalmente.

**Status:** ABERTO — decisao arquitetural para Fase 6.

---

## Issue 6: Packages antigos incompativeis

**Severidade:** Baixa
**Tipo:** Migracao

Packages gerados antes do Data Builder v1.0 nao possuem `data_readiness`, `schema_version`, ou checks estruturados. Se o runner encontrar um destes, trata como NOT_READY.

**Status:** RESOLVIDO para as 3 datas de teste. Para datas futuras, o Data Builder sempre gera no formato correto. Packages historicos antigos precisam ser regenerados se necessarios.

---

## Issue 7: Falta comparacao 06:50 vs 09:00

**Severidade:** Baixa
**Tipo:** Validacao pendente

O briefing menciona comparacao entre packages gerados em horarios diferentes (06:50 vs 09:00). Sem `sync_freshness`, essa comparacao e limitada a diferencas numericas entre dois packages. Script auxiliar criado (`daily-sales-compare-packages.py`) para facilitar comparacao futura.

**Status:** PARCIAL — script criado, mas validacao real depende de packages gerados em horarios diferentes (nao disponiveis nesta fase).
