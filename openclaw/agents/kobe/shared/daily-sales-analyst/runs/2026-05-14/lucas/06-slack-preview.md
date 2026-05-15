<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 14/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Total Shopee: 76 pedidos — R$ 4.284,50 — ticket médio R$ 56,38
- Budamix Store: 35 pedidos — R$ 1.225,37
- Budamix Oficial / Conta 2: 18 pedidos — R$ 1.289,82
- Budamix Shop / Conta 3: 23 pedidos — R$ 1.769,31
- Cancelamentos: 0

🏆 TOP PRODUTOS SHOPEE
- Jarra Medidora De Vidro 500ml com Alça Para Receitas (Store) — 17 unidades
- Conjunto de 5 Potes de Vidro Redondos (Store) — 13 unidades
- Kit 6 Canecas Tulipa 250ml Porcelana Coloridas — 11 unidades
- Kit 6 Canecas Porcelana 200ml Reta Lisa Coloridas (Conta 3) — 9 unidades
- Kit 2 Potes de Vidro 800ml Quadrado Hermético — 6 unidades

🔍 ANÁLISE DA CONTA
- O GMV agregado da plataforma (R$ 4.284,50) não representa saúde distribuída: a composição se inverteu — Conta 3 (Shop) passou a ser a maior contribuidora individual e Conta 1 (Store), historicamente a principal, ficou como a menor; tratar o total como resultado da plataforma mascara que a estrutura de sustentação mudou completamente.
- A queda de Conta 1 pode não ser perda de mercado pura — há canibalização interna ativa: o mesmo produto está listado nas três contas com anúncios distintos e Conta 3 capturou a maior parte desse volume no dia; antes de diagnosticar queda estrutural de demanda em Conta 1, é necessário entender quanto do volume está sendo redistribuído internamente entre as contas. A leitura ainda é limitada — a distribuição de um único dia não estabelece padrão.
- Conta 1 (Store) não tem defesa operacional: mais de 85% dos itens saem de dois produtos e um quarto dos pedidos se concentra na janela 21h-22h — a conta inteira depende da exposição noturna de dois anúncios específicos; qualquer oscilação de posição desses produtos nesse horário é o resultado da conta, sem segundo vetor que absorva. Base parcial — padrão consistente com o dado disponível.

🎯 PRIORIDADES DO DIA
- Lucas: verificar visibilidade e posição dos dois produtos campeões da Conta 1 (Store) especificamente no período 19h-22h, comparando se os mesmos produtos aparecem em posição diferente nos anúncios das outras contas nesse mesmo horário. Por quê: Conta 1 opera como dois anúncios com janela noturna e há sobreposição do mesmo produto entre as três contas; se o anúncio de Conta 3 estiver ganhando posição sobre o de Conta 1 nesse horário, o diagnóstico é redistribuição interna — não perda de demanda — e a ação muda completamente. Confirmar/refutar em até 24h: se os campeões de Conta 1 aparecerem em posição inferior ao equivalente de Conta 3 nos resultados de busca no período 19h-22h, redistribuição interna confirmada; se posição equivalente ou superior, o problema é de demanda e ADS não é a alavanca. Escalar se: Lucas confirmar queda de posição dos campeões de Conta 1 no período noturno em relação ao equivalente de Conta 3 → alinhar com Himmel com diagnóstico fechado, não pedido aberto de aumento de verba.

Dia analisado: 14/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios recebidos. A Granular registrou `risco_de_identificacao: baixo` sem nenhum item de BLOQUEIO PARA SLACK ativo. Todos os produtos citados têm platform_item_id e título real do pedido — identificação feita por pedido real, não por alias ou catálogo.

---

### Decisões de formatação

- Remoção de metadados internos `— base: Operacional + Granular / Granular + Estratégica` dos três insights — motivo: são referências de pipeline interno, proibidas no Slack; teses e nuances preservadas integralmente.
- Preservação de ressalva explícita nos insights 2 e 3 (`"a leitura ainda é limitada"`, `"Base parcial — padrão consistente com o dado disponível"`) — motivo: confiança média declarada pela Condensadora; não transformar hipótese em fato.
- Preservação do conectivo `"mas"` e do contraste `"pode não ser perda de mercado pura"` no insight 2 — motivo: substituição por `"e"` ou suavização eliminaria o alerta central da tese.
- Consolidação do CTL002 (Kit 6 Canecas Tulipa 250ml) nas três contas em uma única linha sem indicação de conta — motivo: produto vendeu em 3 contas (regra: indicar apenas quando vendeu em menos de 2); título genérico consolidado usado no lugar dos três títulos divergentes.
- Consolidação do KIT2YW800SQ_T (Kit 2 Potes 800ml Quadrado) entre Store e Conta 3 em uma única linha sem indicação de conta — motivo: produto vendeu em 2 contas; 6 unidades totais (2+4).
- Indicação de conta para Jarra Medidora e Conjunto 5 Potes Redondos como `(Store)` — motivo: venderam exclusivamente na Budamix Store (menos de 2 contas).
- Indicação de conta para Kit 6 Canecas Porcelana 200ml como `(Conta 3)` — motivo: vendeu exclusivamente na Budamix Shop / Conta 3 (menos de 2 contas).
- Omissão de platform_item_ids, distribuição horária detalhada, volumes unitários por SKU no cruzamento de canibalização, proporção itens/pedidos de Conta 3, hipótese de ausência de promoção, dados de fulfillment brutos e quality flags pelo nome técnico — motivo: todos listados explicitamente em `o_que_nao_pode_ir_para_slack` da Condensadora.
- Omissão de R$ por produto no Top Produtos — motivo: faturamento por produto não disponível no pacote; fabricar valor não é permitido.
- Confiança geral média da Condensadora respeitada: três insights emitidos com ressalvas onde aplicável; nenhuma métrica como manchete analítica.