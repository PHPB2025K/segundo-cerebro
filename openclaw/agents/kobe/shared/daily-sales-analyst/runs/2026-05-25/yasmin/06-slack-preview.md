<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 25/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.127,39
- Pedidos: 108
- Ticket médio: R$ 47,48
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 40 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 11 pedidos
- Kit 6 Canecas Lisas 200ml — 11 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Kit 4 Potes 1050ml — 7 pedidos

🔍 ANÁLISE DA CONTA
- O dia foi forte — 108 pedidos e R$ 5.127,39 de faturamento, acima das últimas 4 segundas e das janelas de 30 e 60 dias. O risco é que esse crescimento veio concentrado num único anúncio: os Potes Vidro 5 Peças responderam por 56,5% do volume — novo pico da série (44% → 47,5% → 56,5%) — e seguem com qualidade do anúncio em regular no sexto dia seguido. O ADS respondeu por 56,7% do faturamento. Conta cresce, piso operacional encolhe.
- Os 3 cancelamentos do dia parecem ter origem nos 3 pedidos que o Kit 10 Potes 1050ml — 10 un gerou estando pausado e sem estoque — a coincidência é forte, mas o pacote não confirma a ligação. Se o ML cancelou automaticamente, a taxa de cancelamentos (hoje em zero) começa a se mover nos próximos 3 a 5 dias e pressiona a reputação verde e o MercadoLíder Gold por dentro, sem aparecer nos números de hoje.
- O Kit 6 Canecas Lisas 200ml chegou na zona crítica: é um anúncio Catálogo Premium em Full, vendeu 11 ontem — acima do ritmo histórico de ~6 por dia — e fechou com 19 unidades. Cobertura de ~1,7 dias sem reposição confirmada em trânsito ao CD do ML. O risco não é só estoque: ruptura num anúncio Catálogo significa perder o Buy Box, e recuperar a posição demora mais do que num Clássico.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o que aconteceu com os 3 pedidos do Kit 10 Potes 1050ml — 10 un (anúncio pausado, sem estoque) e definir entre cancelamento controlado ou reposição emergencial. Se o ML cancelar automaticamente, esses 3 eventos entram na janela de reputação e movem a taxa de cancelamentos — que está em zero hoje e sustenta a conta em reputação verde e MercadoLíder Gold. Confirmar/refutar: taxa de cancelamentos ainda em zero no próximo snapshot e sem novos cancelamentos no anúncio = neutralizado; taxa subindo ou novos cancelamentos vinculados = ML já cancelou automaticamente.
- Yasmin: checar estoque atual e reposição em trânsito ao CD do ML do Kit 6 Canecas Lisas 200ml (anúncio Catálogo Premium em Full). A cobertura é de ~1,7 dias ao ritmo do dia — a janela de 24 a 48h já está aberta. Ruptura num anúncio Catálogo significa perder o Buy Box, e a recomposição demora mais do que num Clássico. Confirmar/refutar: reposição confirmada em trânsito antes de cair abaixo de 5 unidades = neutralizado; abaixo de 5 sem reposição = acionar reabastecimento com urgência. Escalar se: estoque zerar e anúncio entrar em ruptura sem reposição visível.
- Yasmin: registrar ACOS de 14,2%, ADS respondendo por 56,7% do faturamento e ROAS de 7,67x como segundo ponto da série, e aguardar o próximo dia antes de acionar Himmel. O salto foi expressivo — de ~4,4% para 14,2% em um dia — mas o ROAS ainda está acima do ponto de ação. Sem mais um dia, não dá pra saber se foi evento pontual ou início de queda de eficiência. Confirmar/refutar: ACOS abaixo de 12% no próximo dia = evento pontual; ACOS acima de 15% por dois dias seguidos com ADS acima de 50% do faturamento = preparar alinhamento com Himmel. Escalar se: ACOS acima de 20% com ROAS abaixo de 5x no próximo dia.

Dia analisado: 25/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação causal de que os 3 cancelamentos do dia têm origem confirmada nos 3 pedidos do Kit 10 Potes 1050ml — 10 un (MLB4676726433, status=paused, available_quantity=0)
- **Origem do bloqueio:** L05 Condensadora (`o_que_nao_pode_ir_para_slack[0]`)
- **Motivo:** L04 confirmou apenas indício circunstancial (coincidência numérica 3==3) sem vínculo causal order_id↔cancel_id; mecanismo de cancelamento (automático ML vs manual Yasmin) ausente do pacote
- **Agregado autorizado:** não
- **Tratamento aplicado:** substituído por linguagem de hipótese — "parecem ter origem" e "a coincidência é forte, mas o pacote não confirma a ligação"
- **Aparece na mensagem final:** sim, como hipótese — insight 2 e prioridade 1

---

- **Item bloqueado:** Afirmação de que a qualidade do anúncio do MLB3288536143 (Potes Vidro 5 Peças) "estabilizou" ou "piorou" no sexto ponto da série
- **Origem do bloqueio:** L05 Condensadora (`o_que_nao_pode_ir_para_slack[1]`)
- **Motivo:** L04 declarou direção não observável no pacote — série temporal de qualidade do anúncio por anúncio ausente; apenas valor pontual disponível
- **Agregado autorizado:** não
- **Tratamento aplicado:** descrito como "seguem com qualidade do anúncio em regular no sexto dia seguido" — sem afirmar direção (nem estável, nem caindo, nem subindo)
- **Aparece na mensagem final:** sim, como observação neutra do valor pontual no insight 1

