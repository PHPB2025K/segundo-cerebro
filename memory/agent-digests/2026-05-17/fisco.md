---
title: "Digest Fisco — 2026-05-17"
date: 2026-05-17
agent: fisco
status: active
---

# Digest Fisco — 2026-05-17

## Resumo executivo
- Dia sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novo monitor de Simples.
- Atividade relevante: refresh OAuth do Bling manteve Matriz OK quando rodou, mas Filial continuou falhando com HTTP 403 por empresa inativa.

## Decisões novas
- Nenhuma decisão fiscal nova.

## Lições / riscos
- 🔴 Risco operacional persistente: Bling Filial segue inacessível e bloqueia qualquer fluxo fiscal dependente da Filial.
- ⚠️ Risco de automação: uma execução foi bloqueada por allowlist; em outras, o alerta WhatsApp falhou com HTTP 403.

## Pendências novas ou alteradas
- Reconfirmar/corrigir status ou vínculo do token da empresa Filial no Bling.
- Estabilizar política de execução do refresh e canal de alerta WhatsApp.

## Entregas / ações executadas
- Memória diária do Fisco consolidada para 2026-05-17.
- Pendências, decisões e lições próprias do Fisco atualizadas.

## Kobe precisa saber
- A Filial no Bling continua bloqueante para NF interna Filial → Simples e para qualquer teste completo Matriz + Filial.
- Não houve alteração fiscal, emissão, draft ou novo dado de Simples no dia.

## Possível decisão do Pedro
- Acionar responsável pelo Bling para regularizar a empresa Filial vinculada ao token e confirmar o canal de alerta do refresh.
