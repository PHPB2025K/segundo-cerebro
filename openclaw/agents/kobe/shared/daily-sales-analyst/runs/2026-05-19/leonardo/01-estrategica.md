<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` são templates sem nenhuma entrada real — memória analítica está em estágio zero. Não há hipóteses ativas, tese semanal ou mensal acumulada para confirmar ou refutar; hoje inaugura o registro interpretativo da conta. As janelas históricas numéricas (7d/30d/60d/mesmos dias) estão disponíveis e são confiáveis — a limitação é contexto, não dado.

---

### Leitura temporal

- **60d → 30d → 7d em progressão ascendente:** médias de 26,8 → 29,4 → 36,4 pedidos/dia mostram aceleração consistente em múltiplas janelas — não é ruído de um ponto isolado. O 7d (36,4) já estava materialmente acima do 30d (29,4) antes de hoje.
- **Hoje é outlier mesmo dentro da tendência:** 67 pedidos contra avg de mesmos dias da semana de 29,5 (e o melhor desses pares foi 41 em 05/05). A magnitude de 2,3× acima do melhor par histórico é anômala — indica que algo além da tendência operou hoje.
- **Ticket comprimiu em todas as janelas:** R$36,91 hoje vs R$39,92 (30d) e R$40,44 (60d). O crescimento de volume não foi neutro em mix — veio com erosão de ticket de -7,5% a -8,7%, sugerindo que o canal de entrada ou o mix de produto hoje é diferente do padrão histórico.
- **Sem memória histórica:** não há hipóteses ativas para confirmar, enfraquecer ou refutar. A leitura de hoje é ponto de partida, não confirmação de tese.

---

### Leitura estratégica

- A progressão multi-janela (60d→30d→7d) separa o movimento de um evento isolado — quando três janelas convergem na mesma direção, o sinal tem peso maior do que um único dia forte. Mas a magnitude de hoje exorbita essa tendência: 67 pedidos em uma segunda-feira cuja banda dos últimos 4 pares era 23–41. Isso ou representa um salto de patamar genuíno que o 7d ainda não capturou inteiro, ou é pico de uma causa específica que não se sustenta.
- A família IMB501 (variações Preta, Cinza, Vermelha) concentrou ~57% dos pedidos, com IMB501P sozinho em ~45% (30 de 67). O segundo produto (CK4742, Jarra Medidora) representou 18%. A cauda existe mas é rasa. Isso significa que qualquer fragilidade de estoque, Buy Box ou FBA no IMB501P converte diretamente em queda de GMV sem amortecimento — a conta não tem segundo vetor que absorva choque.
- Os 13 cancelamentos (~16% sobre pedidos válidos) são número absoluto elevado para um dia. Em volume anômalo como hoje, cancelamentos altos podem indicar pressão de estoque, problemas de listing ou compras de teste — sem baseline histórica de cancelamentos, não é possível classificar como evento ou padrão, mas o dado é o mais preocupante da sessão.
- A compressão de ticket (-7,5% vs 30d, -8,7% vs 60d) em um dia de volume muito acima do normal sugere que o crescimento veio de um mix mais barato ou de um mecanismo (ADS, promoção, visibilidade pontual) que atrai volume de menor valor médio. Se o volume se consolida com esse ticket, o GMV cresce menos do que os pedidos — diferença relevante para a tese de patamar.

---

### Tese da conta

**Inconclusiva com sinal positivo multi-janela.** A progressão 60d→30d→7d é consistentemente ascendente e sugere que a conta está em processo de ganho de patamar — mas a magnitude de hoje é anômala demais para ser absorvida pela tendência sem confirmação adicional. A ausência de memória semanal e mensal impede distinguir se o movimento da semana passada (já refletido no 7d elevado) é consolidação ou flutuação. A tese hoje é: *há sinal real de aceleração, mas insuficiente para classificar como ganho estrutural confirmado*. Os próximos 3–5 dias determinarão se hoje foi marco de novo patamar ou outlier.

---

### Risco estrutural principal

- **Risco:** Hiperdependência da família IMB501 (especialmente IMB501P) sem segundo vetor estrutural de sustentação.
- **Por que importa:** Com ~57% dos pedidos concentrados em uma família de produto e o segundo ASIN respondendo por apenas 18%, qualquer instabilidade de estoque, Buy Box ou FBA nos ASINs IMB501 compromete diretamente a base de GMV sem amortecimento. Em dia de volume muito acima do normal, esse risco é amplificado — se o pico foi puxado pelos IMB501, a conta está mais exposta do que parece.
- **Histórico:** Sem memória histórica preexistente, não é possível afirmar se essa concentração é padrão crônico ou recente. Registrado hoje como dado inaugural — relevante exatamente por isso: a primeira leitura já aponta para dependência estrutural.
- **Sinal de confirmação:** Concentração dos top 3 acima de 65% por dois ciclos semanais consecutivos confirmaria dependência crônica, não evento de um dia forte.

---

### Sinais a observar

1. **Pedidos abaixo de 40 por 3 dias seguidos** a partir de amanhã confirma que hoje foi pico não sustentado e a 7d avg retorna para a banda de 30d — tese de ganho de patamar seria refutada.
2. **Taxa de cancelamento acima de 10% em 2 dos próximos 5 dias** (cancelamentos/pedidos válidos) confirma padrão operacional recorrente — não evento de volume anômalo.
3. **Ticket médio abaixo de R$37 por 3 dias consecutivos** confirma erosão de mix estrutural: crescimento de volume às custas de margens por pedido menores, o que altera a leitura de qualidade do GMV mesmo se os pedidos se sustentam.