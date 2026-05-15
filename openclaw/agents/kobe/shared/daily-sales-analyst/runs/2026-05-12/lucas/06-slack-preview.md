<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 12/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Consolidado: 118 pedidos — R$ 5.378,44 — ticket médio R$ 45,58 — 13 cancelamentos
- Budamix Store: 76 pedidos — R$ 2.813,88 — 10 cancelamentos
- Budamix Oficial (Conta 2): 23 pedidos — R$ 1.296,64 — 2 cancelamentos
- Budamix Shop (Conta 3): 19 pedidos — R$ 1.267,92 — 1 cancelamento

🏆 TOP PRODUTOS SHOPEE
- Conjunto de 5 Potes de Vidro Redondos — 33 unidades
- Jarra Medidora De Vidro 500ml (Budamix Store) — 29 unidades
- Canecas Tulipa 250ml Porcelana Coloridas — 24 unidades
- Canecas Porcelana 200ml Reta Lisa Coloridas — 10 unidades
- Kit 5 Potes de Vidro Redondos Translúcidos (Conta 2) — 9 unidades

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee fechou o dia com queda real e sincronizada nas 3 contas — o sinal atravessa todas as janelas (30d, 60d, mesmo dia da semana) sem compensação entre contas, o que descarta canibalização e aponta para erosão de plataforma/categoria; o risco imediato, porém, não é o volume em si, é a qualidade operacional da conta que ainda sustenta o canal: a Budamix Store responde por 64% do GMV e 76% dos cancelamentos, e enquanto o diagnóstico desses cancelamentos não estiver fechado, a estabilização aparente da conta principal é uma armadilha de leitura.

🟠 *Budamix Store (Shopee 1):* É a conta de volume e o principal risco operacional do dia — 76 pedidos alinhados à média de 7d sugerem acomodação em novo piso, mas 10 cancelamentos com taxa de 11,6% (2,3x a taxa da Conta 3) confirmam que o problema é localizado nessa conta, não evento de plataforma; sem breakdown por produto, a causa raiz está em aberto, e qualquer leitura de estabilização saudável é prematura enquanto quase 1 em cada 8 tentativas cancela.

🟠 *Budamix Oficial (Shopee 2):* É a conta de ticket médio mais alto (R$ 56,38 vs R$ 37 da Store) e explica faturamento desproporcional ao seu volume — mas está em declínio ativo em todas as janelas, incluindo 7d (-26%), sem sinal de acomodação; o padrão horário atípico do dia (8 pedidos em 7h+23h, apenas 7 no pico 19-22h) não pode ser classificado como desvio ou recorrência por ausência de histórico, mas é o sinal mais relevante a confirmar amanhã antes de qualquer conversa com Himmel sobre exposição nessa conta.

🟠 *Budamix Shop (Shopee 3):* É a conta de maior ticket (R$ 66,73) e menor volume, operando como canal mono-segmento — 81% dos itens saíram de 2 tipos de canecas (Tulipa e Reta Lisa), e a queda de -45% vs 60d e -51% vs mesmo dia da semana, com ticket estável, confirma que o problema é exclusivamente de volume/exposição nesses dois produtos; disponibilidade no dia está confirmada (17 unidades vendidas), mas erosão de ranking ou posicionamento nesses listings permanece hipótese aberta e é o único vetor que explica uma queda dessa magnitude sem deterioração de produto.

🎯 PRIORIDADES DO DIA
- Lucas (hoje): Checar a operação da Budamix Store para entender a origem dos cancelamentos — 10 cancelamentos sobre 76 pedidos válidos (11,6%), concentrados nessa conta e não em evento de plataforma; causa raiz ainda em aberto. Escalar para Kobe se ≥8 cancelamentos se repetirem amanhã, antes de qualquer decisão de ADS ou mix.
- Lucas (amanhã): Observar Budamix Oficial no horário 19-22h — hoje a conta teve apenas 7 pedidos no pico convencional e 8 em 7h+23h; padrão atípico confirmado para o dia, mas sem histórico para classificar. Se padrão se confirmar por 2 dias consecutivos, alinhar com Himmel sobre exposição dessa conta no horário nobre.
- Não acionar Himmel para realocar ou aumentar verba em nenhuma das 3 contas agora — a natureza da queda ainda não está determinada; o diagnóstico dos cancelamentos da Store precisa vir primeiro, antes de qualquer intervenção de mídia.

