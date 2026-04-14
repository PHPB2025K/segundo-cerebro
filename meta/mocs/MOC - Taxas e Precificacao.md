# MOC — Taxas e Precificacao

> Hub comparativo de taxas das 3 plataformas + planilha de precificacao.

---

## Regras de taxas por plataforma

| Plataforma | Skill | Cron monitor | Destaque |
|-----------|-------|-------------|----------|
| Amazon BR | [[skills/marketplace/amazon-fees-rules/SKILL|amazon-fees-rules]] | Quarta 10h SP | Referral 15% Home; promo FBA gratis ≥R$100 (fev-jul/2026) |
| Mercado Livre | [[skills/marketplace/ml-fees-rules/SKILL|ml-fees-rules]] | Quarta 10h SP | Tabela variavel 232 combinacoes peso×preco (desde 02/03/2026) |
| Shopee | [[skills/marketplace/shopee-fees-rules/SKILL|shopee-fees-rules]] | Quarta 10h SP | Armadilha de fronteira R$79,99→R$80 (taxa fixa salta 550%) |

## Planilha de precificacao

- [[skills/spreadsheet-pricing/SKILL|spreadsheet-pricing]] — 4 abas (MELI, SHOPEE, AMAZON, ESTOQUE)
- SSID: `1dUoZtrvrqI6TiX3E_UzGuzglJFj6OVDZuYcgJyBfuRU`
- Mapas de colunas INPUT vs FORMULA por aba

## Skills relacionadas

- [[skills/update-ml-return-rates/SKILL|update-ml-return-rates]] — atualiza Col O (devolucoes) da aba MELI
- [[skills/marketplace/marketplace-optimization/SKILL|marketplace-optimization]] — usa taxas para calcular ROI de otimizacoes
- [[skills/marketplace/consolidado-financeiro/SKILL|consolidado-financeiro]] — usa taxas para validar extratos
- [[skills/operations/inventory-management/SKILL|Gestão de Estoque]] — controle de estoque e reposição integrado com precificação

## Armadilhas documentadas

1. **Shopee R$80**: produto a R$79,99 paga R$4 taxa fixa; a R$80,00 paga R$16 — margem pode ficar negativa
2. **ML tabela variavel**: desde 02/03/2026, nao existe mais "taxa fixa" — sao 232 combinacoes peso×preco
3. **NCM format**: planilha usa pontos (4411.12.10), Amazon exige sem pontos (44111210)
4. **Amazon parcelamento**: isento abaixo de R$40; taxa 1.5% de R$40-R$100

---

*Criado: 10/04/2026 — Auditoria de conexoes*
