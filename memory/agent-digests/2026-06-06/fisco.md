---
title: "Digest Fisco — 2026-06-06"
date: 2026-06-06
agent: fisco
status: active
---

# Digest Fisco — 2026-06-06

## Resumo executivo
- Refresh Bling rodou com resultado fiscal útil nas janelas de 04:17, 09:17, 14:17 e 19:17 BRT.
- Matriz conectou em todas as execuções úteis observadas; Filial segue bloqueada com HTTP 403 “empresa inativa”.
- Sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novos dados de Simples/faturamento.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo 90/10 permanece vigente e qualquer mudança segue exigindo validação da FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- Filial completou 23 dias de bloqueio por HTTP 403; tratar como bloqueio operacional formal, não oscilação.
- Matriz está em recuperação operacional recente, mas ainda exige teste controlado antes de qualquer operação/draft.
- Alerta WhatsApp do refresh continua falhando com HTTP 403, reduzindo visibilidade automática.
- Houve bloqueio inicial por política/allowlist na janela de 19:17 BRT, mas o rerun capturou resultado fiscal útil.

## Pendências novas ou alteradas
- Reconfirmada pendência crítica: corrigir status/vínculo/acesso da Filial no Bling antes de qualquer fluxo Filial → Simples.
- Reconfirmada pendência: validar estabilidade da Matriz com teste controlado antes de operação/draft.
- Reconfirmada pendência: corrigir canal de alerta WhatsApp e reduzir bloqueios/lacunas de automação do refresh.

## Entregas / ações executadas
- Consolidação diária da memória própria do Fisco atualizada.
- Sessão diária do Fisco registrada com eventos em BRT.
- Decisões, lições e pendências próprias revisadas.

## Kobe precisa saber
- Bloqueio fiscal principal permanece na Filial do Bling; não há base segura para drafts/emissões dependentes da Filial.
- Se houver necessidade operacional de NF interna, primeiro precisa corrigir Filial e rodar teste controlado Matriz + Filial.
- Nada novo foi validado pela FOUR/Suellen hoje.

## Possível decisão do Pedro
- Priorizar correção do cadastro/vínculo/acesso da Filial no Bling e validação do canal de alerta, se o fluxo de NF interna for necessário no curto prazo.
