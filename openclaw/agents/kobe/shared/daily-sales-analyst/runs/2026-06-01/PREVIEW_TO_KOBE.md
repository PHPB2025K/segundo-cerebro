# Preview para Kobe — 2026-06-01
**Gerado em:** 2026-06-04T15:04:26.545724+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** APPROVED_WITH_REMARKS
**Prompt Version:** v4.0/shopee
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
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** Os três Menores identificados têm origem parcial na L05 Condensadora (percentuais inteiros em analise_final_condensada e 'booster'/'baseline' nos textos de L05) e foram fielmente reproduzidos pela L06 — a correção prioritária deve ser incorporada nas regras de formatação da L05 para evitar recorrência estrutural nos próximos ciclos.
- **Aviso:** L06 realizou corretamente a correção de 'R$ 3.092' (L05 sem decimais) para 'R$ 3.092,25' (com centavos) — comportamento correto a manter e que demonstra que a L06 já aplica correções de padrão numérico quando identifica desvios explícitos.
- **Aviso:** Inconsistência interna na mensagem final: 'amortecedor' (Análise bullet 1) vs 'booster' (Prioridades bullet 1) para o mesmo conceito de visibilidade — ambas as seções foram fiéis às suas fontes L05 correspondentes (analise_final_condensada e prioridades_condensadas), mas o glossário PT-BR deveria ser aplicado uniformemente pela L06 no momento da escrita.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
