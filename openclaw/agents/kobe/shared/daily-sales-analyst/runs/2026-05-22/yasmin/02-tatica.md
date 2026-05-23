<!-- llm_used=true model=gpt-5.5 fallback=false -->
### Decisão tática

- Dado que a L01 define a conta como **vulnerável por dependência estrutural de Mercado Ads**, a decisão é **não mexer em ADS hoje**: `ads_summary.revenue_ads_yesterday_brl=3228,78` sobre `recipient.totals.gmv=4622,03` dá share ~69,9%, mas com ROAS ~10,9x e `avg_acos_pct=4,57`, a campanha está eficiente e qualquer ajuste agora confundiria a leitura.
- Dado que o risco principal da L01 combina ADS dominante com campeões abaixo de `health=0,80`, a decisão é **checar direção do health antes de agir**: os dois campeões citados seguem em `health=0,75` e `0,71`, mas falta série temporal para saber se a penalização está piorando, estabilizada ou recuperando.
- Dado que a L01 lê acomodação com ticket elevado, não queda real, a decisão é **proteger operação e evidência, não forçar alavanca comercial**: pedidos caem contra 7d/30d/60d, mas `gmv` segue acima de 30d e 60d, então a ação correta é reduzir incerteza por 2 ciclos.
- Dado que a L01 aponta possível ruptura de campeão Full como sinal a observar, a decisão é **proteger cobertura dos itens Full de giro**: o anúncio de canecas em Full está com `available_quantity=9`, ainda não crítico pelo limiar duro, mas perto o suficiente para distorcer leitura de volume se romper.

### O que fazer hoje

- **Yasmin:** checar direção do `health` dos dois campeões penalizados em Full/Catálogo e Full/Clássico — motivo: a L01 marca dependência de ADS sobre anúncios com `health=0,75` e `0,71`, mas sem série temporal a decisão sobre cobertura ADS seria prematura — sinal de resultado: health estável ou recuperando mantém observação; health caindo nos dois por mais 1-2 ciclos justifica alinhamento com Himmel sobre cobertura preventiva, sem mexer antes.
- **Yasmin:** registrar como ponto zero do ciclo o ADS share ~69,9%, ROAS ~10,9x e ACOS `4,57%` — motivo: a L01 trata Mercado Ads como vetor dominante, mas eficiente; a tarefa hoje é separar dependência estrutural de campanha saudável em fase de leitura — sinal de resultado: se o share seguir ≥60% com ROAS alto por 2 ciclos, vira pauta de alinhamento; se cair sem perda de GMV, a dependência enfraquece.
- **Yasmin:** verificar cobertura/reposição do campeão em Full com `available_quantity=9` — motivo: a L01 cita ruptura desse item como possível causa de perda de volume, e a memória já pede confirmação da reposição — sinal de resultado: se houver reposição antes de zerar, a variável operacional sai da leitura; se romper ou sair dos top 10, registrar como confundidor da leitura de pedidos dos próximos dias.

### O que NÃO fazer ainda

- Não pedir ajuste, pausa ou redistribuição de Mercado Ads hoje: apesar do ADS share alto, `avg_acos_pct=4,57` e ROAS ~10,9x indicam eficiência; mexer agora pode quebrar uma campanha que sustenta GMV sem provar que ela está causando o problema.
- Não interpretar a queda de pedidos como queda real de patamar: a L01 mostra `orders_vs_7d_pct=-25,9%` e `orders_vs_30d_pct=-15,4%`, mas `gmv_vs_30d_pct=+3,4%` e `gmv_vs_60d_pct=+17,9%`; ainda é acomodação com ticket maior, não reversão confirmada.
- Não propor migração de modalidade de envio ou mudança estrutural de catálogo: o mix recente dos top 10 mudou para mais Cross-Docking, mas `fulfillment_mix_7d.full_pct=74,9%` e `fulfillment_mix_30d.full_pct=73,7%` ainda mostram predominância de Full; qualquer decisão de migração extrapola a tática diária.

### Escalonamento

**observar** — Yasmin resolve o ciclo de hoje com checagens dirigidas, sem acionar Himmel ou Kobe. A mudança de classificação acontece se ADS share ficar ≥60% por mais 2 ciclos com os dois campeões ainda abaixo de `health=0,80`; nesse caso, Yasmin alinha com Himmel sobre cobertura e intenção da estratégia de mídia. Se o padrão persistir com risco estrutural de dependência mesmo com ROAS alto, aí a discussão passa para Kobe.