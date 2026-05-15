<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 12/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: 118 pedidos — R$ 5.378,44 — ticket médio R$ 45,58
• Budamix Store: 76 pedidos — R$ 2.813,88 (10 cancelamentos)
• Budamix Oficial (Conta 2): 23 pedidos — R$ 1.296,64 (2 cancelamentos)
• Budamix Shop (Conta 3): 19 pedidos — R$ 1.267,92 (1 cancelamento)

🏆 TOP PRODUTOS SHOPEE
• Conjunto de 5 Potes de Vidro Redondos — 33 pedidos
• Jarra Medidora de Vidro 500ml com Alça (Budamix Store) — 29 pedidos
• Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida — 24 pedidos
• Kit 6 Canecas Porcelana 200ml Reta Lisa Coloridas — 10 pedidos
• Kit 5 Potes de Vidro Redondos Translúcidos (Budamix Oficial) — 9 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* As três contas Shopee apresentam queda convergente de volume com ticket médio estável em todas as janelas — o problema é de exposição ou tráfego, não de produto ou precificação — mas a tese de 'causa única transversal' está comprometida pela sobreposição confirmada de produtos entre as contas: as canecas tulipa venderam nas três contas hoje e o produto líder de potes foi dominado pela Store, o que coloca canibalização interna como hipótese em aberto paralela ao problema de exposição.

🟠 *Budamix Store (Shopee 1):* A Store sustenta 64% do volume Shopee e está no menor recuo relativo no curto prazo, mas a leitura de 'conta acomodada' é prematura: 10 cancelamentos não diagnosticados representam uma taxa bruta de ~11,6% sobre os dois produtos que respondem por 76% do volume da conta — enquanto esse dado não tiver origem confirmada, o risco de fragilidade ativa nos próprios campeões que sustentam o canal não pode ser descartado.

🟠 *Budamix Oficial (Shopee 2):* A Conta 2 está em queda ativa no curto prazo (-26% vs 7d), diferente da Store que acomodou, e apresentou distribuição de horário atípica — concentração em 7h e 23h com baixo aproveitamento da janela 19h–22h — o que sugere que os anúncios não estavam entregando no período de maior intenção de compra; o diagnóstico não pode ser confirmado sem histórico comparável de horário, mas o sinal reforça a prioridade de checar campanha e exposição antes de qualquer ajuste de verba.

🟠 *Budamix Shop (Shopee 3):* A Conta 3 tem o pior recuo relativo do canal (-51% vs mesmo dia da semana, -45% vs 60d) com mix concentrado em dois produtos de canecas que também vendem na Store e na Conta 2 — o problema pode ser de exposição isolada, de canibalização pela Store nos produtos sobrepostos, ou os dois em paralelo; sem histórico granular de produto por semana, não é possível separar as causas, mas a profundidade da queda já não é compatível com acomodação.

🎯 PRIORIDADES DO DIA
• Lucas: verificar status dos cancelamentos da Store (10 cancelamentos, ~11,6% da conta de maior volume) — confirmar se estão pulverizados entre pedidos distintos ou concentrados nos potes redondos e na jarra medidora. Se concentrados nos campeões, escalar imediatamente para diagnóstico diferenciado da conta.
• Lucas: checar se houve mudança de campanha, verba ou posicionamento ADS nas Contas 2 e 3 nos últimos 5–7 dias — e verificar se os anúncios dessas contas estão concorrendo com os da Store nos mesmos produtos (canecas tulipa e potes redondos), porque a ação certa muda completamente dependendo da causa: problema externo de exposição aponta para alinhamento com Himmel, canibalização interna aponta para revisão de estratégia por conta antes de qualquer ajuste de verba. Escalar para Himmel se Contas 2 e 3 não reagirem nos horários de pico nos próximos 2 dias consecutivos.
• Lucas: não acionar Himmel para aumento de verba em nenhuma das três contas antes de ter os dois pontos acima respondidos — ampliar verba sobre operação com canibalização interna ativa e cancelamentos não diagnosticados na conta líder pode amplificar custo sem recuperar volume e encobrir as causas reais.

Dia analisado: 12/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs técnicos — `CTL002` (Canecas Tulipa)
  - Origem do bloqueio: Condensadora (campo "o_que_nao_pode_ir_para_slack")
  - Motivo: SKU técnico visível proibido para Slack
  - Agregado autorizado: sim — "canecas tulipa" (infere-se da descrição funcional do produto; a Condensadora autorizou uso de descrição funcional no lugar de códigos internos)
  - Tratamento aplicado: substituído por "canecas tulipa" e "Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida" no Top Produtos
  - Aparece na mensagem final: sim, como agregado descritivo

