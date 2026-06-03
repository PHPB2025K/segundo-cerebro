# Preview para Kobe — 2026-06-02
**Gerado em:** 2026-06-03T10:16:13.572055+00:00
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
- **Aviso:** L06 adicionou 'progresso em 96,1%' no bullet 2 da Análise — dado factualmente correto (ml_snapshot.mercadolider.platinum.progress_pct=96.07) que não estava no texto literal do insight 2 da L05, apenas no bloco de dados subjacente. A adição é precisa, suporta a tese sem alterá-la e não constitui insight novo, portanto não bloqueia. Para o próximo ciclo: L05 pode optar por incluir explicitamente o progress_pct no insight para evitar enriquecimento autônomo pela L06.
- **Aviso:** A comparação do fulfillment_mix_yesterday_top10 (68,5% de cobertura, 135/197 pedidos) contra fulfillment_mix_30d (100% de cobertura, 3.536 pedidos) no bullet 3 da Análise é metodologicamente assimétrica em termos de base. A qualificação 'no top 10' delimita o escopo corretamente e a própria L05 realizou a mesma comparação no insight 3, portanto QA aceita. Para o próximo ciclo: considerar se a L05 deve adicionar ressalva explícita de cobertura ao realizar essa comparação, para preservar rastreabilidade analítica.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-02/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
