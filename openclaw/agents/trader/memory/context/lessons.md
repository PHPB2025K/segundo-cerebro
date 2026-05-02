---
title: "lessons"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

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

### [TÁTICA] Shopee sync on_conflict: parâmetro condicional por tabela (2026-04-02)
**Lição:** `products` usa `on_conflict=platform,platform_item_id`. `price_history` NÃO usa on_conflict (tabela de log).
**Expira:** 2026-05-02

### [ESTRATÉGICA] Validar fonte canônica de planilha antes de diagnosticar custo (2026-04-30)
**Lição:** Antes de concluir que SKU está sem custo ou pedir cadastro aos analistas, validar se o script lê a planilha oficial de precificação. A planilha correta de custos/anúncios é `1u74a...`; `1dUoZ...` é legado/operacional.

### [ESTRATÉGICA] FBA unit_price=0 pode ser fantasma de catálogo (2026-04-30)
**Lição:** Em Amazon FBA, SKU com `unit_price=0` e baixa quantidade pode ser listing órfão/não-Budamix. Filtrar no sync e validar antes de somar ao estoque/margem.

### [ESTRATÉGICA] Settlement não é faturamento comercial (2026-05-01)
**Lição:** Extrato financeiro mede liquidação/repasse, não necessariamente competência comercial do mês. Sempre separar pedidos válidos/faturamento comercial de settlement.

### [ESTRATÉGICA] DRE profissional precisa de estrutura clássica completa (2026-05-01)
**Lição:** DRE não pode virar relatório de marketplace com receita/taxas/ads/resultado. Usar estrutura contábil/gerencial completa e marcar lacunas.

---

_Atualizado na Consolidação Profunda 2026-05-01._
