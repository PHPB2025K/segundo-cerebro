<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.087,71
• Pedidos: 91 pedidos
• Ticket médio: R$ 55,91
• Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto — 23 pedidos
• Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo — 13 pedidos
• Jogo 6 Canequinha 100ml Caneca Café Suporte Madeira Alumínio Amarelo — 8 pedidos
• Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
• Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — 5 pedidos
• Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara — 5 pedidos
• Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo — 3 pedidos
• Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto — 3 pedidos
• Kit Conjunto 4 Potes De Vidro 320ml Tampa Hermético 4 Travas Azul-petróleo — 3 pedidos
• Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
• O anúncio do Kit 06 Canequinhas 100ml com Suporte Acrílico provavelmente gerou os 3 cancelamentos do dia — 3 unidades disponíveis na abertura, 3 pedidos, 3 cancelamentos no fechamento e 3 unidades de volta no CD hoje formam um padrão consistente com ruptura seguida de retorno de reserva Full. O estoque não zerou, mas qualquer pedido adicional sem reposição confirmada realiza a ruptura e começa a contaminar a cancellations_rate, hoje em zero.
• O mapa de risco de saúde dos anúncios é mais amplo do que parece: 4 dos top 10 estão em zona crítica ou de atenção, sendo 2 abaixo do limiar de penalização do ML (health 0,75 e 0,71) e 2 exatamente no limiar (health 0,85 e 0,85). Sem trajetória histórica disponível, não dá para saber se estão caindo ou estáveis — mas o fato de os anúncios com health degradada continuarem convertendo sugere que o ADS de Himmel está cobrindo a exposição orgânica que o algoritmo ML está retirando. Esse equilíbrio é frágil.
• A queda de -20,9% em pedidos vs os últimos 7 dias parece deterioração, mas o controle correto é o mesmo dia da semana: ontem ficou -1,6% em pedidos e +32,4% em GMV vs as últimas 4 quartas. O dia foi dentro do patamar esperado — o que estava acima da média era a janela dos últimos 7 dias, não ontem abaixo. O GMV de R$ 5.087,71 foi sustentado por ticket médio mais alto, não por volume maior.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar se há reposição programada ou pendente para o Kit 06 Canequinhas 100ml com Suporte Acrílico no CD do ML — com 3 unidades em estoque Full e giro de 3 pedidos/dia, a ruptura real está a um ciclo de distância. O padrão do dia sugere que os cancelamentos devolveram as reservas ao CD; sem reposição, o próximo grupo de pedidos zera o estoque e contamina a cancellations_rate. Confirmar/refutar: reposição confirmada com prazo ≤ 48h neutraliza o risco; ausência de confirmação até amanhã mantém o nível crítico. Escalar se: reposição não confirmada em 24h — decidir entre suspender o anúncio preventivamente ou registrar o risco aceito.
• Yasmin: checar a trajetória de health dos dois anúncios abaixo do limiar de penalização via Seller Central — Kit 4 Potes De Vidro Hermético 1050ml (health 0,75) e Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (health 0,71) — para saber se estão caindo, estáveis ou em recuperação. Confirmar/refutar: health estável ou em recuperação = manter observação; health caindo em qualquer um por mais 1 dia = investigar causa raiz e avaliar reforço de cobertura ADS com Himmel. Escalar se: health caindo por 2 dias consecutivos em qualquer dos dois — alinhar com Himmel sobre reforço de cobertura ADS preventivo.
• Yasmin: registrar como ponto zero da série ADS os números de ontem — spend R$ 262,19, receita R$ 3.041,56, share ~59,8% do GMV, ROAS ≈ 11,6x, ACOS 4,64%, 11 campanhas ativas. Confirmar/refutar: ADS share acima de 55% por 3 dias consecutivos com ROAS acima de 5x confirma dependência estrutural; ACOS acima de 15% em qualquer dos próximos 3 dias sinaliza pressão de leilão. Escalar se: ACOS acima de 15% por 2 dias seguidos — alinhar com Himmel sobre revisão de segmentação.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: afirmação categórica de que os 3 cancelamentos foram gerados pelo Kit 06 Canequinhas Acrílico (MLB4410218897)
- Origem do bloqueio: Condensadora
- Motivo: breakdown de cancelamentos por anúncio ausente do pacote; evidência apenas circunstancial
- Agregado autorizado: não — a Condensadora não autorizou agregado; orientou preservar linguagem de hipótese
- Tratamento aplicado: texto usa "provavelmente" e descreve o padrão circunstancial sem afirmar como fato
- Aparece na mensagem final: sim, como hipótese com evidência descrita

