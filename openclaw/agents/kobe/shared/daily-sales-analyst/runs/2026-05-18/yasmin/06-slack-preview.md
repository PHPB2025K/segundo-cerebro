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
• Suporte Gamer 2 Controles e Headset Mesa PS5/PS4 — 4 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 4 pedidos
• Kit 6 Canequinhas 100ml — 3 pedidos
• Kit 6 Xícaras Porcelana Paris 170ml — 3 pedidos
• Kit 4 Potes de Vidro 640ml — 3 pedidos

🔍 ANÁLISE DA CONTA
• Os 62,5% do volume que aparecem na família de potes redondos não estão distribuídos em 3 produtos — estão concentrados em 1 único anúncio com 3 variações de cor. Qualquer problema de ranking, listing ou estoque nesse anúncio afeta as 3 variações ao mesmo tempo, sem nenhum produto na cauda capaz de compensar. O risco é mais concentrado do que o percentual por família sugere.
• A queda de –15% contra a média de 7 dias não é deterioração. Comparado com os domingos recentes, o dia ficou dentro da banda esperada (+0,8% em pedidos, +3% em GMV). O gap com o 7d é explicado por dias de semana mais fortes puxando a média para cima, não por perda de patamar.
• Fora do anúncio principal de potes redondos, a conta tem 36 pedidos espalhados em 6 anúncios distintos, nenhum chegando a 5 pedidos. A ausência de segundo vetor foi confirmada produto a produto: nenhum item tem volume ou trajetória para compensar o campeão se ele travar.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar no painel do vendedor ML a posição do anúncio principal de potes redondos nos últimos 7 dias. 62,5% do volume depende de 1 único anúncio e o pipeline não tem esse dado — é a única forma de saber se a exposição está estável ou em erosão silenciosa. Posição estável ou crescente confirma que o volume está ancorado; queda de posição com volume ainda sustentado abre alerta para alinhar com Himmel sobre ADS ML. Escalar com Himmel se a posição caiu em 2 ou mais dias da última semana.
• Yasmin: registrar na memória semanal o patamar atual da conta e a concentração observada hoje. Weekly e monthly estão sem conteúdo — sem esse registro, os próximos ciclos de análise partem de zero e não conseguem detectar mudança de padrão.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: MLB3288536143 (código interno do anúncio de potes redondos)
- Origem do bloqueio: Condensadora
- Motivo: identificador técnico interno sem valor operacional para Yasmin
- Agregado autorizado: sim, `anúncio principal de potes redondos` / `anúncio do grupo de potes redondos`
- Tratamento aplicado: substituído por agregado `anúncio principal de potes redondos`
- Aparece na mensagem final: sim, como agregado `anúncio principal de potes redondos`

- Item bloqueado: SKUs crus (IMB501P, IMB501C, IMB501V, SPC0111, KIT4YW1050, KIT4YW320, KIT4YW640, 914C, 914C_BAV, XCP002)
- Origem do bloqueio: Condensadora
- Motivo: SKUs crus sem valor direto para operação
- Agregado autorizado: sim, display names aprovados pelo pacote validado
- Tratamento aplicado: substituídos por display_name de cada variação
- Aparece na mensagem final: não (usados apenas os display_names)

- Item bloqueado: pico das 14h como padrão verificado
- Origem do bloqueio: Condensadora / Granular
- Motivo: não confirmado por histórico horário — dado ausente no pacote
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem
- Aparece na mensagem final: não

- Item bloqueado: cancelamento único com hipótese de produto associado
- Origem do bloqueio: Condensadora / Granular
- Motivo: produto do cancelamento não rastreável neste ciclo
- Agregado autorizado: não
- Tratamento aplicado: omitido da seção de análise; cancelamento aparece apenas como dado objetivo em VISÃO (1 cancelamento)
- Aparece na mensagem final: sim, apenas como dado numérico em VISÃO, sem hipótese de produto

- Item bloqueado: posição e ranking dos anúncios como dado verificado
- Origem do bloqueio: Condensadora
- Motivo: dado ausente no pipeline — checagem ainda não realizada
- Agregado autorizado: sim, reformulado como checagem a realizar (prioridade do dia)
- Tratamento aplicado: citado em PRIORIDADES como ação de verificação, não como dado confirmado
- Aparece na mensagem final: sim, como checagem em PRIORIDADES DO DIA

- Item bloqueado: 914C e 914C_BAV como dois produtos distintos
- Origem do bloqueio: Condensadora
- Motivo: 914C e 914C_BAV compartilham o mesmo anúncio MLB4410218897
- Agregado autorizado: sim, `Kit 6 Canequinhas 100ml` como agregado único
- Tratamento aplicado: consolidados em uma linha única em TOP PRODUTOS com o display_name do SKU de confiança alta (914C)
- Aparece na mensagem final: sim, como `Kit 6 Canequinhas 100ml — 3 pedidos` (com pedidos do SKU 914C; 914C_BAV com confiança média omitido do ranking para não duplicar o mesmo listing)

- Item bloqueado: qualquer afirmação sobre fulfillment ou dependência de Mercado Livre Full
- Origem do bloqueio: Condensadora
- Motivo: dado ausente, dimensão opaca neste ciclo
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Granular + Estratégica`, `padrão C/D/E`, `critério`) de todos os insights — motivo: são referências internas do pipeline, não visíveis para Yasmin
- KIT4YW640 incluído em TOP PRODUTOS com display_name simplificado `Kit 4 Potes de Vidro 640ml` — motivo: display_name original truncado com `...`; truncamento removido para clareza, mantendo identificação segura por MLB e SKU validados
- Suporte Gamer SPC0111 incluído com título encurtado `Suporte Gamer 2 Controles e Headset Mesa PS5/PS4` — motivo: título original muito longo; encurtamento preserva identificação sem perda de variação vendável (produto sem variação de cor/tamanho)
- 914C_BAV omitido do TOP PRODUTOS e apenas 914C listado como `Kit 6 Canequinhas 100ml — 3 pedidos` — motivo: ambos compartilham MLB4410218897; listar os dois duplicaria o mesmo listing; 914C tem confiança alta e é a linha de referência; os 3 pedidos adicionais de 914C_BAV (confiança média) não foram incluídos no total para evitar dupla contagem sem validação explícita da Condensadora para soma combinada
- KIT4YW320 e KIT4YW640 mantidos como linhas separadas (não consolidados com KIT4YW1050) — motivo: são MLBs distintos (diferentes capacidades: 320ml, 640ml, 1050ml), não variações do mesmo anúncio; consolidação seria incorreta
- Ranking mantido em ordem decrescente por pedidos: IMB501P (35) > IMB501C (16) > IMB501V (9) > SPC0111 (4) = KIT4YW1050 (4) > 914C (3) = XCP002 (3) = KIT4YW640 (3) — motivo: regra estrutural de ordenação
- KIT4YW320 (3 pedidos, confiança média) omitido do TOP PRODUTOS para não estender excessivamente a lista com produto de confiança média empatado com outros itens de confiança alta já listados — motivo: evitar lista muito longa; o produto está documentado neste log para QA
- Insights da Condensadora preservados integralmente quanto à tese e conectivos — apenas remoção de metadados e pequenos ajustes de pontuação aplicados
- Prioridades preservadas com ação + motivação + sinal de confirmação/refutação + gatilho de escalonamento, conforme Condensadora — sem criação de ação nova