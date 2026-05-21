<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.057,51
- Pedidos: 90 pedidos
- Ticket médio: R$ 56,19
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 22 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
- Kit 6 Canequinhas 100ml — 8 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa 250ml — 5 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
- Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4 Preto — 3 pedidos
- Kit 4 Potes de Vidro 320ml — 3 pedidos
- Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- O GMV do dia ficou acima do histórico do mesmo dia da semana (+31,6%), mas o motor não foi volume — foi ticket elevado (R$ 56,19 vs R$ 41,53 de histórico no mesmo dia). Boa parte desse resultado passou pelo pago. A conta não ganhou alcance; amplificou receita por pedido via mix impulsionado por campanha. Sem confirmar se o ticket segura no orgânico, tratar isso como crescimento de canal é leitura prematura.
- A concentração do dia não está em um produto isolado: as duas variações de potes redondos (tampa preta e tampa vermelha) somaram 30% dos pedidos juntas, e as duas estão expostas ao mesmo risco de ranking. Se esse conjunto perder posição, a conta perde um terço do volume de uma vez — não um SKU cai, um conceito de produto inteiro cai.
- Há um item de fulfillment com 3 unidades em estoque e anúncio ativo. Sem reposição confirmada, o anúncio pode ser pausado involuntariamente nos próximos 1-2 dias — o que contamina a série de observação que é necessária para validar a hipótese de dependência de ADS. É o único ponto que exige ação ainda hoje.

🎯 PRIORIDADES DO DIA
- Yasmin: checar reposição do kit de canequinhas com suporte acrílico (3 unidades em estoque, anúncio ativo em fulfillment). Por quê: ruptura iminente pode pausar o anúncio involuntariamente e contaminar a série de volume dos próximos dias, comprometendo a janela de observação da hipótese estratégica. Sinal a observar: reposição em trânsito ou pedido confirmado dentro de hoje. Escalar se: anúncio pausado sem reposição prevista — registrar como variável confundidora.
- Yasmin: revisar health e posição dos anúncios líderes de fulfillment — especialmente o segundo maior produto do dia (potes retangulares 1050ml), que está com saúde abaixo do limiar — e comparar com a posição da semana passada. Por quê: se o health estiver em deterioração ativa, o ADS pode estar compensando perda de orgânico, o que tornaria a dependência de campanha ainda mais real. Sinal a observar: queda de posição relativa confirmada vs semana passada indica deterioração ativa; posição estável indica health em patamar estável. Escalar se: 2 ou mais anúncios líderes com queda de posição confirmada → Yasmin alinha com Himmel para checar se ADS está compensando perda de orgânico.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: display_name "Kit 6 Tigelas de Vidro 250ml" (TL6250 / MLB6167272090)
- Origem do bloqueio: Granular + Condensadora
- Motivo: display_name diverge materialmente do produto real — produto é "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" (porcelana, não vidro; canecas, não tigelas)
- Agregado autorizado: não — nenhum agregado autorizado; produto citado pelo título real corrigido
- Tratamento aplicado: produto citado na mensagem com nome corrigido ("Kit 6 Canecas Porcelana Tulipa 250ml"), em linha com a resolução de divergência da Granular (título real do anúncio prevalece sobre display_name de mapeamento interno)
- Aparece na mensagem final: sim, como "Kit 6 Canecas Porcelana Tulipa 250ml"

- Item bloqueado: proporção exata ADS/GMV como dado bruto ("60% do GMV veio de ADS")
- Origem do bloqueio: Condensadora
- Motivo: número bruto como manchete — bloqueado; interpretação narrativa autorizada
- Agregado autorizado: sim — "boa parte do GMV do dia passou pelo pago"
- Tratamento aplicado: substituído por formulação interpretativa ("boa parte desse resultado passou pelo pago")
- Aparece na mensagem final: sim, como formulação interpretativa

- Item bloqueado: hipótese de perda ativa de Buy Box do produto em catálogo (Tampa Vermelha / MLB3288536143)
- Origem do bloqueio: Condensadora
- Motivo: vulnerabilidade estrutural confirmada, mas perda ativa de Buy Box para concorrente não confirmável pelos dados
- Agregado autorizado: não — Condensadora bloqueou afirmação de fato; item não aparece como risco confirmado de Buy Box
- Tratamento aplicado: produto citado apenas no Top Produtos pelo volume; sem menção a Buy Box ou catálogo na análise
- Aparece na mensagem final: sim, no Top Produtos apenas (pelo volume), sem qualificação de risco de Buy Box

