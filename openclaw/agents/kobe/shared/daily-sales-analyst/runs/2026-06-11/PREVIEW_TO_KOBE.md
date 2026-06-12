# Preview para Kobe — 2026-06-11
**Gerado em:** 2026-06-12T10:15:19.616109+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** APPROVED_WITH_REMARKS
**Prompt Version:** v4.0/mercado-livre
**Data Builder Version:** v1.3
**LLM Used:** True

## Protecoes Ativas
- send_real_enabled=false in config
- require_kobe_approval_for_real_send=true — no approval document found

## Resumo por Recipient

### Yasmin (mercado_livre)
- **Status:** APPROVED_WITH_REMARKS
- **send_allowed:** False
- **llm_used:** True
  - 01-estrategica: LLM
  - 02-tatica: LLM
  - 03-operacional: LLM
  - 04-granular: LLM
  - 05-condensadora: LLM
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** KIT4YW640 (Kit 4 Potes De Vidro 640ml, MLB5402326666) — slack_short_name=null no pacote. Ficou em 6º lugar por pedidos, fora do Top 5 do Slack; sem impacto na mensagem. Adicionar entrada canônica em config/slack-short-names-ml.json na próxima manutenção de produto.
- **Aviso:** KIT3S099 (Kit 3 Potes de Vidro Hermético, MLB4076957145) — slack_short_name=null no pacote. Ficou em 10º lugar, fora do Top 5. Adicionar entrada canônica em config/slack-short-names-ml.json na próxima manutenção.
- **Aviso:** Gate 12 — ADS lag: L05 classificou o insight como 'fato' (fundamentado em 13+ ciclos de memória) em vez de 'hipótese em aberto'. Tecnicamente desvia do fluxo literal que Gate 12 exige, mas o tratamento é funcionalmente equivalente ou superior. Avaliar com equipe de pipeline se L04/L05 deveria usar classificacao='hipotese' para inconsistências de input mesmo quando a inconsistência está bem fundamentada em série histórica — decidiria a regra de Gate 12 para esses casos.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-11/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
