<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Qualidade da base

Memória presente: weekly.md com 1 entrada acumulada (L05 desta sessão para 2026-05-22), monthly.md sem tese preenchida (template vazio), rules.md operacional mas raso. `ml_snapshot` completo: reputação, mercadolider, fulfillment_mix (7d/30d/top10/base), top_items_details, ads_summary e account_overview com `status: ok`. Janela 60d com 60 dias de dados confirmados. Lacuna em 2026-05-21 (sem daily); última memória diária é 2026-05-20. Monthly não oferece âncora mensal madura — patamar depende do histórico numérico e da weekly.

---

### Leitura temporal

- **vs 60d (patamar de fundo):** GMV +16,3% (`gmv_vs_60d_pct`) com ticket +29,8% (`ticket_vs_60d_pct`) e pedidos -10,4% (`orders_vs_60d_pct`). A conta está acima do patamar de dois meses, mas o motor é exclusivamente ticket — volume segue abaixo do bimestre. O padrão se confirma nas janelas de 30d e 60d simultaneamente, o que o qualifica como deslocamento estrutural de mix, não ruído de dia.

- **vs 30d (banda do mês):** GMV +3,4%, ticket +22,3%, pedidos -15,4%. O GMV está levemente acima da banda mensal, mas os pedidos estão abaixo. A divergência ticket vs volume é idêntica ao sinal dos 60d — consistência entre janelas descarta explicação pontual.

- **vs 7d (movimento recente):** GMV -16,8%, pedidos -25,9% em relação à média dos últimos 7 dias (`avg_7d`: R$5.555, 113,3 pedidos). A média 7d está inflada por uma semana forte recente — o dia de hoje representa retração em relação a esse pico, mas não reverte o ganho de 30d/60d.

- **vs mesmo dia da semana (controle sazonal):** GMV -2,1% e pedidos -17,6% em relação à média de 4 sextas (`same_weekday_avg`: R$4.718,81, 102 pedidos). A volatilidade entre sextas é alta: R$3.214 a R$6.465 nos últimos 4 dados. O dia de hoje (R$4.622) fica dentro dessa banda — o controle não aponta deterioração estrutural.

- **Hipóteses anteriores:** weekly.md confirma que ADS dominância (~69,9%), health abaixo de 0,80 nos dois campeões Full e estoque crítico do Kit 6 Canecas Tulipa (9 unidades) foram sinalizados pelo L05 desta mesma sessão. Todos em primeiro ciclo de observação — sem série temporal anterior para confirmar ou refutar.

---

### Leitura estratégica

- **Lente 1 — Patamar vs banda:** A conta ganhou patamar de GMV em relação ao bimestre (+16,3% vs 60d), mas o ganho é exclusivamente via ticket (+29,8%), não via crescimento de alcance (pedidos -10,4% vs 60d). Esse padrão confirmado em múltiplas janelas aponta deslocamento de mix para itens de maior valor — não expansão de base compradora. A questão estratégica que permanece aberta: quanto desse ganho de ticket é orgânico e quanto é efeito de ADS (Himmel) filtrando compradores de maior valor? Sem histórico de ADS share em janelas anteriores no pacote, essa separação é indecidível hoje.

- **Lentes 3 + 5 — Dependência de anúncio e Mercado Ads:** A conta operou com ADS share de **69,9% do GMV** (`revenue_ads_yesterday_brl` R$3.228,78 / `gmv` R$4.622,03), ROAS 10,87x e ACOS 4,57% — eficiente, mas estruturalmente frágil. O piso orgânico implícito é de aproximadamente R$1.393. Com top 3 em 48,8% e top 5 em 64,3% dos pedidos, a conta tem poucos anúncios gerando volume e a maioria deles depende de campanhas para exposição. A base de 176 anúncios pausados para 81 ativos (relação 2,17:1) confirma cauda morta dominante — a conta opera a partir de poucos listings, amplificados por Himmel.

- **Lentes 2 + 4 — Exposição e saúde dos campeões:** Dois campeões em modalidade de envio Full apresentam health degradada: MLB4073003575 (Kit 4 Potes de Vidro 1050ml, 11 pedidos) com `health=0,75` e MLB3288536143 (Jogo Potes de Vidro Tampa Vermelha, 10 pedidos) com `health=0,71` — ambos abaixo do threshold 0,85. Juntos representam ~25% dos pedidos do dia. Health degradada em anúncio Full corrói ranking orgânico progressivamente, sem impacto imediato no GMV — o efeito aparece com defasagem, reduzindo a sustentabilidade do resultado independente de ADS. Todos os top 10 são Clássico (`gold_special`), exceto o Kit 6 Canecas Lisas 200ml (`gold_pro`, catálogo, 3 pedidos) — a conta não tem segundo vetor Premium com peso relevante.

