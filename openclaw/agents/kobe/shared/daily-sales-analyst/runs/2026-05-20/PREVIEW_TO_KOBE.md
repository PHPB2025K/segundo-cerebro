# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T15:54:27.284805+00:00
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
- **Aviso:** Log de decisão de formatação (Gate 5) registrou incorretamente a ordem de produtos empatados — 'conforme posição no pacote validado (IMB501V antes de TL6250 antes de KIT10YW1050)' — quando o pacote tem KIT10YW1050 na posição 4 e IMB501V na posição 5. A inconsistência é entre log e realidade do pacote, não entre log e mensagem. Corrigir instrução de ordenação de empates para próximos ciclos.
- **Aviso:** Sinais de refutação de P2 e P3 foram comprimidos na redação das prioridades. Versões futuras da Slack Writer devem incluir o critério de resolução/dissipação do risco junto à condição de escalonamento.
- **Aviso:** Palavra 'narrow' em inglês foi preservada literalmente da Condensadora. A Condensadora deve avaliar substituição por equivalente em português nos próximos ciclos.
- **Aviso:** Descritor 'Retangular' atribuído ao KIT4YW320 sem base explícita na fonte — verificar se o produto é de fato retangular e, se sim, atualizar o display_name no mapeamento interno para refletir isso.

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
