<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Dado que a tese L01 aponta dois estoques em risco operacional imediato com perfis de recuperação distintos:** o anúncio Clássico em Cross-Docking de canecas 250ml (available_quantity=1, 3 pedidos hoje) está em ruptura certa no próximo ciclo — Yasmin verifica reposição e decide entre envio emergencial à expedição ou cancelamento controlado antes da pausa automática do ML. Em paralelo, o anúncio Catálogo (is_catalog=true, gold_pro, Full) de canecas lisas 200ml tem cobertura estimada de ~2,8 dias ao ritmo de hoje — Yasmin verifica reposição em trânsito ao CD do ML. Ambas as ações têm urgência operacional, mas critérios diferentes: Cross-Docking é Budamix quem controla; Full depende do CD do ML para reestocagem, e perda de Buy Box em Catálogo tem recuperação lenta.

- **Dado que o risco estrutural da L01 é ADS compensando déficit de orgânico dos campeões em Padrão inferior (4º ciclo consecutivo), e que ROAS está em 11,36x com ACOS em 4,19%:** a decisão correta não é acionar Himmel — campanha eficiente em curso é para observar, não para ajustar. A decisão é registrar o share de hoje (71,2%) como segundo ponto relevante da série pós-22/05, observando se o ciclo de 25/05 confirma segundo consecutivo acima de 65%.

- **Dado que o Kit 6 Canecas Porcelana Tulipa (registrado com 2 unidades no ciclo de 23/05, ritmo de 6-9 pedidos/dia) está ausente do top_items_details de hoje e a conta registrou 2 cancelamentos em metrics.cancelamentos:** a hipótese de ruptura ou pausa automática precisa ser verificada — se confirmada, os cancelamentos prospectivos associados entram na janela rolling de 60d do Platinum (gap R$48.941, ETA 11,9 dias) e impactam cancellations_rate.

- **Dado que a tese L01 classifica o patamar como confirmado em ≥2 janelas mas unidimensional (ticket, não volume):** não testar segundo vetor de anúncio nem escalar qualquer mudança estrutural agora — o patamar precisa de observação e os três pontos acima são ação suficiente para o horizonte de hoje.

---

### O que fazer hoje

**1. Yasmin:** verificar status e estoque do anúncio de canecas 250ml Cross-Docking (available_quantity=1 no snapshot, 3 pedidos gerados hoje) e do Kit 6 Canecas Porcelana Tulipa (ausente do top_items_details hoje, registrado com 2 unidades em 23/05 a um ritmo de 6-9 pedidos/dia) — motivo: ruptura iminente em ambos; ML pode pausar automaticamente e gerar cancelamentos prospectivos que impactam cancellations_rate e entram direto na janela rolling Platinum (gap R$48.941, ETA ~11,9 dias); os 2 cancelamentos de hoje (metrics.cancelamentos) podem ser originários do anúncio de Tulipa — sinal de resultado: reposição viabilizada para o Cross-Docking em 24h neutraliza o risco; ausência de reposição com anúncio pausado confirma ruptura ativa e deve ser registrada como variável confundidora para as próximas leituras de cancellations_rate e de GMV do cluster de canecas.

**2. Yasmin:** verificar reposição em trânsito ao CD do ML para o Kit 6 Canecas Lisas 200ml (Catálogo, gold_pro, Full, available_quantity=25, ~9 pedidos/dia → cobertura estimada de ~2,8 dias) — motivo: anúncio is_catalog=true; perda de Buy Box em Catálogo demora a se recuperar mesmo após reestocagem; é o único anúncio gold_pro ativo da conta (listing_type_mix: gold_pro=7,5%) e contribui com ticket elevado numa conta onde todo o ganho de patamar está no ticket médio — sinal de resultado: reposição confirmada com chegada dentro de 48h neutraliza o risco; ausência de reposição em trânsito eleva a urgência para Yasmin acionar protocolo de manutenção junto ao ML e comunicar Kobe sobre impacto prospectivo na trajetória Platinum.

