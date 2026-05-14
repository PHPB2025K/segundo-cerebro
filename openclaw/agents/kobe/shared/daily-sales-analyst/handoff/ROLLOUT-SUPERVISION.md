# Rollout Supervisionado — Daily Sales Analyst

## Filosofia

Nenhum envio real acontece sem supervisão explícita. O rollout segue etapas progressivas com gates de aprovação.

## Etapas do Rollout

### Etapa 1: Preview Local (ATUAL)
- **Modo:** `--preview-to-kobe`
- **O que faz:** Gera artefatos + `PREVIEW_TO_KOBE.md` local.
- **Envio externo:** NENHUM.
- **Gate:** Kobe/Pedro revisam artefatos e aprovam.
- **Config:** `send_real_enabled=false`, `preview_to_kobe_enabled=true`

### Etapa 2: Send Candidate (FUTURO)
- **Modo:** `--send-candidate`
- **O que faz:** Gera artefatos + marca como candidato a envio.
- **Envio externo:** NENHUM (bloqueado por config).
- **Gate:** Kobe revisa candidate, aprova envio manual.
- **Config:** `send_real_enabled=false`, `require_kobe_approval_for_real_send=true`

### Etapa 3: Envio Supervisionado (FUTURO)
- **Modo:** `--production-send`
- **Pré-requisitos:**
  - `send_real_enabled=true`
  - `llm_layers_enabled=true` (ou fallback aceito explicitamente)
  - `require_kobe_approval_for_real_send=true` com approval document presente
  - LLM layers funcionando (não apenas fallback)
- **Gate:** Kobe aprova cada envio individualmente.

### Etapa 4: Produção Autônoma (FUTURO DISTANTE)
- **Modo:** `--production-send` com cron
- **Pré-requisitos:** Todas as etapas anteriores com histórico positivo.
- **Gate:** `require_kobe_approval_for_real_send=false` (Kobe decide quando).

## Regras de Segurança

1. **Nunca pular etapas.** Cada etapa requer aprovação antes de avançar.
2. **Rollback imediato** se qualquer problema for detectado.
3. **Kill switch** sempre disponível para desligar tudo.
4. **Sem cron** até Etapa 4 ser explicitamente aprovada.
5. **Sem envio externo** (Slack/Telegram) até Etapa 3.

## Critérios para avançar etapa

| De → Para | Critério |
|---|---|
| 1 → 2 | Preview revisado e aprovado por Kobe. LLM layers testadas. |
| 2 → 3 | Candidate revisado. LLM produzindo qualidade aceitável. Kobe aprova. |
| 3 → 4 | Histórico de envios sem incidentes. Kobe remove approval requirement. |

## Estado Atual

- **Etapa ativa:** 1 (Preview Local)
- **Próxima:** 2 (Send Candidate) — aguardando integração LLM profunda.
- **send_real_enabled:** false
- **llm_layers_enabled:** false
- **require_kobe_approval_for_real_send:** true
