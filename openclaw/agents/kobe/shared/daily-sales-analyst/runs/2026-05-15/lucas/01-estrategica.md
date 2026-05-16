<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Memory das três contas está em estado inicial: weekly.md e monthly.md são templates vazios, sem tese semanal ou mensal registrada, sem hipóteses ativas, sem padrões documentados. Não há histórico de leituras diárias anteriores disponível — esta é a primeira entrada analítica estruturada para todas as três contas. As janelas numéricas (7d, 30d, 60d, mesmos dias da semana) estão disponíveis e são a única base histórica confiável. Teses abaixo são pontos de partida, não confirmações.

---

### Leitura temporal

**Budamix Store (conta principal)**
- Nos 60 dias, a conta operou em patamar médio de 98.7 pedidos e R$3.663/dia. Nos 30d caiu para 85.1 pedidos e R$3.297. Nos 7d recuou mais ainda para 62.6 pedidos — mas GMV subiu para R$2.317, sinal de ticket ascendente. Hoje, 66 pedidos com GMV R$3.172 e ticket R$48 (vs R$37-38 histórico): volume ainda deprimido vs bimestre, mas ticket em alta consistente em todas as janelas (+24% vs 30d, +29.5% vs 60d).
- Vs mesmos dias da semana (4 quintas-feiras): média de 84.75 pedidos e R$3.469. Hoje está 22% abaixo em pedidos, 8.6% abaixo em GMV — mas o mesmo dia de 08/05 teve apenas 75 pedidos e R$2.506, e 24/04 teve 72 pedidos. 01/05 (feriado) distorce a média para cima. Excluindo o feriado, a conta está dentro da faixa dos últimos dois ciclos normais.
- **Hipótese anterior:** nenhuma (memória vazia). Hoje estabelece baseline.

**Budamix Oficial-2**
- Nos 60d, média de 37 pedidos e R$1.964/dia. Nos 30d, 31.9 pedidos e R$1.907. Nos 7d, 25.1 pedidos e R$1.450. Hoje: 17 pedidos, R$1.248 — deterioração consistente e progressiva em todas as janelas, não apenas hoje.
- Vs mesmos dias da semana: 26 → 33 → 43 → 39 (cronológico inverso: 17/04 → 24/04 → 01/05 → 08/05). Hoje, 17 — abaixo do menor patamar registrado nessa série. Sinal relevante: o menor ponto anterior era a quinta-feira de 17/04 (26 pedidos); hoje ficou abaixo disso.
- Flag de readiness confirmado: conta fora da banda de 30d (-46.7%), classificada como "partial". Os dados são íntegros — o volume é real, não artefato.

**Budamix Shop-3**
- Nos 60d, média de 32.8 pedidos e R$2.133/dia. Nos 30d, 27 pedidos e R$1.840. Hoje: 27 pedidos, R$1.556, ticket R$57.65. Pedidos empatam exatamente com 30d (0%), mas GMV está -15.4% — o ticket caiu vs 30d (-15.4%) e vs 60d (-11.3%).
- Vs mesmos dias da semana: 22 → 22 → 36 → 19 (17/04 → 24/04 → 01/05 → 08/05). Hoje, 27 — acima da média simples de 24.75. Em pedidos, a conta performa bem hoje. O problema é o GMV (-15.2% vs mesma série), confirmando drift de ticket, não de volume.

---

### Leitura estratégica

- **Store sustenta a plataforma pelo ticket, não pelo volume.** A queda de volume é consistente ao longo das janelas (33% vs 60d, 22% vs 30d), mas o ticket compensou progressivamente. O que segura o GMV não é força de venda — é mix deslocado para produtos de maior valor (Conjunto 5 Potes Redondos domina com 30 pedidos, seguido de Jarra Medidora com 23). Isso torna a conta ao mesmo tempo mais eficiente por transação e mais frágil: qualquer interrupção nos dois campeões derruba volume e GMV simultaneamente, sem cauda para absorver.

