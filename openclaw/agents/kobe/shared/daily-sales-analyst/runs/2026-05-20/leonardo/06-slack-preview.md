<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 20/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 1.663,37
- Pedidos: 40 pedidos
- Ticket médio: R$ 41,58
- Cancelamentos: 3
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Jarra Medidora de Vidro 500ml — 15 pedidos
- Suporte Controle Gamer — 5 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml Preto — 3 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 3 pedidos
- Kit 2 Potes de Vidro 320ml Retangular — 2 pedidos
- Kit 6 Canequinhas 100ml — 2 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml Branco — 2 pedidos
- Kit 6 Xícaras Porcelana Paris 170ml (Colorido) — 1 pedido
- Kit 6 Xícaras Porcelana Paris 170ml (Rosa) — 1 pedido
- Kit 3 Potes de Vidro Herméticos Tampa Bambu — 1 pedido

🔍 ANÁLISE DA CONTA
- O dia performou dentro da nova banda elevada — as três janelas de histórico (60d, 30d, 7d) estão alinhadas em crescimento, confirmando ganho de patamar real. Mas o volume está rodando sobre uma operação opaca: sem Buy Box e FBA do ASIN líder disponíveis, não é possível dizer se a posição que gerou esses 40 pedidos é sustentável ou é uma janela de exposição sem garantia. O número parece bom; a estrutura que o gerou é desconhecida.
- A execução do dia dependeu de um único produto: Jarra Medidora de Vidro 500ml com 37,5% dos pedidos e top 5 em 70% do total. A cauda de 10 SKUs existe, mas nenhum item além do líder passou de 5 pedidos. Com 100% FBA e sem dado de saúde do líder, qualquer instabilidade nesse produto cai direto no GMV da conta sem amortecedor.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box e cobertura de estoque FBA da Jarra Medidora de Vidro 500ml (B0G2CWWMGK) no Seller Central. Com 37,5% dos pedidos concentrados nesse produto em estrutura 100% FBA, é o pré-requisito que valida — ou invalida — o patamar atual. Buy Box ≥85% com FBA sem alerta de ruptura abre caminho para avaliar ADS com Pedro; abaixo disso, pausar qualquer expansão e escalar para Pedro com diagnóstico fechado.
- Leonardo: verificar se os 3 cancelamentos estão concentrados na Jarra Medidora ou distribuídos entre os demais produtos. Cancelamentos distribuídos = ruído aceitável para inaugurar baseline. Concentrados no líder = escalar para Pedro com dados do Seller Central.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: TL250P — display_name "Tigela de Vidro 250ml"
- Origem do bloqueio: Granular / Condensadora
- Motivo: display_name incorreto; produto real do pedido é Kit 6 Canecas de Porcelana Tulipa 250ml Preto (ASIN B0GGTY2BLT)
- Agregado autorizado: sim, "Kit 6 Canecas de Porcelana Tulipa 250ml Preto"
- Tratamento aplicado: substituído pelo nome correto derivado do raw_title, conforme regra Amazon de prioridade ao título real do pedido
- Aparece na mensagem final: sim, como "Kit 6 Canecas de Porcelana Tulipa 250ml Preto"

---

- Item bloqueado: TL250B — display_name "Tigela de Vidro 250ml"
- Origem do bloqueio: Granular / Condensadora
- Motivo: display_name incorreto; produto real do pedido é Kit 6 Canecas de Porcelana Tulipa 250ml Branco (ASIN B0GGTTMD4H)
- Agregado autorizado: sim, "Kit 6 Canecas de Porcelana Tulipa 250ml Branco"
- Tratamento aplicado: substituído pelo nome correto derivado do raw_title, conforme regra Amazon de prioridade ao título real do pedido
- Aparece na mensagem final: sim, como "Kit 6 Canecas de Porcelana Tulipa 250ml Branco"

---

- Item bloqueado: Status de Buy Box e FBA do CK4742
- Origem do bloqueio: Granular / Condensadora
- Motivo: dado não disponível no pacote; inconclusivo
- Agregado autorizado: não
- Tratamento aplicado: não afirmado como saudável nem como frágil; referenciado apenas como dado ausente que precisa ser verificado por Leonardo
- Aparece na mensagem final: não como dado; sim como checagem obrigatória nas prioridades

---

- Item bloqueado: Distribuição dos cancelamentos por ASIN
- Origem do bloqueio: Granular / Condensadora
- Motivo: dado não disponível no pacote; inconclusivo
- Agregado autorizado: não
- Tratamento aplicado: não classificado como normal ou elevado; encaminhado como checagem para Leonardo
- Aparece na mensagem final: não como dado; sim como checagem nas prioridades

---

- Item bloqueado: Recorrência do pico de 22h
- Origem do bloqueio: Granular / Condensadora
- Motivo: sem histórico horário comparativo; inconclusivo
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem final
- Aparece na mensagem final: não

---

- Item bloqueado: SKU "028" e XCP003 com confiança média
- Origem do bloqueio: Condensadora
- Motivo: mapeamento via fallback; confiança média; risco de ambiguidade
- Agregado autorizado: sim — "Kit 3 Potes de Vidro Herméticos Tampa Bambu" para 028 e "Kit 6 Xícaras Porcelana Paris 170ml (Rosa)" para XCP003 via raw_title
- Tratamento aplicado: citados pelo raw_title sem SKU cru visível; ASIN omitido por título suficientemente identificável (decisão registrada abaixo)
- Aparece na mensagem final: sim, via raw_title sem SKU

---

### Decisões de formatação

- Remoção de metadados internos (referências a camadas: Estratégica, Tática, Granular, Condensadora) — metadados de pipeline não vão para Slack conforme regra
- TL250P e TL250B: substituídos por "Kit 6 Canecas de Porcelana Tulipa 250ml Preto" e "Kit 6 Canecas de Porcelana Tulipa 250ml Branco" via raw_title — bloqueio da Granular/Condensadora; display_name "Tigela de Vidro 250ml" incorreto conforme evidência de confiança alta
- XCP003: citado como "Kit 6 Xícaras Porcelana Paris 170ml (Rosa)" via raw_title sem ASIN — título suficientemente identificável para distinção do XCP002 (Colorido vs. Rosa); ASIN omitido e decisão registrada aqui
- 028: citado como "Kit 3 Potes de Vidro Herméticos Tampa Bambu" via raw_title sem SKU cru — SKU "028" genérico não exposto conforme bloqueio da Condensadora
- ASIN de CK4742 (B0G2CWWMGK) incluído apenas na seção de prioridades como referência para Leonardo checar no Seller Central — não incluído no Top Produtos porque o título "Jarra Medidora de Vidro 500ml" é suficientemente identificável; incluído nas prioridades para facilitar a ação operacional direta
- Confiança média global preservada: nenhum dos dois insights foi transformado em certeza; estrutura opaca e risco de dependência mantidos como hipótese de sustentação, não como fato confirmado
- Prioridade de pico de 22h omitida — inconclusivo por falta de histórico comparativo; não encaminhada como ação para Leonardo
- Quebra de frase longa no segundo insight da análise: frase original da Condensadora preservada integralmente sem mudança de tese ou conectivo
- Top Produtos em ordem decrescente por pedidos: 15, 5, 3, 3, 2, 2, 2, 1, 1, 1 — ordem respeitada conforme pacote validado
- TL250P (3 pedidos) e TL250B (2 pedidos) mantidos em posições separadas no ranking — variações distintas (Preto e Branco) com volumes próprios; não consolidados por serem variações vendáveis diferentes