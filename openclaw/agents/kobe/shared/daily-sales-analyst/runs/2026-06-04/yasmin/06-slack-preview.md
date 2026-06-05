<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 04/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 8.647,61
- Pedidos: 179
- Ticket médio: R$ 48,31
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Cinza: 41 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha: 28 pedidos
- Potes Vidro 5 Peças — Tampa Preta: 20 pedidos
- Kit 6 Canecas Tulipa 250ml: 18 pedidos
- Kit 6 Canecas Lisas 200ml: 16 pedidos

🔍 ANÁLISE DA CONTA
- A conta entrou de vez em outro patamar: R$ 8.647,61 de faturamento está 57% acima do mês e 42% acima da média de quartas-feiras — a segunda quarta seguida acima de R$ 8 mil, puxada por volume (179 pedidos) com ticket estável. Não é pico isolado, é o novo ritmo da operação.
- A virada para MercadoLíder Platinum está a R$ 3.810,00 do threshold (98,71% do caminho, prazo estimado em menos de 1 dia ao ritmo atual) — mas a janela da promoção coincide com a janela de risco dos dois Full críticos: a Tulipa fechou com cerca de 7h de cobertura e o Kit 6 Canecas Lisas 200ml com cerca de 16h. Qualquer cancelamento automático por ruptura entra no indicador de cancelamentos oficial bem no momento do threshold e pode ameaçar os critérios de qualidade da medalha.
- O Kit 6 Canecas Lisas 200ml — único anúncio em Catálogo gold_pro do topo, em Full — encadeou 3 ciclos de cobertura caindo: 35 → 28 → 11 unidades, sem nenhuma reposição no meio. Não é falta de demanda, é uma ruptura se aproximando num anúncio onde perder o Buy Box demora dias para recuperar. Esse ponto não comporta mais um ciclo de observação.

🎯 PRIORIDADES DO DIA
- Yasmin: checar estoque atual e se há reposição em trânsito ao CD do ML para o Kit 6 Canecas Lisas 200ml (único Catálogo gold_pro do topo, em Full). A cobertura caiu três ciclos seguidos sem nenhum restock — ruptura aqui derruba o Buy Box em Catálogo e a recuperação leva dias. Como saber se deu certo: reposição confirmada com prazo estimado de até 24h = risco resolvido para os próximos 2-3 dias. Sem reposição confirmada e estoque em 5 unidades ou menos = ruptura iminente, checar novamente em 4-6h. Escalar se: ruptura confirmada com perda de Buy Box e indicador de cancelamentos sair de zero antes da promoção Platinum = escalar para Kobe.
- Yasmin: checar status (ativo ou pausado), estoque atual e reposição em trânsito do Kit 6 Canecas Tulipa 250ml (Full, 7º ciclo do padrão de ruptura recorrente). A cobertura é sub-dia bem no timing do threshold Platinum (falta R$ 3.810,00); um cancelamento automático por ruptura entra no indicador de cancelamentos oficial e pode comprometer os critérios de qualidade da medalha. Como saber se deu certo: anúncio ativo com reposição confirmada = risco resolvido. Anúncio pausado = registrar data e hora como ponto que vai distorcer a leitura das próximas métricas e monitorar o indicador de cancelamentos no próximo snapshot. Escalar se: indicador de cancelamentos sair de zero no próximo snapshot antes da promoção = escalar para Kobe.
- Yasmin: registrar a qualidade do anúncio do Kit 4 Potes 640ml Tampa Azul-petróleo (Full, em nível preocupante) como 2º ponto confirmado abaixo do limite. É o menor nível de qualidade do snapshot; 4 pedidos no dia abaixo do esperado para um Full ativo é coerente com perda de posição orgânica. O 3º ciclo decide se é padrão recorrente ou pontual. Como saber se deu certo: nível de qualidade em 0,68 ou acima no próximo ciclo = manter observação sem ação. Nível em 0,65 ou abaixo, ou 3º ciclo abaixo de 0,70 = Yasmin alinha com Himmel sobre cobertura preventiva de ADS nesse anúncio.

Dia analisado: 04/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atribuição dos 4 cancelamentos do dia a anúncios específicos (Tulipa, Catálogo ou outros)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Inconclusivo por falta de breakdown order_id↔platform_item_id; afirmar origem seria hipótese sem prova
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — cancelamentos citados apenas como dado objetivo (4 cancelamentos) na seção VISÃO, sem atribuição de origem
- **Aparece na mensagem final:** sim, como dado objetivo na VISÃO ("Cancelamentos: 4") sem atribuição de causa ou produto

---

- **Item bloqueado:** Direção do nível de qualidade do anúncio MLB3288536143 (Potes 5 Peças Tampa Cinza+Vermelha) — não afirmar "estável", "caindo" nem "em recuperação"
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Snapshot pontual não permite distinguir estabilidade real de plateau pré-deterioração; ML não publica série interna nem drivers
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido da análise; o anúncio aparece apenas no Top Produtos pelo volume, sem menção ao nível de qualidade
- **Aparece na mensagem final:** não (no que diz respeito à direção do nível de qualidade)

