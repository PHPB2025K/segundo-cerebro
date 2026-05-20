# Preview para Kobe — 2026-05-19
**Gerado em:** 2026-05-20T10:37:08.096692+00:00
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
- **Status:** APPROVED_WITH_REMARKS
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
- **Aviso:** A variação 'diagnosticar causa' vs 'diagnóstico' no bullet consolidado não altera o sentido e não induz erro, mas a Slack Writer não registrou a divergência nas Decisões de Formatação. Em ciclos futuros, qualquer alteração de redação em relação ao texto literal da 6B deve ser documentada no log de decisões.
- **Aviso:** Prioridades expandidas além do texto literal da 6B com adição de estrutura 'Confirmar/refutar:' e 'Escalar se:' oriundas da Condensadora — decisão correta e documentada no log, mas que deve ser padronizada explicitamente nas regras da Slack Writer para Shopee para evitar variação entre ciclos.
- **Aviso:** VISÃO por conta mostra apenas faturamento e pedidos, sem ticket médio individual — dado disponível no pacote; decisão de omitir é defensável (VISÃO é objetiva e análise já cobre ticket por conta), mas deve ser documentada formalmente nas Decisões de Formatação em ciclos futuros.

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
- **Aviso:** Weekly.md e monthly.md são templates vazios — hoje é o dia zero da base narrativa da conta; tese de ganho de patamar apoiada em três janelas quantitativas convergentes mas sem confirmação narrativa acumulada; os próximos 5 dias são críticos para solidificar ou rever a tese
- **Aviso:** Cancelamentos (6 total) sem breakdown por produto ou listing — estrutura atual de dados não permite qualificação; ausência de qualificação na mensagem está correta
- **Aviso:** TL6250: flag de catálogo aberta — raw_title do pedido real ('Kit 6 Canecas Porcelana Tulipa Lisa 250ml') diverge do display_name ('Kit 6 Tigelas de Vidro 250ml'); Slack Writer usou título real corretamente, mas a divergência persiste no mapa SKU→display_name e requer correção no ciclo de catálogo antes do próximo reporte

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
- **Aviso:** Slack Writer optou por incluir ASIN para TL250P (B0GGTY2BLT), TL250B (B0GGTTMD4H) e TL6250 (B0GFPQD4G9) além do raw_title, com justificativa de identificabilidade após divergência de alias. Estritamente a regra exige ASIN apenas para título ambíguo ou risco médio — os raw_titles usados são unívocos. A decisão não induz erro, está documentada nas Decisões de Formatação e é defensável operacionalmente (Leonardo pode cruzar com Seller Central). Registrado como memória interna para calibrar critério em ciclos futuros.
- **Aviso:** Simplificação 'breakdown por ASIN' → 'detalhamento por produto' na Análise da Conta é coerente com a Diretriz Pedro 2026-05-17 (linguagem operacional simples) e não altera a tese. Não é problema, mas registrado para rastreabilidade.
- **Aviso:** Problema sistemático de alias na família TL (TL250P, TL250B, TL6250 mapeados como 'Tigela de Vidro' quando produto real é 'Caneca de Porcelana Tulipa') documentado pela Granular e pela Condensadora para correção no reviewed_sku_display_map antes do próximo ciclo.
- **Aviso:** Weekly e monthly da conta Amazon contêm apenas templates sem conteúdo — toda análise estratégica partiu do zero. Primeiro registro real de 2026-05-19: 67 pedidos, R$2.472,80, 13 cancelamentos (~19% bruto), ticket R$36,91. Confirmar nos próximos 3–5 dias se GMV sustenta acima de R$1.800 com cancelamento abaixo de 15% para validar ganho de patamar.

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
