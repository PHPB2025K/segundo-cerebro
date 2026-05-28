---
title: "Estoque GB — Motor de Movimentações"
created: 2026-05-28
type: project-memory
status: active
tags:
  - estoque
  - gb-importadora
  - budamix-central
  - whatsapp
  - google-sheets
---

# Estoque GB — Motor de Movimentações

## Decisão aprovada — 2026-05-28

Pedro aprovou estruturar a atualização constante da Planilha de Estoque por uma camada de **movimentações auditáveis**, e não por escrita direta dispersa na aba ESTOQUE.

## Princípio operacional

- A aba ESTOQUE da Planilha de Estoque continua como visão/saldo final.
- O controle confiável deve nascer de um livro/motor de movimentos: cada entrada ou saída gera registro com origem, SKU, quantidade, responsável, status, evidência e validação.
- A escrita no saldo só acontece depois de validação suficiente para o tipo de movimento.

## Saídas de estoque a cobrir

1. Vendas diárias com pagamento confirmado em Mercado Livre, Shopee e Amazon.
2. Vendas diárias de atacado recebidas no WhatsApp/grupo de pedidos.
3. Envios de produtos para Full registrados diariamente na planilha de ENVIOS FULL.

## Entradas de estoque a cobrir

1. Mercadorias compradas que chegam no galpão.
2. Devoluções que chegaram íntegras e prontas para voltar ao estoque.
3. Containers novos recebidos no galpão.

## Canais definidos

- WhatsApp: **Estoque - GB Importadora** — a ser criado por Pedro.
- WhatsApp: **Devoluções - GB Importadora** — a ser criado por Pedro.
- Telegram Kobe Hub: tópico **Estoque** — a ser criado por Pedro.

## Regras iniciais

- Entradas via WhatsApp começam como movimento pendente; não devem alterar saldo automaticamente no início.
- Devolução só entra se a pessoa responsável enviar foto/etiqueta no grupo porque validou que o produto voltou inteiro.
- Mercadoria recebida/container deve vir com foto da nota fiscal, listagem de produtos ou documento equivalente.
- Kits/combos exigem tabela de composição para baixar componentes corretos.
- Nenhum movimento deve ser aplicado se SKU não for reconhecido ou se a baixa deixar saldo negativo sem aprovação.

## Próximo desenho necessário

- Campos obrigatórios da tabela de movimentos.
- Estados do fluxo: pendente, validado, aplicado, rejeitado, duplicado, divergente.
- Mapeamento das fontes: marketplaces, atacado WhatsApp, planilha ENVIOS FULL, WhatsApp Estoque, WhatsApp Devoluções.
- Estratégia de composição de kits/BOM.
- Rotina de conciliação diária e alertas de divergência.
- Sincronização segura com a aba ESTOQUE.

