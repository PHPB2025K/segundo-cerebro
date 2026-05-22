<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Janelas quantitativas robustas — 7d, 30d e 60d disponíveis com cobertura 100% nos dados de logística; ml_snapshot completo (reputação, mix de modalidade de envio, ADS summary, account_overview). Ponto fraco: `weekly.md` e `monthly.md` são templates vazios, sem consolidação narrativa; conteúdo do daily anterior (2026-05-20.md) não foi entregue nesta sessão. Sem hipóteses ativas herdadas para confirmar ou refutar — a leitura de hoje inaugura tese em vez de confirmá-la.

---

### Leitura temporal

- **30d e 60d — mudança de patamar em GMV, não em volume:** GMV de R$ 6.113 está +38,7% vs média 30d (R$ 4.407) e +57,3% vs média 60d (R$ 3.886). Pedidos cresceram só +1,7% e +9,3% nas mesmas janelas — o salto de patamar é inteiramente do ticket, que subiu de R$ 44,36 (30d) e R$ 42,05 (60d) para R$ 60,52 no dia (`ticket_vs_30d_pct=+36,4%`, `ticket_vs_60d_pct=+43,9%`). A conta não cresceu em alcance; cresceu em valor por pedido.

- **7d — inversão parcial:** Na janela mais recente, pedidos caíram -15,1% (101 vs avg 118,9), mas GMV subiu +8,8% (R$ 6.113 vs R$ 5.616). O 7d revela que a última semana foi de volume mais alto que a média histórica — o dia analisado entra abaixo do ritmo semanal em pedidos, mas acima em GMV, mantendo a lógica de ticket elevado.

- **Mesmo dia da semana (quinta) — dentro do normal em pedidos, acima em GMV:** Par sazonal das últimas 4 quintas: avg 102,75 pedidos / R$ 4.686 GMV / ticket R$ 45,61. O dia (101 pedidos / R$ 6.113 / ticket R$ 60,52) está -1,7% em pedidos mas +30,5% em GMV vs par — confirmando que o ganho de ticket não é artefato de dia da semana; é consistente com 30d, 60d e o controle sazonal ao mesmo tempo. Rompimento de patamar em GMV com suporte em ≥ 3 janelas independentes.

- **Sem hipóteses anteriores para rastrear** (weekly/monthly vazios, daily anterior sem conteúdo nesta sessão): leitura inaugural da tese narrativa.

---

### Leitura estratégica

- **Lente 5 — ADS dominante, orgânico não testado:** ADS share calculado: R$ 4.593,66 atribuídos / R$ 6.113,02 de GMV = **75,1%**. ROAS 13,4x (R$ 4.594 / R$ 342), ACOS 4,71% — campanha de Himmel extremamente eficiente. O problema não é a eficiência; é a dependência: o orgânico visível representa ~25% do GMV atribuído. O ganho de patamar que as janelas 30d e 60d registram pode ser parcialmente construído sobre expansão progressiva de ADS — não sobre crescimento de base orgânica verificável. Qualquer pausa, corte de orçamento ou mudança de leilão no Mercado Ads derruba proporcionalmente 3/4 do GMV atribuído sem aviso prévio.

- **Lente 3 — Concentração estrutural + inversão de modalidade de envio intraday:** Top 3 em 59,4%, top 5 em 76,2% — dependência crônica da família IMB501 (Potes Redondos: Preta, Cinza, Vermelha) mais Kit 10 Potes 1050ml. O mix de modalidade de envio do dia (top 10: 80,2% Cross-Docking vs 19,8% Full) é **inversão** do padrão 7d (77% Full / 23% Cross-Docking) e 30d (73,6% Full / 26,4% Cross-Docking): os campeões de hoje são Cross-Docking-pesados enquanto a operação estrutural da última semana é Full-pesada. Isso indica que os vetores IMB501 — todos em Cross-Docking — puxaram o dia; o Full que sustentou a semana ficou em segundo plano. Cross-Docking depende diretamente de expedição Budamix: atraso de coleta impacta sem o buffer do CD do ML.

- **Lente 6 — MercadoLíder Gold a 15 dias do Platinum, e o dia ajudou:** `progress_pct=80,04%`, `gap_revenue_brl=R$ 59.091`, ETA 15 dias no ritmo médio de R$ 3.948/dia. O dia (R$ 6.113) está +55% acima desse ritmo — um dia como hoje comprime o ETA para ~10-12 dias se sustentado. Platinum significa boost de Buy Box e prioridade em buscas; cada dia abaixo do ritmo atrasa, cada dia acima adianta. Métricas de qualidade (`claims_rate=0,25%`, `cancellations_rate=0`, `delayed_handling_rate=0,1%`) estão longe dos thresholds de risco — a medalha não está ameaçada, e o avanço para Platinum é o vetor estratégico principal da conta neste momento. Ressalva: `ratings_negative=0,39` (39% das avaliações negativas) é atipicamente alto para uma conta verde — não impacta o termômetro ML, mas é sinal de qualidade percebida que pode deprimir conversão ao longo do tempo. Sinal a observar, não risco confirmado.

