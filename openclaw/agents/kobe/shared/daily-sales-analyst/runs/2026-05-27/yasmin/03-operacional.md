<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- O dia operacionalizou o ganho de patamar identificado pela L01 com volume **e** ticket em alta simultânea: 133 pedidos (+27,2% vs avg_30d=104,6; +41,1% vs same_weekday_avg=94,25) com ticket R$53,76 (+16,0% vs avg_30d=R$46,34; +24,6% vs avg_60d=R$43,16). Diferente dos ciclos anteriores onde o ticket era o único vetor do crescimento de GMV enquanto o volume oscilava perto da banda, hoje o volume também rompeu claramente — 133 pedidos é praticamente idêntico ao único dia de quarta recente que superou esse nível (134 em 29/04). Reforço operacional direto à tese de patamar da L01: não é pico de ticket sobre volume estagnado.

- Os cancelamentos dobraram de 3 para 6: a série diária acumulada é 3 (25/05) → 3 (26/05) → 6 (hoje), trajetória crescente documentada em três ciclos consecutivos. O candidato operacional mais direto é MLB4676726433 (Kit 10 Potes 1050ml, Full, Frete Grátis), que apresenta `available_quantity=4` POST-baixa de 5 pedidos e padrão idêntico ao de 25/05, quando ruptura no mesmo anúncio gerou os primeiros 3 cancelamentos confirmados da série. `cancellations_rate` da reputação permanece em 0 (janela longa do ML), mas a série diária crescente é o sinal precoce que a L02 identificou como ação imediata de Yasmin — e o ciclo de hoje o intensifica.

- A hipótese de migração do MLB3288536143 (cluster IMB501) de Cross-Docking para Full, registrada como "possível" em 24/05 e sustentada em 26/05, está operacionalmente confirmada neste ciclo: `logistic_type=fulfillment` no snapshot e `fulfillment_mix_yesterday_top10.full_pct=100%` (54 ordens resolvidas) vs avg_30d de 76,0% Full. O cluster IMB501 respondeu por 48,1% do dia (Tampa Preta 39 + Tampa Cinza 14 + Tampa Vermelha 11 = 64/133), dentro da banda histórica de 44%–56,5%. A consequência operacional da migração é estrutural: o principal volume do canal agora opera inteiramente via CD do ML, sem a alternativa de coleta em expedição que existia em 22/05. A assimetria se aprofunda — campeões 100% Full, base ativa 40,7% Full.

- ADS sustentou 67,3% do GMV (R$4.811,50/R$7.150,57), ROAS calculado 10,38x, ACOS calculado 9,63% — eficiência operacionalmente saudável, mas é o segundo ciclo consecutivo acima de 65% (22/05: 69,9%). Adiciona evidência direta à hipótese da L01 de que o ganho de patamar é carregado por Mercado Ads, não por expansão orgânica dos campeões: MLB3288536143 (`health=0,71`) e MLB4073003575 (`health=0,75`) estão no 8º ciclo idêntico sem reversão — o ML comprime progressivamente o ranking desses anúncios enquanto a campanha cobre o resultado.

---

### Sinais operacionais relevantes

- **Sinal:** MLB4676726433 (Kit 10 Potes 1050ml, Full, Frete Grátis) com `available_quantity=4` POST-baixa de 5 pedidos — exato padrão de 25/05, quando ruptura gerou 3 cancelamentos automáticos confirmados — **interpretação operacional:** cobertura prospectiva inferior a 1 dia ao ritmo atual; ruptura em Full ocorre sem controle da Budamix (ML retira o anúncio automaticamente); é o mecanismo operacional mais plausível para explicar a escalada de cancelamentos hoje e o candidato mais direto para comprometer `cancellations_rate` na janela Platinum (threshold 0,5%, atual 0%, ETA 9 dias).

- **Sinal:** Série de cancelamentos diários (3→3→6) em três ciclos consecutivos, sem breakdown de origem disponível — **interpretação operacional:** a duplicação em relação ao padrão dos dois ciclos anteriores sugere fonte em intensificação, não fonte estável. Sem atribuição por order_id↔platform_item_id, a causa não é confirmável, mas a trajetória já não é "ruído" — é sinal precoce que deve ser monitorado antes que `cancellations_rate` oficial (hoje zerado) absorva o impacto da janela longa do ML.

- **Sinal:** `fulfillment_mix_yesterday_top10.full_pct=100%` — desvio de +24pp vs avg_30d=76% e +21,1pp vs avg_7d=78,9% — **interpretação operacional:** desvio produto-específico, não sistêmico: reflete migração confirmada do MLB3288536143 para Full. Não é problema per se — é mudança estrutural que concentra os campeões integralmente na modalidade que exige reposição gerenciada pelo CD do ML, aprofundando a assimetria com a base ativa (59,3% Cross-Docking). Qualquer ruptura nos campeões agora tem impacto direto e sem amortecimento.

- **Sinal:** MLB6167272090 (Kit 6 Canecas Tulipa 250ml, Full, `health=null`) com `available_quantity=16` POST-baixa de 6 pedidos — aparente reposição vs 2 unidades em 26/05 — **interpretação operacional:** saiu da zona crítica imediata, mas cobertura prospectiva é ~2,7 dias ao ritmo de 6 pedidos/dia. Sem informação sobre volume da reposição ou se há mais em trânsito, o anúncio pode reentrar na zona ≤5 unidades em 2 ciclos. Padrão de reposição parcial recorrente neste anúncio.

