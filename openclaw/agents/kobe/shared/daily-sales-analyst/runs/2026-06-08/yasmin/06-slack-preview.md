<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 08/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 8.850,18
- Pedidos: 201
- Ticket médio: R$ 44,03
- Cancelamentos: 6

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Cinza — 41 pedidos
- Potes Vidro 5 Peças — Tampa Preta — 28 pedidos
- Kit 2 Potes 1050ml — 20 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 18 pedidos
- Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo — 16 pedidos

🔍 ANÁLISE DA CONTA
- A conta alcançou o MercadoLíder Platinum — ontem foi a segunda segunda-feira seguida acima de R$ 8.500,00 (média histórica de segundas: R$ 5.697,87), e a soma dos últimos 60 dias chegou a R$ 301.153,66, acima do limite de R$ 296.000,00. O foco muda: não é mais conquistar a medalha, é não perdê-la por cancelamento automático na janela dos 60 dias.
- Dois anúncios em Full chegaram juntos com estoque baixo — o mais urgente pode ser o Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico, com 19 unidades. Como o produto vende em média 1,55 unidade por pedido, o estoque pode durar só cerca de 1,1 dia. O Kit 4 Potes 1050ml tem 33 unidades e cobertura de cerca de 2 dias. Sem previsão de quando o restock chega ao CD do ML, qualquer um pausando pode gerar cancelamento automático direto na janela do Platinum recém conquistado — que hoje tem taxa de cancelamento oficial em zero e nenhum histórico de proteção acumulado.
- O crescimento veio mais do orgânico do que do ADS — o ADS respondeu por 47,1% do faturamento (R$ 4.169,41 de R$ 8.850,18), sétimo ciclo seguido de queda desde 69,9% em 22/05, enquanto o faturamento subiu 80% no mesmo período. ROAS 9,7x e ACOS 11,67% seguem eficientes. Himmel não aumentou a verba; a conta está entregando mais com o mesmo investimento. Parece ser uma expansão estrutural do orgânico, mas precisa de mais um ciclo para confirmar.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar quantas unidades restam e quando o restock chega ao CD do ML para o Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico (19 unidades) e o Kit 4 Potes 1050ml (33 unidades), ambos em Full. Ruptura em qualquer um pode virar cancelamento automático direto na janela do Platinum — que tem taxa de cancelamento oficial em zero hoje e nenhum amortecimento. O Canequinhas Acrílico é o mais urgente: vende em múltiplos e o estoque pode durar só ~1,1 dia. Confirmar/refutar por: restock confirmado em até 48h nos dois = risco neutralizado; menos de 8 unidades em qualquer um sem previsão de chegada, ou status pausado = urgente, providenciar reposição ou cancelamento controlado antes de o ML cancelar automaticamente. Escalar se: qualquer um pausar com pedidos pendentes ou a taxa de cancelamento oficial sair de zero no próximo snapshot.
- Yasmin: verificar a direção do nível de qualidade do Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo (nível preocupante) comparando com o snapshot anterior. É o 5º ciclo no nível preocupante — o gatilho para alinhar com Himmel é cair abaixo de 0,63, e a diferença hoje é de 0,03. Confirmar/refutar por: valor igual ou subindo no próximo snapshot = seguir observando sem ação; abaixo de 0,63 = Yasmin alinha com Himmel sobre cobertura de ADS preventiva antes do próximo ciclo. Escalar se: queda abaixo de 0,63, ou queda equivalente no Kit 4 Potes 1050ml (qualidade em regular) ou no Potes Vidro 5 Peças (qualidade em regular).
- Yasmin: registrar o ADS share de hoje (47,1%, ACOS 11,67%) como sétimo ponto da série e observar o próximo dia útil. É o segundo ciclo seguido abaixo de 50% em dia de faturamento alto. Se o próximo confirmar share abaixo de 50% com ACOS voltando a 10% ou menos, a expansão do orgânico deixa de ser hipótese e Yasmin abre pauta com Kobe sobre calibragem da verba. Confirmar/refutar por: share abaixo de 50% com ACOS ≤ 10% no próximo dia útil = hipótese confirmada; ACOS acima de 15% com share voltando acima de 55% = orgânico não está sustentando sozinho, revisar com Himmel. Escalar se: ACOS acima de 20% por dois ciclos seguidos com share acima de 60%.

Dia analisado: 08/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

- L05 `o_que_nao_pode_ir_para_slack`: `[]` (vazio)
- L04 `bloqueios_para_slack`: `[]` (vazio)
- L04 `risco_identificacao.nivel`: `"baixo"` — nenhum produto com risco de identificação ativo

Todos os 10 produtos do top têm convergência de title e raw_title; dois com mapping_confidence=medium (MLB5402326666 e MLB6073033006) foram liberados pela Granular por convergência integral de identidade.

---

### Decisões de formatação

**Metadados internos**
- Campos `padrao`, `base` e `classificacao` suprimidos da mensagem — são metadados de pipeline, não vão para o Slack.

**Preservação de classificação por nuance**
- Insight 1 (`classificacao: "fato"`) — linguagem afirmativa direta: "alcançou", "chegou a", "o foco muda". Sem hedge.
- Insight 2 (`classificacao: "risco latente"`) — preservada com "pode ser", "pode gerar", "pode durar", "pode virar". Não convertido em certeza.
- Insight 3 (`classificacao: "hipótese"`) — preservada com "parece ser uma expansão estrutural", "precisa de mais um ciclo para confirmar". Não convertido em fato.

