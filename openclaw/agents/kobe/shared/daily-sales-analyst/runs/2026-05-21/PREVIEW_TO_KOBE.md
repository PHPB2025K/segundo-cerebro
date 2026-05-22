# Preview para Kobe — 2026-05-21
**Gerado em:** 2026-05-22T18:41:17.578082+00:00
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
- **Aviso:** Os 6 Menores detectados têm causa raiz majoritariamente na L05 (arredondamentos de percentual, paráfrase de 'sem base qualitativa', inconsistência 75% vs 75,1%) ou foram transparentemente documentados pelo L06 (inconsistências de nome cross-section). No próximo ciclo, recomendar à L05: (a) uniformizar valor de ADS share (usar 75,1% consistentemente); (b) usar 1 casa decimal para percentuais de modalidade de envio (80,2% e 73,6%); (c) preservar exatamente 'sem base qualitativa acumulada'.
- **Aviso:** Prioridade 3: o campo sinal_de_confirmacao_refutacao da L05 contém ação prescrita de refutação ('abrir conversa sobre cobertura preventiva de ADS') que não foi replicada explicitamente no Slack. A L06 capturou o threshold no escalar_se mas omitiu o destinatário da ação. Sinalizar à L06 para incluir ação prescrita do sinal de refutação integralmente nas prioridades.
- **Aviso:** Tensão estrutural observada em L05 insight 1: classificacao='risco latente' combinada com linguagem afirmativa 'é cancelamento prospectivo garantido'. A linguagem de 'risco latente' deveria incluir condicionais ('se', 'quando'). L06 foi fiel à L05. A tensão originou-se na L05 e não é violação da L06 — registrar para revisão da regra trava hipótese vs fato na L05 no próximo ciclo.

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
