<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Base robusta para esta sessão: todos os blocos `ml_snapshot` vieram com `status: ok` (reputação, MercadoLíder, fulfillment mix 7d/30d/yesterday top10, top_items_details, ads_summary, account_overview). Weekly.md acumula três entradas (22, 23 e 24/05) com hipóteses ativas rastreáveis; monthly.md presente mas sem tese mensal consolidada ainda (template). Limitação relevante: `health` ausente em 61 dos 79 anúncios ativos (`no_health_data_count=61`) — leitura de qualidade de anúncio é parcial e concentrada nos top da série.

---

### Leitura temporal

- **7d:** GMV essencialmente flat (R$5.127 vs avg_7d R$5.127 — `changes.gmv_vs_7d_pct=0,0%`), mas pedidos subiram 13,3% (`changes.orders_vs_7d_pct`). A implicação: o ticket caiu dentro da semana de R$53,81 para R$47,48 (−11,8%), indicando que os dias mais altos da janela 7d foram puxados por mix de maior valor médio — hoje o crescimento de volume veio com compressão de ticket. Não é deterioração: é composição de mix.

- **30d e 60d:** GMV +11,2% (`changes.gmv_vs_30d_pct`) e +24,0% (`changes.gmv_vs_60d_pct`); pedidos +7,6% e +11,9%; ticket +3,4% e +10,8%. Todas as três dimensões acima das duas janelas longas simultaneamente — o movimento não é ruído de um ponto, é consistência multi-janela.

- **Mesmo dia da semana (segundas):** Today 108 pedidos / R$5.127,39 vs média das últimas 4 segundas de 92,5 pedidos / R$3.911,42 (`changes.orders_vs_same_weekday_pct=+16,8%`, `changes.gmv_vs_same_weekday_pct=+31,1%`). A série das segundas mostra trajetória ascendente: R$2.588 → R$3.665 → R$4.184 → R$5.208 (excepção de 04/05) → R$5.127 hoje. A segunda-feira hoje confirma a faixa superior dessa série — não é outlier.

- **Hipóteses anteriores:** (a) Concentração crescente do cluster IMB501 — **confirmada e em aceleração**: memórias 22/05 → 23/05 → 24/05 registraram 44% → 47,5% do dia; hoje o cluster (Tampa Preta 40 + Cinza 11 + Vermelha 10 = 61 pedidos) chegou a 56,5%. (b) Health estagnada em 0,71 no MLB3288536143 — **quinto ciclo idêntico confirmado**. (c) Kit 10 Potes 1050ml (MLB4676726433) como variável de risco — **confirmado como sinal crítico**: paused com `available_quantity=0` e 3 pedidos gerados.

---

### Leitura estratégica

- **Ganho real de patamar com vetor único:** A conta opera consistentemente acima da banda de 30d e 60d em GMV e pedidos, confirmado pelo controle de sazonalidade de dia da semana. Esse movimento não é acomodação — é patamar em elevação. O problema é a arquitetura do ganho: o cluster IMB501 (MLB3288536143) concentra 56,5% dos pedidos do dia, contra 44% em 22/05. A conta cresce, mas cada dia cresce mais dependente de um único anúncio — e esse anúncio tem `health=0,71` (nível preocupante), sem Frete Grátis (`free_shipping=false`), operando em modo Clássico não-Catálogo (`gold_special`, `is_catalog=false`). A posição em ranking de categoria que sustenta esse volume é progressivamente pressionada pelo ML sem que o resultado financeiro ainda mostre — é depleção silenciosa.

- **ADS como compensador da exposição orgânica degradada:** `ads_summary.revenue_ads_yesterday_brl=R$2.905,50` sobre GMV de R$5.127,39 resulta em ADS share de **56,7%** — zona de ADS dominante (>50%). ROAS de **7,67x** ainda forte, mas ACOS saltou de ~4,43% (23/05) para **14,15%** — a campanha está pagando mais por resultado. Cruzando com o quinto ciclo de health 0,71 no campeão IMB501: a hipótese mais coerente é que o ADS está compensando a perda de exposição orgânica que a health degradada já gerou. Enquanto o ROAS sustenta, o faturamento se mantém — mas a estrutura é dependente de campanha, não de orgânico. Himmel segura o volume; a saúde do anúncio não sustenta por si.

- **Mix de modalidade de envio revela estrutura assimétrica:** Top 10 de ontem: 79,5% Full (`fulfillment_mix_yesterday_top10.full_pct`). Base ativa da conta: 36,7% Full (`account_overview.active_analysis.fulfillment_mix.full_pct`). A diferença entre 79,5% e 36,7% indica que os campeões estão fortemente concentrados em Full, enquanto a base ativa depende de Cross-Docking (63,3%). O padrão é estável nos 7d e 30d (ambos em Full 74,7%), confirmando que os anúncios que carregam o volume vivem no CD do ML — qualquer ruptura de estoque Full em campeão afeta o core do faturamento de forma desproporcionalmente mais intensa do que a participação da conta sugere.

