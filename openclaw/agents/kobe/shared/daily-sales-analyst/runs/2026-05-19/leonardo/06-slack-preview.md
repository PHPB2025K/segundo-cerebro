<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 19/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 2.472,80
- Pedidos: 67 pedidos
- Ticket médio: R$ 36,91
- Cancelamentos: 13
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 30 pedidos
- Jarra Medidora de Vidro 500ml — 12 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 5 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml Preto (ASIN: B0GGTY2BLT) — 5 pedidos
- Suporte Controle Gamer — 4 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 3 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas (ASIN: B0GFPQD4G9) — 2 pedidos
- Kit 6 Canecas de Porcelana Tulipa 250ml Branco (ASIN: B0GGTTMD4H) — 1 pedido
- Kit Conjunto 3 Potes de Vidro Herméticos Tampa Bambu (ASIN: B0F2GHQHRN) — 1 pedido
- Kit 2 Potes de Vidro 1050ml Retangular — 1 pedido

🔍 ANÁLISE DA CONTA
- O dia teve volume expressivo — mais que o dobro do histórico de segunda-feira — mas a leitura positiva está suspensa: a taxa bruta de cancelamento (~19%) não tem detalhamento por produto no pacote, então o volume líquido real pode ser significativamente menor do que aparece. Sem dado de Buy Box e sem histórico interpretativo acumulado, não há base para separar ganho de patamar de burst pontual. O sinal existe — mas precisa ser qualificado antes de ser tratado como confirmação.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box e cobertura FBA do grupo de potes de vidro redondos — em especial a variação tampa preta, que respondeu por quase metade dos pedidos do dia. A conta opera 100% FBA e mais da metade do volume está concentrado em variações de cor do mesmo produto base — instabilidade de Buy Box ou ruptura de FBA nesse produto derruba o resultado sem amortecimento. Confirmar: Buy Box ≥85% e estoque FBA ok abre caminho para, se o GMV sustenta acima de R$ 1.800,00 por mais 3 dias, acionar Pedro. Escalar se Buy Box degradado ou FBA em risco.
- Leonardo: investigar os 13 cancelamentos — identificar se estão concentrados em um produto específico, janela horária ou padrão de fulfillment. Sem esse dado, a leitura positiva do volume permanece formalmente suspensa. Confirmar: cancelamentos dispersos validam o volume; cancelamentos concentrados no produto principal mudam a interpretação do dia. Escalar se concentrados no produto líder — avaliação imediata de listing e FBA.

Dia analisado: 19/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: `TL250P` — display_name `Tigela de Vidro 250ml`
- Origem do bloqueio: Granular + Condensadora
- Motivo: alias manual incorreto; produto real confirmado por pedido é `Budamix Kit 6 Canecas de Porcelana Tulipa 250ml` (ASIN B0GGTY2BLT)
- Agregado autorizado: não (Condensadora orienta omitir citação nominal ou usar raw_title)
- Tratamento aplicado: citado pelo raw_title do pedido com ASIN visível — `Kit 6 Canecas de Porcelana Tulipa 250ml Preto (ASIN: B0GGTY2BLT)`
- Aparece na mensagem final: sim, como raw_title com ASIN (sem alias incorreto)

---

- Item bloqueado: `TL250B` — display_name `Tigela de Vidro 250ml`
- Origem do bloqueio: Granular + Condensadora
- Motivo: alias manual incorreto; produto real confirmado por pedido é `Kit 6 Canecas de Porcelana Tulipa 250ml Branco` (ASIN B0GGTTMD4H)
- Agregado autorizado: não (mesma orientação)
- Tratamento aplicado: citado pelo raw_title do pedido com ASIN visível — `Kit 6 Canecas de Porcelana Tulipa 250ml Branco (ASIN: B0GGTTMD4H)`
- Aparece na mensagem final: sim, como raw_title com ASIN

---

- Item bloqueado: `TL6250` — display_name `Kit 6 Tigelas de Vidro 250ml`
- Origem do bloqueio: Granular + Condensadora
- Motivo: alias manual incorreto; produto real confirmado por pedido é `Budamix Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas` (ASIN B0GFPQD4G9)
- Agregado autorizado: não (mesma orientação)
- Tratamento aplicado: citado pelo raw_title do pedido com ASIN visível — `Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas (ASIN: B0GFPQD4G9)`
- Aparece na mensagem final: sim, como raw_title com ASIN

