---
title: "TEMPLATE"
created: 2026-04-14
type: template
agent: kobe
status: active
tags:
  - agent/kobe
---

# Operação Fiscal — YYYY-MM-DD

## Módulo(s) Executado(s)
- [ ] A — Distribuição
- [ ] B — NF Transferência Matriz→Filial
- [ ] C — NFs Venda Interna Filial→Simples
- [ ] D — Conciliação
- [ ] E — Monitor Simples

## Contexto / Trigger
- **Tipo:** [importação / cron semanal / sob demanda / alerta]
- **Solicitado por:** [Kobe / cron]
- **Referência:** [container X / período Y / CNPJ Z]

## Dados de Entrada
| Fonte | Dado | Período | Status |
|-------|------|---------|--------|
| Trader | Faturamento por CNPJ | _período_ | ✅/🔴 |
| Bling | _dado necessário_ | — | ✅/🔴 |
| Config | tax-rules.json | — | ✅ |

## Execução

### Módulo A — Distribuição (se aplicável)
| CNPJ | Nome | % Calculado | Quantidade |
|------|------|------------|-----------|
| — | — | — | — |
- **Validação soma = total:** ✅/❌
- **Alertas:** [nenhum / CNPJ inativo / B2B > 50%]

### Módulo B — NF Transferência (se aplicável)
- **NF gerada:** [draft / emitida]
- **CFOP:** 6.152
- **Valor total:** R$ ___
- **Itens:** ___ SKUs, ___ unidades
- **Status SEFAZ:** [N/A (draft) / Autorizada / Rejeitada]

### Módulo C — NFs Internas (se aplicável)
| NF | Destinatário | CNPJ | Valor | Itens | Status |
|----|-------------|------|-------|-------|--------|
| 1 | GB Comércio | 07.194.128/0001-82 | R$ ___ | ___ | draft/emitida |
| 2 | Trades | 45.200.547/0001-79 | R$ ___ | ___ | draft/emitida |
| 3 | Broglio | 63.922.116/0001-06 | R$ ___ | ___ | draft/emitida |

### Módulo D — Conciliação (se aplicável)
- **Período analisado:** ___
- **Total pedidos:** ___
- **Total NFs:** ___
- **Taxa de match:** ___%
- **Exceções:** ___ (detalhar abaixo)

### Módulo E — Monitor Simples (se aplicável)
| CNPJ | Acumulado | % do Teto | Projeção Anual | Status |
|------|-----------|-----------|----------------|--------|
| GB Comércio | R$ ___ | ___% | R$ ___ | 🟢/🟡/🔴/🚨 |
| Trades | R$ ___ | ___% | R$ ___ | 🟢/🟡/🔴/🚨 |
| Broglio | R$ ___ | ___% | R$ ___ | 🟢/🟡/🔴/🚨 |

## Exceções Encontradas
| # | Tipo | Detalhe | Severidade | Ação |
|---|------|---------|-----------|------|
| — | — | — | — | — |

## Resultado
- **Status geral:** ✅ Sucesso / ⚠️ Parcial / 🔴 Falha / 🚨 Bloqueado
- **Tempo de execução:** ___ min
- **Escalações:** [nenhuma / detalhar]

## Aprendizados
- _O que aprendi nesta operação (alimentar lessons.md se relevante)_

## Pendências Geradas
- [ ] _pendência 1_
- [ ] _pendência 2_

---

_Log de auditoria: [referência ao log completo]_
