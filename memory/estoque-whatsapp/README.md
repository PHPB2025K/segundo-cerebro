---
title: "Ciclo de Memória — WhatsApp Estoque"
type: memory-cycle
status: active
created: 2026-06-10
area: estoque
---

# Ciclo de Memória — WhatsApp Estoque

## Objetivo

Manter histórico simples e auditável dos resumos diários do grupo WhatsApp **Estoque - GB Importadora**, sem depender só da sessão do dia.

## Camadas

### 1) Memória diária — últimos 7 dias

- Um arquivo por dia em `memory/estoque-whatsapp/daily/`.
- Cada resumo diário recebe ID único no formato `EWDS-YYYYMMDD-HHMM-BRT`.
- Deve registrar:
  - data analisada;
  - mensagens encontradas;
  - interpretação em linguagem simples;
  - o que deve somar no estoque;
  - o que deve baixar/ajustar;
  - o que deve ficar fora do estoque vendável;
  - status: aplicado ou não aplicado.
- A memória diária serve como janela operacional curta para reconsultar os últimos 7 dias.

### 2) Memória semanal consolidada

- Arquivos em `memory/estoque-whatsapp/weekly/`.
- Consolida os resumos diários da semana.
- Deve responder:
  - quais entradas/devoluções apareceram;
  - quais avarias se repetiram;
  - quais produtos tiveram ajuste recorrente;
  - quais ações ficaram pendentes;
  - quais regras novas Pedro definiu.

### 3) Memória mensal consolidada

- Arquivos em `memory/estoque-whatsapp/monthly/`.
- Consolida as semanas do mês.
- Deve guardar apenas o que importa no longo prazo:
  - padrões recorrentes;
  - problemas de processo;
  - produtos com avaria frequente;
  - mudanças de regra;
  - decisões operacionais permanentes.

## Regra de comunicação

Resumos enviados ao Pedro devem ser simplificados, sem termos técnicos. Foco em: o que chegou, o que voltou, o que teve avaria, o que deve atualizar na planilha e o que não deve mexer.

## Regra de segurança

Resumo não aplica estoque. Aplicação só acontece quando Pedro autorizar ou quando uma rotina automática já estiver explicitamente liberada.
