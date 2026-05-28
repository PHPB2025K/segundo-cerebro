---
title: "Decisões — Kobe"
created: 2026-05-28
type: context
status: active
tags:
  - memory
  - context
  - decisions
---

# Decisões — Kobe

## 2026-05-28 — Estoque GB como motor de movimentações auditáveis

- Pedro aprovou a linha operacional para manter a Planilha de Estoque atualizada por meio de um **motor/livro de movimentações de estoque** antes de alterar saldo na aba ESTOQUE.
- A aba ESTOQUE continua como visão/saldo final, mas cada alteração deve nascer de um movimento auditável com origem, SKU, quantidade, responsável, documento/foto quando aplicável, status e validação.
- Saídas a cobrir: vendas pagas/confirmadas dos marketplaces, pedidos de atacado via WhatsApp e envios para Full preenchidos na planilha de ENVIOS FULL.
- Entradas a cobrir: mercadorias compradas recebidas no galpão, devoluções aprovadas como íntegras e containers recebidos.
- Pedro vai criar grupos WhatsApp específicos **Estoque - GB Importadora** e **Devoluções - GB Importadora**, além de um tópico Telegram **Estoque** no Kobe Hub.
- Regra de segurança aprovada: entradas via WhatsApp não devem alterar estoque automaticamente no início; devem criar movimento pendente para interpretação e confirmação antes da escrita no saldo.
- Atualização do mesmo dia: Pedro criou os grupos WhatsApp **Estoque - GB Importadora** e **Devoluções - GB Importadora**, adicionou Kobe via instância Evolution API, e criou no Telegram os tópicos **Estoque** (thread 11932) e **Devoluções** (thread 11937).
- Regra de canal: WhatsApp é a fonte real de inserção/comunicação diária da operação; Telegram fica para desenvolvimento do sistema, alertas, divergências, decisões e assuntos com Pedro fora da rotina operacional.

## 2026-05-28 — Produtos MDF / catálogo operacional

- Pedro definiu que o **Quebra-Cabeça Animais MDF** deve entrar na lista de produtos feitos em MDF da operação mesmo não aparecendo na lista atual da aba ESTOQUE consultada naquele momento.
- Forma de apresentação usada na sessão: **kits de 5, 10 e 20 peças**.
- Contexto: correção explícita de uma primeira resposta que havia sinalizado o item como pendente/fora da lista atual.
