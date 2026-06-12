# Himmel — WhatsApp Shopee

Arquivo canônico para contexto operacional do grupo WhatsApp **[SHOPEE] BUDAMIX + 2**.

## Objetivo

Manter memória dedicada das interações com a Himmel sobre **Shopee**, cobrindo as três contas Budamix, para uso por Kobe, Trader, Spark e outros agentes em análises operacionais, Daily Sales Report v2, planejamento de conta, diagnósticos de ADS e hipóteses de causa/efeito.

## Fonte

- Canal: WhatsApp próprio do Kobe via Evolution API.
- Grupo: **[SHOPEE] BUDAMIX + 2**.
- Escopo: Shopee / planejamento operacional das 3 contas.
- Status de acesso: Kobe consegue localizar o grupo na instância WhatsApp e deve ingerir mensagens novas legíveis via rotina read-only.

## Regras de uso

- Usar como **contexto operacional e hipótese causal**, não como dado de performance por si só.
- Cruzar sempre com dados reais: vendas por shop_id, estoque, campanhas, exposição, ADS, preço, ranking, margem, afiliados, cupons e fulfillment.
- Não culpar agência/Himmel sem evidência quantitativa.
- Quando a mensagem falar apenas “Shopee” sem conta específica, tratar como contexto consolidado das 3 contas e separar impacto por conta nos reports quando os dados permitirem.
- Registrar decisões, planos, projeções, cobranças, responsáveis e janelas de validação.
- Não colar conversa inteira quando não for necessário; resumir o que muda decisão/análise.

## Campos por interação

- Data/hora BRT.
- Participantes relevantes.
- Tema.
- Plataforma/conta.
- Produtos/SKUs citados.
- Decisão/contexto.
- Impacto esperado.
- Como validar nos dados.
- Status: aberto / confirmado / refutado / encerrado.

---

## Interações

### 2026-05-26 09:13–09:47 BRT — Reunião Shopee remarcada com estrategista Himmel

- **Participantes:** Letícia (Himmel) e Lucas / PhaseTec.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada, aplicar como contexto das 3 contas Budamix.
- **Tema:** alinhamento/reunião operacional Shopee do dia.
- **Contexto útil:** reunião originalmente confirmada para 10h foi remanejada para **16h BRT** porque será necessária a participação da estrategista da Himmel.
- **Produtos/SKUs citados:** nenhum.
- **Responsáveis/próximo passo:** Lucas aceitou o remanejamento; Himmel deve entrar com estrategista na reunião das 16h.
- **Como validar nos próximos reports:** aguardar ata/transcrição ou mensagens posteriores para identificar decisões de campanha, verba, produtos priorizados, cupons, afiliados ou janelas de teste que possam afetar o Daily Sales Report v2.
- **Status:** aberto — reunião agendada, ainda sem decisão operacional registrada.

### 2026-05-26 14:15–18:18 BRT — Alinhamento emergencial por queda expressiva de faturamento Shopee

- **Participantes:** Pedro Broglio, Lucas / PhaseTec, Letícia e Raphaella (Himmel).
- **Plataforma/conta:** Shopee consolidado; nenhuma conta específica foi nomeada, então aplicar como contexto das 3 contas Budamix até haver separação por shop_id.
- **Tema:** reunião de alinhamento com Pedro/Lucas por queda expressiva de faturamento e redução de performance em produtos principais.
- **Contexto útil:** Raphaella sinalizou que a reunião precisava ser alinhada diretamente com Pedro “devido à queda expressiva de faturamento da conta” e redução de performance em alguns dos principais produtos. Pedro não conseguiria entrar na reunião original das 16h, mas ajustou participação para 17h; a Himmel confirmou uso do mesmo link. Às 18:18, Raphaella informou que as informações da reunião foram compartilhadas e que havia “pontos alinhados e ações definidas” para recuperar a queda de faturamento das lojas, com acompanhamento das métricas nas próximas semanas.
- **Produtos/SKUs citados:** não houve produto/SKU nomeado no WhatsApp; tratar como alerta genérico sobre produtos principais até transcrição/ata detalhar quais itens caíram.
- **Decisão/contexto:** houve reunião de recuperação de performance Shopee no mesmo dia, com ações definidas pela Himmel/GB; os detalhes operacionais ainda não apareceram no grupo e devem ser buscados na gravação/transcrição ou com Lucas/Pedro antes de virar diagnóstico factual.
- **Impacto esperado:** tentativa de recuperar faturamento Shopee nas lojas e performance dos principais produtos ao longo das próximas semanas.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, comparar vendas, tráfego/conversão, investimento ADS, TACOS/ROAS, ranking/exposição e estoque das 3 contas Shopee; procurar inflexão a partir de 2026-05-26/27 e separar por shop_id. Se houver melhora/queda, registrar como hipótese ligada às ações da reunião, não como causa confirmada.
- **Responsáveis/próximo passo:** Himmel acompanhar evolução das ações e métricas; Lucas/Pedro devem repassar ou disponibilizar a gravação/ata para detalhar ações, produtos e janelas de validação.
- **Status:** aberto — reunião realizada e ações citadas, mas sem detalhamento operacional no WhatsApp.

