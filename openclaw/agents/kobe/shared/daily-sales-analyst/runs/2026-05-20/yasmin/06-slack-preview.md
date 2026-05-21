<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.077,39
• Pedidos: 91 pedidos
• Ticket médio: R$ 55,80
• Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 22 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
• Kit 6 Canequinhas 100ml — 8 pedidos
• Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
• Kit 6 Tigelas de Vidro 250ml — 5 pedidos
• Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
• Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto — 3 pedidos
• Kit Conjunto 4 Potes De Vidro 320ml Tampa Hermético 4 Travas Azul-petróleo — 3 pedidos
• Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
• A queda de -20,9% nos pedidos vs a última semana não é deterioração — é regressão ao patamar normal da conta. A média dos últimos 7 dias estava inflada (cerca de 26% acima da base dos últimos 60 dias), então qualquer comparação contra ela distorce a leitura. Controlando pelo mesmo dia da semana, os pedidos ficaram praticamente flat e o GMV superou a média sazonal em 32%. O dia fechou onde a conta historicamente opera, não abaixo.
• A conta gerou um terço a mais de receita que sua base bimestral com o mesmo número de pedidos — isso vem do ticket subindo (de ~R$ 42 para R$ 55,80), não de mais vendas. Essa expansão aparece de forma consistente em todas as janelas de comparação disponíveis, o que enfraquece a hipótese de ruído e aponta para uma mudança real de mix em direção a produtos de maior valor.
• O risco de dependência do grupo de potes redondos é maior do que o produto líder isolado sugere: as duas variações da família juntas somam cerca de 30% da conta. Sem dado de posição orgânica dos anúncios desse grupo no pacote de hoje, a saúde de exposição desse grupo continua como a maior incógnita ativa — e nenhuma das lacunas (cancelamentos por produto, ranking) foi respondida pelo dado disponível.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar posição e exposição dos anúncios do grupo de potes redondos diretamente na plataforma ML. Esse grupo responde por cerca de 30% da conta e o pacote de hoje não inclui nenhum dado de ranking ou exposição orgânica — a tese de expansão de receita depende da continuidade de visibilidade desse grupo. Se a posição dos anúncios principais caiu em 2 ou mais posições vs semana anterior, alinhar com Himmel sobre ADS ML. Se estável, manter observação sem mexer. Escalar se queda de posição for confirmada em 2 ou mais dias consecutivos.
• Yasmin: acompanhar o ticket médio nos próximos 2-3 dias controlando por dia da semana. O mecanismo de expansão de receita de hoje é inteiramente dependente do ticket. Ticket acima de R$ 50 por 3 dias seguidos confirma a tese de ganho de patamar como estrutural. Ticket abaixo de R$ 45 em 2 dos próximos 4 dias revisa o diagnóstico — nesse caso escalar para decisão estrutural.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs técnicos (KIT2YW1050, IMB501P, IMB501V, KIT4YW1050 etc.) e IDs de anúncio (MLBs)
- Origem do bloqueio: Condensadora
- Motivo: não relevantes para mensagem operacional
- Agregado autorizado: não aplicável (supressão total)
- Tratamento aplicado: omitidos; produtos referenciados apenas por display_name
- Aparece na mensagem final: não

- Item bloqueado: anomalia de razão itens/pedido do Kit 2 Potes de Vidro 1050ml Retangular (2,67 itens/pedido)
- Origem do bloqueio: Condensadora
- Motivo: causa indeterminada; não pode ser interpretada sem checagem de listing
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem
- Aparece na mensagem final: não

- Item bloqueado: origem dos 2 cancelamentos por produto
- Origem do bloqueio: Condensadora
- Motivo: dado desagregado por produto indisponível no pacote; risco de afirmação incorreta
- Agregado autorizado: não (apenas total de 2 cancelamentos permitido na seção VISÃO)
- Tratamento aplicado: citado apenas como total na VISÃO; sem atribuição a produto
- Aparece na mensagem final: sim, como total (2 cancelamentos) sem desagregação

- Item bloqueado: SPC0111 (Suporte Gamer) como evidência de diversificação de mix
- Origem do bloqueio: Condensadora
- Motivo: produto fora da categoria principal com confidence medium e mapeamento genérico
- Agregado autorizado: não (produto pode aparecer no ranking de pedidos, mas não pode ser citado como dado confiável de mix na análise)
- Tratamento aplicado: aparece no Top Produtos pelo volume de pedidos (3 pedidos, 9º lugar); não citado na análise
- Aparece na mensagem final: sim, no Top Produtos apenas com pedidos; ausente da análise

- Item bloqueado: afirmação sobre posição orgânica ou ranking do anúncio líder
- Origem do bloqueio: Condensadora
- Motivo: dado não disponível no pacote; proibido tratar ausência de problema como confirmação de saúde
- Agregado autorizado: não
- Tratamento aplicado: referenciado como lacuna ativa e prioridade de checagem, sem afirmação de saúde
- Aparece na mensagem final: sim, como incógnita e ação para Yasmin

- Item bloqueado: percentual exato de 29,7% da família IMB501 como número central da mensagem
- Origem do bloqueio: Condensadora
- Motivo: proibido virar manchete de métrica; usar formulação descritiva
- Agregado autorizado: sim, "grupo de potes redondos" com "cerca de 30%"
- Tratamento aplicado: substituído por "grupo de potes redondos" e "cerca de 30%"
- Aparece na mensagem final: sim, como agregado descritivo autorizado

---

### Decisões de formatação

- Remoção de `— base: Estratégica + Operacional` e `— base: Granular + Tática` dos três insights — metadados internos de pipeline, não devem aparecer no Slack
- Preservação da nuance de hipótese na tese de ticket — "aponta para uma mudança real de mix" mantém a formulação da Condensadora sem transformar em certeza
- Preservação da ressalva de incógnita ativa na análise do grupo de potes redondos — "continua como a maior incógnita ativa" mantém o tom de dado ausente, não confirmação de saúde
- Substituição de "família IMB501" por "grupo de potes redondos" e "29,7%" por "cerca de 30%" — conforme bloqueio da Condensadora de não usar SKU técnico como manchete e não usar percentual exato como número central
- SPC0111 mantido no Top Produtos (9º lugar, 3 pedidos, confidence medium, produto com platform_item_id confirmado e volume real); ausente da análise conforme bloqueio — decisão item: título visível é suficientemente identificável e não ambíguo; ASIN não aplicável (plataforma ML); nenhuma ressalva de identificação necessária no Slack para esse nível de cauda
- Kit 10 Potes Herméticos 1050ml (4º lugar, 5 pedidos, confidence medium) e Kit 06 Canequinhas com Suporte Acrílico (10º lugar, 3 pedidos, confidence medium) mantidos no Top Produtos pelo mesmo motivo — platform_item_id confirmado, título real do listing disponível, risco de identificação de display_name interno não afeta a mensagem operacional
- Quebra de frase não aplicada — os três insights da Condensadora já estão em extensão adequada para o Slack
- Ranking mantido em ordem decrescente por pedidos: 22, 13, 8, 5, 5, 5, 3, 3, 3, 3 — empates na cauda (posições 4-6 com 5 pedidos e posições 7-10 com 3 pedidos) mantidos na ordem do pacote validado, sem reordenação por conta própria
- Prioridades do dia preservam ação + evidência + sinal de confirmação/refutação + condição de escalonamento conforme saída da Condensadora — sem encurtamento que perdesse as condições táticas