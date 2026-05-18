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

### [TÁTICA] Daily Sales Report: Top Produtos por SKU equivalente, não por título (2026-05-11)
**Lição:** Relatório diário operacional deve consolidar SKUs equivalentes entre ML/Shopee/Amazon e omitir nomes não confiáveis, nunca exibir “Produto não identificado”.
**Expira:** 2026-06-10


### [ESTRATÉGICA] Daily Sales v2: fallback determinístico não pode maquiar falha LLM (2026-05-15)
**Contexto:** Na promoção técnica do Slack Writer LLM + QA Gate LLM para Lucas/Shopee, Yasmin/Mercado Livre e Leonardo/Amazon, os três recipients foram aprovados com ressalvas, mas o envio real permaneceu bloqueado.
**Lição:** Quando LLM for caminho principal aprovado, falha de camada LLM deve bloquear o recipient; fallback determinístico serve para validação mecânica/segurança, não para produzir aparência de aprovação.

### [TÁTICA] Daily Sales v2: QA deve bloquear propagação de formato/log incompleto entre camadas (2026-05-16)
**Contexto:** Preview de 15/05/2026 BRT foi aprovado com ressalvas nos três recipients, com problemas menores herdados da cadeia: percentuais sem 1 casa decimal, moeda em texto sem centavos, mudanças modais sem registro e itens “não pode ir para Slack” sem log formal completo.
**Lição:** A Condensadora/6B e a Slack Writer precisam padronizar números e registrar todos os bloqueios/restrições analíticas antes do QA final. Ressalva menor não bloqueia envio, mas deve virar correção de prompt para não acumular degradação sistêmica.
**Expira:** 2026-06-15

### [TÁTICA] Daily Sales v2 Shopee: correção numérica precisa nascer na consolidação 6B (2026-05-17)
**Contexto:** Preview de 16/05/2026 BRT deixou Lucas/Shopee aprovado com ressalva por tickets e range percentual aproximados sem decimais, herdados da camada Shopee Consolidator; Slack Writer preservou fielmente a origem.
**Lição:** Quando a mensagem Shopee consolidada tiver layer 6B, padronizar moeda/ticket/percentual nessa camada antes da Slack Writer. Corrigir só na saída final melhora aparência, mas não remove a fonte da ressalva e enfraquece auditabilidade.
**Expira:** 2026-06-16