### 2026-05-26 19:40–21:15 BRT — Pedro fecha diagnóstico e muda direção das ações Shopee

- **Participantes:** Pedro Broglio, Raphaella (Himmel) e pessoas marcadas no grupo; contexto destinado à Himmel Shopee.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada para a maior parte das ações, aplicar como contexto das 3 contas Budamix. A mensagem separa impacto estimado de ruptura por conta: Shop ~29% do faturamento, Oficial ~20–25%, Store ~7%.
- **Tema:** diagnóstico da queda de maio e redirecionamento de estratégia de ADS/campanhas para recuperação de faturamento.
- **Produtos/SKUs citados:** potes retangular 1520, quadrado 800, Canelada Rosa, Xícaras Paris, modelos Paris/Canelada/Reta/Tulipa, canecas, Jarra, Kit 5 Potes Redondos.
- **Decisão/contexto:** Pedro atribuiu a queda de maio a três fatores: ruptura dos potes 1520/800; canecas/Paris/Canelada desativadas no teste anti-canibalização apesar de haver estoque; e campanhas GMV Max com ROAS muito alto/travado (15–35) e baixo gasto diário (~R$130–160 por conta). A direção definida foi não segurar investimento: afrouxar TACOS/meta de ROAS nas campeãs com estoque, remanejar verba dos potes em ruptura para itens disponíveis e religar Paris/Canelada.
- **Contexto sobre teste anti-canibalização:** os modelos Paris, Canelada e Reta perderam volume total em maio; Tulipa foi o único modelo que cresceu e ficou ativo nas 3 contas. Hipótese: o teste retirou visibilidade em vez de direcionar volume para uma conta.
- **Campanhas/promos:** campanha de desconto + Premium aprovada em conceito, mas deve ser redirecionada para itens em estoque, não para potes em ruptura. Cupons para gap de pedidos seguem complementares.
- **Janelas de validação:** 06/06 deve ser preparado com canecas/jarra/redondos antes do container; 07/07 já deve considerar potes de volta. Ruptura dos potes só tende a normalizar com container no início de julho.
- **Responsáveis/próximo passo:** GB/Pedro já estava reativando anúncios de Paris e Canelada; Himmel ficou de validar as recomendações em 2026-05-27 e atualizar no grupo.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, observar inflexão a partir de 2026-05-27 por shop_id em faturamento, pedidos, mix vendido, investimento ADS, TACOS/ROAS, GMV Max, exposição e conversão dos itens em estoque; separar recuperação de canecas/jarra/redondos da limitação estrutural dos potes em ruptura.
- **Status:** aberto — aguardando retorno da Himmel e validação com dados pós-ajuste.

### 2026-05-27 10:55 BRT — Pedro cobra execução das ações combinadas para campanhas Shopee

