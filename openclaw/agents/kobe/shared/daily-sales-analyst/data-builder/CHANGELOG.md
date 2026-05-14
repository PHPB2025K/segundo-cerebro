# Changelog — Data Builder

## v1.0 — 2026-05-14

- **Autor:** Daily Sales Analyst Foundation Job
- **Tipo:** Release inicial
- **Escopo:** Criação do Data Builder determinístico (Layer 0)
- **Detalhes:**
  - Script `scripts/daily-sales-data-builder.py`
  - Schema `schema.json` definido
  - Regras de readiness (`readiness-rules.md`)
  - Consulta paginada a Supabase `orders` em janela BRT
  - Separação Shopee por `shop_id` (3 contas)
  - Identificação Amazon por ASIN/platform_item_id do pedido real
  - Histórico 7d/30d/60d e mesmo dia da semana (4x)
  - Concentração top3/top5
  - Reconciliação contra fonte canônica BRT
  - Data Readiness: DADOS_OK / DADOS_PARCIAIS / NOT_READY
  - Quality flags por conta
  - Output: package.json auditável
- **Risco:** Baixo — release inicial sem dependentes
- **Rollback:** N/A (primeira versão)
