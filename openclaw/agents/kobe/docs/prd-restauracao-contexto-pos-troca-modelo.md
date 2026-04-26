---
title: "prd-restauracao-contexto-pos-troca-modelo"
created: 2026-04-26
type: doc
agent: kobe
status: active
tags:
  - agent/kobe
  - doc
---
# PRD — Playbook de Restauração de Contexto após Troca de Modelo no OpenClaw

## Objetivo
Criar um processo simples, replicável e confiável para restaurar contexto, memória operacional e continuidade de agentes OpenClaw após troca de modelo.

## Problema
Após trocar de modelo, alguns agentes passam a operar pior mesmo mantendo a mesma base de memória.

Sintomas mais comuns:
- perda de continuidade
- piora na recuperação de contexto
- menor aderência a decisões e preferências já salvas
- respostas mais desalinhadas
- regressão em tarefas complexas

## Hipótese central
O problema não é apenas o modelo. Pode haver desalinhamento entre:
- índice atual de memória
- padrão de retrieval do novo modelo
- memória recente da sessão
- boot de contexto
- fluxo do GitHub como segundo cérebro

## Tese operacional
Duas ações dão ganho imediato após a troca de modelo:
1. reindexação forçada
2. warm-up estruturado antes de tarefa crítica

## Fluxo recomendado

### 1. Reindexação
Executar:
- `openclaw memory index --force`

### 2. Warm-up
Nos primeiros minutos após a troca:
- reapresentar contexto atual
- reforçar decisões importantes
- citar tarefas, projetos e preferências vivas
- evitar começar direto em tarefa crítica

### 3. Revisão de boot
Garantir que o agente leia corretamente os arquivos-base de identidade e contexto no início da sessão.

### 4. Revisão do GitHub
Garantir fluxo consistente:
1. pull
2. leitura do contexto relevante
3. execução
4. validação
5. registro
6. push

### 5. Revisão de compactação
Garantir flush antes da compactação, salvando:
- decisões
- lições aprendidas
- projetos
- pendências
- nota diária
- índice, quando necessário

## Por que a reindexação ajuda
Mesmo sem trocar explicitamente o embedding model, a reindexação ajuda porque:
- reprocessa todos os arquivos de memória
- recria embeddings do zero
- reorganiza o espaço vetorial do índice atual
- remove ruído e chunks defasados
- melhora a coerência entre busca e padrão de consulta do modelo atual

## Por que o warm-up ajuda
O warm-up cria um centro de gravidade novo de contexto recente.

Na prática:
- injeta contexto real e atualizado
- fortalece memória recente da sessão
- aumenta a chance de o retrieval puxar o que está vivo agora
- reduz dependência de histórico antigo mal recuperado

## Critérios de aceite
O playbook é considerado bem-sucedido se:
- o agente recuperar melhor o contexto após troca de modelo
- houver melhora perceptível na aderência a preferências e decisões já salvas
- o retrieval encontrar memória relevante com mais consistência
- o usuário conseguir repetir o processo em outros agentes com resultado semelhante

## Quick wins imediatos
- rodar reindexação forçada após troca de modelo
- fazer warm-up antes de tarefa crítica
- revisar boot dos arquivos-base
- reforçar GitHub como fonte de verdade
- reforçar flush antes da compactação

## Ver também

- [[openclaw/agents/kobe/IDENTITY]] — identidade do Kobe (modelo atual, escopo, responsabilidades)
- [[openclaw/agents/kobe/SOUL]] — princípios estáveis que persistem entre modelos
- [[openclaw/agents/kobe/AGENTS]] — orquestração com sub-agentes
- [[memory/context/decisoes/2026-04]] — decisões de migração GPT 5.4 / 5.1-mini
- [[meta/mocs/MOC - Governanca OpenClaw]] — governança da plataforma
- [[memory/context/business-context]] — visão geral da operação
