<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 21/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 6.113,02
- Pedidos: 101 pedidos
- Ticket médio: R$ 60,52
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 5 Potes de Vidro Redondos — Tampa Preta — 31 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 16 pedidos
- Kit 5 Potes de Vidro Redondos — Tampa Cinza — 13 pedidos
- Kit 5 Potes de Vidro Redondos — Tampa Vermelha — 9 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml 4 Travas — 8 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos
- Kit 10 Potes Herméticos 520ml Refratário 4 Travas — 2 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas (6 unidades) — 2 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml 4 Travas — 2 pedidos

🔍 ANÁLISE DA CONTA
- O Kit 06 Canequinhas Acrílico está ativo com apenas 1 unidade em estoque e gerou 3 pedidos ontem — cada novo pedido a partir de agora é cancelamento prospectivo garantido. A cancellations_rate hoje está zerada e é indicador crítico para manter o MercadoLíder Gold; qualquer cancelamento aqui começa a contaminar essa janela.
- O mix de modalidade de envio do dia inverteu — 80% Cross-Docking contra o padrão de 74% Full nos últimos 30 dias — mas isso não é mudança de perfil da conta: é a família de Potes de Vidro Redondos Kit 5 Peças dominando o dia inteiro via Cross-Docking. O Cross-Docking está funcionando normalmente; a inversão some quando esses produtos não liderarem.
- O GMV de R$ 6.113,02 veio do ticket (R$ 60,52, +48% vs. média de 60 dias), não de alcance — os pedidos ficaram alinhados ao padrão histórico de quintas. O resultado foi construído com 75% do GMV via Mercado Ads (ROAS 13x, ACOS 4,7%), mas esta é a inauguração da série: sem histórico acumulado, o patamar só se confirma com mais dias de observação — por ora é ganho real nos números e hipótese estrutural em aberto.

🎯 PRIORIDADES DO DIA
- Yasmin: checar o Kit 06 Canequinhas Acrílico (1 unidade em estoque, anúncio ativo em Full) e decidir entre pausar de forma controlada ou confirmar reposição em até 24h. Por quê: cada pedido adicional é cancelamento prospectivo com impacto direto na cancellations_rate, hoje zerada — indicador crítico para manutenção do MercadoLíder Gold e trajetória para Platinum. Confirmar se anúncio foi pausado antes de novo pedido nos próximos 2 dias; reputação protegida se ação for anterior ao próximo pedido. Escalar se: novo cancelamento gerado antes da ação — monitorar cancellations_rate nas próximas 48h e registrar no daily seguinte.
- Yasmin: checar prazo de reposição do Kit 6 Canecas Porcelana Tulipa Lisa 250ml (14 unidades em estoque, modalidade Full, ritmo ~5 pedidos/dia) — runway estimado de ~3 dias, com lead time maior por estar no CD do ML. Por quê: ruptura em Full leva mais tempo para recuperar posição do que em Cross-Docking; o anúncio tem associação a uma entidade de Catálogo ML, então ruptura aqui pode ter impacto adicional em ranking de categoria. Confirmar/refutar por: reposição com ETA igual ou menor a 3 dias neutraliza o risco; ausência de confirmação logística em 24h aciona alerta de ruptura iminente para o próximo daily. Escalar se: sem confirmação de reposição em 24h.
- Yasmin: registrar ticket médio de R$ 60,52 e ADS share de 75,1% como ponto zero da série de observação. Monitorar a direção do health do Kit 4 Potes de Vidro Hermético 1050ml (health=0,75 hoje, único campeão do dia com penalização ativa) nos próximos 2 dias. Por quê: sem histórico qualitativo acumulado, esses são os primeiros pontos de referência para confirmar se o patamar de GMV é estrutural ou amplificação de ADS; a direção do health define se a penalização de exposição orgânica é estabilizada ou progressiva. Confirmar por: ticket acima de R$ 55,00 por 2 dias consecutivos + health estável no Kit 4 Potes = tese de patamar em confirmação. Escalar se: health do Kit 4 Potes cair abaixo de 0,70 ou ticket médio abaixo de R$ 48,00 por 2 dias consecutivos.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Breakdown de cancelamentos por anúncio (concentrado ou pulverizado)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Dado ausente do pacote — metrics.cancelamentos é total agregado sem breakdown por platform_item_id, order_id ou motivo; inconclusivo pela L04
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — cancelamentos aparecem na VISÃO apenas como total (3), sem atribuição por produto
- **Aparece na mensagem final:** não (exceto total agregado na VISÃO)