- **Participantes:** Pedro Broglio; pessoa marcada no grupo Himmel/PhaseTec.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada, aplicar como contexto das 3 contas Budamix.
- **Tema:** follow-up das ações de campanha alinhadas em 2026-05-26.
- **Produtos/SKUs citados:** nenhum novo produto/SKU citado nesta interação; manter como contexto dos itens já priorizados na reunião anterior (canecas, Paris/Canelada, jarra/redondos e produtos com estoque), até detalhamento contrário.
- **Decisão/contexto:** Pedro reforçou que a Himmel/equipe já pode tomar as ações mencionadas em relação às campanhas. Isso confirma que o plano de ajustes discutido no dia anterior saiu da fase de diagnóstico e entrou em execução operacional.
- **Impacto esperado:** possível inflexão de investimento/exposição e mix vendido a partir de 2026-05-27, especialmente em produtos com estoque e anúncios reativados.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id mudanças em investimento ADS, GMV Max, TACOS/ROAS, vendas pagas vs orgânicas, pedidos e faturamento a partir de 2026-05-27/28; separar efeito de campanha de limitações de estoque dos potes em ruptura.
- **Responsáveis/próximo passo:** Himmel/equipe deve executar os ajustes de campanha; Trader deve tratar o período pós-27/05 como janela inicial de validação.
- **Status:** aberto — execução solicitada, aguardando evidência em dados.

### 2026-05-28 12:56–15:07 BRT — Potes priorizados e campanhas Ramp Up criadas nas 3 contas Shopee

- **Participantes:** Lucas / PhaseTec, Pedro Broglio, Leticia e Raphaella (Himmel).
- **Plataforma/conta:** Shopee — ações separadas por conta: Budamix.store, Budamix_store e Budamix.shop.
- **Tema:** cobrança de execução urgente e otimização de campanhas para recuperar volume dos potes nas três contas.
- **Produtos/anúncios citados:**
  - **Budamix.store:** 44860819943, 45010813535, 41081027366, 56610855725.
  - **Budamix_store:** 44710821547, 43831017919, 47110832134, 49710876332.
  - **Budamix.shop:** 45860831209, 52060794046, 49860828629, 45710873981.
- **Decisão/contexto:** Lucas pediu atenção maior nesses potes e estratégias mais fortes para aumentar visibilidade, alcance e conversão nas três contas. Pedro cobrou posição e urgência, reforçando que as três contas estavam em queda livre e que ele não mexeria diretamente nas campanhas para não prejudicar a estratégia da Himmel.
- **Ações informadas pela Himmel:**
  - **Budamix.store:** produtos migrados da GMVMAX para campanha própria **HML | RAMP UP | POTES**; campanha **[HML] - INCUBADORA - NOVOS ITENS** teve ROAS reduzido de **25 para 15**.
  - **Budamix_store:** criada campanha **HML | RAMP UP | POTES HERMÉTICOS** para os 4 anúncios citados, com orçamento diário inicial de **R$50**.
  - **Budamix.shop:** criada campanha **HML | RAM UP | POTES HERM | CC**; campanha **[HML] - INCUBADORA - NOVOS ITENS** teve ROAS reduzido de **28 para 18**.
- **Impacto esperado:** aumento de consumo de verba, visibilidade e volume dos potes priorizados; possível recuperação parcial da queda Shopee a partir de 2026-05-28/29, limitada por estoque, preço e conversão real.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id/anúncio evolução de investimento ADS, ROAS/TACOS, vendas pagas vs orgânicas, pedidos, faturamento, conversão e ranking dos 12 anúncios listados; separar efeito das campanhas Ramp Up do impacto estrutural de ruptura de potes e do mix de canecas/jarra/redondos.
- **Status:** aberto — campanhas otimizadas/criadas em 2026-05-28; validar janela D+1, D+3 e D+7.

### 2026-05-29 11:53–11:56 BRT — Novos itens MDF priorizados para campanhas nas 3 contas Shopee

- **Participantes:** Lucas / PhaseTec.
- **Plataforma/conta:** Shopee — ações separadas por conta: Budamix.store, Budamix_store e Budamix.shop.
- **Tema:** expansão de visibilidade e vendas dos novos itens MDF nas três contas.
- **Produtos/anúncios citados:**
  - **Budamix.store:** 56310173341, 52760159518, 46660201660, 50210185745, 40531001446.
  - **Budamix_store:** 49360200796, 51010172665, 40680725859, 44330709410, 55210742533.
  - **Budamix.shop:** 42530725245, 52710175357, 50860186129, 45660210316, 56510738465.
