<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Leitura operacional do dia

- **Volume comprimido, ticket segurou o resultado:** 84 pedidos estão -15,4% vs avg_30d (99,3) e -17,6% vs média dos pares do mesmo dia da semana (102,0). O GMV de R$4.622,03 ficou apenas -2,1% da média dos pares (R$4.718,81) e +3,4% vs avg_30d — sustentado exclusivamente pelo ticket de R$55,02 (+22,3% vs avg_30d, +29,8% vs avg_60d). Confirma operacionalmente a leitura da L01: canal sem aceleração de alcance, patamar mantido via valor médio por pedido. Nenhuma nova informação aqui — o padrão é consistente com o que a L01 registrou como acomodação de patamar.

- **Líder do dia em Cross-Docking distorceu o mix de modalidade de envio:** O Conjunto 5 Potes Tampa Preta (MLB4535865317, Cross-Docking, 20 pedidos — 23,8% do volume) assumiu a liderança do dia, e somado ao Conjunto 5 Potes Tampa Cinza (MLB4535865311, Cross-Docking, 7 pedidos), puxou `fulfillment_mix_yesterday_top10.full_pct` para 47,1% — divergência expressiva vs banda 7d (74,9%) e 30d (73,7%). Ambos têm health=null por volume historicamente insuficiente para cálculo. Isso não é problema por si — Cross-Docking é modalidade legítima — mas adiciona evidência à hipótese da L01 de que o ADS pode estar priorizando variantes fora do núcleo Full historicamente liderado: os itens que rodaram mais livremente hoje são justamente os que não carregam penalização de health visível.

- **Segundo ciclo consecutivo de ADS share ~70% confirmado operacionalmente:** `revenue_ads_yesterday_brl` R$3.228,78 / GMV R$4.622,03 = 69,9% de share ADS, contra 69,8% registrado no ciclo anterior. ROAS 10,87x e ACOS 4,57% são excepcionais. Mas os dois principais anúncios Full que deveriam puxar orgânico (MLB4073003575, health=0,75; MLB3288536143, health=0,71) permanecem com penalização ML ativa pelo segundo ciclo. O dia confirma operacionalmente o risco estrutural da L01: orgânico enfraquecido por health degradada sendo substituído por mídia paga de alta eficiência — o resultado parece sadio no número, a estrutura por trás não está.

- **Ruptura prospectiva iminente no segundo vetor de categoria:** Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full, `available_quantity=9` pós-baixa dos 6 pedidos do dia) com cobertura prospectiva de ~1,5 dias ao ritmo atual. Esse é o único sinal do dia com urgência operacional real: qualquer pedido acima das 9 unidades disponíveis no CD do ML gera cancelamento automático ML, pressionando `reputation.cancellations_rate` que hoje está em zero. A ruptura elimina operacionalmente o segundo vetor de categoria (canecas) e concentra ainda mais o resultado na família IMB501 — que já responde por 44,0% do volume do dia — confirmando o risco de dependência levantado pela L01.

---

### Sinais operacionais relevantes

- **Sinal:** Família IMB501 somou 37 dos 84 pedidos (44,0%), com variantes Cross-Docking (Preta + Cinza) liderando e variante Full com penalização (Vermelha, health=0,71) em terceiro — **interpretação operacional:** a concentração de família é padrão histórico, mas o dado novo é que as variantes sem health penalizado (Preta e Cinza, health=null) dominaram sobre a que tem penalização ativa; se o ADS estiver direcionando exposição para as variantes sem penalização, o mecanismo explica tanto a liderança Cross-Docking quanto a compressão relativa do campeão Full Vermelho.

- **Sinal:** health=0,71 em MLB3288536143 (Conjunto 5 Potes Tampa Vermelha, `is_catalog=true`, `catalog_product_id` MLB44224272, Full) pelo segundo ciclo consecutivo sem direção conhecida — **interpretação operacional:** penalização ativa em anúncio de Catálogo ameaça Buy Box na página do catálogo MLB44224272; sem série temporal de health (D-7 a D-1), não é possível saber se está deteriorando, estável ou em recuperação — e é justamente essa direção que determina se o risco é latente ou ativo. Confirma a evidência da L02 de que a série temporal de health é o dado operacional mais crítico pendente.

- **Sinal:** Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full) com `available_quantity=9` e ritmo de 6 pedidos/dia — cobertura prospectiva ≈1,5 dias — **interpretação operacional:** ruptura iminente em anúncio de Full não é hipótese, é janela de tempo. Cada pedido novo a partir de agora reduz o buffer. Impacto cascata: `reputation.cancellations_rate` sai de zero e a L01 já sinalizou que o Kit Canecas Tulipa é o único vetor de diversificação de categoria visível na conta.