- **Sinal:** MLB3288536143 (`health=0,71`) e MLB4073003575 (`health=0,75`) — 8º ciclo idêntico sem variação — **interpretação operacional:** mais um ponto na série plana sem recuperação. Não é worsening neste ciclo, mas a migração do IMB501 para Full acrescenta uma camada operacional nova: a degradação orgânica progressiva nesses anúncios agora ocorre exclusivamente na modalidade em que o time não controla o estoque disponível no ponto de distribuição. Confirma risco estrutural da L01 sem sinal de inversão.

---

### Anomalias ou ausência de anomalia

**Anomalia moderada.**

Dois desvios operacionais convergem no mesmo ciclo: (1) série crescente de cancelamentos (3→3→6) com candidato operacional recorrente (MLB4676726433) em perfil de ruptura iminente pelo segundo episódio em três dias; (2) migração confirmada do IMB501 para Full, concentrando 100% dos campeões na modalidade que amplifica o impacto de qualquer falha de reposição no CD do ML. Os números do dia são fortes — volume acima de todas as bandas, reputação estável, todos os anúncios ativos — mas os dois desvios têm causa comum latente (dependência estrutural de Full nos campeões) e se reforçam mutuamente. Desceria para "anomalia leve" se os cancelamentos estivessem estáveis em 3 e a migração estivesse documentada como fato consolidado em ciclos anteriores. Subiria para "anomalia crítica" se o próximo ciclo confirmar ruptura de MLB4676726433 com `cancellations_rate > 0` na reputação oficial — o limiar Platinum está a 0,5pp de distância, janela de 9 dias.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** MLB4676726433 (Kit 10 Potes 1050ml, Full, Frete Grátis) está ativo, pausado ou com estoque esgotado no CD do ML agora, e há reposição confirmada em trânsito? — **motivada por:** `available_quantity=4` POST-baixa de 5 pedidos hoje, cobertura prospectiva < 1 dia, e episódio idêntico de ruptura em 25/05 que abriu a série de cancelamentos que hoje chegou a 6.

- **Pergunta:** Dos 6 cancelamentos de hoje, quantos são atribuíveis a qual platform_item_id, e o mecanismo é ruptura automática de estoque Full ou outro? — **motivada por:** série crescente (3→3→6) sem breakdown de origem disponível em nenhum dos três ciclos; sem atribuição, não é possível avaliar probabilidade de movimento do `cancellations_rate` oficial nos próximos ciclos.

- **Pergunta:** A migração do MLB3288536143 para Full cobre todas as variações (Tampa Preta, Cinza, Vermelha) ou o snapshot reflete apenas o listing-pai? Alguma variação ainda opera em Cross-Docking? — **motivada por:** `fulfillment_mix_yesterday_top10.full_pct=100%` é divergência de +24pp vs 30d; confirmar se é cobertura completa ou parcial muda a leitura do mix de modalidade de envio para todos os ciclos futuros.

- **Pergunta:** MLB6167272090 (Kit 6 Canecas Tulipa 250ml, Full) — a reposição que subiu `available_quantity` de 2 para 16 entre 26/05 e 27/05: qual o volume total em trânsito ao CD do ML e qual a data de entrada? — **motivada por:** cobertura de ~2,7 dias ao ritmo de 6 pedidos/dia; saber se é reposição única de ~14 unidades ou se há lote adicional em trânsito define se o anúncio volta à zona crítica em 2 ciclos ou está coberto por mais tempo.

- **Pergunta:** Qual o breakdown de gasto e receita ADS por platform_item_id nos campeões de hoje (especialmente MLB3288536143, MLB4073003575, MLB6232315532)? — **motivada por:** segundo ciclo consecutivo de ADS share acima de 65% com avg_acos_pct=44,85% (média simples de 11 campanhas com mix heterogêneo confirmado pela divergência vs ACOS calculado de 9,63%); sem breakdown por anúncio, não é possível confirmar se a campanha concentra investimento nos campeões Full com health degradado — pendência documentada desde 22/05 que se torna mais urgente a cada ciclo.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não está no GMV recorde de quarta (R$7.150,57) — está na **série crescente de cancelamentos (3→3→6) combinada com MLB4676726433 em ruptura iminente pelo segundo episódio em três dias**, em Full com Frete Grátis ativo, `available_quantity=4` POST-baixa de 5 pedidos. O mecanismo já funcionou em 25/05 e o perfil é idêntico. O que a Condensadora precisa saber é que esse risco opera na janela mais sensível possível: `cancellations_rate` hoje em 0% com threshold Platinum de 0,5% e ETA de 9 dias — qualquer movimento no rate oficial por ruptura recorrente em Full não é apenas operacional, é risco direto de elegibilidade ao próximo nível. Além disso, a confirmação da migração do IMB501 para Full torna esse risco estruturalmente mais amplo do que parecia nos ciclos anteriores: os campeões do canal agora vivem 100% em modalidade sem controle de expedição pela Budamix, e a série de cancelamentos crescente sugere que o mecanismo de ruptura automática pode estar se tornando padrão, não evento pontual.