- **Oficial-2 mostra deterioração progressiva, não evento pontual.** A sequência 7d → 30d → 60d revela declínio consistente em pedidos; hoje está abaixo até da janela de 7d e abaixo de todos os mesmos dias da semana registrados. O ticket elevado (+38% vs 60d) compensa parcialmente, mas a queda de volume em todas as janelas sugere erosão de exposição ou tráfego — hipótese, não fato, dado ausência de memória anterior.

- **Shop-3 tem estabilidade de pedidos e erosão de valor.** O padrão aqui é invertido: volume em linha com 30d, mas ticket e GMV em queda vs 60d. O mix atual concentra canecas de porcelana (Tulipa + Reta) em vez de potes hermético de maior valor. Se esse drift de mix persistir, a conta perde receita por pedido de forma silenciosa — os números de volume mascaram a deterioração financeira.

- **As três contas não se movem juntas — o sinal não é de Shopee, é de contas individuais.** Store está em acomodação de volume com ticket elevado. Oficial-2 está em trajetória de queda progressiva. Shop-3 está estável em volume mas com drift de GMV. Tratar o agregado de R$5.976 como "Shopee" seria perder o problema.

---

### Tese da conta

**Budamix Store — vulnerável.** A conta mantém GMV próximo da média de 30d via ticket elevado, mas a trajetória de volume é descendente ao longo do bimestre e a dependência dos dois produtos campeões (Potes Redondos + Jarra Medidora, ~80% dos pedidos) é extrema e crônica. Não há segundo vetor visível. A conta opera saudável no número superficial e frágil na estrutura — qualquer choque nesses dois produtos não tem amortecedor.

**Budamix Oficial-2 — em queda real.** A deterioração é observável em todas as janelas temporais disponíveis (7d, 30d, 60d, mesmos dias da semana), não é evento pontual. Hoje representa o piso de todos os registros comparáveis. A memória está vazia, impossibilitando verificar se há causa conhecida. Tese de queda real, com grau de confiança moderado — escalona para alto se próximos dias confirmarem o padrão.

**Budamix Shop-3 — vulnerável.** Pedidos estáveis, mas mix derivando para produtos de menor valor. A conta aparece saudável em volume enquanto o GMV por pedido erode silenciosamente. Não é queda real ainda — mas é vulnerabilidade estrutural se o drift de ticket não se reverter.

---

### Risco estrutural principal

**Conta: Budamix Store**

- **Risco:** Dependência extrema em dois produtos (Conjunto 5 Potes Redondos Tampa Preta e Jarra Medidora 500ml) que concentram ~80% dos pedidos, sem segundo vetor identificado na cauda. Top 5 representa 100% dos pedidos do dia — a conta não tem cauda real.
- **Por que importa:** Qualquer interrupção nesses dois produtos — ruptura de estoque, queda de ranking/exposição na Shopee, aumento de competitividade de concorrentes, desativação de cupom ou ADS — coloca o GMV da conta inteira em risco imediato, sem absorção pela cauda.
- **Histórico:** Memória vazia — impossível determinar se este é padrão histórico ou concentração recente. A concentração de 92.4% nos top 3 é flaggeada pelo sistema. Dado que a memória está sendo inaugurada hoje, este é o primeiro registro formal do risco.
- **Sinal de confirmação:** Concentração dos top 2 produtos acima de 75% dos pedidos por 3 ciclos consecutivos (dentro da semana) confirma que a dependência é estrutural e não pontual.

---

### Sinais a observar

1. **Oficial-2:** Pedidos abaixo de 25 por 2 dias seguidos confirma que a queda de hoje não é ruído e a conta entrou em trajetória de deterioração real; pedidos acima de 30 nos próximos 2 dias refuta a tese e enquadra como oscilação severa pontual.

2. **Shop-3:** GMV abaixo de R$1.600 com pedidos acima de 25 por 3 das próximas 5 sessões confirma drift de mix estrutural (volume mantido, valor por pedido em erosão progressiva); ticket acima de R$65 por 2 dias seguidos reverte a hipótese.

3. **Store:** Conjuntos 5 Potes Redondos + Jarra Medidora representando mais de 70% dos pedidos pelo segundo ciclo semanal consecutivo confirma dependência estrutural nos campeões e eleva o risco de concentração de crítico observado para crítico documentado.