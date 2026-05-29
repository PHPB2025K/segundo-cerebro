<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **Volume e ticket cresceram juntos — expansão dupla sem substituição.** 164 pedidos representam +52,2% sobre a média dos mesmos dias da semana (`same_weekday_avg.avg_orders=107,75`) e +53,6% sobre `avg_30d.avg_orders=106,8`, enquanto o ticket R$51,61 subiu +10,3% vs 30d e +24,9% vs 60d. O GMV de R$8.463 cresce mais rápido (+69,3% vs 30d) do que os pedidos (+53,6%) precisamente porque volume e ticket subiram juntos — não há substituição de alcance por valor unitário. Isso confirma operacionalmente a leitura da L01 de rompimento multidimensional: o canal está entregando mais pedidos *e* pedidos de maior valor, ao mesmo tempo.

- **51,2% do volume veio de um único anúncio com health degradado no oitavo ciclo consecutivo.** As três variações do Conjunto 5 Potes de Vidro (Tampa Preta 42 + Tampa Cinza 22 + Tampa Vermelha 20 = 84 pedidos) são variações de MLB3288536143 — um único anúncio — e o `top3_concentration=51,2%` reflete exatamente essa concentração. MLB3288536143 opera em Full (`logistic_type=fulfillment`) com `health=0,71`, oitavo ciclo estável. Com ADS aparentemente zerado no dia, toda a performance de metade do volume veio de um único vetor orgânico funcionando com qualidade abaixo do nível regular do ML. A L01 identificou isso como risco estrutural principal; o dia não contradiz nem confirma piora — apenas reforça a dependência operacional sobre uma base de health preocupante.

- **Mix de modalidade de envio do top do dia divergiu fortemente do padrão mensal, por razão estrutural confirmada.** `fulfillment_mix_yesterday_top10.full_pct=94,8%` vs `fulfillment_mix_30d.full_pct=76,2%` — diferença de 18,6 pontos percentuais para Full. A divergência não é ruído: quase todos os anúncios no top do dia operam em Full (MLB3288536143, MLB4073003575, MLB6754669844, MLB4073064873, MLB6232315532, MLB4676726433, MLB6167272090), com apenas MLB6739252838 em Cross-Docking (4 pedidos, 5,2% do mix resolvido). A memória de 24/05 registrou como hipótese a migração do IMB501P de Cross-Docking para Full; o snapshot atual confirma `logistic_type=fulfillment` para MLB3288536143 — explicação estrutural para o shift do mix. Não é divergência sistêmica; é produto-específica e decorrente do IMB501 cluster dominando o dia inteiramente em Full.

- **ADS com `spend=R$0` e `revenue=R$0` pelo primeiro ciclo observado — maior dia da série sem atribuição de paid media.** A série histórica registrada na memória (22/05: 69,9% share; 23/05: 49,5%; 25/05: 56,7%; 26/05: 60,7%) não tem continuidade neste ciclo. O GMV de R$8.463 é o maior dia recente e ocorreu inteiramente sem ADS atribuído — confirma operacionalmente a hipótese da L01 de que a conta tem capacidade orgânica superior ao que os ciclos com ADS dominante permitiam mensurar. Como a L02 estabeleceu como pré-requisito, a origem do zero precisa ser confirmada (pausa deliberada de Himmel vs gap de API) antes de qualquer conclusão definitiva — mas a evidência operacional do dia aponta na direção da hipótese orgânica.

---

### Sinais operacionais relevantes

- **Sinal:** Kit 10 Potes 640ml (MLB6754669844, Full, `available_quantity=3` após 11 pedidos do dia) — **interpretação operacional:** cobertura prospectiva ≈ 6 horas ao ritmo do dia (3 ÷ 11); qualquer pedido a partir de agora ultrapassa o estoque disponível no CD do ML e aciona cancelamento automático. Adicionando evidência à ação 1 da L02: risco está ativo agora, não no próximo ciclo. `cancellations_rate=0` está intacto, mas é exatamente o que está em risco se este anúncio não for reabastecido.

- **Sinal:** Kit 10 Potes 320ml 6un (MLB6739252838, Cross-Docking, `available_quantity=2` após 4 pedidos do dia) — **interpretação operacional:** cobertura prospectiva ≈ 12 horas ao ritmo do dia (2 ÷ 4); Cross-Docking é controlado pela Budamix, o que dá margem operacional maior do que o Full (reposição não depende de remessa ao CD do ML) — mas janela é igualmente pequena.

- **Sinal:** Cancelamentos do dia em 4, com padrão 3 → 3 → 4 nos ciclos de 25, 26 e 28/05 — **interpretação operacional:** a escalada é gradual, mas direcional; `cancellations_rate` da reputação permanece em 0 (janela longa), o que significa que os cancelamentos do dia são sinal precoce ainda não incorporado na métrica de reputação. A ruptura iminente de MLB6754669844 e MLB6739252838 — se confirmada antes de reposição — adiciona potencialmente uma segunda fonte ativa de cancelamentos automáticos sobre um padrão que já estava crescendo.

