<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 24/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.024,80
- Pedidos: 99 pedidos
- Ticket médio: R$ 50,76
- Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 29 pedidos
- Kit 4 Potes 1050ml — 18 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Kit 6 Canecas Lisas 200ml — 9 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 8 pedidos

🔍 ANÁLISE DA CONTA
- R$ 5.024,80 com ticket de R$ 50,76 — patamar real, acima da média dos últimos 30 e 60 dias. Mas o resultado depende de duas alavancas frágeis ao mesmo tempo: o anúncio de Potes Vidro 5 Peças (nas três variações de tampa) concentra 47,5% das vendas, com nível de qualidade do anúncio em nível regular (0,71) pelo quarto dia seguido; e o ADS responde por 71,2% do faturamento. Enquanto as duas funcionam juntas, o número parece saudável. Se qualquer uma ceder, o orgânico não está pronto para cobrir.
- O risco urgente não está no faturamento — está nas canecas. O Kit 6 Canecas 250ml (Cross-Docking) ficou com 1 unidade após as vendas de ontem: qualquer pedido novo pode virar cancelamento automático. O Kit 6 Canecas Lisas 200ml (Catálogo Full) tem cobertura para ~2,8 dias ao ritmo atual. Perder o Buy Box em anúncio de catálogo demora a reverter mesmo depois de reestocar. Os 2 cancelamentos do dia chegaram sem origem rastreada — não dá para descartar que o sinal já começou.
- O ADS voltou a 71,2% — mesmo patamar dos ciclos anteriores ao recuo de 23/05. Por ora, não é gatilho de ação: com as campanhas em ~11x de retorno e ACOS 4,22%, mexer agora seria introduzir variável sem motivo. O ponto a observar está no pacote de amanhã. Se o ADS share aparecer acima de 65% pelo segundo dia seguido e o nível de qualidade do anúncio dos dois líderes (0,71 e 0,75) seguir estagnado no quinto ciclo, é o momento de abrir o alinhamento com Himmel.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar estoque em trânsito e prazo de reposição ao CD do ML do Kit 6 Canecas Lisas 200ml (25 unidades restantes, cobertura ~2,8 dias ao ritmo atual) e acionar reposição imediata se ainda não estiver programada. Perder o Buy Box em catálogo demora a reverter mesmo depois de reestocar — a janela de ação é hoje. Confirmar por: reposição em trânsito com prazo ≤ 3 dias = risco resolvido; sem reposição confirmada ou anúncio pausado por estoque zero = registrar como ponto de distorção para GMV e MercadoLíder dos próximos 5 dias.
- Yasmin: verificar o status do Kit 6 Canecas 250ml (Cross-Docking, 1 unidade restante, 3 pedidos ontem) — se há pedido em aberto sem estoque ou cancelamento automático pendente — e confirmar o status do Kit 6 Canecas Porcelana Tulipa, ausente do top há três ciclos. Cancelamento automático nesses anúncios entra direto na janela MercadoLíder Platinum (faltam R$ 48.941,14, prazo estimado ~12 dias) — e os 2 cancelamentos do dia sem origem rastreada podem já ser o primeiro sinal. Confirmar por: ambos os anúncios ativos com reposição programada = cluster estabilizado; cancelamento registrado = marcar data e volume e revisar prazo para Platinum. Escalar se: cancelamento automático confirmado em qualquer um dos dois — comunicar a Kobe se o gap para Platinum cair abaixo de R$ 30.000,00 como consequência.
- Yasmin: no pacote de amanhã (25/05), ler o nível de qualidade do anúncio dos dois líderes em Full — Potes Vidro 5 Peças (0,71, quinto ciclo) e Kit 4 Potes 1050ml (0,75, quinto ciclo) — e o ADS share do dia. Essa leitura define o próximo movimento. Confirmar por: nível acima de 0,85 em qualquer dos dois = risco estrutural enfraquecido, manter observação; nível abaixo de 0,70 em qualquer dos dois com ADS share acima de 65% = Yasmin abre alinhamento com Himmel sobre cobertura preventiva. Escalar se: dado ausente no pacote = registrar como pendência técnica recorrente para o Trader; ADS share acima de 65% por três dias seguidos a partir de amanhã com nível estagnado = abrir discussão com Kobe sobre dependência em mídia paga.

Dia analisado: 24/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos. O campo `o_que_nao_pode_ir_para_slack` da L05 foi entregue como array vazio (`[]`). A L04 declarou `risco_identificacao.nivel: "baixo"` e `bloqueios_para_slack: []`. Todos os produtos citados na mensagem final têm identidade confirmada e não foram objeto de restrição em nenhuma camada.

