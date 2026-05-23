# Preview para Kobe — 2026-05-22
**Gerado em:** 2026-05-23T13:06:38.368814+00:00
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
- **Aviso:** Os 5 Menores do Gate 6 estão todos no sentido de hedging adicional para classificação 'risco latente' (insights 1 e 2) ou de substituição de termo/tempo verbal próximo (insight 3). A tese central, os dados factuais (R$3.228,78, R$4.622,03, health 0,75 e 0,71, 9 unidades, 1,5 dias, 47% vs 74%, 33%), os bloqueios e as prioridades estão integralmente preservados. Nenhum risco de induzir Yasmin a erro operacional foi identificado.
- **Aviso:** A L05 usou linguagem assertiva ('é frágil', 'não está', 'está cobrindo', 'É o único sinal') para insights classificados como 'risco latente' — tecnicamente inconsistente com a regra de linguagem condicional obrigatória para risco latente. L06 corrigiu na direção certa ao adicionar 'parece', gerando os Menores de verbo modal. Em ciclos futuros, a L05 deveria usar linguagem condicional já no texto do insight quando a classificação é 'risco latente', eliminando a ambiguidade de fidelidade para a L06 e os Menores resultantes.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
