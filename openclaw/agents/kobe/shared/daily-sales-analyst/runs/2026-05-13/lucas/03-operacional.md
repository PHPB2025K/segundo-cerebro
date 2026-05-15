<!-- llm_used=true model=sonnet fallback=false -->
### Leitura operacional do dia

- C2 (Budamix Oficial) não operou com volume baixo — operou degradada. 13 pedidos com distribuição horária esparsa (nenhuma janela com mais de 3 pedidos, 8 horas de atividade sem formação de pico) é padrão de conta sem tração de exposição, não de dia fraco. Confirma o risco dominante identificado pela Estratégica e reforça a hipótese tática de campanha inativa ou exposição suprimida: conta operante com visibilidade normal gera concentração horária mesmo em dias fracos; C2 não gerou.

- C1 (Budamix Store) executou abaixo do patamar histórico de volume, mas o mix do dia favoreceu produtos de maior valor — ticket R$43,80 vs média histórica de R$35-38 amorteceu a queda de GMV. Isso é exatamente o padrão de mascaramento que a Estratégica sinalizou: o resultado de GMV de C1 parece dentro de uma banda aceitável, mas está sendo sustentado por composição de mix, não por força de volume. A dependência de 90% nos top 3 (Jarra Medidora 500ml + Potes Vidro Redondos + Canecas Tulipa) confirma operacionalmente o padrão de concentração apontado pela Estratégica — a conta performou, mas com margem mínima para absorver variação nos dois produtos campeão.

- C3 (Budamix Shop) entregou volume próximo ao mesmo dia da semana histórico (-1,6%), mas o GMV ficou 19% abaixo dessa referência — R$58,94 de ticket contra R$71,75 da média de mesmos dias da semana. Operacionalmente, a divergência entre pedidos e receita por pedido é concreta e consistente em múltiplas janelas (30d, 60d, mesmos dias da semana), adicionando evidência operacional à hipótese tática de compressão de ticket em C3.

- O resultado consolidado de R$5.964 é sustentado por C1 (55% do GMV), com C2 praticamente ausente e C3 perdendo receita por pedido mesmo com volume sustentado. A aparência de número razoável no agregado mascara três contas com trajetórias distintas e todas com vetores de risco ativos — nenhuma das três executou um dia operacionalmente saudável.

---

### Sinais operacionais relevantes

- **Sinal:** C2 apresentou distribuição horária completamente esparsa — 8 horas com 1 a 3 pedidos cada, sem formação de janela de pico em nenhum horário — **interpretação operacional:** contas operantes com visibilidade normal, mesmo em dias fracos, tendem a concentrar pedidos em horários específicos (manhã ou noite); ausência total de concentração horária em C2 é sinal de exposição muito reduzida ou campanha inativa, não variação de demanda.

- **Sinal:** C2 registrou 3 cancelamentos em 13 pedidos (~19% de taxa de cancelamento intradiária) — **interpretação operacional:** taxa atípica que, combinada com volume em colapso, sugere que os poucos pedidos que chegaram também estão sendo perdidos; pode indicar produto específico com indisponibilidade ou problema de listing, ou falha mais abrangente na conta que compromete tanto exposição quanto conversão.

- **Sinal:** C1 concentrou ~74% dos itens vendidos em dois produtos (Jarra Medidora 500ml com 31 unidades e Potes Vidro Redondos com 26 unidades) dentro de um total de 80 itens — **interpretação operacional:** a conta operou estruturalmente apoiada em dois SKUs; o ticket elevado de hoje pode ser consequência direta da composição desses produtos no mix — qualquer oscilação neles impacta GMV total de C1 de forma imediata, confirmando o padrão de dependência apontado pela Estratégica.

- **Sinal:** C3 manteve volume (-1,6% vs mesmo dia da semana) enquanto o GMV por pedido caiu ~R$13 em relação à referência histórica de mesmos dias da semana — **interpretação operacional:** não é oscilação casual; é padrão recorrente observável em 30d, 60d e mesmos dias da semana simultaneamente, o que aponta para mix se deslocando para produtos de menor valor unitário ou aumento de cupons/descontos na conta, adicionando evidência operacional à hipótese tática de compressão de ticket.

