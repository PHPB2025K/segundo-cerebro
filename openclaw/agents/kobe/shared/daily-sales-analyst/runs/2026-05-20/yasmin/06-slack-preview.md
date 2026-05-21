<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.087,71
- Pedidos: 91 pedidos
- Ticket médio: R$ 55,91
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 5 Potes de Vidro Hermético Redondo — Tampa Preta: 23 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml: 13 pedidos
- Jogo 6 Canequinhas 100ml com Suporte de Madeira Amarelo: 8 pedidos
- Kit 10 Potes Herméticos 1050ml: 5 pedidos
- Jogo Potes de Vidro 5 Peças — Tampa Vermelha: 5 pedidos
- Kit 6 Canecas Porcelana Tulipa 250ml: 5 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml: 3 pedidos
- Suporte Gamer 2 Controles e Headset Mesa PS5/PS4 Preto: 3 pedidos
- Kit 4 Potes de Vidro 320ml Azul-petróleo: 3 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico: 3 pedidos

🔍 ANÁLISE DA CONTA
- O GMV do dia ficou +32% acima da média das últimas quatro quartas com praticamente o mesmo número de pedidos — o ganho é real, mas veio inteiramente do ticket médio (R$ 55,91 vs R$ 41,53 nas mesmas quartas). A conta não cresceu em alcance; cresceu em valor por pedido. Patamar mais alto confirmado em múltiplas janelas, não resultado pontual.
- O único risco operacional concreto do dia está no Kit 6 Canequinhas com Suporte Acrílico em Full: o snapshot mostra 3 unidades disponíveis no CD do ML com demanda de ~3 pedidos por dia. Se o estoque zerar antes da reposição, o ML pausa o anúncio automaticamente e cancela pedidos pendentes — o que contamina a taxa de cancelamentos da reputação. A janela de ação é de horas, não de dias.
- A campanha está com ROAS 11,6x e ACOS 4,64% — resultado excepcional. Mas ela responde por 59,8% do GMV, e os dois anúncios que mais venderam após o campeão têm health penalizada (0,75 e 0,71), operam sem catálogo e dependem exclusivamente de posição em ranking de categoria. A hipótese — sem confirmação direta por falta de dado disponível — é que o ADS está compensando a perda de posição orgânica desses dois. O patamar de GMV ainda não foi testado sem a campanha.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar estoque do Kit 6 Canequinhas com Suporte Acrílico em Full e providenciar reposição emergencial se o anúncio ainda não pausou. Com 3 unidades no CD do ML e demanda de ~3 pedidos por dia, a margem é mínima ou já zerou — ruptura em Full pausa o anúncio automaticamente e gera cancelamentos que impactam a reputação. Confirmar/refutar por: available_quantity acima de 20 unidades após reposição = risco neutralizado; anúncio pausado na próxima leitura = ruptura já ocorreu antes da reposição. Escalar se: anúncio já pausado ou cancelamentos confirmados neste produto — registrar data e hora como variável confundidora para leituras de reputação dos próximos dias.
- Yasmin: registrar como ponto zero formal da série o ADS share (59,8%), ticket médio (R$ 55,91) e ACOS (4,64%) do dia 20/05/2026. Esta é a primeira leitura estruturada completa — sem esse baseline, futuras leituras de dependência de ADS e variação de ticket ficam sem âncora. Confirmar/refutar por: ADS share acima de 60% por 3 dias consecutivos com ticket mantido = dependência estrutural consolidada; ticket abaixo de R$ 50,00 em dia sem variação de spend = reversão de mix. Escalar se: ADS share acima de 60% por 3 dias consecutivos — abrir discussão com Kobe sobre dependência estrutural; health dos dois anúncios penalizados caindo por 2 ciclos consecutivos — alinhar com Himmel.
- Yasmin: verificar e registrar o health dos dois anúncios penalizados (0,75 e 0,71) na próxima leitura para iniciar a série temporal. Esses valores são o ponto zero do ciclo inaugural — sem registrar a direção nos próximos 2 ciclos, o gatilho de alinhamento com Himmel fica indefinidamente bloqueado. Confirmar/refutar por: health estável ou recuperando em ambos = manter observação; health caindo em um ou ambos por 2 ciclos consecutivos = alinhar com Himmel sobre cobertura preventiva. Escalar se: health abaixo dos valores atuais em 2 leituras consecutivas em qualquer um dos dois anúncios.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atribuição dos 3 cancelamentos do dia ao Kit 6 Canequinhas com Suporte Acrílico ou a qualquer anúncio específico
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Pacote não entrega breakdown de cancelamentos por platform_item_id — distribuição é inconclusiva
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido; urgência da prioridade sustentada pelo risco de ruptura (3 unidades / ~3 pedidos/dia), não por cancelamentos confirmados nesse anúncio
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Afirmação de que Himmel está priorizando ADS especificamente nos dois anúncios com health penalizada
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** ads_summary não tem granularidade por platform_item_id — limitação estrutural do pacote
- **Agregado autorizado:** não
- **Tratamento aplicado:** hipótese preservada com linguagem de indício ("A hipótese — sem confirmação direta por falta de dado disponível — é que o ADS está compensando a perda de posição orgânica desses dois")
- **Aparece na mensagem final:** não como afirmação; sim como hipótese explicitamente qualificada

---

- **Item bloqueado:** Afirmação de que a health dos dois anúncios penalizados está caindo ou em deterioração ativa
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Ciclo inaugural — valores de 0,75 e 0,71 são pontos zero sem série temporal disponível; direção desconhecida
- **Agregado autorizado:** não
- **Tratamento aplicado:** valores reportados como fatos pontuais ("health penalizada (0,75 e 0,71)") sem adjetivo de trajetória; prioridade 3 instrui registrar ponto zero para iniciar série nos próximos ciclos
- **Aparece na mensagem final:** não como deterioração; sim como valores pontuais sem direção

