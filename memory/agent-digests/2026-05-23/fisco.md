---
title: "Digest Fisco — 2026-05-23"
date: 2026-05-23
agent: fisco
status: active
---

# Digest Fisco — 2026-05-23

## Resumo executivo
- Refresh OAuth do Bling segue em falha pelo 9º dia: Matriz OK nas execuções completas; Filial continua com HTTP 403 por empresa vinculada ao token inativa.
- Nenhuma NF-e real emitida, nenhum draft, nenhuma distribuição entre CNPJs, nenhuma conciliação fiscal e nenhum novo monitor Simples consolidado.
- Persistem falha recorrente no alerta WhatsApp e falhas de confiabilidade do cron por bloqueio de aprovação/allowlist e sessão abortada após captura parcial do resultado.

## Decisões novas
- Nenhuma decisão fiscal nova.

## Lições / riscos
- Filial Bling permanece bloqueio operacional para qualquer fluxo Filial → Simples.
- Persistência por 9 dias confirma problema formal de status/vínculo/token, não oscilação transitória.
- Canal de alerta WhatsApp também falha com HTTP 403, reduzindo visibilidade automática.
- Rodadas bloqueadas por política/allowlist devem ser tratadas como ausência de validação fiscal útil.

## Pendências novas ou alteradas
- Reconfirmar correção do status/vínculo/token da Filial no Bling antes de qualquer emissão/draft dependente da Filial.
- Estabilizar cron do refresh: tratar allowlist/política de aprovação, timeouts e resposta consolidada.
- Validar o canal WhatsApp de alerta do refresh.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco atualizada com eventos do dia em BRT.
- Digest preparado para Kobe.

## Kobe precisa saber
- Risco crítico permanece: a Filial no Bling está indisponível; não liberar operação fiscal dependente da Filial até correção e teste controlado.
- A Matriz segue OK nas execuções completas, então o bloqueio está concentrado na Filial e na confiabilidade do monitoramento/alerta.

## Possível decisão do Pedro
- Acionar responsável pelo Bling para reativar/corrigir a empresa Filial vinculada ao token e validar o canal de alerta, se ainda não houver dono definido.
