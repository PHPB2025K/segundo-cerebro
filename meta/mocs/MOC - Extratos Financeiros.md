# MOC — Extratos Financeiros

> Hub dos 3 extratos de marketplace + consolidado. Formato unificado de 23 colunas.

---

## Extratos por plataforma

| Plataforma | Skill | Token | Agente |
|-----------|-------|-------|--------|
| Amazon BR | [[skills/marketplace/amazon-extrato/SKILL|amazon-extrato]] | LWA (longo prazo) | [[openclaw/agents/trader/IDENTITY|Trader]] |
| Mercado Livre | [[skills/marketplace/ml-extrato/SKILL|ml-extrato]] | ML Finance app, 6h | [[openclaw/agents/trader/IDENTITY|Trader]] |
| Shopee | [[skills/marketplace/shopee-extrato/SKILL|shopee-extrato]] | OAuth 4h, 3 contas | [[openclaw/agents/trader/IDENTITY|Trader]] |

## Consolidacao

- [[skills/marketplace/consolidado-financeiro/SKILL|consolidado-financeiro]] — junta os 3 extratos em HTML+Excel
- Design obrigatorio: [[skills/design/report-design-system/SKILL|report-design-system]]

## Formato unificado

Todas as 3 skills geram Excel com **23 colunas identicas**:
- Data, Tipo, ID Pedido, Produto, Valor Bruto, Comissao, Frete, ..., Valor Liquido
- Nomenclatura unificada cross-plataforma em cada skill (`references/nomenclatura-unificada`)

## Regras de taxas (alimentam a precificacao)

- [[skills/marketplace/amazon-fees-rules/SKILL|amazon-fees-rules]]
- [[skills/marketplace/ml-fees-rules/SKILL|ml-fees-rules]]
- [[skills/marketplace/shopee-fees-rules/SKILL|shopee-fees-rules]]

## Planilha de precificacao

- [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] — consome os dados dos extratos para calcular margens

---

*Criado: 10/04/2026 — Auditoria de conexoes*
