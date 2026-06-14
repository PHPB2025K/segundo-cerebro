<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Pacote robusto: memória diária contínua desde 22/05 (14+ entradas), weekly.md com blocos acumulados, monthly.md estruturado, rules.md preenchido. `ml_snapshot` completo — `reputation`, `fulfillment_mix` (7d, 30d, top10), `top_items_details`, `ads_summary` e `account_overview` todos com `status: ok`. Base sustenta tese com confiança alta; única ressalva persistente é ausência de breakdown ADS por `platform_item_id` (22º+ ciclo de pendência), que mantém indecidível a atribuição de receita ADS a anúncios individuais.

---

### Leitura temporal

- **60d vs 30d — compressão recente sobre patamar expandido:** O GMV de ontem (R$ 5.421, `changes.gmv_vs_60d_pct=+4,0%`) está dentro da banda bimestral, mas -19,1% abaixo do avg_30d (R$ 6.705, `changes.gmv_vs_30d_pct`). Não é contradição — é a leitura de uma conta que subiu de patamar entre abril e final de maio (picos de R$ 8k–R$ 10k no início de junho, consolidação do Platinum) e agora comprime em direção ao avg_60d. O patamar bimestral não foi rompido; o que foi rompido é a banda mais recente dos últimos 30 dias.

- **Mesmo dia da semana — sábado fraco dentro do range histórico:** A série dos últimos 4 sábados (R$ 7.065 → R$ 5.124 → R$ 5.623 → R$ 6.542) tem volatilidade intrínseca alta. Ontem (R$ 5.421, 117 pedidos vs `same_weekday_avg.avg_gmv=6.088,61`) está -11,0% abaixo da média, mas bem acima do piso (16/05: R$ 5.124, 91 pedidos). O sábado 06/06 foi atipicamente forte (161 pedidos), o que inflaciona a percepção de queda vs semana imediatamente anterior. Ajustado pela série completa dos 4 sábados, o dia é fraco sem ser anômalo.

- **7d vs 30d — desaceleração pós-pico:** O avg_7d (R$ 7.089, 162,1 pedidos) está consistentemente acima do avg_30d (R$ 6.705, 141,1 pedidos), o que confirma que a semana recente foi forte. Ontem ficou -23,5% abaixo do avg_7d (`changes.gmv_vs_7d_pct`). Com um único ponto abaixo da média semanal, a leitura é inconclusiva sobre reversão estrutural — pode ser ruído de sábado pós-semana forte.

- **Hipóteses anteriores — atualizações:** (a) Platinum manutenção: **confirmada e confortável** — `sales_60d_revenue_brl=R$ 323.667` vs threshold R$ 296.000, buffer R$ 27.667, `ritmo_diario_brl=R$ 5.394/dia` acima do mínimo de sustentação (~R$ 4.933/dia); (b) autonomia orgânica (série ADS share descendente 69,9%→42%): **enfraquecida** — ADS share ontem foi 62,3% (R$ 3.376/R$ 5.421), revertendo após os pontos de 09/06 (44,3%) e 12/06 (42,0%); a série não é monotônica e oscila com o volume do denominador, padrão já observado em 10/06 (59,7% em R$ 8.064); (c) Kit 4 Potes 1050ml em cobertura crítica: **confirmada e persistente** — `available_quantity=11` após 5 pedidos, sem restock efetivo por 3+ ciclos.

---

### Leitura estratégica

- **A compressão de ontem é acomodação dentro do patamar bimestral, não mudança de tendência.** O bimestre (+4,0% GMV vs 60d) confirma que a conta subiu de nível entre abril e maio. Junho mostra os picos iniciais se normalizando em direção ao avg_60d. A conta não está revertendo — está assentando. O dia de ontem, situado entre o piso (05-23: R$ 5.124) e a mediana (05-30: R$ 5.623) dos sábados históricos, é consistente com esse assentamento.

- **A dependência estrutural do IMB501 (MLB3288536143, `health=0,71`, nível regular, 18º+ ciclo idêntico) é o risco mais silencioso e mais persistente da conta.** O cluster carregou 51,3% do top3 ontem (Tampa Preta 37 + Tampa Cinza 13 pedidos), com estoque confortável (1.570 un, `available_quantity`) — sem ruptura imediata. Mas `is_catalog=false` em nível regular significa que o ML comprime progressivamente o ranking de categoria desse listing. A conta não percebe evento; percebe erosão gradual de posição. Com `top3_concentration=51,3%` por múltiplos ciclos sem segundo vetor emergindo, a base de substituição não existe em escala equivalente.

- **Dois anúncios Full em cobertura crítica simultânea configuram a cadeia operacional de maior risco imediato.** Kit 3 Potes (MLB4076957145, Full): `available_quantity=4` após 5 pedidos ontem — runway abaixo de 1 dia ao ritmo do sábado; ruptura iminente sem restock ou pausa intencional. Kit 4 Potes 1050ml (MLB4073003575, Full, `health=0,75`, nível regular): `available_quantity=11` após 5 pedidos — runway ~2,2 dias, terceiro ciclo sem restock efetivo documentado na memória (02/06, 09/06, 11/06, 12/06, hoje). Qualquer pausa automática em Full gera cancelamentos prospectivos que começam a pressionar `cancellations_rate` — hoje em zero, mas sem margem para absorver série.