---

- **Item bloqueado:** Direção do health do Kit 4 Potes 1050ml — se caindo, estável ou recuperando
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Série temporal de health ausente — top_items_details fornece apenas valor pontual; afirmar trajetória seria hipótese sem sustentação de dado
- **Agregado autorizado:** não
- **Tratamento aplicado:** health=0,75 citado como valor pontual ("hoje") sem atribuir direção
- **Aparece na mensagem final:** sim, como `health=0,75 hoje` — valor pontual, sem trajetória

---

- **Item bloqueado:** Quais anúncios específicos concentram a receita ADS de R$ 4.593,66
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** ads_summary é total agregado de 11 campanhas sem breakdown por platform_item_id; limitação estrutural do pacote
- **Agregado autorizado:** não
- **Tratamento aplicado:** ADS share citado como total agregado (75%, ROAS 13x, ACOS 4,7%) sem atribuição por anúncio
- **Aparece na mensagem final:** sim, como total agregado — nenhum anúncio específico nomeado como concentrador de receita ADS

---

- **Item bloqueado:** Inconsistência de título do KIT6YW1050 — anúncio com "Kit 10 Potes... 6 Unidades" (título malformado no ML)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Volume irrisório (2 pedidos); informação técnica de correção de anúncio que não altera a leitura do dia; pertence ao alinhamento operacional direto com Yasmin
- **Agregado autorizado:** não
- **Tratamento aplicado:** produto aparece no Top Produtos com nome simplificado baseado no SKU autoritativo ("Kit 10 Potes Herméticos 1050ml Refratário 4 Travas (6 unidades)"); inconsistência interna do título não mencionada
- **Aparece na mensagem final:** sim, como nome simplificado de produto no Top Produtos — inconsistência não exposta

---

- **Item bloqueado:** Configuração híbrida do anúncio de Kit 6 Canecas Tulipa (catalog_product_id preenchido com is_catalog=false)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Nota técnica de configuração sem confirmação de impacto mensurável; pertence à verificação direta com Yasmin
- **Agregado autorizado:** não
- **Tratamento aplicado:** impacto potencial em ranking de categoria citado na prioridade de reposição (conforme a própria L05 autorizou no campo `por_que` da prioridade), sem expor o detalhe técnico catalog_product_id/is_catalog
- **Aparece na mensagem final:** sim, como contexto de risco de ruptura em Catálogo — detalhe técnico omitido

---

