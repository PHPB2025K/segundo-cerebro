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

- WhatsApp: **Estoque - GB Importadora** — criado por Pedro em 2026-05-28; Kobe foi adicionado pela instância Evolution API própria.
- WhatsApp: **Devoluções - GB Importadora** — criado por Pedro em 2026-05-28; Kobe foi adicionado pela instância Evolution API própria.
- Telegram Kobe Hub: tópico **Estoque** — criado por Pedro em 2026-05-28, thread 11932.
- Telegram Kobe Hub: tópico **Devoluções** — criado por Pedro em 2026-05-28, thread 11937.

## Regra de canal — decisão 2026-05-28

- WhatsApp é a fonte real de inserção e comunicação dos dados no dia a dia da operação.
- Telegram é o canal para falar com Pedro sobre desenvolvimento do sistema, alertas, divergências, decisões técnicas e assuntos fora da operação diária.
- Assuntos de estoque devem ir para o tópico Telegram **Estoque**.
- Assuntos de devoluções devem ir para o tópico Telegram **Devoluções**.
- Não misturar devoluções no fluxo geral de estoque sem classificação; devolução exige triagem específica.

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

## Próxima tarefa imediata

Desenhar o blueprint técnico-operacional completo já considerando os canais criados: arquitetura, tabelas, estados dos movimentos, regras de validação, fluxo WhatsApp → movimento pendente → aprovação/aplicação → sincronização com Planilha de Estoque.

## Fase 1 — Implementação em código iniciada/concluída — 2026-05-28

Status: código implementado em `/var/www/estoque-budamix`, aguardando aplicação da migração no Supabase.

Entregas:
- Migração SQL para `stock_movements`, `stock_movement_evidences`, `sku_aliases` e `kit_bom`.
- `stock_balances` deixado para Fase 2, quando houver motor transacional e conciliação de saldo.
- Tipos TypeScript para movimentos, status, origem, evidências e afins.
- API `GET/POST /api/stock-movements` para listar/criar movimentos sem aplicar saldo.
- Validação mínima de campos e idempotência por origem/evento externo.
- Bloqueio para impedir criação direta de movimento já `aplicado` pela API.
- Painel simples no app para visualizar movimentos recentes, pendentes e divergentes.
- Documentação da Fase 1 no repo.

Garantias:
- A nova camada não escreve na Planilha de Estoque.
- Movimento pendente não altera saldo.
- Fluxo manual legado de entrada/saída pela planilha não foi alterado.

Validação:
- TypeScript `tsc --noEmit` passou.
- `npm run lint` e `npm run build` dependem de corrigir instalação local de dependências dev ausentes no `node_modules`.

Próximo passo imediato:
- Aplicar a migração no Supabase e testar a API/painel com dados reais controlados.

## CMV oficial por período — decisão de estruturação — 2026-06-02

Pedro aprovou começar a estruturação do motor de estoque para virar fonte oficial de CMV por período, permitindo responder com segurança:

- CMV de semana específica.
- CMV de mês.
- CMV por marketplace.
- CMV por SKU.
- CMV por pedido.
- CMV de perdas/avarias separado de venda.
- Margem bruta real por período.

Decisão técnica-operacional:

- O ledger de movimentações será a fonte de quantidade/consumo.
- O CMV oficial virá de snapshots de custo gravados no momento em que o movimento aplicado consome estoque.
- Nunca recalcular CMV histórico usando custo atual da planilha, porque isso distorce períodos antigos quando o custo muda.
- Método inicial recomendado: custo médio ponderado por SKU.
- Modelo deve ficar preparado para evoluir para FIFO por lote/container via Import Hub.
- Envio para Full é transferência logística e não gera CMV na saída do galpão; CMV nasce na venda/perda/ajuste que consome economicamente o produto.
- Perdas e avarias devem ficar separadas de venda para não poluir margem comercial por marketplace.
- Movimento que consome estoque sem custo confiável vira pendência financeira e não entra no CMV oficial até resolver.

Artefatos criados:

- Documento canônico: `docs/stock-cmv-official-periods.md`.
- Migração inicial: `migrations/202606021140_stock_cmv_cost_snapshots.sql`.

Próximos passos:

1. Validar/aplicar a migração de CMV no banco.
2. Integrar a aplicação de movimentos com geração de `stock_movement_cost_snapshots`.
3. Alimentar `stock_cost_layers` com custo inicial confiável por SKU a partir da planilha/Import Hub.
4. Criar consultas/endpoints para CMV semanal, mensal, marketplace, SKU, pedido e perdas/avarias.
