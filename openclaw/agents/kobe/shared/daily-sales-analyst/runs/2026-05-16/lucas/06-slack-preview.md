<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 16/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Consolidado: 99 pedidos — R$ 4.976,92 — ticket médio R$ 50,27 — 1 cancelamento
- Budamix Store: 57 pedidos — R$ 2.353,85
- Budamix Oficial (Conta 2): 22 pedidos — R$ 1.582,54 — 1 cancelamento
- Budamix Shop (Conta 3): 20 pedidos — R$ 1.040,53

🏆 TOP PRODUTOS SHOPEE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 31 pedidos
- Jarra Medidora de Vidro 500ml (Store) — 11 pedidos
- Kit 6 Canecas Tulipa 250ml — 11 pedidos
- Kit 2 Potes de Vidro 800ml Quadrado — 9 pedidos
- Kit 4 Potes de Vidro 800ml Quadrado — 8 pedidos
- Kit 6 Canecas Retas 200ml (Conta 3) — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 5 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A queda de patamar Shopee é transversal (-30% a -40% vs 30d em todas as três contas), mas não é uniforme — a Oficial 2 opera sob lógica própria com ticket em expansão (+20% vs 30d) enquanto Store e Shop 3 deterioram em volume sem compensação, e o total de 99 pedidos nas três contas hoje era o que a Store sozinha fazia em média há 60 dias. O risco concreto não é a queda em si, é a estrutura por trás dela: a Store sustenta 58% dos pedidos da plataforma num único produto (Conjunto 5 Potes Redondos Tampa Preta, 54% da conta), a Shop 3 comprime ticket e volume simultaneamente sem janela de recuperação fora do horário comercial, e só a Oficial 2 oferece sinal divergente — se esse sinal não se confirmar amanhã, a plataforma perde seu único vetor positivo.

🟠 *Budamix Store (Shopee 1):* A Store parece estável vs 7d (-1,8% GMV), mas essa estabilidade é ilusória — sem o Conjunto 5 Potes Redondos Tampa Preta (31 dos 57 pedidos), a conta teria 26 pedidos no dia, abaixo de qualquer sábado recente, com uma cauda de 7 produtos em 1 pedido cada que não sustenta nada. A consequência operacional é direta: qualquer perda de posição orgânica do campeão derruba o GMV da conta e arrasta o agregado da plataforma sem sinal de aviso, porque não existe segundo vetor para absorver o impacto.

🟠 *Budamix Oficial (Shopee 2):* A Oficial 2 é o único vetor positivo da plataforma no dia — ticket de R$ 71,93 contra média 7d de R$ 60,02, GMV +21,4% vs 7d, com Kit 4 Potes de Vidro 800ml Quadrado liderando com 7 pedidos e mix concentrado em produtos mais caros. A progressão de ticket nas janelas (60d R$ 53 → 30d R$ 60 → hoje R$ 72) sugere mix shift gradual e não evento pontual, mas com 22 pedidos e 1 cancelamento no dia, o sinal ainda é frágil — se o padrão não se confirmar em 2 dias consecutivos, a leitura divergente não sustenta.

🟠 *Budamix Shop (Shopee 3):* A Shop 3 deteriora duplamente — volume -38,5% vs 60d e ticket comprimindo para R$ 52 contra média histórica de R$ 65-67 — sem nenhum mecanismo interno de compensação. O agravante identificado no detalhamento do dia é estrutural: a conta operou em apenas 8 horas (10h–19h), sem nenhum pedido fora dessa janela, o que significa que mesmo num dia de demanda noturna ativa na Store, a Shop 3 não captura nada — a deterioração não é só de magnitude, é de cobertura, e isso limita qualquer recuperação diária por definição.

🎯 PRIORIDADES DO DIA
- Lucas: verificar posição orgânica do Conjunto 5 Potes Redondos Tampa Preta na Budamix Store hoje (17/05). Se produto fora do top 3 da categoria, acionar Himmel para investigar ADS Store. Se posição preservada, a causa da queda não é exposição e não se mexe em ADS.
- Lucas: acompanhar Oficial 2 em 17-18/05 com foco em ticket e GMV. Se GMV acima de R$ 1.500,00 e ticket acima de R$ 65,00 por 2 dias consecutivos, confirma trajetória divergente — separar a conta das outras duas na leitura de plataforma e não arrastar pela tese de queda geral.
- Lucas: não acionar Himmel para nenhuma das três contas hoje sem antes confirmar o sinal da Store — em queda de patamar de 60d sem causa identificada, aumentar verba antes de entender o mecanismo arrisca amplificar deterioração em vez de reverter.
- Lucas: monitorar cancelamento da Oficial 2 nos próximos 2 dias — 1 cancelamento em 22 pedidos representa ~4,5% de taxa. Se repetir, avaliar produto e padrão antes de qualquer escalonamento.

