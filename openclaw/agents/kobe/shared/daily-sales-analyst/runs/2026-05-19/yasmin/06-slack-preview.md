<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 19/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.790,64
- Pedidos: 107 pedidos
- Ticket médio: R$ 54,12
- Cancelamentos: 6

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 32 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 10 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 9 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 8 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 7 pedidos

🔍 ANÁLISE DA CONTA
- O dia pode parecer fraco em pedidos, mas o resultado foi positivo: com pedidos ligeiramente abaixo da média de 7 dias e GMV acima, a conta converteu menos unidades e mais valor por pedido. Isso não é deterioração — o mix está mudando para produtos mais caros, e essa tendência aparece nas bandas de 30 e 60 dias também, não é composição acidental de um único dia.
- A dependência nos potes de vidro redondos é mais concentrada do que aparece no ranking: Tampa Preta e Tampa Vermelha dividem o mesmo anúncio no ML — juntas respondem por cerca de 39% dos pedidos em um único ponto de controle. Se esse anúncio perder ranking, elegibilidade ou tiver problema de estoque em qualquer variação, os dois produtos caem ao mesmo tempo. A conta está saudável no GMV, mas opera sobre base mais estreita do que os números sugerem.
- As três checagens mais críticas para avaliar o risco operacional — cancelamentos por produto, estoque do produto líder e status do ML Full nos anúncios principais — não estão no dado automatizado e precisam de acesso manual ao painel. Enquanto essas verificações não são feitas, os pontos de fragilidade mais relevantes da conta permanecem sem resposta.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar no painel ML a posição e o status do anúncio principal dos potes de vidro redondos — checar ranking, elegibilidade e estoque para as variações Tampa Preta e Tampa Vermelha. Esse único anúncio respondeu por cerca de 39% dos pedidos do dia. Confirmar/refutar por: posição estável e estoque confortável → mantém observação sem ação; posição caída ou estoque baixo → alinhar com Himmel sobre ADS ML e verificar cobertura para os próximos dias. Escalar se: posição caída em 2 ou mais variações hoje e persistindo amanhã, ou estoque com menos de 7 dias de cobertura no produto líder.
- Yasmin: registrar os 6 cancelamentos do dia — em qual produto ou anúncio ocorreram e em qual horário, mesmo que seja entrada manual. Se os cancelamentos estiverem concentrados no anúncio dos potes de vidro redondos, o risco operacional sobe de nível.

Dia analisado: 19/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: IDs técnicos de anúncio (MLB3288536143, MLB4535865311, demais MLBs)
- Origem do bloqueio: Condensadora
- Motivo: boas práticas de identificação — IDs técnicos não são operacionalmente interpretáveis por Yasmin
- Agregado autorizado: sim, `"anúncio principal dos potes de vidro redondos"` / `"anúncio dos potes de vidro redondos"`
- Tratamento aplicado: substituído pelo agregado autorizado em análise e prioridades
- Aparece na mensagem final: sim, como agregado `"anúncio principal dos potes de vidro redondos"`

---

- Item bloqueado: Raw SKUs (IMB501P_T, IMB501V_T, IMB501CT, KITIMB501P_T e variantes)
- Origem do bloqueio: Condensadora
- Motivo: boas práticas de identificação — raw SKUs não são legíveis para o destinatário
- Agregado autorizado: sim, nomes de exibição ou agregado de família
- Tratamento aplicado: substituído pelos display_names (`Conjunto 5 Potes de Vidro Redondos Tampa Preta`, `Tampa Vermelha`, `Tampa Cinza`)
- Aparece na mensagem final: sim, como display_names de variação

---

- Item bloqueado: Divergência de material no TL6250 (raw_title "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" vs display_name "Kit 6 Tigelas de Vidro 250ml")
- Origem do bloqueio: Condensadora
- Motivo: questão interna de catálogo, não operacional para Yasmin hoje
- Agregado autorizado: não aplicável — produto não citado na análise; aparece apenas em Top Produtos com display_name padrão fora do top 5
- Tratamento aplicado: omitido da análise; produto não entrou no top 5 do ranking e não foi citado nominalmente na análise
- Aparece na mensagem final: não

---

- Item bloqueado: Quatro produtos com mapeamento de confiança média (KIT10YW1050, 914C_BAV, SPC0111, KIT4YW640) citados como fonte de análise
- Origem do bloqueio: Condensadora
- Motivo: mapped_generic_sku com confiança média — não devem ser fonte nominal de análise
- Agregado autorizado: sim, `"demais produtos"` / `"fora da família principal"` para análise
- Tratamento aplicado: nenhum citado como base analítica; KIT10YW1050 aparece em Top Produtos com display_name (3º posição por pedidos reais, sem bloqueio formal de Top Produtos); os demais ficaram fora do top 5
- Aparece na mensagem final: KIT10YW1050 aparece em Top Produtos (posição 3, pedidos reais validados, platform_item_id confirmado); os demais não aparecem

---

- Item bloqueado: Detalhe de weekly e monthly vazios
- Origem do bloqueio: Condensadora
- Motivo: informação interna do pipeline, não operacional para Yasmin
- Agregado autorizado: não aplicável
- Tratamento aplicado: omitido integralmente da mensagem
- Aparece na mensagem final: não

---

- Item bloqueado: Divergência de leitura do campo `other` no bloco de fulfillment entre camadas
- Origem do bloqueio: Condensadora
- Motivo: questão interna resolvida, conclusão funcional idêntica
- Agregado autorizado: não aplicável
- Tratamento aplicado: omitido integralmente da mensagem
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional`, `— base: Granular`, `— base: Granular + Tática`, padrão de classe `C`, `E`, `B`) — não são legíveis por Yasmin e foram explicitamente proibidos pelo prompt
- Preservação das três teses da Condensadora na íntegra, incluindo o `mas` contrastivo no insight 1 e a distinção "um único ponto de controle" no insight 2 — conectivos e nuances mantidos sem substituição
- Quebra leve no insight 3 para fluir melhor em Slack, sem alterar tese ou termos analíticos
- Substituição de "as variações Tampa Preta e Tampa Vermelha dividem o mesmo anúncio-pai" por formulação equivalente sem terminologia técnica interna ("dividem o mesmo anúncio no ML") — mantém sentido operacional
- Top Produtos limitado ao top 5 por pedidos — corte natural na posição 5 (7 pedidos), com 4 produtos de alta confiança e 1 de confiança média (KIT10YW1050, posição 3, sem bloqueio formal); TL6250 ficou fora do top 5 e a divergência de material não aparece na mensagem
- KIT10YW1050 incluído em Top Produtos como dado objetivo (pedidos reais, platform_item_id confirmado, sem bloqueio formal da Condensadora); não citado como fonte de análise
- Faturamento por produto omitido em todos os itens do top — o pacote não traz receita validada por produto/variação; formato padrão `[nome] — [pedidos] pedidos` aplicado
- Prioridades formatadas com ação + motivação + sinal de confirmação/refutação + condição de escalonamento, preservando a estrutura completa da Condensadora
- Seção ML Full omitida da VISÃO MERCADO LIVRE — pacote não discrimina ML Full no schema; ausência estrutural registrada pela Granular; não inferir nem mencionar como dado disponível
- Cancelamentos incluídos na VISÃO como dado objetivo (6 cancelamentos) sem classificação analítica — confiança baixa por ausência de série histórica preservada