**Omissão de modalidade de envio na seção VISÃO**
- `fulfillment_mix_yesterday_top10` cobre apenas os top 10 itens ponderados por pedidos (n=130 de 201 pedidos = 64,7% do total). Não representa dado objetivo de totalidade — omitido da VISÃO. Modalidade de envio tratada apenas nas seções ANÁLISE e PRIORIDADES via contexto da L05.

**Nomes de produtos — Top Produtos (5 primeiros)**
- IMB501C — usado slack_short_name `"Potes Vidro 5 Peças — Tampa Cinza"` (mapeamento canônico)
- IMB501P — usado slack_short_name `"Potes Vidro 5 Peças — Tampa Preta"` (mapeamento canônico)
- KIT2YW1050 — usado slack_short_name `"Kit 2 Potes 1050ml"` (mapeamento canônico)
- IMB501V — usado slack_short_name `"Potes Vidro 5 Peças — Tampa Vermelha"` (mapeamento canônico)
- KIT4YW640 — usado display_short `"Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo"` (fallback automático; slack_short_name=null para SKU KIT4YW640)

**Nomes de produtos — Análise e Prioridades (fora do top 5 visível)**
- KIT4YW1050 (MLB4073003575, rank 6) — usado slack_short_name `"Kit 4 Potes 1050ml"` (mapeamento canônico)
- 914C_BA (MLB6073033006, rank 8) — usado display_short `"Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico"` (fallback automático; slack_short_name=null para SKU 914C_BA)

**Divergências de denominação cross-layer (L05 → L06)**
- L05 escreveu `"Kit 06 Canequinhas Acrílico"` → L06 usou `"Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico"` — motivo: padronização com display_short do top_products (slack_short_name=null para 914C_BA; "06" normalizado para "6"; atributo "Acrílico" mantido no display_short)
- L05 escreveu `"Kit 4 Potes 1050ml Azul-petróleo"` → L06 usou `"Kit 4 Potes 1050ml"` — motivo: padronização com slack_short_name canônico (mapeamento manual, KIT4YW1050)
- L05 escreveu `"Kit 4 Potes 640ml Azul-petróleo"` → L06 usou `"Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo"` — motivo: padronização com display_short (slack_short_name=null para KIT4YW640)
- L05 escreveu `"Jogo Potes 5 Peças Claro (nível regular 0,71)"` no escalar_se → L06 usou `"Potes Vidro 5 Peças (qualidade em regular)"` — motivo: (a) health é métrica do anúncio MLB3288536143, que cobre IMB501C e IMB501V; referência coletiva sem especificar variação; (b) pontuação numérica 0,71 omitida como label de qualidade per regra; (c) nome simplificado para "Potes Vidro 5 Peças" como referência ao anúncio compartilhado

**Cluster IMB501 — tratamento de variações**
- Title ML genérico `"Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita"` (MLB3288536143) identificado via `confirmed_variation_attributes` por SKU: IMB501C → Tampa Cinza, IMB501V → Tampa Vermelha. Variações comunicadas separadamente no Top Produtos com atributo confirmado incluído no nome. Não consolidadas em linha única (regra: separar variações com identidade real por cor da tampa).
- IMB501P (Tampa Preta) opera via MLB4535865317 (Cross-Docking) — anúncio distinto, não compartilha o MLB3288536143. Tratado como variação separada. ✓

**Simplificações de comunicação aplicadas (Pedro 2026-05-17 e 2026-05-25)**
- `"threshold"` → `"limite"` (contextos de Platinum e qualidade)
- `"janela rolling"` → `"janela dos 60 dias"` (referência à janela de apuração MercadoLíder)
- `"ETA de reposição"` → `"previsão de quando o restock chega"`
- `"cancellations_rate"` → `"taxa de cancelamento oficial"`
- `"Monday"` (anglicismo presente no texto da L05) → `"segunda-feira"`
- `"Mercado Líder"` (grafado com espaço no L05) → `"MercadoLíder"` (grafia oficial do marketplace)
- `"eixo muda"` → `"foco muda"` (mais direto no contexto operacional)
- `"amortecimento acumulado"` mantido — termo claro no contexto de proteção de reputação
- Frases longas da L05 quebradas em duas ou três no Insight 2 e nas Prioridades, mantendo todos os termos analíticos e a tese intacta

**Threshold numérico 0,63 no contexto de gatilho**
- O valor 0,63 foi preservado nas seções Confirmar/refutar e Escalar se da Prioridade 2 — trata-se de gatilho operacional explícito da L02/L05, não de label de qualidade entre parênteses. A regra de omissão de pontuação numérica aplica-se à formatação `"qualidade em regular (0,75)"`, não a thresholds de ação.

**Valores monetários**
- Centavos incluídos em todos os valores: R$ 8.850,18; R$ 44,03; R$ 4.169,41; R$ 8.500,00; R$ 5.697,87; R$ 301.153,66; R$ 296.000,00. Sem mistura de formato com e sem centavos no mesmo bloco.

**Confiança média (L05 alertas_de_confianca.nivel="media")**
- Não aplicada ressalva global explícita de "leitura limitada" (reservada para nível baixo). Nuance preservada via classificação por insight (fato/risco latente/hipótese) conforme acima.

**Atribuição de responsável**
- Yasmin atribuída como responsável nas três prioridades. L05 não atribui responsável — atribuição feita pela L06 conforme papel fixo (Yasmin = Mercado Livre). ✓

**Termos técnicos não traduzidos — mantidos por serem vocabulário ML obrigatório**
- Full (modalidade de envio), Cross-Docking, MercadoLíder Platinum, ROAS, ACOS, Buy Box, CD do ML.