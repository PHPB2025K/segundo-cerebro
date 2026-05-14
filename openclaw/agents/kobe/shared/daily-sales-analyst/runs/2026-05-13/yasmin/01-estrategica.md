<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` contêm apenas templates sem dados preenchidos — a memória analítica desta conta é vazia. Nenhuma hipótese anterior está registrada para confirmar, enfraquecer ou refutar. O que existe são dados numéricos brutos das janelas históricas (7d, 30d, 60d, mesmos dias da semana). **A tese de hoje é ponto de partida, não confirmação.**

---

### Leitura temporal

- **60d vs 30d:** A média de 30d (R$ 4.095 / 99,6 pedidos) supera significativamente a de 60d (R$ 3.428 / 81,7 pedidos), indicando que abril teve período de patamar elevado — provavelmente relacionado ao ciclo pré/pós-Páscoa. Isso contamina o 30d como referência de "normal": a conta não está apenas abaixo da média do mês, está abaixo de um patamar atipicamente alto.

- **7d vs 60d:** O sinal mais relevante é que a média de 7d (R$ 3.258 / 77,1 pedidos) já está **abaixo do patamar de 60d** — não é apenas que hoje foi fraco; a última semana como um todo ficou abaixo da linha de dois meses. Isso não é ruído de um dia.

- **Série de terças:** Os quatro últimos referentes mostram 208 → 84 → 134 → 87 → **65 hoje**. O pico de 15/04 (208 pedidos) tem perfil de evento promocional isolado. Descartado o outlier, a série funcional é 134 → 87 → 65 — três pontos consecutivos em declínio, com distância crescente entre eles.

- **Ticket:** Consistentemente acima de todo o histórico — +11,6% vs 30d, +9,4% vs 60d. A divergência ticket ↑ / volume ↓ é persistente, não pontual.

---

### Leitura estratégica

- **O 30d não é o patamar real da conta.** Abril inflou a média com pelo menos dois eventos de alto volume (15/04 e 29/04). A referência operacional honesta é o patamar de 60d — e contra ele, os pedidos de ontem estão 20% abaixo e o 7d como bloco já rompe esse piso. A conta não está "abaixo do mês"; ela está saindo do patamar de bimestre.

- **A série de terças é o sinal mais limpo disponível.** Três terças consecutivas em queda consistente (134 → 87 → 65) controla a sazonalidade e elimina o argumento de "dia fraco". O movimento é grande o suficiente e direcional o suficiente para não ser ruído — mas, sem hipóteses anteriores registradas, ainda não é possível identificar a causa (perda de exposição, ranking, mix, ADS, competitividade).

- **O ticket elevado é ambíguo — não é conforto, é sinal de alerta de mix.** Ticket acima da história enquanto volume cai sugere que os anúncios de menor valor estão perdendo volume desproporcional. O mix está se concentrando nos produtos de maior ticket, o que pode refletir erosão de exposição na cauda ou mudança de mix deliberada — não dá pra distinguir sem dado de exposição/ranking.

- **A concentração em Potes de Vidro (3 variantes de cores = ~41% dos itens, família única) não tem segundo vetor claro registrado.** Canecas aparecem como segundo cluster mas com volume muito menor. Essa concentração significa que qualquer variação nos anúncios desta família impacta diretamente o resultado do dia.

---

### Tese da conta

**Vulnerável.** A conta opera abaixo do patamar de 60d em pedidos, com 7d já rompendo esse piso como bloco — não como ponto isolado. A série de terças confirma que o enfraquecimento não é sazonalidade de um dia; é trajetória de três ciclos. O ticket elevado mascara parcialmente a erosão de volume, mas não muda a direção. A memória vazia impede atribuir causa — a tese de vulnerabilidade é sustentada pela trajetória numérica, não por hipótese confirmada.

---

### Risco estrutural principal

- **Risco:** Erosão progressiva de volume em múltiplas janelas temporais, com ticket compensando parcialmente mas não estruturalmente. A conta perdeu mais de 20% dos pedidos contra seu próprio patamar de 60d, e o 7d confirma que o movimento já é da semana, não do dia.
- **Por que importa:** Ticket não escala indefinidamente — se a perda de volume continuar, o GMV vai seguir mesmo com ticket alto. A dependência no cluster Potes de Vidro significa que qualquer queda de exposição nessa família amplifica a perda.
- **Histórico:** Não há histórico registrado. Impossível saber se esse movimento é novo ou recorrente. Esse é o primeiro diagnóstico com base analítica.
- **Sinal de confirmação:** Terça seguinte (20/05) com pedidos abaixo de 75 confirmaria o terceiro ponto da série de queda como padrão consolidado, não variação.

---

### Sinais a observar

1. **Série de terças:** Pedidos abaixo de 75 em 20/05 confirma trajetória de queda estrutural na série semanal (seria o quarto ponto consecutivo em declínio). Acima de 90 enfraquece a tese.

2. **Divergência ticket/volume:** Se nos próximos 3 dias o ticket segurar acima de R$ 44 enquanto pedidos continuam abaixo de 75/dia, confirma que há concentração de mix — anúncios de menor valor perdendo volume desproporcional, hipótese de erosão de exposição na cauda ganha peso.

3. **Concentração dos top 3:** Se a concentração de top3 superar 50% por dois dias seguidos (vs 44,3% hoje), confirma estreitamento do mix e aumenta a vulnerabilidade estrutural ao desempenho de um único cluster de produto.