<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 24/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.024,80
• Pedidos: 99 pedidos
• Ticket médio: R$ 50,76
• Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 29 pedidos
• Kit 4 Potes 1050ml — 18 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
• Kit 6 Canecas Lisas 200ml — 9 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 8 pedidos

🔍 ANÁLISE DA CONTA
• O GMV ficou +10% acima do 30d e +23% acima do 60d — mas o número de pedidos não saiu do lugar (99). O crescimento veio inteiro do ticket médio (R$ 50,76). O patamar é real; o risco é que não há volume para amortizar se o ticket recuar.
• O ADS representou 71% do GMV com ROAS de 11x — campanha eficiente. O sinal que chama atenção está embaixo: Potes Vidro 5 Peças e Kit 4 Potes 1050ml estão com nível de qualidade do anúncio em Padrão inferior (0,71 e 0,75) há quatro ciclos seguidos, o que sugere que o ML está restringindo a exposição orgânica deles. O ADS parece estar cobrindo ranking perdido, não amplificando orgânico saudável. O recuo de share do ciclo anterior (49%) parece ter sido oscilação, não virada.
• Quase metade do dia (47,5%) veio de um único anúncio — as três variações de Potes Vidro 5 Peças (Tampa Preta, Vermelha e Cinza) compartilham o mesmo anúncio, com nível de qualidade do anúncio em Padrão inferior (0,71) há quatro ciclos seguidos. A concentração não está em três produtos separados, está num anúncio só — e cresceu pelo terceiro ciclo seguido (44% → 44% → 47,5%). Se esse anúncio perder posição, a cauda atual não parece ser forte o suficiente para absorver.

🎯 PRIORIDADES DO DIA
• Yasmin: checar reposição em trânsito ao CD do ML para o Kit 6 Canecas Lisas 200ml (anúncio Catálogo Premium, Full, com 25 unidades e ritmo de 9 pedidos/dia — cobertura de ~2,8 dias). Ruptura em Catálogo Full implica perda de Buy Box com recuperação lenta, e esse anúncio carrega ticket alto num canal onde todo o ganho de patamar veio do ticket. Confirmar/refutar por: reposição com chegada ao CD em até 48h neutraliza o risco; sem reposição em trânsito confirmada até amanhã, urgência sobe. Escalar se: cobertura cair abaixo de 2 dias sem reposição confirmada — acionar Kobe pelo impacto prospectivo na trajetória MercadoLíder Platinum.
• Yasmin: verificar status do Kit 6 Canecas Porcelana Tulipa — o anúncio sumiu do top hoje; no ciclo anterior estava com 2 unidades e ritmo de 6 a 9 pedidos/dia, o que sugere ruptura ou pausa automática. Verificar também se os 2 cancelamentos do dia têm origem nesse anúncio. Confirmar/refutar por: anúncio ativo com estoque normalizado refuta a hipótese; anúncio pausado ou esgotado confirma ruptura — nesse caso, registrar como variável confundidora para as próximas leituras de cancelamentos. Escalar se: não aplicável — ação direta da Yasmin.
• Yasmin: verificar reposição na expedição Budamix para o Kit 6 Canecas 250ml (Cross-Docking, 1 unidade no estoque — o próximo pedido zera e pode gerar cancelamento automático antes da reposição chegar). Por ser Cross-Docking, a Budamix controla a reposição (mais ágil que Full), mas o ML pode pausar o anúncio antes da chegada. Confirmar/refutar por: reposição disponível na expedição em 24h neutraliza o risco; ausência leva a cancelamento automático no próximo pedido. Escalar se: não aplicável — ação direta da Yasmin.

Dia analisado: 24/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmar que os 2 cancelamentos do dia vieram do Kit 6 Canecas Porcelana Tulipa
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou que o pacote não traz breakdown de cancelamentos por anúncio — correlação é hipótese, não fato
- **Agregado autorizado:** não
- **Tratamento aplicado:** prioridade formulada como verificação operacional ("verificar também se os 2 cancelamentos do dia têm origem nesse anúncio"), sem afirmação causal
- **Aparece na mensagem final:** sim, como checagem hipotética

---

