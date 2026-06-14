# Preview para Kobe — 2026-06-13
**Gerado em:** 2026-06-14T10:21:34.291312+00:00
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
- **Aviso:** KIT4YW640 (MLB5402326666, 8 pedidos em 13/06): adicionar entrada em config/slack-short-names-ml.json na próxima manutenção para eliminar fallback automático no Top Produtos
- **Aviso:** Grafia curta 'Platinum' é padrão recorrente desde L05 — padronizar nas camadas L05 e L06 para sempre usar 'MercadoLíder Platinum' nos próximos ciclos
- **Aviso:** Todos os demais slack_short_names dos top 5 do dia foram aplicados corretamente: IMB501P 'Potes Vidro 5 Peças — Tampa Preta', IMB501C 'Potes Vidro 5 Peças — Tampa Cinza', IMB501V 'Potes Vidro 5 Peças — Tampa Vermelha', KIT10YW520 'Kit 10 Potes 520ml' — mapeamentos canônicos preservados sem alteração
- **Aviso:** Nomes de produto consistentes entre Top Produtos, Análise e Prioridades: IMB501 referenciado como bloco de variações com nomes curtos, KIT3S099 via display_short, KIT4YW1050 via slack_short_name — cross-section coerente

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-13/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
