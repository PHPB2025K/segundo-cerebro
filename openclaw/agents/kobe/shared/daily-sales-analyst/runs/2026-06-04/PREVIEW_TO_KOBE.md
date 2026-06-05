# Preview para Kobe — 2026-06-04
**Gerado em:** 2026-06-05T14:44:52.431201+00:00
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
- **Aviso:** alertas_de_confianca.nivel='media' da L05 preservado corretamente: insights de 'risco latente' usam linguagem condicional ('pode ameaçar', 'se aproximando') e o insight de 'fato' é assertivo. Nenhuma hipótese virou certeza, nenhum risco latente virou alerta consumado.
- **Aviso:** Todos os 5 Top Produtos usaram slack_short_name canônico: IMB501C → 'Potes Vidro 5 Peças — Tampa Cinza', IMB501V → 'Potes Vidro 5 Peças — Tampa Vermelha', IMB501P → 'Potes Vidro 5 Peças — Tampa Preta', TL6250 → 'Kit 6 Canecas Tulipa 250ml', CLR002 → 'Kit 6 Canecas Lisas 200ml'. Todos com confidence='high' e mapping_status='mapped'. Nenhum nome longo ou SKU cru visível.
- **Aviso:** confirmed_variation_attributes aplicado corretamente para o cluster IMB501: Tampa Cinza, Tampa Vermelha, Tampa Preta preservadas como variações distintas no Top Produtos, impedindo consolidação indevida da família inteira.
- **Aviso:** Escalonamentos para Kobe em P1 e P2 vêm explicitamente de L05.prioridades_condensadas[0].escalar_se e [1].escalar_se. P3 não contém escalonamento pois L05 marcou 'não aplicável hoje'. L06 omitiu corretamente.
- **Aviso:** fulfillment_mix_yesterday_top10 (105/179 = 58,7% de cobertura) omitido da VISÃO corretamente, com decisão registrada no log. fulfillment_mix_7d e 30d (ambos com coverage_pct=100%) disponíveis como referência canônica de tendência, não usados no Slack por não serem dado objetivo do dia.
- **Aviso:** available_quantity tratado prospectivamente em toda a mensagem: 'cerca de 7h de cobertura', 'cerca de 16h', '3 ciclos de cobertura caindo'. Nenhuma afirmação retrospectiva tratando o snapshot como pré-baixa. Regra available_quantity POST-baixa respeitada.
- **Aviso:** Contagem de insights L05 vs Slack: 3 insights L05 → 3 bullets Análise. Contagem de prioridades L05 vs Slack: 3 prioridades → 3 bullets Prioridades. Paridade exata preservada sem justificativa necessária.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-04/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
