<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 19/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: R$ 4.070,69 — 74 pedidos — ticket médio R$ 55,01 — 2 cancelamentos
• Budamix Store: R$ 2.120,16 — 45 pedidos
• Budamix Oficial (Conta 2): R$ 1.046,14 — 14 pedidos
• Budamix Shop (Conta 3): R$ 904,39 — 15 pedidos

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 20 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 14 pedidos
• Kit 6 Canecas Tulipa 250ml — 10 pedidos
• Kit 2 Potes de Vidro 800ml Quadrado — 8 pedidos
• Kit 6 Canecas Retas 200ml (Conta 3) — 6 pedidos
• Kit 3 Potes de Vidro Hermético (Conta 2) — 4 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 4 pedidos

🔍 ANÁLISE DAS CONTAS
⚫ *Consolidado (3 contas):* A plataforma Shopee operou em volume mínimo dos últimos 60 dias — 74 pedidos, pior ponto de todos os pares semanais recentes — mas a deterioração não é homogênea: Store e Oficial-2 têm ticket elevado amortecendo parcialmente o GMV (menos pedidos, compradores com intenção mais definida), enquanto Shop-3 caiu nos dois vetores simultaneamente, o que distingue os papéis das contas e impede leitura de bloco; a causa da queda — algoritmo, sazonalidade, exposição — permanece hipótese, e a postura correta é diagnosticar causa antes de qualquer ação.

🟠 *Budamix Store (Shopee 1):* Âncora da plataforma com 61% dos pedidos Shopee, mas operando sobre dois SKUs: IMB501P (Conjunto 5 Potes Redondos Tampa Preta) respondeu sozinho por 44,4% dos pedidos da conta (20/45) e CK4742 (Jarra Medidora 500ml) por mais 31% — juntos 75% da Store — o ticket mais alto (+20% vs 30d) atenua o GMV mas não muda o risco: qualquer pressão sobre disponibilidade ou posição desses dois produtos colapsa a conta âncora da plataforma sem nenhum amortecimento disponível.

🟠 *Budamix Oficial (Shopee 2):* Volume mínimo histórico (14 pedidos, abaixo de todos os pares semanais recentes), sustentando ticket de R$ 74,72 (+38% vs 60d) via perfil de compra de maior valor — KIT3S099 (Kit 3 Potes de Vidro Hermético) e IMB501C (Conjunto 5 Potes Redondos Tampa Cinza) empatados como co-líderes com 4 pedidos cada; o cancelamento de 1 pedido sobre 14 válidos (6,7%) é percentualmente relevante e merece monitoramento, pois em volume tão mínimo qualquer recorrência distorce a leitura operacional da conta sem aparecer no agregado da plataforma.

🟠 *Budamix Shop (Shopee 3):* A única das três em deterioração nos dois vetores simultaneamente — volume -46% vs mesmo dia da semana e ticket comprimido em R$ 60,29 (-10,7% vs 30d), sem o mecanismo de compensação das outras duas — co-líderes KIT6CAR200 (Kit 6 Canecas Retas 200ml) e KIT2YW800SQ (Kit 2 Potes de Vidro 800ml Quadrado) empatados com 6 pedidos cada respondem por 80% da conta, com padrão horário fortemente concentrado na manhã (10 dos 15 pedidos entre 6h-12h) e virtual ausência na tarde, indício não confirmado de perda de exposição localizada nessa janela.

🎯 PRIORIDADES DO DIA
• Lucas: verificar estoque e listing ativo de IMB501P e CK4742 na Store hoje. Com quase metade da conta principal da plataforma em um único SKU, indisponibilidade parcial explica parte da queda sem precisar de hipótese de algoritmo. Confirmar/refutar: se os dois líderes estiverem disponíveis com listing ativo, causa operacional básica descartada e hipótese de exposição ganha peso; se algum tiver ruptura ou problema de listing, diagnóstico definido e ação imediata clara. Escalar se: ruptura de estoque ou listing inativo confirmado — ação operacional imediata, sem necessidade de acionar Himmel.
• Lucas: acompanhar ticket médio da Shop-3 por mais 2 dias consecutivos. A Shop-3 é a única conta sem compensação de ticket, o que a distingue das outras duas. Confirmar/refutar: se ticket permanecer abaixo de R$ 60 com volume também abaixo de 19 pedidos, Shop-3 entra em leitura separada como deterioração mais profunda; se ticket se recuperar acima de R$ 60, o movimento é mais uniforme entre contas. Escalar se: queda dupla (volume + ticket) confirmada por 3 dias consecutivos — alinhar com Himmel sobre exposição específica da Shop-3 antes das outras contas.
• Lucas: monitorar pedidos da Store no bloco 19h-22h hoje e amanhã. É o termômetro mais sensível de exposição orgânica da plataforma. Confirmar/refutar: se o pico noturno não reagir por dois dias, hipótese de queda de exposição orgânica se consolida e abre acionamento de Himmel; se o pico se mantiver próximo ao padrão recente, o problema pode estar localizado em outros horários. Escalar se: Store sem reação no pico noturno por 2 dias — alinhamento com Himmel sobre ADS e exposição da conta.
• Não acionar Himmel para ajuste de ADS em nenhuma conta ainda — a causa da queda é hipótese, não fato confirmado; alterar segmentação ou verba antes de saber se o problema é de tráfego pago ou orgânico queima verba sobre causa que pode não responder a ADS.
• Não tratar as três contas como bloco para qualquer ajuste de configuração — Shop-3 tem dinâmica distinta das outras duas; mudanças simultâneas nas três contas impedem isolar causa e contaminam a leitura do que funciona.