- **Sinal:** Kit 10 Potes Herméticos 320ml 10 Unidades (MLB6739241224, Cross-Docking) com `available_quantity=6` pós-baixa de 2 pedidos — cobertura prospectiva ≈3 dias — **interpretação operacional:** risco de segunda ordem abaixo do Kit Canecas Tulipa (Cross-Docking é menos crítico que Full em ruptura); mas se ADS direcionar mais tráfego para esse item, a cobertura colapsa rapidamente. Monitoramento secundário.

- **Sinal:** 7 anúncios ativos com low_health confirmado (`account_overview.active_analysis.low_health_count=7`), mas apenas MLB4073003575 e MLB3288536143 visíveis no top 10 — **interpretação operacional:** há 5 anúncios com penalização orgânica ativa fora do campo de visão do ciclo. Se algum desses 5 compõe a cauda de vendas que sustenta o orgânico residual (~R$1.393,25 que não vieram de ADS), a conta pode ter exposição orgânica penalizada mais ampla do que os dois campeões visíveis sugerem.

---

### Anomalias ou ausência de anomalia

**Anomalia leve.** Reputação verde (`5_green`), cancelamento isolado (1 — ruído, não padrão), nenhum anúncio pausado rodando pedidos, GMV dentro da banda dos pares do mesmo dia (-2,1%). Os desvios perceptíveis são dois: (1) inversão de mix de modalidade de envio (Full 47,1% vs 73,7% nos 30d) causada por produto-específico identificável, sem padrão acumulado além do dia; (2) estoque crítico prospectivo no Kit 6 Canecas Tulipa em Full — este é o único sinal com prazo de ação, mas ainda não cruzou o limiar de ruptura efetiva. O que elevaria para **anomalia moderada**: ruptura efetiva do Kit Canecas Tulipa gerando cancelamentos automáticos (cancellations_rate saindo de zero), ou confirmação de que a inversão de mix de modalidade de envio no top 10 está se repetindo por segundo dia consecutivo com a mesma causa ADS, sugerindo padrão e não rotação aleatória.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Qual é a disponibilidade real e o status de reposição agendada no CD do ML do Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full, `available_quantity=9`)? — **motivada por:** Sinal 3 — cobertura de ~1,5 dias ao ritmo de 6 pedidos/dia; ruptura gera cancelamento automático ML e impacta `cancellations_rate` que está em zero; é a única decisão com janela de tempo no ciclo.

- **Pergunta:** Qual é a série temporal de health (D-7 a D-1) para MLB4073003575 (0,75) e MLB3288536143 (0,71) — estabilizando, caindo ou subindo por ciclo? — **motivada por:** Sinal 2 e Leitura 3 — segundo ciclo com valores pontuais idênticos mas sem direção; para MLB3288536143 (`is_catalog=true`), direção descendente contínua ativa risco de Buy Box; direção estável ou ascendente muda completamente a urgência tática.

- **Pergunta:** Qual é o breakdown de `revenue_ads_yesterday_brl` (R$3.228,78) por `platform_item_id` (top 5 por spend) — Himmel está priorizando os Cross-Docking da família IMB501 ou os Full penalizados? — **motivada por:** Leitura 2 e Sinal 1 — se o ADS share de 69,9% está sendo direcionado para os itens Cross-Docking sem health penalizado, isso explica simultaneamente a inversão do mix de modalidade de envio e a aparente substituição do orgânico Full por mídia. É a chave para separar "Himmel deslocou foco" de "orgânico Cross-Docking reagiu por demanda própria".

- **Pergunta:** Quais são os IDs e o volume estimado dos 5 anúncios com low_health fora do top 10 (`low_health_count=7`, 2 já visíveis no top 10)? — **motivada por:** Sinal 5 — cauda de penalização orgânica invisível; se algum desses 5 compõe o orgânico residual (~R$1.393 fora do ADS), a penalização orgânica da conta é mais ampla do que os dois campeões sugerem.

---

### Destaque para a Condensadora

O fato operacional central do dia não está no resultado — está na estrutura que o produziu: pelo segundo ciclo consecutivo, ~70% do GMV veio de ADS enquanto os dois principais anúncios Full que deveriam sustentar orgânico operam com penalização de health ativa. O dia confirma esse padrão operacionalmente: os itens que lideraram (Tampa Preta e Tampa Cinza, Cross-Docking, sem health calculada) correram com mais liberdade do que os campeões Full penalizados, e o GMV se manteve em banda não porque o orgânico reagiu, mas porque o ticket subiu e o ADS compensou. A Condensadora deve destacar que o risco estrutural levantado pela L01 não é hipótese especulativa — é o mecanismo pelo qual o dia funcionou. O único sinal com urgência de ação concreta é prospectivo e isolado: o Kit 6 Canecas Tulipa em Full com ~1,5 dias de runway, cuja ruptura seria o primeiro evento visível de deterioração operacional — e que pode passar despercebido por quem lê só o GMV do dia.