Dia analisado: 16/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: produto associado ao cancelamento da Oficial 2
- Origem do bloqueio: Condensadora
- Motivo: dado indisponível — produto do cancelamento não identificável com o pacote atual
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem; menção ao cancelamento restrita ao dado objetivo (1 ocorrência confirmada em 22 pedidos)
- Aparece na mensagem final: não nominalmente; aparece como fato quantitativo na VISÃO e como item de monitoramento em PRIORIDADES

- Item bloqueado: causa dos pedidos da Budamix Store às 0h e 2h (campanha, cupom ou orgânico)
- Origem do bloqueio: Condensadora
- Motivo: dado indisponível — origem do pedido não distinguível com o pacote atual
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem; distribuição horária não mencionada
- Aparece na mensagem final: não

- Item bloqueado: ITEM:57356981475 (Store, 1 pedido, sem raw_sku, confidence medium)
- Origem do bloqueio: Condensadora / Granular
- Motivo: ausência de raw_sku, confidence medium, volume de 1 pedido — não é evidência primária
- Agregado autorizado: não
- Tratamento aplicado: omitido do ranking de Top Produtos
- Aparece na mensagem final: não

- Item bloqueado: SKU 096 com padrão cross-conta (Conta 2 e Conta 3, 1 pedido cada, mapeamento genérico)
- Origem do bloqueio: Condensadora / Granular
- Motivo: mapeamento raw_sku_normalized_with_short_title_fallback em duas contas, confidence medium, risco de agregação incorreta
- Agregado autorizado: não
- Tratamento aplicado: omitido do ranking de Top Produtos (volume de 1 pedido por conta também abaixo do corte)
- Aparece na mensagem final: não

- Item bloqueado: produtos de cauda da Store com confidence medium — RED01B, KIT6S100, FITA500M, CNCOL (1 pedido cada)
- Origem do bloqueio: Condensadora
- Motivo: confidence medium, mapeamento genérico, 1 pedido cada — não são evidência primária de padrão
- Agregado autorizado: não
- Tratamento aplicado: omitidos do ranking de Top Produtos
- Aparece na mensagem final: não

- Item bloqueado: hipótese de causa da janela estreita da Shop 3 (ADS, orgânico, perfil de audiência)
- Origem do bloqueio: Condensadora
- Motivo: hipótese não confirmável com os dados disponíveis
- Agregado autorizado: não
- Tratamento aplicado: mencionado apenas o fato confirmado (conta operou em 8 horas, 10h–19h), sem atribuição de causa
- Aparece na mensagem final: apenas o fato; causa omitida

---

### Decisões de formatação

- Remoção de referência interna "pela Granular" → substituído por "no detalhamento do dia" — regra de linguagem externa clara
- Substituição de SKU cru "IMB501P" por "Conjunto 5 Potes Redondos Tampa Preta" nos textos da análise — proibição de SKU cru visível
- Substituição de SKU cru "KIT4YW800SQ" por "Kit 4 Potes de Vidro 800ml Quadrado" na análise da Oficial 2 — mesma regra
- Adição de espaço entre "R$" e valor em todos os textos da análise e prioridades ("R$71,93" → "R$ 71,93") — padrão numérico obrigatório
- Cabeçalho da seção de análise escrito como "ANÁLISE DAS CONTAS" (não "ANÁLISE DA CONTA") — addendum 7.6, 6B presente com 3 contas
- Indicação de conta para Conjunto 5 Potes Tampa Preta (Store) e Jarra Medidora 500ml (Store): venderam em apenas 1 conta
- Indicação de conta para Kit 6 Canecas Retas 200ml (Conta 3): vendeu em apenas 1 conta
- Indicação de conta para Conjunto 5 Potes Tampa Cinza (Conta 2): vendeu em apenas 1 conta
- Sem indicação de conta para Kit 6 Canecas Tulipa 250ml, Kit 2 Potes 800ml Quadrado, Kit 4 Potes 800ml Quadrado: cada um vendeu em 2 ou mais contas
- Sem faturamento por produto em Top Produtos: pacote não traz receita validada por variação — proibição de estimativa
- Ranking Top Produtos consolidado cross-conta por variação vendável: IMB501P 31 (Store), CK4742 11 (Store), CTL002 11 (cross), KIT2YW800SQ 9 (cross), KIT4YW800SQ 8 (cross), KIT6CAR200 5 (Conta 3), IMB501C 5 (Conta 2); corte em 5 pedidos consolidados
- Cancelamento da Oficial 2 (1 ocorrência) incluído na linha da conta na VISÃO como dado objetivo — dado disponível no pacote, relevante pelo peso percentual (4,5%)
- Prioridades formatadas com "Lucas:" prefixando cada bullet — destinatário único para Shopee; sem escalonamento para Himmel/Kobe adicionado além do que veio da 6B