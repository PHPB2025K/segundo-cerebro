# Skill: Motor de Distribuição (Módulo A) — [[openclaw/agents/fisco/IDENTITY|Fisco]]

_Calcula a distribuição proporcional de estoque importado entre os CNPJs da GB._

---

## Trigger
- Nova importação nacionalizada (Pedro confirma container)
- Solicitação manual do Kobe

## Inputs
- Faturamento dos últimos 3 meses por canal e por CNPJ (via Trader)
- Quantidade total de cada SKU importado (da DI/packing list)
- Custo nacionalizado unitário (da DI — chega pronto, gerado pela Open Trade via Conta e Ordem)

## Modelo de Distribuição (90/10)

O estoque importado é dividido em dois pools:

| Pool | % | Destino | Propósito |
|------|---|---------|-----------|
| Retenção Matriz | 10% fixo | GB Matriz (contábil) | B2B com benefício TTD 409 |
| Transferência Filial | 90% fixo | GB Filial (NF transferência) | Distribuição pra CNPJs Simples + B2B residual |

Dentro dos 90% da Filial, a distribuição é dinâmica:
- Reserva B2B residual (Filial): proporcional ao faturamento B2B da Filial
- Varejo (CNPJs Simples): proporcional ao faturamento de cada CNPJ

**Nota:** Estoque físico 100% vai pra Pedreira. A Matriz retém 10% apenas contabilmente.

## Algoritmo

```
ETAPA 1 — Split 90/10
1. quantidade_total = total de unidades importadas
2. retencao_matriz = quantidade_total × 10% (arredondar pra inteiro)
3. transferencia_filial = quantidade_total - retencao_matriz

ETAPA 2 — Dados de faturamento
4. Puxar faturamento dos últimos 3 meses via Trader:
   a. faturamento_total = ML + Shopee + Amazon (todos os CNPJs)
   b. faturamento_b2b_filial = vendas B2B faturadas pela Filial (via Bling)
   c. faturamento_varejo = faturamento dos 3 CNPJs Simples
   d. Para cada CNPJ Simples: faturamento_cnpj

ETAPA 3 — Distribuição dos 90% da Filial
5. pct_b2b_filial = faturamento_b2b_filial / (faturamento_b2b_filial + faturamento_varejo)
6. reserva_b2b_filial = transferencia_filial × pct_b2b_filial (arredondar)
7. quantidade_varejo = transferencia_filial - reserva_b2b_filial

ETAPA 4 — Distribuição entre CNPJs Simples
8. Para cada CNPJ Simples:
   a. pct_cnpj = faturamento_cnpj / faturamento_varejo
   b. quantidade_cnpj = quantidade_varejo × pct_cnpj (arredondar)
9. Ajustar arredondamento: diferença de ±1 vai pro CNPJ com maior faturamento

ETAPA 5 — Validação
10. OBRIGATÓRIO: retencao_matriz + reserva_b2b_filial + soma(quantidade_cnpj) = quantidade_total
11. Se não bater → PARAR e reportar erro
```

## Proporções Benchmark (referência de sanidade)

Valores reais da operação GB (documento fiscal v2.0, mar/2026). Desvios significativos devem ser sinalizados:

| Métrica | Benchmark | Alerta se |
|---------|-----------|-----------|
| B2B total (Matriz + Filial) | ~4% do faturamento | > 15% (mudança no perfil) |
| Retenção Matriz | 10% fixo | Qualquer desvio (é fixo) |
| GB Comércio (do varejo) | ~50% | Desvio > 15pp |
| Trades (do varejo) | ~30% | Desvio > 15pp |
| Broglio (do varejo) | ~20% | Desvio > 15pp |

## Exemplo Completo (caso canônico de validação)

**Dados:** 10.000 unidades, R$ 50,00/un, R$ 500.000 total

| Faturamento (3 meses) | Valor | % |
|------------------------|-------|---|
| B2B (Filial) | R$ 36.000 | 4% |
| Varejo (Simples) | R$ 864.000 | 96% |
| Total | R$ 900.000 | 100% |

| CNPJ Simples | Faturamento | % do Varejo |
|-------------|-------------|-------------|
| GB Comércio | R$ 432.000 | 50% |
| Trades | R$ 259.200 | 30% |
| Broglio | R$ 172.800 | 20% |

| Destino | Cálculo | Qtd | Valor |
|---------|---------|-----|-------|
| Retenção Matriz (B2B contábil) | 10.000 × 10% | 1.000 | R$ 50.000 |
| Transferência Filial | 10.000 × 90% | 9.000 | R$ 450.000 |
| Reserva B2B Filial | 9.000 × 4% | 360 | R$ 18.000 |
| Pool varejo | 9.000 - 360 | 8.640 | — |
| GB Comércio | 8.640 × 50% | 4.320 | R$ 226.800 |
| Trades | 8.640 × 30% | 2.592 | R$ 136.080 |
| Broglio | 8.640 × 20% | 1.728 | R$ 90.720 |
| **TOTAL** | — | **10.000** | — |

Preço interno unitário (NFs Filial→Simples): R$ 52,50 (R$ 50,00 × 1,05)

## Regra de Flexibilidade B2B

Se não houver demanda B2B suficiente para consumir a reserva da Filial:
- A parcela B2B não vendida pode ser redistribuída para os CNPJs Simples
- Requer nova rodada de NFs de venda interna (Módulo C)
- A retenção de 10% da Matriz é FIXA — não se redistribui

## Output
- Tabela de distribuição: SKU × CNPJ × quantidade × preço unitário
- Retenção Matriz: SKU × quantidade (contábil, sem NF de saída)
- Percentuais calculados com fontes de dados
- Reconciliação: estoque contábil × físico por estabelecimento
- Log auditável do cálculo completo

## Validações
- Soma das partes = total importado (tolerância zero)
- Retenção Matriz = exatamente 10% (arredondado)
- Transferência Filial = exatamente 90% (arredondado)
- Nenhum CNPJ recebe quantidade negativa
- Se faturamento de algum CNPJ = 0 nos últimos 3 meses → alertar (CNPJ inativo)
- Se % B2B total > 15% → alertar (mudança de perfil)
- Se desvio de proporção entre CNPJs > 15pp do benchmark → alertar

## Dependências
- Trader: dados de faturamento
- Bling API: faturamento B2B da Filial
- Config: tax-rules.json (transfer_pct, retention_pct, lookback_months, benchmarks)
