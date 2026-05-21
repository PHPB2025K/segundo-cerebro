# Preview para Kobe — 2026-05-20
**Gerado em:** 2026-05-21T15:43:59.452328+00:00
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
- **Aviso:** DADOS_PARCIAIS declarado no Layer 0 por volume da Shopee-Budamix-Store fora da banda 30d (–45,8%) — não afeta a mensagem ML. Todos os checks relevantes para Mercado Livre retornaram OK: volume_band_mercado-livre OK, reconciliation_mercado-livre OK, timezone_brt OK, product_identity_contract OK.
- **Aviso:** 4 perguntas operacionais enviadas pela camada 3 à camada 4 ficaram sem resposta por ausência de dado no pacote (atribuição ADS por produto, pedidos pendentes em processamento do 914C_BAV, status de reposição logística do TL6250 e do 914C_BAV, posição competitiva em catálogo do IMB501V). Os riscos correspondentes foram comunicados na mensagem com ressalvas de incerteza corretas, sem fabricação de dado — nenhum 'não respondido por falta de dado' foi convertido em conclusão.
- **Aviso:** Sync freshness marcado como 'not_measured' no Layer 0 por limitação de esquema. Limitação registrada e sem impacto na validação da mensagem.
- **Aviso:** Confiança declarada como 'média' pela Condensadora. A limitação é estrutural ao pacote ML deste ciclo e não viola nenhuma regra objetiva — comunicação preserva o grau correto de incerteza.

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
