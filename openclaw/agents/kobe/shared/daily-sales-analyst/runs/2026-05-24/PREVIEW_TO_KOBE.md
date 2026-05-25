# Preview para Kobe — 2026-05-24
**Gerado em:** 2026-05-25T12:23:55.391980+00:00
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
- **Aviso:** L05 insight 2 continha 'cancelamento automático em horas' na descrição do risco prospectivo. L06 corretamente suprimiu 'em horas' (que poderia ser lido como risco retrospectivo ou iminência excessivamente específica), substituindo por 'o ML cancela automaticamente' — resultado correto e alinhado com a regra de available_quantity post-baixa (Gate 10). Contudo, a decisão de formatação não registrou explicitamente essa remoção no log da L06. O resultado está correto; o registro está incompleto.
- **Aviso:** L06 inseriu 'e prejudica o cancellations_rate' no bullet 2 da ANÁLISE. Essa informação provém da L05, mas da seção 'prioridades_condensadas' (prioridade 2, campo 'por_que'), não do 'analise_final_condensada' insight 2. Não é análise nova — é informação autorizada pela L05 em seção diferente. O cruzamento cross-section é aceitável operacionalmente, mas tecnicamente o insight da L05 não autorizava explicitamente essa adição no bullet de análise. Não impacta fidelidade da tese; registrado para revisão de regra no próximo ciclo.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-24/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
