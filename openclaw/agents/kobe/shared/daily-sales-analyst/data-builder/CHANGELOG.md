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

## v1.1 — 2026-05-14

- **Autor:** Kobe / decisão Pedro
- **Tipo:** Ajuste fino de readiness
- **Motivo:** Pedro decidiu que, no caso observado em 2026-05-13, o spike positivo de Amazon não deve bloquear o pipeline inteiro; deve virar `DADOS_PARCIAIS`. Também definiu que anomalias localizadas devem bloquear apenas o responsável afetado quando houver bloqueio real por conta/plataforma.
- **Escopo:** Regra de volume do Layer 0.
- **Mudanças:**
  - Spike positivo fora da banda 30d/60d passa a ser `partial`, não `fail`.
  - Queda fora das bandas, mas acima do piso crítico de 30% da média 30d, também passa a ser `partial`.
  - Apenas queda abaixo do piso crítico (`<30%` da média 30d; `pct_change < -70%`) permanece `fail`.
  - Package gerado com `data_builder_version=v1.1` e `schema_version=daily-sales-data-package/v1.1`.
- **Validação:** Reprocessado 2026-05-13; readiness mudou de `NOT_READY` para `DADOS_PARCIAIS`, com Amazon +68,5% marcada como spike positivo parcial e Shopee Conta 2 -62,9% marcada como parcial acima do piso crítico.
- **Risco:** Baixo/médio — reduz bloqueios falsos por dia legitimamente forte, preservando bloqueio para quedas críticas.
- **Rollback:** Voltar `DATA_BUILDER_VERSION`/`SCHEMA_VERSION` para v1.0 e restaurar tratamento antigo de outside-bands como `fail`.
