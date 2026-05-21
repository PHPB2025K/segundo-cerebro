<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` são templates sem dados preenchidos — não há consolidação semanal nem tese mensal registrada. Sem hipóteses ativas de ciclos anteriores para confirmar ou refutar: esta leitura é **ponto zero da memória**, não confirmação de tese. Dados ML opcionais (reputação, fulfillment mix, ADS summary) vieram completos com `status: ok` — o snapshot ML está robusto. A limitação é a memória histórica rasa, não a qualidade do dado de hoje.

---

### Leitura temporal

- **vs 60d e 30d — ticket sobe, volume flat:** GMV R$5.087,71 está +33,3% acima da média bimestral (R$3.817,90) e +15,7% acima da média mensal (R$4.396,77), mas pedidos ficaram essencialmente flat vs 60d (-0,2% vs avg_60d=91,2) e abaixo do 30d (-8,9% vs avg_30d=99,9). Ticket médio R$55,91 vs média 60d R$41,86 (+33,6%) e vs 30d R$44,03 (+27,0%). A conta está faturando mais com o mesmo volume de pedidos — o vetor de crescimento é ticket, não alcance. Esse padrão se repete em ambas as janelas longas: não é evento.

- **vs mesmo dia da semana — controle confirma:** 91 pedidos vs avg_same_weekday de 92,5 (-1,6%) — volume praticamente idêntico ao par histórico. GMV R$5.087,71 vs avg R$3.841,73 (+32,4%). O controle de sazonalidade elimina a hipótese de dia da semana favorável: a força é de ticket e mix, não de tráfego.

- **vs 7d — divergência de ticket explicada:** Pedidos -20,9% e GMV -4,3% vs avg_7d (115,1 pedidos, R$5.315,70). A semana recente incluiu dias de maior volume a ticket menor — o dia de ontem inverteu a composição (menos pedidos, mais ticket). Isso é consistente com o padrão 30d/60d, mas indica que a semana recente teve algo que elevou o volume (provável intensificação de ADS ou campanha pontual — hipótese, sem dado para confirmar).

- **Hipóteses anteriores:** Nenhuma ativa — memória vazia. A leitura de hoje estabelece as primeiras hipóteses, não confirma nenhuma.

---

### Leitura estratégica

- **O crescimento de GMV é real, mas narrow.** A trajetória 60d confirma patamar de ticket em ascensão (+33,6%), não de alcance. A conta está convertendo mais por pedido — seja por mix de kits maiores, seja por composição de campanha ADS direcionada a SKUs de ticket mais alto. Esse tipo de crescimento é mais frágil do que expansão de volume: depende de manter a composição de campanha e o mix de produto estáveis. Qualquer mudança de estratégia ADS ou ruptura de SKU de alto ticket reverte o indicador rapidamente.

- **ADS é o motor atual — e isso é fragilidade estrutural latente.** `ml_snapshot.ads_summary`: gasto R$262,19, receita atribuída R$3.041,56 — ROAS 11,6x, ACOS 4,33% (campanha Himmel extremamente eficiente). Esse resultado representa **59,8% do GMV total do dia** (R$3.041,56 / R$5.087,71): conta em zona de **ADS dominante**. A eficiência não é o problema — o risco é que, sem confirmação de base orgânica por baixo, qualquer pausa ou redução de campanha remove mais da metade do faturamento. Sem histórico de ADS share em ciclos anteriores (memória vazia), não é possível dizer se 60% é padrão ou escalada recente.

- **Dois campeões operam em penalização de ranking ML.** Kit 4 Potes de Vidro 1050ml (MLB4073003575, 2º produto, 13 pedidos) tem `health=0,75`. Conjunto 5 Potes Tampa Vermelha (MLB3288536143, 5º produto, 5 pedidos) tem `health=0,71`. Ambos abaixo do threshold ML de 0,85, ambos em `logistic_type=fulfillment` (Full) — a penalização de ranking ocorre no orgânico, não no fulfillment. Se ADS estiver sustentando a exposição desses anúncios, a degradação de health pode estar mascarada no faturamento hoje. A leitura orgânica desses dois é decrescente enquanto health não for recuperada.

- **O líder é Cross-Docking e puxa o mix do dia.** Conjunto 5 Potes Tampa Preta (MLB4535865317, 1º produto, 23 pedidos) é `cross_docking`, sem Frete Grátis, `health=null`. O mix top10 ontem ficou em 56,3% Full — abaixo do mix 7d (77,7%) e 30d (73,9%). A divergência é explicada pelo peso do líder em cross-docking. A base da conta (82 ativos vs 174 pausados — razão 2,1x) confirma cauda morta dominante: a operação depende de conjunto restrito de SKUs, com os campeões tendo mix de fulfillment superior à base mas heterogêneo entre si.

---

### Tese da conta

**Vulnerável.** O GMV +33,3% vs 60d e o ticket +33,6% confirmam trajetória real de upgrading de mix — não ruído de um dia. Mas a estrutura que sustenta esse resultado concentra risco em três frentes simultâneas: ADS representa ~60% do GMV sem confirmação de base orgânica, dois dos cinco campeões operam com `health` abaixo de 0,85 e em penalização de ranking ML, e um anúncio top-10 está com `available_quantity=3` (Kit 06 Canequinhas Acrílico — ruptura iminente). A cauda está morta (174 pausados vs 82 ativos). O número de hoje é forte; a estrutura que o produz não está confirmada como sustentável.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads (Himmel) como vetor primário do faturamento, com ADS share ~60% e sem evidência confirmada de base orgânica que sustente o patamar de forma autônoma.

**Por que importa:** Se as campanhas reduzirem — por revisão de verba, pausa operacional, ajuste de estratégia ou qualquer fricção no fluxo Yasmin → Himmel — a conta perde mais da metade do GMV atual sem sinal de aviso no dia anterior. A eficiência de ROAS 11,6x confirma que Himmel está operando bem hoje; não confirma que o orgânico existe em volume suficiente para segurar o patamar.

**Histórico:** Sem registros em ciclos anteriores (weekly.md e monthly.md vazios). Não é possível afirmar se o ADS dominante é padrão histórico ou escalada recente. A hipótese é candidata, não conclusão — hoje é o primeiro ciclo com leitura de share disponível.

**Sinal de confirmação:** ADS share acima de 55% por 3 dias seguidos confirma dependência estrutural. Se o share cair abaixo de 35% num dia com GMV acima de R$4.000 sustentado, confirma base orgânica relevante e enfraquece o risco.

---

### Sinais a observar

1. **Ruptura de estoque do Kit 06 Canequinhas Acrílico (MLB4410218897) nas próximas 24h.** `available_quantity=3` com 3 pedidos ontem — qualquer venda adicional hoje já compromete atendimento. Se o anúncio entrar em out-of-stock, gera cancelamentos prospectivos que ainda não aparecem na `reputation.cancellations_rate` (janela longa, hoje em 0); o impacto na reputação virá nos próximos ciclos sem aviso agregado imediato.

2. **GMV abaixo de R$4.500 por 2 dias seguidos refuta a tese de patamar.** O bimestre médio é R$3.817,90; o dia ficou +33% acima. Dois dias consecutivos abaixo de R$4.500 indicam que o movimento é pico pontual (possivelmente ADS específico ou data de demanda), não patamar estabelecido — e a trajetória de ticket volta a ser inconclusiva.

3. **`health` do Kit 4 Potes 1050ml (MLB4073003575) abaixo de 0,75 ou Conjunto 5 Potes Tampa Vermelha (MLB3288536143) abaixo de 0,70 em leitura seguinte confirma deterioração acelerada de exposição orgânica nesses dois campeões** (se `top_items_details` disponível no pacote). Estabilidade ou recuperação enfraquece o risco de erosão de ranking em Full.