<!-- llm_used=true model=gpt-5.5 fallback=false -->
### Qualidade da base

Base utilizável para tese estratégica: janelas 7d/30d/60d, mesmos dias da semana, memória weekly/monthly/rules e `ml_snapshot` vieram disponíveis. A ressalva é que o pacote está como `DADOS_PARCIAIS` e não traz posição de categoria nem share Buy Box; reputação, MercadoLíder, modalidade de envio e Mercado Ads estão disponíveis.

### Leitura temporal

- A conta não confirma ganho de patamar no curto prazo: `metrics.pedidos_validos=84` está abaixo de 7d (`changes.orders_vs_7d_pct=-25,9%`), 30d (`-15,4%`) e mesmos dias da semana (`-17,6%`). O GMV, porém, fica praticamente alinhado ao par de sexta (`changes.gmv_vs_same_weekday_pct=-2,1%`) e acima de 30d (`+3,4%`), sustentado por ticket maior (`ticket_vs_30d_pct=+22,3%`).
- Em 60d, a conta ainda opera acima do patamar bimestral de GMV (`changes.gmv_vs_60d_pct=+17,9%`), mas com menos pedidos (`orders_vs_60d_pct=-10,4%`). Isso indica mix de maior valor, não expansão clara de alcance.
- O comportamento recente é de acomodação após pico de 7d: GMV abaixo da média curta (`gmv_vs_7d_pct=-16,8%`) e volume abaixo em todas as janelas, sem ruptura negativa contra 30/60d.
- A hipótese anterior de dependência de ADS ganha força: o pacote atual mantém ADS share muito alto e health degradada nos mesmos campeões já citados na memória, mas ainda falta a série temporal de health para separar deterioração progressiva de fotografia repetida.

### Leitura estratégica

- Patamar: a conta está acima da banda de 30/60d em GMV, mas sem confirmação por volume nem por controle de sexta. O sinal mais defensável é acomodação com ticket elevado, não ganho estrutural.
- Exposição e reputação: `ml_snapshot.reputation.color=5_green`, `power_seller_status=gold`, `claims_rate=0,25%`, `cancellations_rate=0` e `delayed_handling_rate=0,12%` sustentam leitura operacional saudável. A queda de pedidos, portanto, não aponta para erosão de reputação; a hipótese mais forte é mix/demanda/ADS.
- Modalidade de envio: a operação usa exatamente duas modalidades de envio ativas, Full e Cross-Docking; Flex está em `0,0%`. No 30d, Full domina (`fulfillment_mix_30d.full_pct=73,7%`), mas os top 10 recentes vieram menos Full (`47,1%`) e mais Cross-Docking (`52,9%`). Isso reduz a leitura de dependência imediata de Full nos campeões, embora a janela 7d ainda seja muito concentrada em Full (`74,9%`).
- Mercado Ads é o principal vetor do resultado: `revenue_ads_yesterday_brl=3228,78` sobre `gmv=4622,03` dá ADS share de aproximadamente `69,9%`; com `spend_yesterday_brl=296,96`, o ROAS é `10,9x` e o ACOS `4,57%`. É mídia eficiente, mas já em zona de ADS dominante, reforçando vulnerabilidade estrutural se o orgânico não sustentar.

### Tese da conta

A conta está **vulnerável**: o patamar de GMV segue saudável contra 30/60d e a reputação permanece verde com MercadoLíder Gold, mas a estrutura depende demais de Mercado Ads e de poucos vetores de venda. A leitura temporal não sustenta queda real, porque GMV segue acima de 30/60d; também não sustenta ganho de patamar, porque pedidos caem contra 7d, 30d, 60d e sextas comparáveis.

### Risco estrutural principal

- **Risco:** dependência estrutural de Mercado Ads em anúncios campeões com health degradada.
- **Por que importa:** com ADS share em `69,9%`, a conta fica exposta a queda brusca se campanha, orçamento ou eficiência mudarem; como `MLB4073003575` tem `health=0,75` e `MLB3288536143` tem `health=0,71`, parte do tráfego pago pode estar compensando perda orgânica de listings penalizados.
- **Histórico:** não é novo; a memória já trazia gatilho ativo de ADS share ≥60% combinado com health abaixo de 0,80 nos mesmos anúncios.
- **Sinal de confirmação:** ADS share ≥60% por mais 2 ciclos, com `MLB4073003575` e `MLB3288536143` ainda abaixo de `health=0,80`, confirma que o faturamento está sendo sustentado por mídia sobre estrutura orgânica enfraquecida.

### Sinais a observar

- `gmv` abaixo de R$ 4.500 por 2 dias seguidos, com pedidos abaixo de 90, confirma reversão do patamar recente para baixo.
- ADS share ≥60% em mais 2 ciclos confirma Mercado Ads como vetor dominante, não apenas amplificador.
- `MLB6167272090` cair a `available_quantity=0` ou sair dos top 10 após estar com apenas 9 unidades confirma ruptura de campeão Full como causa provável de perda de volume.