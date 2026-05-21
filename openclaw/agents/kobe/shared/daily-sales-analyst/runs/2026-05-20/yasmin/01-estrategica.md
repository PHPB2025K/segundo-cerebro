<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` estão com templates vazios — sem nenhuma entrada histórica consolidada. Não há hipóteses anteriores registradas, nenhum padrão documentado, nenhuma tese para confirmar ou refutar; esta leitura é ponto de partida, não continuação de série. As séries numéricas (7d / 30d / 60d / mesmos dias da semana) estão disponíveis e coerentes. Reputação, mix de fulfillment, health dos campeões e `ads_summary` estão presentes no pacote. Único dado ausente relevante: posição em categoria / ranking Mais Vendido e share de Buy Box por anúncio — sem esses, a leitura de exposição orgânica individual é parcial.

---

### Leitura temporal

- **Patamar bimestral em expansão pelo ticket, não pelo volume.** `avg_60d`: 91,2 pedidos / R$3.817,90 GMV / R$41,86 ticket. Hoje: 91 pedidos / R$5.087,71 GMV / R$55,91 ticket. O volume de pedidos praticamente não se moveu (`orders_vs_60d_pct = -0,2%`), mas o GMV cresceu 33,3% e o ticket 33,6%. A conta não está alcançando mais compradores — está extraindo mais receita por pedido. A trajetória de ticket é consistente nas três janelas: R$41,86 (60d) → R$44,03 (30d) → R$46,17 (7d) → R$55,91 (hoje), sugerindo movimento contínuo, não pico pontual.

- **7d em desaceleração de pedidos, mas ticket acima da média recente.** Média 7d: 115,1 pedidos / R$5.315,70 GMV / R$46,17 ticket. Hoje ficou -20,9% em pedidos vs 7d, mas o ticket de R$55,91 supera a média 7d em +21%. O 7d pode estar inflado por dias de pico recentes (29/04 = 134 pedidos / R$5.618 — mesma quarta-feira da série); a desaceleração de volume não é necessariamente deterioração.

- **Controle sazonal reforça o ganho de GMV e isola o ticket como vetor.** Vs mesmas quartas (últimas 4): GMV de hoje +32,4% com pedidos -1,6%. O dia não é excepcional em volume — é excepcional em ticket. As quartas de 06/05 e 13/05 foram fracas (R$3.005 e R$2.984); hoje é a segunda maior quarta da série, atrás apenas de 29/04. A alternância forte–fraco–fraco–forte nas quartas recentes levanta hipótese de ciclo ou ajuste de campanha, mas com apenas 4 pontos e sem histórico semanal consolidado, é inconclusiva por ora.

- **Sem hipóteses anteriores para confirmar ou refutar.** `weekly.md` e `monthly.md` estão vazios. Toda observação é inaugural.

---

### Leitura estratégica

- **Lentes 1 + 5 — O ganho de GMV vs 60d é real, mas ADS é o motor não declarado.** O crescimento de patamar (+33,3% GMV vs 60d, +32,4% vs mesmas quartas) é consistente em múltiplas janelas — não é ruído. Mas a decomposição é crítica: ADS (Himmel) gerou R$3.041,56 com investimento de R$262,19 — ROAS de 11,6x, ACOS de 4,64%, eficiência operacional alta. Esse valor representa **59,8% do GMV do dia** (R$3.041,56 / R$5.087,71), colocando a conta em zona ADS dominante. O crescimento de ticket e GMV que aparece nas janelas longas é provavelmente conduzido por campanha, não por posicionamento orgânico autossustentável. O ROAS forte não neutraliza a fragilidade estrutural: se Himmel pausar ou reduzir verba, a base orgânica é incógnita — ainda sem validação.

- **Lente 3 — Cauda morta dominante + concentração crônica sem segundo vetor confirmado.** 174 anúncios pausados contra 82 ativos (razão 2,1:1, bem acima do limiar de 1,5 que define cauda morta dominante). Top 3 concentra 48,4% do GMV; top 5, 59,3%. O líder isolado (Conjunto 5 Potes Tampa Preta, MLB4535865317) responde por 25,3% dos pedidos do dia sozinho. O mix de fulfillment aprofunda a dependência: os campeões de ontem usaram 56,3% Full (`fulfillment_mix_yesterday_top10.full_pct`) contra 34,1% Full na base inteira (`account_overview.active_analysis.fulfillment_mix.full_pct`) — os anúncios que vendem são excepcionalmente dependentes de Full em relação ao resto do portfólio. Ruptura em qualquer dos top 3 em Full não tem amortecimento de cauda.

- **Lentes 2 + 4 — Reputação estrutural intacta, mas health degradada nos campeões corrói exposição orgânica de forma silenciosa.** Reputação `5_green`, `power_seller_status=gold`, `cancellations_rate=0`, `claims_rate=0,0025` — operação estruturalmente limpa e elegível Mercado Líder. Mas Kit 4 Potes 1050ml (MLB4073003575, 2º do dia com 13 pedidos) tem `health=0,75` e Conjunto 5 Potes Tampa Vermelha (MLB3288536143, 5º do dia com 5 pedidos) tem `health=0,71` — ambos abaixo de 0,85, com penalização de ranking ativa por ML. Os dois são `is_catalog=false`, competindo por posição em categoria via ranking Clássico: health degradada corrói essa posição progressivamente sem que a API de reputação capture o sinal. A reputação protege o selo; o health corrói o alcance orgânico dos anúncios individualmente.

- **Lente 3 — Estoque efetivamente zerado em campeão ativo.** Kit 06 Canequinhas Acrílico (MLB4410218897) tem `available_quantity=3` após 3 pedidos em 20/05. O anúncio está `status=active` — não pausado. Se o estoque estava em 3 unidades no início do dia e os 3 pedidos foram completados, qualquer venda adicional com saldo zero resulta em cancelamento e impacto em `cancellations_rate` nas próximas janelas da API. Com `cancellations_rate=0` hoje, o sinal ainda não chegou à métrica oficial — mas a condição para gerar cancelamentos já existe.

---

### Tese da conta

**Vulnerável.** A conta entregou GMV +33,3% vs 60d com volume estacionário — crescimento real e consistente em múltiplas janelas, ancorado em ticket médio em trajetória ascendente contínua (+33,6% vs 60d). A reputação está verde estável (`5_green`, `gold`, `cancellations_rate=0`), preservando elegibilidade Mercado Líder. O problema não está nos números do dia — está na estrutura que os produz: ADS (Himmel) carrega 59,8% do GMV com eficiência alta, mas o orgânico por trás é desconhecido; a cauda tem 174 anúncios mortos contra 82 ativos; os dois principais campeões em Full têm health abaixo de 0,85 (0,75 e 0,71); e ao menos um anúncio ativo está com estoque efetivamente zerado. A conta cresce sobre base concentrada, com ADS dominante e health corroída nos que mais vendem — qualquer pausa de campanha ou ruptura de campeão expõe um orgânico que ainda não foi validado.

---

### Risco estrutural principal

- **Risco:** Dependência de Mercado Ads (Himmel) sem validação do orgânico subjacente. ADS share de 59,8% do GMV coloca a conta em zona onde qualquer pausa, redução de verba ou mudança de estratégia de campanha impacta diretamente mais da metade do faturamento — sem segundo vetor comprovado para absorver.
- **Por que importa:** ROAS 11,6x e ACOS 4,64% são resultados operacionalmente excelentes, mas mascaram a pergunta não respondida: o que a conta vende organicamente se as campanhas pararem? Com 174 anúncios pausados, cauda morta dominante e health degradada nos campeões, a hipótese de fragilidade orgânica é mais provável que a de robustez — mas ainda não está confirmada. O crescimento de patamar das janelas longas pode ser inteiramente explicado por escalada de ADS, não por ganho de posicionamento estrutural.
- **Histórico:** `weekly.md` e `monthly.md` vazios. Não é possível determinar se essa dependência é crônica ou recente — primeiro ciclo de observação da conta.
- **Sinal de confirmação:** ADS share acima de 50% do GMV por 3 dias consecutivos confirma dependência estrutural (não apenas resultado de um dia de campanha forte). Se Himmel reduzir verba e o GMV cair proporcionalmente sem recuperação nos 2 dias seguintes, tese confirmada.

---

### Sinais a observar

1. **Health dos campeões em Full abaixo de 0,85 por 2 dias consecutivos:** Kit 4 Potes 1050ml (`health=0,75`, MLB4073003575) e Conjunto 5 Potes Tampa Vermelha (`health=0,71`, MLB3288536143) com health degradada em mais 1 ciclo = penalização ML ativa e persistente corroendo ranking orgânico dos 2º e 5º maiores vetores do dia. Confirma erosão silenciosa de exposição independente de reputação ou ADS.

2. **Kit 06 Canequinhas Acrílico (MLB4410218897) gerando cancelamento ou pausando:** `available_quantity=3` após 3 pedidos em 20/05 — estoque efetivamente zerado. Qualquer registro de cancelamento neste item nas próximas 48h ou pausa do anúncio confirma que a condição se materializou e começa a pressionar `cancellations_rate` (verificar se disponível no próximo pacote).

3. **ADS share mantendo-se acima de 50% do GMV ao longo da semana corrente:** Se o share ADS se mantiver ≥50% por 3 dias consecutivos em condições normais de campanha, confirma que o patamar de GMV e ticket observado nas janelas 30d/60d é estruturalmente dependente de campanha — e a classificação de vulnerável se solidifica com evidência temporal antes da próxima semana.