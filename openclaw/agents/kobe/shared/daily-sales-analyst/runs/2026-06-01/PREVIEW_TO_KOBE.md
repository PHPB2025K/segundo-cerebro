# Preview para Kobe — 2026-06-01
**Gerado em:** 2026-06-03T12:38:28.873736+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** APPROVED_WITH_REMARKS
**Prompt Version:** v4.0/shopee
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
  - 06-slack-preview: LLM
  - 07-qa: LLM
- **Aviso:** Faturamento de Budamix Oficial (Conta 2) e Budamix Shop (Conta 3) ausente do pacote do dia — apenas contagem de pedidos disponível para essas contas. Registrar para L00/Trader que GMV desagregado por conta secundária Shopee não foi entregue neste ciclo. Total inferível: ~R$ 1.287,09 distribuídos entre Conta 2 (17 pedidos) e Conta 3 (11 pedidos), mas split não verificável.
- **Aviso:** TOP PRODUTOS SHOPEE cobre apenas Budamix Store (68 dos 96 pedidos = 70,8% do canal) por ausência de product_data para Conta 2 e Conta 3 no pacote. Quando 06b-shopee-consolidator estiver disponível nos próximos ciclos, o TOP deve refletir as 3 contas consolidadas com agrupamento por variação vendável.
- **Aviso:** Data Readiness DADOS_PARCIAIS confirmado: fulfillment_mix (logistic_type null em 100% dos pedidos por backfill pendente), ads_summary (HTTP 403) e shop_performance (HTTP 404) indisponíveis para Budamix Store. Análise e prioridades preservaram essas lacunas corretamente sem fabricar diagnóstico de tráfego ou logística.
- **Aviso:** Base de memória em estado de semente para esta conta: lacuna de 12 dias no daily (último registro 2026-05-20), weekly e monthly com template vazio. Confiança da tese atual é baixa a moderada por ausência de série recente — avaliar upgrade para confiança média após 2-3 ciclos seguidos com snapshot de estoque disponível.
- **Aviso:** CTL002 (Kit 6 Canecas Tulipa) OOS na Store e top 2 do dia com 15 pedidos — bloqueio de canibalização respeitado nesta mensagem. Input ativo para 06b-shopee-consolidator no próximo ciclo: SKU em OOS na conta de maior volume histórico pode redirecionar demanda para Oficial/Shop.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-01/shopee-budamix-store/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
