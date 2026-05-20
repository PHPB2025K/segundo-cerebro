# Preview para Kobe — 2026-05-19
**Gerado em:** 2026-05-20T10:57:07.148365+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** PARTIAL
**Prompt Version:** v3.0
**Data Builder Version:** v1.3
**LLM Used:** True

## Protecoes Ativas
- send_real_enabled=false in config
- require_kobe_approval_for_real_send=true — no approval document found

## Resumo por Recipient

### Lucas (shopee)
- **Status:** BLOCKED
- **send_allowed:** False
- **llm_used:** True
  - 01-estrategica: LLM
  - 02-tatica: LLM
  - 03-operacional: LLM
  - 04-granular: LLM
  - 05-condensadora: LLM
  - 06b-shopee-consolidator: LLM
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** KIT2YW800SQ aparece no Top Produtos apenas com a entrada da Conta 3 (6 pedidos). A Store tinha 2 pedidos do mesmo SKU que não foram exibidos separadamente nem consolidados com a Conta 3. O log de Decisões de Formatação diz 'mantido separado' mas apenas uma das duas entradas aparece na mensagem. Impacto mínimo no resultado dado o volume (2 pedidos), mas a inconsistência entre decisão registrada e execução deve ser corrigida no próximo ciclo.
- **Aviso:** Os 5 Menores do Gate 6 indicam padrão sistemático de simplificação da Slack Writer em relação à 6B: contextos analíticos de apoio foram removidos em três dos quatro blocos de análise (Store, Oficial, Shop-3). Não configuram degradação sistêmica (abaixo do limiar de 6+) e não alteram teses, mas o padrão deve ser monitorado — se persistir nos próximos ciclos, indica tendência de erosão da profundidade analítica autorizada pela 6B.
- **Aviso:** GMV consolidado de R$ 4.070,69 está abaixo do gatilho de intervenção de R$ 4.500. Se a mensagem corrigida for enviada e o GMV de amanhã ficar abaixo de R$ 4.500, será o segundo dia do contador — três dias consecutivos abaixo do gatilho acionam intervenção estruturada Lucas + Himmel.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/05-condensadora.json`
  - `layer6b_shopee_consolidator`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/06b-shopee-consolidator.json`
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/lucas/07-qa.json`

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
- **Aviso:** Slack Writer perdeu o framing Padrão B no insight 3 ao simplificar a frase final. Nas próximas execuções da camada 6, garantir que conectivos contrastivos e a frase positiva do padrão de inversão não sejam removidos na busca por brevidade — a inversion 'parece bom, mas' tem função operacional, não estética.
- **Aviso:** A frase 'Sem essas verificações, a conta parece saudável, mas...' deve ser tratada como âncora de framing em insights de Padrão B, não como detalhe suprimível. O Slack Writer a substituiu por 'Enquanto...' sem registrar a decisão nas Decisões de Formatação — lacuna de documentação menor.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/yasmin/07-qa.json`

### Leonardo (amazon)
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
- **Aviso:** Log da Slack Writer contém entrada inconsistente para KIT2YW1050: registrado como 'omitido (0 pedidos)' com justificativa incorreta, mas item aparece corretamente na mensagem. Corrigir template/lógica de decisão da Slack Writer para o campo de ASIN/ranking na próxima execução: ao omitir 028, o sistema deve recalcular posições restantes antes de gerar os logs de formatação.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-19/leonardo/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
