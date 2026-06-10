---
title: "Digest Fisco — 2026-06-09"
date: 2026-06-09
agent: fisco
status: active
---

# Digest Fisco — 2026-06-09

## Resumo executivo
- Dia sem NF-e real, sem draft, sem distribuição entre CNPJs, sem conciliação fiscal e sem novo monitor de Simples/faturamento.
- Bling Matriz respondeu OK nas quatro execuções úteis observadas; Filial continuou bloqueada com HTTP 403 “empresa inativa”.
- A rodada das 12:17 BRT ficou sem validação fiscal útil por bloqueio/timeout.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo fiscal 90/10 permanece vigente; qualquer mudança continua exigindo validação da FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- Filial no Bling completa 26 dias de HTTP 403 “empresa inativa”; tratar como bloqueio formal de status/vínculo/acesso, não oscilação.
- Matriz está em recuperação operacional, mas ainda exige teste controlado antes de qualquer operação/draft.
- Alertas WhatsApp do refresh seguem falhando com HTTP 403, reduzindo visibilidade automática.
- Allowlist/timeout ainda cria lacunas de monitoramento; resultado fiscal capturado antes de aborto pode ser consolidado, mas rodada sem retorno não deve ser interpretada.

## Pendências novas ou alteradas
- Reconfirmado: resolver Bling Filial antes de qualquer NF interna Filial → Simples.
- Reconfirmado: validar estabilidade da Matriz antes de operação/draft.
- Reconfirmado: corrigir alerta WhatsApp e confiabilidade do cron de refresh.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco atualizada.
- Digest Fisco preparado para Kobe.

## Kobe precisa saber
- Nada novo em emissão fiscal, mas o bloqueio da Filial continua crítico para qualquer fluxo de NF interna.
- Houve lacuna na rodada das 12:17 BRT; não usar essa rodada como evidência de recuperação ou piora.

## Possível decisão do Pedro
- Nenhuma hoje, salvo priorizar correção do status/vínculo da Filial no Bling e validação do canal de alerta.