- **Lente 6 — MercadoLíder Platinum:** Progresso em 81,34% (`progress_pct`), gap R$55.226,77 (`gap_revenue_brl`), ritmo diário atual R$4.012,89 (`ritmo_diario_brl`), ETA estimado 13,8 dias. O dia de hoje (R$4.622) ficou acima do ritmo necessário, contribuindo marginalmente para reduzir o gap. A conta está na zona "gap R$30k–R$100k" — no trilho, mas sem folga. Qualquer contração sustentada do GMV, como a queda de -16,8% vs 7d se persistir, empurraria o ETA para além de 20 dias. Reputação verde estável (`color=5_green`, `power_seller_status=gold`) com métricas operacionais dentro dos thresholds (claims 0,25%, cancelamentos 0%, atrasos 0,12%) — não há risco imediato de rebaixamento de medalha. Ponto de atenção fora dos thresholds operacionais: `ratings_negative=0,39` (39% das avaliações negativas) — sem contexto histórico no pacote para determinar trajetória; não é suficiente para qualificar como risco confirmado, mas merece série temporal.

---

### Tese da conta

**Vulnerável.** O GMV cresceu em relação ao bimestre (+16,3% vs 60d), sustentado inteiramente por expansão de ticket (+29,8%), não por alcance. Mas a estrutura que suporta esse resultado é frágil: 70% do GMV depende de campanhas Himmel; dois campeões Full com health abaixo de 0,80 acumulam penalização orgânica progressiva; a base ativa é pequena (81 anúncios, 176 pausados) e concentrada (top 5 = 64,3% dos pedidos). O número do dia está dentro da banda histórica para a sexta-feira, mas a conta não tem segundo vetor capaz de sustentar o patamar se ADS reduzir ou um dos campeões perder exposição orgânica. A tese de "ganho de patamar" é real no número, porém opaca na origem — e depende de estrutura frágil para se manter.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads (Himmel) sem piso orgânico estabelecido — ADS share de 69,9% do GMV, com base ativa concentrada em poucos anúncios e cauda morta dominante (176 pausados para 81 ativos).

**Por que importa:** Se as campanhas de Himmel reduzirem, pausarem ou perderem eficiência, o GMV cai para um piso orgânico estimado de ~R$1.400 — menos de um terço do nível atual. A tese de "ganho de patamar" não sobrevive a esse cenário. O risco é agravado pelo fato de que o ticket elevado pode ser produto de ADS qualificando compradores de maior valor; com orgânico puro, o ticket provavelmente regride junto com o volume.

**Histórico:** Primeiro ciclo com dado explícito de ADS share quantificado (weekly.md 2026-05-22 é a primeira entrada com essa métrica). Sem série temporal anterior de ADS share no pacote, não é possível afirmar se 70% é padrão estabelecido ou condição recente — o risco é classificado como identificado, não como confirmado estruturalmente.

**Sinal de confirmação:** ADS share acima de 65% por mais 2 ciclos consecutivos com dado confirma dependência estrutural estabelecida. Queda de GMV superior a 25% em dia com `spend_yesterday_brl` abaixo de R$150 seria sinal diagnóstico direto da fragilidade orgânica.

---

### Sinais a observar

1. **GMV abaixo de R$4.000 por 2 dias seguidos** nos próximos 7 dias confirma reversão do patamar 30d e pressiona o ETA de MercadoLíder Platinum para além de 20 dias — retirando a conta da zona "no trilho".

2. **`health` de MLB4073003575 (Kit 4 Potes de Vidro 1050ml) ou MLB3288536143 (Jogo Potes de Vidro Tampa Vermelha) caindo para ≤0,68** no próximo pacote com dado de health, por 2 ciclos consecutivos, confirma degradação progressiva de exposição orgânica nos principais anúncios Full — efeito que não aparece imediatamente no GMV mas corrói sustentabilidade de médio prazo.

3. **Kit 6 Canecas Porcelana Tulipa Lisa 250ml (MLB6167272090, `available_quantity=9`, Full) com 5+ pedidos no dia imediato sem reposição confirmada** sinaliza ruptura de estoque nesse anúncio Full — perda de posição no CD do ML e custo de reintrodução que impactam o ranking mesmo após reabastecimento.