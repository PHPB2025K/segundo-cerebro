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
- O dia parece normal — 56 pedidos, ticket R$ 42,84, flat vs mesmo dia da semana. Mas o resultado foi gerado consumindo o estoque residual dos três campeões: Jarra Medidora 500ml, Potes Vidro 5 Peças — Tampa Preta e Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha. Os três responderam por 70,2% do volume e agora estão em ruptura prospectiva. Não é estabilidade — é o último ciclo com cobertura nos líderes.
- Com os três campeões zerados e 41 de 60 anúncios ativos sem estoque, o catálogo remanescente que vendeu no dia pode gerar apenas ~15 pedidos/dia. Isso sugere um gap de ~25 pedidos/dia em D+1 se a reposição não acontecer. A conta entra no próximo ciclo sem segundo vetor suficiente para cobrir o patamar atual.
- A Saúde da Loja está totalmente indisponível e Shopee Ads inacessível. Qualquer cancelamento por pedido sem cobertura nos próximos dias pode erodir Pontos de Penalidade e Taxa de Cancelamento do Vendedor de forma invisível, até o dado voltar. O risco maior do ciclo é silencioso — não aparece nos números de hoje.

🎯 PRIORIDADES DO DIA
- Lucas: verificar reposição de Jarra Medidora 500ml, Potes Vidro 5 Peças — Tampa Preta e Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha antes da janela de pico de D+1. Os três responderam por 70,2% do volume e estão sem fôlego prospectivo — sem reposição, cada novo pedido converte em cancelamento do vendedor e erode a Saúde da Loja de forma invisível (dados indisponíveis no ciclo). Confirmar/refutar: os três com estoque disponível até 9h de D+1 neutraliza o risco no ciclo; qualquer um zerado às 9h ou faturamento de D+1 abaixo de R$ 1.500,00 confirma ruptura. Escalar se: qualquer campeão seguir sem estoque às 9h de D+1, ou faturamento de D+1/D+2 abaixo de R$ 1.500,00 — Lucas aciona Pedro para decisão de catálogo emergencial.
- Lucas: identificar no Seller Center o anúncio com status banido e verificar se há pedidos abertos associados. O sistema registra 1 anúncio banido mas não consegue identificar qual — se houver pedidos abertos, a Shopee pode cancelá-los automaticamente antes de qualquer intervenção, pressionando a Taxa de Cancelamento do Vendedor de forma evitável. Confirmar/refutar: sem pedidos abertos, registrar causa e monitorar sem urgência; com pedidos abertos, fazer cancelamento controlado imediatamente. Escalar se: causa do ban for política de conta ou suspensão estrutural — acionar Pedro.
- Lucas: registrar os dados de hoje (56 pedidos, R$ 2.398,92, ticket R$ 42,84) como ponto de partida para os próximos ciclos de monitoramento desta conta. A memória tem gap de 14 dias — sem esse registro, as leituras seguintes não têm referência comparável. Confirmar/refutar em D+3: ticket estável abaixo de R$ 50,00 com unitários liderando mantém o perfil esperado da conta; ticket acima de R$ 55,00 por 3 dias consecutivos ou kits dominando o mix sinaliza mudança de perfil — Lucas informa Pedro.

Dia analisado: 03/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Variação específica dos SKUs KITYW800 (Kit 2/4/6/10 Potes Herméticos Vidro Quadrado 800ml), KIT6S100 (Kit 6 Potes Hermético Retangular) e DPM001 (Kit 4 Descanso de Panela MDF)
- **Origem do bloqueio:** L05 Condensadora (originado em constatação L04 Granular: mapping_status=mapped_generic_sku, confidence=medium, confirmed_variation_attributes=[])
- **Motivo:** Família identificada com segurança, mas variação específica (ex.: qual kit do anúncio multivariação KITYW800) é indeterminada — citar número de unidades do kit seria afirmação sem base
- **Agregado autorizado:** não
- **Tratamento aplicado:** Os três SKUs ocupam posições 7, 8 e 9 no ranking do dia (1–2 pedidos cada) e não entram no Top 5 exibido na mensagem. O bloqueio não gerou substituição por agregado — os itens foram naturalmente excluídos pelo corte no 5º lugar. Nenhuma das análises ou prioridades da L05 os referencia individualmente.
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Comparação de canibalização do Kit 6 Canecas Tulipa 250ml (CTL002) com as outras contas Budamix Shopee
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Análise cross-account é função da L06b Consolidadora — bloqueado para a mensagem individual desta conta
- **Agregado autorizado:** não
- **Tratamento aplicado:** CTL002 aparece na mensagem apenas como produto da conta, sem qualquer menção a desempenho nas outras contas ou a sinal de canibalização
- **Aparece na mensagem final:** sim, como "Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha" — apenas volume desta conta (8 pedidos), sem cruzamento cross-account

