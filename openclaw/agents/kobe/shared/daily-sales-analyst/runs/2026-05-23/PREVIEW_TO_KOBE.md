# Preview para Kobe — 2026-05-23
**Gerado em:** 2026-05-24T10:10:43.348548+00:00
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
- **Aviso:** Gate 6, insight 3: conectivo 'apesar de' da L05 virou 'mas' na L06. Ambos são adversativos e a tese central foi preservada — risco zero de induzir Yasmin a erro. Registrar para calibração futura da L06 sobre fidelidade estrita de conectivos.
- **Aviso:** Gate 10 / Gate 4: fulfillment_mix_yesterday_top10 cobre apenas ~54% dos pedidos do dia (49/91). L06 corretamente omitiu da seção VISÃO e contextualizou o dado de 88% Full no bullet da ANÁLISE como 'composição dos campeões, não mudança no perfil da conta'. Comportamento correto preservado.
- **Aviso:** Gate 2 / Gate 10: L05 usou 'reputação verde Gold' (forma composta proibida pelo Gate 10). L06 corrigiu autonomamente para 'reputação verde e nível MercadoLíder Gold', separando os eixos corretamente. Correção proativa registrada — L05 precisa adotar a separação de eixos antes de chegar à L06.
- **Aviso:** Gate 12c: fulfillment_mix_yesterday_top10 com cobertura ~54% (49/91) ficou abaixo do threshold de 70%. L06 omitiu da VISÃO e exibiu o dado apenas na ANÁLISE com ressalva explícita de composição — tratamento correto conforme autorização implícita da L05 que incluiu o insight com contexto. Sem inconsistência bloqueante.
- **Aviso:** Gate 5: KIT6YW1050 e KIT10YW1050 têm mapping_status=mapped_generic_sku e confidence=medium — os dois ficaram nas posições 7 e 10 do Top Produtos (não exibidos na seção Slack de 5 itens). Nenhum impacto na mensagem. Manutenção de confidence pode ser avaliada no próximo ciclo.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-23/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
