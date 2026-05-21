---
title: "Digest Fisco — 2026-05-20"
date: 2026-05-20
agent: fisco
status: active
---

# Digest Fisco — 2026-05-20

## Resumo executivo
- Refresh Bling segue em falha fiscal-operacional: Matriz OK nas execuções completas, Filial com HTTP 403 por empresa vinculada ao token inativa.
- Não houve NF-e real, draft, distribuição entre CNPJs, conciliação fiscal nem novo monitor Simples.

## Decisões novas
- Nenhuma decisão fiscal nova.

## Lições / riscos
- HTTP 403 da Filial persiste pelo sexto dia; tratar como bloqueio formal, não oscilação.
- Alerta WhatsApp do refresh também falha com HTTP 403, reduzindo visibilidade automática.
- Uma rodada do cron abortou antes de resultado fiscal útil; há risco de automação incompleta.

## Pendências novas ou alteradas
- Bling Filial: corrigir status/vínculo/token antes de qualquer operação dependente da Filial.
- Refresh Bling: estabilizar execução para evitar abortos/timeouts.
- Validar canal de alerta WhatsApp.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco atualizada.
- Digest para Kobe preparado às 23:15 BRT.

## Kobe precisa saber
- Fluxos Filial → Simples continuam bloqueados até a Filial voltar a conectar no Bling e passar por teste controlado.
- Matriz não é o bloqueio principal nas execuções completas do dia.

## Possível decisão do Pedro
- Priorizar correção da empresa Filial no Bling e do canal de alerta, caso haja expectativa de emissão/draft fiscal nos próximos dias.
