<!-- llm_used=true model=sonnet fallback=false -->
### Decisão tática

- **Dado que a tese da Store é vulnerabilidade sustentada em todas as janelas (7d, 30d, 60d, mesmo dia da semana), a decisão correta é checar se a causa está no lado de exposição/ADS antes de qualquer ação forte** — proteger os campeões é prioridade, mas mexer em ADS sem causa confirmada pode amplificar o problema, não resolvê-lo.

- **Dado que a tese de Oficial-2 e Shop-3 é explicitamente inconclusiva por qualidade de dado (confiança parcial confirmada pelo runner), a postura correta é observação dirigida com checagem de completude de dado** — ação forte nestas duas contas antes de confirmar se o dado é real seria precipitada e potencialmente geraria resposta equivocada.

- **Dado que o risco estrutural principal é a dependência extrema da Store em dois campeões (top 3 = 88.1%, com dois produtos respondendo por ~76% dos pedidos), a proteção da exposição destes produtos é prioritária sobre qualquer teste de vetor secundário** — a base da conta é frágil para experimentação enquanto a queda não tiver causa identificada.

- **Dado que CTL002 aparece simultaneamente no topo das três contas, o risco de canibalização entre contas existe e não pode ser descartado** — qualquer ação de ADS ou promoção em uma conta que inclua CTL002 precisa ser considerada no contexto das outras duas, não isoladamente.

---

### O que fazer hoje

- **Lucas:** observar GMV da Store pelos próximos 2 dias com referência no sinal definido pela Estratégica (R$2.200 como piso de alerta) — tese é vulnerabilidade sustentada, e o dia hoje (R$2.497) está na fronteira da erosão de patamar; acompanhar com condição explícita evita confundir acomodação com aprofundamento do problema — se GMV cair abaixo de R$2.200 por 2 dias consecutivos, Lucas alinha com Himmel sobre exposição e ADS dos campeões da Store; se manter acima, mantém observação sem mexer.

- **Lucas:** checar se os dados de Oficial-2 e Shop-3 têm indicação interna de incompletude para o dia 18/05 (sincronização pendente, janela de corte, atraso de integração) — o runner sinalizou confiança parcial para as duas contas, e distinguir dado incompleto de queda real é a checagem que desbloqueará o diagnóstico correto — se dado confirmado como completo, queda de Oficial-2 e Shop-3 é real e exige investigação de exposição; se dado incompleto, aguardar próximo ciclo antes de qualquer movimento.

- **Lucas:** verificar se a exposição dos produtos campeões da Store (Conjunto 5 Potes Redondos e Jarra Medidora) está normal nos painéis de listagem — a tese é que a queda pode estar no lado de exposição/ADS, e checar visibilidade destes dois produtos antes de acionar Himmel é o passo mínimo que evita escalar sem diagnóstico — se exposição normal, hipótese se desloca para demanda ou preço; se exposição reduzida ou anúncios inativos, Lucas alinha com Himmel imediatamente.

---

### O que NÃO fazer ainda

- **Não acionar Himmel para aumentar verba ou alterar configuração de ADS em nenhuma das três contas com base nos dados de hoje** — a tese da Store é vulnerabilidade, mas a causa não está confirmada (exposição? ADS? demanda? mix?); sem causa identificada, aumentar verba pode queimar budget em posição que não converte, e a memória das contas é zero — não há histórico para saber se ADS já foi testada como resposta e com qual resultado.

- **Não tomar nenhuma decisão de mix, promoção ou exposição em Oficial-2 e Shop-3 com base no dado de hoje** — as duas contas têm confiança parcial confirmada e tese inconclusiva; qualquer ação baseada neste dado teria mais chance de ser resposta a artefato do que a problema real; a postura correta é esperar confirmação de completude do dado e um segundo ciclo antes de qualquer movimento nestas contas.

- **Não expandir CTL002 nem testar promoção cruzada deste produto entre as três contas simultaneamente** — CTL002 está nos tops das três contas ao mesmo tempo e o risco de canibalização entre elas é explícito na leitura estratégica; sem histórico de mix por conta, qualquer ação coordenada neste SKU pode redistribuir demanda entre contas sem gerar demanda incremental, mascarando o problema e tornando o diagnóstico ainda mais difícil.

---

### Escalonamento

**Observar** — responsável da conta (Lucas) coleta mais 1-2 ciclos antes de qualquer decisão de alinhamento com Himmel.

A tese da Store é vulnerabilidade sustentada, mas a causa não está identificada e a memória das contas parte do zero hoje. Oficial-2 e Shop-3 têm tese explicitamente inconclusiva por qualidade de dado. Neste conjunto, a postura correta é não alterar operação antes de ter ao menos um ciclo completo com dado confirmado e uma checagem de causa na Store. O escalonamento muda de nível se: (a) Lucas confirmar que o dado de Oficial-2 e Shop-3 está completo e ambas as contas mantiverem volume abaixo das referências da Estratégica por mais 2 dias — neste caso, sobe para **alinhar com Himmel** sobre exposição diferenciada por conta; ou (b) Store cair abaixo de R$2.200 de GMV por 2 dias consecutivos com exposição dos campeões normal — neste caso, Lucas alinha com Himmel sobre ADS da Store especificamente. Himmel nunca é acionado para as três contas ao mesmo tempo; cada eventual alinhamento trata uma conta, com diagnóstico fechado antes de escalar.