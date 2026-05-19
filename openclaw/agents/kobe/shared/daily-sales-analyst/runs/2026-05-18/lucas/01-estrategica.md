<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly.md e monthly.md das três contas são templates sem conteúdo preenchido — sem tese semanal acumulada, sem hipóteses ativas, sem riscos documentados de ciclos anteriores. Não há leituras diárias anteriores registradas na memória para confirmar ou refutar. As janelas de 7d/30d/60d e os mesmos dias da semana são as únicas âncoras disponíveis; todas estão presentes e internamente consistentes. A análise parte do zero em memória — teses formuladas hoje são pontos de partida, não confirmações.

---

### Leitura temporal

- **Store — desaceleração sustentada nas três janelas:** 7d médio (62,6 pedidos) já está bem abaixo do 30d (80,8) e do 60d (94,6). O dia de hoje (59) ficou levemente abaixo do próprio 7d, ou seja, a média de curto prazo já incorporou a tendência descendente. Os mesmos dias da semana nos últimos 4 oscilaram entre 54 e 103 (alta variância), mas a média dos pares é 81,5 — hoje ficou 27,6% abaixo disso. Ticket seguindo trajetória oposta: +12,4% vs 60d, o que amortece parcialmente a queda de GMV.

- **Oficial 2 — colapso de volume com inversão de ticket:** 7d (20,9) < 30d (30,2) < 60d (36,1) — mesma estrutura de declínio da Store. Hoje, com 15 pedidos, ficou abaixo do próprio 7d. O dado mais discrepante é o ticket: R$102,88 vs histórico de ~R$60-62, resultando em GMV +19,5% vs 7d apesar de muito menos pedidos. Hipótese: mix se deslocou para produtos de ticket mais alto no dia, não sustentado como tendência — dado insuficiente para concluir.

- **Shop 3 — fora da banda em todas as janelas:** 7d (21,7) < 30d (26,4) < 60d (31,8). Hoje, 9 pedidos, está abaixo do menor mesmo dia da semana dos últimos 4 (18 pedidos em 04/05). A data readiness classifica como "partial — outside both bands but above critical floor". O desvio é estruturalmente maior que os das outras duas contas e ultrapassa a variância esperada de sazonalidade semanal.

- **Padrão transversal — confirmado nas três contas:** 7d < 30d < 60d em pedidos aparece simultaneamente nas três contas. Isso não é ruído de um dia — é movimento acumulado no horizonte de curto e médio prazo do portfólio Shopee como um todo.

---

### Leitura estratégica

- **O portfólio Shopee está em queda de patamar, não em acomodação dentro de uma banda.** A estrutura 7d < 30d < 60d simultânea nas três contas indica que a queda não é sazonalidade nem variação pontual — o próprio horizonte de curto prazo já capturou o declínio. A Store ainda responde por ~71% dos pedidos e ~53% do GMV; enquanto ela declina mais devagar que as outras duas, o agregado depende dela para não colapsar.

- **Ticket em alta é amortecedor, não reversão.** Store (+12,4% vs 60d) e Oficial 2 (+92,4% vs 60d no dia) sustentam GMV parcialmente enquanto o volume cai. O risco é depender desse mecanismo: se o ticket parar de compensar (por pressão competitiva, mudança de mix ou redução de produto de alto valor), o GMV acompanha o volume para baixo. Em Oficial 2, o pico de ticket de hoje é um dado isolado — hipótese de mix shift pontual, não tendência confirmada.

- **Concentração extrema em poucos produtos numa trajetória de queda é combinação estruturalmente frágil.** Na Store, IMB501P (Conjunto 5 Potes de Vidro Redondos) e CK4742 (Jarra Medidora de Vidro) sozinhos respondem por ~76% dos pedidos do dia. Na Shop 3, top 5 = 100%. Qualquer oscilação dos campeões — por estoque, competitividade, exposição ou ADS — traduz diretamente em resultado da conta. Isso é padrão documentável hoje como linha de base, mas em cenário de declínio de volume, essa dependência amplia a vulnerabilidade.

- **Shop 3 levanta hipótese de deterioração de exposição ou ADS específica da conta.** O desvio de hoje (9 pedidos) extrapola a variância de sazonalidade semanal observada nos 4 pares — o mínimo histórico entre os pares era 18 pedidos. A hipótese mais provável (a ser verificada) é perda de exposição ou redução/interrupção de ADS nessa conta específica. A causa não é identificável com os dados disponíveis; precisa de verificação operacional com Himmel via Lucas.

---

### Tese da conta

**em queda real** — as três contas exibem simultaneamente a estrutura 7d < 30d < 60d em pedidos, o que configura um movimento sustentado, não ruído. A Store, que sustenta 71% do volume do portfólio, acumula queda de -37,6% em pedidos vs 60d. Oficial 2 e Shop 3 mostram quedas ainda mais acentuadas. O ticket em alta amortece o GMV mas não reverte a trajetória de volume. A ausência de memória acumulada impede saber se esse movimento já estava em curso antes do horizonte atual ou se é recente — isso é limitação da base, não da tese. Com os dados disponíveis, a classificação honesta é queda real de patamar no portfólio Shopee.

---

### Risco estrutural principal

- **Risco:** Concentração crítica nos campeões da Store (IMB501P + CK4742 com ~76% dos pedidos) numa conta que está em trajetória de queda de volume, sem segundo vetor identificado.
- **Por que importa:** Qualquer evento que afete os dois produtos líderes — ruptura de estoque, queda de exposição, perda de competitividade de preço, redução de ADS — se traduz diretamente em queda de GMV da conta principal, sem amortecedor. A Store responde por mais da metade do GMV do portfólio Shopee; fragilidade nela é fragilidade do canal.
- **Histórico:** Não há leituras anteriores registradas. Esta é a primeira observação documentada — não é possível afirmar se a concentração aumentou, se é padrão histórico estável ou se é nova. Registra-se como linha de base.
- **Sinal de confirmação:** Se nos próximos 3 dias os dois produtos líderes (IMB501P + CK4742) mantiverem individualmente menos de 40% dos pedidos da Store entre si, ou se o top3_concentration cair abaixo de 75%, há indício de diversificação. Se mantiver acima de 85% enquanto o volume total da conta segue abaixo de 65 pedidos/dia, o risco estrutural se confirma como persistente.

---

### Sinais a observar

1. **Queda de patamar da Store confirmada:** Se a média dos próximos 3 dias da Store ficar abaixo de 65 pedidos/dia, o 7d terá convergido para um novo patamar estrutural — não variância de dia da semana. A mesma lógica aplicada ao GMV: abaixo de R$2,600/dia em 3 dias consecutivos confirma o patamar, não oscilação.

2. **Ticket de Oficial 2 — pontual ou mix shift:** Se nos próximos 2 dias o ticket médio de Oficial 2 retornar para a faixa de R$55-70 (histórico 30d-60d), o pico de hoje (R$102,88) foi pontual. Se o ticket se mantiver acima de R$90 com volume de pedidos abaixo de 20, a hipótese de mix shift para produtos de alto ticket ganha peso e justifica investigação de quais produtos estão sustentando.

3. **Shop 3 — deterioração ou variação extrema:** Se Shop 3 registrar menos de 15 pedidos pelo segundo dia consecutivo, a conta entrou em deterioração real de exposição ou ADS — não variação de sazonalidade semanal. Nesse caso, acionamento de Himmel via Lucas para verificar status de ADS e listing da conta é justificado.