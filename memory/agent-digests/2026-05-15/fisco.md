---
title: "Digest Fisco — 2026-05-15"
date: 2026-05-15
agent: fisco
status: active
---

# Digest Fisco — 2026-05-15

## Resumo executivo
- Dia sem NF-e emitida, sem drafts, sem distribuição entre CNPJs, sem conciliação fiscal e sem novo monitor de Simples.
- Atividade relevante: refresh OAuth do Bling falhou de forma recorrente para a Filial; Matriz ficou OK nas execuções completas.

## Decisões novas
- Nenhuma decisão fiscal nova.

## Lições / riscos
- 🔴 Risco operacional: Bling Filial retorna HTTP 403 com indicação de empresa/token inativo; isso bloqueia fluxos futuros de NF interna Filial → Simples.
- Job de refresh teve sinais de fragilidade: uma execução bloqueada por política de aprovação em cron, uma abortada antes de resultado completo e alerta WhatsApp com HTTP 403.

## Pendências novas ou alteradas
- Corrigir status/token OAuth da Filial no Bling antes de qualquer operação fiscal dependente da Filial.
- Ajustar cron de refresh Bling para não depender de aprovação interativa e reduzir abortos/timeout.
- Validar canal de alerta WhatsApp do refresh Bling.

## Entregas / ações executadas
- Consolidação diária da memória do Fisco executada.
- Memória diária, decisões, lições e pendências próprias do Fisco atualizadas.

## Kobe precisa saber
- O ponto crítico novo/recorrente é a Filial do Bling inativa/403; sem isso resolvido, Fisco não deve avançar para drafts/emissões envolvendo Filial.

## Possível decisão do Pedro
- Nenhuma decisão fiscal hoje; pode ser necessário acionar responsável do Bling/conta para reativar ou corrigir vínculo da Filial.
