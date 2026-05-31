<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 30/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.678,64
• Pedidos: 130
• Ticket médio: R$ 43,68
• Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 47 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 15 pedidos
• Kit 6 Canecas Lisas 200ml — 9 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 9 pedidos
• Kit 4 Potes 1050ml — 7 pedidos

🔍 ANÁLISE DA CONTA
• O sábado foi forte: 130 pedidos e R$ 5.678,64 de Faturamento, acima das médias de 30 e 60 dias e dos quatro sábados anteriores. O ticket de R$ 43,68 está menor porque o cluster Potes Vidro 5 Peças dominou o dia com 54,6% do volume — é composição natural de sábado, não erosão de preço.
• Dois anúncios Full fecharam o dia com ~2 dias de cobertura de estoque simultaneamente: o Conjunto Kit 6 Potes Vidro Hermético Tampa Azul-petróleo (Catálogo, 7 unidades pós-baixa de 3 pedidos) e o cluster Potes Vidro 5 Peças (Clássico, 149 unidades pós-baixa de 75 unidades do dia, que concentrou 54,6% do volume). O Catálogo tem agravante de perda de Buy Box com recuperação lenta. O cluster impacta muito mais o Faturamento se romper. MercadoLíder Platinum está a R$ 23.327,75 — previsão de ~5 dias ao ritmo atual — e qualquer cancelamento automático pode comprimir essa janela diretamente.
• Parece que o ADS pode estar cobrindo a queda de alcance orgânico do cluster Potes Vidro 5 Peças: o anúncio está com qualidade em regular pelo oitavo ciclo seguido, sem sinal de recuperação, e o ADS respondeu por 59,5% do Faturamento com ACOS na série 4,4% → 10,96% → 8,23%. A campanha ainda é eficiente no parâmetro do dia (ROAS 11x) e nenhum gatilho foi cruzado hoje — observação continua no próximo ponto da série.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar se tem reposição em trânsito ao CD do ML para o Conjunto Kit 6 Potes Vidro Hermético Tampa Azul-petróleo (Catálogo Full, 7 unidades pós-baixa) e para o cluster Potes Vidro 5 Peças (Full, 149 unidades pós-baixa de 75 do dia) — checar os dois no mesmo movimento. Ruptura em qualquer um gera cancelamento automático e comprime a janela de ~5 dias para MercadoLíder Platinum (gap R$ 23.327,75). O Catálogo tem agravante: Buy Box demora a se recuperar se romper. Confirmar/refutar por: reposição confirmada ou estoque em recomposição nos dois = risco neutralizado; Catálogo com menos de 3 unidades ou pausado, ou cluster com menos de 80 unidades = ruptura ativa confirmada. Escalar se: taxa de cancelamentos da reputação sair de zero, ou os dois anúncios sem reposição confirmada em 24h.
• Yasmin: registrar a leitura de hoje da qualidade do anúncio do cluster Potes Vidro 5 Peças (em regular, oitavo ciclo sem mudança) e do Kit 4 Potes 1050ml (em regular, estável) — sem acionar Himmel ainda. Nenhum cruzou o gatilho hoje. Confirmar/refutar por: qualidade de qualquer um abaixo de 0,70 no próximo ciclo, ou ACOS acima de 10% com ADS respondendo por mais de 60% do Faturamento no segundo ciclo consecutivo. Escalar se: qualquer dos dois gatilhos — Yasmin alinha com Himmel sobre cobertura preventiva.

Dia analisado: 30/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

`o_que_nao_pode_ir_para_slack` da L05 retornou vazio. Nenhum item bloqueado pela L04 Granular (`risco_identificacao.bloqueios_para_slack = []`). Todos os 10 produtos do top_products estão liberados para uso.

---

### Decisões de formatação

**Metadados internos**
- Campos `padrao`, `base` e `classificacao` removidos de todos os insights — metadados de pipeline, não expostos no Slack.

