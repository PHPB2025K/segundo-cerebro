---
title: "Digest Fisco — 2026-06-07"
date: 2026-06-07
agent: fisco
status: active
---

# Digest Fisco — 2026-06-07

## Resumo executivo
- Dia sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novos dados de Simples/faturamento.
- Refresh Bling teve cinco checagens úteis em BRT: Matriz OK em todas; Filial seguiu bloqueada com HTTP 403 “empresa inativa”.
- O alerta WhatsApp do refresh também falhou com HTTP 403 nas checagens úteis.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo fiscal 90/10 segue vigente; qualquer alteração continua exigindo validação FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- Filial Bling chega a 24 dias de bloqueio recorrente; tratar como problema formal de status/vínculo/acesso, não oscilação.
- Matriz está recuperada nas checagens recentes, mas ainda precisa de teste controlado antes de qualquer operação/draft.
- Houve bloqueio inicial por política/allowlist em uma rodada, com rerun útil na mesma janela; risco de confiabilidade da automação permanece.

## Pendências novas ou alteradas
- Resolver HTTP 403 da Filial antes de qualquer fluxo Filial → Simples.
- Validar estabilidade da Matriz em teste controlado antes de operação/draft.
- Corrigir canal de alerta WhatsApp do refresh.
- Ajustar execução automática para evitar bloqueios/lacunas por política/allowlist ou timeout.

## Entregas / ações executadas
- Consolidação diária do Fisco atualizada.
- Memória longa, sessão diária, decisões/lições/pendências próprias do Fisco revisadas.
- Runs internos do refresh Bling absorvidos na memória do Fisco.

## Kobe precisa saber
- Nada crítico novo além do bloqueio persistente: Filial Bling segue impedindo fluxos de NF interna Filial → Simples.
- Não houve emissão de nota, draft fiscal, decisão da FOUR/Suellen ou alteração no modelo 90/10 hoje.

## Possível decisão do Pedro
- Se ainda não tratado, priorizar correção do acesso/status da Filial no Bling e do canal de alerta do refresh.
