<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly.md e monthly.md estão em template vazio — sem tese semanal ou mensal acumulada para contrastar. As janelas quantitativas (7d, 30d, 60d, mesmos dias da semana) têm cobertura completa e consistente; a base numérica é robusta, mas a base de memória estruturada é incipiente. Nenhuma hipótese ativa anterior para confirmar ou refutar — a leitura de hoje serve como primeiro ponto de referência, não como confirmação de tese.

---

### Leitura temporal

- **Aceleração consistente em todas as janelas:** 60d → 30d → 7d → hoje registra subida sequencial: 26,6 → 28,5 → 34,9 → 45 pedidos/dia. O movimento não é spike isolado — o próprio 7d já está acima do 30d, que já está acima do 60d. Todas as janelas confirmam o mesmo vetor.
- **Ticket estável ao longo do tempo:** R$ 40,04 (30d) → R$ 40,15 (60d) → R$ 40,88 (hoje). O crescimento de GMV é inteiramente puxado por volume, não por mix ou preço. Isso torna o ganho mais robusto e mais dependente de manutenção de tráfego.
- **Mesmos dias da semana mostram tendência ascendente estruturada:** 22 → 24 → 33 → 29 → 45 pedidos ao longo dos últimos cinco ciclos. A queda pontual para 29 em 11/05 não inverteu a trajetória — hoje bate novo teto histórico neste dia da semana.
- **Janela de 7d já absorve dias recentes:** a média de 34,9 pedidos/dia na última semana é +22% sobre os 30d. Se esse nível se sustenta, o patamar do mês corrente será significativamente superior ao bimestre anterior — mas com apenas 7 dias observáveis sem tese semanal consolidada, isso ainda é hipótese em construção.

---

### Leitura estratégica

- **O ganho de patamar está na trajetória, não no dia.** O dia de hoje é expressivo, mas o sinal mais relevante é que o 7d já estava elevado antes dele. A conta não subiu ontem — vem subindo de forma consistente ao longo das últimas semanas. O dia confirma e amplifica um movimento já estabelecido nas janelas anteriores.
- **Crescimento de volume sem ancoragem em segundo vetor é vulnerabilidade latente.** O ticket estável valida que o crescimento é orgânico em volume, não distorção de mix. Porém, os dois produtos líderes — Conjunto 5 Potes Tampa Preta e Jarra Medidora 500ml — concentram ~53% dos pedidos. A família IMB501 sozinha (preto + cinza) responde por 33% do volume. O restante do catálogo fragmenta os outros 47% entre oito produtos, nenhum acima de 7%. A conta não tem segundo vetor consolidado — depende de dois ASINs para sustentar o patamar atual.
- **FBA 100% é condição de base, não mérito do dia.** A operação está inteiramente em FBA, o que sustenta elegibilidade e Buy Box para o tráfego pago coordenado por Pedro. Nenhum dado de Buy Box está disponível no pacote — não é possível afirmar que a exposição dos ASINs líderes está saudável, apenas que o fulfillment está estruturado. Qualquer degradação de Buy Box nos dois produtos dominantes teria impacto desproporcional no patamar.
- **A escalada de ADS ainda não é indicada sem confirmação de Buy Box.** O crescimento observado pode refletir otimização de ADS em andamento ou melhora orgânica de ranking. Sem Buy Box disponível e sem tese semanal consolidada anterior, recomendar escalada seria antecipar conclusão que os dados não sustentam — o pré-requisito das rules.md se aplica integralmente.

---

### Tese da conta

**Em ganho de patamar** — com confiança moderada, condicionada à continuidade da semana. A consistência da aceleração em 7d, 30d e 60d, reforçada pela tendência ascendente nos mesmos dias da semana ao longo de cinco ciclos, sustenta que a conta mudou de faixa operacional, não que teve um dia excepcional dentro de um patamar estável. O ticket plano ao longo de todo o histórico reforça que o ganho é estrutural em volume. A ressalva é que sem weekly/monthly consolidados, essa tese ainda é baseada exclusivamente nas janelas quantitativas — ela precisa de confirmação nos próximos 3 a 5 dias para ser tratada como consolidada.

---

### Risco estrutural principal

- **Risco:** Dependência de dois ASINs (Conjunto 5 Potes Tampa Preta + Jarra Medidora 500ml) para ~53% do volume, sem segundo vetor consolidado no catálogo.
- **Por que importa:** O patamar atual — 34,9 pedidos/dia na última semana — não se sustenta se esses dois produtos perderem Buy Box, tiverem ruptura de estoque FBA ou caírem em ranking. O restante do catálogo (8 produtos fragmentando 47% do volume) não tem capacidade de absorção. Uma falha nos líderes não é correção, é colapso de patamar.
- **Histórico:** Sem memória anterior disponível, não é possível afirmar se essa concentração é padrão crônico ou recente. É a primeira leitura estruturada da conta via DSA.
- **Sinal de confirmação:** Concentração dos top 2 acima de 50% por mais dois ciclos semanais consecutivos confirma que a dependência é estrutural, não acidente do dia; perda de Buy Box em IMB501P ou CK4742 (se disponível no pacote) por 2 dias seguidos ativa o risco imediatamente.

---

### Sinais a observar

1. **Média 7d mantida acima de 33 pedidos/dia ao final desta semana** — se a janela de 7d se sustentar no novo patamar após absorver os dias seguintes, o ganho deixa de ser hipótese e passa a ser tese consolidada. Se regredir para abaixo de 30, o dia de hoje foi pico, não novo nível.

2. **Próximo mesmo dia da semana (2026-05-25) acima de 35 pedidos** — a série dos mesmos dias mostra 22 → 24 → 33 → 29 → 45; um próximo ponto acima de 35 confirma tendência ascendente estruturada no ciclo semanal; abaixo de 29 indica que o teto de hoje foi exceção.

3. **Concentração dos top 2 (IMB501P + CK4742) acima de 50% por dois dias consecutivos** — confirma dependência estrutural como padrão e não como resultado do dia; se Buy Box desses ASINs estiver disponível no pacote em dias futuros, monitorar abaixo de 80% como sinal de fragilidade operacional.