---

- **Item bloqueado:** Hipótese de concentração de ADS sobre os anúncios em nível regular/preocupante ("ADS compensando posição orgânica")
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Inconclusivo por falta de breakdown ADS spend/revenue por platform_item_id; pendência estrutural há 14 ciclos
- **Agregado autorizado:** não
- **Tratamento aplicado:** ADS citado apenas com dados agregados confirmados (eficiência, share) sem atribuição por anúncio
- **Aparece na mensagem final:** não (hipótese omitida; ADS não foi tema de insight na Condensadora e não entrou na análise)

---

- **Item bloqueado:** Códigos MLB e SKUs crus (IMB501C/V/P etc.) na análise principal
- **Origem do bloqueio:** L05 Condensadora / convenção ML
- **Motivo:** Convenção ML — usar nome comercial
- **Agregado autorizado:** sim (nomes canônicos via slack_short_name e display_short)
- **Tratamento aplicado:** todos os produtos aparecem pelo nome curto canônico; nenhum MLB ou SKU cru visível na mensagem
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Metadados internos (`padrao`, `base`, `classificacao`) removidos de todos os insights — informação de pipeline, não vai para Slack
- Insight 1 (fato): citado como fato direto, sem linguagem de indício — classificação "fato" permite essa assertividade
- Insight 2 (risco latente): preservada nuance de risco sem transformar em certeza; uso de "pode ameaçar" e "janela coincide" para manter o tom de risco latente sem cravar desfecho
- Insight 3 (risco latente): preservada urgência sem afirmar ruptura consumada; "se aproximando" e "não comporta mais um ciclo" mantêm a tese da Condensadora
- "threshold" traduzido para linguagem natural em todas as ocorrências ("do threshold" mantido pontualmente quando ligado ao termo técnico ML "MercadoLíder Platinum threshold" sem substituto claro; "prazo estimado" no lugar de "ETA")
- "ETA" traduzido para "prazo estimado" em todas as ocorrências na mensagem
- "cancellations_rate" traduzido para "indicador de cancelamentos" em todas as ocorrências
- "runway" traduzido para "cobertura" em todas as ocorrências
- "health" não aparece em nenhum ponto da mensagem; substituído por "nível de qualidade" ou "qualidade do anúncio" conforme vocabulário obrigatório
- "fulfillment" não aparece na mensagem; modalidades descritas como "Full" e "Cross-Docking" quando necessário
- "GMV" não aparece na mensagem; substituído por "Faturamento" em todas as ocorrências
- "share" não aparece na mensagem; substituído por "fatia" ou "%" conforme contexto
- Modalidade de envio omitida da seção 📊 VISÃO MERCADO LIVRE — dado de fulfillment_mix_yesterday_top10 cobre apenas top 10 (105 de 179 pedidos = ~58,7% de cobertura), não representa dado objetivo da plataforma sem ressalva; Condensadora não autorizou explicitamente com cobertura declarada
- **Top Produtos — traduções item a item:**
  - IMB501C → usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - IMB501V → usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - IMB501P → usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - TL6250 → usado slack_short_name "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)
  - CLR002 → usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
- **Análise e Prioridades — traduções de nome de produto:**
  - "Kit 6 Canecas Tulipa 250ml" usado em todas as menções (slack_short_name canônico, mapeamento canônico para TL6250)
  - "Kit 6 Canecas Lisas 200ml" usado em todas as menções (slack_short_name canônico para CLR002)
  - "Kit 4 Potes 640ml Tampa Azul-petróleo" — slack_short_name do pacote é "Kit 4 Potes 640ml" (KIT4YW640, slack_short_name=null); usado display_short simplificado "Kit 4 Potes 640ml Tampa Azul-petróleo" mantendo o atributo de cor do título ML para distinguir do Kit 10 — divergência registrada: L05 escreveu "Kit 4 Potes 640ml Tampa Azul-petróleo" com referência a MLB5402326666; L06 manteve o mesmo nome (fallback display_short com atributo de cor do title ML, pois slack_short_name é null)
- Faturamento de R$ 8.647,61 preservado com centavos em todas as menções monetárias; R$ 3.810,00 com centavos explícitos conforme regra
- Atribuição de Yasmin como responsável fixo em todas as 3 prioridades
- Escalonamento para Kobe preservado nas prioridades 1 e 2 conforme L05; prioridade 3 com "não aplicável hoje" omitido (sem escalar_se na mensagem, pois a L05 não indicou condição)
- Frase "Como saber se deu certo:" usada no lugar de "Confirmar/refutar por:" para manter tom conversacional mantendo a função analítica — preserva o sinal de confirmação/refutação da Condensadora em linguagem mais direta
- Confiança média da Condensadora: 3 insights mantidos (2 risco latente + 1 fato), todos com base robusta declarada pela L05; nível médio não aciona corte de insights, apenas preservação de ressalvas onde aplicável