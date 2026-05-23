<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Weekly com apenas 1 entrada (2026-05-22 — mesmo dia desta análise, segundo ciclo de pipeline); sem entrada de 2026-05-21; `last_daily_file` em 2026-05-20. Monthly sem consolidação preenchida. Base de memória rasa para os últimos dias, sem hipóteses ativas transitando de ciclos anteriores para comparação de progressão. `ml_snapshot` completo: reputação, mix de modalidade de envio, MercadoLíder e `ads_summary` todos com `status: ok` — dados ML robustos para a leitura de hoje, mas sem série de dias consecutivos para confirmar tendências emergentes.

---

### Leitura temporal

- **vs 60d e 30d (patamar):** GMV de R$4.622,03 está +16,3% acima da média 60d (R$3.975,41) e +3,4% acima da média 30d (R$4.470,29). Pedidos recuaram em ambas as janelas (-10,4% vs 60d; -15,4% vs 30d). Ticket médio de R$55,02 está +29,8% vs 60d e +22,3% vs 30d. A conta opera acima do patamar histórico de GMV exclusivamente por expansão de ticket — não por crescimento de volume.

- **vs 7d:** GMV -16,8% e pedidos -25,9% em relação à média de 7 dias (R$5.555,18; 113,3 pedidos). Os últimos 7 dias rodaram num patamar mais alto que a média de 30/60d — ontem representa desaceleração dentro desse intervalo recente, não deterioração estrutural.

- **Controle de dia da semana:** Média das últimas 4 sextas-feiras: 102 pedidos, R$4.718,81 GMV. Ontem: 84 pedidos (-17,6%), R$4.622,03 (-2,1%). Os 4 pontos de controle variam de R$3.214 a R$6.465 — amplitude natural de ~100%. Em GMV, ontem está dentro da banda; em pedidos, ficou abaixo da média mas acima dos dois piores pontos do controle (08/05: 83 pedidos / 24/04: 76 pedidos). O dia foi fraco em volume, não anormal em GMV para essa sexta-feira.

- **Hipóteses anteriores:** O bloco da weekly registra ciclo anterior sobre o mesmo dia (22/05): ADS share 69,9%, health degradada nos campeões Full (0,75 e 0,71), estoque crítico no Kit 6 Canecas Tulipa e cluster IMB501 em 44% do dia. Este é um segundo ciclo de análise sobre os mesmos dados — não há dado de 21/05 para testar progressão de qualquer dessas hipóteses.

---

### Leitura estratégica

- **Ticket como motor, volume como lastre:** O padrão ticket-cresce/volume-cai é consistente nas janelas de 30d e 60d simultaneamente — não é ruído de um dia. A conta converte menos compradores em GMV equivalente por mix de produtos de maior valor (Kit 10 Potes, bundles de canecas). O risco latente: uma queda de exposição em campeão de alto ticket não é absorvida por volume de cauda, que está estruturalmente estagnado (176 anúncios pausados contra 81 ativos, ratio 2,17x acima do limiar de alerta de 1,5x).

- **ADS dominante com orgânico estruturalmente fino:** `ads_summary` — ADS share de 69,9% do GMV (R$3.228,78 / R$4.622,03), ROAS 10,87x, ACOS 4,57%. Campanha Himmel opera em eficiência excepcional, mas o orgânico responde por apenas ~30% da receita. O nível ultrapassa o limiar de fragilidade latente (≥50% = ADS dominante). Sem série histórica de dias consecutivos, não é possível afirmar se esse share é novo ou crônico — mas a condição está ativa hoje e aguarda confirmação no próximo ciclo.

- **Health degradada nos campeões Full mascara perda orgânica:** Lentes 3 e 4 — Kit 4 Potes 1050ml (`health=0,75`, `logistic_type=fulfillment`) e Potes Vidro Tampa Vermelha (`health=0,71`, `logistic_type=fulfillment`) são o 2º e 3º maiores do dia. Health abaixo de 0,85 significa penalização de ranking orgânico ML progressiva. A eficiência de ADS pode mascarar essa deterioração: Himmel compensando exposição orgânica reduzida com mais campanha torna a degradação de health estruturalmente mais perigosa — cria ciclo de retroalimentação onde menos orgânico exige mais gasto.

