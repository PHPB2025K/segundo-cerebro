---
title: "Digest Fisco — 2026-06-05"
date: 2026-06-05
agent: fisco
status: active
---

# Digest Fisco — 2026-06-05

## Resumo executivo
- Dia sem NF-e real, sem draft, sem distribuição entre CNPJs, sem conciliação fiscal e sem novos dados de Simples/faturamento.
- Refresh Bling confirmou Matriz OK nas execuções úteis observadas, mas Filial segue bloqueada por HTTP 403 “empresa inativa”.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo 90/10 permanece vigente; qualquer alteração exige validação FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- Filial Bling está bloqueada há 22 dias; isso impede fluxos Filial → Simples e testes completos Matriz + Filial.
- Alerta WhatsApp do refresh também falhou com HTTP 403, reduzindo visibilidade automática.
- Houve uma rodada sem validação fiscal útil por bloqueio de política/allowlist.

## Pendências novas ou alteradas
- Resolver HTTP 403 da Filial antes de qualquer emissão/draft dependente dela.
- Validar estabilidade da Matriz com teste controlado antes de operação/draft.
- Corrigir alerta WhatsApp e política/allowlist para evitar lacunas de monitoramento.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco atualizada.
- Digest do Fisco preparado para Kobe.

## Kobe precisa saber
- Nada crítico novo além da continuidade do bloqueio: Filial segue inacessível e impede operação fiscal interna dependente do Bling Filial.

## Possível decisão do Pedro
- Nenhuma decisão fiscal hoje; se operação interna com NF-e estiver próxima, Pedro/Kobe precisam priorizar regularização da Filial no Bling antes do fluxo.
