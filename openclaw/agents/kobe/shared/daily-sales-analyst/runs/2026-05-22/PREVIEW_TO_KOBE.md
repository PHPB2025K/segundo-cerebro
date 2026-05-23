# Preview para Kobe — 2026-05-22
**Gerado em:** 2026-05-23T14:56:44.440522+00:00
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
- **Aviso:** Insight 3 da L05 usa linguagem levemente assertiva ('novos pedidos viram cancelamento') apesar de classificacao='risco latente'; a L06 aplicou 'podem virar cancelamento', ficando mais fiel à classificação do que o próprio texto da L05 — melhoria de alinhamento, não alteração de tese. Não é problema, é sinal de que a L05 pode refinar a redação dos insights de risco latente no próximo ciclo.
- **Aviso:** Substituição 'família IMB501' → 'a linha Potes Vidro 5 Peças' no insight 2 e na prioridade 2 está corretamente documentada nas Decisões de formatação e é coerente com os nomes exibidos no Top Produtos da mesma mensagem — consistência cross-section confirmada.
- **Aviso:** alertas_de_confianca.nivel='media' tratado corretamente: limitações de série temporal de health e de breakdown de ADS por anúncio foram incorporadas ponto a ponto nos insights e prioridades sem ressalva global no Slack, alinhado com o que a L05 autorizou.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-22/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
