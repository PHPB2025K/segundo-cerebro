---
title: "Digest Fisco — 2026-06-02"
date: 2026-06-02
agent: fisco
status: active
---

# Digest Fisco — 2026-06-02

## Resumo executivo
- Sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novo dado de Simples/faturamento.
- Risco Bling agravou: Filial segue com HTTP 403 “empresa inativa” e Matriz também retornou HTTP 403 em duas execuções úteis do dia.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo 90/10 segue vigente; qualquer alteração continua exigindo validação da FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- HTTP 403 deixou de estar isolado na Filial; Matriz precisa ser tratada como potencialmente bloqueada até teste controlado confirmar recuperação.
- Alerta WhatsApp do refresh segue falhando com HTTP 403, reduzindo visibilidade automática.
- Houve uma rodada bloqueada por approvals/allowlist e uma com fechamento abortado por timeout após captura do resultado fiscal.

## Pendências novas ou alteradas
- Nova pendência alta: investigar HTTP 403 da Matriz observado às 13:33 e 18:33 BRT.
- Mantidas: corrigir Bling Filial, estabilizar cron de refresh, corrigir alerta WhatsApp e executar teste controlado Matriz + Filial após normalização.

## Entregas / ações executadas
- Memória diária do Fisco consolidada.
- Decisions, lessons e pending próprios revisados.
- Workers internos do refresh absorvidos na memória do Fisco.

## Kobe precisa saber
- Possível bloqueio simultâneo de Matriz e Filial no Bling é o ponto crítico fiscal-operacional do dia.
- Nenhuma emissão fiscal deve avançar sem validação de conectividade Matriz + Filial e sem aprovação explícita quando aplicável.

## Possível decisão do Pedro
- Acionar suporte/conta Bling para verificar status/vínculo das empresas Matriz e Filial, priorizando desbloqueio antes de qualquer operação fiscal dependente do Bling.
