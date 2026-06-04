# Preview para Kobe — 2026-06-03
**Gerado em:** 2026-06-04T15:47:52.098955+00:00
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
- **Aviso:** Gate 6: L05 Insight 1 usa 'figuram em ruptura prospectiva'; Slack usa 'estão em ruptura prospectiva' — mudança de verbo não altera sentido analítico ('estar em' vs 'figurar em' referem ao mesmo estado). Não constitui Minor porque o conectivo central, tese, números e enquadramento de contraste foram preservados integralmente.
- **Aviso:** Gate 6: L05 Insight 3 usa 'vai erodir' (certeza futura); Slack usa 'pode erodir' (condicional). Mudança correta e explicitamente documentada nas Decisões de formatação para preservar nuance de classificacao='risco latente'. Não constitui Minor — é aplicação obrigatória da regra de classificação.
- **Aviso:** Gate 13: L05.status_tese_seed_dia.mudou_em_relacao_ao_ciclo_anterior=false (primeiro ciclo formal, sem ciclo anterior). Trigger de Minor do Gate 13 não se aplica (Minor só ativado quando mudou=true e Slack silencia). Status OK.
- **Aviso:** Gate 12a: ads_summary.campaigns_active_count=null (não >0) e ads_summary.status='unavailable' — condição de Maior do Gate 12a não disparada (requer campaigns_active_count>0 E spend=0). Slack cita 'Shopee Ads inacessível' sem dados como fato. OK.
- **Aviso:** Gate 5: CTL002 (Kit 6 Canecas Tulipa 250ml) — slack_short_name=null; fallback para display_short utilizado e documentado nas Decisões de formatação como 'subótimo'. A regra exige o mapeamento canônico 'quando disponível' — slack_short_name é null, portanto fallback é o procedimento correto. Não constitui violação de regra.

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
