<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE BUDAMIX STORE — 03/06/2026 (Ontem)

📊 VISÃO SHOPEE BUDAMIX STORE
- Faturamento: R$ 2.398,92
- Pedidos: 56
- Ticket médio: R$ 42,84
- Cancelamentos: 1

🏆 TOP PRODUTOS SHOPEE BUDAMIX STORE
- Jarra Medidora 500ml — 22 pedidos
- Potes Vidro 5 Peças — Tampa Preta — 10 pedidos
- Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha — 8 pedidos
- Pote Vidro 520ml — Quadrado — 6 pedidos
- Kit 2 Potes 800ml — Quadrado — 6 pedidos

🔍 ANÁLISE DA CONTA
- O dia parece normal na superfície — 56 pedidos, R$ 2.398,92, ticket de R$ 42,84 puxando o faturamento para +9,1% vs média 30d. Mas os 3 campeões que sustentaram 71,4% do volume — Jarra Medidora 500ml, Potes Vidro 5 Peças — Tampa Preta e Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha — fecharam o dia com estoque zero confirmado no snapshot pós-baixa. Não é estabilidade: é o último dia com o portfólio campeão de pé.
- Sem reposição confirmada em D+1, a cauda com estoque — Pote Vidro 520ml — Quadrado, Kit 2 Potes 800ml — Quadrado, Kit 4 Potes Vidro 520ml Quadrado Hermético Fitness e Kit 4 Descanso de Panela MDF Modular Suporte de Mesa Cozinha — entrega teto de ~15 pedidos/dia no ritmo de 03/06, contra média 7d de ~49 pedidos. Com a Saúde da Loja indisponível (HTTP 404) e Shopee Ads inacessível (HTTP 403), cada pedido novo que cair nos 3 campeões zerados vira cancelamento automático invisível ao pipeline — o risco prospectivo é jogar a Taxa de Cancelamento do Vendedor muito acima do threshold de Vendedor Indicado (< 2%) sem nenhum sinal no pacote. Lucas precisa conferir estoque dos 3 campeões e verificar NFR e Pontos de Penalidade manualmente no Seller Center até 10h de 04/06. Em D+3 sem Saúde da Loja disponível e sem reposição confirmada, escalar para Pedro.
- A conta parece estar operando sem nenhuma alavanca de exposição verificável: Programa de Frete Grátis em 0% de toda a base ativa, 68,3% dos anúncios ativos zerados (41 de 60), fora do Shopee Mall e sem Vendedor Indicado. Não é momento de mexer em Shopee Ads ou Frete Grátis sem informação — a ação concreta é Lucas verificar no Seller Center se o zero do Programa de Frete Grátis é configuração histórica ou desativação recente, para virar input qualificado da próxima conversa com Pedro.

🎯 PRIORIDADES DO DIA
- Lucas: verificar no Seller Center até 10h de 04/06 se Jarra Medidora 500ml, Potes Vidro 5 Peças — Tampa Preta e Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha tiveram reposição overnight; em paralelo, conferir manualmente NFR, Pontos de Penalidade e Taxa de Cancelamento do Vendedor enquanto a Saúde da Loja segue indisponível. Os 3 campeões concentraram 71,4% do volume de 03/06 e fecharam com estoque zero — sem dado oficial de Saúde da Loja, é a única verificação que evita cascata de cancelamentos invisível ao pipeline. Confirmar/refutar por: cancelamentos D+1 ≤ 2 com reposição de ao menos 2 dos 3 campeões = risco contido; cancelamentos D+1 ≥ 5 = cascata em andamento. Escalar se: nenhum dos 3 campeões com reposição confirmada até 10h de 04/06, ou D+3 sem Saúde da Loja disponível — escalar para Pedro.
- Lucas: registrar como ponto zero os números de 03/06 — ticket R$ 42,84, Jarra Medidora 500ml liderando com 39,3% do volume, Programa de Frete Grátis em 0% da base ativa, concentração top 3 em 70,2% — e verificar no Seller Center se o zero do Programa de Frete Grátis é configuração histórica ou desativação recente. É o primeiro ciclo de pipeline com a tese seed e memória vazia: sem esses pontos zero, os próximos ciclos não têm baseline para confirmar ou refinar o papel da conta. Confirmar/refutar por: Programa de Frete Grátis nunca ativado = característica estrutural a subir para Pedro na próxima semana; desativado recentemente = identificar data e cruzar com início da queda de 30d. Sem escalonamento previsto para esta prioridade.

