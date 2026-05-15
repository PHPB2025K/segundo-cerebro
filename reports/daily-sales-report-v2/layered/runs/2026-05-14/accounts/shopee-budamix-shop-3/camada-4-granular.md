### Respostas granulares às perguntas da Operacional

---

#### 1. Pergunta: há algum padrão operacional ou evento nos horários de venda que explique o volume baixo mesmo com ticket alto?

- **Status:** não respondida por falta de dado
- **Evidência:** O pacote validado não contém a relação detalhada de horários dos pedidos do dia nem distribuição horária dos pedidos. Apenas o total agregado do dia está disponível.
- **Leitura:** Não é possível confirmar concentração em horários específicos nem identificar eventos pontuais que possam explicar o volume reduzido em contraposição ao ticket médio elevado.
- **Conclusão granular:** inconclusivo por falta de dado
- **Confiança:** baixa

---

#### 2. Pergunta: as vendas de produtos de cauda (fora do top 3) foram vinculadas a campanhas específicas, cupons ou ações pontuais?

- **Status:** não respondida por falta de dado
- **Evidência:** O pacote da conta não inclui marcadores de campanha, uso de cupons ou referência a ações promocionais atreladas aos pedidos. Tampouco há no detalhamento dos itens/pedidos qualquer indicação de origem promocional ou atribuição de campanha.
- **Leitura:** Não há como afirmar se as vendas de cauda foram impulsionadas por ações específicas; permanece desconhecido se foram totalmente orgânicas ou motivadas.
- **Conclusão granular:** inconclusivo por falta de dado
- **Confiança:** baixa

---

#### 3. Pergunta: há indício de indisponibilidade, ruptura ou exposição reduzida dos produtos fora do top 3?

- **Status:** parcialmente respondida
- **Evidência:** Os pedidos validados mostram que todos os produtos fora do top 3 (pelos pedidos do dia 14/05/2026) tiveram pedidos, ainda que isolados e em volume mínimo:
    - Produto visível: "Conjunto 2 Potes de Vidro 320ml Hermético Quadrado Marmita 4 Travas BPA Free"
      - Conta: Budamix Shop / Conta 3
      - shop_id: 22298562359
      - Fonte: orderItems / pedido real
      - Pedidos: 1
    - Produto visível: "Kit Jogo 6 Potes Vidro Retangulares Hermético Tampa Travas Marmita Fit"
      - Conta: Budamix Shop / Conta 3
      - shop_id: 23294048241
      - Fonte: orderItems / pedido real
      - Pedidos: 1
  Não há, no entanto, informações sobre ruptura de estoque, status de exposição nos listings ou campanhas de mídia. O conjunto de pedidos prova que ao menos estavam disponíveis para serem vendidos, mas não esclarece se todos os demais itens do catálogo estavam igualmente expostos ou se houve alguma parcialidade na oferta.
- **Leitura:** Ausência total de alguns produtos não pode ser afirmada ou negada; mas ao menos dois itens de cauda realizaram venda, indicando disponibilidade parcial. Não há evidência sobre exposição reduzida para outros SKU não vendidos.
- **Conclusão granular:** complica — há indício de disponibilidade mínima em parte da cauda, mas não há base para afirmar ausência de ruptura/exposição reduzida nos demais itens.
- **Confiança:** média (a base mostra apenas o que foi vendido, sem acesso ao panorama de estoque ou exposição geral)

---

### Investigações próprias

Sem investigação adicional motivada hoje.

---

### Risco de identificação ou leitura errada

**Classificação:** baixo

A camada granular dispõe dos nomes dos produtos exatamente como constam nos pedidos reais, todos os itens vêm acompanhados do shop_id, display_name e/ou título real. Não há uso de alias manual, nem ausência de título, plataforma_item_id ou shop_id que fragilizem a identificação de item no Shopee para esta conta. Isso garante rastreabilidade clara dos produtos líderes e de cauda dentro do que foi vendido.  
O único risco moderado, marginal, é para SKUs do catálogo que não tiveram pedidos no dia, para os quais não se pode atestar exposição, mas isso não afeta a confiança das evidências reportadas (pois são baseadas apenas em pedidos efetivos).

---

### Detalhe que a Condensadora não pode perder

- Todos os itens de cauda que apareceram em pedidos no dia foram vendidos em quantidades mínimas (1 pedido cada), e **só se pode atestar disponibilidade para eles, não para o restante potencial do mix** — não confundir “mix disponível” com “mix saudável” — Confiança: média.
- Nenhuma evidência granular de campanha, promoção ou cupom associada aos pedidos de cauda foi registrada — não confundir microvenda fora do top 3 com resultado de ação ativa — Confiança: baixa (informação ausente, não negativa).
- A identificação dos produtos vendidos é robusta — todos os itens listados (top 3 e cauda) possuem nome real, shop_id corretos e origem em pedido validado — **não existe risco de erro de atribuição nominal no reporte** — Confiança: alta.

---

### O que fica só na memória interna

- Lista exata de shop_id e platform_item_id de cada item vendido para eventuais tracebacks futuros.
- O detalhe de que os produtos de cauda vendidos no dia foram:
    - "Conjunto 2 Potes de Vidro 320ml Hermético Quadrado Marmita 4 Travas BPA Free" — shop_id: 22298562359, platform_item_id: 22298562359
    - "Kit Jogo 6 Potes Vidro Retangulares Hermético Tampa Travas Marmita Fit" — shop_id: 23294048241, platform_item_id: 23294048241  
- Anotação: ausência de venda ≠ prova de indisponibilidade, mantendo o tema para ciclos futuros caso haja acesso a estoque/listing.  
- Ausência de detalhamento de horário, campanha/cupom, exposure/stock — limitações explícitas a serem revisitadas se o dado vier em ciclos posteriores.
