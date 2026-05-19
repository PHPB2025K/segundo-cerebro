# Preview para Kobe — 2026-05-18
**Gerado em:** 2026-05-19T11:28:00.281734+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** PARTIAL
**Prompt Version:** v3.0
**Data Builder Version:** v1.3
**LLM Used:** True

## Protecoes Ativas
- send_real_enabled=false in config
- require_kobe_approval_for_real_send=true — no approval document found

## Resumo por Recipient

### Lucas (shopee)
- **Status:** APPROVED_WITH_REMARKS
- **send_allowed:** False
- **llm_used:** True
  - 01-estrategica: LLM
  - 02-tatica: LLM
  - 03-operacional: LLM
  - 04-granular: LLM
  - 05-condensadora: LLM
  - 06b-shopee-consolidator: LLM
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** Os 4 percentuais sem casa decimal (76%, -47%, -66%, -62%) são herança direta do texto produzido pelo 06b-shopee-consolidator, que os gerou com arredondamento. A Slack Writer foi fiel ao 06b. A correção estrutural é aplicar o padrão '1 casa decimal com vírgula' no 06b para os próximos ciclos, não na Slack Writer isoladamente.
- **Aviso:** send_real_allowed permanece false — promoção final pendente de aprovação por Pedro e aplicação pelo Trader.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/05-condensadora.json`
  - `layer6b_shopee_consolidator`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/06b-shopee-consolidator.json`
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/lucas/07-qa.json`

### Yasmin (mercado_livre)
- **Status:** BLOCKED
- **send_allowed:** False
- **llm_used:** True
  - 01-estrategica: LLM
  - 02-tatica: LLM
  - 03-operacional: LLM
  - 04-granular: LLM
  - 05-condensadora: LLM
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** Mensagem bloqueada por 1 Crítico (SPC0111 em Top Produtos). O bloqueio é de regra, não de esquecimento — a Slack Writer registrou a decisão conscientemente nas Decisões de Formatação. Isso indica necessidade de reforço na arquitetura da Slack Writer: bloqueios da Condensadora em 'o_que_nao_pode_ir_para_slack' são invioláveis e não podem ser sobrescritos por julgamento de formatação, independentemente da seção da mensagem.
- **Aviso:** Após remoção de SPC0111 e nova rodada de QA, os dois Menores remanescentes (fraseado Gate 6 e decimal Gate 11) resultariam em 'APROVADO COM RESSALVA' sob a regra de agregação (0 Maiores + 2 Menores).

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/yasmin/07-qa.json`

### Leonardo (amazon)
- **Status:** BLOCKED
- **send_allowed:** False
- **llm_used:** True
  - 01-estrategica: LLM
  - 02-tatica: LLM
  - 03-operacional: LLM
  - 04-granular: LLM
  - 05-condensadora: LLM
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** O conteúdo da mensagem respeita os seis bloqueios da Condensadora no texto; o Gate 8 falhou exclusivamente por incompletude documental do log, não por violação de conteúdo — após complementação do log, nenhuma alteração de texto da mensagem é necessária para este gate.
- **Aviso:** Gate 6 aprovado sem ressalva: os dois insights da Condensadora foram reproduzidos com fidelidade integral — tese central, conectivos, verbos modais, termos analíticos-chave (Buy Box, cobertura FBA, 53%, patamar de crescimento, operacionalmente ancorado, família IMB501, Tampa Preta + Tampa Cinza, 33%, 60%, dois vetores, fulfillment) todos preservados. As duas decisões de formatação registradas (remoção de 'o pacote não contém esses dados' e remoção do nome Leonardo na análise) são coerentes e não alteram tese.
- **Aviso:** Gate 5 aprovado: variações IMB501P (Tampa Preta) e IMB501C (Tampa Cinza) mantidas separadas; TL250B e TL6250 citados com títulos reais derivados de raw_title em substituição aos display_names bloqueados; JMOCE omitido conforme bloqueio da Condensadora; ASINs ausentes sem caso de ambiguidade identificável nos produtos listados.
- **Aviso:** A consistência numérica da seção ANÁLISE DA CONTA está correta: '53%' no insight 1 e '33%' e '60%' no insight 2 são todos fiéis à Condensadora e matematicamente verificáveis pelos dados brutos.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-18/leonardo/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
