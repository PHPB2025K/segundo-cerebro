### Qualidade da base

Memória limitada: não há saída anterior diária nem weekly.md ou monthly.md nesta entrega; a análise depende integralmente das informações temporais fornecidas no pacote validado. As janelas de 30d, 60d e pares de dias da semana estão presentes, viabilizando uma leitura de contexto, porém com baixa granularidade interpretativa sem teses em memória. Base suficiente para diagnóstico da trajetória de patamar, mas sem histórico de hipótese ativa.

---

### Leitura temporal

- A conta opera com queda relevante tanto no GMV quanto em pedidos válidos nas três comparações principais: -37,6% (30d), -39,4% (60d) e -42,7% (mesmos dias da semana) em GMV; em pedidos, a queda é ainda maior (até -58,1% vs 60d e -57,0% vs pares semanais).
- O ticket médio se destaca como contrapeso — está 30,5% acima do patamar de 30 dias e 44,7% acima do patamar de 60 dias, sugerindo que a queda de volume foi parcialmente compensada por vendas de ticket mais alto.
- Concentração dos top 3 produtos está em 62,5% dos pedidos, indicando padrão de dependência alta, porém não extrema (acima de 70% seria crítica para as janelas analisadas). Não há indício no pacote se este nível subiu ou já era recorrente.
- Cancelamentos (2 de 16) estão em padrão administrável, sem histórico fornecido para avaliar recorrência.

---

### Leitura estratégica

- O cenário atual não é ruído pontual: os recuos de pedidos e GMV estão presentes em todas as janelas analisáveis (30d, 60d, variabilidade sazonal), apontando para um provável movimento de acomodação/queda estrutural, e não apenas oscilação natural.
- O ticket médio elevado indica que a perda de volume ocorre na cauda ou em itens de menor valor, ou que clientes restantes têm comportamento diverso. Isso pode ser efeito de mix involuntariamente afunilado — hipótese, já que o dado disponível sobre concentração fortalece (mas não comprova isoladamente) esse viés.
- A dependência dos campeões (top 3 acima de 60%) mantém a vulnerabilidade histórica desse tipo de conta: ainda sem um segundo vetor claro, segue exposta a qualquer oscilação dos líderes.
- Não há memória ou hipótese testada suficiente para afirmar deterioração operacional, mas a falta de reação em pedidos em todas as janelas temporais reforça que não há, por enquanto, reversão do quadro de queda.

---

### Tese da conta

A Budamix Oficial encontra-se **em queda real**, sustentando recuo de volume e faturamento em todas as janelas relevantes (30, 60 dias e mesmos dias da semana), parcialmente mascarado por um ticket médio atipicamente alto no ciclo mais recente. A concentração nos produtos campeões permanece relevante, reiterando vulnerabilidade estrutural já comum nesse tipo de operação, sem evidência de novo vetor de saúde ou reversão de tendência com os dados disponíveis.

---

### Risco estrutural principal

- **Risco:** Dependência elevada de poucos produtos líderes sem segundo vetor consistente.
- **Por que importa:** Expõe a conta a volatilidade excessiva caso algum campeão perca tração, sofra ruptura de estoque, canibalização, ajuste de preço adverso ou mudança de regra pelo marketplace, limitando resiliência e dificultando recuperação em contextos de queda.
- **Histórico:** Não foi possível identificar se houve agravamento ou se o patamar de concentração aumentou, mas a evidência atual confirma manutenção histórica do padrão de risco para o segmento.
- **Sinal de confirmação:** Concentração dos três líderes acima de 60% por mais um ciclo semanal, acompanhada de ausência de crescimento relevante no volume dos produtos secundários, confirma que a vulnerabilidade é crônica e não pontual.

---

### Sinais a observar

1. **Concentração dos top 3 acima de 60% dos pedidos por dois ciclos semanais consecutivos confirma manutenção do risco estrutural.**
2. **Pedidos válidos permanecendo mais de 40% abaixo da média de 30 dias no fechamento do próximo ciclo semanal reforça tese de queda real e não ruído pontual.**
3. **Ticket médio acima de 25% do histórico de 60 dias, sem recuperação do volume de pedidos, sinaliza afunilamento persistente do mix (foco involuntário em tickets altos ao invés de diversificação).**
