<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória com dois ciclos diários recentes ingeridos (22/05 e 23/05 via `weekly.md`); `monthly.md` está em template vazio sem tese mensal consolidada — âncora histórica de longo prazo ausente. Todas as janelas quantitativas (7d, 30d, 60d, mesmo dia da semana) disponíveis com cobertura completa. `ml_snapshot` integralmente presente: reputação, mix de modalidade de envio (7d e 30d, coverage 100%), `top_items_details`, `ads_summary` e `account_overview` com `status: ok`. Hipóteses das leituras de 22/05 e 23/05 têm dados suficientes para confronto.

---

### Leitura temporal

- **Patamar vs 30d e 60d:** GMV de R$5.024,80 está +10,4% acima da média de 30d (R$4.549,64; `changes.gmv_vs_30d_pct`) e +22,7% acima da média de 60d (R$4.096,61; `changes.gmv_vs_60d_pct`), com volume de pedidos praticamente flat (99 vs 99,7 no 30d, -0,7%). A totalidade do ganho de faturamento é por ticket: R$50,76 vs R$45,65 no 30d (+11,2%) e vs R$42,73 no 60d (+18,8%). O patamar subiu; o alcance de pedidos, não.

- **Controle de sazonalidade:** A média dos últimos quatro domingos é R$3.691,93 e 78,75 pedidos (`same_weekday_avg`). O dia ficou +36,1% em GMV e +25,7% em pedidos acima do par histórico — o resultado não é forte apenas em relação às médias gerais; é forte dentro do próprio dia da semana. O único domingo recente comparável é 17/05 (R$5.180, 100 pedidos).

- **Hipóteses anteriores — health estagnado:** MLB3288536143 (Conjunto 5 Potes de Vidro Redondos) permanece em `health=0,71` (Padrão inferior) e MLB4073003575 (Kit 4 Potes 1050ml) em `health=0,75` (Padrão inferior) — ambos pelo **quarto ciclo consecutivo** sem variação. A leitura de 23/05 esperava que o quarto ciclo "definiria direção do nível": a direção confirmada é estagnação em Padrão inferior. Nenhum dos dois campeões principais saiu da zona de risco.

- **Hipóteses anteriores — ADS share e Kit Canecas Tulipa:** ADS share voltou a 71,2% (R$3.578/R$5.025) após recuo a 49,5% em 23/05 — o recuo de um dia não confirmou expansão orgânica, foi oscilação. Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090), registrado com 2 unidades em 23/05 e ritmo de 6–9 pedidos/dia, está ausente do `top_items_details` e do top 10 de hoje — ruptura ou esgotamento provável; impacto em `cancellations_rate` ainda não capturado pela API (janela longa), mas 2 cancelamentos no `metrics.cancelamentos` do dia podem ser relacionados.

---

### Leitura estratégica

- **Ganho de faturamento por ticket, vetor único e frágil (Lente 1):** A conta acumulou ~R$900/dia de GMV médio na janela de 60d sem expansão de volume de pedidos. Esse padrão — mais faturamento, mesmo alcance — indica melhora de mix ou ticket por anúncio, não crescimento de base de compradores. O ganho é real, mas unidimensional: se o ticket cair (por pressão de preço, mudança de mix ou promoção do marketplace), o faturamento recua sem volume como amortecedor. A aceleração de ticket está presente nas duas janelas longas (30d e 60d), o que eleva a confiança de que é movimento de patamar, não ruído.

- **ADS sustenta o patamar cobrindo déficit orgânico dos campeões, não amplificando orgânico saudável (Lente 5):** `ads_summary.revenue_ads_yesterday_brl=R$3.578,05` / `metrics.gmv=R$5.024,80` = **ADS share de 71,2%** — zona de ADS dominante. ROAS de 11,36x (`R$3.578/R$315,10`) e ACOS de 4,19% confirmam eficiência de campanha alta. O problema não é a eficiência — é o que está por baixo: com MLB3288536143 e MLB4073003575 em nível de qualidade Padrão inferior pelo quarto ciclo, o ML já restringe exposição orgânica a esses anúncios. O ADS de Himmel está compensando ranking orgânico perdido, não amplificando posição orgânica forte. A dependência se auto-reforça: menos orgânico → mais ADS necessário → menos volume orgânico para o ML calibrar health positivamente.

- **Concentração em MLB3288536143 aprofunda-se sobre anúncio em Padrão inferior (Lente 3 + Lente 4):** O cluster IMB501 (Tampa Preta 29 + Tampa Vermelha 10 + Tampa Cinza 8 = **47 pedidos, todos no mesmo `platform_item_id` MLB3288536143**) representa **47,5% dos pedidos do dia** — acima dos 44% de 23/05 e dos 44% de 22/05. O anúncio opera com `health=0,71` (Padrão inferior), `is_catalog=false` (Clássico, compete por posição em categoria, não Buy Box), `logistic_type=fulfillment` (Full, estoque no CD do ML). O volume crescente em anúncio com saúde orgânica deprimida é sustentado por ADS, não por posição de ranking. `top5_concentration=74,7%` confirma que o segundo vetor existe mas é fraco — a cauda não compensaria ruptura no cluster IMB501.

