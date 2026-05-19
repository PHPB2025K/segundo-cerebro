<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

Memória vazia nas três contas — weekly.md, monthly.md e rules.md são templates sem conteúdo histórico preenchido. Não há hipóteses ativas, teses anteriores ou padrões documentados para confirmar ou refutar. Todas as janelas temporais (7d, 30d, 60d, mesmos dias da semana) estão tecnicamente disponíveis nos dados, mas sem âncora de memória para contextualizar o que é padrão estabelecido versus comportamento novo. A tese produzida aqui é **ponto de partida**, não confirmação de nada.

---

### Leitura temporal

- **Conta 1 (Budamix Store) — comportamento misto:** ontem (59 pedidos, R$2.497) ficou -6% vs 7d em volume, mas dentro de uma banda que já vinha comprimida — 7d está em 62,6 pedidos/dia contra 80,8 do 30d e 94,6 do 60d. A desaceleração não é de ontem: o patamar de 7d já está ~22% abaixo do 30d e ~34% abaixo do 60d. O ticket subiu consistentemente nessa queda (R$37,66 → R$39,01 → R$41,49), o que sugere mix se estreitando em torno de produtos de maior valor unitário, não recuperação orgânica.

- **Conta 2 (Budamix Oficial / Conta 2) — anomalia de ticket vs volume:** ontem 16 pedidos com ticket de R$98,14, contra média 7d de R$61,91 e 30d de R$60,05. O volume despencou (-47% vs 30d, -53% vs mesmo dia da semana), mas o GMV caiu menos (-13% vs 30d) por efeito de ticket. Esse padrão — poucos pedidos com ticket elevado — é a primeira aparição documentada: pode ser ruído de mix (um ou dois pedidos de kits maiores puxando o ticket) ou sinal de que o tráfego de volume secou e sobrou apenas compra de ticket alto. Sem histórico para distinguir.

- **Conta 3 (Budamix Shop) — colapso de volume consistente em todas as janelas:** -58,5% vs 7d, -65,9% vs 30d, -62,1% vs mesmo dia da semana. O 7d já estava deprimido (21,7 pedidos/dia vs 26,4 do 30d e 31,8 do 60d), e ontem foi pior ainda: 9 pedidos. Não é evento pontual — a queda está presente em todas as comparações. O ticket subiu (+15,8% vs 30d), seguindo o mesmo padrão das outras contas, mas com volume tão baixo a conta está operando em nível residual.

- **Plataforma consolidada (84 pedidos, R$4.768):** a soma das três contas indica que Store concentrou 70% dos pedidos. Conta 2 e Conta 3 juntas respondem por 30% do volume mas com ticket médio mais elevado. O enfraquecimento não é uniforme — Store cai menos em termos relativos e ainda carrega o volume; Conta 3 é a que mais comprime.

---

### Leitura estratégica

- **A desaceleração das três contas é consistente e simultânea, o que reduz a hipótese de problema isolado.** Quando Store, Conta 2 e Conta 3 caem juntas em volume — e todas em relação ao 30d e 60d — o sinal mais provável é algum fator transversal: exposição geral da Budamix na Shopee (ADS, cupons, posição orgânica) ou ciclo de demanda. Sem memória histórica, não dá para saber se esse padrão de queda simultânea é recorrente ou inédito.

- **O ticket médio subindo consistentemente enquanto o volume cai é um sinal ambíguo.** Pode indicar que ADS e/ou cupons estão sendo reduzidos (menos tráfego de entrada, menor ticket médio de aquisição), que o mix está sendo filtrado naturalmente para produtos premium, ou que está havendo estreitamento da cauda — restam pedidos de maior valor mas os de menor valor secaram. Sem dado de ADS/exposição no pacote, a causa permanece hipótese.

- **A Conta 3 opera em nível que começa a ser estruturalmente irrelevante.** 9 pedidos num dia contra média 30d de 26,4 não é variação — é colapso de patamar. Se a 7d já estava em 21,7 (também deprimida vs 30d e 60d), isso sugere que a queda da Conta 3 tem pelo menos 1-2 semanas de duração. Uma conta de 3 dígitos de pedidos/mês com ticket médio de R$77 gera GMV marginal; o risco é que ela está consumindo atenção operacional sem retorno proporcional.

- **Store ainda sustenta a plataforma, mas com dependência alta em dois produtos.** Top 3 concentrando 88,1% dos pedidos — Conjunto 5 Potes de Vidro Redondos (27 pedidos) e Jarra Medidora 500ml (18 pedidos) respondem sozinhos por 76% do volume da conta. Qualquer oscilação nesses dois produtos move o resultado total da conta.

---

### Tese da conta

**Plataforma Shopee: vulnerável — saudável no número de ontem, frágil na estrutura e na trajetória.**

O canal não está em colapso agudo, mas a leitura de 30d vs 60d nas três contas mostra desaceleração que já não é de curto prazo. Store ainda sustenta volume; Conta 2 sustenta GMV por ticket; Conta 3 está em queda real de patamar. A plataforma como um todo opera abaixo do patamar de bimestre em volume e GMV, compensada parcialmente por ticket crescente — mecanismo que tem limite. Como não há memória histórica preenchida, não é possível confirmar se esse é um padrão sazonal recorrente ou deterioração real; a tese é **vulnerável** com ressalva de base fraca.

---

### Risco estrutural principal

- **Risco:** Dependência da plataforma Shopee concentrada na Conta 1 (Store) e, dentro dela, em dois produtos (Conjunto 5 Potes Redondos + Jarra Medidora 500ml), sem segundo vetor identificado em nenhuma das três contas.
- **Por que importa:** Se os dois produtos-âncora da Store sofrerem qualquer oscilação — queda de exposição, ruptura de estoque, competidor com preço mais agressivo — o GMV da plataforma Shopee cai de forma diretamente proporcional e sem amortecimento. Conta 2 e Conta 3 não têm volume para compensar.
- **Histórico:** Não há registro anterior — esta é a primeira leitura documentada. Não é possível afirmar se é padrão crônico ou novo.
- **Sinal de confirmação:** Se Conjunto 5 Potes Redondos (Store) registrar menos de 15 pedidos por dia em 3 dos próximos 5 dias, a dependência estrutural deixa de ser hipótese e passa a ser vulnerabilidade confirmada e ativa.

---

### Sinais a observar

1. **Conta 3 (Budamix Shop) abaixo de 15 pedidos pelo segundo ciclo semanal consecutivo confirma que a queda não é evento — é perda de patamar estrutural** que justifica reavaliação da viabilidade operacional da conta.

2. **Ticket médio da Conta 2 (Budamix Oficial) acima de R$90 por mais de 3 dias seguidos, com volume abaixo de 20 pedidos/dia, confirma que o volume barato secou** e o que resta é compra de kit — sinal de mix estreitando, não de recuperação.

3. **Volume consolidado da Shopee abaixo de 70 pedidos/dia por 3 dias seguidos indica que a Store também perdeu patamar** — hoje ela ainda segura; se ceder, o suporte da plataforma desaparece (exposição ADS Himmel deve ser verificada via Lucas se esse sinal aparecer).