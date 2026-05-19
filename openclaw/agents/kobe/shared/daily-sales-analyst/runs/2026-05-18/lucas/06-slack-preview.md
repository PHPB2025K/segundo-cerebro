<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

DAILY SALES REPORT — SHOPEE — 18/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Consolidado: 84 pedidos — R$4.768,84 — Ticket médio R$56,77
- Budamix Store: 59 pedidos — R$2.497,44 — 3 cancelamentos
- Budamix Oficial (Conta 2): 16 pedidos — R$1.570,30
- Budamix Shop (Conta 3): 9 pedidos — R$701,10

🏆 TOP PRODUTOS SHOPEE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 27 pedidos
- Jarra Medidora de Vidro 500ml (Store) — 18 pedidos
- Kit 6 Canecas Tulipa 250ml — 15 pedidos
- Kit 4 Potes de Vidro 800ml Quadrado (Conta 2) — 4 pedidos
- Kit 2 Potes de Vidro 800ml Quadrado — 4 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 3 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee fechou o dia com 84 pedidos e R$4.768,84, mas o número mascara uma estrutura frágil: a Store carregou 70% do volume com dois produtos que respondem por 76% dos pedidos da própria conta — se esses dois oscilarem, a plataforma inteira sente, porque Conta 2 e Conta 3 não têm volume para amortizar. A queda simultânea nas três contas em relação ao 30d e 60d indica que o enfraquecimento não é evento de ontem, mas a magnitude e o padrão divergem por conta — o que impede qualquer decisão de plataforma antes de diagnosticar cada conta separadamente.

🟠 *Budamix Store (Shopee 1):* A Store explica o volume da plataforma, mas não por diversificação — Conjunto 5 Potes Tampa Preta (27 pedidos) e Jarra Medidora (18 pedidos) sustentam 76% da conta, com os demais SKUs respondendo por menos de 12% somados. Ticket subindo (+8,5% vs 30d) enquanto volume cai (-27%) é sinal de estreitamento de mix, não de saúde — o segundo vetor não existe nessa conta e qualquer queda de exposição nos dois produtos-âncora move diretamente o resultado consolidado da Shopee.

🟠 *Budamix Oficial (Shopee 2):* Volume colapsou -47% vs 30d, mas o padrão horário revela algo mais específico do que queda geral: a conta funcionou entre 8h e 17h e zerou completamente de 18h a 23h — ausência total de uma janela inteira, não queda de conversão distribuída ao longo do dia. O ticket elevado (R$98,14 vs média 30d de R$60,05) parece refletir mix de produtos de kit maior nos 16 pedidos do período ativo, não recuperação de patamar.

🟠 *Budamix Shop (Shopee 3):* A Conta 3 não está em dia fraco — está em colapso de patamar: 9 pedidos contra média 30d de 26,4, com queda em todas as janelas históricas e padrão horário completamente plano (1 pedido por hora em 9 horas distintas, zero horas com 2 ou mais pedidos). Esse é o padrão de conta sem tráfego direcionado ativo, não de conta com demanda baixa. Neste nível de volume, a Conta 3 consome atenção operacional sem retorno proporcional — o diagnóstico de hoje define se o movimento é investigar causa ou avaliar viabilidade da conta.

🎯 PRIORIDADES DO DIA
- Lucas: verificar com Himmel se a Conta 2 (Budamix Oficial) tinha ADS ativo no período de 17h a 23h. A janela noturna zerou por completo, confirmado por pedidos reais — não é queda de conversão distribuída, é ausência de uma janela inteira. Confirmar/refutar: ADS ativo e mesmo assim zerou = problema de exposição orgânica ou demanda; ADS inativo = acionar Himmel especificamente para essa janela da Conta 2, não para as três contas. Escalar se a Conta 2 voltar a zerar o noturno no próximo ciclo.
- Lucas: observar o volume total da Conta 3 (Budamix Shop) hoje. 9 pedidos com padrão horário plano ontem — o segundo dia define o diagnóstico. Confirmar/refutar: acima de 15 pedidos com algum pico horário = evento pontual, atenção normal; abaixo de 12 pelo segundo dia consecutivo = colapso de patamar confirmado. Escalar para Kobe com hipótese de viabilidade operacional da Conta 3, não ADS.
- Lucas: checar se a exposição dos dois produtos-âncora da Store (Conjunto 5 Potes Tampa Preta e Jarra Medidora) caiu nos últimos 2-3 dias vs semana anterior. Confirmar/refutar: exposição em queda = alinhar com Himmel imediatamente; exposição estável = problema de conversão, diagnóstico muda de canal. Este é o gatilho mais sensível da semana.
- Lucas: não acionar Himmel para as três contas ao mesmo tempo. A causa da queda simultânea ainda não está identificada — ação de ADS, se necessária, é por conta e por problema específico; mexer nas três em paralelo amplifica qualquer erro de diagnóstico.
- Lucas: não escalar exposição do CTL002 (Kit 6 Canecas Tulipa 250ml) nas três contas em paralelo. O SKU aparece nas três contas com anúncios distintos — sem dado de ADS por conta, aumentar exposição simultaneamente pode amplificar canibalização entre as próprias contas.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT

