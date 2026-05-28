---
title: "Blueprint — Sistema de Estoque GB"
created: 2026-05-28
type: blueprint
status: draft-approved-direction
project: estoque-gb-movimentacoes
tags:
  - estoque
  - gb-importadora
  - budamix-central
  - whatsapp
  - google-sheets
---

# Blueprint — Sistema de Estoque GB

## 1. Objetivo

Criar um sistema confiável para manter a Planilha de Estoque do Drive atualizada continuamente, sem depender de edição manual dispersa e sem perder rastreabilidade.

A aba ESTOQUE permanece como visão final/saldo operacional. O controle real passa a ser feito por um motor de movimentações auditáveis: cada entrada, saída, transferência ou ajuste nasce como movimento, passa por validações e só então altera o saldo.

## 2. Princípio central

Não escrever direto no saldo como primeira ação.

Fluxo correto:

1. Fonte gera evento.
2. Sistema cria movimento bruto.
3. Motor normaliza SKU, quantidade, origem e evidências.
4. Valida regra do tipo de movimento.
5. Se seguro, aplica automaticamente; se incerto, fica pendente.
6. Saldo é atualizado.
7. Movimento fica auditável para rastreio e conciliação.

## 3. Canais e fonte de verdade operacional

### WhatsApp

- **Estoque - GB Importadora**: fonte operacional real para recebimento de mercadorias, containers, notas, listagens e comunicação diária de estoque físico.
- **Devoluções - GB Importadora**: fonte operacional real para devoluções aprovadas como aptas a retornar ao estoque.

### Telegram Kobe Hub

- **Estoque** (`11932`): desenvolvimento do sistema, alertas, divergências, decisões técnicas e comunicação com Pedro sobre estoque.
- **Devoluções** (`11937`): desenvolvimento, alertas, divergências e decisões sobre devoluções.

Regra: WhatsApp é operação; Telegram é gestão, desenvolvimento, alerta e decisão.

## 4. Tipos de movimento

### Saídas

1. **Venda marketplace confirmada**
   - Origem: Mercado Livre, Shopee, Amazon.
   - Condição: pedido pago/confirmado, não cancelado.
   - Aplicação: automática quando SKU/composição for reconhecido.
   - Risco: kits, combos, variações e pedidos cancelados/devolvidos depois.

2. **Venda atacado WhatsApp**
   - Origem: grupo de pedidos atacado/fluxo Bling.
   - Condição: pedido validado/criado.
   - Aplicação: semi-automática no começo; automática depois que parser e aliases estiverem maduros.
   - Risco: nomes coloquiais, itens marcados, alteração de pedido, pedido duplicado.

3. **Envio para Full**
   - Origem: planilha ENVIOS FULL.
   - Condição: envio registrado com SKU e quantidade.
   - Aplicação: transferência do estoque físico para estoque Full, não perda total de estoque.
   - Risco: tratar erroneamente como baixa definitiva.

4. **Ajuste de perda/quebra**
   - Origem: operação, auditoria ou devolução recusada.
   - Condição: justificativa obrigatória.
   - Aplicação: exige aprovação humana no começo.

### Entradas

1. **Mercadoria comprada recebida**
   - Origem: WhatsApp Estoque.
   - Evidência: foto da nota, listagem ou documento com produtos/quantidades.
   - Aplicação: movimento pendente até validação humana.

2. **Container recebido**
   - Origem: WhatsApp Estoque.
   - Evidência: foto da nota fiscal/documento do container.
   - Aplicação: movimento pendente; idealmente cruzar com Import Hub antes de aplicar.

3. **Devolução íntegra**
   - Origem: WhatsApp Devoluções.
   - Evidência: foto da etiqueta/pedido enviada pela pessoa responsável.
   - Regra operacional: só é enviada no grupo se o produto estiver inteiro e pronto para voltar ao estoque.
   - Aplicação: movimento pendente no início; pode virar automática assistida depois com confiança.

4. **Ajuste positivo de inventário**
   - Origem: auditoria/contagem física.
   - Condição: justificativa obrigatória.
   - Aplicação: aprovação humana.

## 5. Modelo de dados mínimo

### Tabela `stock_movements`

Campos recomendados:

- `id`
- `created_at`
- `source_type`: marketplace, atacado_whatsapp, full_sheet, whatsapp_estoque, whatsapp_devolucoes, import_hub, manual_audit
- `source_channel`: grupo, marketplace ou sistema de origem
- `source_message_id` ou `external_event_id`
- `movement_type`: entrada, saida, transferencia, ajuste
- `status`: recebido, pendente_validacao, validado, aplicado, rejeitado, duplicado, divergente, erro
- `sku_raw`
- `sku_resolved`
- `product_name_raw`
- `quantity`
- `unit`: un, kit, caixa, pacote, etc.
- `location_from`: galpao, full_ml, full_shopee, fba_amazon, devolucao, fornecedor
- `location_to`: galpao, full_ml, full_shopee, fba_amazon, cliente, perda
- `evidence_url` ou referência de mídia/documento
- `responsible_name`
- `validator_name`
- `validated_at`
- `applied_at`
- `error_reason`
- `notes`

