<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 29/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 7.597,76
- Pedidos: 143 pedidos
- Ticket médio: R$ 53,13
- Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 40 pedidos
- Kit 6 Canecas Tulipa 250ml — 19 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 14 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 11 pedidos
- Kit 6 Canecas Lisas 200ml — 9 pedidos

🔍 ANÁLISE DA CONTA
- A conta teve o melhor faturamento da série — R$ 7.597,76, +51% vs média de 30 dias e +50% vs mesma sexta anterior. O resultado veio 100% de anúncios em Full. Mas ao menos quatro desses anúncios têm risco operacional ativo — o ganho é real, a base que o sustenta não está estável.
- O Kit 6 Canecas Tulipa 250ml está pausado e sem estoque, mas gerou 19 pedidos no dia (13% do volume). Se parte desses pedidos virar cancelamento pelo vendedor, a taxa de cancelamentos — que hoje está em zero — sai do chão exatamente na semana em que o MercadoLíder Platinum está a ~6 dias (gap R$ 26.538,39, progresso 91%). Ainda não é possível confirmar se esses pedidos foram atendidos antes da pausa ou vão virar cancelamento.
- Três anúncios Full (Kit 10 Potes 1050ml — 10 un, Kit 10 Potes 1050ml — 6 un e Kit 10 Potes 640ml — 6 un) têm menos de 1,5 dia de cobertura. Em Full, repor estoque depende de chegada ao CD do ML — não é rápido. Sem reposição em trânsito confirmada, ruptura nos próximos um a dois dias é o cenário mais provável.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o status dos 19 pedidos do Kit 6 Canecas Tulipa 250ml (pausado, sem estoque) — descobrir se foram atendidos pelo CD do ML antes da pausa ou se ainda estão pendentes e podem virar cancelamento. Por que importa: se a taxa de cancelamentos sair de zero antes do fechamento da janela de qualificação, a promoção ao Platinum (~6 dias) pode ficar em risco. Como saber se resolveu: taxa de cancelamentos se mantém em zero nos próximos 3 a 5 dias = risco neutralizado; sair de zero em qualquer ciclo = os pedidos entraram na janela oficial. Escalar se: taxa sair de zero antes do fechamento do ciclo de qualificação ao Platinum — sinalizar Kobe.
- Yasmin: acionar urgência de reposição ao CD do ML para os três Kit 10 Potes em cobertura crítica (1050ml 10 un, 1050ml 6 un e 640ml 6 un). Por que importa: três rupturas simultâneas em Full comprimem o portfólio ativo na mesma semana em que o ritmo precisa se sustentar para fechar o gap de R$ 26.538,39 até o Platinum. Como saber se resolveu: previsão de ETA do Platinum no próximo snapshot abaixo de 7 dias com ao menos um dos três com reposição confirmada = sob controle; ETA subindo acima de 8 dias sem reposição em vista = o patamar não se sustenta. Escalar se: nenhum dos três tiver reposição em trânsito confirmada em 2 dias.
- Yasmin: acompanhar a direção do nível de qualidade do Jogo Potes de Vidro 5 Peças (qualidade do anúncio em regular) e do Kit 4 Potes 1050ml (qualidade do anúncio em regular) — oitavo ciclo estável. Por que importa: são os dois principais anúncios da conta em zona penalizada; estabilidade não exige ação, mas qualquer queda combinada com o ADS respondendo por 60,9% do faturamento sinaliza perda de exposição orgânica não compensada. Como saber se resolveu: nível estável ou subindo nos próximos 2 ciclos = manter observação; qualidade caindo abaixo do ponto de corte em qualquer dos dois = alinhar com Himmel sobre cobertura preventiva de ADS.

Dia analisado: 29/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Citar "Kit 10 Potes 1050ml" sem especificar embalagem (sem "10 un" vs "6 un")
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** MLB4676726433 e MLB4676751119 compartilham display_name idêntico no sistema; citar sem embalagem cola os dois anúncios e perde precisão
- **Agregado autorizado:** não — distinção por embalagem ("10 un" / "6 un") é a solução determinada
- **Tratamento aplicado:** todos os trechos que citam os dois Kit 10 Potes 1050ml preservam explicitamente "10 un" e "6 un"
- **Aparece na mensagem final:** sim, como "Kit 10 Potes 1050ml — 10 un", "Kit 10 Potes 1050ml — 6 un"

---

- **Item bloqueado:** Afirmar que os 19 pedidos do Kit 6 Canecas Tulipa 250ml "vão virar cancelamento" como fato
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Granular declarou inconclusivo — snapshot é post-baixa; dois cenários igualmente compatíveis
- **Agregado autorizado:** não — manter linguagem de risco em aberto
- **Tratamento aplicado:** preservada linguagem de hipótese: "se parte desses pedidos virar cancelamento", "ainda não é possível confirmar"
- **Aparece na mensagem final:** sim, como risco latente com linguagem de indício

---

