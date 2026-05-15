<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 12/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: 118 pedidos — R$ 5.378,44 — ticket médio R$ 45,58 — 13 cancelamentos
• Budamix Store (Conta 1): 76 pedidos — R$ 2.813,88 — ticket R$ 37,02 — 10 cancelamentos
• Budamix Oficial (Conta 2): 23 pedidos — R$ 1.296,64 — ticket R$ 56,38 — 2 cancelamentos
• Budamix Shop (Conta 3): 19 pedidos — R$ 1.267,92 — ticket R$ 66,73 — 1 cancelamento

🏆 TOP PRODUTOS SHOPEE
• Conjunto de 5 Potes de Vidro Redondos — 33 unidades
• Jarra Medidora de Vidro 500ml (Budamix Store) — 29 unidades
• Canecas Tulipa Porcelana 250ml — 24 unidades
• Canecas Reta Porcelana 200ml — 10 unidades
• Kit 5 Potes de Vidro Redondos Translúcidos (Conta 2) — 9 unidades

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee entregou 118 pedidos e R$ 5.378,44, mas a queda é estrutural e diferenciada por conta — a Store carrega 64% do volume com ticket de R$ 37 puxando a média para baixo, enquanto Oficial e Shop somam os 36% restantes com tickets 50–80% maiores mas em declínio mais acelerado (-37% a -51% vs mesmo dia da semana); a consolidação esconde três falhas operacionais distintas, não uma, e o único contramovimento — ticket estável nas Contas 2 e 3 — confirma que o problema é de tráfego/exposição, não de competitividade de preço.

🟠 *Budamix Store (Shopee 1):* Sustenta o patamar da plataforma mas opera no limite da concentração estrutural: Potes de Vidro Redondos e Jarra Medidora carregaram 76% das unidades do dia, e os 10 cancelamentos (11,6% dos pedidos) permanecem sem explicação por produto — se estiverem concentrados nesses dois campeões, a única conta que ainda segura o volume Shopee passa de âncora estável para risco operacional agudo sem segunda linha para absorver.

🟠 *Budamix Oficial (Shopee 2):* Opera com deslocamento de tráfego para horários residuais (picos em 7h e 23h, janela 17–22h esvaziada) e -39,1% vs mesmo dia da semana — o ticket estável em R$ 56 descarta erosão de preço e aponta problema de exposição orgânica nos horários fortes; sem Shopee Full ativo, ADS via Himmel é a única alavanca disponível, mas não deve ser acionada antes de confirmar se o padrão horário de hoje é recorrente ou episódico.

🟠 *Budamix Shop (Shopee 3):* Deterioração mais severa das três (-51% vs mesmo dia da semana), operando como conta monotemática de canecas — Canecas Tulipa e Canecas Reta respondem por 81% das unidades, e as Canecas Tulipa competem com elas mesmas nas outras duas contas via anúncios distintos, configurando canibalização multiloja ativa confirmada; a queda não é de demanda por canecas, é de exposição de uma conta sem segundo vetor em competição interna com as próprias irmãs.

🎯 PRIORIDADES DO DIA
• Lucas: verificar onde estão concentrados os 10 cancelamentos da Budamix Store — urgente. Os dois produtos campeões carregaram 76% das unidades; se os cancelamentos estiverem neles, o risco passa de anomalia moderada para urgência operacional. Confirmar/refutar: se distribuídos entre múltiplos produtos → manter observação; se concentrados em um mesmo produto campeão → acionar Himmel sobre exposição da Conta 1. Escalar se dois ou mais cancelamentos confirmados no mesmo produto campeão.
• Lucas: monitorar a janela 17–22h nas Contas 2 e 3 nos próximos dois dias. Padrão de hoje foi atípico — Conta 2 com picos em 7h e 23h, Conta 3 fragmentada em 11 janelas sem pico em nenhuma. Confirmar/refutar: se as duas contas voltarem a concentrar pedidos em 17–22h com ao menos 5 pedidos cada → hipótese de exposição degradada enfraquece; se padrão atípico persistir → confirma e Lucas alinha com Himmel sobre ADS nessas duas contas. Escalar se padrão atípico confirmado por 2 dias seguidos nas duas contas.
• Não acionar Himmel para ajuste de ADS nas Contas 2 e 3 hoje. A causa da queda ainda não foi isolada entre exposição orgânica reduzida e desaceleração de patamar, e sem Shopee Full ativo, ADS sozinho opera sem o reforço de posicionamento que Full conferiria; escalar antes do diagnóstico amplifica gasto sem garantia de retorno.

