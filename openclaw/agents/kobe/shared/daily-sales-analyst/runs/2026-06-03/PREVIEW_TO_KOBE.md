# Preview para Kobe — 2026-06-03
**Gerado em:** 2026-06-04T10:32:38.698355+00:00
**Modo:** PREVIEW_TO_KOBE
**send_real_allowed:** false
**Global Status:** BLOCKED
**Prompt Version:** v4.0/mercado-livre
**Data Builder Version:** v1.3
**LLM Used:** True

## Protecoes Ativas
- send_real_enabled=false in config
- require_kobe_approval_for_real_send=true — no approval document found

## Resumo por Recipient

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
- **Aviso:** Gate 12 — ADS: ads_summary declara campaigns_active_count=12 com spend_yesterday_brl=0,0 e revenue_ads_yesterday_brl=0,0. Condição de Gate 12 ('campaigns_active_count > 0 E spend=0 com todos os campos zerados') está presente. A L05 tratou corretamente como hipótese em aberto (classificacao: 'hipótese') e a L06 preservou linguagem condicional adequada ('antes de chamar isso de piso orgânico, Yasmin precisa confirmar com Himmel...') — condição para tratamento como APROVADO COM RESSALVA neste gate específico está satisfeita. Ação para o fetcher no próximo ciclo: incluir métricas de funil (impressões e cliques por campanha) no pacote ML para permitir distinguir interrupção real de artefato de billing/atribuição sem depender de confirmação manual de Himmel a cada ciclo. Pendência estrutural recorrente — 13º ciclo sem resolução.
- **Aviso:** Gate 12 — Fulfillment coverage: fulfillment_mix_yesterday_top10 cobre 62 de 142 pedidos (43,7%), bem abaixo do limiar de 70%. A L06 não apresentou esse dado como métrica total — escreveu explicitamente 'no top 10 do dia' na Análise e omitiu da VISÃO com log documentado. Anomalia de cobertura não contaminou a mensagem. Para o fetcher: investigar se é possível calcular fulfillment_mix sobre 100% dos pedidos do dia via logistic_type de todos os pedidos (como já feito nas janelas 7d/30d pelo Supabase) e substituir o cálculo top_10_weighted nos próximos ciclos — isso eliminaria a ressalva de cobertura e permitiria apresentar o dado na VISÃO sem restrições.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-06-03/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