- **Decisão/contexto:** Lucas pediu atenção maior aos novos itens de MDF e sinalizou intenção de trabalhar campanhas e estratégias para aumentar visibilidade e impulsionar vendas nas três contas. Isso reforça a linha já levantada nas reuniões Himmel de usar MDF como alternativa de mix enquanto itens âncora importados sofrem ruptura/limitação.
- **Impacto esperado:** aumento de exposição, tráfego e primeiros pedidos dos MDF; potencial para compensar parte da queda de Shopee se houver conversão suficiente, mas ainda precisa validação por anúncio/conta.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id/anúncio investimento ADS, impressões, cliques, pedidos, faturamento, conversão, ROAS/TACOS e evolução orgânica dos 15 anúncios listados; comparar D+1, D+3 e D+7 a partir de 2026-05-29.
- **Responsáveis/próximo passo:** Himmel/equipe deve estruturar campanhas/estratégias para os itens MDF; Trader deve acompanhar separadamente o desempenho dos MDF por conta.
- **Status:** aberto — prioridade operacional registrada, aguardando evidência de campanhas e performance.

### 2026-05-29 13:44–13:50 BRT — Lucas cobra retorno e Himmel informa otimizações em andamento

- **Participantes:** Lucas / PhaseTec e Raphaella (Himmel).
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada, aplicar como contexto das 3 contas Budamix.
- **Tema:** follow-up de retorno da Himmel sobre os itens/ações enviados anteriormente.
- **Produtos/SKUs citados:** nenhum produto novo citado nesta interação; manter vínculo com os itens em aberto dos registros de 2026-05-28 (potes/Ramp Up) e 2026-05-29 (novos MDF), salvo detalhamento posterior.
- **Decisão/contexto:** Lucas cobrou retorno da Himmel. Raphaella respondeu que a equipe estava realizando otimizações naquele momento e que, após concluir essas demandas, analisaria os itens enviados no grupo e retornaria com posicionamento.
- **Impacto esperado:** indica que as ações de campanha ainda estavam em execução/análise na tarde de 2026-05-29; resultados do dia podem refletir ajustes incompletos, e a confirmação operacional definitiva ainda está pendente.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, observar D+1/D+3 a partir de 2026-05-29 por shop_id/anúncio: mudança em investimento ADS, campanhas ativas, ROAS/TACOS, pedidos, faturamento e conversão dos potes e MDF priorizados; tratar qualquer melhora/queda como hipótese até a Himmel detalhar as otimizações concluídas.
- **Responsáveis/próximo passo:** Himmel deve concluir otimizações, analisar itens enviados e retornar com posicionamento; Lucas acompanha cobrança.
- **Status:** aberto — otimizações em andamento e retorno prometido, ainda sem detalhamento de ações concluídas.

### 2026-06-01 14:41–19:06 BRT — MDF segue pendente, RTS para pote inativo e estratégia de afiliados/ADS para novos produtos