- **Item bloqueado:** Afirmar que ADS está priorizando ou amplificando algum anúncio específico
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** breakdown de spend/revenue por anúncio é pendência estrutural desde 22/05 — qualquer afirmação seria especulação
- **Agregado autorizado:** não
- **Tratamento aplicado:** ADS citado apenas em termos agregados (share 60,9%, sem atribuição a anúncio específico)
- **Aparece na mensagem final:** não há afirmação de priorização por anúncio

---

- **Item bloqueado:** Usar "health" ou citar pontuação numérica de qualidade de anúncio (ex.: "health 0,71")
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** vocabulário interno técnico; regra de vocabulário operacional ML obrigatória
- **Agregado autorizado:** não — substituir por nome de faixa ("qualidade do anúncio em regular")
- **Tratamento aplicado:** substituído por "qualidade do anúncio em regular" em todas as ocorrências; nenhum valor numérico de health exposto
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- **Metadados internos (`padrao`, `base`, `classificacao`) removidos** — são marcadores de pipeline; não pertencem à mensagem Slack
- **Classificação `risco latente` do insight 2 (Tulipa) preservada com linguagem de indício** — "se parte desses pedidos virar cancelamento", "ainda não é possível confirmar"; proibido transformar em certeza
- **Classificação `risco latente` do insight 3 (três Kit Potes) preservada com linguagem de indício** — "ruptura nos próximos um a dois dias é o cenário mais provável" (baseado em cobertura <1,5 dia com dado direto de available_quantity); mantida a ressalva de reposição não confirmada
- **Classificação `fato` do insight 1 preservada** — escrito como afirmação direta, sem "parece" ou "sugere"
- **Yasmin atribuída como responsável em todas as três prioridades** — a L05 não atribui responsável; atribuição feita na L06 conforme regra
- **Top Produtos: exatamente os 5 primeiros do `top_products`** — Potes Vidro 5 Peças (Tampa Preta, 1º), Kit 6 Canecas Tulipa 250ml (2º), Potes Vidro 5 Peças (Tampa Vermelha, 3º), Potes Vidro 5 Peças (Tampa Cinza, 4º), Kit 6 Canecas Lisas 200ml (5º)
- **Nenhum MLB visível na mensagem final** — todos os platform_item_id removidos do texto Slack
- **Nomes de produto — mapeamento canônico usado para todos os 5 do Top Produtos:**
  - IMB501P → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - TL6250 → usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)
  - IMB501V → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - IMB501C → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - CLR002 → usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
- **Nomes de produto na Análise e Prioridades — tradução do `title` da L05 para `slack_short_name`:**
  - "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" (L05) → "Kit 6 Canecas Tulipa 250ml" (slack_short_name TL6250)
  - "Jogo Potes de Vidro 5 Peças" (L05) → "Jogo Potes de Vidro 5 Peças" mantido com contexto (não está em Top 5 Produtos, mas referencia a família; a L05 usa essa denominação; preservado para precisão analítica)
  - "Kit 10 Potes 1050ml — 10 un" / "Kit 10 Potes 1050ml — 6 un" / "Kit 10 Potes 640ml — 6 un" → slack_short_names preservados com distinção de embalagem conforme bloqueio da L05
  - "Kit 4 Potes 1050ml" → usado `slack_short_name` "Kit 4 Potes 1050ml" (KIT4YW1050)
- **"health" substituído por "qualidade do anúncio em regular"** em todas as ocorrências; sem pontuação numérica exposta
- **"GMV" não aparece na mensagem** — substituído por "Faturamento" em todas as ocorrências
- **"ETA" não aparece na mensagem** — substituído por "previsão de" / "a ~6 dias" / "nos próximos X dias"
- **"cancellations_rate" não aparece na mensagem** — substituído por "taxa de cancelamentos"
- **"ADS share" não aparece na mensagem** — substituído por "ADS respondendo por 60,9% do faturamento"
- **"available_quantity" não aparece** — referenciado como "cobertura" ou "menos de 1,5 dia de cobertura"
- **Comparações temporais na seção VISÃO omitidas** — seção mostra apenas dados objetivos do dia; comparações (+51% vs 30d, +50% vs mesma sexta) mantidas apenas na seção ANÁLISE, vindas da L05
- **Modalidade de envio na seção VISÃO omitida** — dado de mix de modalidade de envio vem do `fulfillment_mix_yesterday_top10` com cobertura parcial (top 10 apenas, 65 pedidos de 143); a Condensadora não autorizou exibição com ressalva explícita nessa seção; tratado apenas na ANÁLISE
- **"fulfillment" não aparece na mensagem** — substituído por "Full" (modalidade) ou "CD do ML" (infraestrutura)
- **Insight 1 quebrado em duas frases** — frase original da L05 longa; quebrada em: (a) dado de patamar, (b) contraposição de risco; tese preservada intacta
- **"taxa de cancelamentos" no lugar de "elegibilidade"** — "elegibilidade" é jargão; substituído por "qualificação" / "janela de qualificação" conforme glossário
- **"breakeven"/"runway" não aparecem** — substituídos por "cobertura" e "dias de cobertura"
- **Sem frase padrão de dia neutro** — Condensadora entregou 3 insights; inaplicável
- **Sem prioridade de escalonamento ADS** — L05 não trouxe gatilho de Himmel neste ciclo para as prioridades; não adicionado