---

- Item bloqueado: afirmação de volume validado ou ganho de patamar
- Origem do bloqueio: Condensadora
- Motivo: cancelamentos sem breakdown por ASIN e dado de Buy Box ausente — leitura positiva formalmente suspensa
- Agregado autorizado: não aplicável
- Tratamento aplicado: preservada ressalva explícita na análise da conta — "leitura positiva está suspensa", "não há base para separar ganho de patamar de burst pontual"
- Aparece na mensagem final: não como afirmação; aparece como ressalva

---

- Item bloqueado: afirmar causa do burst de 14h–15h como ADS ou promoção
- Origem do bloqueio: Condensadora
- Motivo: causa não determinável por ausência de dado de tráfego no pacote
- Agregado autorizado: não
- Tratamento aplicado: causa do burst não mencionada na mensagem
- Aparece na mensagem final: não

---

- Item bloqueado: afirmar que as três variações do grupo de potes de vidro representam mix diversificado
- Origem do bloqueio: Condensadora
- Motivo: são variações de cor do mesmo produto base, não diversificação de risco operacional
- Agregado autorizado: não
- Tratamento aplicado: prioridade menciona explicitamente "variações de cor do mesmo produto base"
- Aparece na mensagem final: não como afirmação de diversificação; aparece como ressalva na prioridade

---

- Item bloqueado: recomendação de acionamento de Pedro para ADS
- Origem do bloqueio: Condensadora
- Motivo: Buy Box e cancelamentos ainda não validados; pré-requisitos pendentes com Leonardo
- Agregado autorizado: não
- Tratamento aplicado: acionamento de Pedro mantido apenas como condição futura condicional ("se o GMV sustenta acima de R$ 1.800,00 por mais 3 dias, acionar Pedro") — não como recomendação imediata
- Aparece na mensagem final: sim, como condição condicional após pré-requisitos resolvidos

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional + Granular`, `padrão B`) do único insight da Condensadora — mantida a tese, removidos apenas marcadores internos de pipeline
- Preservação integral da ressalva da Condensadora: "leitura positiva está suspensa", "não há base para separar ganho de patamar de burst pontual", "O sinal existe — mas precisa ser qualificado" — linguagem de indício preservada sem suavização
- Faturamento corrigido para R$ 2.472,80 (dado do pacote: 2472.8) — padrão numérico obrigatório aplicado
- TL250P, TL250B e TL6250: citados pelo raw_title com ASIN visível em vez de display_name bloqueado — motivado por bloqueio da Granular/Condensadora e regra Amazon de ASIN visível quando título é ambíguo; título `Tigela de Vidro` é factualmente errado, portanto raw_title prevalece e ASIN incluído para identificabilidade
- SKU `028` (confidence medium, mapped_generic_sku): optado por usar raw_title `Kit Conjunto 3 Potes de Vidro Herméticos Tampa Bambu` com ASIN B0F2GHQHRN visível — motivado por risco médio de identificação e regra Amazon de ASIN quando risco médio presente; registrado aqui para auditoria QA
- Condensadora entregou 1 insight; usado 1 insight sem complemento — sem frase de enchimento
- Prioridades: mantidos os dois itens da Condensadora, com ação, evidência, sinal de confirmação/refutação e condição de escalonamento preservados; atribuição a Leonardo conforme destinatário Amazon
- Escalonamento para Pedro mantido apenas como condição futura e condicional, não como recomendação imediata — fiel à Condensadora e às regras de responsáveis (Leonardo valida pré-requisitos antes de acionar Pedro)
- Burst de 14h–15h: não mencionado na mensagem — causa não determinável e a Condensadora não incluiu como prioridade ou insight; omissão documentada aqui
- Top Produtos: mantidos em ordem decrescente por pedidos; variações da família IMB501 separadas por cor conforme regra obrigatória (Tampa Preta, Cinza, Vermelha em linhas distintas); sem faturamento por produto — pacote não traz receita validada por variação, proibido estimar