- **Participantes:** Lucas / PhaseTec, João Miguel CX, Leticia, Raphaella (Himmel) e Pedro Broglio.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada para a maioria dos pontos, aplicar como contexto das 3 contas Budamix. Para novos produtos, Pedro propôs intercalar entre as 3 contas e usar ADS em apenas uma conta por produto/rodada.
- **Tema:** follow-up de produtos MDF, correção de briefing, destravamento de estoque Full e diretriz de lançamento/tração para produtos novos.
- **Produtos/anúncios citados:** produtos MDF enviados anteriormente; ID **23094048438** — Kit 3 Potes de Vidro Retangulares Herméticos com Vedação e Tampa de 4 Travas (Marmita), inativo, com **30 unidades paradas no Full**.
- **Contexto útil:** Lucas cobrou posicionamento da Himmel sobre os MDF e questionou por que o briefing Shopee incluía falas de Mercado Livre. Raphaella explicou que o trecho de Meli foi incluído incorretamente, sem afetar as informações do briefing apresentado na reunião. Leticia informou que o posicionamento dos MDF ainda estava no fluxo e que retornariam ao concluir.
- **RTS / estoque Full:** Raphaella pediu verificação da possibilidade de reativar ou solicitar abertura de RTS para o produto ID 23094048438, pois há 30 unidades paradas no Full sem possibilidade de movimentação. Pedro respondeu que aguardaria o retorno.
- **Decisão/contexto de ADS e afiliados:** Raphaella sugeriu aumentar o investimento percentual em afiliados para produtos novos em ADS, porque a intenção é forçar venda orgânica; subir publicidade diretamente tenderia a canibalizar os anúncios. Pedro aprovou a ação e levantou a diretriz de intercalar entre as três contas, usando ADS nesses produtos novos em somente uma das três contas por vez.
- **Impacto esperado:** novos produtos devem ganhar tração via afiliados e exposição controlada, com menor risco de canibalização entre contas; resultados de ADS/publicidade dos novos itens precisam ser lidos considerando que a estratégia preferida é concentrar/alternar, não ativar tudo simultaneamente nas 3 contas. O item ID 23094048438 pode gerar recuperação de estoque/caixa se reativado ou liberado via RTS.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id/anúncio evolução de pedidos, faturamento, vendas orgânicas vs pagas, afiliados, investimento ADS, TACOS/ROAS e canibalização dos novos produtos/MDF; monitorar se o ID 23094048438 volta a vender, é reativado ou recebe RTS/liberação do estoque Full.
- **Responsáveis/próximo passo:** Himmel deve retornar posicionamento sobre MDF, revisar/evitar briefing com contexto incorreto de Meli e orientar execução de afiliados/ADS alternado; GB/Pedro/equipe deve verificar reativação ou RTS do ID 23094048438.
- **Status:** aberto — aguardando retorno da Himmel e validação operacional nos dados D+1/D+3/D+7 a partir de 2026-06-01.

### 2026-06-02 09:32–09:41 BRT — Pedro aprova separação/alternância para evitar competição entre contas

- **Participantes:** Leticia (Himmel) e Pedro Broglio.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada, aplicar como contexto das 3 contas Budamix.
- **Tema:** confirmação de estratégia para reduzir competição interna entre as contas Shopee.
- **Produtos/SKUs citados:** nenhum.
- **Decisão/contexto:** Leticia indicou seguir com a estratégia justamente para que uma conta não compita com a outra em lances e não virem concorrentes internas. Pedro aprovou: “podemos seguir dessa forma então”. Esta interação reforça a diretriz de alternar/concentrar ações entre contas quando fizer sentido, em vez de impulsionar o mesmo produto simultaneamente nas três.
- **Impacto esperado:** menor canibalização de lances e leitura mais limpa de performance por conta/produto; possível redistribuição de investimento, exposição e vendas entre as três contas.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id se houve redução de sobreposição de campanhas/produtos, mudanças em investimento ADS, ROAS/TACOS, pedidos e faturamento; avaliar se produtos trabalhados em uma conta ganham tração sem derrubar desnecessariamente as demais.
- **Responsáveis/próximo passo:** Himmel deve conduzir a estratégia aprovada; Trader deve tratar variações entre contas como possível efeito de separação/alternância, não apenas queda isolada.
- **Status:** aberto — estratégia aprovada em 2026-06-02, validar D+1/D+3/D+7.

### 2026-06-08 11:35–12:04 BRT — Estoque parado no Full, RTS e promoção agressiva para Kit 5 Potes Redondos

- **Participantes:** Raphaella (Himmel).
- **Plataforma/conta:** Shopee — conta **Budamix.Store** citada explicitamente; pontos de Full/RTS e promoção devem ser tratados como contexto prioritário dessa conta, mas validar nas 3 contas se houver anúncios equivalentes.
- **Tema:** estoque parado no Full, custo mensal de armazenagem, pendência fiscal em produto suspenso e perda de competitividade em item de alto volume.
- **Produtos/SKUs citados:**
  - **LIVCNCOL24** — Kit Bobbie Goods livro de colorir ROSA 24 peças: 29 unidades paradas no Full.
  - **LIVAZCNCOL24** — Kit Bobbie Goods livro de colorir AZUL 24 peças: 36 unidades paradas no Full.
  - **LIVCNCOL80** — Kit Bobbie Goods livro de colorir ROSA 80 peças: 17 unidades paradas no Full.
  - **LIVCNCOL48** — Kit Bobbie Goods livro de colorir ROSA 48 peças: 11 unidades paradas no Full.
  - **LIVAZCNCOL48** — Kit Bobbie Goods livro de colorir AZUL 48 peças: 23 unidades paradas no Full.
  - **CJT1TP** — Kit Jogo 3 Potes de Vidro Condimento Redondo com Tampa Bambu/Colher/Suporte: 16 unidades paradas no Full; serviço Shopee suspenso por erro nas informações de imposto.
  - **CK4742_B** — Jarra Medidora de Vidro 500ml: 120 unidades paradas no Full.
  - **ID 22393168887** — Conjunto de 5 Potes de Vidro Redondos: Budamix.Store com 734 unidades vendidas/mês vs concorrentes Favorito na Web, Big Achados Shop e Casa & Vídeo com ~1.000 unidades/mês cada.
