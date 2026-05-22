# Preview para Kobe — 2026-05-21
**Gerado em:** 2026-05-22T12:11:41.940014+00:00
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
- **Aviso:** 5 Menores identificados sem impacto bloqueante. Para próximo ciclo: (1) alinhar nomenclatura cross-section de Canecas Porcelana entre Top Produtos e Análise/Prioridades; (2) alinhar denominação cross-layer de Canequinhas entre L05 e L06, ou documentar divergência no log; (3) preservar 'ou API de pedidos' nas prioridades com ruptura técnica ativa; (4) corrigir grafia 'Cross-Docking' nos prompts da L05 e L06; (5) manter centavos em valores monetários de comparação mesmo quando precedidos de '~'.
- **Aviso:** A propagação de 'cross-docking' em minúscula origina-se na L05 (Condensadora) — a correção deve ocorrer no prompt da L05 para que a L06 herde a grafia correta sem precisar sobrepor a fidelidade terminológica.
- **Aviso:** O log de formatação da L06 documenta as simplificações de Top Produtos item a item, mas não registra explicitamente a decisão de adotar denominação diferente da L05 para o produto 914C_BAV na Análise. Adicionar esse tipo de justificativa no log previne flags cross-layer em ciclos futuros.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-21/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
