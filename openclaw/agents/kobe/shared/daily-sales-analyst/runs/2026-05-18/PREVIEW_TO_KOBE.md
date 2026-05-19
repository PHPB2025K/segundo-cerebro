# Preview para Kobe — 2026-05-18
**Gerado em:** 2026-05-19T12:09:41.688164+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** APPROVED_WITH_REMARKS
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
- **Aviso:** Ticket da Oficial 2 (R$ 102,88 em 18/05/2026): confirmação de tendência requer sustentação acima de R$ 90 por mais 2 dias consecutivos com volume < 20 pedidos; se ticket retornar à faixa de R$ 55–R$ 70, dado de hoje é ruído de mix.
- **Aviso:** Shop 3: se registrar menos de 15 pedidos pelo segundo dia consecutivo, deterioração de exposição confirmada independente do resultado da verificação com Himmel.
- **Aviso:** CTL002 presente nas 3 contas em 18/05/2026: Store (45554989236, 7 pedidos), Oficial 2 (46154989273, 4 pedidos), Shop 3 (50954968481, 4 pedidos) — risco de canibalização cross-conta ativo enquanto Shop 3 estiver em colapso de volume.
- **Aviso:** SKU 098 da Oficial 2: divergência confirmada raw_title ('Kit 9 Potes Vidro Quadrados Hermético Vedação Tampa 4 Travas Marmita') vs display_name ('Pote de Vidro Hermético 800ml') — raw_title é a referência correta; pendente revisão do catálogo.
- **Aviso:** Fulfillment (shopee_full) ausente no pacote de 18/05/2026 para as três contas Shopee (campos zerados com pedidos registrados) — dado não capturado; impede validação de status Shopee Full; pendente verificação técnica.

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
- **Aviso:** 914C e 914C_BAV compartilham o mesmo MLB4410218897 (variações do mesmo listing ML). A Slack Writer flagou explicitamente o dilema nas Decisões de Formatação e manteve separados por ausência de autorização explícita da Condensadora para consolidar — decisão correta. Para o próximo ciclo: Condensadora ou Granular deve explicitar a regra de consolidação/nomeação para SKUs distintos que compartilham o mesmo listing-pai ML, evitando que a Slack Writer precise inventar rótulos de diferenciação.
- **Aviso:** O percentual -14,6% aparece na análise como inversão negativa corrigida (padrão C da Condensadora). O bloqueio da Condensadora é qualificado ('como sinal de deterioração') e o Slack Writer documentou a decisão. Para ciclos futuros: se a Condensadora quiser autorizar a citação explícita do percentual no padrão C, deve incluir no campo de bloqueios a qualificação 'permitido em inversão negativa com correção explícita', evitando ambiguidade na QA.

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
- **Aviso:** 914C (Kit 6 Canequinhas 100ml, B0G2SV7NR1, 1 pedido, 2 unidades, confiança alta) foi corretamente omitido do Top Produtos por volume abaixo do limiar de relevância (corte em 2 pedidos), mas a decisão não foi documentada explicitamente no log da Slack Writer. Sinalizar para o próximo ciclo que o log deve cobrir todos os produtos omitidos por nome, especialmente os de confiança alta.
- **Aviso:** Três dados operacionais críticos ficaram sem resposta por ausência no pacote de 2026-05-18: (1) Buy Box de IMB501P (B0GSWJ91JM) e CK4742 (B0G2CWWMGK), (2) cobertura FBA por ASIN, (3) atribuição de cancelamentos por produto. Leonardo deve preencher essas lacunas operacionalmente hoje. O próximo ciclo deve checar se o pacote passou a incluir esses campos.
- **Aviso:** TL250B e TL6250 têm display_name incorreto no sistema (canecas de porcelana mapeadas como tigelas de vidro). A Slack Writer corrigiu via raw_title corretamente, mas o erro de catálogo persiste e deve ser corrigido na base de dados para evitar contaminação silenciosa em análises futuras de mix de categoria.
- **Aviso:** Família IMB501 respondeu por 33% do canal em dois ASINs distintos (B0GSWJ91JM tampa preta 12 pedidos, B0GSWRMDRG tampa cinza 3 pedidos) com estoque FBA separado. Monitorar nos próximos ciclos se a proporção preta/cinza se mantém ou se a cinza começa a ganhar tração — crescimento da cinza mitiga parcialmente o risco de ruptura unitária da família.

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
