### Respostas granulares às perguntas da Operacional

---

- **Pergunta:** há concentração dos cancelamentos nos campeões ou eles permanecem dispersos nos pedidos do dia?
- **Status:** respondida
- **Evidência:**
    - Os dois cancelamentos do dia se distribuíram da seguinte forma (dados extraídos dos pedidos válidos da conta):
        1. **Produto visível:** "Kit 2 Potes de Vidro 1520ml"
            - Conta: Budamix Oficial / Conta 2
            - shop_id: não explicitado individualmente (única conta relevante na base atual)
            - Fonte: orderItems / pedido real
        2. **Produto visível:** "Kit 6 Canecas Tulipa 250ml"
            - Conta: Budamix Oficial / Conta 2
            - shop_id: idem acima
            - Fonte: orderItems / pedido real
- **Leitura:** Os cancelamentos não se concentraram em um único campeão. Ambos foram em produtos que estão entre os top 4 do dia, mas nenhum produto concentrou múltiplos cancelamentos e não há indício de focalização sistêmica — cada cancelamento ocorreu em pedido distinto de produto campeão, sem múltiplas ocorrências por item.
- **Conclusão granular:** confirma dispersão operacional dos cancelamentos; não há antecipação de problema focalizado.
- **Confiança:** alta

---

- **Pergunta:** nos horários de pico (19-22h), houve algum movimento fora do padrão (queda maior ou estabilidade relativa)?
- **Status:** não respondida por falta de dado
- **Evidência:** O pacote validado de dados não inclui o recorte horário dos pedidos (timestamp/hora de venda ausente ou não entregue neste pacote para granularização), inviabilizando a checagem específica do comportamento nas faixas horárias de pico.
- **Leitura:** Não existe elemento granular para avaliar padrão ou anomalia nos horários entre 19h e 22h neste dia.
- **Conclusão granular:** inconclusivo por falta de dado; investigação bloqueada até nova base com timestamps horários por pedido.
- **Confiança:** não aplicável

---

- **Pergunta:** há sinal de conversão fora do top 3 em faixas relevantes, mesmo que abaixo do corte de campeão?
- **Status:** respondida
- **Evidência:** Pedidos válidos ranqueados após o top 3 mostram a seguinte conversão, sempre 1 pedido por produto:
    - **Produto visível:** "Kit 6/12 Rolos De Fita Adesiva Transparente 45mm X 500 Metros Embalagem Resistente Larga Embalar"
        - shop_id: Budamix Oficial / Conta 2
        - Fonte: orderItems / pedido real
        - Pedidos: 1
    - **Produto visível:** "Kit 9 Potes Vidro Quadrados Hermético Vedação Tampa 4 Travas Marmita"
        - shop_id: Budamix Oficial / Conta 2
        - Fonte: orderItems / pedido real
        - Pedidos: 1
    - **Produto visível:** "Budamix Kit 6 Porta Copos MDF 6mm Com Suporte Corte Laser Design Solaris Descanso Copo Bolacha Mesa"
        - shop_id: Budamix Oficial / Conta 2
        - Fonte: orderItems / pedido real
        - Pedidos: 1
- **Leitura:** Fora do top 3, nenhum produto apresentou padrão superior a um único pedido, e nenhum teve avanço relevante (todos permanecem sem múltiplas conversões ou indicação de início de reboque). O volume do mix secundário é insignificante frente ao volume total, sem sinal de estabilização.
- **Conclusão granular:** confirma ausência de reação no mix secundário; cenário segue polarizado nos campeões.
- **Confiança:** alta

---

### Investigações próprias

sem investigação adicional motivada hoje

---

### Risco de identificação ou leitura errada

**Nível de risco:** baixo

**Fontes de risco analisadas:** Todos os produtos citados têm título real do pedido e platform_item_id confirmados nos pedidos válidos. Não há indício de conflito por SKU ambíguo, alias manual, título ausente, ou shop_id ausente (a base disponível é só da Conta 2, conforme escopo). Dados trabalhados são por pedido real, sem uso de catálogo, Ads ou memória para atribuição de produto.

**Impacto:** O risco de erro de identificação de produto ou leitura errada é considerado baixo; todas as evidências utilizadas podem ser citadas nominalmente sem bloqueio para Slack e sustentam as conclusões com segurança.

---

### Divergência entre fontes

Não houve divergência detectada entre fontes de dados relevantes neste ciclo. Todas as leituras referenciam pedidos reais (orderItems válidos) da conta Budamix Oficial / Conta 2, e a conciliação do subset da Shopee está ok na reconciliação fornecida.

---

### Evidência conflitante

Não há hipóteses abertas com evidências conflitantes na granularização do dia.

---

### Detalhe que a Condensadora não pode perder

- Os dois cancelamentos do dia estão dispersos: cada um ocorreu em um produto campeão distinto, sem concentração que sugira sintoma focalizado ou operacional — Confiança: alta.
- Fora do top 3, nenhum produto secundário gerou mais de um pedido; não há início de reação ou fortalecimento de cauda — qualquer mensagem que sugira diluição do mix ou variação relevante secundária estará errada — Confiança: alta.
- O padrão de concentração nos campeões se mantém (top 3 respondem por 62,5% dos pedidos) — sem emergente nos secundários e sem agravamento súbito para patamar crítico — Confiança: alta.

---

### O que fica só na memória interna

- IDs de todos os platform_item_id dos produtos vendidos no dia:
    - 19098263852, 22495667316, 23593154831, 46154989273, 20198187838, 23198542584, 48508383354
- SKUs internos para rastreio e family codes de cada pedido
- Lista exata de todos os títulos dos produtos vendidos (para checagem técnica futura)
- Detalhamento completo dos pedidos por SKU/variation (apenas para troubleshooting granular — não enviar ao Slack)
- Log: ausência de dados horários por pedido impossibilitou granularização do item 2 — registrar para cobrança futura em coleta