- **Mix de modalidade de envio: divergência entre dia e janela longa é sinal de composição, não ruptura:** `fulfillment_mix_yesterday_top10`: Full 47,1% / Cross-Docking 52,9%. `fulfillment_mix_7d`: Full 74,9% / Cross-Docking 25,1%. `fulfillment_mix_30d`: Full 73,7% / Cross-Docking 26,3%. A divergência entre ontem (47% Full) e a média longa (~74% Full) reflete composição do dia: o campeão do dia foi Conjunto 5 Potes Tampa Preta (`cross_docking`, 20 pedidos) enquanto os campeões Full estão com health penalizada. Não é mudança de operação — é o reflexo de Full penalizado gerando menos demanda orgânica e Cross-Docking compensando com estoque abundante (8.375 unidades).

---

### Tese da conta

**Vulnerável.** A conta ML sustenta GMV acima do patamar histórico de 60 dias (+16,3%) por expansão de ticket (+29,8% vs 60d), mas a estrutura é frágil: volume de pedidos em queda nas mesmas janelas (-10,4% vs 60d), 70% do faturamento dependente de Mercado Ads (share 69,9% — sem série para confirmar se é crônico), dois campeões Full com health penalizada (0,75 e 0,71), e cauda morta dominante (176 anúncios pausados / 81 ativos). A reputação verde estável e o MercadoLíder Gold sem proteção preservam a base estrutural de exposição — mas a engrenagem de geração de receita depende de campanhas eficientes para compensar o que o orgânico degradado deixa de entregar.

---

### Risco estrutural principal

- **Risco:** Dependência de Mercado Ads para sustentação do GMV sem orgânico robusto como base — agravada por health degradada nos dois campeões Full, que reduz progressivamente o alcance orgânico dos anúncios de maior volume individual da conta.
- **Por que importa:** Com ADS share em 69,9%, qualquer redução de verba, pausa de campanha ou compressão de ROAS expõe o fator orgânico real — que já opera com dois campeões penalizados. O risco não é colapso imediato, mas erosão silenciosa: health cadente → ranking orgânico menor → ADS precisa compensar mais → ACOS sobe → eficiência cai → ciclo de retroalimentação.
- **Histórico:** Primeiro ponto real da série para esta conta (não há daily anterior disponível com dado comparável). A weekly registrou o ciclo anterior como "segundo ponto", mas como era o mesmo dia, tecnicamente este ainda é o ponto zero de uma série a construir.
- **Sinal de confirmação:** ADS share acima de 65% por 3 ciclos consecutivos com health dos dois campeões Full mantendo-se abaixo de 0,80 confirma dependência estrutural ativa e deterioração orgânica em paralelo — acionável via Yasmin para revisão com Himmel.

---

### Sinais a observar

1. **Health dos campeões Full no próximo ciclo com dado populado:** Kit 4 Potes 1050ml (MLB4073003575, `health=0,75`) e Potes Vidro Tampa Vermelha (MLB3288536143, `health=0,71`) — se ambos permanecerem abaixo de 0,80 por 2 ciclos consecutivos com dado disponível, a perda de ranking orgânico é confirmada e requer revisão estrutural (se `health` disponível no próximo pacote).

2. **Ruptura iminente do Kit 6 Canecas Tulipa em Full (MLB6167272090):** `available_quantity=7`, `logistic_type=fulfillment`, 6 pedidos no dia. Cobertura de ~1 dia. Se o próximo pacote mostrar `status ≠ active` ou `available_quantity=0`, o anúncio sai do ar sem controle direto de Budamix (Full requer reposição no CD do ML) — impacto imediato em GMV e posição. Yasmin deve verificar status de reposição hoje.

3. **MercadoLíder Platinum — ritmo vs gap:** Gap de R$55.226,77, ETA 13,8 dias mantendo ritmo de R$4.012,89/dia. Se GMV diário ficar abaixo de R$3.800 por 3 dias seguidos, ETA sobe acima de 20 dias e a promoção se afasta de forma significativa. Ontem (R$4.622) superou o ritmo necessário em ~R$609 — sinal pontual positivo, mas insuficiente para concluir tendência sem série de dias consecutivos.