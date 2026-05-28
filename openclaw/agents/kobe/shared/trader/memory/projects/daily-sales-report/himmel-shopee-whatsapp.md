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

