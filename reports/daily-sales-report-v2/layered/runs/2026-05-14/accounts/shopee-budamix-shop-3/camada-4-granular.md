### Respostas granulares às perguntas da Operacional

---

- Pergunta: algum produto fora do top 3 apresentou aproximação relevante em número de visitas/carrinhos, ainda que sem converter em venda?  
- Status: não respondida por falta de dado  
- Evidência: O pacote de dados validado enviado para análise contém métricas exclusivamente relacionadas a pedidos válidos, GMV, ticket médio, cancelamentos e top produtos por pedidos/quantidade efetivamente vendidos. Não há dados sobre visitas, visualizações de produto, adição a carrinho, ou métricas de comportamento pré-compra em nível granular de produto dentro deste pacote.  
- Leitura: Não é possível afirmar se algum produto fora do top 3 teve tração em visitas ou comportamento de carrinho, já que tais eventos não são informados neste recorte.  
- Conclusão granular: inconclusivo por falta de dado  
- Confiança: baixa (ausência total do tipo de evidência solicitado)  

---

- Pergunta: houve oscilação atípica na exposição/vitrine dos campeões ao longo do dia, que ajude a explicar a manutenção da concentração ou resistência à diversificação?  
- Status: não respondida por falta de dado  
- Evidência: O pacote validado não possui métricas ou logs horários sobre exposição em vitrine (ex: impressões, mudanças de ranking, alteração manual de destaque), nem detalhamento de comportamento ao longo do dia. Só há registro final do consolidado de vendas por produto.  
- Leitura: Não se pode verificar se houve alteração relevante na exposição dos produtos campeões, nem se a Shopee alterou ou não o posicionamento ao longo do dia.  
- Conclusão granular: inconclusivo por falta de dado  
- Confiança: baixa (tipo de métrica ausente do pacote fornecido)  

---

- Pergunta: existe recorrência ou variação sazonal que explique volume de pedidos abaixo em relação ao histórico, sobretudo nos mesmos dias da semana?  
- Status: parcialmente respondida  
- Evidência:  
    - Métricas históricas apresentadas indicam que o total de pedidos do dia (23) ficou consistentemente abaixo do comparativo de 30 dias (-19%), 60 dias (-32,6%) e do mesmo dia da semana anterior (-22%).  
    - Não há, no pacote fornecido, dados por semana anterior detalhados, registro de sazonalidade, feriados regionais, ou detalhamento de comportamento fora das métricas absolutas (“orders_vs_same_weekday_pct”: -22.0).  
- Leitura: O padrão de queda nos pedidos parece alinhado com uma tendência contínua de redução no comparativo temporal, sem indicativo de anomalia pontual ou ressurgimento sazonal típica. Porém, faltam dados externos (ex: calendário promocional Shopee, feriados, histórico multi-ano) para cravar se há fator externo explicativo, o que limita a explicação exclusivamente a tendência interna da base.  
- Conclusão granular: complica — a evidência mostra decréscimo persistente, mas não permite isolar sazonalidade ou efeito de calendário.  
- Confiança: média (a queda é estatisticamente robusta no dado interno, mas o motivo permanece indeterminado devido à ausência de contexto externo/histórico mais profundo)  

---

### Investigações próprias

sem investigação adicional motivada hoje

---

### Risco de identificação ou leitura errada

**Baixo.**  
- Todos os produtos citados contam com título real visível a partir do pedido (“Kit 6 Canecas Retas 200ml”, “Kit 6 Canecas Tulipa 250ml”, “Kit 3 Potes de Vidro Hermético” e demais), acompanhados de platform_item_id explícito por variação e referência segura ao SKU interno apenas para apoio cruzado.
- Não há uso de alias manual, SKU ambíguo, ausência de título, ausência de shop_id (por ser conta única, a associação é direta na Shopee).
- O único fator limitante relevante para confiança plena das respostas é a ausência das métricas solicitadas nas perguntas 1 e 2, o que limita a possibilidade de erro de identificação dos padrões dos campeões, mas não dos produtos em si.

Conclusão: risco de identificação **baixo** para concentração e desempenho dos produtos, e risco de **leitura incompleta** por déficit de métricas comportamentais externas ao escopo de vendas.

---

### Detalhe que a Condensadora não pode perder

- "Os três produtos campeões respondem por 78,3% dos pedidos válidos na data — se a mensagem não detalhar este grau de concentração específica, dilui o risco real de dependência operacional. — Confiança: alta."
- "Nenhum produto fora do top 3 apresentou sinal mensurável de tração em vendas — qualquer menção a possível reação ou efeito de tentativa tática de diversificação não está sustentada neste recorte. — Confiança: alta."
- "A queda de pedidos em relação a períodos anteriores segue padrão contínuo negativo, sem evidência interna de sazonalidade ou evento externo que explique — não há anomalia pontual, mas sim continuidade da tendência de enfraquecimento. — Confiança: média."

---

### O que fica só na memória interna

- platform_item_id dos top 6 produtos (para rastreio futuro de mix e identificação de variação entre períodos):  
    - Kit 6 Canecas Retas 200ml — platform_item_id: 57756043479  
    - Kit 6 Canecas Tulipa 250ml — platform_item_id: 50954968481  
    - Kit 3 Potes de Vidro Hermético — platform_item_id: 23094048438  
    - Kit 2 Potes de Vidro 800ml Quadrado — platform_item_id: 23298676159  
    - Conjunto 2 Potes de Vidro 320ml Hermético Quadrado Marmita — platform_item_id: 22298562359  
    - Kit Jogo 6 Potes Vidro Retangulares Hermético Tampa Travas Marmita Fit — platform_item_id: 23294048241  
- Lista completa dos SKUs de todos os itens do dia  
- Detalhamento percentual do ticket médio versus histórico para comparação interna
