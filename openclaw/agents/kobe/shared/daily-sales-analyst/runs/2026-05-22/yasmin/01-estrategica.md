<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Pacote completo: reputação, mix de modalidade de envio, `ads_summary` e `account_overview` presentes e com `status: ok`. Janelas 7d, 30d e 60d populadas com cobertura 100%. Ressalva de maturidade: `monthly.md` é template vazio (sem tese mensal consolidada), `weekly.md` tem um único bloco diário (2026-05-22 = este ciclo). A série numérica histórica é robusta, mas **hipóteses formuladas agora são candidatas nascentes, não confirmações de padrão estabelecido** — dois pontos de evidência, não tendência.

---

### Leitura temporal

- **GMV dentro da banda, sustentado por ticket — não por volume.** O dia (R$4.622,03, 84 pedidos) está -2,1% do mesmo dia da semana em GMV (`same_weekday_avg.avg_gmv=R$4.718,81`) e -17,6% em pedidos (`avg_orders=102`). Em relação às janelas longas, GMV está +3,4% vs 30d e +16,3% vs 60d — diferença inteiramente explicada pelo ticket médio (R$55,02 vs R$45,00 no 30d, +22,3%; vs R$42,40 no 60d, +29,8%). A conta não está crescendo em alcance: está faturando mais por pedido com menos pedidos.

- **Patamar de GMV subindo no médio prazo; volume oscilando e sem direção confirmada.** O eixo 60d → 30d mostra GMV médio subindo de R$3.975,41 para R$4.470,29 (+12,4%) — ganho estrutural de patamar em faturamento. Mas pedidos seguem a trajetória inversa no curto prazo: média 7d de 113,3 pedidos vs 84 hoje (-25,9%). A semana recente foi acima da banda (média 7d de R$5.555,18 em GMV, bem acima do 30d e 60d) e hoje representa retração dentro de uma semana forte. Variância intrasemana de sexta-feira é alta nos últimos 4 ciclos (R$3.214 / R$6.465 / R$3.700 / R$5.494 em GMV): o comportamento de hoje está dentro da dispersão histórica da série de sextas.

- **Hipóteses anteriores (único bloco diário disponível — 2026-05-22):** os três sinais registrados no weekly — ADS share acima de 65% como segundo ponto consecutivo, health degradada nos dois campeões Full como segundo ponto, Kit 6 Canecas Tulipa com estoque baixo em Full — se confirmam sem reversão. Sem padrão de semanas, são candidatos robustos, não conclusões.

- **Sinal novo em relação ao padrão histórico de modalidade de envio:** o mix de ontem (`fulfillment_mix_yesterday_top10`: 52,9% Cross-Docking / 47,1% Full) inverte o padrão de 7d (74,9% Full) e 30d (73,7% Full). Essa divergência tem causa identificável nos dados — o anúncio líder do dia (Conjunto 5 Potes Tampa Preta, 20 pedidos) é Cross-Docking, enquanto os dois campeões Full têm health em Padrão inferior. Não é ruptura de operação: é o efeito da composição do dia.

---

### Leitura estratégica

- **A conta opera com GMV sustentado por Mercado Ads sem colchão orgânico confirmado.** ADS share de 69,9% (R$3.228,78 de R$4.622,03; spend R$296,96; ROAS 10,87x; ACOS 4,57%) é o segundo ciclo consecutivo acima de 65%. A eficiência das campanhas de Himmel é extrema — ROAS acima de 10x, ACOS abaixo de 5% — mas isso obscurece a fragilidade estrutural: o patamar orgânico estimado (~30% do GMV atual) ficaria em torno de R$1.400/dia, abaixo do ritmo mínimo para sustentar MercadoLíder Gold (threshold 60d de R$118.400 ÷ 60 ≈ R$1.973/dia). Sem breakdown de `revenue_ads` por `platform_item_id`, é impossível confirmar quais itens têm tração orgânica própria e quais dependem integralmente de campanha.

- **Os dois principais anúncios em modalidade Full têm nível de qualidade do anúncio em Padrão inferior — segundo ponto sequencial sem reversão.** Kit 4 Potes 1050ml Azul-petróleo (MLB4073003575, 11 pedidos, `health=0,75`) e Jogo Potes 5 Peças Tampa Vermelha (MLB3288536143, 10 pedidos, `health=0,71`) estão ambos em Nível Padrão inferior (faixa 0,70–0,84 da escala oficial ML) — o que significa perda progressiva de exposição orgânica em ranking de categoria. O fato de continuarem gerando pedidos sugere que ADS ou volume histórico compensa parcialmente a penalização, mas sem dado de posição em categoria a magnitude da perda não é quantificável. A combinação de health degradada + dependência de ADS cria um ciclo de dependência: se ADS cair, os itens com maior exposição orgânica penalizada não compensam.

