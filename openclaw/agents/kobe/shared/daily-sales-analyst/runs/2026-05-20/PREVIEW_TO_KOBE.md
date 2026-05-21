# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T17:20:27.617935+00:00
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
- **Aviso:** A Condensadora usou notação americana (ponto decimal) para health scores em seu output intermediário — corrigir na próxima versão das regras da Condensadora para garantir que artefatos intermediários já adotem o padrão numérico brasileiro, evitando propagação ao Slack.
- **Aviso:** O bloqueio da Condensadora proibiu 'afirmar reclamação, atraso ou listing como causa' mas não explicitou se hipóteses formuladas com 'pode ser' são permitidas — a Slack Writer interpretou o silêncio como permissão de hipótese. Recomenda-se clarificar na próxima versão das regras se o bloqueio inclui ou exclui formulações hipotéticas, para fechar essa ambiguidade antes do próximo ciclo.
- **Aviso:** O log das Decisões de Formatação descreveu incorretamente 'estoque de 3 unidades' como se fosse 'estoque zerado' — sinaliza necessidade de a Slack Writer citar o trecho literal alterado, não a categoria do bloqueio, para garantir rastreabilidade exata no Gate 8.

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
