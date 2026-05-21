<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` chegaram com estrutura de template sem conteúdo real — sem tese semanal, hipóteses ativas ou padrões consolidados. Yasmin assumiu o ML em 22/04/2026; o histórico computado (7d/30d/60d) existe com cobertura 100%, mas a memória qualitativa está em ponto zero. Sem hipóteses anteriores para confirmar ou refutar — leitura de hoje serve como linha de base da série qualitativa. Dados ML opcionais (reputação, mix fulfillment, ADS) todos presentes com `status: ok`; base suficiente para tese honesta, não para tese confirmada.

---

### Leitura temporal

- **vs 60d e 30d — ticket em expansão consistente:** GMV de R$5.087,71 está +34,2% acima da média de 60 dias (R$3.792,04) e +15,7% acima dos 30 dias (R$4.396,77), com volume de pedidos praticamente igual ao patamar de 60d (`orders_vs_60d_pct = -0,2%`) e levemente abaixo dos 30d (`orders_vs_30d_pct = -8,9%`). O ticket médio saiu de R$41,56 (60d) → R$44,03 (30d) → R$55,91 hoje (`ticket_vs_60d_pct = +34,5%`), movimento confirmado em duas janelas longas — não é ponto, é trajetória.

- **vs mesmo dia da semana — volume estável, GMV em ruptura positiva:** Controle de sazonalidade confirma: pedidos quase neutros (`orders_vs_same_weekday_pct = -1,6%`; avg 92,5 vs 91 do dia) com GMV +32,4% (R$5.087 vs avg R$3.841). Os 4 registros do mesmo dia mostram alta volatilidade (65→87→134→84 pedidos); o dia 29/04 com 134 pedidos e R$5.618 é outlier que infla a média de 7d — o pico já passou, o que explica `orders_vs_7d_pct = -20,9%` sem ser sinal de deterioração.

- **vs 7d — normalização após pico, GMV sustentado por ticket:** A média de 7 dias (115,1 pedidos, R$5.315,7) está acima do dia por efeito do outlier de 29/04. A queda de -20,9% em pedidos com apenas -4,3% em GMV no mesmo intervalo reforça: o dia não é fraqueza operacional, é normalização de volume com ticket preservando o patamar de faturamento.

- **Hipóteses anteriores:** Sem conteúdo em `weekly.md` ou `monthly.md`, não há hipóteses ativas para confirmar, enfraquecer ou refutar. Ponto de partida da memória qualitativa.

---

### Leitura estratégica

- **Expansão de ticket como vetor de GMV (Lente 1):** A conta cresce em faturamento sem crescer em alcance — o GMV sobe 34,2% em 60 dias enquanto o volume de pedidos fica neutro (`-0,2%`). A composição do top10 oferece pista: kits de maior valor (Kit 10 Potes 1050ml, Kit 4 Potes 1050ml, Kit 2 Potes 1050ml) ganharam peso no dia. Hipótese: o portfólio está migrando para produtos de maior ticket médio, seja por recomposição de mix via ADS ou por organização recente de anúncios — não é possível confirmar sem rastrear evolução de GMV por produto nas janelas longas, mas o padrão em 30d e 60d é consistente o suficiente para ser a tese central da conta agora.

- **ADS sustentando o patamar sobre base orgânica com saúde degradada (Lente 5 + Lente 4):** ADS share calculado: R$3.041,56 / R$5.087,71 = **59,8%** — conta em zona ADS dominante. ROAS 11,6x e ACOS 4,33% indicam campanha extremamente eficiente; Himmel está entregando resultado. O problema não é hoje: é que o orgânico que carrega os outros 40% opera com dois campeões em Full com health penalizada — Kit 4 Potes 1050ml (`MLB4073003575`, 2º maior do dia, `health = 0,75`) e Conjunto 5 Potes Tampa Vermelha (`MLB3288536143`, `health = 0,71`). Health abaixo de 0,85 significa penalização ML de exposição orgânica já ativa nesses listings. O patamar de R$5.000+ não é orgânico — é ADS sobre base degradada.

- **Campeões vivem em Full; a base não (Lente 3):** O mix do top10 do dia (Full 56,3%) e das janelas 7d/30d (Full 77,7% e 73,9%) contrasta com o mix da base ativa: `account_overview.active_analysis.fulfillment_mix.full_pct = 34,1%`. Os anúncios que vendem são os que estão em Full — a maioria dos 82 ativos (Cross-docking 65,9%) vende pouco ou nada. Paused/Active ratio de 174/82 = 2,12x confirma cauda morta. A conta opera com uma minoria em Full carregando o volume; qualquer ruptura de estoque nesse núcleo não tem substituto imediato na cauda.

- **Estoque em horizonte curto em dois itens do top10:** Kit 6 Tigelas de Vidro 250ml (`MLB6167272090`, 5 pedidos, `available_quantity = 21`) e Kit 6 Canequinhas Acrílico com Suporte (`MLB4410218897`, 3 pedidos, `available_quantity = 4`). Ao ritmo de ontem, as Canequinhas têm estoque para 1 a 2 dias. Ruptura nesses dois não afeta o volume macro da conta (juntos representam ~8 pedidos), mas reduz a diversificação real da cauda ativa.

---

### Tese da conta

**Vulnerável.** O GMV está em expansão estrutural confirmada em 30d e 60d, puxado por ticket em ascensão consistente — esse é o movimento real da conta. Mas o patamar atual (R$5.000+) é sustentado por ADS com share acima de 59% operado por Himmel com eficiência alta, sobre uma base orgânica que não está se fortalecendo no mesmo ritmo: dois campeões Full com health penalizada, cauda praticamente morta e estoque crítico em pelo menos um item de rotação. A reputação está verde-estável (`color = 5_green`, `power_seller_status = gold`, `cancellations_rate = 0`) — a conta não está em deterioração visível. Mas o crescimento de GMV depende de ADS eficiente continuando a funcionar sobre estrutura orgânica que, se observada isoladamente, não sustentaria o patamar atual.

---

### Risco estrutural principal

- **Risco:** Dependência de Mercado Ads (ADS share 59,8%) sem base orgânica saudável como plano B — dois campeões Full com health penalizada (`health = 0,75` e `0,71`) e cauda morta (174 pausados vs 82 ativos = 2,12x o threshold de 1,5x).
- **Por que importa:** Se as campanhas de Himmel forem pausadas, reduzidas ou perderem eficiência (ROAS abaixo de 5x), o GMV recua para o orgânico — que hoje opera com penalização ativa de exposição nos principais anúncios em Full. A combinação de ADS dominante + health degradada em campeões é risco acumulado: individualmente tolerável, estruturalmente frágil.
- **Histórico:** Sem `weekly.md` ou `monthly.md` preenchidos, não há registro de quando essa dependência se formou nem se é padrão desde 22/04. Identificado agora como linha de base — sem confirmação de recorrência anterior.
- **Sinal de confirmação:** ADS share acima de 55% por 3 dias consecutivos (`ads_summary` disponível no pacote) combinado com health do Kit 4 Potes 1050ml permanecendo abaixo de 0,80 por mais 2 ciclos confirma dependência estrutural ativa e sem reversão orgânica em curso.

---

### Sinais a observar

1. **GMV acima de R$4.800 por 3 dias consecutivos** — confirmaria consolidação do novo patamar de ticket (~R$55) como tendência estrutural; se GMV cair abaixo de R$4.000 por 2 dias seguidos, a expansão de ticket foi ADS-inflada e está revertendo sem o pico de volume.

2. **Kit 6 Canequinhas Acrílico com Suporte (`MLB4410218897`, `available_quantity = 4`) sumindo do top10 por 2 dias consecutivos** — confirmaria ruptura de vetor por exaustão de estoque; ao ritmo de 3 pedidos/dia, o horizonte é de 1 a 2 dias. Kit 6 Tigelas de Vidro 250ml (`MLB6167272090`, `available_quantity = 21`) com mesmo padrão de ausência indica segundo vetor em ruptura simultânea.

3. **Health do Kit 4 Potes 1050ml (`MLB4073003575`) caindo abaixo de 0,70 ou permanecendo abaixo de 0,80 por mais 2 ciclos** — confirmaria deterioração orgânica progressiva em 2º campeão Full; se health retornar acima de 0,85 nos próximos 2 pacotes, hipótese de degradação ativa se enfraquece (sinal condicional à disponibilidade do campo `health` no pacote).