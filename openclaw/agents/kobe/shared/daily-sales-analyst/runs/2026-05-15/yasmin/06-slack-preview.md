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
- Kit 2 Potes de Vidro 1520ml Retangular — 32 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 20 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 12 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 9 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 9 pedidos
- Kit 6 Canequinhas 100ml — 7 pedidos
- Kit 4 Potes de Vidro 640ml — 3 pedidos
- Kit 4 Potes de Vidro 320ml — 3 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 3 pedidos
- Kit 4 Potes de Vidro 1520ml Retangular — 2 pedidos

🔍 ANÁLISE DA CONTA
- O ticket elevado de R$47,78 tem base real no mix — os kits de maior volume (1520ml e conjuntos de 5 peças) responderam por 65% dos pedidos do dia, o que explica o ticket sem precisar de cuponagem ou evento de preço. A confirmação exige mais 2-3 dias com ticket na mesma faixa.
- A dependência estrutural nas duas famílias líderes não está colapsada em um único anúncio: dois anúncios operam em patamar equivalente, cada um com aproximadamente 28% do volume. Perda de posição em qualquer um impacta cerca de 28% da conta — mas a checagem precisa cobrir os dois, não só um.
- O dia converge com todas as janelas históricas acima dos benchmarks, o que sugere hipótese de patamar em formação, não pico isolado. A ressalva é real: a memória da conta ainda é rasa e os próximos dois mesmos dias da semana (22 e 29/05) são o teste decisivo.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar posição dos dois anúncios líderes no ML — potes retangulares (Kit 2 Potes 1520ml) e potes redondos com tampas preta e vermelha — e comparar com 7 dias atrás. Posição estável ou em melhora nos dois confirma suporte operacional para a tese de patamar; queda em qualquer um, registrar e monitorar por mais 2 dias. Escalar se: queda simultânea nos dois por 2 dias seguidos → alinhar com Himmel sobre exposição.
- Yasmin: observar ticket médio amanhã e depois. Ticket ≥ R$45 por dois dias seguidos confirma deslocamento de mix como padrão; queda abaixo de R$42 por dois dias indica que o ticket de ontem foi evento pontual.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios recebidos. A Granular definiu risco de identificação como baixo e não emitiu BLOQUEIO PARA SLACK para nenhum item. Todos os produtos do ranking foram tratados conforme as restrições de confiança descritas nas Decisões de formatação.

---

### Decisões de formatação

- `KIT4YW640 referenciado como "Kit 4 Potes de Vidro 640ml"` — motivo: confiança média, mapeamento genérico e título truncado no pacote; Condensadora explicitou não afirmar cor ou especificação exata para esse item
- `KIT4YW320 referenciado como "Kit 4 Potes de Vidro 320ml"` — motivo: mesma condição do KIT4YW640; nome sem cor ou detalhe adicional
- `IMB501P e IMB501V mantidos como linhas separadas no ranking` — motivo: são variações vendáveis distintas (tampa preta vs. tampa vermelha); consolidar como família única seria inválido conforme regra de variação vendável; compartilhamento de platform_item_id (MLB3288536143) é comportamento padrão de variação ML, não justifica colapso de linha
- `Compartilhamento de platform_item_id entre IMB501P e IMB501V não citado no Slack` — motivo: Condensadora classificou como risco latente e comportamento padrão ML, não anomalia ativa; risco monitorável internamente, sem evidência de erro no pacote atual
- `"Produto líder" não usado no singular` — motivo: Granular confirmou dois anúncios em patamar equivalente (~28% cada); uso do singular seria impreciso e contradiria alerta explícito da Condensadora
- `Ticket elevado tratado como confirmado com ressalva, não como incerteza total nem certeza plena` — motivo: Condensadora classificou confiança média para o dado de mix da Granular (87% do volume coberto, 13% inconclusivo); preservada ressalva de confirmação por 2-3 dias
- `Hipótese de patamar preservada como hipótese, não fato` — motivo: Condensadora explicitou que confirmação exige os próximos dois mesmos dias da semana; proibido transformar hipótese em fato
- `Fulfillment não citado` — motivo: Condensadora bloqueou; pacote registra inconsistência (subcampos zerados com total=115); ML Full não pode ser confirmado ou descartado
- `Cancelamentos citados apenas como dado agregado na seção VISÃO` — motivo: Condensadora bloqueou distribuição por produto; dado sem rastreabilidade por SKU no pacote; qualquer afirmação de concentração por variação seria invenção
- `Kit de Canequinhas não caracterizado como segundo vetor` — motivo: Condensadora bloqueou; 7 pedidos (6,1%) representam presença real mas insuficiente para vetor funcional; diagnóstico sustentado pela Granular
- `Metadados internos removidos (base: Estratégica/Tática/Granular etc.)` — motivo: padrão de formatação Slack; teses e nuances mantidas intactas, apenas referências ao pipeline removidas
- `Escalonamento para Himmel condicionado a critério explícito` — motivo: Condensadora estabeleceu gatilho claro (queda simultânea nos dois anúncios por 2 dias); não antecipar alinhamento sem esse critério atingido