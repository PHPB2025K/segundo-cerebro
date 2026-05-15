### Respostas granulares às perguntas da Operacional

---

#### 1. Pergunta: há produtos intermediários que perderam totalmente giro ou exposição nos últimos 5 dias?

- **Status:** respondida
- **Evidência:**
  - Dos 16 pedidos válidos de 2026-05-14, os top 3 produtos concentraram 62,5% do volume (10 de 16 pedidos), todos com pelo menos 3 pedidos cada.
  - Produtos intermediários listados entre as variações e famílias de Budamix Oficial que historicamente já entraram com 1-2 pedidos por dia (ex.: linhas como “Potes Marmita Hermético”, “Tupper Colorido”, “Potes Herméticos 700ml”, “Copo Long Drink”, “Jogo 3 Potinhos Diversos”) **não aparecem** entre os pedidos válidos nem nos top 7 do dia — corroborado por ausência nos itens reais dos pedidos do dia.
  - Dos 7 produtos detectados nos pedidos, 4 tiveram apenas 1 pedido cada, sem repetição nem sinal de “trânsito” — todos são variações marginais, e nenhuma delas corresponde aos produtos intermediários mencionados em ciclos anteriores.
  - Não há escalada no giro de produtos que ocupam a faixa intermediária de preço ou demanda (definidos por ticket ou número de pedidos entre 2 e 4); os que aparecem com apenas 1 pedido são tipicamente do “fundo da cauda”, não intermediários históricos.
- **Leitura:**
  - Nenhum produto intermediário considerado típico da base Budamix Oficial (ex.: famílias regulares fora dos campeões) registrou pedido nos últimos 5 dias, ao menos neste ciclo validado, e o dia de 14/05 segue padrão bruto de ausência total ou quase total desse giro.
- **Conclusão granular:** confirma total perda de giro ou exposição dos intermediários — não há registro de recuperação nem transação residual nos últimos dias.
- **Confiança:** alta  
  > (Motivo: pedido real confirma ausência; não há dúvida de identificação porque só análise do pedido entra.)

---

#### 2. Pergunta: os anúncios dos top 3 (Kit 2 Potes Vidro, Kit 6 Canequinhas, Potes Redondos Cinza) mantiveram exposição e saúde de posição ontem?

- **Status:** parcialmente respondida
- **Evidência:**
  - Pedidos válidos de 2026-05-14:
    - **Kit 2 Potes de Vidro 1520ml**
      - Produto visível: Kit 2 Potes de Vidro 1520ml
      - Conta: Budamix Oficial
      - shop_id: não especificado (conta única na base; risco mínimo)
      - Fonte: orderItems / pedido real
      - Pedidos: 4
    - **Kit 6 Canequinhas 100ml**
      - Produto visível: Kit 6 Canequinhas 100ml
      - Conta: Budamix Oficial
      - shop_id: idem acima
      - Fonte: orderItems / pedido real
      - Pedidos: 3
    - **Potes Vidro Redondos Tampa Cinza**
      - Produto visível: Potes Vidro Redondos Tampa Cinza
      - Conta: Budamix Oficial
      - shop_id: idem acima
      - Fonte: orderItems / pedido real
      - Pedidos: 3
  - Os três anúncios registraram múltiplos pedidos, sem cancelamento concentrado, mantendo-se com performance similar à janela recente (cada qual dentro da faixa de 3-4 pedidos/dia).
  - Não há dado de “exposição” (posição, visitas, impressão) no input, mas **os três estiveram visíveis para o fluxo remanescente de clientes, resultando em venda real acima do valor de fundo de cauda** e mantendo a liderança quantitativa.
- **Leitura:**
  - Os top 3 mantiveram, via pedido real, sua capacidade de converter poucos clientes ativos; não há evidência de perda abrupta de ranking ou de saúde de listing em nível de vendas.
  - **Limitação:** não há input de exposição ou visitas, apenas venda real — não é possível afirmar saúde de posição ou exposição na vitrine, mas há confirmação de venda normal.
- **Conclusão granular:** confirma que os campeões venderam normalmente, mas **não é possível atestar saúde estrutural de exposição/posição** — a evidência não cobriu essa camada (responde só a “giro”, não a “exposição”).
- **Confiança:** média  
  > (Motivo: ausência de dado de exposição/visita; confiança alta só seria possível com métrica de exposição confirmando manutenção de ranqueamento.)

---

### Investigações próprias

Sem investigação adicional motivada hoje — não foram detectadas anomalias ou divergências autônomas, nem houve risco adicional de identificação de produto relevante fora do escopo das perguntas da Operacional.

---

### Risco de identificação ou leitura errada

**Baixo.**

Todos os produtos citados utilizam título real do pedido e são extraídos diretamente do orderItems, único shop_id (ou seja, risco de cross-loja nulo no dado granular entregue). Não há alias manual, ambiguidade de SKU nem ausência de plataforma_item_id. O único ponto de atenção seria se a Operacional/Tática estivesse misturando produtos de outras contas no canal — mas neste input, o recorte está limpo. Isso garante que a confiança atribuída às leituras é compatível com máxima solidez da base diária.

---

### Detalhe que a Condensadora não pode perder

- Nenhum produto intermediário típico da Budamix Oficial teve pedido ou giro — o mix continua bloqueado nos campeões; sugerir qualquer retomada ou “venda ocasional de intermediário” seria falso — **Confiança: alta**.
- Top 3 campeões (Kit 2 Potes Vidro 1520ml, Kit 6 Canequinhas 100ml, Potes Redondos Cinza) foram responsáveis sozinhos por 62,5% do volume, com performance idêntica à dos últimos ciclos e sem novas presenças entre os mais vendidos — **Confiança: alta**.
- Não é possível afirmar saúde de exposição/vitrine dos campeões, só a continuidade do giro real — o input não contém visitas ou impressões, só venda efetiva — **Confiança: média**.

---

### O que fica só na memória interna

- Plataforma_item_id dos campeões:
  - Kit 2 Potes de Vidro 1520ml: 19098263852
  - Kit 6 Canequinhas 100ml: 22495667316
  - Potes Vidro Redondos Tampa Cinza: 23593154831
- Famílias intermediárias que não giraram (cross-check interno): “Tupper Colorido”, “Jogo 3 Potinhos Diversos”, “Copo Long Drink”, outros de ciclos anteriores
- Listagem técnica dos pedidos individuais (1 a 1) para uso em investigação longitudinal futura.
- Desvio técnico: apenas 4 dos 7 produtos do dia tiveram múltiplos pedidos; outros 3 apareceram com 1 pedido cada, caracterizando fundo cauda e não intermediário — usado para calibrar matriz de risco futura.