- **ADS share de 62,3% em dia de GMV comprimido (R$ 5.421), com ROAS 14,34x e ACOS 4,41%:** campanha eficiente por Himmel, mas o padrão confirma correlação observada desde 10/06 — quando o orgânico comprime (denominador baixo, sábado, líder com health degradada), o ADS share sobe. A hipótese de autonomia orgânica do canal, formulada a partir dos pontos abaixo de 45% em 09/06 e 12/06, não pode ser validada em dias de volume comprimido. O canal depende do ADS para sustentar o piso em dias fracos — estruturalmente frágil se campanhas pausarem.

---

### Tese da conta

**Vulnerável.** Os indicadores macro estão saudáveis: Platinum confirmado e mantido com folga (buffer R$ 27.667), reputação `5_green`, ROAS de campanha excelente. Mas a estrutura subjacente opera sobre três fragilidades simultâneas: (1) IMB501 carregando ~51% do top3 com `health=0,71` há 18+ ciclos sem recuperação — erosão orgânica em andamento sem data de evento; (2) dois anúncios Full em cobertura crítica (Kit 3 Potes <1 dia de runway, Kit 4 Potes 1050ml ~2,2 dias) convivendo com `cancellations_rate=0` que ainda não absorveu os ciclos de ruptura recentes — qualquer cancelamento automático comprime diretamente a margem Platinum; (3) ADS share oscilando entre 42% e 62% sem convergência para autonomia orgânica, indicando dependência de campanha quando o orgânico comprime. O dia de ontem está dentro da banda bimestral, mas a acomodação de junho com dois vetores Full em runway curto e líder com health degradada define uma conta saudável no número e frágil na estrutura.

---

### Risco estrutural principal

**Risco:** Degradação persistente do nível de qualidade do anúncio do IMB501 (MLB3288536143, `health=0,71`, nível regular) no 18º+ ciclo consecutivo sem recuperação, em listing que carrega ~35–51% do volume diário.

**Por que importa:** Anúncio `is_catalog=false` em nível regular perde ranking de categoria progressivamente no ML. A erosão é silenciosa — a conta não percebe evento, percebe volume declinando gradualmente no líder, inicialmente confundível com sazonalidade ou dia fraco. Quando cruzar para nível preocupante (<0,70) ou perder posição no Mais Vendido da categoria, a recuperação é lenta (depende de histórico de engajamento, reviews e satisfação acumulados). Não há segundo vetor de escala equivalente na cauda — `top3_concentration` histórico de 51–63% confirma a ausência de substituto estrutural.

**Histórico:** Risco presente em todos os 14+ ciclos disponíveis na memória desde 22/05. Nunca saiu de nível regular. É o risco mais recorrente e persistentemente não-resolvido da série.

**Sinal de confirmação:** `health` do MLB3288536143 cair abaixo de 0,68 em dois ciclos consecutivos (`top_items_details[].health`) — gatilho já documentado na memória para alinhamento com Himmel. Alternativamente, pedidos do cluster IMB501 recuarem para menos de 40/dia por 3 dias úteis consecutivos sem redução proporcional equivalente no restante da conta.

---

### Sinais a observar

1. **Kit 3 Potes (MLB4076957145, Full): `available_quantity ≤ 0` e/ou `status=paused` no snapshot de amanhã** — confirma ruptura em anúncio Full com runway abaixo de 1 dia; os pedidos subsequentes viram cancelamentos automáticos que começam a pressionar `cancellations_rate` (hoje em zero, sem margem de absorção no contexto de Platinum). Observação: próximo ciclo imediato.

2. **ADS share em dias de GMV ≥ R$ 6.000 nos próximos 3 dias úteis:** se ADS share permanecer acima de 55% em dois dias com GMV ≥ R$ 6.000, a hipótese de autonomia orgânica fica refutada e a dependência de campanha volta a ser o framework principal; se dois dos três dias ficarem abaixo de 45% com GMV ≥ R$ 6.000, a hipótese se consolida. Leitura em dia de denominador comprimido (como ontem) não é válida para distinguir as hipóteses — o controle de volume do dia é obrigatório.

3. **Buffer Platinum nos próximos 7 dias:** se o GMV diário médio da semana ficar abaixo de R$ 4.933/dia (mínimo de manutenção do threshold R$ 296k na janela 60d rolling), o buffer atual de R$ 27.667 começa a erodir; alerta se buffer cair abaixo de R$ 15.000 em qualquer leitura semanal — indica que ruptura operacional ou cancelamentos acumulados nos dois Full críticos podem ameaçar a medalha dentro do ciclo mensal.