- **Sinal:** Perfis de distribuição horária são distintos entre C1 e C3: C1 concentra em 09h-16h (bloco de manhã-tarde), C3 distribui mais uniformemente com atividade em madrugada e picos em 12h e 20h-22h — **interpretação operacional:** as contas têm bases de comprador e comportamento de exposição independentes; análise agregada das três contas perderia esse sinal e poderia mascarar problema localizado.

---

### Anomalias ou ausência de anomalia

**Anomalia crítica** — localizada em C2 (Budamix Oficial).

O que sustenta: C2 apresentou colapso de volume consistente em todas as janelas temporais disponíveis (-55% vs 7d, -63% vs 30d, -66% vs 60d, -59% vs mesmo dia da semana), distribuição horária esparsa sem formação de pico em nenhum horário, e taxa de cancelamento de ~19% nos poucos pedidos que chegaram. Esse conjunto operacional — volume abaixo de qualquer banda histórica + ausência de padrão horário + cancelamentos elevados — não é desvio pontual; é funcionamento degradado da conta. O sistema de qualidade já flagou C2 como "partial confidence" por volume fora da banda normal. C1 e C3 apresentam anomalia leve a moderada (desaceleração de volume e compressão de ticket, respectivamente), mas sem comprometimento de execução do mesmo nível de C2. Para descer de nível em C2, seria necessário identificar causa pontual (ex.: evento externo de dia) e ver recuperação rápida para a banda histórica nos próximos 1-2 dias. Para subir de nível, C2 manter-se abaixo de 20 pedidos por mais um dia sem causa identificada confirmaria deterioração estrutural.

---

### O que precisa ser investigado pela Granular

- **Pergunta:** Os 3 cancelamentos de C2 estão concentrados em qual produto ou têm origens distintas? — **motivada por:** taxa de cancelamento de ~19% em C2, muito acima das outras contas; se concentrados em um produto, o problema é de listing/estoque específico; se pulverizados, aponta falha mais sistêmica na conta.

- **Pergunta:** Em C2, houve alguma janela horária com mais de 3 pedidos consecutivos, ou a distribuição foi completamente esparsa ao longo de todo o dia? — **motivada por:** sinal de distribuição horária de C2 sem formação de pico identificável; entender se houve algum intervalo de atividade normal pode indicar se havia campanha rodando parcialmente ou se a conta ficou sem exposição o dia todo.

- **Pergunta:** O ticket elevado de C1 (R$43,80) é sustentado por pedidos com Jarra Medidora 500ml e Potes Redondos em quantidades maiores por pedido, ou por compra de kits de maior valor (ex.: KIT6S097 ou KIT4YW800SQ)? — **motivada por:** leitura de que o ticket mais alto de C1 é amortecedor temporário de mix, não recuperação de demanda; entender qual mecanismo está gerando o ticket elevado é necessário para avaliar se o amortecedor vai se sustentar ou colapsar nos próximos dias.

- **Pergunta:** O Kit 6 Canecas Porcelana 200ml (produto líder de C3 com 12 vendas) tem qual faixa de preço praticada em C3 comparado ao histórico desse SKU na conta? — **motivada por:** produto líder de C3 respondendo por ~39% dos itens vendidos pode ser o principal vetor de compressão de ticket se estiver sendo vendido com cupom ou desconto, o que explicaria operacionalmente a divergência entre volume estável e GMV em queda.

---

### Destaque para a Condensadora

O fato operacional dominante do dia é que C2 (Budamix Oficial) não teve um dia fraco — teve um dia de funcionamento degradado. A distribuição horária esparsa sem formação de pico em nenhuma janela, combinada com taxa de cancelamento de ~19% nos poucos pedidos que chegaram, é padrão operacional de conta sem exposição, não de conta com demanda baixa. Isso confirma e quantifica operacionalmente o risco dominante que a Estratégica apontou como inaugural e a Tática colocou como prioridade de investigação. O risco que pode passar despercebido na Condensadora: o número consolidado de R$5.964 é razoável à primeira vista, mas está sendo carregado por C1 usando ticket como amortecedor e por C3 entregando volume mas perdendo receita por pedido — a plataforma está em equilíbrio frágil, e C2 em colapso por dois dias seguidos sem causa identificada comprometeria esse equilíbrio de forma visível no GMV consolidado.