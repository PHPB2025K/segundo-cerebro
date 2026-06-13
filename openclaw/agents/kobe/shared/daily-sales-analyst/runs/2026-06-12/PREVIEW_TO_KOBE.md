# Preview para Kobe — 2026-06-12
**Gerado em:** 2026-06-13T10:16:11.367597+00:00
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
- **Aviso:** L06 usou valores exatos do pacote (R$ 321.406,28 e R$ 25.406,28) em vez dos valores arredondados da L05 ('R$ 321.406' e 'R$ 25 mil'). Tese preservada, sem risco de erro. Decisão documentada no log de formatação. Para próximos ciclos: alinhar com L05 a política de arredondamento — se L05 usou verbal ('R$ 25 mil'), L06 deve preservar o arredondamento; se L05 usou exato, L06 mantém exato. A inconsistência de critério entre os dois valores (R$ 321.406,28 exato vs L05 'R$ 321.406' sem centavos) é registrada aqui como sinal para revisão da diretriz de centavos na próxima manutenção.
- **Aviso:** ACOS com 2 casas decimais: a regra de formatação (1 casa) conflita com a regra de fidelidade ao valor explícito da L05. Para próximos ciclos, a instrução da L06 deve deixar claro que a regra de formatação prevalece e que L06 deve arredondar para 1 casa mesmo quando a L05 forneceu o número com mais casas — salvo quando o arredondamento cruzar limiar analítico relevante (e.g., 9,96% → 10,0% cruza o número redondo de 10%, o que pode ser relevante dependendo do contexto de campanha).

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-12/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
