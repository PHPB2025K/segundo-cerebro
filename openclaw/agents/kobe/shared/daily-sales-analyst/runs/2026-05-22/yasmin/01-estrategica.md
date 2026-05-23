<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Memória rasa: `weekly.md` e `monthly.md` são templates sem dados reais preenchidos; `rules.md` contém apenas estrutura genérica. Último daily registrado em 2026-05-20 — lacuna em 2026-05-21. Sem hipóteses ativas de ciclos anteriores para confirmar ou refutar; esta leitura parte do zero histórico de memória. Compensando: `ml_snapshot` completo e confiável em todos os blocos (`status: "ok"`), cobertura de modalidade de envio em 100% dos pedidos nas janelas 7d e 30d. Tese construída exclusivamente sobre dados do pacote.

---

### Leitura temporal

- **vs 7d e mesmos dias da semana:** O dia (84 pedidos, R$4.622) está muito abaixo dos últimos 7 dias (`avg_7d=113,3 pedidos / R$5.555`, `orders_vs_7d_pct=-25,9%`, `gmv_vs_7d_pct=-16,8%`) e da sexta-feira anterior (115 pedidos, R$5.495 em 2026-05-15). Porém, a série de sextas é altamente volátil nas últimas 4 ocorrências: 76 → 83 → 134 → 115 pedidos. A sexta de 2026-05-08 teve 83 pedidos e R$3.700 — similar ao dia atual. O dia está dentro da dispersão histórica de sextas; o `gmv_vs_same_weekday_pct=-2,1%` confirma que o resultado não é fraco em relação ao controle de dia da semana.

- **vs 30d e 60d — divergência estrutural volume/ticket:** O GMV de R$4.622 fica +3,4% acima da média 30d (R$4.470) e +16,3% acima da média 60d (R$3.975), com pedidos 15,4% e 10,4% abaixo das mesmas janelas. A divergência entre volume e faturamento é consistente nas três janelas — a trajetória de ticket é o movimento dominante: R$42,40 (60d) → R$45,00 (30d) → R$55,02 (dia), `ticket_vs_60d_pct=+29,8%`. A conta mantém ou cresce GMV sem crescer alcance.

- **Trajetória 30d vs 60d:** Média de pedidos subiu levemente de 93,8 (60d) para 99,3 (30d), mas o dia atual reverte esse ganho. O GMV cresceu de R$3.975 (60d) para R$4.470 (30d) inteiramente por ticket. O patamar de volume não está em expansão; o patamar de faturamento está, mas por ticket — não por alcance.

- **Hipóteses anteriores:** Nenhuma hipótese ativa em memória (weekly/monthly zerados, lacuna em 2026-05-21). Esta leitura é ponto de partida, não confirmação de tese.

---

### Leitura estratégica

- **ADS como motor oculto do crescimento de ticket:** O GMV cresce nas janelas longas porque o ticket sobe — não porque o volume cresce. Por trás desse número, Mercado Ads gerou R$3.228,78 de R$4.622,03 do dia — **ADS share de 69,8%**, acima do limiar de 50% que classifica como ADS dominante — com ROAS de 10,9x (`R$3.228,78 / R$296,15`) e ACOS de 4,55%. O crescimento de ticket pode estar sendo induzido por campanhas direcionadas a itens de maior valor médio, não por demanda orgânica expandindo. A distinção importa: o patamar de GMV pode ser real e sustentável, ou pode ser um efeito de mídia que mascara volume orgânico mais fraco. Hipótese com ADS share de 69,8% exigindo vigilância — não evento pontual.

- **Saúde degradada nos campeões Full, com inversão de modalidade de envio no top10 do dia:** A janela 7d e 30d registra Full dominante (74,9% e 73,7%) — padrão robusto. Mas o `fulfillment_mix_yesterday_top10` registrou Full 47,1% / Cross-Docking 52,9% — inversão atípica puxada pelo líder do dia, Conjunto 5 Potes Tampa Preta (MLB4535865317, 20 pedidos), que opera em Cross-Docking. Os dois anúncios Full do top 3 acumulam sinais de penalização: Kit 4 Potes 1050ml (MLB4073003575) com `health=0,75` e Conjunto 5 Potes Tampa Vermelha (MLB3288536143) com `health=0,71` — ambos abaixo do limiar 0,85 do ML. Anúncios Full com health degradada perdem exposição orgânica progressivamente. Se os campeões Full recuarem por penalização, o líder Cross-Docking (Tampa Preta) pode absorver o volume — mas a modalidade de envio do top10 migraria de forma permanente, com implicações para SLA e ranking.