Dia analisado: 03/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Anúncio banido (`account_overview.totals.banned=1` — identidade desconhecida)
- **Origem do bloqueio:** L05 Condensadora (fundamentado em L04 Granular)
- **Motivo:** `banned_ids` não exposto no pacote; `top_items_details.items` veio vazio; identidade não recuperável sem consulta manual ao Seller Center
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido integralmente da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Fôlego prospectivo em dias por anúncio da cauda (Pote Vidro 520ml — Quadrado, Kit 2 Potes 800ml — Quadrado, Kit 4 Potes Vidro 520ml Quadrado Hermético Fitness, Kit 4 Descanso de Panela MDF Modular Suporte de Mesa Cozinha)
- **Origem do bloqueio:** L05 Condensadora (fundamentado em L04 Granular)
- **Motivo:** `available_quantity` por anúncio ausente do pacote (`top_items_details.items` vazio); cálculo de fôlego em dias é inconclusivo; só é lícito citar teto operacional no ritmo de 03/06
- **Agregado autorizado:** sim — "teto de ~15 pedidos/dia no ritmo de 03/06, contra média 7d de ~49 pedidos"
- **Tratamento aplicado:** substituído pelo agregado autorizado (teto operacional relativo ao ritmo do dia)
- **Aparece na mensagem final:** sim, como "teto de ~15 pedidos/dia no ritmo de 03/06, contra média 7d de ~49 pedidos"

---

- **Item bloqueado:** Kit 6 Canecas Tulipa / Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha em 3º lugar como evidência de enfraquecimento ou refinamento da tese seed Volume/Giro
- **Origem do bloqueio:** L05 Condensadora (fundamentado em L04 Granular)
- **Motivo:** L04 confirmou contaminação por stock-out simultâneo dos campeões de vidro; confiança baixa; 1 ciclo insuficiente para qualquer leitura de papel
- **Agregado autorizado:** não
- **Tratamento aplicado:** produto aparece no Top Produtos e nos insights apenas como parte da lista de campeões zerados (fato confirmado), sem qualquer leitura de divergência de mix ou tese
- **Aparece na mensagem final:** sim, apenas como campeão com estoque zero e como item da cauda a verificar — sem qualificação de papel

---

- **Item bloqueado:** Comparação cross-account com Budamix Oficial 2 ou Budamix Shop 3; citação nominal de canibalização envolvendo Kit 6 Canecas Tulipa (CTL002)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Regra Shopee — análise por conta isolada; cruzamento cross-account é função da L06b Consolidadora
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido integralmente
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Afirmar que a Saúde da Loja está deteriorando ou que NFR/Pontos de Penalidade estão subindo
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** `shop_performance.status=unavailable` (HTTP 404) — sem dado real; só é lícito declarar risco prospectivo e zona cega de detecção
- **Agregado autorizado:** não
- **Tratamento aplicado:** redigido exclusivamente como risco prospectivo ("o risco prospectivo é jogar a Taxa de Cancelamento do Vendedor muito acima do threshold...") — sem afirmação de deterioração presente
- **Aparece na mensagem final:** não como fato de deterioração; sim como risco prospectivo com linguagem adequada

---