---

### Respeito de bloqueios

- Item bloqueado: SKU 098 — Conta 2 (platform_item_id: 23198542584)
- Origem do bloqueio: Granular + Condensadora
- Motivo: divergência entre raw_title do pedido real ("Kit 9 Potes Vidro Quadrados Hermético Vedação Tampa 4 Travas Marmita") e display_name mapeado ("Pote de Vidro Hermético 800ml"); mapeamento interno declarado como high confidence contradiz a divergência visível — risco médio de identificação incorreta
- Agregado autorizado: não (Condensadora orientou "referência agregada à Conta 2 ou citar pelo raw_title até correção do catálogo", mas sem agregado explícito aprovado para uso no Slack)
- Tratamento aplicado: item omitido do ranking de Top Produtos e da análise; os 3 pedidos não aparecem nominalmente em nenhuma seção
- Aparece na mensagem final: não

- Item bloqueado: ITEM:57356981475 — Store (platform_item_id: 57356981475)
- Origem do bloqueio: Condensadora
- Motivo: sem SKU interno, mapeado apenas por platform_item_id com confiança média; 1 pedido no dia; Condensadora listou explicitamente em "o que não pode ir para Slack"
- Agregado autorizado: não
- Tratamento aplicado: omitido do ranking de Top Produtos
- Aparece na mensagem final: não

- Item bloqueado: FITA500M — Store (platform_item_id: 22398347517)
- Origem do bloqueio: Granular (confiança média — mapped_generic_sku, raw_sku_normalized_with_short_title_fallback)
- Motivo: confiança média de mapeamento; 1 pedido no dia; volume irrelevante para ranking
- Agregado autorizado: não
- Tratamento aplicado: omitido do ranking de Top Produtos; bloqueio recebido sem agregado autorizado
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção dos metadados "— base: Operacional + Granular / Estratégica + Granular" dos insights da análise — metadados internos, não pertencem ao Slack; teses preservadas integralmente
- Título da seção de análise alterado para "ANÁLISE DAS CONTAS" — regra 7.6: quando 06b-shopee-consolidator existe, o título visual reflete as 3 contas
- Fonte analítica obrigatória: 06b-shopee-consolidator — regra de fonte hierárquica para Lucas/Shopee; as quatro linhas de análise vêm diretamente da 6B
- Faturamento por produto omitido no Top Produtos — pacote não traz receita validada por produto/variação; formato aplicado: "[nome] — [pedidos] pedidos"
- CTL002 (Kit 6 Canecas Tulipa 250ml) consolidado nas 3 contas sem indicação de conta — vendeu em 3 contas (Store: 7, Conta 2: 4, Conta 3: 4 = 15 pedidos); regra: indicar conta apenas quando vendeu em menos de 2 contas
- KIT2YW800SQ (Kit 2 Potes de Vidro 800ml Quadrado) consolidado Store+Conta3 sem indicação de conta — vendeu em 2 contas (4 pedidos); regra de indicação não se aplica
- IMB501P indicado como "(Store)" — vendeu apenas em 1 conta
- CK4742 indicado como "(Store)" — vendeu apenas em 1 conta
- KIT4YW800SQ indicado como "(Conta 2)" — vendeu apenas em 1 conta
- IMB501C indicado como "(Conta 2)" — vendeu apenas em 1 conta
- SKU 098 omitido do Top Produtos — bloqueio recebido sem agregado autorizado; 3 pedidos da Conta 2 não contabilizados no ranking
- Shopee Full omitido da VISÃO — valor 0 nas três contas; dado disponível mas irrelevante
- Cancelamentos incluídos na VISÃO junto à Budamix Store — 3 cancelamentos confirmados nessa conta, relevantes em relação ao volume da conta; Conta 2 e Conta 3 com zero cancelamentos, omitidos
- Confiança geral preservada como média — alertas de confiança da Condensadora mantidos implicitamente pela linguagem de indício ("parece refletir", "aponta para") nos trechos correspondentes
- Prioridade de "não fazer" (não acionar Himmel para 3 contas / não escalar CTL002) mantida como bullet de prioridade — veio das priority_lines da 6B e representa ação operacional concreta para Lucas
- Nenhuma análise própria adicionada — todo conteúdo analítico rastreável às camadas anteriores (06b como fonte primária)