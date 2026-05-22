<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 21/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 6.082,82
- Pedidos: 100 pedidos
- Ticket médio: R$ 60,83
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 5 Potes de Vidro Redondos — Tampa Preta — 31 pedidos
- Kit 10 Potes Herméticos 1050ml 4 Travas — 16 pedidos
- Kit 5 Potes de Vidro Redondos — Tampa Cinza — 13 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml 4 Travas — 8 pedidos
- Kit 5 Potes de Vidro Redondos — Tampa Vermelha — 8 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 6 Canequinhas 100ml — Suporte de Madeira Acrílico — 3 pedidos
- Kit 10 Potes Herméticos 520ml 4 Travas — 2 pedidos
- Kit 10 Potes Herméticos 1050ml 4 Travas — 6 Unidades — 2 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml 4 Travas — 2 pedidos

🔍 ANÁLISE DA CONTA
- O GMV esconde dois anúncios Full em situações diferentes de ruptura. O Kit 6 Canequinhas 100ml já estourou — 3 pedidos aceitos com apenas 2 unidades no CD do ML; cada pedido sem cobertura vira cancelamento ML que bate na reputação antes de aparecer no indicador oficial. O Kit 6 Canecas Porcelana 250ml tem ~3-4 dias de cobertura em fulfillment (19 unidades, 5 pedidos/dia), mas repor em fulfillment exige envio ao CD — a janela para agir preventivamente é hoje, não amanhã.
- O GMV de R$ 6.082,82 é o melhor dos últimos dois meses (+38% vs 30d, +57% vs 60d), mas 75,5% veio de campanhas ADS. Como é a primeira leitura com esse dado calculável — sem histórico semanal ou mensal acumulado — não dá para saber quanto o orgânico sustentaria sozinho. Os parâmetros de hoje são ponto zero da série, não confirmação de tendência consolidada.
- O fulfillment do dia ficou 80% cross-docking contra 77% Full na média dos últimos 7 dias — parece uma virada, mas é composição: a família IMB501 (três variações, 52 pedidos combinados, todos cross-docking) dominou o topo. Quando esse grupo lidera, o fulfillment do dia segue o mix do topo, não muda a configuração da conta.

🎯 PRIORIDADES DO DIA
- Yasmin: consultar o painel ML para identificar quais pedidos do Kit 6 Canequinhas 100ml ainda estão em estado pré-envio e permitem cancelamento controlado. Ruptura já consumada — 3 pedidos aceitos com 2 unidades no CD; cada pedido sem cobertura vira cancelamento ML que impacta a reputação. Confirmar/refutar: reposição confirmada em menos de 24h neutraliza o risco; se cancelamentos subirem acima de 5/dia nos próximos 2 ciclos, o impacto já vazou para a reputação antes do indicador oficial atualizar. Escalar se: cancelamentos ML-originados já registrados sem reversão possível — acionar ressuprimento Full imediatamente ou executar cancelamento controlado antes que a janela feche.
- Yasmin: verificar hoje o andamento de reposição do Kit 6 Canecas Porcelana 250ml em fulfillment. 19 unidades disponíveis, 5 pedidos/dia, ~3-4 dias de cobertura — mas fulfillment exige envio ao CD do ML, então a janela real é mais curta do que os dias sugerem. Confirmar/refutar: se ritmo cair para 2 pedidos/dia ou menos nos próximos 2 dias, urgência reduz; se mantiver 5 pedidos/dia ou mais sem confirmação de reposição em trânsito, urgência passa a crítica. Escalar se: reposição não confirmada em trânsito para o CD em menos de 24h com ritmo de vendas mantido.
- Yasmin: registrar os parâmetros de ADS de hoje como ponto zero da série — share 75,5%, ticket R$ 60,83, ACOS 4,71%, spend R$ 341,72 — e não acionar ajuste nas campanhas neste ciclo. Eficiência atual é excepcional e, sem histórico acumulado, qualquer mudança impede isolar o comportamento orgânico da conta nos próximos dias. Confirmar/refutar: ADS share acima de 70% por 3 dos próximos 5 dias confirma dependência estrutural; ticket abaixo de R$ 50,00 com spend similar (~R$ 341) indica que o ticket atual é ADS-induzido. Escalar se: ADS share acima de 70% por 3 dias consecutivos — abrir discussão sobre dependência estrutural de mídia paga com Kobe.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Estado individual dos pedidos abertos do Kit 6 Canequinhas 100ml (order_ids e status por pedido)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Dado não disponível no schema ml-snapshot/v1; L04 confirmou não ser derivável do pacote
- **Agregado autorizado:** não
- **Tratamento aplicado:** ruptura tratada como fato consumado sem granularidade de order_id; mensagem orienta Yasmin a consultar o painel ML diretamente
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Causa e direção do health=0,75 no Kit 4 Potes 1050ml (estabilizando, caindo ou recuperando)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Pacote retorna apenas valor pontual sem série temporal nem breakdown por dimensão; L02 definiu observação por 2-3 dias antes de ação
- **Agregado autorizado:** não
- **Tratamento aplicado:** health e Kit 4 Potes omitidos da mensagem; nenhuma afirmação de direção ou causa do indicador; produto aparece normalmente no ranking de TOP PRODUTOS sem menção ao health
- **Aparece na mensagem final:** não (health); sim (produto no ranking, apenas com pedidos)

