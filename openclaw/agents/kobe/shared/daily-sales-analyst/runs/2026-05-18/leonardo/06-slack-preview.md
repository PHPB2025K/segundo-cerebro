<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 18/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 1.839,70
- Pedidos: 45 pedidos
- Ticket médio: R$ 40,88
- Cancelamentos: 2
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 12 pedidos
- Jarra Medidora de Vidro 500ml — 12 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 3 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml — 3 pedidos
- Suporte Controle Gamer — 2 pedidos
- Kit 6 Xícaras Porcelana Paris 170ml — 2 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas — 2 pedidos

🔍 ANÁLISE DA CONTA
- O dia teve volume excepcional — +67% sobre o padrão histórico de segundas-feiras e acima da média dos últimos 7 dias — mas a leitura positiva não pode ser tratada como patamar confirmado: o dado de Buy Box dos dois ASINs líderes não estava disponível e, sem ele, não dá pra separar se a demanda foi orgânica sustentada ou janela momentânea de exposição favorável. Acionar escalonamento de ADS agora é precipitado com base no que está disponível.
- A dependência estrutural da conta é maior do que parece na leitura individual: a família de potes redondos (variações tampa preta + tampa cinza, dois ASINs distintos com estoque FBA separado) somou 15 pedidos — 33% do canal — e a Jarra Medidora somou outros 27%, chegando a 60% do volume concentrado em dois vetores do mesmo nicho. Ruptura em qualquer variação dos potes ou na jarra derruba diretamente o resultado, sem cauda suficiente para absorver.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box dos dois ASINs líderes — potes redondos (variação tampa preta) e Jarra Medidora 500ml. É o ponto cego que bloqueia qualquer leitura segura do dia: sem Buy Box ≥85% confirmado nos dois, não dá pra saber se o volume veio de exposição orgânica estável ou de janela temporária. Buy Box ≥85% nos dois confirma base operacional sólida e abre o caminho para conversar ADS com Pedro; abaixo disso, pausa em ADS se mantém. Escalar para Pedro se Buy Box estiver abaixo de 85% em qualquer dos dois — como problema operacional a resolver, não como oportunidade de ampliar tráfego.
- Leonardo: verificar cobertura de estoque FBA dos dois ASINs líderes. 100% dos pedidos rodaram via FBA sem nenhum fallback — ruptura não é hipótese distante se a cobertura estiver curta. Cobertura ≥14 dias confirma que não há urgência de reposição; abaixo de 7-10 dias, acionar logística antes de qualquer outro movimento.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: TL250B e TL6250 — display_name interno ("Tigela de Vidro 250ml" / "Kit 6 Tigelas de Vidro 250ml")
- Origem do bloqueio: Granular + Condensadora
- Motivo: display_name incorreto — raw_title dos pedidos reais descreve canecas de porcelana Tulipa; citar pelo display_name interno nomearia o produto errado no Slack
- Agregado autorizado: não (a Condensadora orienta usar o título visível do pedido real se necessário citar)
- Tratamento aplicado: TL250B citado pelo raw_title ("Kit 6 Canecas de Porcelana Tulipa 250ml"); TL6250 citado pelo raw_title ("Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas")
- Aparece na mensagem final: sim, como título do pedido real (não como display_name interno)

- Item bloqueado: JMOCE e KIT2CK4742 — citação com certeza de nome
- Origem do bloqueio: Granular + Condensadora
- Motivo: mapeamento genérico por fallback de título, confiança média
- Agregado autorizado: não
- Tratamento aplicado: KIT2CK4742 não aparece na mensagem (1 pedido, confiança média, abaixo do corte de volume relevante); JMOCE não aparece na mensagem pelo mesmo motivo
- Aparece na mensagem final: não

- Item bloqueado: afirmação de ganho de patamar confirmado/consolidado
- Origem do bloqueio: Condensadora
- Motivo: ausência de Buy Box impede conclusão; a Condensadora instrui usar "em trajetória ascendente" ou "patamar em construção"
- Agregado autorizado: sim — linguagem de indício preservada
- Tratamento aplicado: insight escrito com ressalva explícita de que o patamar não pode ser tratado como confirmado
- Aparece na mensagem final: sim, como ressalva preservada

- Item bloqueado: cancelamentos com atribuição de produto ou ASIN
- Origem do bloqueio: Granular + Condensadora
- Motivo: dado não disponível no pacote
- Agregado autorizado: não
- Tratamento aplicado: cancelamentos citados apenas como número total na VISÃO (2 cancelamentos), sem atribuição de produto
- Aparece na mensagem final: sim, apenas como dado objetivo sem atribuição

---

### Decisões de formatação

- Remoção de metadados internos das análises ("base: Estratégica + Operacional + Granular", "padrão B", "padrão D") — itens internos de pipeline não vão para Slack conforme regra
- TL250B e TL6250 citados pelo raw_title do pedido real, não pelo display_name mapeado — bloqueio da Condensadora; display_name descreve produto errado (porcelana → vidro, caneca → tigela)
- JMOCE e KIT2CK4742 omitidos do Top Produtos — confiança média por mapped_generic_sku e volume de 1 pedido cada; abaixo do limiar de citação segura e relevância de volume
- Top Produtos em ordem decrescente por pedidos: IMB501P (12), CK4742 (12), IMB501C (3), TL250B (3), SPC002 (2), XCP002 (2), TL6250 (2) — empates de pedidos mantidos com a variação de potes (IMB501C) antes de outros por pertencer à família líder
- ASIN omitido de todos os itens do ranking — confidence high nos líderes com título identificável suficientemente, sem ambiguidade que exija ASIN visível; decisão registrada item a item: IMB501P (título claro, sem ASIN), CK4742 (título claro, sem ASIN), IMB501C (título claro, sem ASIN), TL250B (raw_title usado, identifica produto, sem ASIN), SPC002 (título claro, sem ASIN), XCP002 (título claro, sem ASIN), TL6250 (raw_title usado, identifica produto, sem ASIN)
- Família IMB501 mantida separada em duas linhas (tampa preta 12 pedidos, tampa cinza 3 pedidos) — são ASINs distintos com estoque FBA separado; consolidar seria erro de agregação indevida, conforme regra de variação vendável
- Análise da conta usa dois insights da Condensadora, preservando tese, nuance e ressalva de Buy Box indisponível — sem simplificação que mude sentido
- Prioridades do dia preservam condição de confirmação/refutação e gatilho de escalonamento para Pedro exatamente como entregue pela Condensadora
- Frase de escalonamento para Pedro preservada nas prioridades — veio explicitamente da Condensadora/Tática como condição operacional
- Sem omissão de insight por confiança baixa global — confiança média, não baixa; dois insights são o máximo sustentável conforme alerta da Condensadora, e dois foram entregues
- Comparações temporais (+67%, médias históricas) presentes apenas na seção ANÁLISE DA CONTA, não na VISÃO — conforme regra de separação dado objetivo vs. interpretação