- Item bloqueado: SKUs técnicos — `IMB501P_T` (Potes Redondos)
  - Origem do bloqueio: Condensadora (campo "o_que_nao_pode_ir_para_slack")
  - Motivo: SKU técnico visível proibido para Slack
  - Agregado autorizado: sim — "produto líder de potes" / "potes redondos" / "Conjunto de 5 Potes de Vidro Redondos"
  - Tratamento aplicado: substituído por descrição funcional em análise e título de produto no Top Produtos
  - Aparece na mensagem final: sim, como descrição funcional e título do produto

- Item bloqueado: SKUs técnicos — `IMB501C_T`, `CK4742_B`, `KIT6CAR200`, `KIT4YW800SQ_T`, demais
  - Origem do bloqueio: Condensadora (campo "o_que_nao_pode_ir_para_slack")
  - Motivo: SKU técnico visível proibido para Slack
  - Agregado autorizado: sim — títulos dos produtos usados no Top Produtos; não citados na análise
  - Tratamento aplicado: substituídos por títulos descritivos no Top Produtos; não mencionados nominalmente na análise
  - Aparece na mensagem final: sim, como títulos de produto no Top Produtos apenas

- Item bloqueado: taxa de cancelamento como número cru sem contexto de diagnóstico
  - Origem do bloqueio: Condensadora (campo "o_que_nao_pode_ir_para_slack")
  - Motivo: pode soar alarmista sem a ressalva de inconclusivo
  - Agregado autorizado: sim — a própria Condensadora e a 6B trouxeram a taxa com contexto ("10 cancelamentos, ~11,6% da conta de maior volume… confirmar se estão pulverizados ou concentrados")
  - Tratamento aplicado: taxa incluída com contexto exato da 6B, mantendo ressalva de diagnóstico em aberto
  - Aparece na mensagem final: sim, com contexto completo

- Item bloqueado: afirmação de que a Store está estável ou acomodada sem ressalva dos cancelamentos
  - Origem do bloqueio: Condensadora
  - Motivo: leitura prematura que pode induzir ação errada
  - Tratamento aplicado: Store descrita como "menor recuo relativo no curto prazo" + ressalva dos cancelamentos não diagnosticados, preservando nuance exata da 6B
  - Aparece na mensagem final: não como afirmação de estabilidade; sim com ressalva

- Item bloqueado: hipótese de comportamento de horário atípico na Conta 2 como anomalia confirmada
  - Origem do bloqueio: Condensadora
  - Motivo: sem histórico comparável para classificar como desvio ou padrão recorrente
  - Tratamento aplicado: preservada como "sugere" e "o diagnóstico não pode ser confirmado sem histórico comparável de horário"
  - Aparece na mensagem final: sim, como hipótese com ressalva de inconclusividade

---

### Decisões de formatação

- Remoção de metadados internos ("base: Operacional + Granular", "base: Estratégica + Granular", etc.) da análise — regra da Slack Writer; teses e nuances preservadas integralmente
- Substituição de `CTL002` por "canecas tulipa" / "Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida" — SKU técnico bloqueado; descrição funcional autorizada pela Condensadora
- Substituição de `IMB501P_T` por "potes redondos" / "produto líder de potes" / "Conjunto de 5 Potes de Vidro Redondos" — mesma regra
- Receita por produto omitida do Top Produtos — dado não disponível no pacote (top_products contém apenas quantity, não revenue por item); impossível calcular sem inventar; registrado como limitação de dado, não como bloqueio analítico
- Consolidação de `CTL002` nas 3 contas (7+8+9=33... aguarda: Store 7 + Conta 2 8 + Conta 3 9 = 24 pedidos) — mesmo SKU físico em três listagens distintas confirmado pela Granular; apresentado como produto único no ranking, sem indicador de conta (vendeu em 3 das 3 contas)
- Consolidação de `KIT6CAR200` na Conta 2 (2) e Conta 3 (8) = 10 pedidos — mesmo SKU em 2 contas; por regra, sem indicador de conta (vendeu em 2+ contas)
- Indicador de conta aplicado à Jarra Medidora (`CK4742_B`): vendeu exclusivamente na Budamix Store — regra: indicar conta quando produto vendeu em menos de 2 contas
- Indicador de conta aplicado ao Kit 5 Potes Translúcidos (`IMB501C_T`): vendeu exclusivamente na Budamix Oficial — mesma regra
- Percentuais de queda (-26% vs 7d, -51% vs mesmo dia da semana, -45% vs 60d) preservados na análise — vieram explicitamente nos analysis_lines da 6B; não são inserção própria da Slack Writer
- Conectivo "mas" preservado em todas as ocorrências (Consolidado, Store) — proibição expressa de trocar "mas" → "e"
- "sugere" preservado na análise da Conta 2 para a hipótese de horário — confiança baixa confirmada pela Condensadora; proibido transformar em fato
- Prioridade 3 (não acionar Himmel) mantida como bullet afirmativo de restrição — veio explicitamente da 6B como priority_line; não é inserção própria