- **Sinal:** Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo gold_pro, Full, `available_quantity=75` após 7 pedidos) — **interpretação operacional:** inversão do risco crítico registrado em 26/05 (31 unidades, cobertura ~2,1 dias). A cobertura atual é de ≈10,7 dias ao ritmo do dia — reposição aparentemente entrou. O único anúncio em Catálogo (`is_catalog=true`) entre os top performers saiu da zona crítica; Buy Box no Catálogo não sofreu ruptura no período de risco. Risco prospectivo atualizado para não urgente neste anúncio.

- **Sinal:** Kit 4 Potes 1050ml Tampa Azul-petróleo (MLB4073003575, Full, `available_quantity=57` após 15 pedidos, `health=0,75`) — **interpretação operacional:** cobertura prospectiva ≈ 3,8 dias ao ritmo do dia (57 ÷ 15). Não é ruptura iminente, mas é horizonte curto para um anúncio Full com health em zona regular há 8 ciclos e volume acima da média histórica. Se o volume do dia se mantiver no novo patamar, o anúncio entra em zona crítica antes de D+4; reposição ao CD do ML precisa estar em trânsito.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada.**

Dois vetores operacionais simultâneos sustentam a classificação: (1) MLB6754669844 com cobertura prospectiva de ~6 horas em Full — ruptura ativa ou iminente antes do próximo pacote, sem reposição confirmada; (2) escalada de cancelamentos 3→3→4 nos últimos três ciclos, convergindo com o momento em que dois anúncios estão entrando em ruptura de estoque. Cada sinal isolado seria anomalia leve; a sobreposição de ruptura iminente em Full com escalada de cancelamentos — em conta que está a 7,6 dias de Platinum com `cancellations_rate=0` como métrica ativa — eleva para moderada.

Não atinge anomalia crítica porque: `cancellations_rate=0` na janela de reputação, conta verde (`5_green`), `claims_rate=0,0019` em 38% do threshold, e os cancelamentos do dia (4 em 164 pedidos = 2,4%) ainda são operacionalmente contidos. Sobe para crítica se MLB6754669844 aparecer com `status=paused` ou `available_quantity=0` no próximo pacote e `cancellations_rate` sair de zero — especialmente dado o gap de Platinum em R$33.193 com ETA 7,6 dias.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual o estoque atual de MLB6754669844 (Kit 10 Potes 640ml, Full) no CD do ML agora — e há reposição em trânsito confirmada? — **motivada por:** sinal 1 (cobertura ~6h ao ritmo do dia); L02 identificou esta como única ação que não pode esperar mais dados; L04 precisa confirmar se a ruptura já ocorreu ou se ainda há janela.

- **Pergunta:** Os 4 cancelamentos do dia têm origem em MLB6754669844 ou MLB6739252838 — ou vêm de outra fonte? — **motivada por:** sinal 3 (escalada 3→3→4) e sinal 1+2 (ruptura iminente nestes dois anúncios); se os cancelamentos do dia já provêm desses anúncios, `cancellations_rate` começa a ser pressionado agora, não nos próximos dias.

- **Pergunta:** O `spend_yesterday_brl=R$0` com 11 campanhas ativas foi pausa deliberada de Himmel, ajuste operacional ou gap de atribuição da API do Mercado Ads? — **motivada por:** sinal central da L01 e condição imposta pela L02 para qualquer conclusão sobre orgânico vs paid; a resposta define se o dia deve ser registrado como experimento orgânico válido ou como dado contaminado.

- **Pergunta:** O health de MLB3288536143 (0,71) e de MLB4073003575 (0,75) está estável, caindo ou subindo neste ciclo vs o ciclo anterior? — **motivada por:** oitavo ciclo idêntico sem confirmação de direção; com volume máximo da série e ADS zerado, a direção do health nos campeões principais define se a hipótese de piso de nível ganha ou perde força.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o volume recorde — é a tensão entre o maior resultado recente e a fragilidade de dois anúncios em Full que podem cancelar automaticamente nas próximas horas. MLB6754669844 tem cobertura prospectiva de ~6 horas ao ritmo do dia; MLB6739252838 tem ~12 horas. Se a ruptura se concretizar antes de reposição, `cancellations_rate` — hoje zerado — começa a se mover exatamente quando a conta está a 7,6 dias de Platinum com gap de R$33.193. Cancelamentos automáticos por ruptura de estoque são diferentes de cancelamentos por insatisfação: entram direto na janela da reputação, são previsíveis, e neste caso havia sinal desde o pacote anterior. A Condensadora deve carregar esse risco prospectivo como o fato operacional central do dia, não o patamar de GMV em si — que confirma a tese da L01 mas não é acionável hoje. O que é acionável hoje é a reposição urgente dos dois anúncios antes que o pipeline de Platinum seja pressionado por cancelamentos que poderiam ter sido evitados.