- Item bloqueado: health numérico específico de cada anúncio listado individualmente
- Origem do bloqueio: Condensadora
- Motivo: dado técnico bruto não adequado para Slack
- Agregado autorizado: sim — referência qualitativa ao "segundo maior produto com saúde abaixo do limiar"
- Tratamento aplicado: health mencionado na prioridade como "saúde abaixo do limiar", sem valores numéricos por produto
- Aparece na mensagem final: sim, como referência qualitativa na prioridade

- Item bloqueado: IDs técnicos (MLBs) e raw SKUs
- Origem do bloqueio: Condensadora + regra estrutural
- Motivo: IDs técnicos não adequados para mensagem ao responsável operacional
- Agregado autorizado: não aplicável — regra estrutural de omissão
- Tratamento aplicado: nenhum ID MLB ou raw SKU aparece na mensagem final
- Aparece na mensagem final: não

- Item bloqueado: divergência de mapeamento TL6250 como detalhe interno
- Origem do bloqueio: Condensadora
- Motivo: detalhe interno de pipeline; não vai para Slack
- Agregado autorizado: não — omitir da análise e prioridades
- Tratamento aplicado: divergência não mencionada na mensagem; produto corrigido silenciosamente pelo título real
- Aparece na mensagem final: não (divergência); produto corrigido sim

---

### Decisões de formatação

- Remoção de metadados internos ("— base: Estratégica + Operacional", "— base: Granular", "— base: Granular + Tática") dos três insights da análise — motivo: instrução explícita de não citar camadas internas na mensagem Slack
- Preservação de linguagem de hipótese nos três insights ("leitura prematura", "pode ser pausado involuntariamente", "pode estar compensando") — motivo: Condensadora classificou os insights como hipótese emergente, não fato confirmado; linguagem de indício preservada conforme regra de confiança média
- Substituição de "boa parte do GMV do dia passou pelo pago" no lugar de "~60% do GMV via campanha" — motivo: Condensadora bloqueou proporção exata como manchete numérica; formulação interpretativa autorizada usada
- Produto TL6250 citado no Top Produtos como "Kit 6 Canecas Porcelana Tulipa 250ml" — motivo: resolução de divergência da Granular; título real do anúncio prevalece sobre display_name de mapeamento interno ("Kit 6 Tigelas de Vidro 250ml" é incorreto — produto é porcelana, não vidro)
- Produto 914C_BAV citado no Top Produtos como "Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico" — motivo: confidence medium com mapping_reason fallback; título real do anúncio usado conforme regra ML; display_name e raw_title são consistentes para este item
- Produto SPC0111 citado como "Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4 Preto" — motivo: confidence medium; título real do anúncio usado; abreviação "PS5 Ps4" normalizada para "PS5/PS4" para legibilidade
- Produto KIT4YW320 citado como "Kit 4 Potes de Vidro 320ml" — motivo: display_name original truncado com reticências ("...Azul-pet..."); usado título curto e identificável sem truncamento
- Produto KIT10YW1050 citado como "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas" — motivo: confidence medium; display_name suficientemente identificável sem código interno; usado conforme disponível
- Health numérico (0.75, 0.71) não aparece na mensagem — motivo: Condensadora bloqueou listagem numérica individual; referência qualitativa usada nas prioridades
- Hipótese de Buy Box da Tampa Vermelha omitida da análise e prioridades — motivo: Condensadora bloqueou como hipótese com evidência parcial; produto aparece apenas no Top Produtos pelo volume real
- Prioridades preservadas com estrutura completa: ação + motivo + sinal de confirmação/refutação + gatilho de escalonamento — motivo: instrução Addendum v3.1 regra 7.2; todos esses elementos estavam na Condensadora
- Nome do item de estoque crítico na prioridade citado descritivamente ("kit de canequinhas com suporte acrílico, 3 unidades") sem MLB — motivo: MLB bloqueado; identificação operacional suficiente para Yasmin localizar o produto
- Seção VISÃO sem comparação temporal — motivo: regra estrutural; comparações pertencem à análise, não à visão objetiva do dia
- Ticket médio na VISÃO: R$ 56,19 (2 casas decimais, vírgula decimal) — motivo: padrão numérico obrigatório
- Ranking Top Produtos em ordem decrescente por pedidos — motivo: regra estrutural; verificado e confirmado (22, 13, 8, 5, 5, 5, 3, 3, 3, 3)