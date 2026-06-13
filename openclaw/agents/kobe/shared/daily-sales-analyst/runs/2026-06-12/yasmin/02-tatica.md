<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Decisão tática

- **Risco operacional iminente não resolvido (responde ao risco estrutural principal da L01):** A tese estratégica identifica `MLB6167272090` (Kit 6 Canecas Tulipa 250ml, `status=paused`, `available_quantity=0`) como o único vetor capaz de derrubar o MercadoLíder Platinum recém-conquistado via `cancellations_rate` sem sinalização antecipada no GMV. Com 5 pedidos gerados hoje nesse anúncio pausado — somados a 9+ ciclos documentados desde 31/05 (4, 11, 6, 12, 5 pedidos/dia) sem restock confirmado — a decisão é **agir hoje**: Yasmin apura causa da pausa persistente e ETA de restock, antes que a acumulação entre na janela oficial do ML.

- **Cobertura crítica em segundo vetor Full (responde ao sinal 2 da L01):** `MLB4073003575` (Kit 4 Potes 1050ml, `health=0,75`, `available_quantity=13`, `logistic_type=fulfillment`) está no 3º ciclo consecutivo de cobertura crítica (~1,9 dias ao ritmo de 7 pedidos/dia) sem restock confirmado na memória. A decisão é **checar cobertura hoje**: se `available_quantity` caiu abaixo de 6 ou status virou `paused`, é risco operacional iminente — adiciona cancelamentos prospectivos e retira velocidade de ranking de um segundo Full ativo no catálogo de categoria.

- **ADS eficiente em expansão orgânica — não acionar Himmel (responde à tese orgânica da L01):** A L01 documenta série ADS share descendente 69,9%→42,0% com GMV acima da média de 30d — hipótese de autonomia orgânica passando de candidata para tendência. Com `revenue_ads_yesterday_brl=R$2.688,95` / `gmv=R$6.397,92` (42,0%), ROAS 11,41x e ACOS 9,96%, a campanha é eficiente e o orgânico cresce mais rápido. A decisão é **não tocar em ADS**: qualquer ajuste interrompe a série de observação e impede isolar efeito de comportamento natural.

- **Health crônico de MLB3288536143 — observar sem ação forte (responde à Lente 4 da L01):** O campeão IMB501 (`health=0,71`, 18º+ ciclo idêntico, `is_catalog=false`) carrega 51,3% do top3 com risco de erosão lenta de ranking de categoria. Sem dados de direção (subindo/caindo/estável) confirmados no pacote e com `available_quantity=1.563` descartando ruptura, a decisão é **manter observação**: ação forte (alinhamento com Himmel sobre cobertura) só se justifica se health cruzar abaixo de 0,68 — gatilho definido em ciclos anteriores e ainda não atingido.

---

### O que fazer hoje

1. **Yasmin:** Apurar o que está impedindo o restock de `MLB6167272090` (Kit 6 Canecas Tulipa 250ml, `status=paused`, `available_quantity=0`) — 5 pedidos foram gerados hoje nesse anúncio pausado, configurando cancelamentos prospectivos garantidos; somados aos ciclos de 31/05, 05/06, 06/06 e 11/06 (volume acumulado estimado em 40–55 pedidos prospectivos na série), o acúmulo pode já estar dentro ou próximo da janela oficial ML (`transactions_completed=6.993`: cada ~35 cancelamentos move a taxa em ~0,5pp); com `cancellations_rate=0` ainda, há margem de ação antes de o Platinum ser comprometido — sinal de resultado: restock confirmado no CD do ML e status voltando a `active` no próximo snapshot neutraliza o vetor; anúncio seguindo `paused` com `available_quantity=0` confirma falha operacional não resolvida e Yasmin escala internamente para providenciar reposição de urgência.