---

- **Item bloqueado:** Interpretação de health=null no campeão do dia (Kit 5 Potes Tampa Preta, 23 pedidos) como risco de penalização ou sinal de alerta
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou que health=null é ausência de cálculo ML, não penalização; 78% dos anúncios ativos da conta têm health=null
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da análise e das prioridades
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Divergência de fulfillment mix (43,7% Cross-Docking vs 26,1% no 30d) tratada como sinal sistêmico ou problema de modalidade
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Divergência produto-específica causada pelo peso do campeão em Cross-Docking; não é anomalia sistêmica
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da análise
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Platform_item_ids (MLBs) na análise principal ou nas prioridades
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Regra ML da Condensadora — MLBs não aparecem na comunicação direta para Yasmin
- **Agregado autorizado:** não — substituídos por nomes comerciais
- **Tratamento aplicado:** todos os MLBs substituídos por nome simplificado do produto (ex: "Kit 6 Canequinhas com Suporte Acrílico" no lugar de "MLB4410218897")
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) de todos os 3 insights — são campos de pipeline, não informação para Yasmin
- Preservação de nuance `hipótese` no insight 3: mantida frase "A hipótese — sem confirmação direta por falta de dado disponível" para não transformar hipótese em fato; substituída expressão "dado granular" (referência interna a camada) por "dado disponível"
- Preservação de nuance `risco latente` no insight 2: linguagem condicional mantida ("Se o estoque zerar antes da reposição…")
- Fulfillment omitido da seção VISÃO MERCADO LIVRE — dado de fulfillment_mix_yesterday_top10 cobre apenas os top 10 por peso de pedidos (71 de 91 pedidos); cobertura parcial, sem autorização explícita da Condensadora para exibir com ressalva nesta seção
- Referência a "Kit 06 Canequinhas com Suporte Acrílico" (em vez de MLB4410218897) aplicada na análise e nas prioridades — nome comercial derivado do título ML real simplificado
- Atribuição de Yasmin como responsável em todas as 3 prioridades — regra fixa ML (Condensadora não atribui responsável, Slack Writer atribui)
- Simplificações de título ML real item a item:
  - **IMB501P** — `"Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto"` → `"Kit 5 Potes de Vidro Hermético Redondo — Tampa Preta"`: reordenado para clareza ("Kit" na frente); "Com Tampa" removido como redundante com atributo confirmado; confirmed_variation_attributes `["Tampa Preta"]` adicionado após travessão
  - **KIT4YW1050** — `"Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo"` → `"Kit 4 Potes de Vidro Hermético 1050ml"`: removido "Tampa 4 Travas Vedação Azul-petróleo" para brevidade; confirmed_variation_attributes vazio — sem atributo a acrescentar; dimensão crítica 1050ml mantida
  - **914C** — `"Jogo 6 Canequinha 100ml Caneca Café Suporte Madeira Alumínio Amarelo"` → `"Jogo 6 Canequinhas 100ml com Suporte de Madeira Amarelo"`: normalizado plural ("Canequinha" → "Canequinhas"); "Caneca Café" removido como SEO redundante; "Alumínio" condensado com "Amarelo" para "Amarelo" — atributo presente no título ML real, mantido para diferenciar do 914C_BAV
  - **KIT10YW1050** — `"Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades"` → `"Kit 10 Potes Herméticos 1050ml"`: removido "Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" como SEO/redundante (quantidade já expressa em "Kit 10"); dimensão crítica 1050ml mantida
  - **IMB501V** — `"Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita"` → `"Jogo Potes de Vidro 5 Peças — Tampa Vermelha"`: "Claro Mantimentos Marmita" removido como SEO; "Claro" descreve o corpo de vidro (material), não a variação — confirmado pela L04 como não-conflito; confirmed_variation_attributes `["Tampa Vermelha"]` adicionado após travessão; display_name não utilizado (título ML real disponível e válido)
  - **TL6250** — `"Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara"` → `"Kit 6 Canecas Porcelana Tulipa 250ml"`: removido "Lisa Coloridas Xícara" como adjetivos genéricos/SEO; tipo (Porcelana Tulipa) e dimensão (250ml) mantidos
  - **KIT2YW1050** — `"Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo"` → `"Kit 2 Potes de Vidro Hermético 1050ml"`: mesmo critério aplicado a KIT4YW1050; dimensão 1050ml mantida para diferenciar de KIT4YW320
  - **SPC0111** — `"Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto"` → `"Suporte Gamer 2 Controles e Headset Mesa PS5/PS4 Preto"`: removido "Organizador" como redundante; PS5/PS4 normalizado para legibilidade; "Preto" mantido por estar no título ML real
  - **KIT4YW320** — `"Kit Conjunto 4 Potes De Vidro 320ml Tampa Hermético 4 Travas Azul-petróleo"` → `"Kit 4 Potes de Vidro 320ml Azul-petróleo"`: removido "Conjunto" (redundante com Kit), "Tampa Hermético 4 Travas"; dimensão 320ml e Azul-petróleo mantidos para diferenciar de KIT4YW1050
  - **914C_BAV** — `"Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico"` → `"Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico"`: normalizado "06" → "6", "Ml" → "ml"; "Acrílico" mantido como distinção essencial em relação ao 914C (Alumínio Amarelo)
- Display_name interno não utilizado em nenhum dos 10 produtos — título ML real disponível em todos os casos com convergência confirmada pela L04; display_name ficou como fallback não acionado
- Expressão "dado granular" do insight 3 da Condensadora substituída por "dado disponível" — "granular" é referência a camada interna de pipeline, não deve aparecer na mensagem para Yasmin