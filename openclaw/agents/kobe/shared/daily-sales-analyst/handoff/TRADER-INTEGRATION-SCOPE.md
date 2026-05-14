# Escopo de Integração Trader ↔ DSA

**Versão:** 1.0
**Data:** 2026-05-14
**Status:** Documentação de escopo — NÃO implementa envio nem cron.

---

## 1. Objetivo

Documentar o escopo exato de modificações que o Trader precisará sofrer para integrar o DSA, e o sincronismo com o rollout.

**Esta Fase 3 NÃO implementa envio, cron, runner ou modificação em scripts de produção.**

---

## 2. Estado Atual

### Cron existente
- **Nome:** "Daily Sales Report — Slack Funcionários"
- **Status:** PAUSADO
- **Script:** `send-daily-sales-v2-slack-funcionarios.py`
- **Comportamento:** Wrapper/script solto que gera e envia report diretamente
- **Decisão:** Só deve ser religado em rollout supervisionado (Fase 6)

### Script de fallback
- **Arquivo:** `send-daily-sales-v2-slack-funcionarios.py`
- **Status:** Permanece como fallback histórico até rollout completo do DSA
- **Decisão:** Não deve ser alterado ou removido até que o fluxo Trader → DSA esteja validado e em produção

---

## 3. Transição Futura: Script Solto → Fluxo Trader → DSA

A troca será de:
```
Cron → send-daily-sales-v2-slack-funcionarios.py (script solto, sem contexto operacional)
```

Para:
```
Cron → Trader → DSA (pipeline com contexto, memória, QA e auditoria)
```

### O que muda:
1. Cron passa a chamar o Trader, não o script diretamente.
2. Trader monta input payload conforme `input-schema.json`.
3. Trader chama DSA (via runner ou invocação direta).
4. DSA executa Layer 0 + 7 camadas.
5. DSA devolve output conforme `output-schema.json`.
6. Trader avalia output e decide envio por destinatário.
7. Trader registra resultado, aplica memória, escala se necessário.

### O que NÃO muda:
- Trader continua dono do Daily Sales Report.
- Envio real continua sendo responsabilidade do Trader.
- Pedro continua podendo desligar tudo.

---

## 4. Arquivos/Scripts do Trader a Alterar (Fase Futura)

### Fase 4 — Runner dry-run
| Arquivo | Alteração | Fase |
|---------|-----------|------|
| `scripts/daily-sales-analyst-runner.py` | **CRIAR** — runner que executa pipeline DSA | Fase 4 |

### Fase 6 — Rollout supervisionado
| Arquivo/Config | Alteração | Fase |
|----------------|-----------|------|
| Cron "Daily Sales Report" | Reconfigurar para chamar Trader → DSA em vez de script solto | Fase 6 |
| `send-daily-sales-v2-slack-funcionarios.py` | Manter como fallback. Desativar após rollout estável | Fase 6+ |
| `shared/daily-sales-analyst/config/daily-sales-analyst.json` | Ativar `send_real_enabled: true` | Fase 6 |

### Contexto do Trader
| Item | Alteração | Fase |
|------|-----------|------|
| Trader memory/rules | Registrar que DSA é executor do Daily Sales Report | Fase 4 |
| Trader handoff knowledge | Carregar contrato e schemas do handoff | Fase 4 |
| Trader escalation flow | Implementar escalonamento para Kobe conforme `escalation-rules.md` | Fase 4-6 |

---

## 5. Comandos/Contratos para Fase 4 e Fase 6

### Fase 4 — O que o Trader deverá chamar

```
# Invocação do runner dry-run
python3 scripts/daily-sales-analyst-runner.py \
  --date 2026-05-14 \
  --mode DRY_RUN \
  --recipients lucas,yasmin,leonardo \
  --prompt-version current
```

O runner:
1. Carrega config de `shared/daily-sales-analyst/config/daily-sales-analyst.json`.
2. Verifica kill switch.
3. Executa Layer 0 (Data Builder).
4. Avalia Data Readiness.
5. Se `DADOS_OK` ou `DADOS_PARCIAIS`: executa 7 camadas por destinatário.
6. Se `NOT_READY`: retorna output com `global_failure = "layer0"`.
7. Salva artefatos em `shared/daily-sales-analyst/runs/YYYY-MM-DD/`.
8. Retorna output conforme `output-schema.json`.

### Fase 6 — O que o Trader deverá chamar

```
# Invocação em produção
python3 scripts/daily-sales-analyst-runner.py \
  --date 2026-05-14 \
  --mode PRODUCTION_SEND \
  --recipients lucas,yasmin,leonardo \
  --prompt-version current
```

Diferenças vs Fase 4:
- `send_real_allowed` pode ser `true` (depende de QA + config).
- Trader avalia output e envia Slack se `send_allowed = true` por destinatário.
- Trader registra em `sent-reports.md`.
- Trader escala Kobe se `escalation.required = true`.

---

## 6. O que Fase 3 NÃO implementa

| Item | Status |
|------|--------|
| Runner (scripts/daily-sales-analyst-runner.py) | NÃO criado |
| Cron reativado | NÃO |
| Envio Slack real | NÃO |
| Envio Slack preview | NÃO |
| Modificação em scripts de produção | NÃO |
| Modificação no Trader | NÃO |
| Canal Slack criado/alterado | NÃO |
| send_real_enabled ativado | NÃO |

---

## 7. Pré-condições para Fase 4

Antes de criar o runner:
1. Este contrato (Fase 3) deve estar aprovado por Kobe.
2. Schemas validados estruturalmente.
3. Exemplos compatíveis com schemas.
4. Escalation rules revisadas.
5. Trader ciente do contrato.

---

## 8. Referências

- Contrato: `handoff/TRADER-CONTRACT.md`
- Input schema: `handoff/input-schema.json`
- Output schema: `handoff/output-schema.json`
- Exemplos: `handoff/examples/`
- Escalation: `handoff/escalation-rules.md`
- Config: `config/daily-sales-analyst.json`
- Plano completo: `/root/segundo-cerebro/reports/daily-sales-report-v2/PLANO-IMPLEMENTACAO-DAILY-SALES-ANALYST.md`