- **Decisão/contexto:** Himmel recomenda avaliar **RTS (Retirada de Estoque)** para itens de baixo giro/excluídos no Full ou acelerar giro com ajustes de preço, campanhas promocionais, ofertas relâmpago, cupons, combos e reforço em publicidade, priorizando itens com maior volume parado. Também pede avaliação de promoção mais agressiva para o Conjunto de 5 Potes Redondos, porque a Budamix.Store está perdendo espaço para concorrentes no volume mensal.
- **Impacto esperado:** reduzir custo de armazenagem Full e liberar estoque parado; recuperar giro/competitividade do Kit 5 Potes Redondos; destravar CJT1TP depende de correção fiscal antes de escalar campanha.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id/anúncio: estoque Full, custo/risco de armazenagem, status de serviço do CJT1TP, vendas e conversão do ID 22393168887, preço final/cupom/ofertas, ranking frente aos concorrentes citados, investimento ADS e efeito D+1/D+3/D+7 após qualquer promoção/RTS/correção fiscal.
- **Responsáveis/próximo passo:** GB/Pedro/equipe deve decidir entre RTS vs aceleração promocional para cada SKU parado e corrigir pendência fiscal do CJT1TP; Himmel deve orientar campanhas/cupons/ofertas para giro e competitividade.
- **Status:** aberto — recomendação recebida; requer decisão operacional sobre RTS/promoção/correção fiscal e validação nos dados.

### 2026-06-08 13:01–13:42 BRT — Estratégia de capa por variação nas canecas para recuperar CTR/conversão

- **Participantes:** Pedro Broglio e Raphaella (Himmel).
- **Plataforma/conta:** Shopee — ações separadas por conta: **budamix.shop**, **budamix.store** e **budamix_store**.
- **Tema:** recuperação de vendas das canecas via otimização de imagem principal/variação ativa dos anúncios.
- **Produtos/SKUs citados:** canecas; variações **Colorida**, **Rosa**, **Branca**, **Azul** e **Amarela**.
- **Decisão/contexto:** Raphaella sugeriu analisar a curva de saída das variações em cada conta e alterar a foto de capa dos anúncios para a variação com melhor desempenho ou maior potencial, já que a imagem principal representa a variação ativa e pode melhorar atratividade, CTR e conversão. Pedro informou que estava verificando e daria posição até o fim do dia; Raphaella disse que também estava analisando as demais contas.
- **Exemplos por conta:**
  - **budamix.shop:** Colorida foi a variação com maior volume no mês anterior; faz sentido manter/configurar capa para Colorida.
  - **budamix.store:** Colorida liderou, mas Rosa ficou próxima em segundo; avaliar teste de capa com Rosa.
  - **budamix_store:** Colorida liderou; Branca foi a segunda mais vendida; Azul e Amarela tiveram baixo desempenho, com Amarela sem vendas no período. Raphaella levantou possibilidade de testar capa com Branca, Azul ou Amarela.
- **Impacto esperado:** otimização simples para tentar recuperar volume de canecas, aumentando clique/conversão por conta sem depender apenas de ADS ou preço.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, acompanhar por shop_id/anúncio/variação: CTR, conversão, pedidos, faturamento, mix de cores, investimento ADS, TACOS/ROAS e efeito D+1/D+3/D+7 após eventual troca de capa. Tratar melhora/queda como hipótese até confirmar que a mudança foi aplicada.
- **Responsáveis/próximo passo:** Pedro/GB deve confirmar posição e decidir/aplicar as trocas de capa; Himmel deve concluir análise das demais contas e acompanhar resultado.
- **Status:** aberto — estratégia sugerida; aguardando posição do Pedro e/ou confirmação de implementação.