- **Item bloqueado:** Afirmar migração de modalidade de envio (Cross-Docking → Full) no anúncio líder das Potes Vidro 5 Peças
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** L04 resolveu a divergência — um platform_item_id tem único logistic_type; o anúncio sempre foi Full; memória anterior misturou fontes; a "inversão de mix" da L03 é artefato de leitura anterior, não sinal sistêmico
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** omitido integralmente; nenhuma menção a inversão de mix ou migração de modalidade de envio na mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Tratar health=null nos anúncios do top como sinal saudável
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** health=null significa volume insuficiente para o ML calcular — zona cega, não confirmação positiva
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum anúncio com health=null recebeu qualificação positiva; análise referencia apenas os dois anúncios com health calculável (0,71 e 0,75)
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Recomendação de ajuste em ADS ML
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** ROAS 11x e ACOS 4,19% — campanha em zona de alta eficiência; regra operacional Lente 5 — campanha eficiente em curso é para observar, não para mexer
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** omitido; análise caracteriza a campanha como eficiente e posiciona o share alto como sintoma de orgânico deprimido, sem sugerir ajuste; nenhuma prioridade envolve ação em ADS
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Citação de MLBs técnicos (platform_item_id) na mensagem narrativa
- **Origem do bloqueio:** L05 Condensadora / regra estrutural L06
- **Motivo:** MLB serve apenas à rastreabilidade técnica interna; usar nome comercial no Slack
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** todos os produtos referenciados por slack_short_name ou nome comercial aprovado; nenhum MLB visível na mensagem
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`): nenhum aparece na mensagem Slack; usados apenas internamente para orientar linguagem e nuance.
- Insight 1 (classificação `fato`): escrito como afirmação direta, sem hedge — "O crescimento veio inteiro do ticket médio" — consistente com a classificação.
- Insights 2 e 3 (classificação `risco latente`): preservada linguagem de indício — "sugere que o ML está restringindo", "parece estar cobrindo", "parece ter sido oscilação", "parece ser forte o suficiente" — sem transformar hipótese estrutural em fato.
- Modalidade de envio omitida da seção VISÃO: `fulfillment_mix_yesterday_top10` cobre 47 dos 99 pedidos do dia (~47%), abaixo do threshold operacional; Condensadora não autorizou exibição com ressalva de cobertura nessa seção — omitido conforme regra da L06.
- Atribuição de Yasmin como responsável nas três prioridades: L05 não atribui responsável; L06 aplica regra fixa de responsável para Mercado Livre.
- Escalonamento para Kobe mantido apenas na prioridade 1, onde L05 indicou `escalar_se` explicitamente; prioridades 2 e 3 com "não aplicável — ação direta da Yasmin", conforme L05.
- **Top Produtos — tradução de nomes (item a item):**
  - IMB501P — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - KIT4YW1050 — usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico)
  - IMB501V — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - CLR002 — usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
  - IMB501C — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- Análise — aggregate do anúncio MLB3288536143: referenciado como "Potes Vidro 5 Peças" (sem cor de tampa) para representar o anúncio único com as três variações; escolha consistente com o prefixo comum dos três `slack_short_names` (IMB501P/V/C); não há `slack_short_name` de nível familiar — inferência mínima necessária e conservadora.
- Análise — divergência cross-layer insight 2: L05 escreve "os dois campeões em Full" sem nomear; L06 nomeia como "Potes Vidro 5 Peças" e "Kit 4 Potes 1050ml" — correspondência com `slack_short_name` de IMB501 (aggregate) e KIT4YW1050 respectivamente; nomes registrados.
- Prioridade 1 — nome: "Kit 6 Canecas Lisas 200ml" — `slack_short_name` de CLR002 (mapeamento canônico); consistente com L05.
- Prioridade 2 — nome: "Kit 6 Canecas Porcelana Tulipa" — produto ausente do `top_products` do pacote (MLB6167272090 não está entre os 10 itens); sem `slack_short_name` mapeado; usado nome de memória/L05 como fallback raríssimo por ausência de alternativa disponível.
- Prioridade 3 — divergência cross-layer: L05 usa "Kit 6 Canecas 250ml Canelada"; L06 usa "Kit 6 Canecas 250ml" — padronização com `slack_short_name` aprovado para K6CAN250 (atributo "Canelada" não consta no nome canônico manual).
- Sem insight de enchimento: Condensadora entregou 3 insights, todos preservados, nenhum adicionado.
- Sem prioridade inventada: 3 prioridades da Condensadora preservadas sem acréscimo ou supressão.
- Cancelamentos apresentados como contagem simples (2) na seção VISÃO — sem valor monetário associado, consistente com a natureza do campo `metrics.cancelamentos`.