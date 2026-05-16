<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 15/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: 111 pedidos / R$ 6.048,16 / ticket médio R$ 54,49 / 5 cancelamentos
• Budamix Store: 67 pedidos / R$ 3.243,64
• Budamix Oficial (Conta 2): 17 pedidos / R$ 1.248,10
• Budamix Shop (Conta 3): 27 pedidos / R$ 1.556,42

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 30 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 23 pedidos
• Kit 6 Canecas Tulipa 250ml — 21 pedidos
• Kit 6 Canecas Retas 200ml (Conta 3) — 8 pedidos
• Kit 2 Potes de Vidro 800ml Quadrado — 6 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee fechou 111 pedidos / R$ 6.048,16 com arquitetura interna desequilibrada: a Store carregou 60% do volume sustentando o canal via elevação de ticket enquanto a Oficial 2 colapsou para 15% com padrão horário de ausência de impressões, e a Shop 3 manteve volume com compressão silenciosa de valor — o número agregado parece aceitável, mas as três contas não operam em complementaridade: há colapso localizado (Oficial 2), degradação de valor silenciosa (Shop 3) e dependência extrema de dois produtos sem amortecedor (Store), e agir nas três como bloco ou não agir em nenhuma seriam igualmente errados.

🟠 *Budamix Store (Shopee 1):* A Store entregou R$ 3.243,64 com volume −21% abaixo do 30d mas ticket +25% acima, sustentada por Tampa Preta (30 pedidos) e Jarra Medidora 500ml (23 pedidos) que juntos respondem por 79% dos 67 pedidos válidos — top5 cobre 100% do volume, sem cauda operacional; a conta performou no dia, mas a tendência de volume nas janelas longas (−32% vs 60d) indica que o patamar atual não é recuperação, é sustentação precária via ticket elevado em dois campeões sem redundância.

🟠 *Budamix Oficial (Shopee 2):* A Oficial 2 entregou apenas 17 pedidos / R$ 1.248,10 com queda uniforme em todas as janelas (−51,8% vs mesmo dia da semana, −46,7% vs 30d) e distribuição horária que revela ausência de tráfego em 15 das 24 horas — incluindo zero pedidos no bloco inteiro de 0h–10h — o que aponta para problema de exposição ou ADS desta conta, não de demanda fraca: os poucos pedidos que chegaram converteram em ticket R$ 73,42 (+22,9% vs 30d), evidenciando que quem chegou comprou bem, mas simplesmente não chegou.

🟠 *Budamix Shop (Shopee 3):* A Shop 3 sustentou volume no patamar de 30d (27 pedidos), mas comprimiu ticket para R$ 57,65 (−15,4% vs 30d, −11,3% vs 60d) pela rotação de mix para canecas — Kit 6 Canecas Tulipa 250ml e Kit 6 Canecas Retas 200ml juntos respondem por 59% dos pedidos, produtos de menor valor unitário que os potes herméticos —, e acumulou 3 cancelamentos em 27 pedidos (~11%), taxa superior à Store (3%) e à Oficial 2 (zero); o volume estável mascara compressão de valor já em curso no bimestre e um sinal de cancelamento sem causa identificada por produto.

