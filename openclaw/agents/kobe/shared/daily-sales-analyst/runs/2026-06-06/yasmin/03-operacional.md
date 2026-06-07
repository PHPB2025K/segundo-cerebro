<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **Volume nominal mascara ruptura em escala:** 162 pedidos nominais (40,3% acima do mesmo dia da semana, `orders_vs_same_weekday_pct=+40,3%`) escondem que 79 desses pedidos (48,8%) vieram de três anúncios em `status=paused` com `available_quantity=0` — MLB3288536143 (67 pedidos, Conjunto 5 Potes Vidro Tampa Vermelha, Full), MLB6582682928 (6, Kit 6 Canecas Canelada, Cross-Docking) e MLB5322494954 (6, Kit 2 Potes 1520ml, Cross-Docking). O volume operacionalmente válido estimado é ~83 pedidos e GMV ~R$3.387 — abaixo do avg_30d (R$5.810, 120,6 pedidos). Confirma operacionalmente a tese da L01: o patamar declarado é artefato de ruptura, não ganho de tração.

- **A concentração do dia é concentração de família sob ruptura:** MLB3288536143 gerou 67/162 pedidos (41,4%) sozinho. Somando IMB501P (Tampa Preta, Cross-Docking ativo, 12 pedidos) e IMB501C (Tampa Cinza, Cross-Docking ativo, 10 pedidos), a família IMB501 respondeu por 89/162 = 54,9% do volume — idêntico ao `top3_concentration=54,9%`, confirmando que a concentração é inteiramente intrafamiliar. O que o dia acrescenta operacionalmente: as variações ativas em Cross-Docking (estoque >8.000 unidades cada) sustentaram fluxo, mas com 22 pedidos combinados contra os 67 do Full pausado — os substitutos activos entregaram menos de um terço do volume que o líder captou mesmo estando fora.

- **O mix de modalidade de envio visível é ilusão contábil dos pedidos prospectivos:** `fulfillment_mix_yesterday_top10.full_pct=72,8%` vs `fulfillment_mix_30d.full_pct=80,8%` — divergência de -8pp. Mas esse cálculo ponderado ainda conta os 67 pedidos do Full pausado no numerador. Dos 125 pedidos resolvidos do top10, 91 são Full — mas 67 deles são prospectivamente canceláveis. Se os pedidos de MLB3288536143 cancelarem, o Full válido do top10 cai para 24/58 = ~41%, colapsando ao perfil de base ativa da conta (`account_overview.active_analysis.fulfillment_mix.full_pct=41,3%`). A divergência de -8pp já sinaliza a ruptura; o número real pós-cancelamento é -32pp. Confirma e amplifica operacionalmente a leitura estratégica da L01 sobre o mix.

- **A fila de Full ativos chega degradada ao momento em que mais precisaria performar:** MLB5402326666 (Kit 4 Potes 640ml, `health=0,66`, `logistic_type=fulfillment`, `status=active`) está no 3º ciclo consecutivo abaixo de 0,85 — confirmado como recorrente conforme antecipado em memória 04–05/06, adicionando evidência operacional à hipótese L01/L02 de erosão orgânica. MLB4931700052 (Kit 4 Potes 800ml, `health=0,75`) e MLB5322494954 (paused, `health=0,75`) igualmente degradados. Os únicos Full com `health=0,85` no top10 são MLB4076957145 e MLB4073064873 — no limite inferior do threshold —, gerando 4 pedidos cada. A cauda ativa Full não tem condição de substituir o líder em volume nem em exposição orgânica enquanto o health permanecer nesse patamar.

---

### Sinais operacionais relevantes

- **Sinal:** MLB3288536143 (Conjunto 5 Potes Vidro Tampa Vermelha, Full, `status=paused`, `available_quantity=0`) gerou 67 pedidos — o maior gerador de volume do dia, mesmo operando em pausa com ruptura de estoque. — **Interpretação operacional:** Anúncio pausado captou pedidos pelo mecanismo ML que os mantém como ordens pendentes/canceláveis. Se classificados como "cancelamentos pelo vendedor", os 67 pedidos elevam `cancellations_rate` de 0 para ~1% dos `transactions_completed=6.622` — acima do threshold de 0,5% que ameaça elegibilidade Platinum. Este é o sinal mais grave do dia.

- **Sinal:** Mix de modalidade de envio do top10 aparentemente estável (full=72,8%, -8pp vs 30d) é sustentado pelos próprios pedidos prospectivos do anúncio pausado. — **Interpretação operacional:** O número 72,8% Full hoje é uma ilusão contábil: sem os 67 pedidos do Full pausado, o Full válido do top10 cai para ~41%. A conta não está operando com 73% Full — está operando com ~41% Full válido, com 32pp ilusórios carregados por pedidos que reverterão. Risco operacional de que a leitura de mix apareça "estável" e passe despercebida.

- **Sinal:** MLB5402326666 (Kit 4 Potes 640ml Azul-petróleo, Full, `health=0,66`) no 3º ciclo consecutivo abaixo de threshold 0,85 — recorrência confirmada. — **Interpretação operacional:** Este anúncio Full é um dos únicos vetores ativos disponíveis para compensar o líder pausado. Saúde degradada em 3 ciclos consecutivos num momento de maior necessidade é operacionalmente relevante: menor exposição orgânica exatamente quando o anúncio deveria estar absorvendo volume migrado. Adiciona evidência à ação 3 da L02 (checar direção do health).

