---
title: "BOOTSTRAP"
created: 2026-04-14
type: boot-sequence
agent: kobe
status: active
tags:
  - agent/kobe
---

# BOOTSTRAP.md — Bootstrap Operacional + Recuperação de Contexto

_Arquivo de bootstrap para sessões do Kobe._

## Startup obrigatório

No início de cada sessão principal:
1. Ler `SOUL.md`
2. Ler `USER.md`
3. Ler `MEMORY.md`
4. Ler `memory/sessions/YYYY-MM-DD.md` de hoje e ontem
5. Ler `memory/pending.md`
6. Se houver indício de contexto fraco, conferir `BOOT.md` e este arquivo

## Sinais de contexto degradado

Tratar como contexto degradado se ocorrer qualquer um destes sintomas:
- perda de continuidade após troca de modelo
- respostas genéricas apesar de memória existente
- baixa aderência a decisões, preferências ou projetos ativos
- repetição de erros já resolvidos
- retrieval semântico encontrando contexto irrelevante ou incompleto

## Playbook pós-troca de modelo

### Etapa 1 — Reindexação forçada
Executar:
- `openclaw memory index --force`

Objetivo:
- reprocessar arquivos de memória
- recriar embeddings
- limpar ruído de índice antigo
- recalibrar retrieval para o padrão de uso do modelo atual

### Etapa 2 — Warm-up antes de tarefa crítica
Nos primeiros minutos após a troca:
- reapresentar projetos ativos
- reforçar decisões permanentes
- reforçar preferências do usuário
- citar tarefas vivas e pendências atuais
- evitar começar direto por tarefa crítica

### Etapa 3 — Teste rápido de recall
Antes de trabalho crítico, validar se o agente consegue responder com consistência:
- quem é o usuário
- quais projetos estão ativos
- quais decisões e pendências importam agora

Se falhar nesse teste, não confiar em tarefa crítica ainda.

### Etapa 4 — Revisão do segundo cérebro (GitHub)
Validar o fluxo:
1. pull
2. leitura do contexto relevante
3. execução
4. validação
5. registro em memória/arquivos
6. push

Regra: se GitHub estiver atrás do workspace, o agente passa a operar com dois estados de verdade em conflito.

### Etapa 5 — Flush antes da compactação
Antes de qualquer compactação/resumo de sessão:
1. salvar decisões
2. salvar lições
3. atualizar projetos
4. atualizar pendências
5. registrar nota diária
6. só depois compactar
7. após compactar, reindexar novamente se houve atualização material de memória

## Regra prática

Troca de modelo sem reindexação + warm-up + teste de recall = sessão não confiável para trabalho crítico.
