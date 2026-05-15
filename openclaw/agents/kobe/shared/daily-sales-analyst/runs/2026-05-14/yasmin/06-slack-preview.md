<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 14/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 6.539,97
- Pedidos: 140 pedidos
- Ticket médio: R$ 46,71
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita — 47 pedidos — (variações combinadas do anúncio líder)
- Kit 2 Potes Vidro 1520ml Tampa Hermético Travas Vedação Verde-escuro — 22 pedidos
- Kit 4 Potes De Vidro 520ml Tampa Hermética 4 Travas Vedação Verde-escuro — 9 pedidos
- Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto — 9 pedidos
- Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo — 9 pedidos

🔍 ANÁLISE DA CONTA
- O resultado de 14/05 no ML é real, mas a leitura de patamar está em aberto: volume e ticket subiram juntos em padrão bimodal (bloco 8–11h e 20–22h) que não é compatível com crescimento orgânico puro — a checagem com Himmel sobre intervenção ativa de ADS é o único dado que separa pico episódico de novo piso real. Sem essa checagem, qualquer calibração de expectativa ou verba está sobre premissa não confirmada.
- A dependência da conta em um único anúncio é estruturalmente mais severa do que o indicador de concentração sugere: o anúncio líder (Jogo Potes 5 Peças Claro) responde por 30% dos itens nas suas variações combinadas — com os dois anúncios dominantes somando 44% do volume. Qualquer perda de ranking, estoque ou elegibilidade nesse anúncio tem impacto imediato de ~30% no volume total.

🎯 PRIORIDADES DO DIA
- Yasmin: checar com Himmel se houve intervenção ativa de ADS ML (boost, campanha, ajuste de lance) nos últimos 2 dias. Volume e ticket subiram juntos em padrão bimodal — estrutura incompatível com crescimento orgânico. Essa checagem é o critério que valida ou derruba a tese de patamar antes de qualquer decisão de verba ou exposição. Confirmar/refutar: Himmel confirma intervenção ativa → resultado tem componente efêmero e 140 pedidos não é novo piso; Himmel nega intervenção → sinal de patamar ganha peso e justifica observação atenta nos próximos 2 dias úteis.
- Yasmin: observar GMV dos próximos 2 dias úteis (15/05 e 16/05) com referência explícita a R$ 4.500. A tese de ganho de patamar só se sustenta se o GMV confirmar a faixa acima de R$ 4.500 em pelo menos 2 dos próximos 3 dias úteis. Confirmar/refutar: GMV acima de R$ 4.500 em 2 dos próximos 3 dias → patamar se confirma; retorno consistente à faixa R$ 3.000–3.500 → 14/05 foi pico episódico.

Dia analisado: 14/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs individuais (IMB501P_T, IMB501C_T, IMB501V_T, KIT2YW1520) e IDs técnicos MLB3288536143, MLB5322494954
- Origem do bloqueio: Condensadora
- Motivo: desnecessários para leitura Slack; MLBs técnicos não devem aparecer nominalmente
- Agregado autorizado: sim — "anúncio líder", "Jogo Potes 5 Peças Claro" (título real), "variações combinadas do anúncio líder"
- Tratamento aplicado: substituído por descritores autorizados; SKUs individuais omitidos; MLB IDs omitidos
- Aparece na mensagem final: não nominalmente; sim, como agregado com título real e descritivo

- Item bloqueado: top3_concentration (41,7%) sem ressalva
- Origem do bloqueio: Condensadora
- Motivo: métrica induz leitura incompleta da dependência real; listing líder isolado já é 30% dos itens
- Agregado autorizado: sim — "30% dos itens nas suas variações combinadas" + "dois anúncios dominantes somando 44% do volume"
- Tratamento aplicado: substituído pela leitura por listing consolidado autorizada pela Granular/Condensadora
- Aparece na mensagem final: sim, como agregado corrigido (30% e 44%)

- Item bloqueado: série de quintas (98→81→115→75→140) como argumento de tendência
- Origem do bloqueio: Condensadora
- Motivo: volatilidade documentada não sustenta direcional
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

---

### Decisões de formatação

- Consolidação de MLB3288536143 (3 SKUs) em listing único no Top Produtos — Granular confirmou mesmo platform_item_id; volume somado = 47 unidades; exibido como anúncio líder com título real
- Remoção de metadados internos (`— base: Estratégica + Operacional + Granular`) dos insights — dados de pipeline não vão para Slack
- Preservação de ressalva de confiança média nos dois insights — Condensadora sinalizou composição do resultado em aberto; linguagem "está em aberto" e "não é compatível com crescimento orgânico puro" preservadas integralmente
- Preservação de condição falsificável nas duas prioridades — sinal confirma/refuta mantido conforme Condensadora
- Omissão de top3_concentration (41,7%) como métrica bruta — substituída pela leitura consolidada por listing (30% e 44%) autorizada pela Condensadora
- Omissão de MLBs técnicos e SKUs individuais no corpo da mensagem — descritores em linguagem natural usados no lugar
- Seção VISÃO sem comparação temporal — dados objetivos do dia apenas; comparações pertencem à ANÁLISE
- Ticket médio formatado como R$ 46,71 — padrão monetário aplicado
- Faturamento formatado como R$ 6.539,97 — ponto como separador de milhar, vírgula decimal
- Cancelamentos incluídos (3) — disponíveis no pacote e operacionalmente registráveis mesmo sendo irrelevantes em taxa
- Ranking Top Produtos ordenado por volume consolidado por listing (47 → 22 → 9 → 9 → 9) — consolidação MLB3288536143 colocou o anúncio líder na posição correta com volume real