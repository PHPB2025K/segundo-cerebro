# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T19:20:31.950287+00:00
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
- **Aviso:** Valores monetários abreviados na seção de análise (R$ 3.041 e R$ 5.087) são herança direta da Condensadora, que adotou o mesmo tratamento para esses valores ilustrativos de proporção ADS/GMV. A Slack Writer foi fiel à fonte, o que é correto. Para eliminar o Menor nos próximos ciclos, considerar que a Condensadora já entregue esses valores com decimais completos quando citados em contexto monetário, evitando que a Slack Writer precise escolher entre fidelidade e padrão numérico.
- **Aviso:** Primeira leitura qualitativa do ciclo ML desde que Yasmin assumiu em 22/04/2026. Memória qualitativa estabelecida hoje como linha de base: ADS share 59,8%, ROAS 11,6x, ACOS 4,33%, ticket R$ 55,91, GMV R$ 5.087,71. Nenhuma hipótese anterior para confirmar ou refutar.
- **Aviso:** Kit 06 Canequinhas com Suporte Acrílico (MLB4410218897) encerrou o dia com available_quantity=4 e 3 pedidos — ruptura iminente em ~1 dia. Prioridade operacional corretamente transmitida à Yasmin. Verificar no próximo ciclo se houve reposição ou novos cancelamentos.
- **Aviso:** Health dos dois campeões Full (KIT4YW1050=0,75 e IMB501V=0,71) sem série temporal disponível no pacote — direção não determinável. Dado central para próximo ciclo: valores de D-1 e D-2 para calcular tendência e confirmar ou refutar erosão orgânica progressiva.

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
