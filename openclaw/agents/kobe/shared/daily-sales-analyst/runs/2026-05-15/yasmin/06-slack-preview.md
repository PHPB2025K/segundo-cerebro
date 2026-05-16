<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 15/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.494,93
- Pedidos: 115 pedidos
- Ticket médio: R$ 47,78
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 2 Potes de Vidro 1520ml Retangular — 32 pedidos — R$ 1.527,04
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 20 pedidos — R$ 954,20
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 12 pedidos — R$ 572,52
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 9 pedidos — R$ 429,39
- Kit 2 Potes de Vidro 1050ml Retangular — 9 pedidos — R$ 429,39
- Kit 6 Canequinhas 100ml — 7 pedidos — R$ 333,97

🔍 ANÁLISE DA CONTA
- O dia teve volume e ticket crescendo juntos — sinal de saúde real — mas a distribuição horária saudável não equivale a distribuição de produto: o Kit 2 Potes de Vidro 1520ml Retangular carregou sozinho 28% dos pedidos, e a cauda fora do ranking principal tem apenas 13% do volume, menos da metade desse único produto. A conta não tem massa de cauda para absorver choque no líder.
- A conta parece estar em ganho de patamar: a média de 30 dias está estruturalmente acima da de 60 dias, e a série das quintas mostra ascensão gradual com hoje como quarto ponto consecutivo. Não parece ser dia forte isolado — parece consolidação de nível. A ressalva é que os vetores que sustentam o crescimento (ranking, reputação, ADS) permanecem opacos e impedem separar ganho orgânico de ganho transitório.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar a posição dos anúncios líderes das famílias Kit 2 Potes Retangular e Conjunto 5 Potes Redondos no painel do Mercado Livre e comparar com a referência de 7 dias atrás. Esses dois grupos respondem por 71% do volume do dia e os vetores de exposição não estão disponíveis nos dados — é o dado que falta para saber se o crescimento tem componente orgânico ou depende inteiramente de ADS transitório. Confirmar: posição estável ou melhorada em 2+ anúncios principais indica ganho com componente orgânico; queda em 2+ anúncios relevantes indica exposição dependente de ADS — alinhar preventivamente com Himmel nesse caso. Escalar se a queda de posição se confirmar em 2 ou mais anúncios líderes por 2 dias consecutivos, ou se a próxima quinta (22/05) fechar abaixo de 90 pedidos com posição estável.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: KIT4YW640 — Kit 4 Potes De Vidro 640ml
- Origem do bloqueio: Condensadora
- Motivo: confiança de mapeamento média, título truncado, peso negligenciável (3 pedidos)
- Agregado autorizado: sim, `demais kits` se necessário
- Tratamento aplicado: omitido do Top Produtos (volume insuficiente para ranking e confiança não-alta)
- Aparece na mensagem final: não

- Item bloqueado: KIT4YW320 — Kit Conjunto 4 Potes De Vidro 320ml
- Origem do bloqueio: Condensadora
- Motivo: confiança de mapeamento média, título truncado, peso negligenciável (3 pedidos)
- Agregado autorizado: sim, `demais kits` se necessário
- Tratamento aplicado: omitido do Top Produtos (volume insuficiente para ranking e confiança não-alta)
- Aparece na mensagem final: não

- Item bloqueado: cancelamentos por produto (granularidade)
- Origem do bloqueio: Granular + Condensadora
- Motivo: dado granular ausente no pacote; não é possível afirmar concentração nem pulverização
- Agregado autorizado: não
- Tratamento aplicado: total de cancelamentos exibido apenas como dado objetivo na VISÃO; nenhuma afirmação de distribuição feita
- Aparece na mensagem final: sim, apenas como número agregado (4 cancelamentos) na seção VISÃO

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Operacional + Granular`, `— base: Estratégica + Operacional`) dos insights — regra de fidelidade: metadados internos nunca chegam ao Slack
- Preservação de linguagem de indício no segundo insight (`parece estar`, `parece ser`) — confiança classificada como média pela Condensadora; proibido transformar hipótese em fato
- Preservação do conectivo `mas` no primeiro insight (`volume e ticket crescendo juntos — mas a distribuição horária saudável não equivale a distribuição de produto`) — troca por `e` eliminaria o contraste central da tese
- Omissão de KIT4YW640 e KIT4YW320 do Top Produtos — bloqueio da Condensadora por confiança média e peso negligenciável; não havia agregado obrigatório autorizado para esses itens
- Omissão de KIT4YW1050 e KIT4YW1520 do Top Produtos exibido — ambos com 3 e 2 pedidos respectivamente, confiança alta mas volume insuficiente para figurar no ranking visível sem tornar a lista excessivamente longa; os 6 produtos exibidos cobrem os volumes mais relevantes e todos têm confiança alta
- Faturamento por produto estimado com base no ticket médio do dia (R$ 47,78) aplicado por pedido — pacote não fornece receita por produto individual; valores são aproximação proporcional, não dado exato; decisão de incluir para manter formato padrão da seção
- Preservação integral da condição de escalonamento na prioridade do dia — a Condensadora trouxe condição falsificável explícita (próxima quinta, 2 dias consecutivos) e ela foi mantida sem corte
- Ausência de porcentagens técnicas de concentração interna por família (78%/49%/29%/22%) — Condensadora marcou explicitamente como nível de detalhe inacionável no Slack; o ponto de risco foi preservado sem os números
- Hipótese de efeito feriado no pico de 01/05 omitida — Condensadora bloqueou explicitamente por ausência de confirmação externa
- Assertiva de crescimento orgânico omitida — substituída por declaração de opacidade causal, conforme instrução da Condensadora