---

- **Item bloqueado:** Afirmação de que as campanhas de Himmel priorizaram ativamente produtos cross-docking, explicando o fulfillment mix invertido do dia
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Hipótese em aberto — ads_summary sem breakdown por platform_item_id; correlação observacional, não evidência confirmada
- **Agregado autorizado:** não
- **Tratamento aplicado:** insight 3 cita composição de produto como causa da inversão de fulfillment, sem nenhuma menção a causalidade ADS→fulfillment
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** health=null como indicador de saúde nos demais anúncios do top 10
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** health=null indica volume insuficiente para cálculo ML, não que o anúncio está saudável; distinção ativa registrada pela L04
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum anúncio citado como "saudável" por ausência de health em qualquer parte da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** display_name de KIT6YW1050 ("Kit 10 Potes Herméticos 1050ml Refratário 4 Travas") como referência ao produto
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** display_name de KIT6YW1050 é idêntico ao de KIT10YW1050, omitindo o diferencial crítico de quantidade ("6 Unidades"); risco de confusão interna entre os dois produtos
- **Agregado autorizado:** não aplicável — divergência resolvida pela fonte primária
- **Tratamento aplicado:** título ML real usado: "Kit 10 Potes Herméticos 1050ml 4 Travas — 6 Unidades" (atributo "6 Unidades" preservado do title ML como diferenciador obrigatório)
- **Aparece na mensagem final:** sim, como "Kit 10 Potes Herméticos 1050ml 4 Travas — 6 Unidades" (correto, via title ML)

---