2. **Yasmin:** Verificar `available_quantity` atual do Kit 4 Potes 1050ml (MLB4073003575, `available_quantity=13` no snapshot de hoje, `health=0,75`, 3º ciclo consecutivo em cobertura crítica) — ao ritmo de 7 pedidos/dia dos últimos dias, cobertura efetiva é ~1,9 dias; memória de 09/06 a 11/06 mostra que restock entrou de forma parcial e insuficiente entre ciclos — sinal de resultado: `available_quantity` > 20 e status `active` no próximo snapshot indica restock efetivo e risco neutralizado por 2–3 dias; `available_quantity` ≤ 6 ou status=`paused` aciona providência imediata de reposição ao CD do ML antes de cancelamento automático.

3. **Yasmin:** Registrar ADS share de hoje (42,0% = R$2.688,95 / R$6.397,92) e ACOS (9,96%) como ponto válido da série de observação — 11/06 teve lag de API e o ponto de hoje é o mais recente confirmado; dois ciclos consecutivos com share ≤ 45% e GMV ≥ R$6.000 confirmam a hipótese de autonomia orgânica estrutural da L01 e abrem discussão com Kobe sobre mix de campanha a médio prazo — sinal de resultado: se próximo ciclo com `ads_summary` válido retornar share entre 40–45% com denominador saudável, tendência se consolida; share acima de 55% em dia de GMV normal indicaria reversão pontual ou ajuste de campanha por Himmel não comunicado.

---

### O que NÃO fazer ainda

- **Não acionar Himmel sobre ADS ML:** ROAS 11,41x e ACOS 9,96% são parâmetros de campanha eficiente; ADS share em 42% com orgânico crescendo mais rápido que spend é exatamente o cenário onde mexer introduz variável e impede isolar o comportamento natural. A série de 10+ ciclos documentada na memória é insumo analítico — não gatilho de intervenção. O gatilho de alinhamento com Himmel definido em ciclos anteriores (ACOS > 30% ou share > 60% por dois ciclos) está distante.

- **Não tomar ação forte sobre o health crônico de MLB3288536143 (health=0,71, 18º+ ciclo):** Estagnação em nível regular há 18+ ciclos não é queda — é ausência de melhora. Sem dados de direção confirmados no pacote e com estoque de 1.563 unidades descartando ruptura a curto prazo, qualquer cobertura preventiva de ADS nesse anúncio via Himmel seria precipitada. O gatilho permanece sendo health cruzar abaixo de 0,68 em dois ciclos consecutivos — evento que não ocorreu.

- **Não abrir discussão estrutural sobre concentração de mix com Kobe:** Top3 em 51,3% (IMB501 cluster) é padrão documentado há 14+ ciclos sem deterioração de GMV — não é evento novo nem emergência. A decisão de diversificação de catálogo é estrutural e pertence ao Trader/Kobe, mas não tem urgência tática nos próximos 5–7 dias enquanto os dois riscos operacionais imediatos (Tulipa parada e cobertura do Kit 4 Potes 1050ml) não forem resolvidos. Abrir essa pauta agora dispersa atenção do que é urgente.

---

### Escalonamento

**observar** — com ação operacional imediata de Yasmin nos dois riscos de ruptura (Tulipa e Kit 4 Potes 1050ml), sem acionamento de Himmel ou Kobe hoje.

A conta não apresenta condição para escalonamento de ADS (campanha eficiente, orgânico expandindo, ACOS dentro do envelope) nem para escalonamento estrutural (Platinum mantido, GMV acima da média de 30d e mesmos dias da semana). O que exige ação é operacional — restock de dois anúncios Full — e está dentro da alçada de Yasmin. O acionamento de Himmel só se justifica se, após resolução dos dois riscos operacionais, ADS share cruzar abaixo de 40% por dois ciclos com GMV saudável (abertura de escalada de campanha num canal com orgânico sólido) ou se health de MLB3288536143 cair abaixo de 0,68 (cobertura preventiva de ranking). O acionamento de Kobe se justifica se `cancellations_rate` sair de zero no próximo snapshot — não como problema de ADS, mas como risco direto de perda de Platinum, que é decisão estrutural de canal.