### 2026-06-09 09:53–10:12 BRT — Promoção para estoque Full, Bobbie Goods descontinuados e capas por melhor variação

- **Participantes:** Pedro Broglio, Raphaella (Himmel) e Lucas / PhaseTec.
- **Plataforma/conta:** Shopee — **Budamix.Store** citada explicitamente para estoque Full; estratégia de capa por variação deve ser tratada por conta nas 3 contas Shopee.
- **Tema:** execução das recomendações de 2026-06-08: liquidação de estoque parado no Full, ajuste de preço/ADS e otimização de imagem principal por variação.
- **Produtos/SKUs citados:** **CK4742_B** com 120 unidades no Full; kits **Bobbie Goods**; **CJT1TP**; produto não nomeado no trecho ingerido com preço final definido em **R$ 26,90**.
- **Decisão/contexto:** Pedro informou que vai criar promoção com desconto direto e agressivo nos itens parados do Full da Budamix.Store, priorizando CK4742_B e kits Bobbie Goods. Raphaella alertou que os kits Bobbie Goods foram descontinuados da loja por denúncia, então Pedro indicou que tentará pelo menos fazer a remoção/RTS desses itens. Pedro também informou que a pendência fiscal do **CJT1TP** foi regularizada e que ele já pode entrar normalmente junto com os demais.
- **Preço/ADS:** Pedro definiu redução do preço final de um produto para **R$ 26,90**; como a margem já está apertada, a competitividade deve ser compensada por reforço de ADS/visibilidade, não por corte adicional de preço. Não amarrar automaticamente esse preço ao ID 22393168887 sem validação, pois o SKU/produto não veio nomeado no trecho novo.
- **Capas/variações:** Pedro informou que a equipe já está ajustando imagens de capa, colocando na frente a variação de melhor desempenho de cada conta. Isso confirma início de implementação da estratégia discutida em 2026-06-08 para canecas/variações.
- **Reunião:** Raphaella confirmou reunião Shopee às 10h BRT; Lucas confirmou participação.
- **Impacto esperado:** giro acelerado de estoque parado no Full, redução de custo/risco de armazenagem, eventual recuperação de CTR/conversão por capa de melhor variação e aumento de vendas via ADS para item com preço limitado por margem. Bobbie Goods pode deixar de ser frente promocional e virar prioridade de remoção por denúncia/descontinuação.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id/anúncio: mudança de preço final para R$ 26,90 no produto correto, início/efeito de promoção dos itens Full, status/RTS dos Bobbie Goods, normalização do **CJT1TP**, alterações de imagem principal por conta, CTR, conversão, pedidos, faturamento, estoque Full, investimento ADS e TACOS/ROAS. Validar D+1/D+3/D+7 a partir de 2026-06-09.
- **Status:** aberto — ações em execução; validar aplicação real e efeito nos dados.

### 2026-06-09 10:32–10:33 BRT — Himmel otimiza campanhas Shopee e isola anúncios com potencial de escala

- **Participantes:** Leticia (Himmel).
- **Plataforma/conta:** Shopee — ações separadas por conta: **Budamix.store**, **Budamix_store** e **Budamix.shop**.
- **Tema:** otimizações de campanhas e campanhas isoladas para trazer exposição a itens com potencial de escala.
- **Produtos/anúncios/campanhas citados:**
  - **Budamix.store:** anúncios **23094203124**, **23036701291**, **23594198474** em campanhas isoladas/orçamento próprio; campanha **HML | RAMP UP | POTES**; **Kit 4 Descanso de Panela MDF Modular Suporte**.
  - **Budamix_store:** **HML | RAMP UP | POTES HERMÉTICOS**; **HML | CC | VSL - CAMPANHA DE POTES 2**; anúncio **22097667091** saindo da campanha **HML | CC | VSL - CAMPANHA DE POTES 1** por boa performance; **HML | CC | VSL - CAMPANHA DE POTES 1**; anúncio **23094203035** em campanha isolada.
  - **Budamix.shop:** **HML | RAM UP | POTES HERM | CC**; **HML | CC | VSL - CAMPANHA DE POTES 1**; anúncio **23298676159** isolado por boa performance; anúncios **23698553207** e **22494052928** isolados.
