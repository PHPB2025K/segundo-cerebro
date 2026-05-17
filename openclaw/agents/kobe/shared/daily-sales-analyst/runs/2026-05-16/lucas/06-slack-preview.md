<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 16/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: 99 pedidos — R$ 4.976,92 — ticket médio R$ 50,27
• Budamix Store (Shopee 1): 57 pedidos — R$ 2.353,85
• Budamix Oficial (Shopee 2): 22 pedidos — R$ 1.582,54
• Budamix Shop (Shopee 3): 20 pedidos — R$ 1.040,53
• Cancelamentos: 1 (Conta 2)

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 31 pedidos (Store)
• Kit 6 Canecas Tulipa 250ml — 11 pedidos (Store: 6 + Conta 2: 4 + Conta 3: 1)
• Jarra Medidora de Vidro 500ml — 11 pedidos (Store)
• Kit 2 Potes de Vidro 800ml Quadrado — 9 pedidos (Store: 2 + Conta 3: 7)
• Kit 4 Potes de Vidro 800ml Quadrado — 8 pedidos (Conta 2: 7 + Conta 3: 1)
• Kit 6 Canecas Retas 200ml — 5 pedidos (Conta 3)
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 5 pedidos (Conta 2)

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee entregou 99 pedidos e R$ 4.976,92 de GMV com as três contas em queda simultânea vs 30d e 60d, o que confirma movimento sistêmico de canal — mas o diagnóstico correto exige separação: Store e Oficial-2 estão em acomodação de patamar com ticket compensando parcialmente o volume perdido, enquanto Shop-3 comprime volume e ticket ao mesmo tempo e sem atividade noturna, configurando perfil de queda real distinto das outras duas. Tratar o canal como bloco homogêneo leva à ação errada.

🟠 *Budamix Store (Shopee 1):* A Store foi o motor de volume do canal (57 de 99 pedidos), mas o resultado não foi da conta — foi de um produto: o Conjunto 5 Potes Redondos Tampa Preta (IMB501P) carregou 31 dos 57 pedidos (54,4%), com top3 em 84,2%, e sem nenhum segundo vetor com capacidade de absorção visível; em um patamar já 31% abaixo do 30d, isso significa que qualquer oscilação no campeão — exposição, preço ou algoritmo — derruba a conta inteira sem amortecimento.

🟠 *Budamix Oficial (Shopee 2):* A Oficial-2 foi a conta de maior ticket do canal (R$ 71,93, +35,1% vs 60d), com o Kit 4 Potes 800ml Quadrado liderando com 7 de 22 pedidos e o GMV acima da média 7d (+21,4%) apesar do volume deprimido vs 30d (-29,7%) — o padrão é consistente com retirada de mecanismo de suporte de baixo ticket (cupom ou ADS): o que sobrou é demanda mais qualificada, menor e mais cara; o único cancelamento do canal está nesta conta e sem produto identificável no pacote, o que impede descartar problema localizado.

🟠 *Budamix Shop (Shopee 3):* Shop-3 é o caso de risco real do dia: com GMV de R$ 1.040,53 (-42,6% vs 30d) e ticket de R$ 52,03 (-22,9% vs 30d), é a única conta onde volume e ticket caem simultaneamente — sem compensação — e toda a atividade se concentrou no intervalo 10h-19h com lacuna em 12h-13h e nenhuma venda noturna, enquanto Store e Oficial-2 apresentaram distribuição ao longo de todo o dia; a causa (exposição específica da conta vs mix/preço) ainda não está confirmada, mas o padrão é evidência de um dia e requer monitoramento imediato com gatilho definido.

🎯 PRIORIDADES DO DIA
• Lucas: monitorar o GMV da Shop-3 hoje com gatilho em R$ 1.200 — se ficar abaixo por mais um dia, avaliar se parece exposição (acionar Himmel para avaliar campanha da conta) ou mix/preço (decisão interna antes de escalar). Confirmar/refutar: GMV acima de R$ 1.200 amanhã mantém leitura de variação dentro da banda deprimida; abaixo por dois dias consecutivos sai do ruído.
• Lucas: verificar se houve fim de campanha, cupom encerrado ou mudança de ADS comum às três contas nos últimos 20-30 dias, consultando histórico de ações com Himmel — a queda foi abrupta e simultânea nas três contas, mais consistente com retirada de mecanismo do que com sazonalidade gradual. Escalar se evento identificado: levar para alinhamento com Himmel antes de qualquer decisão de verba.
• Lucas: confirmar que o Conjunto 5 Potes Redondos Tampa Preta (IMB501P) mantém posição de exposição adequada na Store — com 54,4% dos pedidos da conta concentrados neste produto, qualquer redução de ranking ou visibilidade derruba o GMV da conta sem absorção possível. Se posição estável, Store opera dentro da banda atual sem ação imediata.
• Lucas: não acionar Himmel para aumento de verba ADS sem causa confirmada — o mecanismo da queda ainda não foi identificado; aumentar verba sobre operação em patamar inferior amplifica custo sem garantia de recuperação.
• Lucas: não iniciar teste de segundo vetor em Shop-3 agora — a conta está em compressão dupla sem estabilização; o momento certo é após Shop-3 estabilizar.

