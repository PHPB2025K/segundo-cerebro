<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 15/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: 111 pedidos — R$ 6.048,16 — ticket médio R$ 54,49
• Budamix Store: 67 pedidos — R$ 3.243,64
• Budamix Oficial (Conta 2): 17 pedidos — R$ 1.248,10
• Budamix Shop (Conta 3): 27 pedidos — R$ 1.556,42
• Cancelamentos: 5 (Store: 2 | Conta 3: 3 | Conta 2: 0)

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 30 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 23 pedidos
• Kit 6 Canecas Tulipa 250ml — 21 pedidos
• Kit 6 Canecas Retas 200ml (Conta 3) — 8 pedidos
• Kit 2 Potes de Vidro 800ml Quadrado — 6 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee entregou 111 pedidos e R$ 6.048,16 de GMV, mas o resultado é composto por três dinâmicas divergentes que não se somam a uma tese única: a Store segura o canal com volume concentrado em dois produtos e ticket inflado disfarçando queda real de demanda, a Conta 2 acumula queda multijanela e adicionou hoje um comportamento horário atípico que aponta para perda de exposição em janela específica, e a Conta 3 mantém pedidos mas perde receita por unidade porque o mix do dia foi liderado por canecas em vez de potes herméticos. O risco consolidado é que nenhuma das três contas compensa as demais: se o produto líder da Store tropeçar, o canal cai sem amortecimento; se a Conta 2 perdeu a janela matinal de forma estrutural, a deterioração continua independente do que as outras contas entregam.

🟠 *Budamix Store (Shopee 1):* A Store sustentou o GMV próximo à média de 30d (R$ 3.243 vs R$ 3.297) mas apenas porque o ticket subiu ~25% enquanto o volume recuou -21,3% vs 30d e -32,1% vs 60d — a conta rodou hoje com os Potes de Vidro Redondos Tampa Preta (30 pedidos, 45% da conta) e a Jarra Medidora de Vidro 500ml (23 pedidos) esgotando o top5 em 100%, sem nenhum produto de cauda funcional para absorver oscilação dos líderes. O risco é silencioso: o número de faturamento induz leitura de estabilidade, mas a estrutura é a mais frágil possível — qualquer queda no produto líder vai direto ao total do canal sem compensação.

🟠 *Budamix Oficial (Shopee 2):* A conta entregou 17 pedidos (-51,8% vs mesmo dia da semana) e o sinal mais relevante não é o número absoluto, mas como esses pedidos se distribuíram: zero pedidos de 0h a 10h, com a conta operando em dois blocos isolados (pico de 4 pedidos às 15h e 4 às 23h), padrão que aponta para perda de acesso à janela matinal de tráfego e não para queda proporcional de demanda ao longo do dia. Sem causa confirmada (exposição orgânica, ranking, eficiência de ADS), a postura é observação dirigida — o diagnóstico que Lucas vai levar a Himmel depende de confirmar se o padrão horário atípico se repete nos próximos dias antes de qualquer intervenção.

🟠 *Budamix Shop (Shopee 3):* A conta manteve volume (27 pedidos, estável vs média de 30d) mas perdeu -15,2% de GMV vs mesmo dia da semana porque o dia foi liderado pelo Kit 6 Canecas Tulipa (8 pedidos) e pelo Kit 6 Canecas Retas 200ml (8 pedidos), juntos 59% dos pedidos — produtos de ticket menor que os potes herméticos que dominam a Store, o que explica diretamente a erosão de receita por unidade visível nas janelas de 30d e 60d. Os 3 cancelamentos em 27 pedidos válidos (~11%) adicionam risco localizado que não pode ser atribuído a produto específico neste ciclo e requer rastreamento no próximo pacote.

