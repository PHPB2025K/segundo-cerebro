# Preview para Kobe — 2026-06-10
**Gerado em:** 2026-06-11T10:14:13.705463+00:00
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
- **Aviso:** O problema Crítico do Gate 12c não invalida o diagnóstico analítico: a tese de que a divergência do mix é produto-específica (Tampa Cinza Cross-Docking em 2º lugar, somada a Canequinhas e Kit 10 Potes) está plenamente sustentada pelo L04 com confiança alta. A correção é de apresentação — não de diagnóstico. Após ajuste do insight 3, todos os demais gates estão OK e a mensagem seria aprovável com ressalva do Menor no Gate 6.
- **Aviso:** A L06 operou corretamente ao ser fiel à L05. O erro de origem é da L05, que comparou fulfillment_mix_yesterday_top10 (50,3% cobertura) com fulfillment_mix_30d (100% cobertura) na mesma frase sem ressalva — apesar de a L04 ter explicitamente sinalizado que as duas fontes 'não são comparáveis diretamente'. O gate correto para capturar esse problema seria ter bloqueado na L05; o Gate 12 da QA funciona como rede de segurança para exatamente esse tipo de propagação.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-10/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
