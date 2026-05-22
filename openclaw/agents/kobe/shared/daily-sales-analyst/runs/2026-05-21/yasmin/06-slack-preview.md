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
- Kit 5 Potes de Vidro Hermético Redondo — Tampa Preta — 31 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 16 pedidos
- Kit 5 Potes de Vidro Hermético Redondo — Tampa Cinza — 13 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml 4 Travas — 8 pedidos
- Kit 5 Potes de Vidro Hermético Redondo — Tampa Vermelha — 8 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico — 3 pedidos
- Kit 10 Potes Herméticos 520ml Refratário 4 Travas — 2 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas (6 unidades) — 2 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml 4 Travas — 2 pedidos

🔍 ANÁLISE DA CONTA
- A reputação está verde-gold e o taxa de cancelamentos oficial é zero — mas o Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico seguia ativo com apenas 1 unidade disponível às 15h de hoje, sem pausa nem reposição confirmada no CD. Qualquer pedido adicional antes de uma ação corretiva vira cancelamento automático pelo ML e entra na janela longa da taxa de cancelamentos. O indicador oficial ainda não reflete o risco — a janela de atuação é agora.
- O GMV de ontem (+38% vs média 30d, +29,8% vs mesmo dia da semana passada) parece crescimento saudável, mas a estrutura é frágil: 75,5% do GMV passou pelo Mercado Ads (R$ 4.593,66 de R$ 6.082,82) e o ticket subiu +37% com volume de pedidos flat. A conta não ganhou alcance orgânico — ganhou ticket via mídia paga. Se as campanhas pararem ou o custo subir, não há piso orgânico visível para segurar o resultado.
- O mix de modalidade de envio de ontem (80% Cross-Docking no top 10 contra padrão histórico de 73–77% Full em 7d/30d) não é sinal de mudança sistêmica — é reflexo de três anúncios Cross-Docking que lideraram o volume: Potes de Vidro Tampa Preta com 31 pedidos, Kit 10 Potes 1050ml com 16 e Potes Tampa Cinza com 13. O padrão histórico Full da conta está intacto; o que o dia revela é que a base Full depende de poucos anúncios específicos para sustentar o mix das janelas recentes.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o status do Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico (1 unidade disponível, ativo às 15h de hoje) e pausar antes de novo pedido ou confirmar reposição emergencial no CD do ML. Qualquer pedido adicional gera cancelamento automático pelo ML que entra na taxa de cancelamentos da janela longa — degradando a reputação verde-gold de forma silenciosa antes do próximo ciclo de apuração. Confirmar/refutar por: anúncio pausado ou reposição confirmada até o fechamento BRT de hoje = risco neutralizado; anúncio permanecendo ativo sem reposição = checar taxa de cancelamentos no próximo snapshot de reputação. Escalar se: cancelamento automático confirmado pelo ML ou taxa de cancelamentos subir acima de 0 no próximo ciclo de reputação.
- Yasmin: registrar como ponto zero da série de ADS ML — share de 75,5% (R$ 4.593,66 sobre GMV de R$ 6.082,82), spend R$ 341,72, ROAS 13,4x, ACOS 4,71%, ticket médio R$ 60,83. Esta é a primeira leitura com dados de ADS disponíveis e sem histórico anterior na conta; sem esse registro, os próximos ciclos não têm base para confirmar se a dependência de mídia paga é crônica ou pontual. Confirmar/refutar por: share acima de 70% por 3 ciclos consecutivos confirma dependência estrutural crônica; share abaixo de 60% por 2 dias com GMV acima de R$ 5.500,00 indica orgânico crescendo como vetor real. Escalar se: share superar 70% por 3 dias consecutivos — abrir discussão com Kobe sobre dependência estrutural do canal em mídia paga.
- Yasmin: checar a trajetória do health do Kit 4 Potes de Vidro Hermético 1050ml (health=0,75, penalização ML ativa) nos registros disponíveis antes de qualquer decisão de cobertura ADS. É o maior acumulado de vendas em Full no top 10 e está rodando penalizado — a erosão de exposição orgânica não aparece no GMV agregado até acumular múltiplos ciclos. Confirmar/refutar por: health estável ou em recuperação nos próximos 2 ciclos = continuar observando sem ação; health caindo por 2 dias consecutivos = alinhar com Himmel sobre cobertura ADS preventiva para este anúncio. Escalar se: health cair abaixo de 0,70 ou volume do anúncio cair por 2 dias consecutivos sem variação de estoque ou preço.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação direcional sobre trajetória de health do Kit 4 Potes 1050ml (caindo, estável ou em recuperação)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Dado estruturalmente ausente do pacote — apenas valor pontual de health=0,75 no snapshot; série histórica por platform_item_id não existe na coleta atual. Qualquer afirmação direcional seria invenção.
- **Agregado autorizado:** não
- **Tratamento aplicado:** mencionado health=0,75 como fato pontual na prioridade, sem afirmar direção; ação enquadrada como "checar trajetória" e não como "health está caindo"
- **Aparece na mensagem final:** sim, como `health=0,75, penalização ML ativa` sem qualificação direcional

