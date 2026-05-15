---
title: "Agent Digests — Protocolo de Consolidação em Camadas"
created: 2026-05-15
type: memory-protocol
status: active
tags:
  - memory
  - agents
  - consolidation
---

# Agent Digests — Protocolo de Consolidação em Camadas

## Objetivo

Separar a consolidação de memória por agente direto do Kobe, reduzindo timeout e mantendo Kobe consciente do estado do time sem precisar varrer toda a memória interna de cada agente.

## Agentes diretos do Kobe

Somente estes agentes escrevem digest diário para o Kobe:

- Trader
- Spark
- Builder
- Fisco
- RH

Subagentes, workers, analysts internos e tarefas temporárias NÃO escrevem digest direto para Kobe. O agente-pai absorve esses resultados na própria memória e só sobe o que importa no digest.

## Fonte canônica

- Memória completa: fica dentro do workspace/memória do próprio agente.
- Digest para Kobe: fica em `memory/agent-digests/YYYY-MM-DD/<agent>.md`.
- Kobe lê apenas os digests dos agentes diretos e o próprio contexto.
- Kobe não edita memória interna de Trader/Spark/Builder/Fisco/RH durante a consolidação diária.

## Template obrigatório do digest

Cada digest diário deve usar esta estrutura:

```md
---
title: "Digest <Agente> — YYYY-MM-DD"
date: YYYY-MM-DD
agent: <agent-id>
status: active|quiet|error
---

# Digest <Agente> — YYYY-MM-DD

## Resumo executivo
- ...

## Decisões novas
- Nenhuma, ou bullets específicos.

## Lições / riscos
- Nenhuma, ou bullets específicos.

## Pendências novas ou alteradas
- Nenhuma, ou bullets específicos.

## Entregas / ações executadas
- Nenhuma, ou bullets específicos.

## Kobe precisa saber
- Nada crítico, ou bullets objetivos.

## Possível decisão do Pedro
- Nenhuma, ou bullets objetivos.
```

## Regras

- Digest é resumo do resumo, não transcrição.
- Não incluir logs brutos, comandos, paths internos, tokens ou credenciais.
- Não duplicar conteúdo extenso da memória do agente.
- Se o agente não teve atividade relevante, criar digest `status: quiet` com uma frase clara.
- Se houve erro de consolidação, criar digest `status: error` com causa resumida e impacto.
- Todos os horários visíveis devem estar em BRT.

## Pipeline diário

- 22:45 BRT — Trader
- 22:55 BRT — Spark
- 23:05 BRT — Builder
- 23:15 BRT — Fisco
- 23:25 BRT — RH
- 23:45 BRT — Kobe consolida próprio dia + digests dos agentes diretos
- 00:05 BRT — Commit/index/sanity check do pipeline
