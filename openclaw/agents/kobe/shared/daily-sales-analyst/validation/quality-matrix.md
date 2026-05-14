# Quality Matrix — Phase 5

**Avaliado em:** 2026-05-14
**Modo:** Fallback deterministico (sem LLM)

---

## Legenda

- **OK**: Criterio atendido
- **PARCIAL**: Atendido com limitacoes
- **FALHA**: Nao atendido
- **N/A**: Nao aplicavel (ex: pipeline bloqueada)
- **LIMITE_FALLBACK**: Nao avaliavel por limitacao do modo fallback

---

## Matrix por Data/Recipient

### 2026-05-11

| Criterio | Lucas (Shopee) | Yasmin (ML) | Leonardo (Amazon) |
|----------|---------------|-------------|-------------------|
| Data Readiness correto | OK | OK | OK |
| Profundidade da analise | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) |
| Fidelidade aos dados | OK | OK | OK |
| Ausencia de SKU cru | OK | OK | PARCIAL* |
| Produto correto | LIMITE_FALLBACK | LIMITE_FALLBACK | LIMITE_FALLBACK |
| ASIN/titulo correto (Amazon) | N/A | N/A | LIMITE_FALLBACK** |
| Separacao contas Shopee | OK (3 contas) | N/A | N/A |
| Ausencia mistura plataformas | OK | OK | OK |
| Prioridades acionaveis | LIMITE_FALLBACK | LIMITE_FALLBACK | LIMITE_FALLBACK |
| Bloqueios corretos | OK (nenhum) | OK (nenhum) | OK (nenhum) |
| Clareza Slack final | LIMITE_FALLBACK (placeholder) | LIMITE_FALLBACK (placeholder) | LIMITE_FALLBACK (placeholder) |
| Utilidade para destinatario | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) |

*Layer 03 lista top products com titulo do pedido, nao SKU interno — parcialmente ok.
**Fallback nao resolve ASIN para nome comercial legivel.

### 2026-05-12

| Criterio | Lucas (Shopee) | Yasmin (ML) | Leonardo (Amazon) |
|----------|---------------|-------------|-------------------|
| Data Readiness correto | OK | OK | OK |
| Profundidade da analise | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) |
| Fidelidade aos dados | OK | OK | OK |
| Ausencia de SKU cru | OK | OK | PARCIAL |
| Produto correto | LIMITE_FALLBACK | LIMITE_FALLBACK | LIMITE_FALLBACK |
| ASIN/titulo correto (Amazon) | N/A | N/A | LIMITE_FALLBACK |
| Separacao contas Shopee | OK (3 contas) | N/A | N/A |
| Ausencia mistura plataformas | OK | OK | OK |
| Prioridades acionaveis | LIMITE_FALLBACK | LIMITE_FALLBACK | LIMITE_FALLBACK |
| Bloqueios corretos | OK (nenhum) | OK (nenhum) | OK (nenhum) |
| Clareza Slack final | LIMITE_FALLBACK (placeholder) | LIMITE_FALLBACK (placeholder) | LIMITE_FALLBACK (placeholder) |
| Utilidade para destinatario | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) | LIMITE_FALLBACK (2/5) |

### 2026-05-13 (BLOCKED)

| Criterio | Lucas (Shopee) | Yasmin (ML) | Leonardo (Amazon) |
|----------|---------------|-------------|-------------------|
| Data Readiness correto | OK (NOT_READY) | OK (NOT_READY) | OK (NOT_READY) |
| Profundidade da analise | N/A (bloqueado) | N/A (bloqueado) | N/A (bloqueado) |
| Fidelidade aos dados | N/A | N/A | N/A |
| Ausencia de SKU cru | N/A | N/A | N/A |
| Produto correto | N/A | N/A | N/A |
| ASIN/titulo correto (Amazon) | N/A | N/A | N/A |
| Separacao contas Shopee | N/A | N/A | N/A |
| Ausencia mistura plataformas | N/A | N/A | N/A |
| Prioridades acionaveis | N/A | N/A | N/A |
| Bloqueios corretos | OK (bloqueio correto) | OK (bloqueio correto) | OK (bloqueio correto) |
| Clareza Slack final | N/A (nao gerado) | N/A (nao gerado) | N/A (nao gerado) |
| Utilidade para destinatario | OK (3/5 — evitou desinformacao) | OK (3/5) | OK (3/5) |

---

## Avaliacao Honesta

### O que funciona bem (infraestrutura)
1. **Data Readiness** funciona corretamente: DADOS_OK quando ok, NOT_READY quando volume fora da banda
2. **Bloqueio** funciona: pipeline para quando deve parar
3. **Separacao de contas Shopee** funciona: 3 contas distintas nos artefatos
4. **Isolamento de plataforma** funciona: nenhuma mistura detectada
5. **Artefatos auditaveis**: 8 layers por recipient, JSON valido, markdown legivel
6. **send_real_allowed=false**: enforced em todos os cenarios

### O que NAO funciona (qualidade analitica)
1. **Sem profundidade**: Artefatos sao dumps de dados, nao analises
2. **Sem prioridades**: Fallback nao sabe o que e importante
3. **Sem contexto de produto**: Nao resolve ASIN para nome comercial
4. **Sem Slack formatado**: Placeholder, nao mensagem final
5. **Sem insight acionavel**: Lucas/Yasmin/Leonardo nao conseguiriam agir com base nestes artefatos
6. **Utilidade real: 2/5**: Dados corretos mas sem valor analitico

### Veredito
**Infraestrutura: APROVADA** — Pipeline, artefatos, bloqueios, schema, auditoria funcionam.
**Qualidade analitica: PENDENTE** — Requer integracao LLM (Fase 6+) para valor real.
