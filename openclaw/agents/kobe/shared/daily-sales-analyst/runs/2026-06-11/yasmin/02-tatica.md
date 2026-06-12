<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a tese da L01 identifica dependência crônica de MLB3288536143 com formação de segundo vetor sistematicamente abortada por rupturas recorrentes nos adjacentes:** a ação de maior impacto hoje não está no líder (estoque em 1.523 unidades, risco imediato ausente) — está em proteger as duas posições em ruptura iminente que compõem ou abortam esse segundo vetor: MLB6232315532 (único Catálogo `is_catalog=true` do topo, `available_quantity=4`) e MLB6167272090 (Tulipa Full, `available_quantity=5`, 12 pedidos hoje). Ruptura simultânea dessas duas posições aprofunda exatamente o risco principal diagnosticado pela L01.

- **Dado que o único Catálogo no topo (MLB6232315532, gold_pro) está com `available_quantity=4` e 5 pedidos hoje (runway < 1 dia):** ruptura em Catálogo é operacionalmente mais grave que ruptura em Clássico — perda de Buy Box exige restock físico no CD do ML antes de recuperar posição, ciclo de recuperação mais lento. Esta é a ação de prioridade máxima do dia, independente do vetor ADS.

- **Dado que o dado de Mercado Ads é inválido (`spend_yesterday_brl=0,0` com `campaigns_active_count=13`, contradizendo 13 ciclos de memória com gasto entre R$262 e R$422):** nenhuma decisão sobre campanha pode ser tomada neste ciclo. Himmel não deve ser acionado com base em zero-spend que é provável lag de API. A tese de ADS share descendente (série 69,9%→44,3% desde 22/05) fica suspensa até dado válido.

- **Dado que a compressão de ticket (-17,7% vs 30d, de R$47,97 para R$39,48) é efeito de composição do cluster IMB501 (`top3_concentration=63,2%`) documentado em múltiplos ciclos:** não há sinal de deterioração de preço ou competitividade — é mecânica de mix. Sem dado válido de ADS share, não é possível separar efeito de composição de efeito de campanha. Nenhuma ação sobre ticket ou precificação.

---

### O que fazer hoje

1. **Yasmin:** verificar ETA de reposição no CD do ML para o Catálogo Canecas Lisas 200ml (MLB6232315532, `is_catalog=true`, gold_pro, Full, `available_quantity=4`, 5 pedidos hoje, runway < 1 dia) — motivo: é o único anúncio em Catálogo no topo da conta; quando pausar por estoque a posição de Buy Box vai para concorrente e a recuperação depende de restock físico no CD do ML antes de reativar ranking — ciclo de recuperação mais lento que Clássico; padrão de depleção confirmado pela memória (10/06: 5 un → hoje: 4 un, sem reposição em dois ciclos) — sinal de resultado: ETA de restock confirmado no CD em < 24h neutraliza o risco; `status=paused` antes da reposição registra ruptura de Buy Box em Catálogo e inicia protocolo de reativação.

2. **Yasmin:** confirmar `available_quantity` e `status` do Kit 6 Canecas Tulipa 250ml (MLB6167272090, Full, `available_quantity=5`, 12 pedidos hoje, runway < 0,5 dia) no snapshot de amanhã — motivo: 8º+ ciclo de ruptura recorrente documentado desde 31/05; cada ciclo pausado gera pedidos prospectivamente canceláveis que, acumulados, pressionam `cancellations_rate` (hoje ainda em zero); a L01 identifica este item como parte do segundo vetor abortado — sinal de resultado: `available_quantity > 0` e `status=active` amanhã indica reposição parcial; `status=paused` confirma 9º+ ciclo e classifica como ausência de solução estrutural de reposição para este item, sinalizar para Yasmin escalar ETA junto à expedição.

3. **Yasmin:** verificar se entrada de estoque para o Kit 4 Potes 1050ml (MLB4073003575, Full, `health=0,75`, `available_quantity=19`, 7 pedidos hoje, runway ~2,7 dias) foi programada — motivo: terceiro ciclo de cobertura crítica sem resolução definitiva documentado pela L01 (28 un em 10/06 → 19 un hoje); item ainda não atingiu o limiar de ≤5 unidades, mas ao ritmo atual cruza a zona crítica em 2–3 dias sem restock — sinal de resultado: `available_quantity > 25` amanhã indica restock entrou; `available_quantity < 12` indica aceleração sem restock e eleva para ação imediata de cobertura.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel sobre ADS:** `spend_yesterday_brl=0,0` com `campaigns_active_count=13` contradiz 13 ciclos de memória com gasto real — é lag de API, não realidade operacional. Acionar Himmel com base em zero-spend pode introduzir ajuste desnecessário num sistema que opera normalmente. A série de ADS share (69,9%→44,3% desde 22/05) fica suspensa até próximo ciclo com dado válido. Qualquer leitura de eficiência ou ineficiência de campanha hoje é impossível.

2. **Não agir sobre a queda de ticket (-17,7% vs 30d) via preço, campanha ou mix:** a compressão para R$39,48 é efeito direto de composição — cluster IMB501 com `top3_concentration=63,2%` carregando 117 dos 185 pedidos, mecânica documentada em múltiplos ciclos. Sem ADS share válido, não é possível separar efeito de composição de efeito de campanha. Agir sobre preço ou segmentação sem esse dado é precipitado e pode comprimir margem sem causa real.

3. **Não tratar `health=0,71` do anúncio líder (MLB3288536143) como gatilho de ação imediata junto a Himmel:** health estabilizado no 18º+ ciclo idêntico sem queda observável — o risco estrutural existe e está documentado pela L01, mas a postura correta é verificar direção interna (estável/caindo/subindo) antes de qualquer movimento. Escalar ou pausar sobre health cronicamente estagnado, sem evidência de deterioração ativa no ciclo atual, introduz variável num sistema que opera com esse nível há semanas sem ruptura.

---

### Escalonamento

**Observar — com gatilho explícito para acionamento de Kobe em 48h se ruptura de Catálogo não for revertida.**

A operação hoje não requer Himmel (dado ADS inválido em 100% do ciclo, suspende qualquer decisão de campanha) nem Kobe (sem decisão estrutural pendente). Yasmin resolve as três ações operacionais com autonomia. O único ponto de escalada latente é MLB6232315532: se o anúncio entrar em `status=paused` antes da reposição e o ETA de restock no CD do ML ultrapassar 72h, a decisão de priorizar alocação de estoque para este Catálogo (vs outros itens da expedição da Budamix) extrapola tática diária e deve ser aberta com Kobe. Quando dado de Mercado Ads retornar com `spend > 0` no próximo ciclo, Yasmin verifica ADS share: abaixo de 40% com GMV sustentado confirma hipótese de autonomia orgânica estrutural e abre discussão com Kobe sobre dependência de mídia paga; acima de 55% no retorno indica que o GMV de hoje foi operado sem ADS, exigindo leitura do impacto real da ausência antes de qualquer ajuste com Himmel.