- **Item bloqueado:** platform_item_ids (MLB...) nos textos principais de análise e prioridades
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Identificadores técnicos que não pertencem à comunicação principal do Slack
- **Agregado autorizado:** não aplicável — substituição por nome comercial
- **Tratamento aplicado:** todos os MLBs substituídos por nome comercial do produto em todas as seções
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) — campos internos de pipeline, não pertencem ao Slack
- Insight 1 (risco latente — Kit 06 Canequinhas): linguagem preservada como risco operacional direto e urgente; verbo "é cancelamento prospectivo garantido" mantido conforme a Condensadora; sem suavização
- Insight 2 (fato — inversão de mix de modalidade de envio): escrito como fato sem ressalva de indício; "Cross-Docking está funcionando normalmente" preservado conforme o `classificacao: fato` da L05
- Insight 3 (hipótese — ticket-led growth + ADS): linguagem de hipótese preservada — "hipótese estrutural em aberto", "só se confirma com mais dias de observação"; proibido transformar em certeza
- `alertas_de_confianca.nivel == "media"`: não exige ressalva explícita de confiança baixa; os três insights têm sustentação direta de dado e foram publicados normalmente
- Atribuição de Yasmin como responsável em todas as três prioridades — L05 não atribui responsável, L06 atribui conforme regra
- Preservação de condições de confirmação/refutação e escalonamento nas três prioridades — nenhuma alternativa operacional suprimida
- Simplificação do título ML real — item a item:
  - `IMB501P`: title ML "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto" + confirmed_variation_attributes ["Tampa Preta"] → "Kit 5 Potes de Vidro Redondos — Tampa Preta" (removido "Hermético Redondo Com Tampa", SEO; tipo "Kit" e quantidade "5 Peças" preservados; atributo "Tampa Preta" de confirmed_variation_attributes incluído)
  - `KIT10YW1050`: title ML "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" → "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas" (removido "Budamix Azul-petróleo 10 Unidades" — marca repetitiva e cor que não é atributo de variação confirmado; confirmed_variation_attributes vazio)
  - `IMB501C`: title ML "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Cinza" + confirmed_variation_attributes ["Tampa Cinza"] → "Kit 5 Potes de Vidro Redondos — Tampa Cinza" (mesma lógica IMB501P)
  - `IMB501V`: title ML "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Vermelho" + confirmed_variation_attributes ["Tampa Vermelha"] → "Kit 5 Potes de Vidro Redondos — Tampa Vermelha" (confirmed_variation_attributes usa "Tampa Vermelha"; title diz "Vermelho" — atributo autoritativo de confirmed_variation_attributes prevalece)
  - `KIT4YW1050`: title ML "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 4 Potes de Vidro Hermético 1050ml 4 Travas" (removido "Tampa", "Vedação Azul-petróleo" — cor não é confirmed_variation_attribute; confirmed_variation_attributes vazio)
  - `TL6250`: title ML "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" → "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" (removido "Coloridas Xícara" — SEO genérico; confirmed_variation_attributes vazio)
  - `914C_BAV`: title ML "Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico" → "Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico" (capitalização ajustada, "De" removido de "De 100 Ml"; confirmed_variation_attributes vazio)
  - `KIT10YW520`: title ML "Kit 10 Potes Herméticos 520ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" → "Kit 10 Potes Herméticos 520ml Refratário 4 Travas" (mesma lógica KIT10YW1050)
  - `KIT6YW1050`: title ML "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 6 Unidades" → "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas (6 unidades)" — SKU KIT6YW1050 indica 6 unidades; título ML malformado com "Kit 10" contradiz "6 Unidades"; a L05 bloqueou a exposição da inconsistência mas não o produto; usado o título ML com "(6 unidades)" entre parênteses para preservar a quantidade correta sem expor o conflito; confirmed_variation_attributes vazio
  - `KIT2YW1050`: title ML "Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 2 Potes de Vidro Hermético 1050ml 4 Travas" (mesma lógica KIT4YW1050)
- Omissão de modalidade de envio na seção VISÃO MERCADO LIVRE — `fulfillment_mix_yesterday_top10` cobre apenas o top 10 (91/101 pedidos, 90,1%); não representa dado objetivo da totalidade da conta; modalidade de envio tratada somente na ANÁLISE DA CONTA conforme regra
- Divergência de denominação cross-layer: L05 usou "Potes de Vidro Redondos Kit 5 Peças" no insight 2 da `analise_final_condensada`; L06 usou "Potes de Vidro Redondos Kit 5 Peças" na ANÁLISE (fidelidade à L05) e "Kit 5 Potes de Vidro Redondos — Tampa [Cor]" no Top Produtos (padronização com título ML simplificado) — divergência registrada; tese e produto referenciados são os mesmos
- Divergência de denominação cross-layer: L05 usou "Kit 06 Canequinhas Acrílico" em insight 1 e prioridade 1; L06 usou "Kit 06 Canequinhas Acrílico" na ANÁLISE (fidelidade à L05) e "Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico" no Top Produtos (título ML simplificado) — denominação da L05 preservada nas seções de análise e prioridades
- Divergência de denominação cross-layer: L05 usou "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" na prioridade 2; L06 usou o mesmo nome na PRIORIDADE (fidelidade à L05) e "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" no Top Produtos — denominação consistente entre seções
- Divergência de denominação cross-layer: L05 usou "Kit 4 Potes de Vidro Hermético 1050ml" na prioridade 3; L06 usou "Kit 4 Potes de Vidro Hermético 1050ml 4 Travas" no Top Produtos (título ML simplificado) e "Kit 4 Potes de Vidro Hermético 1050ml" na prioridade (fidelidade à L05) — denominação da L05 preservada na prioridade