# Preview para Kobe — 2026-05-21
**Gerado em:** 2026-05-22T15:23:34.847614+00:00
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
- **Aviso:** Os 4 Menores cross-section de nomes de produto derivam de uma decisão de formatação não documentada explicitamente: L06 manteve nomes curtos da L05 na Análise e Prioridades ('Potes de Vidro Tampa Preta', 'Potes Tampa Cinza', 'Kit 10 Potes 1050ml', 'Kit 4 Potes de Vidro Hermético 1050ml') em vez de expandir para os nomes padronizados do Top Produtos. O log de Decisões de formatação registrou que os nomes foram 'expandidos', mas essa expansão ocorreu apenas no Top Produtos — o log é impreciso sobre o escopo da decisão. Para o próximo ciclo: L06 deve definir e registrar explicitamente a política de nomenclatura cross-section (nomes curtos L05 uniformes em todas as seções, ou nomes completos Top Produtos uniformes em todas as seções).
- **Aviso:** O detalhe '(962 unidades vendidas)' foi omitido da Prioridade 3 na tradução da L05 para o Slack. Embora Menor, esse número fundamenta a afirmação de 'maior acumulado em Full no top 10' e deve ser mantido em próximas iterações: detalhes quantitativos que justificam prioridades não devem ser omitidos na simplificação de linguagem.
- **Aviso:** Erro gramatical 'o taxa' (deve ser 'a taxa') na abertura do bullet 1 da Análise. Menor e sem impacto operacional, mas deve ser corrigido em próximas iterações do template de escrita da L06.
- **Aviso:** A compressão de 'subida acima de 0 nos próximos 1-2 ciclos' (L05, Prioridade 1) para 'taxa de cancelamentos subir acima de 0 no próximo ciclo de reputação' (L06) reduz a janela de observação de 1-2 ciclos para 1 ciclo. Menor em contexto de operação diária, mas remove a tolerância temporal originalmente definida pela Condensadora — registrar para alinhamento de escrita futura.

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
