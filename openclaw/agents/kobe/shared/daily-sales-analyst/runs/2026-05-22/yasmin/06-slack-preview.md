<!-- llm_used=true model=gpt-5.5 fallback=false -->
### Mensagem Slack

```text
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.622,03
- Pedidos: 84 pedidos
- Ticket médio: R$ 55,02
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta — 20 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 11 pedidos
- Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha — 10 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza — 7 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 6 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades — 4 pedidos
- Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida — 3 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades — 3 pedidos
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades — 2 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 2 pedidos

🔍 ANÁLISE DA CONTA
- A leitura ainda é limitada, mas o dia parece saudável pelo GMV e pela eficiência de Mercado Ads. A base, porém, ficou frágil: pedidos caíram, o ticket segurou o faturamento e Mercado Ads respondeu por cerca de 69,9% do GMV. Como dois campeões Full seguem com health abaixo de 0,80 e não há ADS por anúncio, a leitura segura é risco de dependência agregada, não prova de que um produto específico está sendo sustentado por mídia.

🎯 PRIORIDADES DO DIA
- Yasmin: não mexer em Mercado Ads hoje; usar o dia como ponto zero da série. Mercado Ads está dominante, mas ainda eficiente, e qualquer ajuste agora confundiria a leitura entre campanha saudável e dependência estrutural. Confirmar/refutar nos próximos 2 ciclos se ADS share segue ≥60% com ROAS alto; se cair abaixo de 60% sem perda de GMV, a hipótese de dependência enfraquece. Escalar se ADS share ficar ≥60% por mais 2 ciclos com os dois campeões Full ainda abaixo de health 0,80.
- Yasmin: checar a direção do health dos dois campeões Full abaixo de 0,80. O pacote confirma health baixo no retrato atual, mas não mostra se está piorando, estável ou recuperando. Confirmar/refutar em 1 a 2 ciclos: health estável ou subindo mantém a leitura em observação; health caindo nos dois reforça risco de perda orgânica compensada por mídia. Escalar se health cair nos dois anúncios por mais 1 a 2 ciclos junto com ADS share ≥60%.
- Yasmin: verificar cobertura ou reposição do Kit 6 Canecas Porcelana Tulipa Lisa 250ml no Full. O anúncio fechou com 9 unidades pós-baixa após 6 pedidos no dia; isso não afeta pedidos passados, mas pode distorcer os próximos ciclos se romper. Confirmar/refutar no próximo ciclo: reposição confirmada ou estoque acima do ritmo recente remove o risco; estoque zerado ou saída do top 10 reforça ruptura prospectiva como confundidor da leitura de volume. Escalar se estoque chegar a 0 ou não houver confirmação de reposição antes do próximo ciclo.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

### Respeito de bloqueios

- **Item bloqueado:** MLB4676751119 — alias interno "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas"
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** conflito de identificação; alias colide com outro anúncio e omite que este item é de 6 unidades
- **Agregado autorizado:** não
- **Tratamento aplicado:** alias bloqueado não usado; título simplificado com quantidade explícita usado no Top Produtos
- **Aparece na mensagem final:** sim, como "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades"

- **Item bloqueado:** MLB4676726433 — alias interno "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas"
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** conflito de identificação; alias colide com o anúncio de 6 unidades e precisa preservar quantidade explícita
- **Agregado autorizado:** não
- **Tratamento aplicado:** alias bloqueado não usado; título simplificado com quantidade explícita usado no Top Produtos
- **Aparece na mensagem final:** sim, como "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades"

- **Item bloqueado:** atribuir receita de Mercado Ads aos campeões com health baixo ou ao campeão Cross-Docking
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** pergunta inconclusiva; não há breakdown de receita ADS por anúncio
- **Agregado autorizado:** sim, "risco de dependência agregada"
- **Tratamento aplicado:** substituído por leitura agregada
- **Aparece na mensagem final:** sim, como "risco de dependência agregada"

- **Item bloqueado:** dizer que houve ruptura ou problema retroativo nos pedidos do Kit 6 Canecas Porcelana Tulipa Lisa 250ml
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** available_quantity é snapshot pós-baixa; risco apenas prospectivo
- **Agregado autorizado:** sim, "risco prospectivo de ruptura"
- **Tratamento aplicado:** mantido como risco prospectivo, sem problema retroativo
- **Aparece na mensagem final:** sim, como "pode distorcer os próximos ciclos se romper"

- **Item bloqueado:** tratar Cross-Docking como problema ou sugerir anomalia de Flex
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Flex zerado e Cross-Docking é modalidade de envio legítima na operação
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitida qualquer leitura de problema em Cross-Docking ou Flex
- **Aparece na mensagem final:** não

### Decisões de formatação

- Metadados internos removidos — `padrao`, `base` e `classificacao` não foram expostos na mensagem Slack.
- Ressalva de baixa confiança preservada — análise abriu com "A leitura ainda é limitada" e manteve linguagem de indício.
- Classificação de risco latente preservada — insight foi escrito como risco de dependência agregada, não como certeza.
- Atribuição de ADS a produtos específicos bloqueada — mantida apenas a leitura agregada autorizada.
- Insight limitado a 1 item — alerta global de confiança baixa impede multiplicar leituras confiantes.
- Prioridades mantidas em 3 itens — ações vieram da Condensadora e são checagens seguras, sem criação de ação nova.
- Yasmin atribuída como responsável — responsável fixo da conta Mercado Livre nas prioridades.
- Modalidade de envio omitida da VISÃO MERCADO LIVRE — dado do mix do dia cobre apenas top 10 e não representa a totalidade objetiva da conta.
- Top Produtos sem faturamento por item — pacote validado trouxe pedidos por produto, não receita validada por produto.
- Top Produtos no nível de variação — atributos confirmados por SKU foram incluídos quando disponíveis.
- "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" recebeu "Tampa Preta" — atributo confirmado por SKU preservado.
- "Jogo Potes de Vidro 5 Peças Claro" recebeu "Tampa Vermelha" — atributo confirmado por SKU preservado.
- "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" recebeu "Tampa Cinza" — atributo confirmado por SKU preservado.
- Kits YW1050 diferenciados por quantidade — bloqueio de alias colidido respeitado usando nomes com "10 Unidades" e "6 Unidades".
- Divergência de denominação cross-layer: L05 usou "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"; L06 manteve o mesmo nome — sem divergência.
- Divergência de denominação cross-layer: L05 usou leitura genérica "dois campeões Full"; L06 manteve sem nomes na análise — evita atribuição indevida de ADS por produto.
- Quebras de frase aplicadas na análise — frase longa da Condensadora foi separada para clareza sem alterar tese.
- Ruptura das canecas tratada como prospectiva — preservada a lógica pós-baixa e removida qualquer leitura retroativa.