- **Item bloqueado:** MLBs (platform_item_ids) no corpo da mensagem
- **Origem do bloqueio:** L05 Condensadora (regra ML explícita)
- **Motivo:** platform_item_ids não devem aparecer na análise condensada, prioridades nem em nenhuma seção da mensagem Slack
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum MLB citado; todos os produtos referenciados pelo nome comercial derivado do title ML
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) removidos de todos os insights — campos de controle de pipeline, não conteúdo para Slack.
- Insight 1 (classificação: fato) — linguagem direta e sem hedge usada: "já estourou", "a janela é hoje"; tom de urgência da Condensadora preservado integralmente.
- Insight 2 (classificação: risco latente) — linguagem de indício preservada: "não dá para saber", "ponto zero da série, não confirmação de tendência consolidada"; transformação em fato proibida e não aplicada.
- Insight 3 (classificação: fato) — nuance "parece uma virada, mas é composição" preservada sem suavização.
- Fulfillment omitido da seção VISÃO MERCADO LIVRE — `fulfillment_mix_yesterday_top10` cobre apenas os top 10 itens (90 de 100 pedidos); a Condensadora não autorizou exibição com ressalva de cobertura parcial nesta seção; fulfillment tratado exclusivamente no Insight 3 da ANÁLISE, onde a L05 o incluiu explicitamente.
- Faturamento por produto omitido em TOP PRODUTOS — pacote não entrega receita validada por variação; proibido calcular ou estimar via ticket médio × pedidos.
- Simplificação de títulos ML em TOP PRODUTOS (item a item):
  - IMB501P: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto" + `confirmed_variation_attributes` ["Tampa Preta"] → "Kit 5 Potes de Vidro Redondos — Tampa Preta" (tipo + quantidade + atributo confirmado por SKU; palavras-chave SEO removidas)
  - KIT10YW1050: "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" → "Kit 10 Potes Herméticos 1050ml 4 Travas" (marca e "Refratário" removidos; "10 Unidades" omitido por redundância com "Kit 10"; nenhum `confirmed_variation_attributes`)
  - IMB501C: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Cinza" + ["Tampa Cinza"] → "Kit 5 Potes de Vidro Redondos — Tampa Cinza"
  - KIT4YW1050: "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 4 Potes de Vidro Hermético 1050ml 4 Travas" (cor Azul-petróleo removida — ausente em `confirmed_variation_attributes`; proibido adicionar atributo não confirmado)
  - IMB501V: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Vermelho" + ["Tampa Vermelha"] → "Kit 5 Potes de Vidro Redondos — Tampa Vermelha"
  - TL6250: "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" → "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" ("Coloridas Xícara" removido como adjetivo genérico/SEO)
  - 914C_BAV: "Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico" → "Kit 6 Canequinhas 100ml — Suporte de Madeira Acrílico" ("06" normalizado para "6"; separador adicionado para leitura)
  - KIT10YW520: "Kit 10 Potes Herméticos 520ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" → "Kit 10 Potes Herméticos 520ml 4 Travas" (mesmo critério de KIT10YW1050)
  - KIT6YW1050: "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 6 Unidades" → "Kit 10 Potes Herméticos 1050ml 4 Travas — 6 Unidades" ("6 Unidades" preservado do title ML como diferenciador obrigatório vs KIT10YW1050; display_name não usado conforme bloqueio registrado acima)
  - KIT2YW1050: "Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 2 Potes de Vidro Hermético 1050ml 4 Travas" (mesmo critério de KIT4YW1050)
- Atributos de variação (cor de tampa) incluídos apenas para IMB501P, IMB501C e IMB501V, onde `confirmed_variation_attributes` confirma o atributo. Nenhum atributo de cor adicionado aos demais produtos onde o campo está vazio.
- Divergência display_name vs title ML para KIT6YW1050 resolvida na mensagem usando title ML; divergência não citada no Slack conforme regra (registrada apenas neste bloco de log).
- Kit 4 Potes (health=0,75) listado normalmente em TOP PRODUTOS sem menção ao health — penalização ativa não bloqueia citação no ranking; bloqueio se aplica à análise de causa/direção, não à presença do produto.
- Alertas de confiança (nível: médio) — nível não reduziu a quantidade de insights nem exigiu ressalva global; os três gaps granulares (order_ids Canequinhas, causa/direção health, breakdown ADS) foram tratados individualmente nos bloqueios; ação sobre o Canequinhas é clara mesmo sem granularidade de order_id, conforme indicação da L05.
- Referências internas a camadas do pipeline removidas de todos os trechos e substituídas por linguagem operacional direta.
- Yasmin atribuída como responsável em todas as prioridades — responsável fixo para Mercado Livre.
- Nenhum MLB visível na mensagem final.