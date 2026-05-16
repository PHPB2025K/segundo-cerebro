<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 15/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 878,00
- Pedidos: 27 pedidos
- Ticket médio: R$ 32,52
- Cancelamentos: 0
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Jarra Medidora de Vidro 500ml — 7 pedidos
- Suporte Controle Gamer — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 4 pedidos
- Kit 6 Xícaras Porcelana Paris 170ml — 1 pedido
- Kit 2 Potes de Vidro 1050ml Retangular — 1 pedido

🔍 ANÁLISE DA CONTA
- Parece dia fraco pelo GMV, mas o volume entregou exatamente o patamar histórico — 27 pedidos contra média 30d de 27,6 e mesmo dia da semana de 27,5. A queda de faturamento é inteiramente explicada pelo ticket, não por perda de tração de pedidos. A hipótese é que o mix-do-dia comprimiu o ticket médio para R$ 32,52 contra R$ 40–43 histórico, mas essa hipótese é consistente com o dado, não provada — o detalhamento do dia não tem receita desagregada por ASIN.
- A execução foi limpa — FBA 100%, zero cancelamentos, reconciliação perfeita — mas o pré-requisito tático central ainda está em aberto: Buy Box por ASIN não está coberta pelos dados disponíveis. O piso operacional confirma que o canal não quebrou, mas a saúde específica dos ASINs líderes requer verificação manual no Seller Central antes de qualquer leitura definitiva sobre condição de escalonamento.
- A cauda girou — 7 SKUs diferentes com 1 pedido cada — mas não tem espessura para absorver variação nos campeões: o ASIN líder responde sozinho por 26% dos pedidos do dia e os top 3 por 59%. Não é possível afirmar se essa concentração é padrão histórico ou variação do dia — hoje é o primeiro registro estrutural da conta.

🎯 PRIORIDADES DO DIA
- Leonardo: checar status de Buy Box nos ASINs líderes diretamente no Seller Central. A postura de observar sem intervir pressupõe operação saudável, mas Buy Box por ASIN não está coberta pelos dados. Confirmar: Buy Box ≥ 85% nos top-3 ASINs valida o pré-requisito operacional; qualquer ASIN líder com Buy Box comprometida inverte a leitura de acomodação para fragilidade operacional ativa. Escalar para resolução imediata se Buy Box em erosão ou ausente em qualquer um dos top-3 — antes de qualquer discussão sobre ADS com Pedro.
- Leonardo: observar ticket médio dos próximos 2 dias sem intervir. Ticket retornando para faixa R$ 38–43 confirma evento pontual de mix; ticket abaixo de R$ 35 por 2 dias consecutivos indica compressão estrutural e muda a tese de acomodação para vulnerável. Escalar para diagnóstico de causa e análise mais profunda com Buy Box confirmada antes de qualquer decisão sobre ADS.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: TL250P e TL6250 — canecas de porcelana tulipa com display_name incorreto no mapeamento interno
- Origem do bloqueio: Granular + Condensadora
- Motivo: divergência confirmada entre raw_title do pedido real (canecas de porcelana tulipa) e display_name do sistema (tigela de vidro) — material e categoria distintos; volume irrelevante hoje (1 pedido cada)
- Agregado autorizado: não — Condensadora indicou que esses produtos não são relevantes para o Slack de hoje pelo volume; bloqueio é por nome publicável incorreto, não por volume
- Tratamento aplicado: omitidos do Top Produtos e da análise
- Aparece na mensagem final: não

- Item bloqueado: hipótese de compressão de ticket por mix como conclusão confirmada
- Origem do bloqueio: Granular + Condensadora
- Motivo: Granular sinalizou explicitamente — hipótese consistente com o dado, não provada; pacote não tem receita desagregada por ASIN
- Agregado autorizado: não aplicável — não é item de produto, é restrição de linguagem
- Tratamento aplicado: preservada como hipótese com linguagem de indício ("a hipótese é que... mas essa hipótese é consistente com o dado, não provada")
- Aparece na mensagem final: sim, com nuance preservada

- Item bloqueado: SPC013 e KJP0041 — confidence medium com mapeamento genérico
- Origem do bloqueio: Condensadora
- Motivo: mapping_status mapped_generic_sku sem revisão confirmada; volume irrelevante (1 pedido cada)
- Agregado autorizado: não
- Tratamento aplicado: omitidos do Top Produtos
- Aparece na mensagem final: não

- Item bloqueado: declaração de operação totalmente validada (Buy Box por ASIN)
- Origem do bloqueio: Granular + Condensadora
- Motivo: Buy Box por ASIN não foi respondida pelo pacote de dados; passar impressão de validação completa seria erro
- Agregado autorizado: não aplicável — restrição de linguagem
- Tratamento aplicado: preservada ressalva explícita na análise e nas prioridades ("Buy Box por ASIN não está coberta pelos dados disponíveis… requer verificação manual")
- Aparece na mensagem final: sim, ressalva preservada integralmente

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Operacional + Granular`, `— base: Tática + Granular`, `— base: Estratégica + Granular`) — metadados de pipeline interno, não pertinentes ao Slack
- Substituição de "a Granular sinalizou" por "o detalhamento do dia não tem receita desagregada por ASIN" — linguagem externa preservando o conteúdo sem expor nome de camada interna
- Substituição de "a Granular marcou" por "não está coberta pelos dados disponíveis" — mesma razão
- Preservação de linguagem de hipótese em todos os pontos onde a Condensadora classificou como hipótese ou confiança média — não transformada em fato
- Preservação de ressalva de Buy Box em ambas as seções de análise e prioridades — Condensadora sinalizou como pré-requisito crítico não respondido; não pode ser omitida
- TL250P e TL6250 omitidos do Top Produtos — bloqueio por display_name incorreto confirmado pela Granular; volume irrelevante hoje e nome publicável seria produto errado
- SPC013 e KJP0041 omitidos do Top Produtos — confidence medium com mapeamento genérico e volume irrelevante (1 pedido cada); Top Produtos exibe apenas produtos com identificação segura e volume relevante
- KIT2PANO800AZ omitido do Top Produtos — confidence medium (mapped_generic_sku) e volume de 1 pedido; mesmo tratamento que SPC013 e KJP0041
- Top Produtos exibe os 5 itens com maior volume e identificação segura: CK4742 (7 pedidos, high), SPC002 (5 pedidos, high), IMB501P (4 pedidos, high), XCP002 (1 pedido, high), KIT2YW1050 (1 pedido, high) — todos com confidence high e mapeamento revisado
- ASIN não exibido para nenhum produto — títulos são claros, unívocos e não ambíguos; nenhum produto foi marcado com risco médio de identificação entre os exibidos; regra de ASIN visível não ativada
- Faturamento de Top Produtos omitido — pacote não tem receita desagregada por produto; exibir valor agregado sem base por produto seria inferência proibida; formato adaptado para `— [pedidos] pedidos` sem faturamento individual
- Quebra de frase longa no terceiro insight da análise ("Não é possível afirmar se essa concentração é padrão histórico ou variação do dia — hoje é o primeiro registro estrutural da conta") — frase original preservada em conteúdo e tese; adequação de comprimento sem mudança de sentido
- Prioridades formatadas com: responsável + ação + evidência + sinal de confirmação/refutação + condição de escalonamento — estrutura exigida pelo prompt preservada integralmente