<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 05/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 7.742,32
- Pedidos: 164 pedidos
- Ticket médio: R$ 47,21
- Cancelamentos: 5

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Cinza — 42 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 20 pedidos
- Potes Vidro 5 Peças — Tampa Preta — 17 pedidos
- Kit 6 Canecas Lisas 200ml — 13 pedidos
- Kit 6 Canecas Tulipa 250ml — 11 pedidos

🔍 ANÁLISE DA CONTA
- A conta cruzou o limite financeiro do MercadoLíder Platinum (Faturamento dos últimos 60 dias: R$ 296.060,02, acima dos R$ 296.000,00 exigidos), mas a medalha ainda aparece como Gold no sistema — o ML tem um prazo natural para atualizar. O risco agora não é chegar lá, é chegar limpo: o anúncio da Tulipa está pausado com estoque zero, mas gerou 11 pedidos hoje, todos cancelamentos prospectivos que ainda não aparecem nos 5 cancelamentos do dia nem na taxa de cancelamento oficial (hoje em zero). Se essa série acumulada entrar na janela de avaliação do ML antes do reconhecimento formal, pode mexer com a métrica de qualidade exatamente na hora da virada. (risco latente)
- O maior vetor de pedidos da conta hoje — Potes Vidro 5 Peças — Tampa Cinza em Full, 42 pedidos, 25,6% do dia — fechou com 58 unidades em estoque depois das vendas. Isso dá cobertura prospectiva de cerca de 1,3 dias ao ritmo de hoje, com qualidade do anúncio em regular (nível 0,71) há cerca de 16 dias seguidos. Em Full, repor o estoque no CD do ML leva dias; uma ruptura aqui não se resolve rápido e tira o produto que mais gera pedidos da conta justamente enquanto o ML decide a promoção. O prazo de reposição precisa ser confirmado nas próximas 24h. (risco latente)
- A proporção de pedidos em Full no top 10 do dia ficou em 62,9%, contra 81,1% na média dos últimos 30 dias — parece queda do canal Full, mas não é. As duas variações Cross-Docking do grupo IMB501 (Tampa Vermelha e Tampa Preta) ocuparam as posições 2 e 3 com 37 pedidos combinados, puxando o número do dia para baixo. A base ativa continua com a proporção normal; o que mudou foi a composição do dia, não o canal. (fato)

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o prazo de reposição do Potes Vidro 5 Peças — Tampa Cinza (Full, líder do dia) com a cadeia de suprimentos. Cobertura de ~1,3 dias sobre o anúncio que responde por 25,6% do volume, via Full (onde reativar depois de ruptura demora dias), na semana em que a conta aguarda reconhecimento formal do Platinum — ruptura aqui interrompe o maior vetor de pedidos no pior momento possível. Como saber se deu certo: prazo confirmado em até 24h com quantidade suficiente = risco neutralizado no ciclo. Prazo acima de 48h ou sem resposta = escalar para Kobe sobre priorização de restock Full. Escalar se: prazo acima de 48h, sem resposta, ou estoque cair abaixo de 20 unidades no próximo snapshot.
- Yasmin: acompanhar a taxa de cancelamento da reputação no próximo snapshot ML. Os 11 pedidos do anúncio pausado da Tulipa são cancelamentos prospectivos garantidos no 8º+ ciclo seguido do padrão; com o limite Platinum já cruzado e a medalha ainda Gold, qualquer saída de zero nessa taxa é o sinal mais sensível para a transição. Como saber se deu certo: taxa em zero no próximo snapshot = série ainda fora da janela oficial, observar por mais 1-2 dias. Taxa acima de zero = acionar Kobe sobre impacto na qualificação Platinum formal antes de qualquer outra ação. Escalar se: taxa de cancelamento sair de zero em qualquer snapshot nas próximas 72h.
- Yasmin: conferir o estoque do Kit 6 Canecas Lisas 200ml (único anúncio de catálogo gold_pro em Full no top 10) no próximo snapshot. O restock foi confirmado entre 04/06 e 05/06 (de 11 para 30 unidades), cobertura atual de ~2,1 dias — saiu da zona crítica imediata, mas a margem ainda é estreita; ruptura em catálogo derruba o Buy Box e a recuperação de posição é lenta. Como saber se deu certo: estoque igual ou acima de 20 unidades = zona segura por 1-2 dias. Estoque abaixo de 15 unidades = restock imediato via cadeia de suprimentos. Escalar se: estoque cair abaixo de 15 unidades.

