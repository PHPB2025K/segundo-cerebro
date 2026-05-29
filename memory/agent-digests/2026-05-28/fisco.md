---
title: "Digest Fisco — 2026-05-28"
date: 2026-05-28
agent: fisco
status: active
---

# Digest Fisco — 2026-05-28

## Resumo executivo
- Sem NF-e real, draft, distribuição entre CNPJs, conciliação fiscal ou novo monitor de Simples/faturamento.
- Matriz Bling OK nas execuções completas; Filial segue bloqueada com HTTP 403 “empresa inativa”.

## Decisões novas
- Nenhuma decisão fiscal nova.

## Lições / riscos
- Filial Bling inacessível permanece bloqueio para fluxos Filial → Simples e testes completos Matriz + Filial.
- Alerta WhatsApp do refresh segue falhando com HTTP 403, reduzindo visibilidade automática.
- Cron ainda teve rodada sem validação útil e outra com resposta final abortada após capturar resultado.

## Pendências novas ou alteradas
- Reconfirmadas: corrigir Bling Filial, estabilizar refresh automático e validar canal de alerta WhatsApp.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco atualizada.
- Digest de Fisco preparado para Kobe.

## Kobe precisa saber
- Nada novo de FOUR/Suellen ou de emissão fiscal; risco principal continua sendo Filial Bling inativa há quatorze dias.

## Possível decisão do Pedro
- Se ainda não acionado, priorizar regularização do status/vínculo/token da Filial no Bling antes de qualquer emissão/draft dependente da Filial.
