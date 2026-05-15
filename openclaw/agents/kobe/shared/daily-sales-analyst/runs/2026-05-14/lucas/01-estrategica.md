<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly.md e monthly.md das três contas são templates vazios — sem teses, hipóteses ou padrões históricos registrados. Não há hipóteses ativas anteriores para confirmar ou refutar. Último daily disponível: 2026-05-12 (lacuna de um dia sem registro). A memória operacional desta análise parte do zero. Volumes de Conta 1 e Conta 2 foram marcados como `partial` pelo sistema de data readiness; no entanto, a normalidade de Conta 3 (status `ok`) sugere que os números refletem performance real — não falha de coleta.

---

### Leitura temporal

- **Conta 1 (Budamix Store) — deterioração em todas as janelas:** A trajetória 60d (102 pedidos/dia de média) → 30d (88) → 7d (69) → hoje (35) é uma curva descendente documentada em três janelas independentes. O dia não é outlier que retorna — é a continuação de um declínio gradual. O ponto de hoje está abaixo do menor comparável das últimas quatro quartas (75 pedidos em 23/04), ou seja, está fora do intervalo histórico de sazonalidade semanal.

- **Conta 2 (Budamix Oficial) — queda de volume com elevação de ticket:** Mesma trajetória descendente em pedidos (60d: 38 → 30d: 34 → 7d: 27 → hoje: 18), mas o ticket médio subiu +35% em relação ao 60d (R$71,66 vs R$52,80). O GMV cai menos do que o volume indicaria isoladamente — levanta hipótese de mix-shift para produtos de maior valor, não confirmada.

- **Conta 3 (Budamix Shop) — dentro do padrão:** Queda de volume existe (60d: 34 → 30d: 28 → 7d: 24 → hoje: 23), mas o ritmo é significativamente menor. O dia está dentro do intervalo das últimas quatro quartas (23–45 pedidos) e o GMV de hoje (R$1.769) supera a média de 7d (R$1.513). É a única conta operando dentro das expectativas históricas.

- **Fraqueza concentrada, não sistêmica:** Conta 1 e Conta 2 concentram toda a deterioração. Conta 3 se comporta normalmente. Isso rejeita a hipótese de evento amplo de plataforma Shopee e aponta para dinâmica interna específica das duas maiores contas por volume histórico.

---

### Leitura estratégica

- **A queda de Conta 1 não é evento de um dia.** A degradação de 102 pedidos de média (60d) para 35 hoje é observável em 60d, 30d e 7d — três janelas convergindo na mesma direção. Com concentração extrema nos dois produtos campeões (~86% dos itens), a conta não tem segundo vetor que absorva erosão de exposição. Qualquer enfraquecimento dos campeões — por posição de anúncio, concorrência de preço ou mudança de algoritmo — se traduz diretamente em colapso do GMV, sem alternativa de sustentação.

- **Conta 2 exibe um padrão estruturalmente diferente de Conta 1.** Menos pedidos, ticket mais alto, GMV relativamente sustentado. Se o ticket elevado for mix-shift real (clientes comprando kits maiores, menor volume de entrada com maior valor por pedido), a conta pode estar se especializando — e a queda de volume é menos preocupante do que o número bruto sugere. Se for apenas perda de tráfego de menor valor, a leitura muda. A hipótese não tem evidência de mais de um ponto ainda.

- **Conta 3 é o único vetor estável da plataforma neste ciclo.** O GMV acima da média de 7d com ticket elevado (+14% vs 30d) sugere que esta conta pode estar ganhando participação relativa — ou que simplesmente não está sofrendo a mesma erosão das outras. Com memória vazia, não é possível distinguir tendência de flutuação.

- **O sinal agregado da plataforma é de encolhimento real liderado por Conta 1 e Conta 2**, com Conta 3 isolando parte do impacto. A ausência de cancelamentos é positiva operacionalmente, mas não altera a leitura de volume.

---

### Tese da conta

**Plataforma Shopee — vulnerável**, com leitura diferenciada por conta. Conta 1 (Store): **em queda real** — deterioração documentada em 60d, 30d e 7d, com o dia abaixo do mínimo histórico de quartas; sem segundo vetor estrutural. Conta 2 (Oficial): **inconclusiva** — volume em queda consistente, mas ticket subindo de forma que muda o diagnóstico dependendo da causa; hipótese de mix-shift com um único ponto de evidência ainda não é confirmação. Conta 3 (Shop): **em acomodação** — dentro da banda histórica, desempenho relativo superior às outras contas. A fraqueza da plataforma não é distribuída uniformemente — está concentrada nas duas contas com maior volume histórico, o que aumenta a relevância do risco. A memória vazia impede qualquer leitura sobre se essa queda de Conta 1 é nova ou aceleração de padrão já conhecido.

---

### Risco estrutural principal

- **Risco:** Conta 1 (Store) sustentada por dois produtos (Jarra Medidora de Vidro e Potes de Vidro Redondos) que respondem por ~86% dos itens vendidos, em trajetória de declínio de volume que atravessa 60d, 30d e 7d — sem segundo vetor identificado.
- **Por que importa:** A conta não tem diversificação que absorva oscilação nos campeões. Se a exposição ou relevância desses dois produtos enfraquecer — por posição de anúncio, concorrência de preço ou mudança de algoritmo —, o GMV da conta colapsa sem alternativa de sustentação interna. A combinação de dependência extrema com trajetória de declínio ativo é o cenário de risco mais crítico.
- **Histórico:** Memória vazia. Não é possível afirmar se este é risco novo ou padrão já documentado. Este diagnóstico é o ponto zero de registro para esta conta.
- **Sinal de confirmação:** Volume de Conta 1 abaixo de 50 pedidos em 3 dos próximos 5 dias confirma que a deterioração é estrutural e que o patamar histórico de 30d (88 pedidos/dia) foi perdido — não recuperável sem intervenção.

---

### Sinais a observar

1. **Conta 1 — teste de patamar:** GMV de Conta 1 abaixo de R$2.000 em mais 2 dos próximos 5 dias confirma perda de patamar (30d: R$3.422) — e transforma a leitura de hoje de ponto de queda em tendência com janela temporal estabelecida.

2. **Conta 2 — mix-shift ou perda de tráfego:** Ticket médio de Conta 2 acima de R$65 por 3 dias consecutivos enquanto volume de pedidos permanece abaixo de 25 confirma a hipótese de mix-shift (menos pedidos, maior valor médio), mudando o diagnóstico de queda de patamar para acomodação em nível menor com qualidade superior.

3. **Conta 3 — segundo vetor emergente ou coincidência:** GMV de Conta 3 acima de R$1.700 em 3 dos próximos 5 dias indicaria que a conta está ganhando participação relativa dentro da plataforma — e potencialmente capturando demanda que Conta 1 não está convertendo.