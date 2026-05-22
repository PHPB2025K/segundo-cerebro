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
- O resultado foi bom no número mas frágil na estrutura: os três anúncios Full com volume relevante chegaram ao dia com limitações operacionais — o Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico em ruptura consumada (1 unidade em estoque, 3 pedidos registrados), o Kit 6 Canecas Porcelana Tulipa Lisa 250ml com cobertura estimada de apenas 2-3 dias ao ritmo atual, e o Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo com health penalizado (0,75) sem série histórica para saber se está caindo ou estabilizando. O que sustentou o dia foi a família Potes de Vidro Hermético Redondo em Cross-Docking, não o Full. Os 3 cancelamentos do dia podem já ter vindo do Canequinhas — correlação circunstancial, não confirmada — o que significa que a taxa de cancelamentos (hoje em zero no termômetro oficial do ML) pode não estar limpa.
- O mix de modalidade de envio do dia (Full em 19,8% contra 73,6% no mês) parece sinal de colapso sistêmico do Full, mas a leitura correta é outra: a família Potes de Vidro Hermético Redondo Kit 5 Peças nas variações Tampa Preta, Cinza e Vermelha somou 53 pedidos em Cross-Docking — 52,5% do volume total — e sozinha explica a inversão. O Full não encolheu estruturalmente na conta; o dia foi dominado pelo Cross-Docking por concentração produto-específica.
- O ADS respondeu por 75,1% do GMV (R$ 4.593,66 de R$ 6.113,02) com ROAS 13,4x e ACOS 4,71% — campanha eficiente, mas esta é a primeira leitura estruturada da conta e não há série histórica para saber se o share é estrutural ou pontual. O orgânico estimado ficou em cerca de R$ 1.519,36 no dia. A decisão correta agora não é ajustar: é registrar o ponto zero e observar o padrão por 3 dias antes de qualquer movimentação.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar status do Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico no CD do ML e providenciar reposição urgente ou cancelamento controlado dos pedidos em aberto, antes de pausa automática pelo ML. Ruptura consumada: 1 unidade disponível com 3 pedidos registrados no dia, anúncio ainda ativo no snapshot — cancelamento automático pelo ML contamina a taxa de cancelamentos (hoje em zero no termômetro oficial), e a correlação circunstancial com os 3 cancelamentos do dia não pôde ser descartada; cancelamento controlado é menos danoso à reputação do que o automático. Confirmar/refutar por: anúncio pausado ou fechado no próximo pacote sem reposição confirmada = risco já materializado, registrar como variável para leituras de reputação dos próximos dias; reposição chegando ao CD antes da pausa = risco neutralizado. Escalar se novos cancelamentos aparecerem nos próximos 2 dias com o termômetro de reputação começando a se mover.
- Yasmin: verificar cobertura de estoque do Kit 6 Canecas Porcelana Tulipa Lisa 250ml no CD do ML e acionar reposição ou alerta em até 24h. Cobertura estimada de 2-3 dias ao ritmo de 5 pedidos por dia com 14 unidades disponíveis em Full — anúncio em Full sem estoque fica inativo aguardando reabastecimento e perde posicionamento no período; janela preventiva ainda aberta, diferente do Canequinhas onde a ruptura já é fato. Confirmar/refutar por: reposição confirmada com cobertura para pelo menos 7 dias = risco neutralizado; estoque caindo abaixo de 5 unidades nos próximos 2 pacotes sem movimento confirmado = acionar alerta prioritário equivalente ao Canequinhas.
- Yasmin: registrar como ponto zero da série — ADS share de 75,1% e ticket médio de R$ 60,52 em 21/05/2026. Nenhuma ação em campanhas. Primeira leitura estruturada sem histórico interpretativo confirmado — sem série não é possível determinar se a dependência de ADS é estrutural ou pontual, nem se o ticket elevado é sustentável organicamente. Confirmar/refutar por: ADS share acima de 60% por 3 dias consecutivos confirma dependência estrutural; ticket acima de R$ 55,00 por 3 dias sem aumento de spend sugere deslocamento orgânico de mix; ticket abaixo de R$ 46,00 em dia de spend reduzido confirma que o ticket alto é ADS-driven. Escalar se ADS share acima de 60% por 3 dias consecutivos — abrir discussão sobre cronicidade da dependência.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação de que os 3 cancelamentos do dia vieram especificamente do Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 declarou inconclusivo por falta de dado — correlação circunstancial (3 pedidos coincidentes com 3 cancelamentos) existe mas não é confirmável sem breakdown de cancelamentos por order_id; dado estruturalmente ausente do pacote
- **Agregado autorizado:** não
- **Tratamento aplicado:** preservada a correlação como "correlação circunstancial, não confirmada" com linguagem de indício — não atribuída causalidade
- **Aparece na mensagem final:** não como afirmação; sim como ressalva de incerteza ("podem já ter vindo")

---

