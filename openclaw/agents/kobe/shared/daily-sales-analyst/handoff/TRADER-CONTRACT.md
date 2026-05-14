# Contrato de Delegação — Trader ↔ Daily Sales Analyst

**Versão:** 1.0
**Data:** 2026-05-14
**Status:** Aprovado para implementação
**Checkpoint Kobe:** Pendente

---

## 1. Partes

| Papel | Agente | Responsabilidade |
|-------|--------|-----------------|
| Dono/Orquestrador | **Trader** | Aciona DSA, decide envio, envia Slack, escala Kobe |
| Executor | **Daily Sales Analyst (DSA)** | Executa pipeline Layer 0 + 7 camadas, devolve artefatos |
| Governança | **Kobe** | Valida rollout, bloqueios, mudanças estratégicas, divergências graves |
| Decisor humano | **Pedro** | Decisão final, pode desligar tudo a qualquer momento |

---

## 2. Hierarquia Operacional

1. **Cron** aciona o **Trader**, nunca o DSA diretamente.
2. **Trader** monta o payload de input e chama o DSA.
3. **DSA** executa o pipeline e devolve o output padronizado.
4. **Trader** decide envio por destinatário/plataforma com base no output.
5. **Kobe** entra em bloqueios, rollout, mudança estratégica e divergência grave.

O DSA **não tem autonomia de canal**:
- Não fala com Pedro.
- Não fala com funcionários.
- Não envia Slack.
- Não toma decisão de rollout.
- Não altera regra permanente sem governança.

---

## 3. Input — O que o Trader envia ao DSA

Schema formal: `input-schema.json`

O Trader envia:
- Data analisada (YYYY-MM-DD, BRT).
- Modo de execução (`DRY_RUN`, `SHADOW`, `PREVIEW_TO_KOBE`, `SEND_CANDIDATE`, `PRODUCTION_SEND`).
- Pacote do Layer 0 (caminho ou objeto inline).
- Status de Data Readiness (`DADOS_OK`, `DADOS_PARCIAIS`, `NOT_READY`).
- Destinatários solicitados (`lucas`, `yasmin`, `leonardo`).
- Versão de prompt (`current` ou `vX.Y.Z`).
- Versão do Data Builder.
- Referências de contexto (memória, regras, Himmel) quando aplicável.
- Identificação do solicitante (`Trader`).

---

## 4. Output — O que o DSA devolve ao Trader

Schema formal: `output-schema.json`

O DSA devolve:
- `global_status` — agregação visual/auditável da rodada.
- `global_failure` — indica falha sistêmica, se houver.
- `send_real_allowed` — booleano global de permissão de envio.
- `date`, `mode`, `prompt_version`, `data_builder_version`.
- `recipients` — status individual por destinatário/plataforma:
  - `platform`, `status`, `send_allowed`
  - `slack_payload` — mensagem Slack pronta
  - `layers` — resultado de cada camada
  - `qa` — resultado do QA Gate
  - `blockers`, `warnings`
- `escalation` — se escalonamento é necessário e motivo.
- `memory_updates` — atualizações de memória sugeridas e aplicadas.
- `audit_refs` — referências para auditoria.

---

## 5. Regra Crítica de Decisão de Envio

> **`global_status` é agregação visual/auditável. NÃO decide envio.**

A decisão de envio é **sempre por destinatário/plataforma**, usando:
- `recipients.<nome>.status`
- `recipients.<nome>.send_allowed`

### Regras:
1. O Trader **nunca** envia ou bloqueia olhando apenas `global_status`.
2. Uma plataforma bloqueada **não impede** envio das outras aprovadas.
3. Só aborta **tudo** quando `global_failure` indicar falha sistêmica.

### Execução parcial:
- Lucas pode receber mesmo se Yasmin bloqueou.
- Yasmin pode receber mesmo se Leonardo bloqueou.
- Leonardo pode receber mesmo se Lucas bloqueou.

### Quando abortar tudo (`global_failure` ≠ `false`):
- Layer 0 global `NOT_READY`
- Timezone incorreto
- Fonte canônica divergente de forma sistêmica
- Runner quebrado
- Prompt version inválida
- Kill switch global ativo

---

## 6. Modos de Execução

| Modo | Gera análise | Envia Slack | Para quem |
|------|-------------|-------------|-----------|
| `DRY_RUN` | Sim | Não | Ninguém |
| `SHADOW` | Sim | Não | Ninguém (salva logs) |
| `PREVIEW_TO_KOBE` | Sim | Só para Kobe/Pedro | Revisão interna |
| `SEND_CANDIDATE` | Sim | Se QA + Layer 0 + send_real_allowed | Funcionários |
| `PRODUCTION_SEND` | Sim | Se QA + Layer 0 + send_real_allowed | Funcionários |

---

## 7. Fluxo de Execução

```
Cron → Trader
         │
         ├── 1. Verifica kill switch
         ├── 2. Verifica config (enabled, send_real_enabled, destinatários)
         ├── 3. Monta input payload
         ├── 4. Chama DSA
         │       │
         │       ├── Layer 0 — Data Builder
         │       ├── Camada 1 — Estratégica
         │       ├── Camada 2 — Tática
         │       ├── Camada 3 — Operacional
         │       ├── Camada 4 — Granular
         │       ├── Camada 5 — Condensadora
         │       ├── Camada 6 — Slack Writer
         │       └── Camada 7 — QA Gate
         │
         ├── 5. Recebe output padronizado
         ├── 6. Avalia global_failure
         ├── 7. Para cada destinatário: avalia status + send_allowed
         ├── 8. Envia Slack (se permitido)
         ├── 9. Registra logs
         └── 10. Escala Kobe (se necessário)
```

---

## 8. Responsabilidades Pós-Execução

### Trader:
- Registra resultado da rodada.
- Atualiza `sent-reports.md` se houve envio.
- Aplica `memory_updates` aprovados.
- Escala Kobe se `escalation.required = true`.

### DSA:
- Não executa nenhuma ação pós-retorno.
- Toda ação pós é responsabilidade do Trader.

---

## 9. Versionamento

- Input/output schemas são versionados junto com este contrato.
- Mudança estrutural de schema = nova versão major do contrato.
- Ajuste fino = versão minor.
- Correção pontual = patch.

---

## 10. Referências

- Schema de input: `handoff/input-schema.json`
- Schema de output: `handoff/output-schema.json`
- Exemplos: `handoff/examples/`
- Regras de escalonamento: `handoff/escalation-rules.md`
- Escopo de integração: `handoff/TRADER-INTEGRATION-SCOPE.md`
- Plano completo: `/root/segundo-cerebro/reports/daily-sales-report-v2/PLANO-IMPLEMENTACAO-DAILY-SALES-ANALYST.md`
