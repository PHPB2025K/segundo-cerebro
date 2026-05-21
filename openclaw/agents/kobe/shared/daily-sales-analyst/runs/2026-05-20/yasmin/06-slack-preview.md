<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.087,71
• Pedidos: 91 pedidos
• Ticket médio: R$ 55,91
• Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 23 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
• Kit 6 Canequinhas 100ml — 8 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
• Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
• Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
• Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
• Suporte Gamer 2 Controles e Headset Mesa PS5/PS4 Preto — 3 pedidos
• Kit 4 Potes de Vidro 320ml Retangular — 3 pedidos
• Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
• O dia parece forte no GMV, mas o resultado é narrow e apoiado em estrutura frágil: o ADS (Himmel) respondeu por cerca de 60% do faturamento, e dois dos campeões em Full operam com health abaixo do threshold do ML — penalização de ranking que o número de ontem não mostra porque o ADS cobriu a exposição. O crescimento de ticket é real, mas depende de manter a composição de campanha e o mix de produto estáveis; qualquer ajuste de verba ou mudança de estratégia desfaz o número sem aviso de volume.
• A queda de 21 pontos no mix de fulfillment não é degradação de infraestrutura Full — é o produto que mais vendeu no dia operando em cross-docking e pesando o agregado para baixo. Tirando esse produto do cálculo, o mix dos demais anúncios volta ao padrão histórico. Não há sinal operacional autônomo aqui.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar estoque disponível do anúncio de baixíssimo estoque (Kit 06 Canequinhas 100ml Acrílico, top10 da conta). O snapshot registrou 3 unidades disponíveis e 3 pedidos ontem — qualquer pedido hoje pode ter zerado o estoque ou disparado pausa automática no ML. Se o anúncio entrou em pausa ou aparecerem cancelamentos ligados a esse produto, avaliar reposição urgente com expedição.
• Yasmin: registrar o ADS share de ontem (~60% do GMV) como primeiro ponto da série e acompanhar nos próximos 2–3 dias. O ROAS está eficiente; o risco não é a campanha em si, é não saber ainda se há base orgânica sustentável por baixo. Se o share ficar acima de 55% por 3 dias seguidos e o GMV começar a cair abaixo de R$ 4.500, alinhar com Kobe.
• Yasmin: registrar os health atuais dos dois campeões em Full (0,75 e 0,71 — ambos abaixo do threshold ML de 0,85) como baseline e calcular a direção no próximo ciclo. Se health cair nos dois por 2 leituras seguidas e GMV ficar abaixo de R$ 4.500, alinhar com Himmel.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** TL6250 pelo display_name interno "Kit 6 Tigelas de Vidro 250ml"
- **Origem do bloqueio:** Granular / Condensadora
- **Motivo:** alias incorreto — o produto real identificado pelo pedido e pelo title do anúncio (MLB6167272090) é "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara"; citar pelo alias nomearia categoria errada (tigelas de vidro ≠ canecas de porcelana)
- **Agregado autorizado:** sim — uso do raw_title "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" como nome identificável do produto real
- **Tratamento aplicado:** substituído pelo nome derivado do raw_title; display_name interno suprimido
- **Aparece na mensagem final:** sim, como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"

---

- **Item bloqueado:** Afirmação ligando os 3 cancelamentos ao anúncio de estoque crítico (MLB4410218897)
- **Origem do bloqueio:** Granular / Condensadora
- **Motivo:** a Granular não encontrou breakdown de cancelamentos por produto; a conexão não está evidenciada
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados apenas como total agregado na VISÃO (3 cancelamentos); nenhuma ligação com o anúncio crítico foi feita
- **Aparece na mensagem final:** não (a ligação); somente o total aparece em VISÃO

---

- **Item bloqueado:** Afirmação de ruptura consumada do anúncio de baixíssimo estoque (MLB4410218897)
- **Origem do bloqueio:** Granular / Condensadora
- **Motivo:** ambiguidade de timing — não é possível confirmar se ruptura já ocorreu ou ainda é iminente
- **Agregado autorizado:** sim — formulação de risco iminente ("pode ter zerado o estoque ou disparado pausa automática")
- **Tratamento aplicado:** formulação preserva indício sem afirmar ruptura como fato
- **Aparece na mensagem final:** sim, como risco iminente com linguagem de indício