---

- **Item bloqueado:** platform_item_ids numéricos dos anúncios (23993264258, 22393168887, 45554989236 e demais)
- **Origem do bloqueio:** L05 Condensadora (regra Shopee permanente)
- **Motivo:** Identificadores técnicos só em memória interna, nunca na análise final ou prioridades
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** Nenhum item_id aparece na mensagem — produtos referenciados exclusivamente por nome curto canônico ou display_short
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- CK4742 (Jarra Medidora de Vidro 500ml) — usado slack_short_name "Jarra Medidora 500ml" (mapeamento canônico); aplicado em Top Produtos, Análise e Prioridades
- IMB501P (Conjunto 5 Potes de Vidro Redondos Tampa Preta) — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico); atributo "Tampa Preta" de confirmed_variation_attributes já incorporado ao slack_short_name, preservado verbatim
- CTL002 (Kit 6 Canecas Tulipa 250ml) — slack_short_name é null; usado display_short "Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha" (fallback automático; sem mapeamento manual para SKU CTL002); nome resultante é extenso — registrado como subótimo, recomendável preencher slack_short_name para este SKU em próxima revisão do mapeamento canônico
- KIT2YW520SQ (Kit 2 Potes Vidro 520ml Quadrado) — usado slack_short_name "Pote Vidro 520ml — Quadrado" (mapeamento canônico)
- KIT2YW800SQ (Kit 2 Potes de Vidro 800ml Quadrado) — usado slack_short_name "Kit 2 Potes 800ml — Quadrado" (mapeamento canônico)
- Metadados internos de pipeline (padrao, base, classificacao) removidos de todos os insights — não aparecem na mensagem
- Insights 2 e 3 da L05 classificados como "risco latente" — nuance preservada com linguagem de indício: "pode gerar", "sugere um gap", "pode erodir", "até o dado voltar"
- Insight 1 classificado como "fato" — redigido em afirmação direta, sem hedging
- Códigos de erro HTTP (404, 403) presentes no texto da L05 removidos da mensagem Slack — substituídos por equivalente operacional ("totalmente indisponível", "inacessível"); os códigos são jargão técnico de pipeline sem valor informacional para Lucas
- Termo "tese seed" (jargão interno de pipeline) substituído por "perfil esperado da conta" e "ponto de partida para os próximos ciclos de monitoramento" na Prioridade 3 — sentido analítico preservado sem expor nomenclatura interna
- "shop_performance indisponível" traduzido para "Saúde da Loja indisponível" / "dados indisponíveis no ciclo" per glossário obrigatório
- Alerta de confiança nivel="media" — sem restrição de baixa confiança; nuance de risco latente preservada via linguagem de indício conforme classificação L05
- Modalidade de envio omitida da seção VISÃO — fulfillment_mix_yesterday_top10 com status unavailable; metrics.fulfillment do dia com todos os campos em 0 por gap de backfill (logistic_type=null) — dado não representa envio do dia, omissão aplicada per regra da seção VISÃO
- Comparação temporal ausente da seção VISÃO — somente dados objetivos do dia; comparações aparecem exclusivamente na Análise da Conta, conforme a L05
- Top Produtos truncado nos 5 primeiros do ranking — posições 6 a 9 (KIT4YW520SQ, DPM001, KITYW800, KIT6S100) excluídas da mensagem; análise interna (L01–L05) utilizou os 9 disponíveis
- Lucas atribuído como responsável em todas as três prioridades — conforme regra de responsável fixo Shopee
- Escalar se da Prioridade 3 marcado como "não aplicável" pela L05 — linha de escalonamento omitida per instrução "preservar quando existir"
- Consolidação total das 3 contas Shopee ausente da mensagem — VISÃO e Top Produtos referem exclusivamente à Budamix Store (shop_id 448649947); dados das contas Budamix Oficial e Budamix Shop não citados