### Respostas granulares às perguntas da Operacional

---

#### 1. Houve algum micro movimento de vendas (mesmo pedido isolado ou sacola) nos produtos da cauda longa fora do top 3?

- **Pergunta:** houve algum micro movimento de vendas (mesmo pedido isolado ou sacola) nos produtos da cauda longa fora do top 3?
- **Status:** respondida
- **Evidência:**  
  Dos 35 pedidos válidos, 32 estão concentrados nos três produtos líderes abaixo:
  - Produto visível: Jarra Medidora de Vidro 500ml  
    - Conta: Budamix Store  
    - shop_id: não destacado individualmente (mas único em pacote)  
    - platform_item_id: 23993264258  
    - quant.: 17  
    - Fonte: orderItems / pedido real
  - Produto visível: Potes Vidro Redondos Tampa Preta  
    - Conta: Budamix Store  
    - shop_id: idem  
    - platform_item_id: 22393168887  
    - quant.: 13  
    - Fonte: orderItems / pedido real
  - Produto visível: Kit 2 Potes de Vidro 800ml Quadrado  
    - Conta: Budamix Store  
    - shop_id: idem  
    - platform_item_id: 22593169868  
    - quant.: 2  
    - Fonte: orderItems / pedido real

  Fora do top 3, apenas 3 pedidos únicos:
  - Produto visível: Kit 5 Potes de Vidro Hermetico com Tampa Marmita Alimentos Freezer Micro-ondas  
    - platform_item_id: 49056997127  
    - quant.: 1  
    - Fonte: orderItems / pedido real
  - Produto visível: Kit 6 Canequinhas 100ml  
    - platform_item_id: 23036701291  
    - quant.: 1  
    - Fonte: orderItems / pedido real
  - Produto visível: Kit 6 Canecas Tulipa 250ml  
    - platform_item_id: 45554989236  
    - quant.: 1  
    - Fonte: orderItems / pedido real

- **Leitura:**  
  A cauda longa vendeu 3 unidades distribuídas, cada uma em produto diferente, sem repetição nem indício de tração (1 pedido isolado para cada variação). Não houve pacotes/sacolas multivariate nem sinal de sacola combinada entre cauda e líderes.
- **Conclusão granular:**  
  Confirma ausência de tração/viabilidade de expansão de mix no dia — cauda apenas subsiste via venda pontual e isolada, sem padrão nem repetição.
- **Confiança:**  
  Alta (fonte: orderItems real, base robusta para o tamanho do canal no dia, sem risco relevante de identificação).

---

#### 2. Algum dos top 3 apresentou sinal de oscilação de estoque, preço ou tempo de entrega nas últimas 24h?

- **Pergunta:** algum dos top 3 apresentou sinal de oscilação de estoque, preço ou tempo de entrega nas últimas 24h?
- **Status:** não respondida por falta de dado
- **Evidência:**  
  O pacote não inclui dados de estoque, logs de alteração de preço, nem registro de SLAs/tempo de entrega sinalizado no detalhe granular do dia.
- **Leitura:**  
  Não é possível afirmar, com base apenas nos pedidos válidos e na métrica agregada do dia, se houve ou não qualquer alteração operacional nos parâmetros de estoque, preço ou lead-time percebidos na plataforma.
- **Conclusão granular:**  
  Inconclusivo por ausência de evidência granular sobre estoque/preço/entrega.
- **Confiança:**  
  Não aplicável (ausência da evidência primária necessária).

---

#### 3. Identificou-se alteração na exposição dos produtos fora do top 3 na vitrine ou busca orgânica Shopee?

- **Pergunta:** identificou-se alteração na exposição dos produtos fora do top 3 na vitrine ou busca orgânica Shopee?
- **Status:** não respondida por falta de dado
- **Evidência:**  
  O pacote não contém métricas de exposição/vitrine, posição em busca, logs de visualizações ou dados similares para os produtos da cauda. Só há registro de vendas efetivamente realizadas.
- **Leitura:**  
  Não há elemento granular que permita aferir qualquer alteração de exposição orgânica ou de vitrine; permanece desconhecido se o não-venda da cauda resulta apenas de falta de demanda ou também baixa exposição.
- **Conclusão granular:**  
  Inconclusivo por ausência de dado diretamente sobre exposição.
- **Confiança:**  
  Não aplicável (falta de evidência necessária).

---

### Investigações próprias

Sem investigação adicional motivada hoje. Não há anomalia, divergência entre fontes ou sinal de risco de identificação além das perguntas obrigatórias.

---

### Risco de identificação ou leitura errada

**Baixo.**  
Todos os produtos citados têm identificação direta e exclusiva por título real do pedido + platform_item_id (Shopee), sem ambiguidades entre SKUs, sem uso de alias manual, sem duplicidade de shop_id (única conta da Budamix Store), e sem ausência de atributos primários no pacote. Não há microamostras interpretadas como padrão, nem dado agregado demais.  
Nenhum item entra em **BLOQUEIO PARA SLACK**.

---

### Divergência entre fontes

Nenhuma divergência detectada entre pedidos reais (orderItems) e agregados do top 3/concentração. As contagens e o ranking de produtos coincidem integralmente.

---

### Detalhe que a Condensadora não pode perder

- Fora do top 3, cada produto da cauda vendeu exatamente 1 unidade — isso reforça o diagnóstico de inexistência total de tração fora dos campeões; se omitido, sugeriria indevidamente alguma “diversidade” no mix — Confiança: alta.
- Todos os pedidos foram processados sem cancelamentos ou anomalia operacional, mas a “estabilidade” do dia é artificial: só existiu porque os campeões sustentaram absolutamente tudo — Confiança: alta.
- A confiança em cada identificação de produto está em nível máximo, pois toda citação nominal usada como base advém exclusivamente dos pedidos reais, sem alias manual nem risco de leitura por dado ambíguo — Confiança: alta.

---

### O que fica só na memória interna

- Lista dos platform_item_id dos produtos de cauda para rastreio técnico: 49056997127, 23036701291, 45554989236.
- Não foram identificadas divergências técnicas que exijam log para revisão futura.
- Pedidos de investigação sobre oscilação de estoque/preço/tempo de entrega e exposição permanecem abertos para próxima janela, caso dados surjam (podem ser solicitados em rotina futura).