- **Item bloqueado:** `platform_item_id` numérico dos campeões e da cauda em narrativa para Lucas
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Regra Shopee — item_id Shopee numérico proibido na mensagem narrativa
- **Agregado autorizado:** não aplicável (substituído por nomes comerciais)
- **Tratamento aplicado:** todos os anúncios referenciados por nome comercial (slack_short_name ou display_short conforme regra)
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- **Remoção de metadados internos** — campos `padrao`, `base` e `classificacao` não incluídos na mensagem; são metadados de pipeline sem uso no Slack
- **Preservação de nuance `fato` (insight 1)** — escrito como afirmação direta: "fecharam o dia com estoque zero confirmado"; "Não é estabilidade: é o último dia com o portfólio campeão de pé"
- **Preservação de nuance `risco latente` (insight 2)** — linguagem prospectiva obrigatória: "o risco prospectivo é jogar a Taxa de Cancelamento do Vendedor muito acima do threshold"; sem afirmação de deterioração presente
- **Preservação de nuance `hipótese` (insight 3)** — linguagem de indício: "A conta parece estar operando sem nenhuma alavanca de exposição verificável"; "não é momento de mexer... sem informação"
- **Preservação dos 4 elementos densos do risco prospectivo (insight 2)** — (1) estimativa quantitativa: ~15 pedidos/dia vs ~49 da média 7d; (2) threshold com referência: Taxa de Cancelamento do Vendedor < 2% (Vendedor Indicado); (3) janela temporal: D+1, até 10h de 04/06, D+3; (4) fonte alternativa de verificação: Lucas confere NFR e Pontos de Penalidade no Seller Center. Todos 4 presentes.
- **Confiança média** — sem ressalva global de baixa confiança; nuances de classificação preservadas insight a insight
- **Nomes de produtos — Jarra Medidora 500ml (SKU CK4742)** — usado `slack_short_name="Jarra Medidora 500ml"` (mapeamento canônico)
- **Nomes de produtos — Potes Vidro 5 Peças — Tampa Preta (SKU IMB501P)** — usado `slack_short_name="Potes Vidro 5 Peças — Tampa Preta"` (mapeamento canônico); atributo confirmado `confirmed_variation_attributes=["Tampa Preta"]` incorporado no nome conforme regra
- **Nomes de produtos — Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha (SKU CTL002)** — `slack_short_name=null`; usado `display_short="Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha"` verbatim (fallback automático; sem mapeamento manual para SKU CTL002)
- **Nomes de produtos — Pote Vidro 520ml — Quadrado (SKU KIT2YW520SQ)** — usado `slack_short_name="Pote Vidro 520ml — Quadrado"` (mapeamento canônico)
- **Nomes de produtos — Kit 2 Potes 800ml — Quadrado (SKU KIT2YW800SQ)** — usado `slack_short_name="Kit 2 Potes 800ml — Quadrado"` (mapeamento canônico)
- **Nomes de produtos — Kit 4 Potes Vidro 520ml Quadrado Hermético Fitness (SKU KIT4YW520SQ)** — `slack_short_name=null`; usado `display_short="Kit 4 Potes Vidro 520ml Quadrado Hermético Fitness"` verbatim (fallback automático; sem mapeamento manual para SKU KIT4YW520SQ)
- **Nomes de produtos — Kit 4 Descanso de Panela MDF Modular Suporte de Mesa Cozinha (SKU DPM001)** — `slack_short_name=null`; usado `display_short="Kit 4 Descanso de Panela MDF Modular Suporte de Mesa Cozinha"` verbatim (fallback automático; sem mapeamento manual para SKU DPM001)
- **Tradução no insight 2 (L05)** — L05 escreveu "Jarra Medidora de Vidro 500ml", "Conjunto 5 Potes Vidro Redondos Tampa Preta" e "Kit 6 Canecas Tulipa 250ml" nos textos analíticos; substituídos pelos nomes canônicos conforme mapeamento acima em todas as menções da mensagem
- **Omissão de modalidade de envio na seção VISÃO** — `fulfillment_mix_yesterday_top10.status=unavailable`; `fulfillment_mix_30d/7d` também indisponíveis (backfill pendente); dado de mix de ativo (`active_analysis.fulfillment_mix`) cobre panorama estrutural, não pedidos do dia — Condensadora não autorizou exibição; omitido da VISÃO
- **Omissão de fôlego em dias por anúncio** — substituído por teto operacional relativo ao ritmo de 03/06, conforme agregado autorizado pela L05
- **Omissão do anúncio banido** — bloqueio recebido sem agregado autorizado; item omitido
- **Afirmação de estoque como POST-baixa** — toda referência ao estoque zero dos campeões escrita como estado pós-baixa confirmado no snapshot, com risco expressamente prospectivo (D+1 em diante)
- **Atribuição de Lucas como responsável** — todas as prioridades atribuídas a Lucas; sem menção a Himmel salvo onde a Condensadora não trouxe instrução de alinhamento com Himmel (não trouxe neste ciclo)
- **Escalonamento para Pedro preservado** — condição de escalonamento (D+3 sem Saúde da Loja, ou nenhum campeão reposto até 10h de 04/06) mantida conforme L05
- **Simplificação de frases longas** — estruturas tipo "configurando uma conta hipotetizada como Volume/Giro operando hoje sem nenhuma alavanca" reescritas em ordem direta sem alterar sentido analítico