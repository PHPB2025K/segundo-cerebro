---
title: "Digest Fisco — 2026-06-13"
date: 2026-06-13
agent: fisco
status: active
---

# Digest Fisco — 2026-06-13

## Resumo executivo
- Dia sem emissão de NF-e real, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novos dados de faturamento/Simples.
- Refresh Bling teve cinco execuções úteis em BRT: Matriz OK em todas; Filial falhou em todas com HTTP 403 “empresa inativa”.
- Alerta WhatsApp do refresh também falhou com HTTP 403 em todas as execuções úteis observadas.

## Decisões novas
- Nenhuma decisão fiscal nova.
- Modelo fiscal 90/10 permanece vigente; qualquer mudança continua exigindo validação FOUR/Suellen via Kobe/Pedro.

## Lições / riscos
- Filial Bling segue bloqueio operacional para NF interna Filial → Simples e para testes completos Matriz + Filial.
- Persistência por trinta dias do erro HTTP 403 da Filial reforça problema de status/vínculo/acesso, não oscilação transitória.
- Matriz permanece operacional nas checagens do dia, mas ainda exige teste controlado antes de qualquer operação/draft.
- Falha do alerta WhatsApp reduz visibilidade automática sobre erro fiscal-operacional.

## Pendências novas ou alteradas
- Reconfirmada: resolver Bling Filial HTTP 403 antes de qualquer emissão/draft dependente da Filial.
- Reconfirmada: validar estabilidade da Matriz com teste controlado antes de operação/draft.
- Reconfirmada: corrigir canal de alerta WhatsApp do refresh.
- Sem novas pendências fiscais adicionadas.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco atualizada.
- Digest diário para Kobe preparado.
- Runs internos do refresh Bling absorvidos na memória do Fisco.

## Kobe precisa saber
- Nada para ação fiscal imediata além do bloqueio já conhecido: Filial Bling continua indisponível para fluxos Filial → Simples.
- Não houve NF-e emitida/pendente, decisão fiscal nova, validação da FOUR/Suellen ou mudança em Simples/faturamento hoje.

## Possível decisão do Pedro
- Nenhuma nova; se houver urgência para NF interna/draft, Pedro/Kobe precisam priorizar regularização do acesso/status da Filial no Bling e correção do alerta WhatsApp.