Dia analisado: 12/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: breakdown de cancelamentos por produto/SKU
- Origem do bloqueio: Condensadora
- Motivo: dado indisponível no pacote — cancelamentos reportados apenas como total agregado por conta, sem itemização por SKU ou platform_item_id
- Agregado autorizado: sim — "10 cancelamentos sobre 76 pedidos válidos" e "concentrados nessa conta"
- Tratamento aplicado: mencionado apenas em nível de conta, conforme autorizado; causa por produto omitida
- Aparece na mensagem final: sim, como agregado de conta

---

- Item bloqueado: SKUs técnicos (IMB501P_T, CK4742_B, CTL002, KIT6CAR200, etc.) e platform_item_ids
- Origem do bloqueio: Condensadora
- Motivo: IDs técnicos internos não entram no Slack
- Agregado autorizado: sim — nomes comerciais dos produtos usados no lugar dos códigos
- Tratamento aplicado: substituídos por títulos descritivos dos produtos em Top Produtos e em referências analíticas
- Aparece na mensagem final: não como SKU; sim como nome de produto

---

- Item bloqueado: hipótese de canibalização entre listings do mesmo produto nas 3 contas
- Origem do bloqueio: Condensadora
- Motivo: hipótese plausível estruturalmente, sem dado de tráfego para sustentar
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem
- Aparece na mensagem final: não

---

- Item bloqueado: classificação do padrão horário da Conta 2 como "perda de exposição confirmada"
- Origem do bloqueio: Condensadora
- Motivo: hipótese, não fato; sem série histórica horária para confirmar desvio ou recorrência
- Agregado autorizado: sim — "padrão horário atípico do dia... não pode ser classificado como desvio ou recorrência por ausência de histórico"
- Tratamento aplicado: preservada como hipótese com linguagem de indício; mencionado como sinal a confirmar amanhã
- Aparece na mensagem final: sim, como hipótese aberta com condição de confirmação

---

- Item bloqueado: erosão de ranking ou preço relativo dos produtos de canecas da Conta 3
- Origem do bloqueio: Condensadora
- Motivo: hipótese aberta sem dado de listing ou impressões; disponibilidade confirmada no dia
- Agregado autorizado: sim — "hipótese aberta" preservada textualmente
- Tratamento aplicado: mantida como hipótese aberta na análise da Conta 3
- Aparece na mensagem final: sim, como hipótese aberta e não como diagnóstico fechado

---

### Decisões de formatação

- Remoção das tags `— base: Operacional + Granular`, `— base: Estratégica + Operacional` dos insights — metadados internos do pipeline, não entram no Slack
- Remoção das marcações `*[HOJE — Lucas]*`, `*[AMANHÃ — Lucas]*`, `*[NÃO FAZER]*` dos bullets de prioridade — convertidas para formato `Lucas (hoje):`, `Lucas (amanhã):` e parágrafo de não-ação, conforme template aprovado
- "2 SKUs de canecas (Tulipa + Reta Lisa)" → "2 tipos de canecas (Tulipa e Reta Lisa)" — remoção de jargão interno "SKU" substituída por linguagem externa equivalente; sentido analítico preservado
- Faturamento por produto omitido do Top Produtos — o pacote validado não contém revenue por produto; fabricar valores quebraria a regra de não inferir dados; listagem feita apenas com unidades
- CTL002 (Tulipa 250ml): consolidado nas 3 contas (7+8+9 = 24 unidades); conta não indicada por vender em 3 contas
- IMB501P_T (Potes Redondos 5 pçs): consolidado nas 3 contas (31+1+1 = 33 unidades); conta não indicada por vender em 3 contas
- CK4742_B (Jarra Medidora 500ml): Budamix Store indicada — vendeu em 1 conta apenas
- IMB501C_T (Potes Translúcidos 5 pçs): Conta 2 indicada — vendeu em 1 conta apenas
- KIT6CAR200 (Canecas Reta Lisa 200ml): consolidado nas 2 contas (2+8 = 10 unidades); conta não indicada por vender em 2 contas
- Título da seção analítica: "ANÁLISE DAS CONTAS" (plural) — 06b presente e com os 4 blocos; conforme regra 7.6
- Padrão horário da Conta 2 preservado como hipótese com linguagem de indício ("não pode ser classificado... por ausência de histórico") — bloqueio de Condensadora respeitado
- Hipótese de erosão de ranking da Conta 3 preservada como aberta — disponibilidade confirmada, causa não rastreável; nuance da Condensadora intacta
- Percentuais numéricos convertidos para padrão PT-BR com vírgula: "11,6%", "-26%", "-45%", "-51%", "2,3x" — conforme padrão numérico obrigatório; valores já vinham corretos da 06b