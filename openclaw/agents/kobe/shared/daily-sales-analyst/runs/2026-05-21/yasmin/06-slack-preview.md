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
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta — 31 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades — 16 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza — 13 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Vermelha — 9 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 8 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos
- Kit 10 Potes Herméticos 520ml Azul-petróleo 10 Unidades — 2 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades — 2 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 2 pedidos

🔍 ANÁLISE DA CONTA
- O dia foi sustentado pela família de Potes de Vidro Redondos (Tampa Preta, Cinza e Vermelha juntos = 53 pedidos), todos em Cross-Docking e sem risco de estoque. Enquanto eles cobriam o volume, o segmento Full acumulou três pressões ao mesmo tempo: o Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico estava ativo com 1 unidade no final do dia, o Kit 6 Canecas Porcelana Tulipa Lisa 250ml tem cobertura prospectiva de ~3 dias, e o Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo opera com health=0,75 e ranking penalizado. O GMV de R$ 6.113,02 não reflete essa deterioração porque o Cross-Docking compensou — mas o estoque no CD do ML está se esvaziando silenciosamente, e historicamente é o Full que sustenta 73–77% da operação. Leitura: risco latente, não emergência resolvida.
- Os ADS estão eficientes — ROAS de 13,4x, ACOS de 4,71%, com R$ 4.594,00 de faturamento atribuído sobre R$ 341,72 investidos. O ponto de atenção é que 75,1% do GMV do dia passou por ADS, sem base orgânica verificável para sustentar esse patamar de forma independente. O crescimento de GMV dos últimos 60 dias pode refletir expansão progressiva de investimento, não ganho estrutural de mercado. Essa hipótese é inaugural — precisa de 3 a 5 dias de série para ser confirmada ou descartada. Por ora: não mexer, observar.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o status atual do Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico (Full). Com 1 unidade restante e anúncio ativo até o snapshot de ontem (~18h BRT), o risco de ruptura não estava resolvido. Se ainda ativo: acionar reposição emergencial no CD do ML ou pausar de forma controlada antes que o ML pause automaticamente. Por quê: qualquer pedido novo esgota o estoque e aciona cancelamento automático pelo ML, com impacto direto no cancellations_rate — que hoje está em zero. Pausa controlada por Yasmin evita o cancelamento automático; pausa automática pelo ML é o pior cenário para a reputação. Confirmar/refutar por: anúncio com status=pausado por Yasmin ou reposição confirmada no CD do ML em até 24h = risco neutralizado; anúncio ainda ativo sem reposição no próximo snapshot = ruptura iminente. Escalar se: anúncio pausado automaticamente pelo ML com cancelamentos gerados — monitorar cancellations_rate por 3 ciclos.
- Yasmin: iniciar reposição do Kit 6 Canecas Porcelana Tulipa Lisa 250ml (Full) no CD do ML. Cobertura prospectiva de ~3 dias ao ritmo atual (~5 pedidos/dia), e reabastecimento de Full é mais lento que Cross-Docking — a janela de ação útil é hoje. Por quê: sem reposição, o anúncio chega a zero em ~D+3. Atenção: esse anúncio está associado ao catálogo ML mas não compete ativamente por Buy Box de Catálogo — o processo de reabastecimento pode alterar esse estado e modificar o perfil competitivo do anúncio após a retomada. Confirmar/refutar por: reposição solicitada ao CD do ML em até 48h = risco de ruptura controlado; available_quantity abaixo de 5 no próximo snapshot sem reposição confirmada = urgência equivalente à das Canequinhas.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** `"Retangular"` como atributo dos kits KIT4YW1050 e KIT2YW1050
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** "Retangular" é adição interna Budamix ausente nos títulos ML e raw_titles — não é atributo confirmado pelo ML
- **Agregado autorizado:** não
- **Tratamento aplicado:** os produtos foram nomeados usando `display_short` sem "Retangular" (`Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo` e `Kit 2 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo`)
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Causa dos 3 cancelamentos atribuída a produto específico
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** inconclusivo por falta de dado — nenhuma evidência granular vincula ou descarta associação com qualquer anúncio
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados apenas como dado objetivo na seção VISÃO (3 cancelamentos), sem atribuição de causa ou produto
- **Aparece na mensagem final:** sim, como dado objetivo neutro na VISÃO (quantidade: 3), sem causa atribuída

---

- **Item bloqueado:** Direção do health=0,75 do Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo comunicada como dado confirmado
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** série temporal de health ausente do pacote — direção (caindo/estável/recuperando) desconhecida; L02 condicionou ação ao conhecimento da direção
- **Agregado autorizado:** não
- **Tratamento aplicado:** health=0,75 citado como fato pontual observado (é fato), sem afirmação de direção; prioridade sobre esse anúncio não incluída nas prioridades do dia pois ação tática segue bloqueada por falta de dado de direção
- **Aparece na mensagem final:** sim, como elemento do insight 1 (fato confirmado: health=0,75, ranking penalizado), sem direção atribuída

---