**Preservação de nuance por classificação**
- Insight 2 (`classificacao: "risco latente"`): uso de "pode comprimir" em vez de "comprime"; linguagem prospectiva mantida para o risco de ruptura.
- Insight 3 (`classificacao: "hipótese"`): uso de "parece que o ADS pode estar cobrindo", "segue eficiente no parâmetro do dia" — hipótese preservada, nenhuma certeza introduzida.

**Nível de qualidade do anúncio — pontuação numérica**
- `health=0,71` e `health=0,75` não aparecem em parênteses na mensagem — uso exclusivo do nome da faixa ("em regular"), conforme regra obrigatória. Valor numérico do gatilho (0,70) aparece apenas na condição de confirmação/refutação da Prioridade 2, não como descrição da faixa atual.

**Nomes de produto — Top Produtos (mapeamento canônico)**
- IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico).
- IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico).
- CLR002 — usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico).
- IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico).
- KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico).

**Nomes de produto — Análise e Prioridades**
- Cluster IMB501 (MLB3288536143, três variações IMB501P/C/V compartilhando o mesmo anúncio): referenciado como "cluster Potes Vidro 5 Peças" em todas as menções de Análise e Prioridades — raiz comum dos três slack_short_names, adequado para referência agregada do anúncio único. L05 usou o título ML longo "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita"; L06 usou "cluster Potes Vidro 5 Peças". Divergência registrada — motivo: padronização com a raiz dos slack_short_names do Top Produtos e clareza operacional para Yasmin.
- MLB6437847224 (KIT6S097): slack_short_name null — usado display_short "Conjunto Kit 6 Potes Vidro Hermético Tampa Azul-petróleo" (fallback automático; sem mapeamento manual para SKU KIT6S097). L05 usou "Conjunto Kit 6 Potes Vidro Hermético Vedação Tampa 4 Travas Azul-petróleo"; L06 usou display_short com ruído SEO ("Vedação", "4 Travas") já removido pelo pipeline L00. Divergência registrada — motivo: aplicação do fallback display_short conforme regra.
- Kit 4 Potes 1050ml (KIT4YW1050): usado slack_short_name "Kit 4 Potes 1050ml" nas Prioridades. L05 usou "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo". Divergência registrada — motivo: padronização com mapeamento canônico do Top Produtos.

**Traduções de glossário aplicadas**
- "ETA de 5 dias" → "previsão de ~5 dias ao ritmo atual".
- "ADS share" → "ADS respondeu por 59,5% do Faturamento" e "ADS respondendo por mais de 60% do Faturamento" — nunca "ADS share" no Slack.
- "GMV" → "Faturamento" em todas as ocorrências.
- `cancellations_rate` → "taxa de cancelamentos da reputação".

**Modalidade de envio — omissão da seção VISÃO**
- Modalidade de envio (Full / Cross-Docking) omitida da seção 📊 VISÃO MERCADO LIVRE. Dado disponível (`fulfillment_mix_yesterday_top10`) cobre apenas os 47 pedidos do top10 de 130 totais (~36% de cobertura), não representando a totalidade do dia sem ressalva. Condensadora não autorizou exibição com cobertura explícita nesta seção. Modalidade de envio tratada exclusivamente na 🔍 ANÁLISE DA CONTA, conforme regra da seção.

**Atribuição de responsável**
- "Yasmin:" adicionado no início de ambas as prioridades — L05 não atribui responsável; L06 atribui conforme regra fixa para Mercado Livre.

**Frases longas**
- Insights e prioridades da L05 quebrados em frases mais curtas — diretriz Pedro 2026-05-17 e princípios de comunicação simples 2026-05-25. Tese, classificação e números preservados integralmente.

**alertas_de_confianca.nivel = "media"**
- Nível médio: dois insights com nuance de hipótese/risco latente preservados com linguagem de indício. Nenhum insight foi suprimido por confiança — o nível médio não exige corte, apenas preservação de ressalvas, aplicada nos insights 2 e 3.