---

- **Item bloqueado:** SKUs crus com confidence=medium (914C_BAV, KIT10YW1050, SPC0111, KIT4YW320) citados nominalmente
- **Origem do bloqueio:** Condensadora
- **Motivo:** mapping_reason=mapped_generic_sku; não citar nominalmente
- **Agregado autorizado:** sim — uso dos display_names disponíveis nos dados para os respectivos produtos em Top Produtos
- **Tratamento aplicado:** produtos aparecem pelos nomes de display derivados dos títulos reais, sem SKU cru visível
- **Aparece na mensagem final:** sim, pelos nomes de produto (sem SKU cru)

---

- **Item bloqueado:** Afirmação de que GMV +33% vs 60d representa patamar consolidado
- **Origem do bloqueio:** Condensadora
- **Motivo:** primeiro ciclo com leitura estruturada; sem weekly ou monthly que confirme trajetória; formulação correta é "trajetória de ticket em ascensão", não "patamar estabelecido"
- **Agregado autorizado:** não aplicável (formulação, não produto)
- **Tratamento aplicado:** a análise preserva "o crescimento de ticket é real" sem afirmar patamar consolidado; a comparação temporal foi omitida da seção VISÃO (conforme regra da seção); a nuance de fragilidade foi mantida na ANÁLISE
- **Aparece na mensagem final:** não como afirmação de patamar; sim como crescimento de ticket com ressalva de dependência

---

- **Item bloqueado:** Platform_item_ids técnicos (MLB...) na mensagem final
- **Origem do bloqueio:** Condensadora
- **Motivo:** desnecessários para o responsável operacional
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum MLB aparece na Mensagem Slack
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional + Granular`, `Padrão B`, `Padrão A`) dos dois insights — motivo: linguagem de pipeline interna, proibida na mensagem Slack
- Preservação literal dos dois insights da Condensadora sem reescrita — ambos entregues com linguagem direta e operacional; nenhuma simplificação foi necessária além da remoção dos metadados
- Preservação da nuance "parece forte" (indício, não fato) no primeiro insight — motivo: a Condensadora classificou o padrão como "parece bom, mas estrutura mostra fragilidade"; transformar em "foi forte" inverteria a tese
- Preservação do conectivo "mas" no primeiro insight — motivo: troca por "e" removeria o contraste central da tese (proibição explícita de alteração de conectivo que muda nuance)
- Seção VISÃO sem comparação temporal — motivo: regra da seção; comparações pertencem à ANÁLISE e só se vieram da Condensadora; os dois insights da Condensadora não foram enquadrados como comparação de VISÃO
- TL6250 citado pelo raw_title real ("Kit 6 Canecas Porcelana Tulipa Lisa 250ml") em vez do display_name incorreto — motivo: bloqueio confirmado pela Granular/Condensadora; raw_title + platform_item_id são fonte primária e identificam o produto corretamente
- Top Produtos em ordem decrescente por pedidos (23, 13, 8, 5, 5, 5, 3, 3, 3, 3) — motivo: regra de ranking decrescente; itens empatados em 5 pedidos ordenados conforme posição no pacote validado (IMB501V antes de TL6250 antes de KIT10YW1050)
- Produtos com confidence=medium (KIT10YW1050, SPC0111, KIT4YW320, 914C_BAV) citados pelos títulos derivados do raw_title disponível — motivo: platform_item_id e raw_title presentes no pacote sustentam identificação razoável; sem SKU cru visível conforme bloqueio da Condensadora
- "Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico" usado em vez do display_name truncado "Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico" — motivo: adequação de caixa para leitura no Slack; nome derivado do título real sem desvio de identificação
- Prioridades redigidas em formato `Yasmin: [ação]. [Por quê]. [Sinal]. [Escalar se].` conforme template aprovado — motivo: padrão obrigatório da seção
- Nenhum ASIN exibido (plataforma ML, não Amazon) — motivo: regra de IDs técnicos visíveis aplicável apenas à Amazon quando necessário
- Nenhuma conta Shopee mencionada — motivo: mensagem direcionada a Yasmin/ML; proibição de mistura de plataformas