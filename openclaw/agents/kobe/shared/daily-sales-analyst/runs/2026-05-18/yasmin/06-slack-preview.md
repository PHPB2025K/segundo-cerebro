<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 18/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 4.184,38
• Pedidos: 96 pedidos
• Ticket médio: R$ 43,59
• Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 35 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 16 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 9 pedidos
• Suporte Gamer 2 Controles e Headset Mesa Ps5 Ps4 Preto — 4 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 4 pedidos
• Kit 6 Canequinhas 100ml — 3 pedidos
• Kit 6 Xícaras Porcelana Paris 170ml — 3 pedidos

🔍 ANÁLISE DA CONTA
• O resultado parece fraco por causa da comparação com os últimos 7 dias (-14,6%), mas a leitura correta é outra: a média de 7d foi puxada para cima por dias úteis recentemente mais fortes. Comparado com os últimos quatro domingos, hoje ficou acima: +3% GMV e +0,8% pedidos. Domingo é estruturalmente mais lento nesta conta; o resultado está dentro do esperado, não abaixo.
• A conta entregou um domingo sólido, mas inteiramente apoiada em um único listing com três variações de cor que concentra 62,5% dos pedidos — e dentro desse listing, a variação Tampa Preta responde sozinha por mais de um terço do volume total da conta. O restante do mix está pulverizado em sete produtos com 3 a 4 pedidos cada, sem nenhum candidato visível a segundo vetor. Se esse listing perder ranking, exposição ou tiver problema de estoque, não há nada no mix que absorva o impacto.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar posição e saúde dos anúncios líderes do grupo de potes redondos nos próximos 2 dias. 62,5% do volume saiu de um único listing — se a posição estiver caindo, não há segundo vetor para compensar. Confirmar: posição estável em 3+ anúncios da família dentro de 48h → campeão sustentado, nenhuma ação adicional. Refutar: posição caiu em 2+ anúncios líderes → alinhar com Himmel sobre ADS ML.
• Yasmin: checar status de Full ML para os anúncios líderes do grupo de potes redondos. Sem esse dado, não é possível saber se a competitividade do campeão da conta está sustentada por fulfillment ou apenas por posição orgânica. Full ativo e estável → fecha a dúvida; Full inativo ou parcial → abre investigação de competitividade.
• Yasmin: observar nos próximos dias se algum produto fora do grupo de potes redondos aparece com 5+ pedidos por 2 dias seguidos. A cauda atual está pulverizada: sete produtos entre 3 e 4 pedidos cada, sem candidato emergindo. Se a dispersão se repetir → confirma dependência crônica e o risco sobe de prioridade para a semana. Se concentração acima de 60% confirmar por 3 dias consecutivos sem candidato emergente → escalar para Kobe.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: platform_item_id MLB3288536143
- Origem do bloqueio: Condensadora
- Motivo: detalhe técnico interno, não necessário para a leitura operacional
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: raw_skus das variações (IMB501P_T, KITIMB501P_T, IMB501PT, etc.)
- Origem do bloqueio: Condensadora
- Motivo: nível técnico de mapeamento, não acionável pela Yasmin
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: distribuição horária detalhada
- Origem do bloqueio: Condensadora
- Motivo: nenhuma anomalia de janela identificada, dado não muda a leitura
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: SPC0111, KIT4YW320, KIT4YW640, 914C_BAV (nomes individuais com mapeamento medium confidence)
- Origem do bloqueio: Condensadora
- Motivo: mapeamento medium confidence; instrução é usar "demais produtos da cauda" sem nomear individualmente se necessário
- Agregado autorizado: sim, "demais produtos da cauda" — mas a prioridade não exigiu nomeação individual; os itens foram simplesmente omitidos do corpo analítico
- Tratamento aplicado: omitidos da seção de análise; não aparecem nas prioridades; aparecem no Top Produtos apenas os produtos com mapeamento high confidence (IMB501P, IMB501C, IMB501V, KIT4YW1050, 914C, XCP002) e SPC0111 (medium, mas com título suficientemente identificável e volume de 4 pedidos — ver Decisões de formatação)
- Aparece na mensagem final: SPC0111 aparece no Top Produtos (ver decisão abaixo); KIT4YW320, KIT4YW640, 914C_BAV omitidos do Top Produtos

