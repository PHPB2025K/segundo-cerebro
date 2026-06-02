# Estoque GB — CMV oficial por período

Status: aprovado para estruturação inicial em 2026-06-02
Projeto: Estoque GB / motor de movimentações auditáveis

## Objetivo

Transformar o histórico de movimentações de estoque em fonte oficial para cálculo de CMV e margem bruta por período, com rastreabilidade suficiente para responder com segurança:

- CMV de uma semana específica
- CMV de um mês
- CMV por marketplace
- CMV por SKU
- CMV por pedido
- CMV de perdas/avarias separado de venda
- margem bruta real por período

## Princípio contábil-operacional

O saldo de estoque responde “quantas unidades existem”.

O CMV responde “quanto custaram as unidades consumidas”.

Por isso, o motor de movimentações precisa gravar um snapshot financeiro no momento em que uma movimentação aplicada consome estoque. Não basta consultar o custo atual da planilha depois, porque o custo pode mudar e recalcular períodos antigos errado.

## Regra central

Todo movimento aplicado que consome estoque deve gerar uma linha imutável de custo.

Essa linha deve conter:

- movimento de origem
- data de competência do movimento
- SKU componente consumido
- quantidade consumida
- custo unitário em reais usado naquele momento
- custo total em reais
- método de custeio usado
- fonte do custo
- marketplace/canal quando houver
- pedido quando houver
- categoria de CMV

Depois de gravado, esse snapshot não deve ser recalculado automaticamente. Correção posterior deve ser feita por ajuste/reprocessamento auditável.

## O que entra e o que não entra em CMV

### Entra em CMV

1. Venda marketplace confirmada
   - Mercado Livre, Shopee, Amazon.
   - Categoria: venda.
   - Competência: data do pedido aprovado/faturado conforme regra do relatório comercial.

2. Venda atacado confirmada
   - Categoria: venda_atacado.
   - Competência: data do pedido validado/faturado.

3. Perda, quebra ou avaria sem retorno ao estoque
   - Categoria: perda_avaria.
   - Não mistura com CMV de venda.
   - Deve aparecer separado para não poluir margem comercial.

4. Ajuste negativo de inventário
   - Categoria: ajuste_negativo.
   - Separado de venda e de perda operacional quando possível.

### Não entra em CMV imediatamente

1. Envio para Full
   - É transferência de local: galpão → Full ML/Shopee/FBA.
   - Não é consumo econômico.
   - Só vira CMV quando a venda daquele estoque acontece.

2. Entrada de container/compra nacional
   - Aumenta estoque/camadas de custo.
   - Não gera CMV.

3. Devolução íntegra
   - Reverte/retorna estoque.
   - Deve ser tratada como entrada ou reversão, não como venda nova.

## Método de custeio recomendado

### Fase inicial: custo médio ponderado por SKU

Usar custo médio ponderado por SKU como método oficial inicial.

Motivos:

- é mais simples de operar;
- funciona melhor com a operação atual de poucos SKUs e alto giro;
- evita complexidade prematura de lote/container;
- já permite CMV confiável por semana, mês, SKU, pedido e marketplace.

### Evolução futura: FIFO por lote/container

Depois que containers, compras nacionais e Import Hub estiverem completamente conectados, evoluir para FIFO por camada/lote se fizer sentido.

O modelo de dados já deve permitir essa evolução, mesmo que a regra inicial use médio ponderado.

## Fonte do custo

Ordem recomendada para resolver custo unitário:

1. Snapshot de custo já gravado no movimento, se existir.
2. Camada de custo do SKU no motor financeiro de estoque.
3. Último custo validado da planilha de precificação/estoque.
4. Custo vindo do Import Hub/container, quando disponível e validado.
5. Custo manual aprovado.

Se não houver custo confiável, o movimento pode até baixar estoque operacionalmente, mas não deve entrar como CMV oficial. Ele fica marcado como pendência financeira de custo.

## Dados mínimos por movimento para CMV

Além dos campos atuais de `stock_movements`, a camada de CMV precisa conseguir enxergar:

- `movement_id`
- `source_type`
- `source_channel`
- `external_event_id`
- `movement_type`
- `sku_resolved`
- `quantity`
- `location_from`
- `location_to`
- `applied_at`
- `movement_business_date`
- `marketplace`
- `order_id`
- `order_item_id`
- `cmv_category`
- `gross_revenue_brl`, quando disponível
- `unit_cost_brl`
- `total_cost_brl`
- `costing_method`
- `cost_source_type`
- `cost_source_ref`

## Relatórios oficiais que essa camada deve permitir

### CMV por período

Filtros:

- data inicial
- data final
- categoria: venda, venda_atacado, perda_avaria, ajuste_negativo
- marketplace/canal opcional

Saídas:

- quantidade consumida
- CMV total
- receita bruta/receita comercial quando disponível
- margem bruta em reais
- margem bruta percentual

### CMV por marketplace

Agrupar por:

- Mercado Livre
- Shopee
- Amazon
- Atacado
- Manual/outros

Regra: Full não é marketplace de CMV por si só; Full é localização logística. O marketplace vem da venda que consome o estoque.

### CMV por SKU

Agrupar por SKU componente real, não necessariamente SKU do anúncio.

Kits e combos devem ser decompostos via BOM. O CMV oficial do pedido é a soma dos componentes consumidos.

### CMV por pedido

Cada pedido deve conseguir abrir:

- itens vendidos
- componentes baixados
- quantidade por componente
- custo por componente
- custo total do pedido
- receita do pedido, quando disponível
- margem bruta do pedido

### Perdas/avarias separado de venda

Perda e avaria devem ter relatório próprio, com:

- SKU
- quantidade
- custo total
- origem/evidência
- responsável/validador quando houver
- motivo

Esse valor não deve ser misturado automaticamente na margem de venda por marketplace.

## Guardrails

1. Nunca recalcular CMV histórico usando custo atual da planilha.
2. Movimento aplicado que consome estoque sem custo confiável vira pendência financeira.
3. Kit sem BOM não pode gerar CMV automático.
4. Transferência para Full não é CMV.
5. Devolução íntegra não é venda nem CMV novo.
6. Perda/avaria deve ficar separada da margem comercial.
7. Todo ajuste retroativo precisa deixar trilha: quem, quando, motivo, período afetado.

## Implementação em fases

### Fase CMV-1 — estrutura de dados

- Criar tabela de camadas/fontes de custo por SKU.
- Criar tabela de snapshots de custo por movimento aplicado.
- Criar views de agregação por período, SKU, marketplace e pedido.
- Marcar movimentos sem custo como pendência financeira.

### Fase CMV-2 — resolução de custo

- Resolver custo médio ponderado por SKU.
- Alimentar custos iniciais a partir da planilha de estoque/precificação.
- Preparar entrada futura do Import Hub/container.
- Bloquear CMV oficial quando custo estiver ausente ou inválido.

### Fase CMV-3 — relatórios

- Criar consultas/endpoint para CMV semanal/mensal.
- Criar consulta por marketplace.
- Criar consulta por SKU.
- Criar consulta por pedido.
- Criar relatório separado de perdas/avarias.

### Fase CMV-4 — margem bruta real

- Cruzar CMV com receita comercial por pedido/período.
- Separar vendas, frete, descontos, taxas e ADS conforme regra do relatório financeiro.
- Entregar margem bruta real por período, marketplace, SKU e pedido.

## Decisão inicial

A fonte oficial de CMV por período será o ledger de movimentações aplicado + snapshot de custo no momento da aplicação.

A planilha continua útil como cadastro/custo atual, mas não deve ser usada sozinha para recalcular CMV histórico.
