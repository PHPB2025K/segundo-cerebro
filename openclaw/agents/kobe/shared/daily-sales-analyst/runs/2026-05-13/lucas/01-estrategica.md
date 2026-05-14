<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Weekly, monthly e rules estão carregados para as 3 contas, mas são **templates vazios** — sem consolidação real, sem tese mensal documentada, sem hipóteses ativas registradas. Esta leitura serve como ponto de partida da memória, não como confirmação de tese. Todas as janelas temporais (7d, 30d, 60d, same weekday) estão disponíveis; Conta 2 tem flag PARTIAL por volume fora da banda (-62.9% vs avg30), com confiança reduzida para tese forte sobre essa conta. O spike de 22/04 na média de mesmo dia da semana (181 pedidos na Store, provável campanha) infla a comparação de same weekday para cima — queda aparente vs same weekday é parcialmente contaminada por esse outlier.

---

### Leitura temporal

- **Store (Conta 1) — dominante, 63% dos pedidos e 55% do GMV da plataforma:** acima da média dos últimos 7 dias em pedidos (+8.1%) e com GMV expressivamente acima (+34.6%), o que revela elevação de ticket (R$43.80 hoje vs avg7d R$35.15). Porém, ao expandir a janela, o quadro inverte: -17.4% em pedidos vs 30d e -27.7% vs 60d. O patamar de bimestre (média 103.7 pedidos/dia) está sendo entregue bem abaixo. O ticket sobe (+19.6% vs 60d), o que atenua o GMV, mas não reverte a queda de volume. Comparando as quartas-feiras anteriores: excluindo o outlier de 22/04 (181 pedidos), as 3 quartas restantes médiam ~85 pedidos — hoje com 75 estaria dentro de uma faixa aceitável, não em colapso.

- **Conta 2 — colapso em todas as janelas:** -55% vs 7d, -62.9% vs 30d, -66.4% vs 60d, -59.4% vs same weekday. É o sinal mais severo do dia. O ticket alto (R$65.57, acima do avg30 R$57.77) sugere que os poucos pedidos que entraram foram de produtos mais caros — mas o volume sumiu em magnitude que transcende variação normal. Dado o flag PARTIAL, a confiança é reduzida, mas a divergência entre essa conta e as outras duas não sustenta a hipótese de efeito de dado isolado.

- **Shop 3 — estabilidade de volume, compressão de ticket:** -1.6% vs same weekday em pedidos, mas -19.2% em GMV. O volume está essencialmente estável ao longo das quartas-feiras recentes (24/30/43/29 → hoje 31), mas o ticket caiu de R$71.75 (avg same weekday) para R$58.94. Vs 30d: pedidos levemente acima (+7.3%), GMV abaixo (-6.0%). Vs 60d: ambos abaixo. Mix se movendo para produtos de menor valor.

- **Hipóteses anteriores:** não há hipóteses documentadas para confirmar ou refutar — memória está vazia.

---

### Leitura estratégica

- **A Shopee como plataforma não pode ser lida como bloco.** A Store está em trajetória de queda de patamar de pedidos ao longo do bimestre (60d > 30d > semana recente), parcialmente mascarada pela elevação de ticket. A Shop 3 apresenta volume estável mas mix comprimido. A Conta 2 é um outlier de queda não explicado. Os três comportamentos são distintos — generalizá-los como "Shopee foi fraca" perde o diagnóstico.

- **A Store sustenta a plataforma com concentração estrutural perigosa.** Top 3 com 90% dos pedidos (Jarra 500ml, Conjunto 5 Potes, Canecas Tulipa) significa que qualquer oscilação nesses SKUs se transmite integralmente ao GMV da conta — e da plataforma. O ticket mais alto de hoje, que compensou parcialmente a queda de volume, pode refletir mix que favoreceu os produtos mais caros desse top 3, mas isso é hipótese sem dado de preço médio por SKU para confirmar.

- **A Conta 2 exibe sinal de deterioração consistente em todas as janelas temporais**, o que a separa de variação de dia da semana ou ruído pontual. Sem memória histórica preenchida, não é possível dizer se essa queda é nova ou vem se acumulando — o que é em si um dado preocupante: a conta entrou no pipeline de análise sem lastro histórico documentado.

- **A compressão de ticket na Shop 3 ao longo das quartas-feiras** (de R$71.75 avg para R$58.94 hoje) não é evento de um dia — o delta GMV vs same weekday (-19.2%) com volume estável (-1.6%) indica que o mix está consistentemente se movendo para produtos mais baratos. Se esse padrão continuar, o GMV da conta encolhe mesmo com volume mantido.

---

### Tese da conta

**Shopee — vulnerável.**

A plataforma entrega volume aceitável quando se compara com os últimos 7 dias, mas está em deterioração de patamar quando a janela se abre para 30d e 60d — e isso é consistente nas três contas, em graus diferentes. A Store (principal vetor) perde pedidos sistematicamente ao longo do bimestre enquanto o ticket sobe, sugerindo que o canal está se estreitando: vende menos, vende mais caro, mas o segundo vetor não existe. A Conta 2 apresenta colapso não explicado que precisaria de histórico documentado para ser classificado como estrutural ou transitório — e a ausência desse histórico é parte do problema. A tese de **vulnerável** (e não "em queda real") se sustenta porque a Store ainda não está abaixo do patamar de 7d e o GMV do dia ficou dentro de uma faixa razoável. Mas a estrutura de dependência e a trajetória de longo prazo apontam para fragilidade real, não conforto.

---

### Risco estrutural principal

**Risco:** Concentração crítica nos campeões da Store (top 3 = 90% dos pedidos) sem segundo vetor identificável, combinada com queda de volume no patamar de 30d e 60d.

**Por que importa:** Qualquer oscilação nos 3 SKUs líderes da Store — desabastecimento, perda de exposição, mudança de cupom/ADS ou aumento de concorrência — se transmite integralmente ao GMV da plataforma. Não há cauda longa que absorva o choque. O ticket mais alto hoje atenua temporariamente, mas não constrói resiliência.

**Histórico:** Sem memória preenchida, não é possível afirmar há quantas semanas esse padrão existe. A concentração de 90% no top 3 é o dado mais alto entre as três contas — indica que o mix nunca se diversificou ou que houve estreitamento recente. Inconclusivo sem histórico.

**Sinal de confirmação:** Top 3 da Store acima de 85% de concentração pelo segundo ciclo semanal consecutivo confirma dependência estrutural crônica, não evento de mix do dia.

---

### Sinais a observar

1. **Conta 2:** Volume abaixo de 20 pedidos por 3 dias seguidos nos próximos 5 dias confirma deterioração real de patamar — descarta hipótese de ruído de dado ou variação sazonal isolada e exige diagnóstico de exposição/ADS/mix via Lucas/Himmel.

2. **Store — ticket vs volume:** Ticket acima de R$42 com pedidos abaixo de 80 por 2 dias seguidos nos próximos 5 dias confirma a hipótese de estreitamento do mix — canal vendendo mais caro e menos, sem recuperação de volume base.

3. **Shop 3 — compressão de ticket:** GMV/pedido abaixo de R$60 por 3 das próximas 5 quartas-feiras confirma que o mix está se movendo estruturalmente para produtos de menor valor, e que a estabilidade de volume não está sustentando o faturamento.