Dia analisado: 12/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Sem bloqueios recebidos. A Condensadora e a Granular não emitiram BLOQUEIO PARA SLACK para nenhum produto ou item. O risco de identificação marcado pela Granular (nível médio) refere-se à incompletude de dados granulares (cancelamentos sem desagregação por SKU, ausência de histórico horário e de top_products histórico), não a ambiguidade de produto. Todos os produtos citados foram identificados por platform_item_id e título real de pedido, com confiança alta nas investigações próprias da Granular.

---

### Decisões de formatação

- Remoção de SKU técnicos nas análises — `IMB501P_T + CK4742_B` (Conta 1) substituídos por "Potes de Vidro Redondos e Jarra Medidora"; `CTL002 + KIT6CAR200` (Conta 3) substituídos por "Canecas Tulipa e Canecas Reta"; Condensadora não bloqueou os produtos, apenas SKU técnicos são proibidos para Slack.
- Preservação de ressalva de confiança no terceiro insight da Condensadora — linguagem de aberto mantida ("permanecem sem explicação por produto", "se estiverem concentrados"); não convertido para fato.
- Percentuais de queda (-37% a -51%, -39,1%, -51%) mantidos na seção ANÁLISE DAS CONTAS — comparações pertencem à análise, não à VISÃO; fonte 6B incluiu esses números como evidência da tese.
- Seção nomeada "ANÁLISE DAS CONTAS" (plural) — seguindo layout específico Shopee aprovado pelo addendum v3.1 para destinatário Lucas com 6B disponível.
- Quatro blocos de análise em parágrafo denso (não lista) — seguindo regra 7.6 do addendum: parágrafos curtos e densos, não lista longa.
- Conta indicada em Jarra Medidora "(Budamix Store)" — produto vendeu exclusivamente na Conta 1 (29 unidades, 0 nas outras); regra de indicação de conta ativada (menos de 2 contas).
- Conta indicada em Kit 5 Potes Translúcidos "(Conta 2)" — produto vendeu exclusivamente na Conta 2 (9 unidades, 0 nas outras); mesma regra.
- Conjunto de 5 Potes de Vidro Redondos sem indicação de conta — SKU IMB501P_T presente nas três contas (31 Store + 1 Conta2 + 1 Conta3 = 33 unidades); tecnicamente 3 contas, regra de indicação não ativada; concentração de 94% na Store não altera regra formal.
- Canecas Tulipa e Canecas Reta sem indicação de conta — CTL002 presente nas três contas (7+8+9 unidades), KIT6CAR200 presente em duas contas (2+8 unidades); regra de indicação não ativada em ambos.
- Faturamento omitido por produto em TOP PRODUTOS — pacote não contém receita desagregada por produto; apenas quantidade (unidades) disponível por SKU; inventar faturamento por produto seria fabricação proibida; formato adaptado para "unidades" sem valor monetário por produto.
- Ticket médio por conta incluído em VISÃO — dado objetivo sem análise; referenciado na análise como evidência de que o problema não é de preço; adição justificada como dado bruto disponível no pacote.
- Cancelamentos por conta incluídos em VISÃO — relevantes (13 cancelamentos de 118 pedidos = 11%; Conta 1 com 10 dos 13); disponíveis no pacote; sem análise nessa seção.
- Prioridade "Não fazer hoje" mantida como bullet negativo — vinda das priority_lines da 6B; preserva orientação tática direta da Condensadora/Consolidadora; sem inventar novo escalonamento.