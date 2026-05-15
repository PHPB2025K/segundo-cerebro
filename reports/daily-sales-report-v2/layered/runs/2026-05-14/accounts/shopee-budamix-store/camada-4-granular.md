### Respostas granulares às perguntas da Operacional

---

#### 1. Pergunta: houve qualquer variação diária de exposição, preço ou feedback operacional especificamente nos três campeões?

- **Status:** não respondida por falta de dado
- **Evidência:** O pacote de dados contém pedidos válidos, títulos reais, SKUs, quantidade e métricas dos top 3 produtos (“Jarra Medidora de Vidro 500ml”, “Potes Vidro Redondos Tampa Preta”, “Kit 2 Potes de Vidro 800ml Quadrado”), mas **não há registro de dados granulares de exposição (ex.: page view, ranking, posição de anúncio), flutuação de preço ao longo do dia ou feedback operacional do anúncio (catálogo, restrição, atualização de anúncio, ou histórico de edição/listagem)**.
    - Dados disponíveis limitam-se a volume por item, SKU, título e ausência de cancelamento, sem nenhuma camada de evento de exposição, alteração de preço intra-dia ou anotação operacional.
- **Leitura:** Não é possível granularizar variação intra-dia de exposição/preço ou intervenção operacional específica nos três campeões apenas com pedidos válidos e top produtos.
- **Conclusão granular:** inconclusivo por falta de dado (ausência de log de exposição/preço/feedback de anúncio)
- **Confiança:** baixa

---

#### 2. Pergunta: existe indício técnico de limitação (catalogação, restrição, atualização de anúncio) nos pedidos residuais da cauda longa?

- **Status:** parcialmente respondida
- **Evidência:**  
    - Pedidos dos itens fora do top 3 (total: 4 pedidos, distribuídos entre 4 produtos, cada um respondendo por 1 pedido).
    - Para todos esses itens, o dado disponível é limitado a:  
        - “Kit 5 Potes de Vidro Hermetico com Tampa Marmita Alimentos Freezer Micro-ondas”  
        - “Kit 6 Canequinhas 100ml”  
        - “Kit 6 Canecas Tulipa 250ml”  
        - Dados presentes: título real do pedido, SKU, platform_item_id, quantidade.
    - **Não há nenhuma indicação agregada de erro de catálogo, restrição, deslistagem ou atualização recente no anúncio nem motivo de bloqueio/cancelamento para esses pedidos**.
    - Porém, a ausência de pedidos com mais de 1 unidade e nenhum pedido adicional nos secundários **pode sugerir mobilidade inercial**.
- **Leitura:** Não há indício explícito de limitação técnica a partir dos campos disponíveis; a ausência total de mobilidade na cauda longa não pode ser atribuída granularmente a restrição ou catalogação. O dado confirma apenas o resultado de vendas nulas/baixas; não permite confirmar se houve tentativa frustrada ou bloqueio invisível sem dado de exposição, motivos de restrição, ou log de atualização.
- **Conclusão granular:** enfraquece a hipótese de limitação técnica explícita — mas mantém possibilidade aberta por falta de dado granulado de restrição.
- **Confiança:** média (dado de pedido real suficiente para ausência de problema explícito, mas amostra mínima e ausência de evento técnico)

---

#### 3. Pergunta: os pedidos dos três campeões vieram pulverizados ao longo do dia ou concentrados em horários/ondas específicas?

- **Status:** não respondida por falta de dado
- **Evidência:** O dado granular entregue não inclui timestamp/hora-evento dos pedidos ou distribuição horária, apenas contagem final por produto.
- **Leitura:** Não é possível afirmar se a concretização dos pedidos dos campeões se deu de modo homogêneo ou concentrado ao longo do dia.
- **Conclusão granular:** inconclusivo por falta de dado (ausência de timestamp/fatia horária dos pedidos).
- **Confiança:** baixa

---

### Investigações próprias

sem investigação adicional motivada hoje

---

### Risco de identificação ou leitura errada

**Nível:** baixo

Todos os produtos citados são identificados pelo nome real do pedido e platform_item_id oriundos do sistema de pedidos Shopee. Não há alias manual, ausência de título ou SKU ambíguo. A conta é única (Budamix Store), e todos os dados são provenientes dos pedidos válidos. Não há evidência de risco de leitura equivocada nem ambiguidade de identificação de produto que exija ressalva ou bloqueio.

---

### Detalhe que a Condensadora não pode perder

- Os três campeões (“Jarra Medidora de Vidro 500ml”, “Potes Vidro Redondos Tampa Preta” e “Kit 2 Potes de Vidro 800ml Quadrado”) respondem sozinhos por 91,4% dos pedidos do dia, cada um identificado por título real do pedido e platform_item_id; não houve ruído de catálogo, e a dependência crítica está materializada sem ambiguidade — Confiança: alta.
- A cauda longa ficou restrita a quatro produtos, todos com apenas um pedido, sem registro de bloqueio, erro de catálogo, cancelamento ou atualização visível — reforçando imobilidade e dependência do mix — Confiança: média (amostra mínima, mas ausência de ruído explícito).
- Nenhuma métrica ou evento granular aponta concentração de pedidos líder em horário específico ou onda operacional — mas esse dado não foi entregue, e qualquer leitura sobre pico/momento de venda é especulativa — Confiança: baixa (não afirmar concentração horária sem base).

---

### O que fica só na memória interna

- platform_item_id dos secundários para checagem futura:  
    - “49056997127” (“Kit 5 Potes de Vidro Hermetico com Tampa Marmita Alimentos Freezer Micro-ondas”)
    - “23036701291” (“Kit 6 Canequinhas 100ml”)
    - “45554989236” (“Kit 6 Canecas Tulipa 250ml”)
- Quantitativo exato por produto: líder (17), vice (13), terceiro colocado (2), secundários (1 cada).
- Falta de timestamp/hora dos pedidos impossibilita auditoria do perfil temporal — necessário log para investigação futura de ondas/concentração horária.
- Não há item em BLOQUEIO PARA SLACK neste ciclo.
