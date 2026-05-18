<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 17/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.180,78
- Pedidos: 100 pedidos
- Ticket médio: R$ 51,81
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 21 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 15 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 11 pedidos
- Kit 2 Potes de Vidro 1520ml Retangular — 9 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 9 pedidos
- Kit 6 Canequinhas 100ml — 3 pedidos

🔍 ANÁLISE DA CONTA
- O risco de concentração não está distribuído pela família de potes redondos como bloco — está em um único anúncio que responde por 36% de todos os pedidos da conta. As duas variações mais vendidas, tampa preta e tampa cinza, rodam no mesmo anúncio: uma queda de posição derruba as duas de uma vez. A checagem de ranking não é precaução geral — é a verificação mais importante que existe hoje na conta.
- O dia cresceu em faturamento porque o ticket médio subiu, não porque a conta vendeu mais. Pedidos ficaram dentro da banda histórica, mas o GMV está bem acima — o que é positivo, mas com fundamento parcial: não há dado disponível que explique por que o ticket subiu. Sem essa resposta, o R$ 51,81 fica registrado como baseline, mas não confirmado como patamar sustentável.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar ranking e posição do anúncio principal dos potes redondos no ML — o anúncio que concentra as variações de tampa preta e tampa cinza. Esse único anúncio responde por 36% do volume total da conta; se perdeu posição, o impacto pode já estar acontecendo sem aparecer no resultado de hoje. Confirmar/refutar: posição estável nas últimas 24–48h confirma que o resultado não está sob ameaça imediata. Escalar se posição caiu em relação à última semana — alinhar com Himmel sobre exposição via ADS.
- Yasmin: registrar o ticket médio de hoje (R$ 51,81) como referência explícita para os próximos dias. Weekly e monthly estão sem dados históricos processados — este é o ponto zero da série. Confirmar/refutar: ticket acima de R$ 46,00 por dois dias seguidos confirma que o nível não é pontual; queda abaixo de R$ 46,00 por dois dias consecutivos nos próximos 5 dias indica ganho dependente de evento, não de mix sustentado. Escalar se ticket cair abaixo de R$ 46,00 por dois dias seguidos — escalar para Kobe reavaliar tese de patamar.

Dia analisado: 17/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: IDs técnicos de listing (MLB3288536143, MLB4535659243)
- Origem do bloqueio: Condensadora
- Motivo: IDs técnicos internos sem relevância operacional para o destinatário
- Agregado autorizado: sim, `anúncio principal dos potes redondos` / `anúncio que concentra as variações de tampa preta e tampa cinza`
- Tratamento aplicado: substituído por agregado autorizado em toda a mensagem
- Aparece na mensagem final: sim, como agregado `anúncio principal dos potes redondos`

- Item bloqueado: SKUs brutos (IMB501P, IMB501C, IMB501V, KIT2YW1520, KIT4YW1050 e demais)
- Origem do bloqueio: Condensadora
- Motivo: SKUs técnicos não visíveis para o responsável operacional
- Agregado autorizado: sim, nomes de display por variação vendável
- Tratamento aplicado: substituído por display_name em Top Produtos; análise usa agregados descritivos
- Aparece na mensagem final: não (SKUs brutos); sim, como nomes de variação (Tampa Preta, Tampa Cinza, etc.)

- Item bloqueado: hipótese sobre origem do ticket elevado (reajuste, desconto, mix)
- Origem do bloqueio: Condensadora
- Motivo: inconclusivo por falta de dado de preço e promoção
- Agregado autorizado: não
- Tratamento aplicado: preservada a opacidade da causa — "não há dado disponível que explique por que o ticket subiu"
- Aparece na mensagem final: não como hipótese afirmada; aparece como ausência confirmada de dado

- Item bloqueado: padrão horário do bloco 11h–15h (comparação histórica com sábados anteriores)
- Origem do bloqueio: Condensadora
- Motivo: comparação histórica não disponível; afirmar como dado confirmado seria erro
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem final
- Aparece na mensagem final: não

- Item bloqueado: gap de schema de fulfillment para ML Full
- Origem do bloqueio: Condensadora
- Motivo: limitação técnica interna, sem relevância para a mensagem operacional
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem final
- Aparece na mensagem final: não

- Item bloqueado: distribuição uniforme de 3 pedidos nos produtos de posição 6–10
- Origem do bloqueio: Condensadora
- Motivo: detalhe granular sem ação associada hoje
- Agregado autorizado: não
- Tratamento aplicado: produtos de posição 6–10 omitidos do Top Produtos (apenas os com ação ou volume relevante foram incluídos)
- Aparece na mensagem final: não — Top Produtos encerra em posição 6 (Kit 6 Canequinhas 100ml, 3 pedidos, confidence high); posições 7–10 com confidence medium e sem ação omitidas

- Item bloqueado: nível de confiança médio dos produtos de cauda
- Origem do bloqueio: Condensadora
- Motivo: risco residual interno que não afeta a leitura central
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem final; apenas produtos high confidence ou com base sólida incluídos nominalmente
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Operacional + Granular`, `— base: Estratégica + Granular`, referências a Padrão E/B) — metadados de pipeline não devem aparecer no Slack
- Substituição de IDs de listing por agregado descritivo autorizado pela Condensadora — preserva o sentido operacional sem expor técnico
- Substituição de SKUs brutos por display_name por variação vendável — regra de Top Produtos para ML
- Preservação de ressalva explícita no segundo insight ("fundamento parcial", "não confirmado como patamar sustentável") — confiança média marcada pela Condensadora; hipótese não vira fato
- Preservação de linguagem de indício ("não há dado disponível que explique por que o ticket subiu") — origem do ticket inconclusiva por falta de dado; proibido transformar ausência de dado em certeza
- Omissão dos produtos de posição 7–10 (KIT6S100, KIT2YW640, KIT4YW640, KIT4YW320) do Top Produtos — todos com confidence medium e bloqueio implícito de detalhe granular sem ação; Kit 6 Canequinhas (posição 6, confidence high) mantido
- Omissão do padrão horário 11h–15h — comparação histórica indisponível; Condensadora bloqueou
- Omissão do gap de fulfillment ML Full — limitação técnica interna
- Prioridades redigidas com estrutura completa: ação + por quê + sinal de confirmação/refutação + condição de escalonamento — exigência do prompt para prioridades com esses elementos na fonte
- Ticket registrado como "R$ 51,81" e limiar de escalonamento como "R$ 46,00" — padrão numérico obrigatório com duas casas decimais
- Top Produtos em ordem decrescente por pedidos (21 → 15 → 11 → 9 → 9 → 3) — ranking obrigatório