- Item bloqueado: detalhe dos 13 pedidos além do top 10 não identificados individualmente
- Origem do bloqueio: Condensadora
- Motivo: dado incompleto, não acionável
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: 914C e 914C_BAV compartilham platform_item_id — detalhe de estrutura de listing
- Origem do bloqueio: Condensadora
- Motivo: detalhe técnico não acionável no Slack
- Agregado autorizado: não
- Tratamento aplicado: omitido da análise; 914C aparece no Top Produtos como "Kit 6 Canequinhas 100ml" apenas pelo volume de 3 pedidos; 914C_BAV omitido (medium confidence, mesmo listing, evita duplicação)
- Aparece na mensagem final: 914C aparece como "Kit 6 Canequinhas 100ml — 3 pedidos"; 914C_BAV não aparece

- Item bloqueado: cancelamento único sem dado de produto associado
- Origem do bloqueio: Condensadora
- Motivo: irrelevante e sem evidência para citar no corpo analítico
- Agregado autorizado: não aplicável — número de cancelamentos (1) aparece na VISÃO como dado objetivo; a análise do cancelamento foi omitida
- Tratamento aplicado: número registrado na VISÃO como dado factual; nenhuma análise sobre o cancelamento incluída
- Aparece na mensagem final: sim, como dado objetivo na VISÃO (1 cancelamento)

- Item bloqueado: dado de Full ML ausente descrito como falha técnica do pacote
- Origem do bloqueio: Condensadora
- Motivo: a mensagem deve ser a checagem recomendada, não a ausência como problema de dados
- Agregado autorizado: não aplicável
- Tratamento aplicado: a prioridade foi formulada como ação de checagem de Yasmin, sem mencionar ausência de dado no pacote
- Aparece na mensagem final: não como falha técnica; sim como checagem ativa

- Item bloqueado: status interno de mapeamento de SKUs e confiança de identificação
- Origem do bloqueio: Condensadora
- Motivo: metadado interno, não necessário no Slack
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção do trecho `— base: Estratégica + Operacional` e `— base: Granular + Operacional + Estratégica` dos insights — metadados internos de camadas, proibidos no Slack
- Remoção do padrão classificatório interno (C — inversão negativa, B — inversão positiva, F — métrica ok) — nomenclatura interna de pipeline
- Preservação integral da tese de ambos os insights da Condensadora, incluindo conectivos e nuances ("mas", "inteiramente apoiada", "não há nada no mix que absorva") — proibido trocar conectivos que mudam nuance
- SPC0111 incluído no Top Produtos com 4 pedidos, apesar de confidence medium — decisão: o título "Suporte Gamer 2 Controles e Headset Mesa Ps5 Ps4 Preto" é suficientemente identificável e o volume (4 pedidos, empatado com KIT4YW1050) justifica inclusão; registrado aqui para QA
- KIT4YW320, KIT4YW640, 914C_BAV omitidos do Top Produtos — confidence medium, volume de 3 pedidos cada, não determinantes para a leitura; a Condensadora bloqueou nomeação individual de itens medium confidence na análise; mesma cautela aplicada ao Top Produtos para itens com título truncado ou ambíguo
- 914C aparece como "Kit 6 Canequinhas 100ml" no Top Produtos (high confidence, 3 pedidos); 914C_BAV omitido — mesmo platform_item_id MLB4410218897, medium confidence; consolidar os dois seria somar variações possivelmente distintas sem autorização explícita; manter só o high confidence
- Top Produtos em ordem decrescente de pedidos: 35, 16, 9, 4, 4, 3, 3 — ranking preservado; empate 4+4 (SPC0111 e KIT4YW1050) mantido na ordem do pacote validado
- KIT4YW1050 com display_name "Kit 4 Potes de Vidro 1050ml Retangular" usado no lugar do raw_title — high confidence, revisado, mais claro para o destinatário
- Faturamento por produto omitido de todo o Top Produtos — o pacote não traz receita validada por variação; proibido calcular, estimar ou aproximar
- Seção VISÃO sem comparação temporal — dados objetivos do dia apenas, conforme regra
- Prioridades com estrutura ação + por quê + confirmar/refutar + escalar se — preservadas da Condensadora, com linguagem direta para Yasmin
- Ausência de Full ML formulada como checagem ativa, não como falha de dado — conforme instrução da Condensadora
- Condensadora entregou 2 insights; ambos usados — dentro do limite de até 3; nenhum insight de enchimento adicionado
- Metadado `send_real_allowed = false` não incluído na mensagem — é instrução de execução, não conteúdo Slack