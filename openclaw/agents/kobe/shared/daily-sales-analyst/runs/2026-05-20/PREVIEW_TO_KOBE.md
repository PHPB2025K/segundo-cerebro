# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T13:53:06.922960+00:00
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
- **Aviso:** O produto TL6250 foi corretamente referenciado como 'Kit 6 Canecas Porcelana Tulipa 250ml' na mensagem final, respeitando o bloqueio da Granular e da Condensadora sobre o display_name interno incorreto. O alias interno 'Kit 6 Tigelas de Vidro 250ml' deve ser corrigido no mapeamento reviewed_sku_display_map antes de ser usado em análise de família ou mix histórico nas próximas entradas de memória.
- **Aviso:** O KIT4YW320 (MLB4073064873) tem confidence 'medium' e mapping_status 'mapped_generic_sku'; o uso de 'Retangular' no nome do Top Produtos é artefato de inferência familiar, não de fonte validada. Registrar para revisão do mapeamento.
- **Aviso:** O data readiness DADOS_PARCIAIS refere-se exclusivamente ao volume_band da conta Shopee (Budamix Store -43,2%), sem impacto na validade dos dados ML. A mensagem ML não menciona o status parcial porque não há dado ML com qualidade comprometida — comportamento correto.

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

### Lucas (shopee)
- **Status:** BLOCKED
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
- **Aviso:** Erro de percentual originado na camada 6B — a Slack Writer reproduziu fielmente o dado incorreto da fonte analítica. A cadeia de fidelidade funcionou corretamente; o problema está na 6B, não na Slack Writer. Correção deve partir da 6B antes de reprocessar.
- **Aviso:** Todos os demais gates passaram sem problema: estrutura Slack correta, bloqueios da Condensadora integralmente respeitados e documentados, variações de tampa (IMB501P Tampa Preta / IMB501C Tampa Cinza) preservadas em todos os contextos, prioridades fiéis à Condensadora com sinais de confirmação/refutação, padrão numérico PT-BR consistente em toda a mensagem.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/05-condensadora.json`
  - `layer6b_shopee_consolidator`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/06b-shopee-consolidator.json`
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/lucas/07-qa.json`

### Leonardo (amazon)
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
- **Aviso:** Weekly e monthly da Amazon são templates vazios — este é o primeiro ciclo analítico. A linha de base de concentração (CK4742 = 37,5%), volume (40 pedidos, R$1.663,37), ticket (R$41,58) e cancelamento (3 / 7,5%) deve ser registrada na weekly ao final do ciclo.
- **Aviso:** TL250P e TL250B têm display_name incorreto no catálogo interno ('Tigela de Vidro 250ml' vs produto real 'Canecas de Porcelana Tulipa 250ml'). Correção deve ser solicitada antes que o volume desses ASINs cresça.
- **Aviso:** Buy Box e FBA do CK4742 (B0G2CWWMGK) não estavam disponíveis no pacote — gap estrutural da arquitetura de dados a resolver para os próximos ciclos.
- **Aviso:** Três perguntas prioritárias da Operacional (cancelamentos por ASIN, Buy Box/FBA do líder, recorrência do pico de 22h) ficaram 3/3 sem resposta por ausência de dado granular — registrar como gaps a resolver na arquitetura do pacote.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-20/leonardo/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