---

- **Item bloqueado:** Breakdown de receita ADS por anúncio ou por modalidade de envio
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Limitação estrutural da coleta — ads_summary entrega apenas totais agregados por conta, sem granularidade por platform_item_id. Hipótese sobre distribuição de cobertura ADS entre Cross-Docking e Full é irrespondível.
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da mensagem; citado apenas o total de ADS share (75,5%, R$ 4.593,66) que é dado disponível e validado
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Identidade dos 6 anúncios com health abaixo de 0,85 fora do top 10
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Não identificáveis no pacote — apenas o Kit 4 Potes (MLB4073003575) é o penalizado visível no top 10; os outros 6 são lacuna de visibilidade sem dado de produto disponível.
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da mensagem; health da conta referenciada apenas pelo anúncio identificável (Kit 4 Potes)
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Estimativa precisa de ruptura do Kit 6 Canecas Porcelana Tulipa 250ml e do Kit 10 Potes Herméticos 1050ml 10 Unidades
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Série diária de pedidos por produto ausente do pacote; coberturas estimadas (~3,8 e ~4,6 dias) são indicativas sem histórico confirmado e podem subestimar o risco.
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitidos das prioridades; apenas o Kit 06 Canequinhas (risco de 24h com dado confirmado) foi mantido como ação prioritária
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Confirmação de que ruptura do Kit 06 Canequinhas ainda não ocorreu ou de que pedidos foram cancelados
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Snapshot de 15h UTC não captura movimentação intraday pós-fechamento BRT; confiança média — não é possível afirmar com certeza se a ruptura já ocorreu ou está pendente.
- **Agregado autorizado:** não
- **Tratamento aplicado:** preservada a incerteza na análise e na prioridade com linguagem de risco latente ("qualquer pedido adicional antes de uma ação corretiva vira cancelamento"); não afirmado que cancelamento já ocorreu
- **Aparece na mensagem final:** sim, como risco latente com linguagem de indício, sem afirmar fato consumado

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) — são campos internos de pipeline, não pertencem à mensagem Slack.
- Preservação de classificação `risco latente` para Insights 1 e 2 via linguagem de indício: "sugere", "parece", "a janela de atuação é agora", "não há piso orgânico visível" — sem transformar em certeza.
- Classificação `fato` do Insight 3 mantida com linguagem direta: "não é sinal de mudança sistêmica", "o padrão histórico Full da conta está intacto".
- Confiança `media` da Condensadora preservada: nenhuma afirmação categórica sobre perguntas não respondidas pela Granular; todos os pontos abertos tratados como checagem, não como diagnóstico fechado.
- Nomes internos de camadas (Estratégica, Tática, Operacional, Granular, Condensadora) removidos integralmente da mensagem.
- MLBs removidos da mensagem; produtos referenciados por nome simplificado do título ML.
- Atribuição de responsável fixo Yasmin nas 3 prioridades — a L05 não atribui responsável; inserção feita na L06 conforme regra.
- Omissão da modalidade de envio na seção `📊 VISÃO MERCADO LIVRE` — dado de `fulfillment_mix_yesterday_top10` cobre apenas o top 10 (90 pedidos de 100), não a totalidade do dia; não autorizado pela Condensadora para esta seção.
- Simplificação de títulos ML no Top Produtos (registrada item a item):
  - `Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto` → `Kit 5 Potes de Vidro Hermético Redondo — Tampa Preta` (removido "Hermético Redondo Com Tampa"; atributo Tampa Preta via `confirmed_variation_attributes`)
  - `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades` → `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas` (removido "Budamix Azul-petróleo 10 Unidades" — marca/cor do pote não é atributo de variação confirmado para este SKU; `confirmed_variation_attributes` vazio)
  - `Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Cinza` → `Kit 5 Potes de Vidro Hermético Redondo — Tampa Cinza` (mesma lógica do Tampa Preta; atributo Tampa Cinza via `confirmed_variation_attributes`)
  - `Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo` → `Kit 4 Potes de Vidro Hermético 1050ml 4 Travas` (removido "Vedação Azul-petróleo" — cor do vedante é atributo não confirmado em `confirmed_variation_attributes`; campo vazio para este SKU)
  - `Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Vermelho` → `Kit 5 Potes de Vidro Hermético Redondo — Tampa Vermelha` (atributo Tampa Vermelha via `confirmed_variation_attributes`)
  - `Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara` → `Kit 6 Canecas Porcelana Tulipa Lisa 250ml` (removido "Coloridas Xícara" — palavras de SEO sem atributo de variação; `confirmed_variation_attributes` vazio)
  - `Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico` → `Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico` (leve encurtamento; title, raw_title e display_name idênticos; mantido "Acrílico" como descritor relevante do suporte)
  - `Kit 10 Potes Herméticos 520ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades` → `Kit 10 Potes Herméticos 520ml Refratário 4 Travas` (removido "Budamix Azul-petróleo 10 Unidades"; mesma lógica do KIT10YW1050)
  - `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 6 Unidades` → `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas (6 unidades)` (mantido "(6 unidades)" entre parênteses para diferenciar do KIT10YW1050 de 10 unidades que aparece na posição 2; `confirmed_variation_attributes` vazio)
  - `Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo` → `Kit 2 Potes de Vidro Hermético 1050ml 4 Travas` (mesma lógica do KIT4YW1050; removido "Vedação Azul-petróleo")