---

### Decisões de formatação

- **Metadados internos removidos** (`padrao`, `base`, `classificacao`) — são campos de pipeline, não vão para Slack.
- **Insight 1 (classificação: risco latente)** — nuance preservada com "parece saudável", "se qualquer uma ceder", "não está pronto para cobrir". Sem transformação de hipótese em certeza.
- **Insight 2 (classificação: risco latente)** — nuance preservada com "pode virar cancelamento automático", "não dá para descartar que o sinal já começou". Ruptura descrita como prospectiva (pedidos novos), nunca retrospectiva — conforme regra de estoque POST-baixa.
- **Insight 3 (classificação: hipótese)** — nuance preservada com "por ora, não é gatilho de ação", "é o momento de abrir o alinhamento" (condicional). Sem afirmação conclusiva sobre ADS.
- **Top Produtos — 5 primeiros do pacote exibidos, sem faturamento por produto** — pacote não traz receita validada por produto/variação; formato aplicado: `[nome] — [pedidos] pedidos`.
- **Modalidade de envio omitida da seção VISÃO** — `fulfillment_mix_yesterday_top10` cobre apenas 47 de 99 pedidos (~47%), sem representatividade da totalidade do dia. Modalidade citada apenas na Análise e Prioridades, com origem analítica da L05.
- **Nomes dos produtos — mapeamento canônico (slack_short_name) aplicado em todas as menções:**
  - IMB501P → `Potes Vidro 5 Peças — Tampa Preta` (slack_short_name, mapeamento canônico; atributo "Tampa Preta" já incluso no nome)
  - KIT4YW1050 → `Kit 4 Potes 1050ml` (slack_short_name, mapeamento canônico; sem atributo confirmado a adicionar)
  - IMB501V → `Potes Vidro 5 Peças — Tampa Vermelha` (slack_short_name, mapeamento canônico; atributo "Tampa Vermelha" já incluso)
  - CLR002 → `Kit 6 Canecas Lisas 200ml` (slack_short_name, mapeamento canônico; sem atributo confirmado)
  - IMB501C → `Potes Vidro 5 Peças — Tampa Cinza` (slack_short_name, mapeamento canônico; atributo "Tampa Cinza" já incluso)
  - K6CAN250 → `Kit 6 Canecas 250ml` (slack_short_name, mapeamento canônico — mencionado na Análise e Prioridades, produto rank 6 do pacote com relevância analítica confirmada pela L05)
  - Kit 6 Canecas Porcelana Tulipa — produto ausente do top_products do pacote; sem slack_short_name disponível; nome usado conforme referência analítica da L05 e memória de ciclos anteriores. MLB suprimido.
- **Cluster IMB501 referenciado como bloco** — "anúncio de Potes Vidro 5 Peças (nas três variações de tampa)"; preserva que é um único anúncio com variações, conforme instrução da L04/L05. Divergência cross-layer: L05 usa "cluster IMB501" e "anúncio único"; L06 traduziu para nome comercial padronizado do Top Produtos.
- **`health` traduzido** para "nível de qualidade do anúncio em nível regular (0,71)" e "nível de qualidade do anúncio dos dois líderes (0,71 e 0,75)" — nunca "health" no Slack.
- **"runway" traduzido** para "cobertura" (~2,8 dias).
- **"ETA" traduzido** para "prazo estimado" ou "prazo".
- **"fulfillment" não aparece** no Slack; "Full" usado como nome da modalidade de envio onde necessário, "Cross-Docking" idem.
- **Buy Box mantido** — termo ML reconhecido, aplicável ao contexto de anúncio de catálogo.
- **MercadoLíder Platinum mantido** — nomenclatura oficial ML.
- **Gap MercadoLíder Platinum** — L05 menciona "R$48.941" (sem centavos); L06 aplica padrão numérico obrigatório: `R$ 48.941,14` (valor exato do pacote: 48941.14). Threshold de escalonamento: `R$ 30.000,00`.
- **Yasmin atribuída como responsável** em todas as três prioridades — responsável fixo ML conforme arquitetura.
- **Alinhamento com Himmel via Yasmin** — nunca acionamento direto do DSA.
- **Escalonamento para Kobe e Trader mantidos** conforme L05 — condições preservadas verbatim.
- **Confiança média** — L05 entregou 3 insights; nenhuma degradação de cardinalidade aplicada. Ressalvas preservadas via linguagem de indício nos insights de risco latente e hipótese.
- **Frases longas quebradas** em sentenças mais curtas sem perda de conteúdo analítico — diretriz Pedro 2026-05-17 e 2026-05-25 aplicada.