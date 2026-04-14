---
title: "reconciliation report"
created: 2026-04-14
type: agent
agent: kobe
status: active
tags:
  - agent/kobe
---

# Relatório de Conciliação Fisco

_Gerado pelo Fisco — Módulo D_

---

**Período:** {{periodo_inicio}} a {{periodo_fim}}
**Data de geração:** {{data}}

---

## 1. Resumo

| Métrica | Valor |
|---------|-------|
| Total de pedidos (marketplaces) | {{total_pedidos}} |
| Total de NF-e emitidas | {{total_nfs}} |
| Pedidos com NF correspondente | {{matched}} ({{match_pct}}%) |
| Exceções identificadas | {{total_excecoes}} |

---

## 2. Exceções por Tipo

| Tipo | Quantidade | Impacto |
|------|-----------|---------|
| PEDIDO_SEM_NF | {{qty_pedido_sem_nf}} | Pedido entregue sem NF emitida |
| NF_SEM_PEDIDO | {{qty_nf_sem_pedido}} | NF emitida sem pedido correspondente |
| VALOR_DIVERGENTE | {{qty_valor_div}} | Diferença > R$0,50 entre NF e pedido |
| CNPJ_INCORRETO | {{qty_cnpj_inc}} | NF emitida por CNPJ diferente do esperado |

---

## 3. Exceções por Plataforma

| Plataforma | PEDIDO_SEM_NF | NF_SEM_PEDIDO | VALOR_DIV | CNPJ_INC |
|------------|--------------|---------------|-----------|----------|
| Mercado Livre | {{ml_psn}} | {{ml_nsp}} | {{ml_vd}} | {{ml_ci}} |
| Shopee | {{sh_psn}} | {{sh_nsp}} | {{sh_vd}} | {{sh_ci}} |
| Amazon | {{az_psn}} | {{az_nsp}} | {{az_vd}} | {{az_ci}} |

---

## 4. Exceções por CNPJ

| CNPJ | Nome | Total Exceções |
|------|------|---------------|
| 07.194.128/0001-82 | GB Comércio | {{gb_exc}} |
| 45.200.547/0001-79 | Trades | {{trades_exc}} |
| 63.922.116/0001-06 | Broglio | {{broglio_exc}} |

---

## 5. Detalhamento

### PEDIDO_SEM_NF
| # | Pedido | Plataforma | Valor | Data | CNPJ Esperado |
|---|--------|-----------|-------|------|---------------|
| {{n}} | {{pedido_id}} | {{plat}} | R$ {{valor}} | {{data}} | {{cnpj}} |

### NF_SEM_PEDIDO
| # | NF | Chave de Acesso | Valor | Data | CNPJ Emissor |
|---|-----|----------------|-------|------|-------------|
| {{n}} | {{nf_num}} | {{chave}} | R$ {{valor}} | {{data}} | {{cnpj}} |

### VALOR_DIVERGENTE
| # | Pedido | NF | Valor Pedido | Valor NF | Diferença |
|---|--------|-----|-------------|----------|-----------|
| {{n}} | {{pedido_id}} | {{nf_num}} | R$ {{val_ped}} | R$ {{val_nf}} | R$ {{diff}} |

---

## 6. Recomendações

{{recomendacoes}}

---

_Este relatório é informativo. O Fisco NÃO corrige exceções automaticamente. Todas as correções requerem revisão humana._

_Log de auditoria: {{log_ref}}_
