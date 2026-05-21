<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.077,39
- Pedidos: 91 pedidos
- Ticket médio: R$ 55,80
- Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 22 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
- Kit 6 Canequinhas 100ml — 8 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
- Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto — 3 pedidos
- Kit 4 Potes de Vidro 320ml Retangular — 3 pedidos
- Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- A queda de pedidos vs 7d (-20,9%) parece deterioração, mas a comparação correta é a mesma quarta-feira — e ali o volume está essencialmente flat (-1,6%); o GMV acima do histórico vem do ticket em elevação estrutural (R$ 40 na 60d, R$ 44 na 30d, R$ 55,80 hoje), não de força de volume. Tratar o delta 7d como sinal de queda de demanda seria ler o dado errado.
- Um anúncio pausado com estoque zerado gerou 3 pedidos no dia — os 2 cancelamentos registrados hoje não refletem esse risco; se não houver ação, esses 3 pedidos viram cancelamentos planejáveis nos próximos dias, impactando a métrica de reputação sem aviso no agregado de hoje.
- O item com menor cobertura de estoque Full tem poucos dias de unidades no CD do ML, e o listing é de catálogo — ruptura aqui não significa apenas venda perdida: significa perda de posição na página de catálogo do ML para outros sellers, com recuperação mais lenta do que em listing convencional.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar os 3 pedidos do anúncio pausado com estoque zerado e acionar cancelamento controlado ou reposição de emergência antes que o marketplace cancele automaticamente. Anúncio confirmado com status pausado e estoque zerado no CD do ML — sem ação, são cancelamentos prospectivos que afetam a reputação. Confirmar/refutar: se nos próximos 2 dias aparecerem cancelamentos atribuídos a esse anúncio no painel ML, o risco se materializou; se os pedidos forem processados normalmente, confirmar com que estoque foram atendidos. Escalar para Kobe se não houver estoque disponível para atender os 3 pedidos.
- Yasmin: confirmar previsão de reposição para o kit de potes retangulares 1050ml em kit de 2 no CD do ML (cobertura curta, listing de catálogo). Ruptura pode resultar em perda de posição da página de produto para outros sellers. Confirmar/refutar: se reposição confirmada antes do esgotamento, risco desativado; se sem previsão em 48h, ruptura é iminente. Escalar para Kobe se sem previsão de reposição em 48h.
- Yasmin: checar posição de ranking e situação de health do kit de 4 potes retangulares 1050ml em Full (2º produto do dia) no painel ML. O dado atual mostra health abaixo do threshold, mas sem histórico disponível não dá para cravar se está em deterioração ou estabilizado — a incerteza justifica a checagem. Confirmar/refutar: se health estiver em queda nos últimos 7 dias ou posição de ranking caiu, confirma deterioração ativa; se estável ou em recuperação, mantém observação sem ação. Escalar e alinhar com Himmel sobre exposição se health abaixo de 0,70 ou queda de pedidos do item por 2 dias consecutivos.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** TL6250 identificado internamente como "Kit 6 Tigelas de Vidro 250ml"
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** Divergência categórica confirmada — display_name interno e campo title do pacote indicam "Tigelas de Vidro", mas raw_title do pedido e ml_snapshot confirmam produto real como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara"; categorias materialmente diferentes
- **Agregado autorizado:** sim — usar título real do produto confirmado por raw_title/ml_snapshot
- **Tratamento aplicado:** substituído pelo título real "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" na mensagem final
- **Aparece na mensagem final:** sim, como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" (título real validado pela Granular)

---

- **Item bloqueado:** SKUs técnicos (KIT2YW1050, TL6250, 914C_BAV, IMB501P, KIT4YW1050, etc.) e platform_item_ids (MLB*)
- **Origem do bloqueio:** Condensadora
- **Motivo:** Referências técnicas sem valor para a mensagem destinada a Yasmin
- **Agregado autorizado:** sim — usar descrições legíveis dos produtos
- **Tratamento aplicado:** todos os produtos citados na análise e prioridades aparecem por descrição legível, não por SKU ou MLB
- **Aparece na mensagem final:** não (SKUs e MLB omitidos em toda a mensagem)

---