- **Decisão/contexto:** Himmel informou campanhas otimizadas com sucesso. A lógica geral foi aumentar exposição dos itens com potencial, reduzir/ajustar metas de ROAS em campanhas existentes e isolar anúncios que performaram bem para dar orçamento próprio.
- **Ajustes principais de ROAS/orçamento:**
  - **Budamix.store:** 23094203124 com ROAS 20 e orçamento 10; 23036701291 com ROAS 21 e orçamento 10; 23594198474 com ROAS 19 e orçamento 10; **HML | RAMP UP | POTES** de ROAS 10,3 para 13; Kit 4 Descanso de Panela MDF Modular de ROAS 24,5 para 22,1.
  - **Budamix_store:** **HML | RAMP UP | POTES HERMÉTICOS** de ROAS 12,9 para 15; **HML | CC | VSL - CAMPANHA DE POTES 2** de ROAS 16 para 14; **22097667091** isolado com ROAS 14 e orçamento 15; **HML | CC | VSL - CAMPANHA DE POTES 1** de ROAS 20 para 18; **23094203035** isolado com ROAS 13 e orçamento 10.
  - **Budamix.shop:** **HML | RAM UP | POTES HERM | CC** de ROAS 12,3 para 14; **HML | CC | VSL - CAMPANHA DE POTES 1** de ROAS 12,1 para 13; **23298676159** isolado com ROAS 12 e orçamento 10; **23698553207** de ROAS 15 para 13; **22494052928** isolado com ROAS 13 e orçamento 10.
- **Impacto esperado:** mais verba controlada e exposição para anúncios de boa performance/potencial de escala, com leitura mais limpa por item isolado; possível aumento de pedidos e faturamento Shopee a partir de 2026-06-09/10, especialmente em potes e MDF priorizados.
- **Como validar nos dados:** nos próximos Daily Sales Reports v2, checar por shop_id/anúncio/campanha: investimento ADS, ROAS/TACOS, pedidos, faturamento, vendas pagas vs orgânicas, conversão, CTR e ranking; comparar D+1/D+3/D+7 a partir de 2026-06-09. Separar efeito de campanhas isoladas dos ajustes de capa/variação, promoções Full e limitações de estoque.
- **Responsáveis/próximo passo:** Himmel aguarda retorno da GB/Pedro/Lucas para avaliar possibilidade de forçar ADS nesses itens; Trader deve tratar 2026-06-09 como nova janela de validação das campanhas Shopee.
- **Status:** aberto — otimizações reportadas como concluídas; aguardando decisão sobre reforço adicional em ADS e validação com dados.

### 2026-06-12 14:59 BRT — Letícia cobra retorno pendente sobre alinhamento Shopee

- **Participantes:** Leticia (Himmel); pessoas marcadas no grupo.
- **Plataforma/conta:** Shopee consolidado; sem conta específica nomeada, aplicar como contexto das 3 contas Budamix apenas se o retorno se referir às ações em aberto.
- **Tema:** cobrança de retorno pendente.
- **Produtos/SKUs citados:** nenhum novo produto/SKU citado.
- **Decisão/contexto:** Leticia perguntou se havia retorno “sobre isso”, mas a mensagem ingerida não trouxe o assunto anterior no próprio trecho. Tratar como cobrança de pendência aberta da Himmel, provavelmente ligada aos alinhamentos recentes de campanhas/ADS/ações Shopee, até haver confirmação do tema.
- **Impacto esperado:** nenhum impacto operacional confirmado ainda; pode indicar que existe decisão/validação pendente da GB antes da Himmel avançar.
- **Como validar nos dados:** não usar como causa de performance sem contexto adicional. Nos próximos reports, apenas sinalizar se houver resposta posterior ligando a cobrança a campanhas, produtos, orçamento, promoções, capas/variações ou contas específicas.
- **Responsáveis/próximo passo:** aguardar resposta no grupo ou buscar a mensagem anterior caso seja necessário destravar a pendência.
- **Status:** aberto — cobrança registrada, sem conteúdo operacional suficiente para alterar diagnóstico.