Dia analisado: 16/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKU 097 em Oficial-2 — display_name `Pote de Vidro Hermético 600ml`
- Origem do bloqueio: Granular + Condensadora
- Motivo: raw_title do pedido real (`Conjunto 6 Potes de Vidro Quadrados Herméticos com Tampa 4 Travas e Vedação`) conflita com display_name mapeado — produtos de natureza distinta (kit de 6 unidades vs pote único); BLOQUEIO GRANULAR explícito
- Agregado autorizado: não
- Tratamento aplicado: omitido do Top Produtos e de qualquer citação na mensagem
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Granular`, referências a camadas) em toda a seção de análise — conformidade com regra de tom; nomes de camadas internas não vão para Slack
- Seção `🔍 ANÁLISE DA CONTA` renomeada visualmente para `🔍 ANÁLISE DAS CONTAS` — conforme regra 7.6 e layout aprovado para Lucas/Shopee quando a 6B existe
- Quatro blocos de análise (⚫ Consolidado + 3 🟠 contas) extraídos da 6B sem rediagnóstico; SKU interno removido do corpo da análise por limpeza visual e para evitar ID técnico no Slack, sem alterar tese nem produto citado
- Comparações temporais (`+21,4% vs 7d`, `+35,1% vs 60d`, `-42,6% vs 30d`) preservadas na seção `🔍 ANÁLISE DAS CONTAS` e ausentes da seção `📊 VISÃO SHOPEE` — comparações são interpretação e pertencem à análise, não à visão objetiva
- Top Produtos: ranking reordenado por volume consolidado descendente após consolidação cross-conta por SKU/variação vendável — produtos com 11 pedidos precedem produtos com 9 e 8 pedidos
- Top Produtos: KIT2YW800SQ consolidado entre Store (2 pedidos) e Shop-3 (7 pedidos), totalizando 9 pedidos — mesma variação vendável confirmada por SKU idêntico
- Top Produtos: KIT4YW800SQ consolidado nas duas contas onde apareceu (Oficial-2 com 7 pedidos + Shop-3 com 1 pedido = 8 pedidos totais) — mesma variação vendável confirmada por SKU idêntico; consolidação autorizada pela regra de equivalentes
- Top Produtos: CTL002 (Kit 6 Canecas Tulipa 250ml) consolidado nas três contas (Store 6 + Oficial-2 4 + Shop-3 1 = 11 pedidos) — mesma variação vendável confirmada por SKU idêntico e citado pela Granular como único produto cross-conta rastreável
- Top Produtos: contas indicadas em todos os produtos — produto vendeu em menos de 3 contas na maioria dos casos; CTL002 consolidado como cross-conta com contagem explícita por conta
- Top Produtos: SKU 097 de Oficial-2 omitido — bloqueio Granular/Condensadora explícito; sem agregado autorizado
- Top Produtos: produtos de cauda com confidence medium e 1 pedido (ITEM:57356981475, RED01B, KIT6S100, FITA500M, CNCOL, 096, KIT4YW520SQ, KIT4YW320) omitidos ou não priorizados — faturamento por produto não disponível no pacote validado; nenhum entrou no ranking consolidado relevante
- Prioridades: cinco bullets extraídos da 6B `priority_lines` sem reescrita de tese; dois bullets negativos (`não acionar Himmel`, `não iniciar teste`) preservados — conformidade com regra de não criar ação nova
- Confiança média preservada na análise de Shop-3 — ausência noturna descrita como padrão de hoje com monitoramento, não como fato histórico confirmado; formulação `evidência de um dia` da Condensadora mantida
- Produto do cancelamento em Oficial-2 não citado — dado não identificável no pacote; Condensadora bloqueou inferência
- Faturamento por produto omitido de Top Produtos — pacote não traz receita validada por produto/variação; proibido calcular ou estimar