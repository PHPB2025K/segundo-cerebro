# Preview para Kobe — 2026-05-17
**Gerado em:** 2026-05-18T10:29:13.540285+00:00
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
- **Aviso:** A Slack Writer identificou corretamente a ambiguidade da linha duplicada nas Decisões de Formatação e delegou a decisão ao QA. Para ciclos futuros, a Slack Writer deve resolver internamente conflitos de duplicação de produto antes de passar ao QA — a Decisão de Formatação deve registrar a resolução, não a dúvida.
- **Aviso:** Gate 8 — RESSALVA de log: o bloco Respeito de Bloqueios declara 'Aparece na mensagem final: não' para platform_item_ids e raw_skus técnicos. Os raw_skus (IMB501P_T, CK4742_B) de fato não aparecem; os variation_skus (IMB501P, CK4742) aparecem vindos da 6B. O log não distingue explicitamente raw_sku de variation_sku, gerando imprecisão interna. Não é bloqueante (a 6B é a fonte autorizada e a Condensadora não bloqueou variation_skus), mas o log deve ser mais preciso em ciclos futuros.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/05-condensadora.json`
  - `layer6b_shopee_consolidator`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/06b-shopee-consolidator.json`
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/lucas/07-qa.json`

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
- **Aviso:** Três perguntas da Granular transitam abertas para o próximo ciclo por falta de dado: (1) ranking histórico do anúncio MLB3288536143 nos últimos 7 dias — IMB501P e IMB501C; (2) origem do ticket elevado (reajuste de preço, redução de desconto ou mix shift natural); (3) distribuição horária dos quatro sábados anteriores para comparar com o bloco 11h–15h de 17/05. Alimentar pipeline para capturar nas próximas coletas.
- **Aviso:** Schema de fulfillment não captura modalidade ML Full — todos os valores categorizados retornam zero com total=100. Limitação técnica interna; registrar para correção no pipeline. Para os produtos que dominam o volume da conta (IMB501 e KIT YW), a modalidade de fulfillment é invisível no pacote atual.
- **Aviso:** Weekly e monthly são shells vazios — 2026-05-17 é o primeiro ponto de baseline. Ticket R$ 51,81 registrado como ponto zero da série. Tese de ganho de patamar sustentada nos números mas sem hipótese prévia confirmada; próximos ciclos devem acumular evidência para consolidar ou refutar.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/yasmin/07-qa.json`

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
- **Aviso:** Display_name incorreto de TL250B ('Tigela de Vidro 250ml') e TL250P ('Tigela de Vidro 250ml') persiste no catálogo interno — produto real é Kit 6 Canecas de Porcelana Tulipa 250ml; erro confirmado por raw_title e ASIN dos pedidos reais; deve ser corrigido na fonte para evitar contaminação em ciclos futuros.
- **Aviso:** TL250R com mapeamento por fallback (confidence medium, mapped_generic_sku) continua requerendo tratamento de cautela até revisão do mapeamento para reviewed_sku_display_map.
- **Aviso:** As três perguntas operacionais críticas — cancelamentos por ASIN, Buy Box da Jarra Medidora (B0G2CWWMGK), cobertura FBA dos Top 3 — não foram respondidas neste ciclo por ausência de dado no pacote. Leonardo deve consultar Seller Central e trazer os dados para o próximo ciclo; sem isso a análise operacional do próximo dia parte da mesma lacuna.
- **Aviso:** Hipótese de ganho de patamar inaugurada neste ciclo (44 pedidos, R$ 2.091,77, +93% vs mesmos sábados). Próximos 2–3 dias são determinantes: volume acima de 35 pedidos confirma; retorno à banda 28–32 encerra a hipótese.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-17/leonardo/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