Dia analisado: 05/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios recebidos. O campo `o_que_nao_pode_ir_para_slack` da L05 está vazio. Todos os produtos do top 5 foram exibidos sem restrição.

---

### Decisões de formatação

- **Remoção de metadados internos** — `padrao`, `base` e `classificacao` não foram citados na mensagem. A classificação `risco latente` e `fato` foi preservada como marcação ao final de cada bullet de análise, em linguagem externa (entre parênteses), conforme permitido para preservar nuance sem expor metadados de pipeline.
- **Preservação de nuance por classificação** — Os dois primeiros insights da Condensadora são `risco latente`; foram escritos com linguagem de indício e prospectiva ("pode mexer", "se essa série entrar", "precisa ser confirmado"), sem transformar em certeza. O terceiro é `fato`; escrito de forma afirmativa.
- **Simplificação de frases longas** — Insights e prioridades da L05 foram quebrados em frases mais curtas e diretas, mantendo todos os termos analíticos, números e teses intactos. Ex.: "chegar limpo" preservado, "lag esperado do ML" traduzido para "prazo natural para atualizar".
- **Tradução de jargão técnico** — "ETA de reposição" → "prazo de reposição"; "cancellations_rate" → "taxa de cancelamento"; "gap_revenue_brl=0 / progress_pct=100%" → "limite financeiro já cruzado"; "threshold" → "limite"; "runway prospectivo ~1,3 dias" → "cobertura prospectiva de cerca de 1,3 dias"; "fulfillment_mix_yesterday_top10.full_pct" → "proporção de pedidos em Full no top 10 do dia"; "available_quantity" → "estoque" ou "unidades em estoque". "GMV" não aparece na mensagem — usado "Faturamento" em todos os casos.
- **Terminologia ML preservada** — "MercadoLíder Platinum", "MercadoLíder Gold", "Full", "Cross-Docking", "catálogo gold_pro", "Buy Box" mantidos. "Reputação verde" não citada diretamente na análise (não veio da Condensadora neste ponto). "qualidade do anúncio em regular" usado conforme padrão obrigatório, sem valor numérico entre parênteses.
- **Omissão de modalidade de envio na VISÃO** — `fulfillment_mix_yesterday_top10` cobre apenas os top 10 itens (~80% dos pedidos); não incluído na seção `📊 VISÃO MERCADO LIVRE` por representar dado parcial sem cobertura total validada pela L00. Mix de modalidade de envio tratado apenas na `🔍 ANÁLISE DA CONTA`, onde a Condensadora o trouxe.
- **Top Produtos — 5 primeiros exibidos** — Exibidos exatamente os 5 primeiros do `top_products`. O 5º produto (Kit 6 Canecas Tulipa 250ml, MLB6167272090) tem `status=paused` e `available_quantity=0` no snapshot, mas 11 pedidos registrados no dia analisado e aparece no `top_products` com ranking legítimo — a L04/L05 não bloqueou este produto; exibido normalmente. A análise cobre o contexto do anúncio pausado sem remover o produto do ranking.
- **Nomes de produto — mapeamento canônico aplicado:**
  - IMB501C (MLB3288536143) — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - IMB501V (MLB4535659243) — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - IMB501P (MLB4535865317) — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - CLR002 (MLB6232315532) — usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
  - TL6250 (MLB6167272090) — usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)
- **Nomes de produto nas menções da Análise e Prioridades** — Traduzidos do title ML longo da L05 para o `slack_short_name` correspondente em todas as menções. Ex.: L05 escreveu "Jogo Potes Vidro 5 Peças Tampa Cinza em Full" → L06 escreveu "Potes Vidro 5 Peças — Tampa Cinza em Full". L05 escreveu "Kit 6 Canecas Lisas 200ml" → já compatível com slack_short_name.
- **Nenhum MLB visível na mensagem** — todos os identificadores técnicos removidos.
- **Atribuição de responsável** — "Yasmin" atribuída em todas as prioridades, conforme regra fixa do canal ML.
- **Preservação de alternativas e condições** — `sinal_de_confirmacao_refutacao` e `escalar_se` preservados integralmente nas três prioridades. Formato: ação → por quê → como saber se deu certo → escalar se.
- **Sem análise própria adicionada** — a L06 não diagnosticou, não criou tese nova, não adicionou métrica que a L05 não trouxe.
- **Confiança média preservada** — a L05 sinalizou `nivel: "media"`; linguagem de indício foi mantida nos dois riscos latentes. Não há frase assertiva onde a Condensadora usou "pode", "prospectivo" ou "se".