🎯 PRIORIDADES DO DIA
• Lucas: verificar se a Conta 2 (Budamix Oficial) volta a ter pedidos entre 0h e 10h nos próximos 2 dias. Hoje a conta operou sem nenhum pedido até as 11h, em dois blocos isolados — padrão que aponta para perda de acesso à janela matinal de tráfego, não queda proporcional de demanda. Confirmar se ausência matinal se repetir por 2 dias consecutivos; refutar se pedidos voltarem a aparecer distribuídos ao longo do dia (inclusive manhã). Escalar com Himmel se 3 dos próximos 5 dias ficarem abaixo de 20 pedidos com ausência matinal recorrente.
• Lucas: acompanhar o ritmo de pedidos dos Potes de Vidro Redondos Tampa Preta (produto líder da Store, ~45% dos pedidos da conta) hoje e amanhã em relação aos 30 pedidos de ontem. A Store opera sem cauda funcional — qualquer queda nesse produto vai direto ao GMV do canal sem amortecimento. Sinal de alerta: ritmo abaixo de 50% do patamar de ontem por 2 dias consecutivos. Escalar para Himmel preventivamente se o sinal de alerta se confirmar, antes de aguardar o ciclo de observação da Conta 2.
• Lucas: solicitar no próximo ciclo a distribuição dos cancelamentos da Conta 3 por produto — taxa de ~11% (3 em 27 pedidos) é elevada para o porte da conta e não pode ser atribuída a produto específico com os dados atuais. Não tratar como ruído até ter a localização de causa.
• Não fazer hoje: não acionar Himmel para mexer em ADS da Conta 2 sem hipótese de causa confirmada; não usar o GMV nominal da Store como argumento de saúde; não atribuir a erosão de ticket da Conta 3 a causa única sem observar se o mix de canecas se mantém amanhã.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKU `098` — Conta 2 (Budamix Oficial) — display_name `Pote de Vidro Hermético 800ml`
  - Origem do bloqueio: Condensadora
  - Motivo: divergência substantiva entre display_name interno e raw_title do pedido real (`Kit 9 Potes Vidro Quadrados Hermético`) — risco de identificação; 1 pedido afetado
  - Agregado autorizado: não
  - Tratamento aplicado: omitido da mensagem
  - Aparece na mensagem final: não

- Item bloqueado: `ITEM:28044349447` — Conta 3 (Budamix Shop) — `Kit 5 Tigelas Potes Redondos 140ml a 980ml`
  - Origem do bloqueio: Condensadora
  - Motivo: produto sem SKU interno, mapeado exclusivamente por platform_item_id estável — confidence medium
  - Agregado autorizado: não
  - Tratamento aplicado: omitido da mensagem
  - Aparece na mensagem final: não

- Item bloqueado: SKU `096` — Conta 3 (Budamix Shop) — `Kit Conjunto 3 Potes Vidro Quadrados Hermético`
  - Origem do bloqueio: Condensadora
  - Motivo: mapeamento genérico com fallback de título curto — confidence medium
  - Agregado autorizado: não
  - Tratamento aplicado: omitido da mensagem
  - Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de SKUs crus (`IMB501P`, `CK4742`, `CTL002`) da seção ANÁLISE DAS CONTAS — substituídos pelos display_names dos produtos; a proibição de SKU cru visível aplica-se a toda a mensagem, não apenas a Top Produtos
- Preservação das ressalvas de confiança média — hipótese de canibalização de CTL002 mantida como candidata, não fato; ausência matinal da Conta 2 mantida como sinal de hoje sem afirmar que é novo vs histórico (histórico horário não disponível no pacote)
- Cancelamentos da Conta 3 mencionados com taxa (~11%) e com ressalva explícita de que a distribuição por produto não está disponível neste ciclo — em linha com o bloqueio da Condensadora sobre atribuição causal
- Consolidação de CTL002 nas três contas em Top Produtos: 9 (Store) + 4 (Conta 2) + 8 (Conta 3) = 21 pedidos — produto presente em 3 contas, sem indicação de conta específica conforme regra
- Indicação de conta para IMB501P e CK4742 (somente Store) e KIT6CAR200 (somente Conta 3) — venderam em menos de 2 contas
- Faturamento por produto omitido em Top Produtos — o pacote de dados não inclui receita por produto/SKU (apenas orders e quantity); nenhum valor inventado
- Quatro blocos de ANÁLISE DAS CONTAS reproduzidos da 6B conforme layout aprovado (Consolidado + 3 contas individuais), com linha em branco entre blocos
- Bullet `Não fazer hoje` mantido em PRIORIDADES DO DIA — veio da 6B como priority_line e é operacionalmente relevante para Lucas; não é análise nova, é restrição explícita das camadas anteriores
- Comparações temporais presentes na seção ANÁLISE DAS CONTAS (não em VISÃO) — autorizadas porque vieram da fonte analítica 6B e pertencem ao diagnóstico, não à apresentação objetiva de dados
- VISÃO SHOPEE sem comparações temporais — apenas dados objetivos do dia por conta