# Preview para Kobe — 2026-05-25
**Gerado em:** 2026-05-26T10:12:56.179648+00:00
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
- **Aviso:** Os dois Menores do Gate 10 reproduzem uma estrutura que veio da própria L05 ('pressiona a reputação verde e o MercadoLíder Gold por dentro'). A correção definitiva deve ser aplicada na L05 no próximo ciclo para que a L06 não precise corrigir um padrão herdado da camada superior.
- **Aviso:** ACOS 14,15% foi arredondado para 14,2% pela L06 conforme regra de percentual com 1 casa decimal. Valor preciso é 14,15; análises de tendência interna devem usar 14,15 para evitar acúmulo de erro de arredondamento em séries comparativas.
- **Aviso:** Cluster IMB501 é referenciado na Análise como 'os Potes Vidro 5 Peças' (MLB3288536143 agregado, 61 pedidos) e no Top Produtos como variações individuais com slack_short_name. A estrutura de dois níveis hierárquicos é correta e está documentada no log da L06, mas Yasmin pode questionar por que há 3 linhas separadas de Potes no Top e uma única menção agregada na Análise — vale alinhar no próximo ciclo se houver dúvida de leitura.

**Artefatos:**
  - `layer0_data_package`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/00-data-package.json`
  - `layer1_estrategica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/01-estrategica.md`
  - `layer2_tatica`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/02-tatica.md`
  - `layer3_operacional`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/03-operacional.md`
  - `layer4_granular`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/04-granular.json`
  - `layer5_condensadora`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/05-condensadora.json`
  - `layer6b_shopee_consolidator`: ``
  - `layer6_slack_writer`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/06-slack-preview.md`
  - `layer7_qa_gate`: `/root/segundo-cerebro/shared/daily-sales-analyst/runs/2026-05-25/yasmin/07-qa.json`

## Acao Requerida

Kobe/Pedro: revisar artefatos acima e decidir:
- [ ] APROVADO — preview aceitavel, pode avancar para send-candidate
- [ ] BLOQUEADO — problemas encontrados, corrigir antes de avancar

---
*Este arquivo e um artefato local. Nenhum envio externo foi realizado.*
