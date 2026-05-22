---
title: "Digest Fisco — 2026-05-21"
date: 2026-05-21
agent: fisco
status: active
---

# Digest Fisco — 2026-05-21

## Resumo executivo
- Refresh OAuth do Bling segue em falha parcial: Matriz OK nas execuções completas; Filial continua com HTTP 403 por empresa vinculada ao token inativa.
- Sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novo monitor Simples.

## Decisões novas
- Nenhuma decisão fiscal nova.

## Lições / riscos
- HTTP 403 da Filial persiste por sete dias e deve seguir tratado como bloqueio formal, não oscilação.
- Alerta WhatsApp do refresh também falha com HTTP 403, reduzindo visibilidade automática.
- Algumas execuções tiveram bloqueio inicial por allowlist ou abortaram antes da resposta final, mantendo risco de automação incompleta.

## Pendências novas ou alteradas
- Reconfirmada pendência crítica: corrigir status/vínculo/token da Filial no Bling antes de qualquer operação fiscal dependente da Filial.
- Reconfirmada pendência: validar canal de alerta WhatsApp do refresh.
- Reconfirmada pendência: estabilizar execução do cron para evitar bloqueios e sessões sem resposta consolidada.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco executada às 23:15 BRT.
- Digest diário preparado para Kobe.

## Kobe precisa saber
- Qualquer fluxo de NF interna Filial → Simples permanece bloqueado até correção e teste controlado da Filial no Bling.
- Matriz segue estável; o problema operacional está concentrado na Filial, nos alertas e na confiabilidade do cron.

## Possível decisão do Pedro
- Priorizar correção do acesso/status da empresa Filial no Bling se houver previsão de emissão interna ou teste completo de NF-e.
