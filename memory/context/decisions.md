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

## 2026-05-28 — Aba ESTOQUE da planilha de precificação deve listar apenas SKUs pai/unitários, com exceções operacionais explícitas

- Pedro definiu que a aba **ESTOQUE** deve listar exclusivamente produtos unitários / SKUs pai, sem linhas de kits/composições de marketplace.
- Exceções aprovadas como unitárias dentro da ESTOQUE: **Kits Jardinagem**, **Kits MDF (porta-copos e descansos de panela)** e o **conjunto de 5 potes redondos IMB501**, por serem tratados operacionalmente como produto unitário.
- Pedro aprovou deletar fisicamente da aba ESTOQUE os demais kits de potes e kits quebra-cabeças, em vez de apenas limpar conteúdo.
- Pedro decidiu que o **QCB002 — Kit 10 Quebra-cabeças Animais** deve voltar/ficar na aba ESTOQUE como item unitário.
- Pedro também aprovou corrigir os SKUs das Xícaras 95ml RR na ESTOQUE para o mapeamento correto: **verde = 308_B** e **rosa = 309_B**.
- Contexto: reorganização da planilha para que a ESTOQUE fique como base canônica de produtos unitários, sem recalcular por enquanto o preço de custo nas abas MELI/SHOPEE/AMAZON.