- **Sinal:** Três anúncios paused+zero simultâneos no top10 totalizando 79 pedidos — maior evento de ruptura simultânea da série histórica registrada desde 22/05. — **Interpretação operacional:** Ciclos anteriores registravam no máximo 1–2 anúncios pausados com volumes de 4–18 pedidos prospectivos. O evento de hoje é 4–17× maior em volume de ordens prospectivas e concentrado num único dia, coincidindo com a janela de reconhecimento Platinum. Não há precedente na série disponível para calibrar o comportamento do `cancellations_rate` nessa escala.

- **Sinal:** `metrics.cancelamentos=5` do dia com `reputation.cancellations_rate=0` — janelas sem cruzamento ainda. — **Interpretação operacional:** Os 5 cancelamentos registrados no dia são sinal precoce; o campo oficial ainda não se moveu. A divergência semântica é esperada (janelas diferentes). O que é operacionalmente relevante agora: os 5 do dia podem já ser precursores das 79 ordens prospectivas sendo processadas pelo ML — ou podem ser de anúncios ativos, o que indicaria problema adicional. Sem atribuição por platform_item_id, a origem não é identificável.

---

### Anomalias ou ausência de anomalia

**Anomalia crítica.**

79/162 pedidos (48,8%) vieram de anúncios em `status=paused` com `available_quantity=0` — o maior evento isolado de ruptura multi-anúncio da série registrada. O vetor Full principal (MLB3288536143, líder em 15+ ciclos, 40–56% do volume histórico diário) opera em pausa com estoque zero, gerando pedidos prospectivamente canceláveis que, se classificados pelo ML como "cancelamentos pelo vendedor", elevam `cancellations_rate` de 0 para ~1,19% da base — acima do threshold de 0,5% para manutenção de elegibilidade MercadoLíder. Isso ocorre no segundo ciclo consecutivo com `progress_pct=100%` e `gap_revenue_brl=0` sem conversão formal de `power_seller_status` para `platinum`. A distribuição horária do dia foi normal (sem colapso de tração em horários fortes), o que descarta anomalia de demanda — a anomalia é inteiramente de execução operacional. O que rebaixaria para anomalia moderada: confirmação de ETA de reposição ≤ 2 dias + `cancellations_rate` permanecendo em zero no próximo snapshot. O que manteria ou agravaria: qualquer valor > 0 em `cancellations_rate` no próximo ciclo.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Os 67 pedidos do MLB3288536143 (Conjunto 5 Potes Vidro Tampa Vermelha, Full paused) já foram processados pelo ML como cancelamentos automáticos, e qual é o mecanismo registrado — cancelamento pelo vendedor ou pelo comprador? — **Motivada por:** A classificação do mecanismo determina se `cancellations_rate` da reputação é impactado (sinal 1 e sinal 5 — os dois vetores de maior risco do dia).

- **Pergunta:** Qual o `available_quantity` atual e o status de reposição em trânsito ao CD do ML para MLB3288536143, e se possível discriminado por variação (Tampa Vermelha / Cinza / Preta)? — **Motivada por:** ETA de reposição é a variável que define se a crise dura 2–3 dias (risco pontual) ou >7 dias (impacto estrutural no patamar) — leitura operacional bullet 2, confirmando hipótese madura de memória 05/06.

- **Pergunta:** Os 5 cancelamentos do dia (`metrics.cancelamentos=5`) são atribuídos a quais platform_item_ids — concentrados nos anúncios pausados ou distribuídos por anúncios ativos? — **Motivada por:** Atribuição de origem é o que diferencia precursores dos 79 prospectivos já em curso de problema adicional em anúncios ativos (sinal 5).

- **Pergunta:** Qual a direção do `health` do MLB5402326666 (Kit 4 Potes 640ml, `health=0,66`) nos dois ciclos anteriores — estabilizando ou caindo? E qual driver dominante aparece na tela de qualidade do anúncio (claims, atraso de envio, listing)? — **Motivada por:** 3º ciclo consecutivo abaixo de 0,85 em Full ativo que precisa compensar o líder ausente — sinal 3 e leitura operacional bullet 4.

---

### Destaque para a Condensadora

O fato operacional central do dia é a coincidência de escala: a conta gerou seu maior evento de ruptura simultânea da série histórica (79 pedidos prospectivos em três anúncios paused+zero, liderados pelo vetor Full principal que carregava 40–56% do volume em 15+ ciclos) no exato momento em que aguarda reconhecimento formal de MercadoLíder Platinum pelo segundo ciclo com critérios financeiros e de qualidade cruzados. A L01 e a L02 já nomearam esse risco — o que a camada operacional confirma é que o dia não deixou nenhuma saída alternativa: os Cross-Docking ativos da família IMB501 entregaram menos de um terço do volume do Full pausado, os Full ativos na cauda chegam com health de 0,66 a 0,75, e o mix de modalidade de envio aparentemente estável (72,8% Full) é uma ilusão contábil que colapsa para ~41% se os pedidos prospectivos cancelarem. O risco operacional silencioso que pode passar despercebido: o número de Full em destaque no top10 vai fazer o mix parecer estável no relatório — só o cruzamento com os pedidos dos anúncios pausados revela que o Full válido do dia é menos da metade do que os números nominais sugerem.