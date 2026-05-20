<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- O GMV de R$5.790 ficou materialmente acima do padrão real da segunda-feira (excluindo o outlier de 28/04, a média do mesmo dia da semana é ~R$4.174) sem que o volume de pedidos tenha acelerado — 107 pedidos está próximo dos 99-106 registrados nas últimas segundas normais. O motor operacional do dia foi inteiramente o ticket (R$54,12 vs média 30d de R$43,42), e isso confirma ponto a ponto a leitura estratégica de que o crescimento de GMV está apoiado em mix/preço, não em expansão de demanda.

- A família IMB501 respondeu por ~49 pedidos do dia (~45,8%), com três variações no topo do ranking — confirmando o risco de dependência estrutural levantado pela Estratégica. Um detalhe operacional relevante: as variações Tampa Preta (32 pedidos) e Tampa Vermelha (10 pedidos) compartilham o mesmo anúncio (MLB3288536143), ou seja, 42 pedidos — ~39% do volume total — dependem de um único listing. A Estratégica calculou a concentração por variação; operacionalmente a exposição ao risco desse anúncio é maior do que o recorte por variação sugere.

- A distribuição horária apresentou dois picos funcionais: almoço (12h: 11 pedidos) e noturno (20h: 8 pedidos), com atividade consistente de manhã (9-10h: 15 pedidos combinados). Não há janela horária dominante nem buraco de tração perceptível — o dia se distribuiu de forma relativamente equilibrada para o canal.

- Os 6 cancelamentos (5,3% do total) são operacionalmente baixos em volume, mas sem informação sobre sua distribuição por produto ou anúncio não é possível afirmar se são ruído pulverizado ou concentração em produto específico — a Tática não os citou como pré-requisito, mas a Granular precisa verificar.

---

### Sinais operacionais relevantes

- **Sinal:** ticket R$54,12 (+20,5% vs 7d) com volume abaixo do 7d (-5,3%) — **interpretação operacional:** o dia operou com pedidos de maior valor unitário enquanto a frequência de compra ficou levemente pressionada; o GMV cresceu porque cada pedido valeu mais, não porque chegaram mais compradores; isso sustenta a leitura estratégica de motor de ticket, mas torna o resultado frágil a reversões de mix.

- **Sinal:** Tampa Preta e Tampa Vermelha (IMB501) compartilham o mesmo listing (MLB3288536143) e somaram 42 pedidos (~39% do volume) — **interpretação operacional:** a concentração real em um único anúncio é maior do que o recorte por variação indica; qualquer problema de ranking, visibilidade ou reputação nesse listing afeta dois dos três maiores produtos simultaneamente, amplificando o risco estrutural apontado pela Estratégica.

- **Sinal:** itens/pedido = 1,056 (113 itens para 107 pedidos) — **interpretação operacional:** quase todo pedido foi de item único, sem composição de cesta; o ticket elevado vem do preço do produto, não de cross-sell — o que confirma que uma reversão de mix (produto mais caro saindo menos) derrubaria ticket sem que cross-sell amortecesse.

- **Sinal:** fulfillment 100% "other" — sem ML Full — **interpretação operacional:** não há interferência logística de Full neste resultado; o dia não foi beneficiado nem limitado por visibilidade de Full, o que remove esse vetor de explicação tanto para o bom resultado quanto para eventual degradação futura.

- **Sinal:** concentração top5 em 61,7% dos pedidos com 10 produtos mapeados no topo — **interpretação operacional:** a cauda do catálogo contribui apenas com ~38% do volume em ~5+ produtos; o catálogo não tem segundo vetor de sustentação em escala suficiente para absorver queda dos líderes — adiciona evidência à hipótese tática de que Yasmin precisa estabelecer baseline dos anúncios líderes agora, enquanto a conta está saudável.

---

### Anomalias ou ausência de anomalia

**Sem anomalia relevante** — com ressalva de base narrativa semente.

O dia operou dentro do comportamento esperado para o canal: volume próximo ao padrão real das segundas-feiras, GMV acima sustentado por ticket, distribuição horária equilibrada, sem quality flags, reconciliação ok. Nenhuma dimensão operacional (volume, horário, fulfillment, cancelamentos em nível agregado) foge do padrão quantitativo disponível. A ressalva é que weekly e monthly são templates vazios — comparações com padrões narrativos anteriores (ex.: "ticket elevado já havia aparecido na semana passada?") não são possíveis. Isso não transforma o dia em anomalia, mas impede afirmar normalidade com confiança narrativa plena. Para subir de nível seria necessário cancelamentos concentrados em produto específico ou queda detectável em horário forte; para afirmar normalidade com confiança total, seria necessário ao menos 2 semanas de memória acumulada.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** os 6 cancelamentos estão concentrados em algum produto ou anúncio específico, ou são pulverizados entre diferentes SKUs? — **motivada por:** cancelamentos representam 5,3% dos pedidos e não foram qualificados operacionalmente; se concentrados no listing MLB3288536143 (IMB501P + IMB501V), o sinal muda de ruído para indicador de problema específico no anúncio mais crítico da conta.

- **Pergunta:** qual a posição atual (ranking e exposição) do anúncio MLB3288536143 no Mercado Livre comparada à semana anterior? — **motivada por:** esse único listing sustenta ~39% do volume do dia; a Tática indicou que Yasmin precisa estabelecer baseline de posição — mas operacionalmente o ponto de partida para esse baseline é justamente o anúncio que concentra Tampa Preta e Tampa Vermelha juntas, não as variações separadas.

- **Pergunta:** o ticket médio elevado (R$54,12) está distribuído entre diferentes produtos ou vem majoritariamente de um produto de preço unitário mais alto que vendeu mais hoje? — **motivada por:** itens/pedido de 1,056 indica ausência de cross-sell; se o ticket alto vem de um produto específico de maior valor unitário com desempenho acima do normal hoje, o sinal de "mix elevado" é mais frágil do que parece na média.

---

### Destaque para a Condensadora

O fato operacional mais importante do dia não é o GMV absoluto — é a estrutura que o sustenta: um único anúncio (MLB3288536143, Tampa Preta + Vermelha juntas) respondeu por ~39% do volume em uma conta onde o crescimento já depende de ticket, não de pedidos. Esse anúncio e o ticket são dois vetores que se reforçam mutuamente enquanto funcionam, mas que podem reverter simultaneamente sem aviso anterior — o volume não dará sinal antecipado porque está crescendo mais devagar. A Estratégica identificou a dependência por família; operacionalmente a dependência é por listing único, o que estreita ainda mais a margem. Isso não muda a tese de ganho de patamar, mas define o que a Condensadora deve chamar atenção para Yasmin: o trabalho desta semana é construir o baseline de posição desse anúncio específico antes que qualquer degradação apareça nos números.