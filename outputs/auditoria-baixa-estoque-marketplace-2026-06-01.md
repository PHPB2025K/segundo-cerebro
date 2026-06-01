# Auditoria — Daily Marketplace Baixa Estoque

Data da auditoria: 2026-06-01
Escopo: desde o início operacional do cron `daily-marketplace-baixa`, com base nos pedidos espelhados das plataformas e nos registros de `marketplace_sales_log` + `stock_movements`.

## Janela auditada

O primeiro dia de venda processado pela rotina foi **2026-05-28**. O cron roda em D+1 às 10:00 BRT.

Dias auditados: **28/05, 29/05, 30/05 e 31/05/2026**.

## Regra real encontrada

A rotina busca pedidos por `order_date` no dia BRT e status considerado pagável/confirmado pelo script.

Classificação de logística:

- **Amazon:** sempre tratado como `full`; não baixa estoque físico do galpão.
- **Mercado Livre:** `logistic_type = fulfillment` vira `full`; `cross_docking`, `xd_drop_off`, `self_service`, `not_specified` e `drop_off` viram `seller`.
- **Shopee:** `raw_payload.shipping_carrier = Full` vira `full`; qualquer outro carrier preenchido vira `seller`.

A baixa real só é enviada para `ingest-safe-outbound` quando o item é classificado como `seller`.

## Resultado executivo

### Veredito sobre filtro Full/FBA

**Passou.** Na amostra completa desde o início do cron, não encontrei nenhum movimento de estoque físico gerado para pedido classificado como Full/FBA.

Checks executados:

- Full com `applied_to_stock = true`: **0**
- Movimento `stock_movements` originado de pedido Full/FBA: **0**
- Amazon FBA baixada do galpão: **0**
- ML fulfillment baixado do galpão: **0**
- Shopee `shipping_carrier = Full` baixado do galpão: **0**

### Veredito sobre pedidos pagos/confirmados

A rotina não inclui cancelados/pending. Isso está correto.

Ponto de atenção: o script não considera explicitamente alguns status Shopee pós-pagamento como `to_confirm_receive`. Como o status do pedido muda com o tempo, a comparação atual contra o snapshot do dia da execução fica parcialmente ruidosa em 28–30/05. Mesmo assim, os registros de baixa não mostram baixa indevida de Full.

## Resumo por dia

| Dia da venda | Pedidos/status no banco atual | Itens esperados confirmados hoje | Itens logados | Full logado | Seller logado | Movimentos de estoque originados no dia de venda | Movimentos aplicados | Movimentos divergentes | Unidades físicas/componentes aplicados | Baixa indevida de Full/FBA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2026-05-28 | 286 | 265 | 247 | 195 | 52 | 129 | 89 | 40 | 216 | 0 |
| 2026-05-29 | 258 | 236 | 224 | 182 | 42 | 93 | 59 | 34 | 194 | 0 |
| 2026-05-30 | 251 | 228 | 173 | 173 | 0 | 47 | 7 | 40 | 20 | 0 |
| 2026-05-31 | 361 | 323 | 323 | 270 | 53 | 70 | 63 | 7 | 228 | 0 |

Observação: “unidades físicas/componentes” aumenta quando um SKU vendido é kit/BOM, porque um item vendido pode gerar múltiplos movimentos de componentes.

## Achados por dia

### 28/05

- Cron aplicado inicialmente em 29/05 à noite.
- Havia 52 itens seller no log, com 12 aplicados na primeira rodada e 40 divergentes.
- Após os ajustes de aliases/BOMs e retrofix autorizado em 31/05, movimentos originados de vendas de 28/05 somam 89 movimentos aplicados e 40 divergentes.
- Nenhuma baixa indevida de Full/FBA.
- Existem diferenças item-a-item entre `orders` atual e `marketplace_sales_log`, principalmente Shopee, por alteração posterior de status/SKU e correção posterior para `model_sku`.

### 29/05

- Cron rodou em 30/05 às 10h BRT.
- Log do cron: 42 eventos seller; 8 aplicados inicialmente e 34 divergentes.
- Movimentos atuais originados das vendas de 29/05: 59 aplicados e 34 divergentes.
- Nenhuma baixa indevida de Full/FBA.
- Diferenças item-a-item concentradas em Shopee, pelos mesmos motivos de `model_sku`/status mutável.

### 30/05

- Cron rodou em 31/05 às 10h BRT.
- Problema encontrado: o cron processou eventos seller e gerou movimentos, mas o `marketplace_sales_log` não recebeu as linhas seller do dia. O log da rotina mostra `log_seller_inserted = 0`.
- Resultado: a baixa ocorreu parcialmente, mas a trilha de conciliação no `marketplace_sales_log` ficou incompleta para seller.
- Movimentos atuais originados das vendas de 30/05: 7 aplicados, 40 divergentes, 20 unidades físicas/componentes aplicados.
- Nenhuma baixa indevida de Full/FBA.

### 31/05

- Cron rodou em 01/06 às 10h BRT.
- Dia mais limpo da janela.
- Itens esperados = itens logados: 323 vs 323.
- Full logado: 270. Seller logado: 53.
- Movimentos originados das vendas de 31/05: 63 aplicados e 7 divergentes, com 228 unidades físicas/componentes aplicados.
- Nenhuma baixa indevida de Full/FBA.

## Problemas encontrados

1. **Audit trail incompleto em 30/05:** seller foi processado, mas não entrou no `marketplace_sales_log`. Isso precisa correção, porque a baixa física pode acontecer sem a linha de conciliação correspondente.

2. **Comparação retroativa fica ruidosa porque `orders.status` e SKUs Shopee mudam depois:** o banco atual não preserva snapshot do status/SKU no momento do cron. Isso afeta principalmente 28–30/05.

3. **Shopee antes do fix de `model_sku` gerou diferenças de SKU:** em 28–30/05 aparecem casos onde o log antigo usou SKU pai ou SKU anterior, enquanto o pedido atual aponta para `model_sku` correto. O fix aplicado em 31/05 corrigiu a lógica; 31/05 fechou 100% esperado vs logado.

4. **Divergentes ainda precisam fila diária de resolução:** divergente não é baixa errada; é item seller pago que deveria baixar, mas travou por SKU/BOM/estoque insuficiente. Em 31/05 restaram 7 divergentes.

## Recomendações

1. **Corrigir imediatamente a gravação de `marketplace_sales_log` para seller**, especialmente o caso de `log_seller_inserted = 0` com movimentos já gerados.
2. **Persistir snapshot de classificação no log**: status usado, carrier/logistic_type usado, sku usado e source timestamp do pedido. Isso elimina ruído de auditoria retroativa.
3. **Adicionar check pós-cron obrigatório:** quantidade de eventos seller enviados ao `ingest-safe-outbound` precisa bater com linhas seller inseridas no `marketplace_sales_log`; se não bater, alertar no tópico Estoque.
4. **Adicionar auditoria automática anti-Full:** todo dia checar se existe movimento `source_type=marketplace` cujo pedido original era Amazon/FBA, ML fulfillment ou Shopee Full. Se >0, travar/alertar.
5. **Resolver divergentes diariamente**, separando divergente por falta de SKU/BOM vs estoque insuficiente.

## Conclusão

A lógica de não baixar Full/FBA funcionou. O problema real não é baixa indevida de Full; é a confiabilidade da trilha de conciliação e o lote de divergentes, principalmente antes do fix de `model_sku` da Shopee.