- **Item bloqueado:** Recomendação de ação sobre o Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo com base no health=0,75
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 não respondeu à pergunta sobre direção do health — série temporal não disponível no pacote; pré-condição da L02 para qualquer ação não foi atendida
- **Agregado autorizado:** não
- **Tratamento aplicado:** produto citado na análise apenas como elemento de contexto estrutural (health penalizado, direção desconhecida); nenhuma prioridade tática criada para ele
- **Aparece na mensagem final:** sim, como dado de contexto em ANÁLISE DA CONTA, sem recomendação de ação

---

- **Item bloqueado:** Uso do alias "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas" para identificar qualquer produto individualmente
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou colisão de display_name — KIT6YW1050 (MLB4676751119, 6 unidades) e KIT10YW1050 (MLB4676726433, 10 unidades) compartilham esse alias interno; qualquer menção sem diferenciador é ambígua
- **Agregado autorizado:** não aplicável — substituição por title ML real com diferenciador de unidades
- **Tratamento aplicado:** usados os display_shorts distintos: "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" e "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades"
- **Aparece na mensagem final:** não como alias ambíguo; sim como titles distintos em Top Produtos

---

- **Item bloqueado:** Composição do ADS revenue por anúncio — se a campanha priorizou ou não a família IMB501
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 não respondeu — breakdown de spend/revenue por platform_item_id é dado estruturalmente ausente do pacote; ads_summary é agregado
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da mensagem; ADS mencionado apenas nos termos agregados disponíveis (share, ROAS, ACOS total)
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Platform_item_ids (MLB...) em texto narrativo de análise ou prioridades
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Regra ML — MLBs não aparecem no Slack
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum MLB presente na mensagem; produtos identificados exclusivamente por nome comercial
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) dos três insights — são metadados de pipeline; informação analítica preservada, rótulos internos omitidos
- Insight 1 (classificacao: risco latente) — mantida linguagem de indício: "podem já ter vindo", "pode não estar limpa"; tese e estrutura da L05 preservadas integralmente
- Insight 2 (classificacao: fato) — escrito assertivamente: "a leitura correta é outra", "O Full não encolheu estruturalmente"; sem hedging, consistente com classificação de fato
- Insight 3 (classificacao: risco latente) — mantida incerteza explícita: "não há série histórica para saber se o share é estrutural ou pontual"; nenhuma conclusão definitiva sobre dependência estrutural
- Omissão de modalidade de envio na seção VISÃO MERCADO LIVRE — dado disponível apenas via `fulfillment_mix_yesterday_top10` (cobertura ~90% / top 10 ponderado, não totalidade do dia); Condensadora não autorizou exibição com ressalva explícita de cobertura nessa seção
- `display_short` usado verbatim para todos os 10 produtos do Top Produtos, sem alterações de capitalização, ordem ou conteúdo
- `confirmed_variation_attributes` adicionados ao nome dos três SKUs da família IMB501: Tampa Preta (IMB501P), Tampa Cinza (IMB501C), Tampa Vermelha (IMB501V) — formato "[display_short] — [atributo confirmado]"
- Colisão de display_name resolvida via display_short: KIT10YW1050 → "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades"; KIT6YW1050 → "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades" — diferenciação por número de unidades presente nos display_shorts da L00, não inferida
- Orgânico estimado: L05 usou "cerca de R$1.500" (arredondamento); renderizado como "cerca de R$ 1.519,36" (valor calculado do data package: R$ 6.113,02 − R$ 4.593,66) — centavos obrigatórios por regra numérica; é formatação, não reanalíse
- Valores ADS precisos do data package: R$ 4.593,66 (revenue_ads_yesterday_brl) e R$ 6.113,02 (gmv) — L05 usou aproximações "R$4.593" e "R$6.113"; renderizados com centavos obrigatórios
- Thresholds das prioridades formatados com centavos: "R$ 55,00" e "R$ 46,00" (L05 escreveu "R$55" e "R$46")
- `escalar_se: "não aplicável"` na prioridade 2 — linha de escalonamento omitida da mensagem; registrado aqui para QA
- "cancellations_rate" substituído por "taxa de cancelamentos" em texto narrativo — jargão técnico de API desnecessário para Yasmin; terminologia operacional equivalente
- Atribuição de Yasmin como responsável fixo nas três prioridades do dia — L05 não atribui responsável; atribuição feita aqui conforme regra da L06
- Sem divergência cross-section de denominação: nomes usados pela L05 nos insights/prioridades (Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico; Kit 6 Canecas Porcelana Tulipa Lisa 250ml; Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo; família Potes de Vidro Hermético Redondo Kit 5 Peças) coincidem com os display_shorts correspondentes do Top Produtos — sem divergência a registrar
- Referência interna "a Condensadora apontou" / "a Granular bloqueou" — nenhuma menção de camadas internas na mensagem Slack; terminologia de pipeline omitida integralmente