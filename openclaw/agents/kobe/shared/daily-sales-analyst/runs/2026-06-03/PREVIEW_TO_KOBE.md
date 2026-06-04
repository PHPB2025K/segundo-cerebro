# Preview para Kobe — 2026-06-03
**Gerado em:** 2026-06-04T16:48:24.159022+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** APPROVED_WITH_REMARKS
**Prompt Version:** v4.0/shopee
**Data Builder Version:** v1.3
**LLM Used:** True

## Protecoes Ativas
- send_real_enabled=false in config
- require_kobe_approval_for_real_send=true — no approval document found

## Resumo por Recipient

### Lucas (shopee)
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
- **Aviso:** Abreviações inglesas 'NFR' e 'threshold' foram introduzidas pela L05 e reproduzidas fielmente pela L06 — ajuste deve ser propagado ao template da L05 para evitar reincidência sistêmica nos próximos ciclos desta e das demais contas Shopee.
- **Aviso:** L06 inseriu condição 'escalar_se' de prioridades dentro do bullet de análise — template de L06 deve explicitar regra de não cross-section entre analise_final_condensada e prioridades_condensadas.
- **Aviso:** Referência ao papel hipotetizado ('Volume/Giro') foi omitida do insight 3 na conversão L05→L06 — template de L06 deve preservar menções ao papel da tese seed quando presentes nos insights da L05, especialmente em primeiro ciclo de pipeline com memória vazia.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/shopee-budamix-store/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