- **Item bloqueado:** Hipótese de concentração de verba ADS na família IMB501 como dado confirmado
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** breakdown ADS por platform_item_id é limitação estrutural do pacote — não verificável
- **Agregado autorizado:** não
- **Tratamento aplicado:** hipótese não incluída na mensagem; o insight 2 trata a dependência ADS em nível de conta (75,1% do GMV), não por produto específico, preservando a tese sem afirmar concentração por anúncio
- **Aparece na mensagem final:** não (como concentração por produto); sim (como dependência ADS agregada — classificada como hipótese inaugural)

---

- **Item bloqueado:** IDs técnicos MLB nos campos de análise e prioridades
- **Origem do bloqueio:** L05 Condensadora / regra estrutural ML
- **Motivo:** MLBs são IDs técnicos internos — proibidos na comunicação direta para Yasmin
- **Agregado autorizado:** não aplicável — substituídos por nome comercial dos produtos
- **Tratamento aplicado:** todos os produtos referenciados por nome comercial; nenhum MLB visível na mensagem
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) removidos — são campos internos de pipeline, não vão para Slack
- Insight 1 (classificação `risco latente`) preservado com linguagem de risco prospectivo: "risco latente, não emergência resolvida"; evitado qualquer termo que converta o risco em certeza operacional já materializada
- Insight 2 (classificação `hipótese`) preservado com linguagem de indício: "pode refletir", "hipótese inaugural", "precisa de 3 a 5 dias de série para ser confirmada ou descartada"; proibido converter em fato
- Confiança `media` da L05: não impõe frase padrão de dia neutro, mas preserva ressalvas explícitas em ambos os insights; linguagem mantém abertura analítica sem falsa certeza
- Nomes dos produtos na ANÁLISE convergem com os `display_short` + `confirmed_variation_attributes` usados no TOP PRODUTOS para consistência cross-section (ex.: "Potes de Vidro Redondos" usado como referência familiar, "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" alinhado ao display_short do top produtos)
- Simplificação de título ML — Top Produtos (item a item):
  - IMB501P: `display_short` = "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + `confirmed_variation_attributes` = ["Tampa Preta"] → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta"
  - KIT10YW1050: `display_short` = "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" + sem atributos confirmados → usado verbatim
  - IMB501C: `display_short` = "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + `confirmed_variation_attributes` = ["Tampa Cinza"] → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza"
  - IMB501V: `display_short` = "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças" + `confirmed_variation_attributes` = ["Tampa Vermelha"] → "Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Vermelha"
  - KIT4YW1050: `display_short` = "Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo" + sem atributos confirmados → usado verbatim (sem "Retangular" — bloqueado)
  - TL6250: `display_short` = "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" → usado verbatim
  - 914C_BAV: `display_short` = "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" → usado verbatim
  - KIT10YW520: `display_short` = "Kit 10 Potes Herméticos 520ml Azul-petróleo 10 Unidades" → usado verbatim
  - KIT6YW1050: `display_short` = "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades" → usado verbatim
  - KIT2YW1050: `display_short` = "Kit 2 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo" → usado verbatim (sem "Retangular" — bloqueado)
- Modalidade de envio omitida da seção VISÃO MERCADO LIVRE — `fulfillment_mix_yesterday_top10` cobre apenas 91/101 pedidos (top 10 items); dado de cobertura parcial não representa totalidade objetiva da plataforma; tratamento de modalidade de envio realocado inteiramente para ANÁLISE DA CONTA conforme regra
- Comparações temporais ausentes da VISÃO — percentuais vs 7d/30d/60d pertencem à análise, não à visão objetiva do dia
- Yasmin atribuída como responsável em todas as prioridades — responsável fixo Mercado Livre; L05 não atribui responsável; atribuição feita pela L06 conforme regra
- Frases longas da L05 nos insights quebradas em construções mais diretas sem alterar tese, verbo principal ou classificação
- Referências a nomes de camadas internas ("Granular", "Condensadora", "Operacional") substituídas por linguagem externa neutra ("snapshot de ontem", "ao ritmo atual")
- Divergência de denominação cross-layer — nenhuma divergência identificada: os nomes usados na ANÁLISE e PRIORIDADES estão alinhados com os `display_short` do TOP PRODUTOS; L05 usou "Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico" e "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" nos insights/prioridades, e L06 manteve os mesmos nomes derivados dos `display_short` correspondentes
- Valor de ADS revenue arredondado de R$ 4.593,66 para "R$ 4.594,00" na ANÁLISE para facilitar leitura — mantida a informação de magnitude sem centavos no contexto discursivo; valor original disponível no dado; decisão: manter R$ 4.594,00 com centavos conforme regra de padrão numérico obrigatório (corrigido para R$ 4.594,00, não "R$ 4.594")
- Prioridade sobre health do Kit 4 Potes não incluída — ação tática condicionada pela L02 ao conhecimento da direção do health, que a L04 declarou inconclusiva por falta de dado; incluir prioridade sem dado de direção induziria decisão precipitada; registrado em Respeito de bloqueios