# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T22:32:29.808281+00:00
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
- **Aviso:** Gate 5: display_name canônico do pacote para IMB501P é 'Conjunto 5 Potes de Vidro Redondos Tampa Preta' — a Condensadora e layers upstream devem padronizar o uso de 'Conjunto' vs 'Kit' para evitar divergência com o raw_title na próxima geração.
- **Aviso:** Gate 11: Condensadora entregou percentuais sem decimal (32%, 56%, 60%, 74%) — regra de formatação de 1 casa decimal deve ser aplicada na Condensadora ou documentada como exceção para números redondos; a omissão de 'hoje' em '60% desse resultado passou por ADS' (vs Condensadora: 'passou por ADS hoje') também ocorreu na Gate 6.
- **Aviso:** Gate 11: Identificador técnico '5_green/gold' oriundo da API ML foi reproduzido pela Condensadora e pelo Slack Writer — próximo ciclo deve avaliar substituição por nomenclatura de display ('verde/ouro' ou 'MercadoLíder Ouro') para aderência ao padrão de mensagem sem IDs técnicos.
- **Aviso:** Diretriz Pedro 2026-05-17: troca de 'O problema é que' por 'O ponto de atenção:' é consistente com simplificação operacional pedida; ajuste aceitável para hipótese não confirmada, mas a tese da Condensadora usa 'O problema é que' com intenção — registrar para calibrar a Condensadora ML no próximo ciclo.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