### Tabela `stock_balances`

- `sku`
- `product_name`
- `physical_qty`
- `full_ml_qty`
- `full_shopee_qty`
- `fba_amazon_qty`
- `reserved_qty`
- `available_qty`
- `last_movement_at`
- `last_sync_sheet_at`

### Tabela `sku_aliases`

- `alias_raw`
- `sku`
- `confidence`
- `source`
- `active`

Exemplos: nomes coloquiais, abreviações internas, nomes de pedido atacado, nomes de marketplace e nomes usados pela expedição.

### Tabela `kit_bom`

- `kit_sku`
- `component_sku`
- `component_qty`
- `active`
- `valid_from`
- `valid_to`

Essa tabela é obrigatória para kits, combos e anúncios compostos. Sem BOM, não aplicar baixa automática.

### Tabela `stock_evidences`

- `movement_id`
- `media_type`: foto, pdf, audio, texto, planilha
- `url_or_storage_key`
- `ocr_text`
- `parsed_payload`
- `created_at`

## 6. Estados do fluxo

1. **Recebido**: evento bruto chegou.
2. **Pendente de interpretação**: precisa OCR/LLM/parser ou extração de dados.
3. **Pendente de validação**: dados extraídos, mas precisa humano confirmar.
4. **Validado**: pronto para aplicar.
5. **Aplicado**: saldo alterado e movimento travado.
6. **Rejeitado**: não deve alterar estoque.
7. **Duplicado**: evento já processado.
8. **Divergente**: há conflito de SKU, quantidade, saldo, documento ou origem.
9. **Erro técnico**: falha de API, planilha, parser ou integração.

## 7. Regras de aplicação automática

### Pode ser automático desde a fase 1

- Venda marketplace paga/confirmada com SKU reconhecido e sem kit desconhecido.
- Envio Full com SKU reconhecido e quantidade clara.
- Pedido marketplace simples, unitário, sem status cancelado.

### Deve começar semi-automático

- Pedido atacado via WhatsApp.
- Entrada por nota/listagem/foto no WhatsApp Estoque.
- Devolução aprovada no WhatsApp Devoluções.
- Container recebido.

### Nunca aplicar automático sem validação no início

- SKU desconhecido.
- Alias com baixa confiança.
- Kit sem composição cadastrada.
- Baixa que deixa saldo negativo.
- Devolução sem foto/etiqueta.
- Entrada com quantidade ilegível.
- Mensagem com múltiplas interpretações possíveis.
- Ajuste manual.

## 8. Regra por origem

### Marketplaces

- Buscar pedidos pagos/confirmados diariamente.
- Ignorar cancelados.
- Deduplicar por marketplace + order_id + item_id.
- Resolver SKU do anúncio para SKU base.
- Se anúncio for kit, decompor via BOM.
- Criar movimento de saída por componente.
- Aplicar automaticamente se tudo estiver claro.

### Atacado WhatsApp

- Ler mensagens do grupo de pedidos de atacado.
- Extrair cliente, itens, quantidades e observações.
- Resolver aliases para SKU.
- Conferir se pedido foi validado/criado no fluxo Bling.
- Criar movimentos de saída.
- No início, manter pendente quando houver qualquer ambiguidade.

### Planilha ENVIOS FULL

- Ler novas linhas desde último processamento.
- Resolver SKU e quantidade.
- Criar movimento de transferência: galpão → Full correspondente.
- Não tratar como venda.
- Aplicar automaticamente se SKU e quantidade forem claros.

### WhatsApp Estoque

- Cada mensagem com foto/documento/listagem vira candidato a entrada.
- OCR/extração tenta identificar SKUs, produtos e quantidades.
- Entrada fica pendente para validação humana.
- Depois de validada, aplica no saldo físico do galpão.

### WhatsApp Devoluções

- Cada foto/etiqueta enviada vira candidato a entrada de devolução.
- Regra operacional: a pessoa só envia quando produto está inteiro.
- Sistema tenta identificar marketplace/pedido/SKU.
- No início, pendente para validação.
- Após validação, entrada no galpão com origem devolução.

### Containers

- Mensagem no WhatsApp Estoque com NF/documento de chegada.
- Cruzar com Import Hub quando possível.
- Criar lote de movimentos por SKU/quantidade.
- Exigir validação antes de aplicar, porque impacto financeiro/operacional é alto.

