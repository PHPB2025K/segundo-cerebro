<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly.md e monthly.md são templates vazios — sem tese semanal ou mensal constituída. Não há hipóteses ativas para confirmar ou refutar. O último daily disponível é 2026-05-12 (dois dias de gap). Âncoras históricas existem nas janelas de 7d/30d/60d via dados estruturados, e rules.md está operacional. Base fraca para memória qualitativa — tese hoje serve como ponto de partida da série, não confirmação de tendência anterior.

---

### Leitura temporal

- **Tendência de base (7d > 30d > 60d):** As médias mostram escalonamento consistente: 60d em R$1.035/26 pedidos → 30d em R$1.107/27,6 → 7d em R$1.195/29,3. Antes do dia de ontem, a conta já vinha de trajetória de leve elevação de patamar — não estagnação.
- **Spike de 2026-05-14 vs todas as janelas:** 40 pedidos e R$2.085 de GMV representam +74% vs 7d, +88% vs 30d, +101% vs 60d, e +107% vs mesmas quartas-feiras. É resultado mais que dobra qualquer referência disponível — fora da banda esperada em qualquer janela.
- **Ticket médio elevado:** R$52,12 vs R$40,12 na média de 30d (+30%). O crescimento de GMV não foi só volume — o ticket subiu junto, o que sugere mix shift ou produto de ticket mais alto puxando a composição do dia.
- **Mesmos dias da semana:** As últimas 4 quartas oscilaram entre R$684 e R$1.225, com tendência de queda nas duas mais recentes (R$1.010 e R$1.099 vs R$1.225 em 23/04). Ontem inverteu e ultrapassou com folga o melhor ponto da série — não é confirmação de sazonalidade favorável, é exceção positiva dentro do ciclo semanal.

---

### Leitura estratégica

- **O dia de ontem é anomalia positiva, não confirmação de novo patamar.** A base já vinha em leve inclinação ascendente (7d > 30d > 60d), o que é sinal saudável — mas o salto de 2026-05-14 está fora da banda de qualquer janela histórica disponível. Um ponto excepcional dentro de série ainda não valida mudança estrutural de patamar.
- **O ticket elevado muda a leitura do GMV.** R$52/pedido vs R$40 de média de 30d sugere que o resultado não foi apenas mais pedidos — foi pedidos com mix diferente. A Jarra Medidora sozinha representou 16 dos 50 itens (32% dos itens vendidos) e, sendo produto de ticket presumivelmente maior, pode explicar parte significativa da elevação de ticket. Hipótese: a Jarra teve exposição ou promoção favorável no dia — não confirmado, não há dado de Buy Box ou posição de anúncio no pacote.
- **A concentração dos top produtos é fato estrutural já presente, não novidade.** Top 3 em 54%, top 5 em 70%, com Jarra Medidora em posição dominante. Sem historical de top products para comparar, não é possível afirmar se essa concentração aumentou ou é padrão crônico — mas a dependência de um ASIN campeão em 32% dos itens significa que qualquer oscilação da Jarra repercute diretamente no resultado da conta.
- **FBA 100% é positivo operacionalmente.** Toda operação via FBA elimina risco de fulfillment próprio e sustenta elegibilidade de Buy Box (dado não disponível no pacote para confirmação direta).

---

### Tese da conta

**Inconclusiva — momentum de base presente, spike não validado.**

A conta estava em leve ganho de patamar nos últimos 30-60d (7d > 30d > 60d em pedidos e GMV). Isso é sinal positivo de fundo. O resultado de 2026-05-14, porém, é um spike bem acima de qualquer banda histórica e não tem histórico de memória para contextualizar se é recorrente, sazonal ou excepcional. Sem hipóteses anteriores para confirmar e sem weekly/monthly constituídos, não há âncora qualitativa para interpretar o que causou o salto. A tese honesta é: conta em trajetória de base saudável, com um dia excepcional que precisa de ao menos 2-3 dias de sequência para indicar se há mudança de patamar ou se é ruído positivo isolado.

---

### Risco estrutural principal

**Risco:** Dependência de ASIN único campeão (Jarra Medidora) sem segundo vetor consolidado.

**Por que importa:** Com a Jarra representando ~32% dos itens do dia e top 3 em 54% de concentração, qualquer perda de Buy Box, queda de ranking, problema de estoque ou competição agressiva nesse ASIN tem impacto desproporcional no resultado da conta. O ticket elevado do dia reforça que parte do resultado financeiro também passa desproporcionalmente pelo campeão. Escalar ADS sobre essa estrutura sem validar Buy Box e estoque do ASIN líder amplifica vulnerabilidade em vez de resultado.

**Histórico:** Não há histórico qualitativo disponível (weekly/monthly são templates). Impossível afirmar se é padrão crônico ou recente — trata-se do primeiro ponto de registro.

**Sinal de confirmação:** Jarra Medidora abaixo de 8-10 unidades em 2 dos próximos 5 dias, com GMV da conta retornando para banda de 30d (abaixo de R$1.300), confirmaria que o dia de ontem foi exceção sustentada pelo campeão e que a dependência estrutural é real.

---

### Sinais a observar

1. **GMV acima de R$1.500 por 3 dias consecutivos nos próximos 7 dias** confirmaria que há ganho real de patamar e não apenas spike isolado — caso contrário, resultado retorna à banda e a leitura é de ruído positivo.

2. **Ticket médio acima de R$48 por 3 dias seguidos** confirmaria que o mix shift (produtos de maior valor puxando composição) é tendência estrutural e não artefato do dia — se o ticket retornar para R$40-42, o dia de ontem foi exceção de mix, não mudança de comportamento do canal.

3. **Jarra Medidora com menos de 8 unidades em 2 dos próximos 5 dias, coincidindo com queda de GMV abaixo de R$1.200**, confirmaria dependência estrutural do ASIN campeão e sinal de que o resultado de ontem não é replicável sem o volume específico desse produto (verificar estoque FBA e Buy Box disponível no pacote, se disponível).