- Item bloqueado: afirmação de trajetória de health (caindo, estável ou em recuperação) para qualquer anúncio
- Origem do bloqueio: Condensadora
- Motivo: pacote disponibiliza apenas valor pontual; série temporal ausente
- Agregado autorizado: não
- Tratamento aplicado: texto preserva incerteza — "não dá para saber se estão caindo ou estáveis"
- Aparece na mensagem final: sim, com ressalva explícita

- Item bloqueado: afirmação de que o ADS de Himmel cobre especificamente os anúncios com health degradada
- Origem do bloqueio: Condensadora
- Motivo: ads_summary contém apenas totais agregados; cobertura por anúncio não verificável
- Agregado autorizado: não
- Tratamento aplicado: texto usa "sugere que o ADS de Himmel está cobrindo", preservando hipótese
- Aparece na mensagem final: sim, como hipótese

- Item bloqueado: códigos MLB no corpo da mensagem
- Origem do bloqueio: Condensadora
- Motivo: identificadores técnicos não adequados para comunicação com Yasmin
- Agregado autorizado: não aplicável
- Tratamento aplicado: omitidos; usados títulos reais dos anúncios ML conforme top_items_details
- Aparece na mensagem final: não

- Item bloqueado: aliases internos Budamix como nomes de produto (display_names)
- Origem do bloqueio: Condensadora / Granular
- Motivo: divergência estrutural confirmada — top_products[i].title == display_name interno; título real está em top_items_details[i].title e raw_title
- Agregado autorizado: não aplicável
- Tratamento aplicado: todos os produtos citados usam título real ML (top_items_details[i].title / raw_title)
- Aparece na mensagem final: não

---

### Decisões de formatação

- Uso de títulos reais ML (top_items_details[i].title / raw_title) em vez de display_names para todos os 10 produtos do Top Produtos — motivo: divergência estrutural confirmada pela L04; display_names são aliases internos Budamix não reconhecidos por Yasmin na plataforma
- Preservação de linguagem de hipótese para o insight dos cancelamentos ("provavelmente", descrição circunstancial) — motivo: Condensadora classificou como hipótese e bloqueou afirmação categórica
- Preservação de linguagem de incerteza para trajetória de health ("não dá para saber se estão caindo ou estáveis") — motivo: dado de série temporal ausente do pacote; Condensadora bloqueou classificação de direção
- Preservação de linguagem de hipótese para cobertura ADS por anúncio ("sugere que o ADS de Himmel está cobrindo") — motivo: Condensadora bloqueou afirmação por ausência de breakdown por anúncio no pacote
- Remoção de metadados internos das camadas ("base: Estratégica | Granular", "padrão D — Enquadramento estrutural" etc.) — motivo: metadados de pipeline não pertencem à comunicação com Yasmin
- Omissão de códigos MLB em todos os campos visíveis — motivo: bloqueio explícito da Condensadora; IDs técnicos não adequados para Slack operacional
- Seção VISÃO sem comparações temporais — motivo: regra estrutural; comparações pertencem à Análise da Conta
- Dados de ADS registrados na prioridade 3 como valores de referência sem comparação — motivo: ponto zero da série; sem histórico comparável disponível
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas: produto com confiança medium (mapping_status: mapped_generic_sku) incluído no Top Produtos — motivo: Condensadora não emitiu bloqueio para esse item; confiança media não implica bloqueio automático; título real ML disponível e consistente com raw_title
- Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto e Kit 06 Canequinhas: ambos com confiança medium incluídos no Top Produtos pelo mesmo motivo — sem bloqueio da Condensadora, raw_title e top_items_details.title consistentes
- Ranking mantido em ordem decrescente por pedidos, conforme pacote validado