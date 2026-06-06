# Preview para Kobe — 2026-06-05
**Gerado em:** 2026-06-06T10:06:51.253212+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** BLOCKED
**Prompt Version:** v4.0/mercado-livre
**Data Builder Version:** v1.3
**LLM Used:** True

## Protecoes Ativas
- send_real_enabled=false in config
- require_kobe_approval_for_real_send=true — no approval document found

## Resumo por Recipient

### Yasmin (mercado_livre)
- **Status:** BLOCKED
- **send_allowed:** False
- **llm_used:** True
  - 01-estrategica: LLM
  - 02-tatica: LLM
  - 03-operacional: LLM
  - 04-granular: LLM
  - 05-condensadora: LLM
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** Após correção dos 2 Maiores, a mensagem está apta para envio: fidelidade à L05 preservada em todos os 3 insights (tese central, conectivos, verbo modal e classificação corretamente sinalizados por linguagem — não por rótulo), 3 prioridades completas com sinal_de_confirmacao_refutacao e escalar_se, estrutura Slack correta nas 6 seções, slack_short_name canônico aplicado no Top Produtos e nas menções de Prioridades.
- **Aviso:** Após eliminação dos Maiores, considerar também alinhar as menções de Análise ('Tampa Vermelha', 'Tampa Preta') para o slack_short_name completo ('Potes Vidro 5 Peças — Tampa Vermelha', 'Potes Vidro 5 Peças — Tampa Preta') — não é bloqueante, mas elimina o Menor de consistência cross-section.
- **Aviso:** Substituir ocorrências de 'snapshot' por 'próxima atualização' ou 'próxima leitura' nas prioridades elimina o Menor de jargão técnico e alinha com o critério de simplicidade de vocabulário aplicado pela L06 nas demais traduções (ETA → prazo, threshold → limite, fulfillment_mix → proporção de pedidos em Full).

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-05/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
