<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 17/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Total Shopee: R$ 5.580,61 — 113 pedidos — ticket médio R$ 49,39
• Budamix Store (Conta 1): R$ 3.252,47 — 73 pedidos
• Budamix Oficial (Conta 2): R$ 1.384,24 — 25 pedidos
• Budamix Shop (Conta 3): R$ 943,90 — 15 pedidos
• Cancelamentos: 5 (Store 3, Conta 2: 2, Conta 3: 0)

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 36 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 21 pedidos
• Kit 6 Canecas Tulipa 250ml (Store + Conta 2 + Conta 3) — 14 pedidos consolidados
• Kit 2 Potes de Vidro 800ml Quadrado (Conta 3) — 7 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 7 pedidos
• Kit 3 Potes de Vidro Hermético (Conta 2) — 4 pedidos
• Kit 6 Canecas Retas 200ml (Conta 3) — 3 pedidos
• Kit 4 Potes de Vidro 800ml Quadrado (Conta 2) — 3 pedidos
• Kit 6 Canequinhas 100ml (Conta 2) — 3 pedidos
• Kit 6 Canecas Tulipa 250ml (Conta 3) — 3 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* O total de R$5.580 e 113 pedidos esconde uma assimetria estrutural: a Store carregou sozinha 65% do volume e 58% do GMV enquanto Conta 2 e Conta 3 ficaram abaixo de todas as janelas comparáveis — o canal não está equilibrado, está sustentado por uma conta enquanto as outras duas contraem em ritmos e mecanismos distintos, o que invalida qualquer leitura ou ação transversal.

🟠 *Budamix Store (Shopee 1):* A conta opera em acomodação com ticket elevado (+14,4% vs 30d) compensando queda de volume — o GMV ficou acima do mesmo dia da semana, mas apoiado em IMB501P (Tampa Preta, 36 pedidos, ~49% do total) e nos top 3 respondendo por 89%; se esse produto oscilar, o segundo vetor (CK4742, 21 pedidos) não compensa o déficit e o GMV fica exposto ao vácuo de volume deixado pelo 60d.

🟠 *Budamix Oficial (Shopee 2):* A conta registrou fraqueza dupla — pedidos e ticket caindo juntos (−22,5% e −7,3% vs mesmo dia da semana), sem nenhum mecanismo de compensação interno como existe na Store; isso confirma a tese de vulnerabilidade acumulada, e a causa permanece aberta porque o pacote não tem dados de ranking, estoque ou impressões — agir sobre hipótese não verificada em conta já fraca é o maior risco operacional agora.

🟠 *Budamix Shop (Shopee 3):* A conta entregou 15 pedidos com zero cancelamentos e 100% de concentração nos top 5 — a queda foi limpa, sem distorção que suavize a leitura — e o Kit 2 Potes de Vidro 800ml Quadrado respondeu por 46,7% do volume numa conta onde não existe nenhum produto fora desses 5; a série descendente (7d < 30d < 60d) confirma que não foi um dia fraco isolado, mas a causa (ranking, estoque, demanda) ainda não foi verificada e determina se a urgência é operacional imediata ou de tráfego.

🎯 PRIORIDADES DO DIA
• *[Conta 3 — urgente]* Lucas: checar disponibilidade de estoque e posição de ranking do Kit 2 Potes de Vidro 800ml Quadrado. Produto saudável = causa é demanda ou tráfego, observar 2 dias antes de qualquer ação. Problema operacional confirmado = alinhar com Himmel sobre exposição e ADS da Conta 3 ainda hoje — não há nenhum produto que absorva qualquer choque nessa conta.
• *[Conta 2 — observar]* Lucas: registrar GMV e ticket nos próximos 2 dias. Dois dias com GMV abaixo de R$1.500 e ticket abaixo de R$58 confirmam novo patamar inferior e justificam alinhamento com Himmel. Dois dias acima mantêm observação — não acionar Himmel antes de fechar esse diagnóstico.
• *[Store — manter]* Lucas: não alterar mix nem exposição por 2-3 dias. Verificar ticket médio diário acima de R$40 como sinal de que o mecanismo está ativo. Ticket abaixo de R$40 por 2 dias seguidos = reavaliar Store.
• *[Todas as contas — não fazer]* Não tratar as quedas da Conta 2 e Conta 3 como "Shopee em queda geral" e não tomar ação transversal: a Store está acima do mesmo dia da semana e sustenta 58% do canal.