## 9. Sincronização com a Planilha de Estoque

A planilha deve receber apenas o saldo consolidado, nunca eventos brutos.

Regra:

1. Motor calcula saldo por SKU.
2. Confere contra aba ESTOQUE.
3. Atualiza apenas colunas permitidas/input de estoque.
4. Nunca sobrescreve fórmula.
5. Valida visualmente/numericamente após escrita.
6. Registra `last_sync_sheet_at`.

A escrita precisa respeitar a regra de formato brasileiro para valores quando houver custo/valor, e preservar fórmulas da planilha.

## 10. Alertas

### Alertas no Telegram Estoque

- SKU não reconhecido.
- Kit sem composição.
- Baixa levaria saldo negativo.
- Divergência entre saldo calculado e planilha.
- Falha ao ler marketplace/Full/WhatsApp.
- Documento de entrada ilegível.
- Movimento pendente há mais de 24h.

### Alertas no Telegram Devoluções

- Devolução com etiqueta ilegível.
- Pedido/SKU não identificado.
- Tentativa de entrada duplicada.
- Devolução pendente há mais de 24h.
- Divergência entre marketplace e etiqueta.

## 11. Painel operacional ideal

No Budamix Central:

- Saldo por SKU.
- Movimentos pendentes.
- Movimentos divergentes.
- Últimos movimentos aplicados.
- Origem dos movimentos por dia.
- Estoque físico × Full × total.
- Fila de validação de entradas.
- Fila de validação de devoluções.
- Relatório diário de conciliação.

## 12. Implantação por fases

### Fase 0 — Preparação

- Confirmar IDs dos grupos WhatsApp via Evolution.
- Confirmar acesso aos novos tópicos Telegram.
- Consolidar lista de SKUs unitários da aba ESTOQUE.
- Resolver duplicidades críticas, especialmente SKUs duplicados.
- Criar/limpar aliases principais.
- Montar primeira versão da tabela de kits/BOM.

### Fase 1 — Livro de movimentos sem escrita automática

- Criar tabela de movimentos.
- Ingerir eventos dos canais.
- Mostrar pendentes e divergentes.
- Não alterar saldo ainda.
- Validar parsing com dados reais por alguns dias.

### Fase 2 — Saídas automáticas seguras

- Aplicar automaticamente vendas marketplace simples.
- Aplicar automaticamente envios Full claros.
- Manter atacado, entradas e devoluções como pendentes.
- Gerar relatório diário de baixas.

### Fase 3 — Entradas assistidas

- WhatsApp Estoque cria entradas pendentes com OCR/extração.
- WhatsApp Devoluções cria entradas pendentes por etiqueta/foto.
- Validação humana aplica saldo.
- Criar histórico por documento/foto.

### Fase 4 — Sincronização com a aba ESTOQUE

- Calcular saldo consolidado.
- Comparar com planilha.
- Atualizar saldos com validação.
- Alertar divergências antes de sobrescrever quando diferença for grande.

### Fase 5 — Automação avançada

- Atacado automático quando pedido for validado.
- Devoluções automáticas de alta confiança.
- Containers com conferência contra Import Hub.
- Conciliação diária automática.
- Alertas inteligentes por SKU crítico.

## 13. Ordem recomendada de implementação

1. Mapear IDs reais dos novos grupos WhatsApp.
2. Criar tabela `stock_movements`.
3. Criar tabela `kit_bom`.
4. Criar tabela `sku_aliases`.
5. Criar ingestão WhatsApp Estoque e Devoluções em modo somente leitura.
6. Criar ingestão da planilha ENVIOS FULL.
7. Criar ingestão de vendas marketplace confirmadas.
8. Criar painel de movimentos pendentes/divergentes.
9. Validar por 3 a 5 dias sem alterar saldo.
10. Liberar saídas automáticas seguras.
11. Liberar entradas assistidas.
12. Liberar sync com aba ESTOQUE.

## 14. Decisão técnica recomendada

Implementar no Budamix Central/Supabase como camada canônica de movimentos, usando Google Sheets apenas como interface/saldo final sincronizado.

Motivo: Google Sheets sozinho não dá histórico, idempotência, validação robusta, anexos, estados de processamento nem auditoria confiável. Para estoque operacional, isso é essencial.

## 15. Ponto crítico

Antes de automatizar escrita real no estoque, precisa resolver três bases:

1. SKU único e limpo na aba ESTOQUE.
2. Aliases reais usados pela equipe.
3. Composição de kits/combos.

Sem isso, o sistema até roda, mas baixa produto errado. Esse é o risco que precisa ser eliminado primeiro.