- **Dois estoques críticos com perfis de recuperação distintos (Lente 3):** MLB6232315532 (Kit 6 Canecas Lisas 200ml, Catálogo, gold\_pro Premium, Full, `available_quantity=25`, 9 pedidos hoje) — cobertura estimada de **~2,8 dias**. Modalidade Full: ruptura exige reposição ao CD do ML antes de retomar estoque; em anúncio Catálogo, a perda de Buy Box demora a se recuperar mesmo após reposição. MLB6582645908 (Kit 6 Canecas Porcelana 250ml, Cross-Docking, `available_quantity=1` após 3 pedidos hoje) — **ruptura praticamente certa no próximo ciclo**; Cross-Docking tem recuperação mais rápida porque o estoque está na expedição Budamix, mas o ML pode pausar o anúncio automaticamente e gerar cancelamentos prospectivos.

---

### Tese da conta

**Vulnerável.** O faturamento da conta ML cresceu estruturalmente (+22,7% vs 60d, consistente em 30d e no controle de dia da semana), mas o mecanismo de sustentação é frágil em camadas: o ganho é inteiramente por ticket médio com volume de pedidos flat; o ticket é sustentado por ADS que cobre o déficit de ranking orgânico dos campeões em Padrão inferior (MLB3288536143 e MLB4073003575, quarto ciclo sem evolução); e o volume se concentra progressivamente num único `platform_item_id` (47,5% dos pedidos). Com ADS share em 71,2%, qualquer interrupção de campanha expõe a ausência de orgânico saudável — o patamar não se sustenta por si. A projeção MercadoLíder Platinum está no caminho (progresso 83,47%, gap R$48.941, ETA ~11,9 dias), mas qualquer combinação de ruptura em Canecas Lisas (Full) + cancelamentos prospectivos de MLB6167272090 + oscilação de campanha estreita simultaneamente o ETA e a saúde estrutural da conta.

---

### Risco estrutural principal

**Risco:** ADS dominante (share 71,2% em 24/05) operando sobre campeões com nível de qualidade do anúncio em Padrão inferior pelo quarto ciclo consecutivo — MLB3288536143 (`health=0,71`) e MLB4073003575 (`health=0,75`) — sem sinal de recuperação. O orgânico não sustenta o patamar de faturamento sem mídia paga.

**Por que importa:** A estrutura cria dependência crescente e auto-reforçada: o ML restringe exposição orgânica de anúncios em Padrão inferior; o ADS compensa, mas sem volume orgânico suficiente para o ML recalcular health positivamente; o health estagna, exigindo ADS ainda mais para manter posição. Se Himmel pausar, reduzir verba ou ACOS subir acima do threshold interno, o faturamento recua sem amortecedor — e os campeões, com health deprimido, não recuperam posição orgânica rapidamente. O cluster IMB501 (47,5% dos pedidos) amplifica a vulnerabilidade: um único anúncio com saúde orgânica degradada carrega quase metade do volume.

**Histórico:** Sinal detectado em 22/05 (ADS share 69,9%, segundo ciclo consecutivo acima de 65%, health já em Padrão inferior). Em 23/05, share recuou a 49,5% (não confirmou tendência naquele ciclo), mas health permaneceu estagnado. Em 24/05, share volta a 71,2% com health ainda sem movimento — dois pontos altos separados por um recuo não invalidam a tendência estrutural; o health é o dado mais estável e é o que define o risco.

**Sinal de confirmação:** ADS share acima de 65% por dois ciclos consecutivos — sem melhora de `health` em MLB3288536143 acima de 0,85 (saída de Padrão inferior) — nos próximos 5 dias confirma dependência estrutural. Se `health` de MLB3288536143 cair abaixo de 0,70 (entrada em Básico), o risco passa de latente a crítico.

---

### Sinais a observar

1. **MLB6232315532 (Kit 6 Canecas Lisas 200ml) em ruptura iminente Full:** `available_quantity=25`, ~9 pedidos/dia → cobertura estimada de 2–3 dias. Se o anúncio pausar ou zerar estoque por **2 dias consecutivos**, confirma perda de Buy Box em anúncio Catálogo Premium Full — impacto direto em faturamento do cluster de canecas e em trajetória Platinum (receita da janela 60d rolling).

2. **ADS share por ciclo:** Share acima de 65% por **segundo ciclo consecutivo** nos próximos 5 dias, sem `health` de MLB3288536143 ou MLB4073003575 superando 0,85, confirma que a dependência de ADS é estrutural — orgânico não está em expansão e o mecanismo de auto-sustentação não está funcionando. Gatilho para Yasmin acionar revisão com Himmel e Kobe.

3. **Health dos campeões no quinto ciclo:** MLB3288536143 em `health ≤ 0,71` e MLB4073003575 em `health ≤ 0,75` no próximo pacote confirma estagnação por cinco leituras consecutivas — hipótese ativa de que nível de qualidade Padrão inferior se tornou estado estável nos dois principais anúncios, não condição transitória. Qualquer `health ≥ 0,85` em qualquer dos dois seria reversão da tendência e enfraqueceria o risco estrutural principal.