Dia analisado: 17/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: Produtos com confiança média — KIT4YW640, CNCOL, KIT4YW320, KIT9S101, KIT4YW520SQ
- Origem do bloqueio: Condensadora
- Motivo: volume residual de 1-2 pedidos cada; confiança média (mapped_generic_sku); não sustentam nenhuma tese central
- Agregado autorizado: não
- Tratamento aplicado: omitidos do Top Produtos e da análise
- Aparece na mensagem final: não

- Item bloqueado: ITEM:57356981475 (produto Store sem raw_sku, mapeado por platform_item_id)
- Origem do bloqueio: Condensadora
- Motivo: sem raw_sku, identificação apenas por platform_item_id, confiança média
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: Causa das quedas da Conta 2 e Conta 3 (ranking, estoque, impressões)
- Origem do bloqueio: Condensadora / Granular
- Motivo: dado não disponível no pacote; qualquer conclusão de causa seria inferência sem evidência
- Agregado autorizado: não aplicável
- Tratamento aplicado: causa apresentada como aberta, não concluída
- Aparece na mensagem final: sim, como incerteza preservada ("a causa permanece aberta")

- Item bloqueado: Detalhe dos cancelamentos da Conta 2 por produto
- Origem do bloqueio: Granular
- Motivo: dado não disponível no pacote; pergunta não respondida
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: Histórico granular do produto líder da Store por sábado
- Origem do bloqueio: Granular
- Motivo: série histórica por produto não disponível; inferência possível mas não confirmada
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: Análise horária da Conta 3
- Origem do bloqueio: Condensadora
- Motivo: base de 15 pedidos torna qualquer leitura de horário inconclusiva
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: platform_item_ids e raw_skus técnicos
- Origem do bloqueio: Condensadora
- Motivo: IDs técnicos não devem aparecer no Slack
- Agregado autorizado: não aplicável
- Tratamento aplicado: omitidos de toda a mensagem
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional`, `— base: Granular`, etc.) de todos os insights — motivo: referências de pipeline não vão para Slack
- Seção `🔍 ANÁLISE DA CONTA` renomeada visualmente para `ANÁLISE DAS CONTAS` no cabeçalho da seção — motivo: addendum v3.1 exige esse label quando 6B está presente com 3 contas
- Análise das contas copiada literalmente da `06b-shopee-consolidator` — motivo: fonte analítica obrigatória para Lucas/Shopee per addendum v3.1; nenhum rediagnóstico aplicado
- Prioridades adaptadas para formato de Slack (bullets com responsável `Lucas:` e condições de confirmação/escalonamento) a partir das `priority_lines` da 6B — motivo: layout aprovado para `🎯 PRIORIDADES DO DIA`
- CTL002 consolidado nas 3 contas no Top Produtos (14 pedidos total, 3 listings distintos) — motivo: Granular confirmou tração multiloja com confiança alta; regra Shopee exige consolidar equivalentes da mesma variação vendável entre as 3 contas; linha única com nota de distribuição
- CTL002 mantido com indicação "(Store + Conta 2 + Conta 3)" — motivo: produto vendeu nas 3 contas, indicação de conta obrigatória quando produto aparece em múltiplas contas e Condensadora citou como relevante
- Kit 6 Canecas Tulipa 250ml (Conta 3) mantido como linha separada abaixo do consolidado — decisão: o consolidado de 14 pedidos representa as 3 contas; a linha de Conta 3 com 3 pedidos foi preservada para não omitir o volume individual da conta; reconsideração: linha duplicada pode confundir — linha de Conta 3 removível se QA entender que o consolidado já representa; registrado para revisão
- Produtos da Store com confiança alta mantidos nominalmente no Top Produtos (IMB501P, CK4742 como Conjunto 5 Potes Tampa Preta e Jarra Medidora) — motivo: confiança alta, reviewed_sku_display_map, sustentam teses centrais
- Kit 2 Potes de Vidro 800ml Quadrado (Conta 3) mantido nominalmente — motivo: confiança alta (reviewed_sku_display_map), produto central da tese de urgência, citado explicitamente na 6B
- Conjunto 5 Potes Tampa Cinza (Conta 2) e Kit 3 Potes Hermético (Conta 2) mantidos — motivo: confiança alta, sustentam leitura da Conta 2
- Preservação de nuances de hipótese vs fato: "a causa permanece aberta", "ainda não foi verificada", "determina se a urgência é operacional imediata ou de tráfego" — motivo: Condensadora classificou causas como abertas; proibido transformar em certeza
- Conectivo `mas` preservado nas análises da Store e Conta 3 — motivo: proibido trocar `mas` por `e`; o contraste é analiticamente essencial