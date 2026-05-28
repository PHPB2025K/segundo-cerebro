---
title: "Digest Fisco — 2026-05-27"
date: 2026-05-27
agent: fisco
status: active
---

# Digest Fisco — 2026-05-27

## Resumo executivo
- Dia sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novos dados de Simples/faturamento.
- Refresh Bling manteve padrão crítico: Matriz OK nas execuções completas; Filial bloqueada por HTTP 403 “empresa vinculada ao token está inativa”.
- Alertas WhatsApp do refresh seguem falhando com HTTP 403; houve rodadas sem validação útil por bloqueio/aborto da automação.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo fiscal 90/10 permanece vigente; qualquer alteração exige validação FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- Filial Bling segue bloqueio operacional para NF interna Filial → Simples e para teste completo Matriz + Filial.
- Falha do alerta WhatsApp reduz visibilidade automática do problema.
- Bloqueios por política/allowlist e abortos seguem sendo risco operacional separado da falha fiscal da Filial.

## Pendências novas ou alteradas
- Reconfirmada prioridade alta: resolver Bling Filial HTTP 403 antes de qualquer emissão/draft dependente da Filial.
- Reconfirmada prioridade alta: estabilizar cron de refresh Bling para evitar rodadas sem validação útil.
- Reconfirmada prioridade média: corrigir canal WhatsApp de alerta do refresh.

## Entregas / ações executadas
- Consolidação diária do Fisco atualizada.
- Pendências, decisões e lições próprias do Fisco revisadas.
- Workers internos de refresh Bling do dia absorvidos na memória do Fisco.

## Kobe precisa saber
- Nada novo de NF-e ou faturamento; o risco central continua sendo a Filial inativa no Bling.
- Enquanto a Filial não for corrigida e testada, qualquer fluxo fiscal dependente dela deve permanecer parado.

## Possível decisão do Pedro
- Acionar responsável do Bling/cadastro da Filial para corrigir status/vínculo/token e liberar teste controlado Matriz + Filial.
