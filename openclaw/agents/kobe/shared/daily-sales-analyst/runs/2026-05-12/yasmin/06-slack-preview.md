<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 12/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 4.081,49
• Pedidos: 91
• Ticket médio: R$ 44,85
• Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
• Jogo Potes de Vidro 5 Peças — tampa preta — 26 pedidos
• Jogo Potes de Vidro 5 Peças — tampa cinza — 15 pedidos
• Jogo Potes de Vidro 5 Peças — tampa vermelha — 11 pedidos
• Jogo 6 Canequinha 100ml Suporte Madeira Alumínio Amarelo — 6 pedidos
• Kit 4 Potes Vidro Tampa Hermética 1520ml Verde-escuro — 6 pedidos

🔍 ANÁLISE DA CONTA
• A leitura de "55% concentrado nos top 3 produtos" distorce o risco real: os três SKUs do topo são variantes de cor de um único anúncio — qualquer problema de ranking, preço ou operação nesse listing afeta os três simultaneamente, sem separação de risco entre eles.
• O GMV ficou dentro da banda mensal, mas o que segurou o número foi o ticket acima da média, não o volume de pedidos — a conta está saudável no número e vulnerável na estrutura: se o anúncio líder perder posição ou preço competitivo, não há cauda com capacidade para absorver o impacto.
• A comparação com outras terças mostra queda expressiva, mas o resultado de 28/04 (provável evento ou campanha pontual) puxa a média para cima; excluindo esse outlier, a conta fica a -16,7% de um benchmark limpo — fraqueza real mas moderada, não sinal de deterioração consolidada.

🎯 PRIORIDADES DO DIA
• Yasmin: checar posição de ranking e preço relativo do anúncio líder (Jogo Potes Vidro 5 Peças) em relação aos principais concorrentes. 55% dos itens vendidos dependem de um único listing sem variação real de risco entre os SKUs — qualquer degradação colapsa o GMV sem mecanismo de compensação de mix. Se posição estável e sem concorrente relevante identificado abaixo no ranking, manter observação sem ação. Escalar para Himmel se posição tiver caído ou concorrente com preço inferior aparecer no ranking.
• Yasmin: verificar se algum produto da cauda (posições 4–10) acumulou crescimento nos últimos 3–5 dias — o snapshot de ontem por si só não responde essa pergunta. Se encontrar produto com crescimento de 50%+ vs média recente, observar por mais 2–3 dias antes de qualquer decisão de exposição. Se cauda estiver flat, confirma dependência crônica — registrar como padrão observado.

Dia analisado: 12/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs individuais (IMB501P_T, IMB501C_T, IMB501V_T)
- Origem do bloqueio: Condensadora
- Motivo: IDs técnicos internos não devem aparecer no Slack
- Agregado autorizado: sim, "anúncio líder" / variantes por cor do produto
- Tratamento aplicado: substituídos por descrição de cor da tampa (preta, cinza, vermelha) para identificação do produto no Top Produtos, sem expor SKU cru
- Aparece na mensagem final: sim, como variantes de cor do produto

- Item bloqueado: platform_item_id técnico (MLB3288536143)
- Origem do bloqueio: Condensadora
- Motivo: ID técnico não deve aparecer no Slack
- Agregado autorizado: sim, "anúncio líder" / "principal listing da conta"
- Tratamento aplicado: omitido; produto referenciado pelo nome comercial
- Aparece na mensagem final: não

- Item bloqueado: afirmação sobre relevância ou distribuição dos cancelamentos
- Origem do bloqueio: Condensadora
- Motivo: breakdown por produto não disponível no pacote — não é possível afirmar que são irrelevantes ou pulverizados
- Agregado autorizado: não
- Tratamento aplicado: cancelamentos exibidos apenas como dado objetivo na VISÃO (total=4), sem qualificação analítica
- Aparece na mensagem final: sim, como dado objetivo sem interpretação

- Item bloqueado: afirmação sobre Full ML ou competitividade de exposição vs concorrentes com Full
- Origem do bloqueio: Condensadora
- Motivo: schema não captura campo ml_full; qualquer afirmação seria sem base de dado
- Agregado autorizado: não
- Tratamento aplicado: omitido integralmente da mensagem
- Aparece na mensagem final: não

- Item bloqueado: tendência de cauda por produto como fato confirmado
- Origem do bloqueio: Condensadora
- Motivo: pacote não tem histórico diário granular por produto; ausência no snapshot não confirma ausência de tendência
- Agregado autorizado: não (bloqueio de afirmação, não de menção)
- Tratamento aplicado: prioridade mantida como checagem diagnóstica, sem afirmar ausência de candidato emergente como fato
- Aparece na mensagem final: sim, como checagem aberta ("o snapshot de ontem por si só não responde essa pergunta")

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Granular`, `— base: Estratégica + Operacional`) dos insights — motivo: texto de pipeline interno, não pertence ao Slack
- Preservação de linguagem de contraste nos insights 1 e 2 (`mas`, `não há cauda com capacidade`) — motivo: conectivos analíticos essenciais; trocá-los mudaria a nuance e a tese
- Preservação da inversão no insight 2 ("saudável no número e vulnerável na estrutura") — motivo: tese central da Condensadora; suavizar ou reordenar perderia o alerta
- Preservação da ressalva do insight 3 ("fraqueza real mas moderada, não sinal de deterioração consolidada") — motivo: confiança alta, mas a qualificação é parte da tese — omiti-la transformaria hipótese em certeza
- Omissão da percentagem de comparação com mesmo dia da semana na seção ANÁLISE — motivo: o dado (-30,9%) sem o contexto do outlier seria interpretado incorretamente; a Condensadora trouxe o insight com a ressalva e o número isolado seria ruído
- Top Produtos: três variantes do anúncio líder mantidas como linhas separadas com identificação por cor de tampa — motivo: são SKUs vendáveis distintos com volumes distintos; consolidar em uma linha única ocultaria a distribuição real de demanda por variação
- Top Produtos: listados os 5 primeiros fora do critério de agrupamento (variantes de cor do mesmo listing + 2 produtos distintos) — motivo: ranking seguro disponível no pacote, sem bloqueio de identificação, risco de identificação baixo conforme Granular
- Prioridade de escalonamento para Himmel preservada como condicionada — motivo: a Condensadora trouxe condição de escalonamento explícita; transformar em ação direta seria ultrapassar o escopo
- Checagem de cauda mantida como pergunta aberta, não como diagnóstico — motivo: Condensadora bloqueou afirmação de ausência de candidato emergente como fato; formulação aberta preserva a nuance correta
- Omissão da seção de Full ML nas prioridades — motivo: bloqueio explícito da Condensadora; sem dado estrutural, qualquer ação seria sem base