---

- **Item bloqueado:** Atribuição do salto de ACOS (de ~4,4% para 14,2%) a um anúncio específico (cluster IMB501 ou qualquer outro)
- **Origem do bloqueio:** L05 Condensadora (`o_que_nao_pode_ir_para_slack[2]`)
- **Motivo:** L04 declarou breakdown de ADS spend/revenue por platform_item_id ausente do pacote — qualquer atribuição seria especulação
- **Agregado autorizado:** não
- **Tratamento aplicado:** ACOS e ROAS tratados como métricas agregadas da conta, sem atribuição a produto específico; prioridade 3 registra como série de observação sem diagnóstico de causa
- **Aparece na mensagem final:** sim, como dado agregado sem atribuição — prioridade 3

---

- **Item bloqueado:** Termo "health" no texto Slack
- **Origem do bloqueio:** L05 Condensadora (`o_que_nao_pode_ir_para_slack[3]`)
- **Motivo:** regra de vocabulário ML — "health" é jargão técnico proibido no Slack; usar "qualidade do anúncio" + nome natural da faixa
- **Agregado autorizado:** não aplicável (substituição de termo, não de conteúdo)
- **Tratamento aplicado:** substituído por "qualidade do anúncio em regular" (faixa 0,70–0,84) em todas as menções da mensagem
- **Aparece na mensagem final:** não — o termo "health" não aparece em nenhum ponto

---

### Decisões de formatação

- **IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)**
- **IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)**
- **CLR002 — usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)**
- **IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)**
- **KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)**
- **KIT10YW1050 (MLB4676726433) — usado slack_short_name "Kit 10 Potes 1050ml — 10 un" (mapeamento canônico); mencionado em Análise e Prioridades, não no Top 5 (posição 8 no top_products)**
- **MLb6232315532 (CLR002 compartilha MLB) — usado slack_short_name "Kit 6 Canecas Lisas 200ml" (mapeamento canônico); aparece no Top 5 (posição 3) e mencionado em Análise e Prioridades**
- **Cluster IMB501 na Análise — L05 referenciou "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" como anúncio-cluster inteiro (MLB3288536143, 3 variações: Tampa Preta 40 + Cinza 11 + Vermelha 10 = 61 pedidos). Traduzido para "os Potes Vidro 5 Peças" (base comum dos slack_short_names das 3 variações, sem atributo de cor, pois a referência é ao MLB inteiro e não a uma variação isolada). Não há slack_short_name no nível de MLB — nome de cluster derivado dos slack_short_names das variações por ser a denominação mais fidedigna disponível.**
- **Divergência de denominação cross-layer — Análise/Prioridades: L05 escreveu "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades"; L06 escreveu "Kit 10 Potes 1050ml — 10 un". Motivo: padronização com slack_short_name do top_products (KIT10YW1050).**
- **Divergência de denominação cross-layer — Análise: L05 escreveu "Kit De 6 Canecas De Porcelana Lisa Reta Para Chá E Café Colorida 200 Ml Caneca Colorida"; L06 escreveu "Kit 6 Canecas Lisas 200ml". Motivo: padronização com slack_short_name do top_products (CLR002).**
- **"health" → "qualidade do anúncio em regular" — faixa 0,70–0,84 = regular; nunca citado o valor numérico entre parênteses; nunca escrito "health" no Slack**
- **"GMV" → "faturamento" — em todas as menções, regra absoluta**
- **"ADS share" → "ADS respondeu por X% do faturamento" — em todas as menções**
- **"ciclo" → "dia" — traduzido em todas as ocorrências: "no sexto dia seguido", "nos próximos 3 a 5 dias", "próximo dia", "dois dias seguidos"**
- **ACOS 14,15% → 14,2% — arredondado para 1 casa decimal conforme padrão numérico obrigatório de percentuais**
- **Metadados internos removidos — `padrao`, `base` e `classificacao` não citados na mensagem; nuances de classificação preservadas via linguagem: risco latente → "o risco é que..." / "o risco não é só..."; hipótese → "parecem ter origem" / "a coincidência é forte, mas..." / "Se o ML cancelou automaticamente"**
- **Atribuição de responsável Yasmin — adicionada nas 3 prioridades; L05 não atribui responsável, L06 atribui conforme regra**
- **Modalidade de envio omitida da seção VISÃO — `fulfillment_mix_yesterday_top10` cobre apenas 44 dos 108 pedidos do dia (top 10 ponderado, ~40% da cobertura); não representa dado objetivo da plataforma sem ressalva; omitido desta seção conforme regra; modalidade de envio tratada em Análise via L05 (referência a Full no insight 3)**
- **"Kit 6 Canecas Lisas 200ml" descrito como "Catálogo Premium em Full" — L05 usou esta denominação; preservada; "Catálogo" = is_catalog=true, "Premium" = listing_type=gold_pro, "Full" = logistic_type=fulfillment**
- **Centavos preservados em todos os valores monetários — R$ 5.127,39 e R$ 47,48 com 2 casas decimais obrigatórias**
- **Comparações temporais ausentes da seção VISÃO — faturamento, pedidos, ticket médio e cancelamentos apresentados como dados objetivos do dia sem comparação com janelas históricas; comparações pertencem à Análise e vieram da Condensadora**