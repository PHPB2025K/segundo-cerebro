# Preview para Kobe — 2026-05-31
**Gerado em:** 2026-06-01T10:11:02.202259+00:00
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
- **Aviso:** L06 corrigiu os valores monetários arredondados da L05 (R$ 8.267 → R$ 8.267,83 e R$ 19.876 → R$ 19.876,77) usando a fonte primária do pacote — comportamento correto e rastreável; sinalizar para L05 entregar centavos completos nos próximos ciclos, evitando dependência de correção na L06.
- **Aviso:** TL6250 (Kit 6 Canecas Tulipa 250ml, posição 8 no top_products com 4 pedidos) não aparece no Top Produtos do Slack — correto, pois o Slack exibe apenas os 5 primeiros. O produto é citado corretamente na Análise e Prioridades com o slack_short_name canônico 'Kit 6 Canecas Tulipa 250ml'.
- **Aviso:** Cluster IMB501 (MLB3288536143) referenciado como 'Potes Vidro 5 Peças (as três tampas)' nas seções de Análise e Prioridades: construção derivada da raiz comum dos três slack_short_names sem atributo de cor. Não há slack_short_name para o agregado; a decisão de formatação está documentada na L06 e preserva o sentido operacional de anúncio único. Registrar para eventual adição de entrada de agregado canônico em config/slack-short-names-ml.json se a referência ao cluster virar padrão recorrente.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-31/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
