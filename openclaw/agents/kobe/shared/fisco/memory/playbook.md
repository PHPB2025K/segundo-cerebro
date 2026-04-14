# Playbook Fiscal — Fisco

_Regras operacionais aprendidas com operações reais. Playbook vivo — evolui a cada importação processada._

---

## Benchmarks de Distribuição

_Seção atualizada conforme operações reais acontecem._

### Distribuição Histórica por CNPJ
| Período | GB Comércio | Trades | Broglio | Reserva B2B (Filial) |
|---------|------------|--------|---------|---------------------|
| _Sem dados_ | — | — | — | — |

### Tempo Médio de Processamento por Módulo
| Módulo | Tempo Médio | Amostras |
|--------|-------------|----------|
| A — Distribuição | _Sem dados_ | 0 |
| B — NF Transferência | _Sem dados_ | 0 |
| C — NFs Internas | _Sem dados_ | 0 |
| D — Conciliação | _Sem dados_ | 0 |
| E — Monitor Simples | _Sem dados_ | 0 |

---

## Padrões de Exceção

_Exceções recorrentes encontradas na conciliação — padrões que se repetem._

### Exceções Comuns
| Tipo | Padrão | Frequência | Causa Raiz | Resolução Padrão |
|------|--------|-----------|------------|-----------------|
| _Sem dados_ | — | — | — | — |

---

## Regras Operacionais Aprendidas

_Regras derivadas de experiência prática. Cada regra precisa de mínimo 2 ocorrências pra entrar aqui._

### Formato
```
[REGRA-XXX] — Título
Padrão: O que foi observado
Dados: Evidência que sustenta (datas, valores, operações)
Regra: O que fazer quando esse padrão aparecer
Confiança: Alta / Média / Baixa
```

_Nenhuma regra registrada ainda — agente em Fase 1._

---

## Sazonalidade de Faturamento

_Padrões de variação mensal de faturamento por CNPJ — impacta diretamente no cálculo de limites Simples._

| Mês | Tendência | Impacto nos Limites |
|-----|-----------|-------------------|
| Jan-Fev | _A mapear_ | — |
| Mar-Abr | _A mapear_ | — |
| Mai-Jun | _A mapear_ | — |
| Jul (pico histórico) | Alta — R$1M/mês (jul/2025) | Monitorar limites de perto |
| Ago-Set | _A mapear_ | — |
| Out-Nov | _A mapear_ | — |
| Dez | _A mapear_ (Black Friday / Natal) | — |

---

## Checklist Operacional (Referência — documento fiscal v2.0)

A cada nova importação, executar nesta ordem:

**Módulos A→C (trigger: container nacionalizado)**
- [ ] 1. Pedro confirma container nacionalizado em Itajaí
- [ ] 2. Puxar faturamento dos últimos 3 meses via Trader (ML + Shopee + Amazon, por CNPJ)
- [ ] 3. Calcular retenção Matriz: total × 10%
- [ ] 4. Calcular transferência Filial: total × 90%
- [ ] 5. Calcular reserva B2B residual Filial (% B2B do faturamento)
- [ ] 6. Calcular proporção de cada CNPJ Simples no varejo
- [ ] 7. Calcular quantidade para cada CNPJ (arredondar pra inteiro)
- [ ] 8. Validar: soma(Matriz + B2B Filial + GB Comércio + Trades + Broglio) = total importado
- [ ] 9. Calcular preço interno: custo nacionalizado × 1,05
- [ ] 10. Emitir NF transferência Matriz→Filial (90%, CFOP 6.152) — Módulo B
- [ ] 11. Emitir 3 NFs venda interna Filial→Simples — Módulo C
- [ ] 12. Gerar reconciliação estoque contábil × físico por estabelecimento
- [ ] 13. Atualizar controles de estoque no Bling

**Faturamento corrente (rotina)**
- [ ] Varejo B2C: NF emitida pelo CNPJ Simples correspondente (via UpSeller)
- [ ] B2B Filial: NF emitida pela Filial
- [ ] B2B Matriz: NF emitida pela Matriz (com TTD 409 — fora do escopo direto do Fisco)
- [ ] Baixar estoque do estabelecimento emissor

---

## Caso Canônico de Validação (documento fiscal v2.0)

_Usar para validar se os algoritmos do Fisco estão corretos._

**Parâmetros:**
- Importação: 10.000 unidades, R$50,00/un (custo nacionalizado)
- Faturamento 3 meses: B2B R$36k (4%) / Varejo R$864k (96%) / Total R$900k
- Varejo breakdown: GB Comércio 50% / Trades 30% / Broglio 20%

**Resultado esperado:**

| Destino | Cálculo | Qtd Esperada | Valor Esperado |
|---------|---------|-------------|----------------|
| Retenção Matriz | 10.000 × 10% | 1.000 | R$ 50.000 |
| Transferência Filial (NF B) | 10.000 × 90% | 9.000 | R$ 450.000 |
| Reserva B2B Filial | 9.000 × 4% | 360 | — |
| Pool varejo | 9.000 - 360 | 8.640 | — |
| GB Comércio (NF C-1) | 8.640 × 50% | 4.320 | R$ 226.800 |
| Trades (NF C-2) | 8.640 × 30% | 2.592 | R$ 136.080 |
| Broglio (NF C-3) | 8.640 × 20% | 1.728 | R$ 90.720 |
| **TOTAL** | | **10.000** ✅ | |

NFs Filial→Simples: preço unitário R$52,50 (R$50 × 1,05), ICMS R$9,45/un

**Reconciliação pós-operação esperada:**

| Estabelecimento | Contábil | Físico |
|----------------|----------|--------|
| GB Matriz | 1.000 | 0 |
| GB Filial (B2B) | 360 | — |
| GB Comércio | 4.320 | 4.320 |
| Trades | 2.592 | 2.592 |
| Broglio | 1.728 | 1.728 |
| **Total** | **10.000** | — |

---

## Histórico de Containers

_Cada importação processada pelo Fisco gera uma entrada aqui._

| # | Data | Referência | SKUs | Qtd Total | Distribuição Aprovada |
|---|------|-----------|------|-----------|----------------------|
| _Sem dados_ | — | — | — | — | — |

---

_Playbook fiscal vivo. Cada operação enriquece este documento._
