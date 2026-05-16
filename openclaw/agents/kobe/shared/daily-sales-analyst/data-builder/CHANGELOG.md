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

## v1.2 — 2026-05-16

- **Autor:** Kobe / decisão Pedro
- **Tipo:** Endurecimento estrutural do contrato de identidade de produto
- **Motivo:** eliminar de forma definitiva dois erros de origem da Layer 0: (1) consolidação indevida por família genérica quando existe variação vendável real; (2) vazamento de título SEO longo/SKU cru para análises e Slack em vez de nome curto comercial confiável.
- **Escopo:** contrato de Top Produtos e identidade de produto do Layer 0 + validação fail-closed no runner.
- **Mudanças:**
  - `data_builder_version` promovida para `v1.2` e `schema_version` para `daily-sales-data-package/v1.2`.
  - Layer 0 agora entrega, por Top Produto: `raw_sku`, `raw_title`, `mapped_variation_sku`, `parent_family`, `short_product_name`, `confidence`, `mapping_status` e `mapping_reason`.
  - IMB501 passou a mapear deterministamente por variação vendável (`IMB501P`, `IMB501C`, `IMB501V`) usando SKU bruto, aliases conhecidos e título como evidência complementar.
  - Quando há conflito ou baixa confiança, o item fica explícito como inseguro/ambíguo em vez de ser consolidado silenciosamente em família genérica.
  - Produtos revisados do catálogo geral passaram a usar mapa determinístico de nome curto comercial na própria Layer 0.
  - Runner do DSA agora bloqueia package antigo ou Top Produto sem `mapped_variation_sku` + `short_product_name` confiáveis.
  - Camadas determinísticas visíveis do runner passaram a usar `short_product_name` como nome canônico do produto.
- **Validação:** `py_compile` OK; casos críticos cobrindo IMB501 por SKU, IMB501 por título, SKU revisado do catálogo e fallback genérico passaram; validador do runner confirmou `[]` para package compatível com o novo contrato.
- **Risco:** Médio — endurece o gate e pode bloquear packages antigos ou produtos ainda não mapeados corretamente, mas evita erro silencioso nas camadas analíticas.
- **Rollback:** restaurar `v1.1`, schema `daily-sales-data-package/v1.1` e remover a validação fail-closed do runner.
