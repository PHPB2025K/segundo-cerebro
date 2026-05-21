<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Dado que a tese da L01 é "Vulnerável" com risco estrutural de dependência de ADS compensando health degradada nos campeões:** a decisão tática correta é proteger os dois ativos que sustentam o GMV corrente — o campeão de catálogo com `health=0,71` (`MLB3288536143`) e o item com estoque crítico de 3 unidades (`MLB4410218897`) — antes de qualquer outra ação. A eficiência de ADS não neutraliza esses riscos; os amplifica (quanto mais verba cobrindo anúncios frágeis, maior o impacto de uma ruptura ou queda de posição não detectada a tempo).

- **Dado que ADS representa 59,8% do GMV com ROAS 11,6x e ACOS 4,64% (`ml_snapshot.ads_summary`) e esta é a primeira leitura documentada sem memória semanal/mensal:** a decisão é explicitamente **não acionar Himmel**. A campanha está em fase de leitura inaugural com performance acima de qualquer limiar de intervenção. Mexer agora introduz variável que impede separar comportamento natural de efeito de ajuste.

- **Dado que a queda de -4,3% em GMV vs 7d e -20,9% em pedidos vs 7d pode parecer sinal de alerta:** o controle correto é o mesmo dia da semana — ontem ficou +32,4% em GMV e -1,6% em pedidos vs média das últimas 4 quartas (`changes.orders_vs_same_weekday_pct`, `changes.gmv_vs_same_weekday_pct`). A leitura de patamar da L01 está confirmada para a janela temporal correta; a variação vs 7d reflete janela inflada por dias fortes recentes, não deterioração.

- **Dado que `Conjunto 5 Potes Tampa Vermelha` (`MLB3288536143`) opera como `is_catalog=true` com `health=0,71`:** este é o anúncio de maior risco estrutural entre os campeões — perda de posição em catálogo demora a recuperar e ocorre silenciosamente. Proteger agora é mais barato que recuperar posição depois.

---

### O que fazer hoje

1. **Yasmin:** verificar `available_quantity` do campeão de cauda curta em Full com 3 unidades restantes e giro de 3 pedidos/dia (`ml_snapshot.top_items_details` — item com `available_quantity=3`, `logistic_type=fulfillment`) e confirmar se há reposição de estoque programada ou pendente para o CD do ML — motivo: dado que o sinal de ruptura iminente foi identificado pela L01 como risco operacional imediato, se o anúncio sair do ar por esgotamento com pedidos abertos, cada cancelamento gerado impacta `reputation.cancellations_rate` (hoje em zero, `ml_snapshot.reputation.cancellations_rate=0`) e queima a vantagem reputacional estrutural da conta — sinal de resultado: reposição confirmada com prazo ≤ 48h neutraliza o risco; ausência de reposição exige decisão de Yasmin entre suspensão preventiva do anúncio (evita cancelamentos) ou aceitação do risco de ruptura com log para análise futura.

2. **Yasmin:** verificar direção do `health` do anúncio de catálogo `Conjunto 5 Potes Tampa Vermelha` (`is_catalog=true`, `health=0,71`, `MLB3288536143`) — confirmar se health está caindo, estável ou em recuperação nos últimos 3 dias acessando o histórico interno de saúde do anúncio (via Seller Central ML ou ferramenta de monitoramento da conta) — motivo: dado que a L01 identificou `health=0,71` abaixo do limiar de penalização de 0,85 em anúncio de catálogo, perda de posição em Buy Box de catálogo ML não é linear e demora a recuperar; a direção do health hoje define se o risco é iminente (caindo) ou contido (estável/subindo) — sinal de resultado: health estável ou em recuperação = manter observação sem ação adicional; health caindo por mais 1 dia = Yasmin investiga causa raiz antes de próximo ciclo (conteúdo, preço relativo, avaliações) e avalia com Himmel se cobertura de ADS sobre esse item precisa ser reforçada preventivamente.

3. **Yasmin:** registrar `ticket_medio=R$55,91`, `gmv=R$5.087,71`, `ads_spend=R$262,19`, `ads_revenue=R$3.041,56`, `acos=4,64%` e `ads_share≈59,8%` como ponto zero da série de observação de ADS vs orgânico — motivo: dado que esta é a primeira leitura documentada sem memória semanal/mensal (`weekly.md` e `monthly.md` em estado de template, conforme L01), sem esse registro não há linha de base para comparar nos próximos dias e qualquer decisão sobre ADS permanece sem fundamento histórico — sinal de resultado: se nos próximos 3 dias o `ads_share` ficar acima de 55% com ROAS sustentado acima de 5x, a série começa a confirmar a hipótese de dependência estrutural da L01; se ACOS subir para acima de 15% em qualquer dos próximos 3 dias, Yasmin alinha com Himmel sobre revisão de segmentação.

---

### O que NÃO fazer ainda

1. **Não acionar Himmel para ajustar verba, segmentação ou campanhas hoje.** ROAS 11,6x e ACOS 4,64% (`ml_snapshot.ads_summary`) estão em patamar de alta eficiência — muito abaixo do limiar de intervenção (ROAS < 3x ou ACOS > 30%). Esta é a leitura zero sem histórico comparável; qualquer ajuste de campanha agora elimina a possibilidade de isolar comportamento natural da conta nas próximas janelas. Precipitado porque: a hipótese de dependência estrutural precisa de 3-5 dias de observação de série antes de merecer decisão de verba.

2. **Não tratar a queda de pedidos vs 7d (-20,9%) como sinal de deterioração de patamar.** A janela de 7d é a mais elevada de todas as referências históricas disponíveis (`avg_orders_7d=115,1` vs `avg_30d=99,9` e `avg_60d=91,2`). O controle correto — mesmo dia da semana — mostra -1,6% em pedidos e +32,4% em GMV. Agir sobre a variação vs 7d seria responder a uma ilusão estatística gerada por dias recentes acima da média, não por deterioração real.

3. **Não iniciar checagem detalhada ou ação sobre os demais anúncios em Full com `health` abaixo de limiar sem antes saber a direção do health do campeão de catálogo.** A L01 identificou `7 anúncios com low_health` e `64 sem dado de health` (`account_overview.active_analysis`). Varrer todos agora sem prioridade definida dilui o foco de Yasmin e pode gerar ações desconexas. A ação correta é sequencial: proteger o campeão de catálogo (prioridade 2 acima) antes de expandir o escopo de checagem para os demais. Precipitado porque: a evidência atual não indica risco iminente nos itens além dos dois identificados pela L01 — expandir o escopo sem confirmação é resposta a hipótese, não a fato.

---

### Escalonamento

**observar**

A conta está em ganho de patamar confirmado nas janelas longas, com reputação intacta e ADS eficiente. Os dois riscos identificados pela L01 — health degradada nos campeões e ruptura iminente de estoque — são verificáveis por Yasmin diretamente sem necessidade de acionamento de Himmel ou Kobe. A decisão de não mexer em ADS é fundamentada e não exige alinhamento externo. Yasmin resolve os itens 1 e 2 de "O que fazer hoje" autonomamente.

O escalonamento muda em dois cenários: (a) se `health` do anúncio de catálogo (`MLB3288536143`) continuar caindo por mais 1 dia após a checagem de hoje, Yasmin alinha com Himmel sobre reforço de cobertura de ADS preventivo para esse item específico; (b) se `ads_share` ficar acima de 55% por 3 dias consecutivos com ROAS mantendo acima de 5x, Yasmin abre discussão com Kobe sobre dependência estrutural de mídia paga — essa decisão extrapola tática diária e envolve redirecionamento de verba ou diversificação de catálogo.