- **Item bloqueado:** Leitura de queda de -20,9% em pedidos vs 7d como deterioração de demanda
- **Origem do bloqueio:** Condensadora
- **Motivo:** Comparação incorreta — a comparação correta (mesmo dia da semana) mostra -1,6%; usar o delta 7d como sinal induziria Yasmin a erro
- **Agregado autorizado:** não aplicável — bloqueio de interpretação, não de produto
- **Tratamento aplicado:** insight preservado com a formulação exata da Condensadora, explicitando que a comparação correta é o mesmo dia da semana
- **Aparece na mensagem final:** não como deterioração; aparece como contextualização correta do dado

---

- **Item bloqueado:** Citar previsão de cobertura de estoque em dias específicos como dado preciso
- **Origem do bloqueio:** Condensadora
- **Motivo:** Cálculos são estimativas de 1 dia de volume; citar número de dias específico passa falsa precisão
- **Agregado autorizado:** sim — usar referência qualitativa ("cobertura curta", "poucos dias")
- **Tratamento aplicado:** nas prioridades, substituído por "cobertura curta" sem número de dias
- **Aparece na mensagem final:** sim, como referência qualitativa sem número preciso

---

- **Item bloqueado:** Health score do KIT4YW1050 como confirmação de deterioração ativa
- **Origem do bloqueio:** Condensadora + Granular
- **Motivo:** Sem histórico de health no pacote — não é possível confirmar deterioração; tratar como sinal não resolvido, não como fato
- **Agregado autorizado:** sim — linguagem de indício/incerteza preservada
- **Tratamento aplicado:** prioridade formulada com "não dá para cravar se está em deterioração ou estabilizado — a incerteza justifica a checagem"
- **Aparece na mensagem final:** sim, com nuance de incerteza preservada

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional`, `— base: Granular + Tática`, etc.) de todos os insights da análise — metadados do pipeline não pertencem à mensagem Slack
- Produto TL6250 substituído pelo título real "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" — bloqueio da Granular/Condensadora por divergência categórica confirmada; raw_title e ml_snapshot prevalecem sobre display_name interno
- Top Produtos: 914C_BAV aparece como "Kit 06 Canequinhas 100ml Com Suporte de Madeira Acrílico" (título legível) — SKU e MLB omitidos; listing pausado com 3 pedidos no dia aparece no ranking porque os pedidos existem no pacote validado; Condensadora não bloqueou o produto do Top Produtos, apenas bloqueou o SKU técnico e os IDs
- Cobertura de estoque do KIT2YW1050 mantida como "cobertura curta" sem número de dias — bloqueio da Condensadora contra falsa precisão em estimativa de 1 dia de volume
- Health do KIT4YW1050 mantido com linguagem de incerteza ("não dá para cravar") — bloqueio da Condensadora contra transformar dado sem histórico em confirmação de deterioração
- Percentual de queda vs 7d preservado no insight 1 apenas como referência contextual, com a inversão da Condensadora explicitada — proibição de tratar -20,9% como sinal de queda de demanda respeitada
- Prioridades formuladas com ação + motivação + sinal de confirmação/refutação + condição de escalonamento — estrutura completa da Condensadora preservada sem criar ação nova
- Yasmin atribuída como responsável nas 3 prioridades — canal Mercado Livre, conforme regra de responsáveis
- Himmel citado na 3ª prioridade (escalonamento sobre exposição) apenas porque a Condensadora trouxe explicitamente esse escalonamento via Yasmin; não adicionado por iniciativa própria
- Ticket médio R$ 55,80 na seção VISÃO — dado objetivo do dia sem comparação temporal (comparações ficaram restritas à ANÁLISE DA CONTA, onde a Condensadora as trouxe)
- IMB501P aparece como "Conjunto 5 Potes de Vidro Redondos Tampa Preta" — variação correta, sem agregar família IMB501 genérica
- IMB501V aparece como "Conjunto 5 Potes de Vidro Redondos Tampa Vermelha" — variação correta, separada de IMB501P; ambas com volumes próprios
- Ranking mantido em ordem decrescente de pedidos: 22, 13, 8, 5, 5, 5, 3, 3, 3, 3 — produtos com mesmo volume (5 pedidos: KIT10YW1050, IMB501V, TL6250) mantidos na ordem do pacote validado, sem reordenação por julgamento próprio
- Faturamento por produto omitido em todos os itens do Top Produtos — pacote não traz receita validada por produto/variação; proibido calcular ou estimar via ticket médio × pedidos