**3. Yasmin:** registrar ADS share de hoje (71,2%), health dos dois campeões em Full — Conjunto 5 Potes de Vidro (health=0,71, 4º ciclo) e Kit 4 Potes 1050ml (health=0,75, 4º ciclo) — e ADS share do ciclo de 25/05 quando disponível, como série de observação estruturada — motivo: L01 identificou dependência de ADS sobre orgânico deprimido como risco estrutural; share voltou a 71,2% após recuo de 23/05 (49,5%), mas a série ainda é irregular; o health é o indicador mais estável e determina quando o gatilho de Himmel e Kobe é acionado — sinal de resultado: share abaixo de 65% em 25/05 enfraquece hipótese de dependência estrutural; share acima de 65% em 25/05 com health estagnado em ambos os campeões aciona alinhamento de Yasmin com Himmel sobre cobertura preventiva; health ≥ 0,85 em qualquer dos dois campeões reverte o risco estrutural identificado pela L01.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel para ajustar as campanhas de ADS ML:** ROAS em 11,36x e ACOS em 4,19% colocam a campanha em zona de alta eficiência — regra da Lente 5 é clara: ADS share acima de 50% com ROAS alto e ACOS baixo é para observar, não para mexer. A dependência estrutural identificada pela L01 é problema de orgânico deprimido, não de ineficiência de campanha; ajustar ADS agora retiraria o único amortecedor de exposição dos campeões em Padrão inferior sem resolver o health, e introduziria variável que impede separar comportamento orgânico de efeito de mídia na série de leitura em andamento.

2. **Não tomar ação sobre o health dos dois campeões em Full (Conjunto 5 Potes de Vidro e Kit 4 Potes 1050ml):** quatro ciclos estagnados em Padrão inferior são preocupantes, mas health estagnado ≠ health caindo — a direção do quinto ciclo é o dado que desbloqueia a decisão. Sem breakdown de ADS por platform_item_id (dado pendente desde 22/05), não é possível confirmar se os anúncios estão ganhando ou perdendo exposição líquida. Pausa, redistribuição de verba ou qualquer intervenção nesses anúncios sem esse dado pode deteriorar ranking sem diagnóstico suficiente.

3. **Não abrir discussão estrutural com Kobe sobre dependência de ADS hoje:** o gatilho exige share acima de 65% por dois ciclos consecutivos sem melhora de health. O ciclo de 23/05 ficou em 49,5% (abaixo do threshold), quebrando a sequência. O ciclo de 24/05 com 71,2% é o primeiro ciclo acima de 65% na série recomeçada — o segundo consecutivo só se confirma em 25/05. Abrir essa discussão antes da confirmação seria precipitado e dilui a credibilidade do sinal quando ele se confirmar de fato.

---

### Escalonamento

**observar**

A tese estrutural da L01 está consolidada (vulnerável, ADS cobrindo déficit orgânico dos campeões em Padrão inferior pelo quarto ciclo), mas os gatilhos de escalonamento ainda não foram atingidos. Os dois riscos operacionais imediatos — ruptura do anúncio Cross-Docking de canecas 250ml e cobertura crítica do anúncio Catálogo de canecas lisas 200ml — estão dentro do alcance operacional direto da Yasmin, sem necessidade de acionar Himmel ou Kobe. Gatilhos que mudam essa classificação: se o ADS share ficar acima de 65% em 25/05 (segundo ciclo consecutivo com health estagnado nos campeões), Yasmin alinha com Himmel sobre cobertura preventiva → classificação muda para **alinhar com Himmel**. Se esse alinhamento não produzir melhora de health nos campeões em mais 3 ciclos, ou se a perda de Buy Box no anúncio Catálogo de canecas se confirmar sem solução de reposição, Yasmin abre com Kobe a discussão sobre dependência estrutural da conta em mídia paga → classificação muda para **escalar para Kobe**.