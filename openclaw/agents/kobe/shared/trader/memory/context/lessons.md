# Lições Aprendidas — [[openclaw/agents/trader/IDENTITY|Trader]]

_Erros e aprendizados. [ESTRATÉGICA] = permanente | [TÁTICA] = expira em 30 dias._

---

### [ESTRATÉGICA] Consolidado financeiro com dados parciais = relatório inválido (2026-04-03)
**Contexto:** Consolidado de março entregue com extrato Shopee de 01-20/03, apresentado como mês completo.
**Lição:** NUNCA entregar relatório financeiro sem validar que TODOS os extratos cobrem o período completo. Dado parcial ≠ dado completo. 5 regras de QA financeiro implementadas — seguir sem exceção.

### [ESTRATÉGICA] Margem consolidada SEMPRE ponderada por volume (2026-03-21)
**Lição:** Margem média simples mascara problemas. SEMPRE ponderar por volume E plataforma.

### [ESTRATÉGICA] Sync custos: puxar das 4 abas da planilha (2026-03-26)
**Lição:** Planilha tem SKUs distribuídos em 4 abas (ESTOQUE > MELI > SHOPEE > AMAZON). SEMPRE mapear todas.

### [ESTRATÉGICA] Amazon pending = venda real no Live Sales (2026-03-27)
**Lição:** Amazon FBA pending com total_amount > 0 → cliente já pagou. Contar no faturamento. ML e Shopee excluem pending.

### [ESTRATÉGICA] Amazon SP-API ItemPrice.Amount é total do line item (2026-04-01)
**Lição:** Sempre dividir ItemPrice.Amount pela quantidade para obter preço unitário.

### [ESTRATÉGICA] Cron de relatório financeiro: validar tokens ANTES de executar (2026-04-01)
**Lição:** Se qualquer token falhar (ML, Shopee 3 contas, Amazon), abortar e notificar — não executar parcialmente.

### [TÁTICA] Shopee extrato multi-conta: ~13 min para 3.300 pedidos (2026-03-20)
**Expira:** 2026-04-20

### [TÁTICA] ML API: MLB IDs ≠ seller SKUs (2026-03-26)
**Lição:** Mapeamento via `attributes.SELLER_SKU`. 7/10 auto, 3 manuais.
**Expira:** 2026-04-26

### [TÁTICA] Shopee sync on_conflict: parâmetro condicional por tabela (2026-04-02)
**Lição:** `products` usa `on_conflict=platform,platform_item_id`. `price_history` NÃO usa on_conflict (tabela de log).
**Expira:** 2026-05-02

---

_Atualizado na Consolidação Profunda 2026-04-04._