Dia analisado: 19/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** KIT9S101 — Conjunto de 9 Potes de Vidro Retangulares (Store, 1 pedido)
  - Origem do bloqueio: Condensadora
  - Motivo: confidence medium (mapped_generic_sku / raw_sku_normalized_with_short_title_fallback); produto de cauda sem impacto na leitura central
  - Agregado autorizado: não
  - Tratamento aplicado: omitido de Top Produtos e de toda a mensagem
  - Aparece na mensagem final: não

- **Item bloqueado:** KIT6S100 — Kit 6 Potes de Vidro Hermético Retangular 4 Travas (Store, 1 pedido)
  - Origem do bloqueio: Condensadora
  - Motivo: confidence medium (mapped_generic_sku / raw_sku_normalized_with_short_title_fallback); produto de cauda sem impacto na leitura central
  - Agregado autorizado: não
  - Tratamento aplicado: omitido de Top Produtos e de toda a mensagem
  - Aparece na mensagem final: não

- **Item bloqueado:** produto associado ao cancelamento da Conta 2 (produto não identificável pelo pacote)
  - Origem do bloqueio: Condensadora
  - Motivo: produto do cancelamento não identificável pelo pacote de dados; citar produto seria afirmação sem base
  - Agregado autorizado: não
  - Tratamento aplicado: cancelamento da Conta 2 citado apenas como métrica percentual (1/14, 6,7%) sem associação a produto específico
  - Aparece na mensagem final: não nominalmente

- **Item bloqueado:** CTL002 descrito como "produto que funcionou" ou "destaque multiloja" sem menção ao risco de canibalização
  - Origem do bloqueio: Condensadora
  - Motivo: a leitura positiva sem o contexto de canibalização distorceria a mensagem; a evidência multiloja é real mas ambivalente
  - Agregado autorizado: não — CTL002 aparece em Top Produtos apenas com volume consolidado (10 pedidos), sem qualificação de destaque positivo
  - Tratamento aplicado: citado em Top Produtos como produto consolidado nas 3 contas; não qualificado como "destaque" nem como "risco" na mensagem
  - Aparece na mensagem final: sim, como item de ranking (10 pedidos, sem indicator de conta por ter vendido nas 3)

- **Item bloqueado:** afirmação de que a Shop-3 perdeu exposição na tarde como fato
  - Origem do bloqueio: Condensadora
  - Motivo: hipótese não confirmada por falta de dado horário histórico; não é possível afirmar se é novo desvio ou padrão habitual
  - Agregado autorizado: sim — linguagem de indício ("indício não confirmado de perda de exposição localizada nessa janela")
  - Tratamento aplicado: preservado o qualificador da 6B ("indício não confirmado") na análise da Conta 3
  - Aparece na mensagem final: sim, como indício com ressalva

- **Item bloqueado:** hipótese de causa da queda (algoritmo, sazonalidade, exposição) como fato
  - Origem do bloqueio: Condensadora
  - Motivo: todas as causas permanecem hipóteses; memória qualitativa vazia, sem dado de tráfego ou impressão
  - Agregado autorizado: sim — linguagem de hipótese explícita
  - Tratamento aplicado: todas as referências a causa mantêm "permanece hipótese" ou lista as possibilidades sem eleger uma
  - Aparece na mensagem final: sim, como hipótese com ressalva explícita

---

### Decisões de formatação

- `Título da seção 🔍 ajustado para ANÁLISE DAS CONTAS — fonte analítica obrigatória é a 6B, que sintetiza as 3 contas; addendum v3.1 exige título "ANÁLISE DAS CONTAS" quando 6B existe`
- `Análise das 4 contas preservada integralmente do 06b-shopee-consolidator — sem reescrita, apenas remoção do texto que estava em JSON e passagem para Markdown de Slack`
- `Top Produtos consolidados cross-conta para mesma variação vendável: CTL002 somado (5+3+2=10), KIT2YW800SQ somado (2+6=8) — mesma variação vendável em múltiplas contas consolidada conforme regra`
- `IMB501P e CK4742 com indicador de conta (Store) — venderam em apenas 1 conta`
- `KIT6CAR200 com indicador de conta (Conta 3) — vendeu em apenas 1 conta`
- `KIT3S099 e IMB501C com indicador de conta (Conta 2) — cada um vendeu em apenas 1 conta`
- `CTL002 sem indicador de conta — vendeu nas 3 contas`
- `KIT2YW800SQ sem indicador de conta — vendeu em 2 contas (Store e Conta 3); regra de indicar aplica-se apenas a menos de 2 contas`
- `KIT9S101 e KIT6S100 omitidos de Top Produtos — bloqueio Condensadora por confidence medium; 1 pedido cada, cauda sem impacto na leitura central`
- `Faturamento por produto omitido de Top Produtos — pacote não traz campo de receita validada por variação; formato aplicado: [nome] — [pedidos] pedidos`
- `Ranking ordenado decrescente por volume total consolidado: 20, 14, 10, 8, 6, 4, 4`
- `Prioridades: 3 ações afirmativas (Lucas:) + 2 itens de não-fazer da 6B — itens de não-fazer mantidos sem prefixo "Lucas:" por serem diretivas operacionais gerais, não ações atribuídas individualmente`
- `Prioridade 4 e 5 (não acionar Himmel; não tratar como bloco) preservadas da 6B — representam postura explícita da Condensadora/Tática que não deve ser omitida`
- `Seção VISÃO SHOPEE sem comparações temporais — dados objetivos do dia apenas; comparações aparecem exclusivamente na seção de análise, vindas do 6B`
- `Ressalva de causa hipotética preservada em todos os trechos onde a 6B a incluiu — "permanece hipótese", "indício não confirmado"; nenhuma hipótese foi convertida em fato`
- `Conectivos da 6B preservados integralmente — nenhum "mas" substituído por "e", nenhum "enquanto" substituído por "e"`