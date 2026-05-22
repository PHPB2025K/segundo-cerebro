---
title: "Lições — Kobe"
created: 2026-05-21
type: context
status: active
tags:
  - memory
  - context
  - lessons
---

# Lições — Kobe

## 2026-05-21 — [TÁTICA] Recovery de atendimento precisa validar até mensagem agent real

Em Canggu/Ana, corrigir parser/source do webhook não bastou para declarar recovery. O teste intermediário provou que mensagens inbound chegavam e que `process-message` respondia manualmente, mas o dispatch automático ainda não gerava resposta. Critério correto para recovery: mensagem real do cliente → webhook → invoke do process-message → fechamento de pending → mensagem `sender=agent` com tokens/tempo de resposta.

## 2026-05-21 — [TÁTICA] Sync automático de vault não deve fazer Git direto sem lock

Autosave, pull periódico e commits manuais no mesmo vault criam risco de corrida. Fluxos automáticos devem passar por wrapper de escrita segura/lock e registrar backup antes de mudança estrutural. Lock local resolve concorrência na mesma máquina; conflito distribuído Mac↔VPS ainda exige disciplina de push/pull ou lock compartilhado.

## 2026-05-22 — [TÁTICA] Diagnóstico da Ana precisa validar conversa real completa, não só teste controlado

Em Canggu/Ana, receber mensagem no Supabase e até responder um teste manual não prova recovery. O caso real de 22/05 mostrou que clientes podem receber apenas a mensagem inicial de origem/canal, com imagens e textos corretamente ingeridos, mas sem nascer a resposta LLM posterior. Critério correto de saúde: cliente real ou teste que simule o fluxo real completo → mensagem inicial → resposta à origem/canal → nova mensagem/pergunta/imagem → mensagem `sender=agent` posterior com `tokens_used` e envio confirmado.

