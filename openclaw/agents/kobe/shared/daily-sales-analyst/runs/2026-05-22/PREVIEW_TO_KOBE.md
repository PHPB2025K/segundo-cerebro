# Preview para Kobe — 2026-05-22
**Gerado em:** 2026-05-24T00:19:30.522596+00:00
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
- **Aviso:** {'gate': 'Gate 10 — vocabulário ML / nível de qualidade do anúncio', 'observacao': "L05 usa a frase 'nível de qualidade dos dois campeões Full' em vez do termo canônico aprovado 'nível de qualidade do anúncio'. L06 reproduziu fielmente a frase da L05 (correto em termos de fidelidade ao pipeline) e incluiu os nomes de faixa corretos ('Padrão inferior') com os valores numéricos — nenhuma condição de bloqueio da Gate 10 foi atingida (não há 'health' solta, número sem faixa, tradução errada ou health=null tratado como saudável). Recomendação sistêmica: alinhar o prompt da L05 para usar o termo exato 'nível de qualidade do anúncio' em todas as referências ao campo health da API ML, evitando que a paráfrase chegue à L06 por fidelidade."}
- **Aviso:** {'gate': 'Gate 5 e Gate 6 — nomenclatura de cluster IMB501', 'observacao': "L05 usa o identificador técnico 'cluster IMB501' na analise_final_condensada; L06 traduziu para 'cluster de Potes Vidro 5 Peças' para padronizar com os slack_short_names canônicos, decisão documentada no log de formatação. A tradução é justificada e sem risco de confusão para Yasmin — os três produtos (Tampa Preta/Vermelha/Cinza) são inequivocamente identificados em ambos os nomes. Registrar como sinal de manutenção: em revisões de memória ou histórico que cruzem referência ao cluster por nome técnico, a discrepância 'IMB501' vs 'Potes Vidro 5 Peças' deve ser explicitada para evitar ambiguidade interna entre camadas."}
- **Aviso:** {'gate': 'Gate 12 — cobertura do fulfillment_mix_yesterday_top10', 'observacao': "O campo fulfillment_mix_yesterday_top10 cobre 68 de 84 pedidos do dia (80,9%) — acima do limiar de 70% que dispararia BLOQUEIO Crítico. A mensagem usa corretamente o escopo explícito ('52,9% do top 10'), não como métrica total do canal. Manter monitoramento em ciclos futuros: dias com volume concentrado fora do top 10 (anúncios longtail, promoções pontuais) podem comprimir a cobertura abaixo de 70% e exigir tratamento explícito de ressalva na L05 para autorizar exibição."}

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
