<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que o risco operacional imediato da L01 é a ruptura iminente do Kit 6 Canecas Porcelana Tulipa 250ml (Full, `available_quantity=2`, 9 pedidos ontem):** a decisão é agir hoje — verificar estoque disponível no CD do ML e acionar reposição se ainda não houver envio em trânsito; se estoque já zerou ou anúncio pausou automaticamente, checar se pedidos foram gerados sem cobertura e avaliar cancelamento controlado antes que o ML cancele e impacte `reputation.cancellations_rate`, hoje em 0 mas vulnerável a qualquer cancelamento automático de múltiplos pedidos simultâneos.

- **Dado que a tese da L01 é "vulnerável" pelo terceiro ciclo consecutivo de `health < 0,85` nos dois campeões Full em Padrão inferior (MLB3288536143 `health=0,71`, MLB4073003575 `health=0,75`):** a decisão é observar com checagem dirigida — estabelecer se o health de hoje é estável, caindo ou em recuperação em relação ao ciclo anterior; somente direção descendente confirmada (especialmente MLB3288536143 atingindo `health ≤ 0,69`) justifica acionar Himmel sobre cobertura preventiva. Três pontos idênticos sem movimento não são aval para ação, são aval para medir a quarta leitura.

- **Dado que o ADS share caiu de ~70% (22/05) para 49,5% hoje com ROAS ~9x e ACOS 4,43% (`ads_summary`):** a decisão é não tocar. A queda de share é sinal de que o orgânico cresceu (de ~R$1.391 para ~R$2.586), não de que a campanha piorou. Campanha eficiente em conta sem `monthly.md` consolidado é série nova — qualquer ajuste destrói o ponto zero.

- **Dado que a tese da L01 identifica o patamar em ganho confirmado em ≥2 janelas (GMV +13,9% vs 30d, +27% vs 60d, +14,6% vs média dos sábados) sustentado por ticket em elevação bimestral:** a decisão é proteger o padrão sem forçar expansão — o volume de 91 pedidos está dentro da variância intrínseca de sábados (par forte/par fraco documentado na L01), não é sinal de fraqueza. Nenhuma ação de patamar hoje.

---

### O que fazer hoje

1. **Yasmin:** verificar o `available_quantity` e o `status` do Kit 6 Canecas Porcelana Tulipa 250ml em Full (hoje em 2 unidades, 9 pedidos gerados ontem) — risco operacional imediato: se pedidos ontem superaram o estoque disponível, há cancelamentos prospectivos em formação que vão impactar `reputation.cancellations_rate` (hoje em 0,0) e introduzir variável confundidora na leitura de ETA Platinum (gap de R$51.794, ritmo diário precisa se manter em ~R$4.070/dia) — sinal de resultado: se `available_quantity > 0` e anúncio ativo com reposição em trânsito = risco neutralizado, registrar data de reposição; se anúncio pausado ou estoque zerado com pedidos confirmados = registrar como ruptura ativa e avaliar cancelamento controlado antes de cancelamento automático ML.

2. **Yasmin:** checar a direção (estável / caindo / em recuperação) do `health` dos dois campeões em Full em Padrão inferior no pacote de hoje — o Conjunto 5 Potes (MLB3288536143, `health=0,71`, três ciclos consecutivos sem movimento) e o Kit 4 Potes 1050ml (MLB4073003575, `health=0,75`, idem) — motivo: três leituras idênticas não distinguem piso estabilizado de degradação lenta; a quarta leitura estabelece direção e define se a hipótese de erosão orgânica silenciosa que ADS compensa se confirma ou para — sinal de resultado: health estável ou acima de 0,71/0,75 = observar sem ação; health abaixo de 0,71 em MLB3288536143 ou abaixo de 0,72 em MLB4073003575 = alinhar com Himmel sobre cobertura ADS preventiva para os dois.

3. **Yasmin:** registrar o ADS share de hoje (49,5% = R$2.538,63 / R$5.124,32) e o orgânico implícito (~R$2.586) como segundo ponto da série pós-22/05 — motivo: a queda de ~70% para 49,5% é mudança relevante de comportamento, mas um único ciclo não distingue expansão orgânica real de variância de um dia; segundo ciclo abaixo de 55% consolida a hipótese de orgânico em crescimento; segundo ciclo acima de 65% reativa o gatilho de escalonamento a Kobe (três ciclos consecutivos ≥ 65%) — sinal de resultado: ADS share ≤ 55% no próximo pacote = hipótese de orgânico em expansão se fortalece; ADS share ≥ 65% = gatilho de Kobe volta a estar vivo e exige terceiro ponto para confirmar.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para ajuste de campanha.** ROAS ~9x e ACOS 4,43% (`ads_summary`) estão muito acima dos limiares de eficiência (ROAS > 5x, ACOS < 10%); a campanha está em fase de leitura com série curta e sem `monthly.md` consolidado. Qualquer ajuste de lance, segmentação ou verba destrói a linha de base e impede separar efeito de comportamento natural da conta. A queda do share de ~70% para 49,5% é o tipo de variação que se observa por 2-3 ciclos antes de qualquer decisão.

- **Não tratar os dois campeões Full em Padrão inferior como caso de ação imediata sobre os anúncios.** A L01 registra três ciclos consecutivos em `health=0,71`/`0,75` sem reversão — mas também sem aceleração confirmada. `available_quantity` dos dois está confortável (469 e 139 unidades), anúncios ativos, volume sustentado. Mexer em anúncio com health baixo mas estável (pausar, alterar preço, alterar título) sem saber se health está descendo ou estabilizando é o caso clássico de piorar o que está funcionando — a regra explícita da L01 é: sem direção definida, não age.

- **Não interpretar os 91 pedidos como queda de volume que exige ação.** O `orders_vs_7d_pct=-16,4%` é distorcido pelo spike atípico de 05-16 (184 pedidos, maior da série de 4 sábados); vs `same_weekday_avg` o dia está em +14,6% de GMV. A L01 registra que "leitura de 'queda recente' não é sustentada". Nenhuma ação de volume, patamar ou verba se justifica com base nessa métrica.

---

### Escalonamento

**observar**

O único risco que exige ação hoje é operacional e está no escopo direto da Yasmin (ruptura de Kit 6 Canecas Tulipa em Full). Os dois riscos estruturais da tese da L01 — health dos campeões e dependência de ADS — precisam de um ciclo adicional para estabelecer direção: o health dos campeões está em terceiro ponto idêntico (sem aceleração confirmada), e o ADS share tem apenas dois pontos na nova série (22/05 e 23/05). Himmel não é acionado enquanto ROAS ~9x e ACOS 4,43% se mantiverem, independentemente do share. Kobe só entra em dois cenários: (a) ADS share voltar a ≥ 65% no próximo ciclo e confirmar terceiro ciclo consecutivo acima desse patamar — gatilho de discussão sobre dependência estrutural de mídia paga; (b) health de MLB3288536143 cair para ≤ 0,69 (entrada em nível Básico) indicando aceleração da degradação de ranking orgânico — decisão sobre mix de anúncio ou reforço estrutural extrapola tática diária.