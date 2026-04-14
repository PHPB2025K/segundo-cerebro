---
title: "distribution report"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Relatório de Distribuição de Estoque

_Gerado pelo Fisco — Módulo A_

---

**Data:** {{data}}
**Importação:** {{referencia_importacao}}
**Período de referência:** Últimos {{lookback_months}} meses ({{periodo_inicio}} a {{periodo_fim}})

---

## 1. Faturamento de Referência

| Canal | Faturamento (3 meses) | % do Total |
|-------|----------------------|------------|
| Mercado Livre | R$ {{ml_fat}} | {{ml_pct}}% |
| Shopee | R$ {{shopee_fat}} | {{shopee_pct}}% |
| Amazon | R$ {{amazon_fat}} | {{amazon_pct}}% |
| **Total** | **R$ {{total_fat}}** | **100%** |

### Breakdown B2B vs Varejo

| Tipo | Faturamento | % |
|------|-------------|---|
| B2B (Filial) | R$ {{b2b_fat}} | {{b2b_pct}}% |
| Varejo (Simples) | R$ {{varejo_fat}} | {{varejo_pct}}% |

### Distribuição por CNPJ Simples

| CNPJ | Nome | Faturamento Varejo | % do Varejo |
|------|------|-------------------|-------------|
| 07.194.128/0001-82 | GB Comércio | R$ {{gb_fat}} | {{gb_pct}}% |
| 45.200.547/0001-79 | Trades | R$ {{trades_fat}} | {{trades_pct}}% |
| 63.922.116/0001-06 | Broglio | R$ {{broglio_fat}} | {{broglio_pct}}% |

---

## 2. Distribuição Calculada

| SKU | Descrição | Qtd Total | Reserva Filial (B2B) | GB Comércio | Trades | Broglio |
|-----|-----------|-----------|---------------------|-------------|--------|---------|
| {{sku}} | {{desc}} | {{qtd_total}} | {{qtd_b2b}} | {{qtd_gb}} | {{qtd_trades}} | {{qtd_broglio}} |

**Total:** {{total_unidades}} unidades → Filial: {{total_b2b}} | GB Comércio: {{total_gb}} | Trades: {{total_trades}} | Broglio: {{total_broglio}}

**Validação:** soma das partes = total importado ✅/❌

---

## 3. NFs a Emitir

Com base nesta distribuição, serão geradas:
- 1 NF Transferência Matriz→Filial (CFOP 6.152, {{total_unidades}} unidades)
- 3 NFs Venda Interna Filial→Simples:
  - GB Comércio: {{total_gb}} unidades, valor R$ {{valor_gb}}
  - Trades: {{total_trades}} unidades, valor R$ {{valor_trades}}
  - Broglio: {{total_broglio}} unidades, valor R$ {{valor_broglio}}

---

_Log de auditoria: {{log_ref}}_