🎯 PRIORIDADES DO DIA
• *[Hoje — urgente]* Lucas verifica com Himmel o status de ADS e exposição da Oficial 2 (Conta 2): a distribuição horária com 15 horas zeradas — incluindo todo o bloco 0h–10h — é evidência de ausência de impressões, não de demanda fraca; diagnóstico de causa antes de qualquer decisão de campanha. Se ADS e exposição estiverem normais, o problema migra para operacional (listing, estoque, reputação) e Lucas investiga por esse caminho.
• *[Hoje]* Lucas confirma disponibilidade de estoque de Tampa Preta e Jarra Medidora 500ml para os próximos 5–7 dias: esses dois produtos respondem por 79% dos pedidos da Store e não há amortecedor no mix atual — ruptura de qualquer um derruba o GMV da conta sem recuperação imediata.
• *[Amanhã]* Lucas registra e reporta o volume de pedidos da Oficial 2 na sexta-feira: referência de controle é 28+ pedidos para classificar hoje como outlier ou abaixo de 25 para confirmar deterioração em segundo ciclo e acionar diagnóstico ativo.
• *[Investigar]* Lucas apura a causa dos 3 cancelamentos da Shop 3: taxa de ~11% é a mais alta entre as três contas e a origem por produto não está identificada — se concentrados em um SKU, é problema de listing ou estoque naquele item específico, não evento pontual.
• *[Não fazer]* Não acionar mudança de ADS em nenhuma das três contas sem diagnóstico concluído da Oficial 2: subir verba sobre problema operacional queima recurso sem recuperar volume, e mexer na Store ou na Shop 3 ao mesmo tempo sem evidência transversal aumenta risco de canibalização entre anúncios do mesmo produto — Kit 6 Canecas Tulipa 250ml já vende em anúncios distintos nas três contas simultaneamente.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: Kit 5 Tigelas Potes Redondos 140ml a 980ml (ITEM:28044349447, Shop 3)
- Origem do bloqueio: Granular
- Motivo: confiança média — ausência de raw_sku, mapeado apenas por platform_item_id estável
- Agregado autorizado: não
- Tratamento aplicado: omitido (1 pedido, não alcança top 5 consolidado; bloqueio sem agregado autorizado)
- Aparece na mensagem final: não

- Item bloqueado: SKU 096 — Kit Conjunto 3 Potes Vidro Quadrados (Shop 3)
- Origem do bloqueio: Granular
- Motivo: confiança média — SKU genérico numérico, mapeado por title fallback
- Agregado autorizado: não
- Tratamento aplicado: omitido (1 pedido, não alcança top 5 consolidado; bloqueio sem agregado autorizado)
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de shop_id técnico (`860803675`) da análise da Oficial 2 — substituído por "desta conta"; IDs técnicos não visíveis no Slack conforme regra estrutural
- Remoção de raw SKUs (`IMB501P`, `CK4742`) da análise da Store — substituídos pelos display names "Tampa Preta" e "Jarra Medidora 500ml"; SKU cru não visível no Slack conforme regra estrutural
- Remoção de raw SKUs (`CTL002`, `KIT6CAR200`) da análise da Shop 3 e da prioridade — substituídos por "Kit 6 Canecas Tulipa 250ml" e "Kit 6 Canecas Retas 200ml"; mesma regra
- Receita por produto omitida do Top Produtos — dado de faturamento por SKU não presente no pacote validado (Layer 0 top_products contém apenas orders e quantity); não houve estimativa ou inferência; formato adaptado para pedidos apenas
- CTL002 consolidado nas 3 contas: Store 9 + Oficial 2 4 + Shop 3 8 = 21 pedidos — mesma variação vendável confirmada com confiança alta nas três contas; sem indicação de conta pois vendeu em 3 contas
- KIT2YW800SQ consolidado: Store 2 + Oficial 2 1 + Shop 3 3 = 6 pedidos — mesma variação confirmada com confiança alta; sem indicação de conta
- Conta indicada no Top Produtos apenas para Tampa Preta (Store, única conta) e Kit 6 Canecas Retas 200ml (Conta 3, única conta)
- Cabeçalho da seção de análise adaptado para `🔍 ANÁLISE DAS CONTAS` conforme addendum v3.1 regra 7.6 — 6B presente, layout de 4 blocos obrigatório
- Fallback de 05-condensadora ignorado — fonte analítica obrigatória para Lucas/Shopee é 06b-shopee-consolidator conforme addendum v3.1; 06b presente e válida
- Hipótese de confiança média da Oficial 2 (ticket elevado = viés de seleção vs qualidade de demanda preservada) preservada implicitamente na análise: o texto da 06b já carrega a nuance ("quem chegou comprou bem, mas simplesmente não chegou") sem cravar uma das pontas; mantida sem alteração de sentido
- Sem decisões ambíguas de formatação além das registradas acima