- **O vetor líder do dia migrou para Cross-Docking, revelando que a dominância histórica de Full nos dias recentes era ancorada em itens específicos.** O Conjunto 5 Potes Tampa Preta (MLB4535865317, Cross-Docking, health=null, estoque 8.375 unidades) assumiu a liderança com 20 pedidos — puxando o mix do dia para 52,9% Cross-Docking contra o padrão estrutural de 7d/30d (74% Full). A base inteira da conta (`account_overview.active_analysis.fulfillment_mix`) é 33,3% Full / 66,7% Cross-Docking — a dominância histórica de Full nos indicadores agregados era produzida pelos campeões, não pela base. Com dois desses campeões Full com health degradada, o dia "voltou à base". Hipótese: se health dos campeões Full continuar caindo, o mix da conta se aproximará ainda mais da composição da base (Cross-Docking dominante), com menor exposição garantida e maior dependência de logística própria da Budamix.

- **MercadoLíder Gold estável; trajetória para Platinum ativa com margem estreita.** Reputação verde (`color=5_green`), `power_seller_status=gold`, sem proteção ativa (`real_level=null`). Faturamento rolling 60d: R$240.773,23 — 81,34% do threshold Platinum (R$296.000). Gap: R$55.226,77; ETA: 13,8 dias ao ritmo atual de R$4.012,89/dia. O GMV de hoje (R$4.622,03) está acima do ritmo necessário, contribuindo positivamente. A conta está no corredor — não há urgência, mas a margem é suficiente para manutenção, não para recuperação caso o ritmo caia por ciclos seguidos. Nota: `ratings_negative=0,39` (39% das avaliações são negativas) é proporção anômala para conta verde com MercadoLíder Gold — `claims_rate=0,0025` (0,25%) ainda está distante do limite de 1%, mas a proporção de negativas é sinal precoce que merece acompanhamento se `claims_rate` subir.

---

### Tese da conta

**Vulnerável.** O GMV está dentro da banda histórica de 30d e acima da de 60d — os números de superfície são saudáveis. Mas a arquitetura que sustenta esse resultado tem duas fragilidades sobrepostas e inter-relacionadas: Mercado Ads (Himmel) carrega ~70% do faturamento pelo segundo ciclo consecutivo, sem evidência de que o orgânico sustentaria o patamar sem campanha; e os dois anúncios Full que historicamente dominavam o mix da conta estão com nível de qualidade do anúncio em Padrão inferior nos dois únicos pontos medidos, perdendo exposição orgânica progressivamente. O patamar de GMV está subindo no eixo 60d → 30d — mas o vetor é ticket, não volume, e o volume está caindo em todas as janelas. A conta tem boa saúde reputacional e trajetória Platinum ativa, mas a fragilidade está na dependência de poucas variáveis controladas externamente (ADS) sobre uma base de anúncios com saúde degradada.

---

### Risco estrutural principal

**Risco:** Dependência estrutural de Mercado Ads sem colchão orgânico confirmado — ADS share acima de 65% por dois ciclos consecutivos, com ROAS excepcional (10,87x) que mascara a vulnerabilidade.

**Por que importa:** Se as campanhas de Himmel forem pausadas, ajustadas ou restritas por política ML, o GMV colapsa para o patamar orgânico estimado (~30% do atual), insuficiente para sustentar o ritmo mínimo de MercadoLíder Gold na janela rolling de 60d. A situação é agravada pelo health em Padrão inferior dos dois campeões Full — a recuperação orgânica seria mais lenta do que em uma conta com anúncios em nível Profissional ou Padrão superior.

**Histórico:** Registrado como segundo ponto de série no weekly.md (2026-05-22). Sem consolidação semanal anterior — é hipótese nascente com dois pontos de evidência, não padrão confirmado de semanas.

**Sinal de confirmação:** ADS share acima de 60% por mais dois ciclos consecutivos (totalizando 4+ dias) sem evidência de tração orgânica em pelo menos um dos anúncios campeões confirma a dependência como estrutural. O sinal fica indecidível enquanto o pacote não trouxer breakdown de `revenue_ads_yesterday_brl` por `platform_item_id` — dado registrado como pendente desde o ciclo anterior.

---

### Sinais a observar

1. **Health dos campeões Full:** se Kit 4 Potes 1050ml Azul-petróleo (MLB4073003575) e Jogo Potes 5 Peças Tampa Vermelha (MLB3288536143) mantiverem `health < 0,80` nos próximos dois pacotes consecutivos, a penalização de exposição orgânica sai de hipótese e vira tendência confirmada — com implicação direta para a capacidade de sustentação do patamar se ADS for reduzido. Se health subir acima de 0,85 em qualquer um dos dois no próximo ciclo, hipótese de degradação progressiva enfraquece.

2. **Estoque do Kit 6 Canecas Tulipa Lisa 250ml (MLB6167272090) em Full:** 7 unidades após 6 pedidos em um dia. Se o próximo pacote mostrar `available_quantity ≤ 3` ou `status=paused`, o anúncio sai do Full — perda de exposição garantida e, dado `health=null`, sem dado de posição para avaliar impacto em ranking de categoria.

3. **ADS share por terceiro e quarto ciclos consecutivos:** se o share de Mercado Ads ficar acima de 65% por mais dois ciclos (totalizando 4 dias), a dependência transita de hipótese para padrão operacional — momento para Yasmin acionar Himmel para avaliação da composição orgânico-pago e plano de contingência caso campanha seja reduzida ou restringida.