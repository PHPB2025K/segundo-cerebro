# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T22:57:50.158022+00:00
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
- **Aviso:** Gate 4 — Fulfillment omitido da seção VISÃO MERCADO LIVRE: a Slack Writer justificou a omissão pela cobertura parcial do fulfillment_mix_yesterday_top10 (71 de 91 pedidos), decisão documentada e não indutora de erro. A Condensadora não autorizou nem proibiu explicitamente a exibição com ressalva de cobertura. Em ciclos futuros, avaliar se o mix Full/Cross-Docking (56,3% / 43,7% no top 10, divergindo +17,6pp do padrão 30d por efeito do campeão em Cross-Docking) deve aparecer na VISÃO com nota de cobertura parcial — a divergência produto-específica documentada pela L03 e L04 é contexto relevante para Yasmin entender a conta.
- **Aviso:** Gate 6 — Insight 2: 'o snapshot do dia mostra' (Condensadora) simplificado para 'o snapshot mostra' (Slack Writer). Omissão de 'do dia' sem impacto semântico (há um único snapshot por ciclo). Registrado para consistência de linguagem entre camadas em ciclos futuros.
- **Aviso:** Confiança geral média (conforme Condensadora): estruturalmente justificada por ausência de breakdown de ADS revenue por platform_item_id, ausência de série temporal de health (ciclo inaugural com pontos zero registrados para MLB4073003575 health=0,75 e MLB3288536143 health=0,71) e irrastreabilidade dos 3 cancelamentos por anúncio. A Slack Writer preservou corretamente todas as incertezas — hipótese qualificada no insight 3, condicional no insight 2, ausência de afirmação de direção de health. Nenhuma limitação foi convertida em certeza. Série temporal de health e ADS breakdown por item devem ser priorizados para os próximos ciclos para destravar o gatilho de escalonamento com Himmel.
- **Aviso:** Gate 5 — KIT10YW1050 (confidence=medium, mapping_status=mapped_generic_sku) aparece como '4º produto' no Top com 5 pedidos. Risco formal de mapeamento médio, risco prático baixo por convergência de title ML e raw_title confirmada pela L04. Nenhuma ação necessária — registrado para monitoramento de recorrência do SKU na série.

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