- Divergência de denominação cross-layer: a L05 usou "Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico" nos insights e prioridades; a L06 usou "Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico" (simplificação mínima do título ML). Motivo: padronização com o nome usado no Top Produtos; sem alteração de identidade ou atributo.
- Divergência de denominação cross-layer: a L05 usou "Potes de Vidro Tampa Preta", "Kit 10 Potes Herméticos 1050ml" e "Potes Tampa Cinza" nos insights (versões encurtadas informais). A L06 expandiu ligeiramente para os nomes padronizados do Top Produtos ("Kit 5 Potes de Vidro Hermético Redondo — Tampa Preta", "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas", "Kit 5 Potes de Vidro Hermético Redondo — Tampa Cinza") para consistência interna da mensagem.
- Substituição de "cancellations_rate" e "reputation.cancellations_rate" por "taxa de cancelamentos" — terminologia operacional para Yasmin; "cancellations_rate" é campo técnico de API.
- "Mercado Ads" mantido no lugar de "Mercado Ads de Himmel" — nome de Himmel não vai ao Slack; Yasmin alinha com Himmel quando necessário, conforme regra de acionamento.
- `~R$ 341,72` preservado com 2 casas decimais na prioridade 2 (R$ 341,72); não usado `~` pois o valor exato está disponível no pacote.
- Comparações temporais (+38% vs 30d, +29,8% vs mesmo dia da semana) mantidas exclusivamente na `🔍 ANÁLISE DA CONTA`, vindas da Condensadora — não inseridas na `📊 VISÃO MERCADO LIVRE`.
- Rodapé com data 21/05/2026 em BRT, janela 00:00–23:59, conforme data analisada.