- **Cauda morta e concentração estrutural:** 176 anúncios pausados vs 81 ativos — `paused > active × 2,1`, bem acima do limiar de alerta (1,5x). Top 3 concentra 48,8% do volume (`top3_concentration=48,8%`), top 5 concentra 64,3%. No conjunto dos 81 ativos, 7 têm `low_health` e 63 não têm health calculada — 77,8% dos anúncios ativos sem sinal de saúde disponível. A conta opera com cauda essencialmente morta e base de saúde auditável limitada aos 18 anúncios com health calculada.

- **MercadoLíder Gold → Platinum: no ritmo, patamar de qualidade sólido:** `sales_60d_revenue_brl=R$240.773`, gap de R$55.227 para o threshold Platinum de R$296.000, progresso em 81,34%. Ritmo médio atual: R$4.012,89/dia; ETA estimado em 13,8 dias mantendo o ritmo. O dia de R$4.622 está acima do ritmo — contribuição ligeiramente positiva. Reputação operacional sólida: `color=5_green`, `cancellations_rate=0`, `delayed_handling_rate=0,1%`, `claims_rate=0,25%` — todos dentro dos limites exigidos para Platinum. Ponto de atenção fora das métricas operacionais: `ratings_negative=0,39` (39% das avaliações recebidas são negativas) — não afeta o termômetro de reputação diretamente, mas pode comprometer conversão orgânica nos anúncios avaliados.

---

### Tese da conta

**Vulnerável.** A conta sustenta GMV acima da média 60d via expansão de ticket — movimento real nas janelas longas — mas cuja causa é estruturalmente ambígua: ADS share de 69,8% com ROAS 10,9x e ACOS 4,55% é eficiente, mas coloca a conta em dependência de campanhas Himmel como vetor primário de faturamento. O orgânico subjacente não é auditável com clareza enquanto ADS responde por quase 70% do resultado. Adicionalmente, dois dos três anúncios Full do top 3 operam com health abaixo de 0,85 (0,75 e 0,71), sinalizando erosão progressiva de exposição orgânica nesses itens — que são exatamente os que deveriam carregar o orgânico. A cauda está morta, a base Full concentra a operação em anúncios com saúde parcialmente auditável, e o termômetro reputacional está verde com métricas de qualidade sólidas. A vulnerabilidade é estrutural — não operacional.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads (Himmel) como motor primário do GMV, com saúde orgânica dos campeões Full em erosão silenciosa — ADS share de 69,8% sustenta o patamar enquanto MLB4073003575 (`health=0,75`) e MLB3288536143 (`health=0,71`) perdem exposição algorítmica gradualmente.

**Por que importa:** Se as campanhas pausarem ou o orçamento for reduzido, o volume orgânico subjacente será exposto sem a sustentação atual. Paralelamente, health degradada em campeões Full implica perda progressiva de posição em categoria antes que o impacto apareça no faturamento — o ML penaliza algoritmicamente, não de forma imediata. A combinação (ADS sustentando + orgânico enfraquecendo) passa despercebida enquanto o ROAS é alto, e se materializa de forma abrupta quando campanhas param.

**Histórico:** Sem memória acumulada (weekly/monthly zerados) — não é possível confirmar se esse padrão é novo ou crônico. Esta é a primeira leitura com dado disponível.

**Sinal de confirmação:** GMV abaixo de R$3.800 em dia sem redução declarada de orçamento ADS, ou MLB4073003575 / MLB3288536143 com `health < 0,65` nos próximos 3 dias (se health disponível no pacote).

---

### Sinais a observar

1. **Ritmo MercadoLíder Platinum:** GMV diário abaixo de R$3.800 por 2 dias consecutivos indica ritmo insuficiente para manter o ETA de ~14 dias — cada ciclo abaixo dessa marca estende a promoção. O dia de R$4.622 está acima do ritmo médio necessário (R$4.013/dia); qualquer semana com média abaixo de R$3.500/dia adia o Platinum em semanas.

2. **Health dos campeões Full:** Se MLB4073003575 (Kit 4 Potes 1050ml, `health=0,75`) ou MLB3288536143 (Conjunto 5 Potes Tampa Vermelha, `health=0,71`) registrarem `health < 0,65` ou saírem do top 5 por 2 dias consecutivos sem explicação de estoque, confirma erosão orgânica estrutural nos anúncios Full — sinal válido se health disponível no pacote.

3. **Estoque Kit 6 Canecas Tulipa Lisa 250ml:** MLB6167272090 tem `available_quantity=12` com 6 pedidos no dia — estoque para aproximadamente 2 dias no ritmo atual. Se o anúncio sair do top 10 sem reposição documentada e sem substituto aparecendo na cauda, confirma exposição a ruptura de vetor secundário (canecas) sem plano B visível na base ativa.