- **Lente 3 (estoque) — rupturas iminentes em Full:** Kit 06 Canequinhas Acrílico (`MLB4410218897`): `available_quantity=1`, 3 pedidos no dia — ruptura em D+0 ou D+1. Kit 6 Canecas Porcelana Tulipa (`MLB6167272090`): `available_quantity=14`, 5 pedidos no dia — ~3 dias de estoque. Ambos em Full: reabastecimento exige entrada no CD do ML, mais lento que repor Cross-Docking. Adicionalmente, Kit 4 Potes 1050ml (`MLB4073003575`): `health=0,75` em Full — abaixo do threshold 0,85, com penalização de ranking em andamento progressivo.

---

### Tese da conta

**Vulnerável.**

A conta ML está num patamar de GMV materialmente superior ao bimestre — +57,3% vs 60d — sustentado por ticket crescente e campanha de ADS altamente eficiente (ROAS 13,4x, ACOS 4,71%). Reputação estrutural verde, MercadoLíder Gold estável com métricas de qualidade dentro dos limites e trajetória ativa para Platinum em ~15 dias. O número de hoje é bom. A estrutura por trás dele tem três fragilidades sobrepostas que impedem a leitura de "saudável": (1) 75,1% do GMV é ADS-atribuído, sem orgânico verificável como base independente; (2) dois anúncios em Full estão em ruptura iminente de estoque — Canequinhas Acrílico com 1 unidade, Canecas Porcelana com 14; e (3) o Kit 4 Potes 1050ml, campeão em Full, opera com health=0,75 e penalização progressiva de ranking. A conta cresce no número que importa (GMV), mas a estrutura que sustenta esse crescimento é concentrada, ADS-dependente e com vetores Full se deteriorando silenciosamente.

---

### Risco estrutural principal

**Risco:** Dependência de Mercado Ads sem base orgânica verificável — ADS share de 75,1% com cobertura de 3/4 do GMV atribuído.

**Por que importa:** Se o patamar de GMV dos últimos 30-60d foi construído sobre expansão progressiva de investimento em ADS em vez de crescimento orgânico, o resultado é reversível — não é ganho estrutural de mercado. Qualquer interrupção nas campanhas de Himmel (pausa, corte de verba, mudança de regra de leilão do Mercado Ads) retorna a conta ao patamar anterior sem suporte de tráfego pago. Um ROAS de 13,4x também pode indicar que o leilão está favorável agora, mas leilões mudam — e a conta não tem, no dado disponível, evidência de que o orgânico sustenta o patamar atual de forma independente.

**Histórico:** Primeiro ciclo com dado de ADS share visível; sem registro anterior desse padrão na memória narrativa. Não há como afirmar se a dependência é crônica ou recente — a base é inaugural.

**Sinal de confirmação:** ADS share acima de 60% por 3 dias consecutivos confirma que a dependência é padrão operacional da conta, não pico de campanha pontual. Abaixo de 40% em 2 dias seguidos, hipótese de dependência estrutural enfraquece.

---

### Sinais a observar

1. **Ruptura de estoque em Full nos próximos 2 dias:** Canequinhas Acrílico (`MLB4410218897`, `available_quantity=1`) e Canecas Porcelana Tulipa (`MLB6167272090`, `available_quantity=14`) em Full — se qualquer um aparecer com `out_of_stock=true` ou `status=paused` nos próximos 2 ciclos, ruptura confirmada com impacto prospectivo em `cancellations_rate` e perda de posição em Full (reabastecimento lento).

2. **ADS share acima de 60% por 3 dias consecutivos** — confirma que o patamar de GMV 30/60d é sustentado estruturalmente por ADS, não por crescimento orgânico. Se o share cair abaixo de 40% em 2 dias seguidos, a hipótese de dependência perde força e a tese migra para "saudável".

3. **`ratings_negative` acima de 30% ao longo de 2 ciclos com dado de reputação disponível** — se a taxa de avaliações negativas se mantiver nesse nível nos próximos pacotes, há hipótese de erosão de conversão nos anúncios mais expostos afetando organicamente o volume de pedidos ao longo do tempo. Sinal condicional a dado disponível no pacote.