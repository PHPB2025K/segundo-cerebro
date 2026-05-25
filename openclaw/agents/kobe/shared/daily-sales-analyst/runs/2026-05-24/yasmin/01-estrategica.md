<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória recente robusta: weekly.md tem 3 entradas diárias vivas (22, 23 e 24/05) com hipóteses ativas, contagens precisas de ciclos e contexto ADS acumulado. Janelas 7d, 30d e 60d com dados completos (coverage 100% em todos). monthly.md sem tese mensal registrada — ausência normal para fim de mês em conta nova. Todos os blocos `ml_snapshot` com `status: ok`.

---

### Leitura temporal

- **vs 60d e 30d:** GMV hoje (R$5.024,80) está +22,7% acima da média 60d (R$4.096,61) e +10,4% acima da 30d (R$4.549,64), com ticket +18,8% e +11,2% nas mesmas janelas e pedidos estáveis (+3,2% e -0,7%). A conta ganhou patamar ao longo do bimestre de forma ticket-led — não por alcance, por mix de maior valor. Consistência em duas janelas confirma tendência, não ruído.

- **vs 7d:** GMV -2,5% em relação à média 7d (R$5.153,29) com pedidos +3,6% — o ticket caiu de R$53,92 (7d avg) para R$50,76, inversão oposta à tendência bimestral. A janela de 7d inclui o domingo 17/05 (R$5.180,78), pico recente; hoje ficou -3,2% abaixo desse teto. Leitura: conta está se acomodando dentro do novo patamar, não rompendo para cima.

- **vs mesmo dia da semana:** +36,1% GMV sobre a média dos 4 domingos anteriores (R$3.691,93), mas essa média é puxada pelo domingo anômalo de 10/05 (R$2.355,62). A referência mais limpa é 17/05 (R$5.180,78) — hoje ficou abaixo, dentro da banda do novo patamar semanal.

- **Hipóteses anteriores:** (a) health de MLB3288536143 (0,71) e MLB4073003575 (0,75) em nível regular pelo **quarto ciclo consecutivo** sem movimento detectado — estagnação confirmada, memória de 24/05 registra quinto ciclo como definidor; (b) Kit 6 Canecas Porcelana Tulipa (MLB6167272090) ausente do top hoje — confirma ruptura ou pausa conforme hipótese ativa desde 22/05; (c) ADS share retornou a 71,2% após recuo de 49,5% em 23/05 — **primeiro** ponto da nova série pós-recuo, não segundo consecutivo ainda.

---

### Leitura estratégica

- **Patamar real sustentado por estrutura frágil:** o ganho bimestral (GMV +22,7% vs 60d, ticket +18,8%) é genuíno na série, mas sua manutenção depende de dois vetores simultâneos em estado de risco: Mercado Ads com share de 71,2% (`revenue_ads_yesterday_brl` R$3.578,05 / GMV R$5.024,80, ROAS 11,3x, ACOS 4,22%) operando **sobre** anúncios em nível regular de qualidade (MLB3288536143 `health` 0,71; MLB4073003575 `health` 0,75), não ao lado de orgânico saudável. A eficiência de ADS mascara a erosão — não é sinal de força estrutural.

- **ADS compensando degradação orgânica, não amplificando crescimento:** MLB3288536143 e MLB4073003575 — 65 dos 99 pedidos do dia — são ambos `gold_special` fora de catálogo (`is_catalog: false`), competindo por ranking em categoria. Health degradada nessa tipologia significa que o ML está reduzindo exposição orgânica progressivamente. A conta está rodando **contra** o algoritmo de ranking enquanto ADS compensa o que o orgânico está perdendo. O nível de qualidade estagnado há 4 ciclos não é plateau — é deterioração sem recuperação visível.

- **Cluster de canecas em colapso de estoque simultâneo:** segundo vetor da conta se desintegra em três pontos paralelos: Kit 6 Canecas 250ml (MLB6582645908, Cross-Docking) com 1 unidade restante após 3 pedidos hoje — ruptura em curso; Kit 6 Canecas Lisas 200ml (MLB6232315532, Catálogo Premium Full) com 25 unidades a ~9 pedidos/dia = ~2,8 dias de cobertura — ruptura iminente com efeito Buy Box de recuperação lenta por ser `is_catalog: true`; Kit 6 Canecas Porcelana Tulipa (MLB6167272090) ausente do top — provável ruptura ou pausa já confirmada. Os três pontos convergem na mesma janela de 2-3 dias.

