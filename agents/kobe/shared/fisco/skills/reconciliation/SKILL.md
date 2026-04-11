# Skill: Conciliação Fisco (Módulo D) — [[agents/fisco/IDENTITY|Fisco]]

_Cruza NF-e emitidas com pedidos dos marketplaces para identificar inconsistências._

---

## Trigger
- Cron mensal (ou sob demanda do Kobe)
- Período: mês anterior completo

## Fluxo

```
1. Puxar NF-e emitidas no período:
   - Do Bling (NFs internas — transferência e venda interna)
   - Do UpSeller (NFs B2C — via export, sem API)
2. Puxar pedidos do período:
   - Via Trader (ML, Shopee, Amazon)
   - Incluir: número do pedido, valor, data, CNPJ emissor, status
3. Cruzar:
   a. Para cada pedido com status "entregue/concluído":
      - Existe NF correspondente?
      - Valor da NF bate com valor do pedido?
      - CNPJ emissor correto?
   b. Para cada NF emitida:
      - Existe pedido correspondente?
      - Se NF sem pedido → exceção (NF fantasma ou erro)
4. Classificar exceções:
   - PEDIDO_SEM_NF: pedido entregue sem NF emitida
   - NF_SEM_PEDIDO: NF emitida sem pedido correspondente
   - VALOR_DIVERGENTE: NF e pedido com valores diferentes (tolerância: R$0,50)
   - CNPJ_INCORRETO: NF emitida por CNPJ diferente do esperado
5. Gerar relatório de exceções
```

## Fontes de Dados

| Fonte | Tipo de NF | Via |
|-------|-----------|-----|
| Bling | NFs internas (transferência, venda interna) | API v3 |
| UpSeller | NFs B2C (consumidor final) | Export manual ou scraping |
| Trader | Pedidos ML, Shopee, Amazon | APIs marketplace |

## Output — Relatório de Conciliação

Template: `shared/fiscal/templates/reconciliation-report.md`

Seções:
1. Resumo: total de pedidos, total de NFs, taxa de match
2. Exceções por tipo (PEDIDO_SEM_NF, NF_SEM_PEDIDO, etc.)
3. Exceções por plataforma
4. Exceções por CNPJ
5. Detalhamento de cada exceção (pedido/NF, valor, data)

## Validações
- Tolerância de valor: R$0,50 (para arredondamentos)
- Tolerância de data: ±2 dias (para NFs emitidas com delay)
- NFs de transferência e venda interna (Módulos B/C) NÃO entram no cruzamento B2C
- Pedidos cancelados/devolvidos devem ser excluídos

## Regras
- Fisco NÃO corrige exceções — apenas identifica e reporta
- Toda exceção vai pro relatório, mesmo que pareça irrelevante
- Relatório vai pro Kobe, que decide se repassa ao Pedro

## Dependências
- Trader: dados de pedidos por marketplace/CNPJ
- Bling API v3: NFs internas emitidas
- UpSeller exports: NFs B2C