- **Três vulnerabilidades simultâneas no topo do portfólio:** MLB6232315532 (Kit 6 Canecas Lisas 200ml) com `available_quantity=19` e ritmo de ~11 pedidos/dia — cobertura de ~1,7 dias; é Catálogo Premium (`gold_pro`, `is_catalog=true`), então ruptura significa perda de Buy Box com recuperação lenta, não apenas estoque. MLB4676726433 (Kit 10 Potes 1050ml) com `status=paused` e `available_quantity=0` gerou 3 pedidos no dia — cancelamentos prospectivos garantidos com impacto direto na `cancellations_rate` ML nos próximos ciclos. MLB3288536143 (campeão IMB501) com `health=0,71` — quinto ciclo, ranking orgânico em compressão. Os três não são eventos isolados: ocorrem simultaneamente no topo da conta.

---

### Tese da conta

**Em ganho de patamar, com vulnerabilidade estrutural crescente.** O GMV e os pedidos estão consistentemente acima da banda de 30d e 60d, com controle de sazonalidade confirmando que o movimento é estrutural, não pontual. A trajetória das últimas segundas-feiras reforça a leitura de patamar em elevação. Porém, o ganho está construído sobre um tripé frágil: um único anúncio-cluster com health preocupante (IMB501, 56,5% do dia), ADS share acima de 50% com ACOS em elevação, e dois pontos de ruptura iminente no top do portfólio (estoque crítico em Catálogo Premium e anúncio pausado com pedidos ativos). A conta ganha patamar, mas o piso desse crescimento é estreito — uma pausa de campanha, uma ruptura de estoque Full ou a continuação da degradação de health podem comprometer o vetor sem aviso nos agregados financeiros imediatos.

---

### Risco estrutural principal

**Risco:** Dependência crescente do cluster IMB501 (MLB3288536143) como vetor primário da conta, com `health=0,71` (nível preocupante) estagnado há cinco ciclos consecutivos, sem Frete Grátis, e sustentado por ADS share em zona dominante (56,7%) com ACOS em elevação (14,15%).

**Por que importa:** O cluster representa 56,5% do volume do dia e opera em ranking de categoria (Clássico não-Catálogo) — visibilidade orgânica depende diretamente do nível de qualidade do anúncio. Com `health=0,71`, o ML já penaliza o ranking progressivamente. Se o ADS recuar (campanha pausada, ajuste de verba, ou ineficiência crescente de ACOS), a queda orgânica que está mascarada vai se materializar. A conta não tem segundo vetor capaz de absorver a perda: top 5 concentration em 73,1%, portfólio com 179 anúncios pausados contra 79 ativos, e nenhum anúncio emergente com volume próximo ao IMB501.

**Histórico:** Aparece nas memórias de 22, 23 e 24/05 com percentuais crescentes (44% → 47,5% → 56,5% hoje). Health estagnada em 0,71 por cinco ciclos. Não é risco novo — é tendência em aceleração sem contra-movimento detectado.

**Sinal de confirmação:** IMB501 abaixo de 50% do volume por 2 dias seguidos com ACOS acima de 18%, ou health de MLB3288536143 caindo abaixo de 0,68 no próximo ciclo, confirmam que o risco virou problema operacional real.

---

### Sinais a observar

1. **Ruptura iminente em Catálogo Premium:** MLB6232315532 (Kit 6 Canecas Lisas 200ml) com `available_quantity=19` e ritmo histórico de ~11 pedidos/dia. Se no próximo pacote `available_quantity` aparecer abaixo de 5 ou o anúncio figurar como pausado, a ruptura está em andamento — Buy Box em Catálogo (`is_catalog=true`, `gold_pro`) não é recuperado na mesma velocidade de um Clássico. Janela: próximas 24–48h. Isso foi sinalizado pela primeira vez em 23/05 (`available_quantity=33`) e perdeu cobertura a cada ciclo.

2. **Cancelamentos prospectivos de MLB4676726433 na `cancellations_rate`:** Kit 10 Potes 1050ml pausado com estoque zero gerou 3 pedidos no dia. Se `cancellations_rate` da API ML — atualmente em 0 — subir acima de 0,005 nos próximos 3 a 5 ciclos, esses cancelamentos estão entrando na janela de reputação de forma que ainda não aparece nos agregados hoje. Monitorar junto com qualquer nova ocorrência de anúncio pausado com pedido.

3. **Trajetória do ACOS de ADS:** ACOS saltou de 4,43% (23/05) para 14,15% hoje (`ads_summary.avg_acos_pct`). Se no próximo ciclo ACOS superar 20% com ADS share mantendo-se acima de 50%, confirma tendência de ineficiência crescente de campanha — testando diretamente a hipótese de que ADS compensa exposição orgânica perdida. ROAS abaixo de 5x seria o segundo marcador de alerta no mesmo vetor.