- **MercadoLíder Platinum e janela comprimida por duas frentes:** gap R$48.941,14, progresso 83,47%, ETA ~11,9 dias ao ritmo de R$4.117,65/dia (`mercadolider.ritmo_diario_brl`). GMV de hoje (R$5.024,80) está acima do pace necessário — positivo. O risco real é que rupturas no cluster de canecas comprimam essa janela por dois canais simultâneos: receita perdida (reduz pace) e cancelamentos automáticos de pedidos já realizados (deteriora `cancellations_rate`, que hoje está em zero mas pode mudar rapidamente se MLB6582645908 ou MLB6232315532 gerarem pedidos sem estoque).

---

### Tese da conta

**Vulnerável.** O patamar bimestral (GMV +22,7% vs 60d) é real, mas a estrutura que o sustenta opera em dependência dupla: Mercado Ads com share dominante (71,2%) cobrindo a erosão orgânica progressiva dos dois campeões em nível regular de qualidade há quatro ciclos consecutivos, sem segundo vetor orgânico saudável emergindo para substituição. O cluster de canecas — que representaria esse segundo vetor — está em colapso de estoque em pelo menos dois pontos simultâneos com janela de dias. A conta está correndo contra dois relógios: o da qualidade dos anúncios de potes (quinto ciclo como ponto definidor) e o das rupturas de canecas (2-3 dias, não semanas). Faturamento acima da banda histórica convive com operação progressivamente mais frágil por baixo.

---

### Risco estrutural principal

**Risco:** Dois anúncios líderes (MLB3288536143 e MLB4073003575) em nível regular de qualidade (`health` 0,71 e 0,75) pelo quarto ciclo consecutivo, sustentados por Mercado Ads com share dominante (71,2%), sem segundo vetor orgânico saudável confirmado — dependência dupla onde erosão orgânica de ML e eficiência de ADS operam em direções opostas.

**Por que importa:** A degradação de `health` em anúncios Clássico fora de catálogo (`is_catalog: false`) é progressiva e reduz exposição orgânica no ranking de categoria. Se o ML continuar esse movimento e ADS for ajustado, pausado ou perder eficiência, o impacto é multiplicativo — não linear. O patamar de ticket adquirido nos últimos 60d pode se reverter rapidamente se o volume de pedidos contrair antes que novo vetor orgânico se consolide. O `low_health_count` de 7 e `no_health_data_count` de 62 na base (de 80 ativos) indicam que o risco de degradação não está limitado aos dois campeões.

**Histórico:** Registrado desde ciclo de 22/05 (memória: "segundo ponto idêntico entre ciclos"). Quarto ciclo. Persistente e crescente em severidade, sem sinal de reversão.

**Sinal de confirmação:** `health` de MLB3288536143 ≤ 0,69 no quinto ciclo — cruzamento de nível regular para preocupante no anúncio responsável por ~47% dos pedidos do dia, combinado com ADS share acima de 65% por segundo dia consecutivo, confirma o risco como estrutural ativo e não mais latente.

---

### Sinais a observar

1. **Nível de qualidade de MLB3288536143 no quinto ciclo (próximo pacote):** `health` ≤ 0,69 (preocupante) confirma degradação cruzando patamar qualitativo no anúncio de maior volume da conta; `health` ≥ 0,85 (bom) reverte o risco para hipótese enfraquecida. Sem esse dado, tese de erosão orgânica permanece não resolvida.

2. **ADS share nos próximos 2 dias consecutivos acima de 65%:** segundo ponto acima de 65% em 25/05 com nível de qualidade dos campeões estagnado aciona alinhamento Yasmin–Himmel sobre cobertura preventiva e dependência orgânica vs mídia paga (gatilho registrado na memória de 24/05).

3. **Ruptura de MLB6232315532 (Kit 6 Canecas Lisas 200ml, Catálogo Premium Full, 25 unidades, ~9 pedidos/dia) nos próximos 2-3 dias sem reposição visível:** confirma perda de Buy Box no único vetor `gold_pro` + `is_catalog: true` do top da conta, com impacto direto no pace do MercadoLíder Platinum e cancelamentos prospectivos que deterioram `cancellations_rate`.