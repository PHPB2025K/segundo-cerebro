<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 24/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.024,80
- Pedidos: 99
- Ticket médio: R$ 50,76
- Cancelamentos: 2

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 29 pedidos
- Kit 4 Potes 1050ml — 18 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Kit 6 Canecas Lisas 200ml — 9 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 8 pedidos

🔍 ANÁLISE DA CONTA
- O Faturamento ficou dentro da banda esperada, mas a concentração está subindo. Os Potes Vidro 5 Peças (Tampa Preta, Vermelha e Cinza) juntos fizeram 47 dos 99 pedidos — e o anúncio está com qualidade em regular pelo quarto ciclo seguido. Isso sugere que a conta está vendendo cada vez mais por um anúncio que o ML vem reduzindo em aparecimento orgânico.
- O grupo de canecas teve dois alertas de estoque no mesmo dia. O Kit 6 Canecas 250ml fechou com 1 unidade restante após 3 pedidos — é Cross-Docking, reposição depende da Budamix. Sem reposição antes do próximo pedido, o ML cancela automaticamente e prejudica o cancellations_rate. O Kit 6 Canecas Lisas 200ml caiu de 33 para 25 unidades entre os últimos dois ciclos sem reposição visível — cobertura de ~2,8 dias no ritmo atual. Se romper, perde a Buy Box do Catálogo Premium, e a recuperação é lenta mesmo depois de reestocar.
- O ADS respondeu por 71% do Faturamento (ROAS 11x, ACOS 4,22%) — campanha eficiente, mas é o primeiro ponto da nova série depois do recuo de 23/05. Campanha eficiente em fase de leitura não se toca. O gatilho para alinhar com o Himmel só dispara se amanhã o ADS ficar acima de 65% pelo segundo dia seguido com a qualidade dos dois campeões ainda travada.

🎯 PRIORIDADES DO DIA
- Yasmin: checar estoque disponível e previsão de reposição ao CD do ML do Kit 6 Canecas Lisas 200ml (Catálogo Premium Full, 25 unidades, ~9 pedidos/dia). Por quê: é o único Catálogo Premium do top em queda de cobertura (~2,8 dias) — ruptura aqui derruba a Buy Box com recuperação lenta mesmo depois de reestocar, e prejudica o ritmo para o MercadoLíder Platinum. Confirmar/refutar por: reposição em trânsito com chegada prevista em até 48h = risco neutralizado; sem reposição confirmada em 24h = risco passou de iminente para ativo. Escalar se: cobertura cair abaixo de 2 dias sem reposição confirmada — Yasmin aciona quem gerencia o abastecimento Full (Trader/Kobe).
- Yasmin: checar status, estoque e pedidos em aberto do Kit 6 Canecas 250ml (Cross-Docking, 1 unidade restante) e pausar preventivamente se houver pedido novo entrando sem reposição. Por quê: o próximo pedido sem estoque vira cancelamento automático do ML, entra na janela rolling de cancellations_rate (hoje em zero) e aperta o gap para o MercadoLíder Platinum. Confirmar/refutar por: anúncio pausado com pedidos em aberto encaminhados = risco neutralizado; anúncio ativo com pedido novo sem estoque = pausa imediata antes do cancelamento automático.
- Yasmin: checar a qualidade dos anúncios Potes Vidro 5 Peças e Kit 4 Potes 1050ml no próximo snapshot — ambos em regular pelo quarto ciclo seguido, quinto ciclo é o ponto definidor. Não mexer em campanha hoje. Por quê: os dois somam 65 dos 99 pedidos do dia. Se a qualidade cair para preocupante em qualquer um, a erosão orgânica vira ativa e justifica alinhar com o Himmel. Se subir para bom, o risco enfraquece. Confirmar/refutar por: qualidade caindo para preocupante = erosão confirmada; chegando em bom = risco revertido; quinto ciclo estável em regular nos dois = degradação lenta confirmada, cobertura preventiva passa a ser urgente. Escalar se: qualidade cair para preocupante no quinto ciclo combinado com ADS no segundo dia acima de 65% — Yasmin alinha com Himmel sobre cobertura preventiva.

Dia analisado: 24/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atribuição dos 2 cancelamentos do dia a qualquer anúncio específico (incluindo Kit 6 Canecas 250ml / MLB6582645908)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** L04 declarou inconclusivo por falta de breakdown por platform_item_id — hipótese de origem concentrada não pode ser apresentada como fato
- **Agregado autorizado:** não
- **Tratamento aplicado:** o cancelamento automático prospectivo do Kit 6 Canecas 250ml é tratado exclusivamente como risco futuro condicional ("próximo pedido sem estoque vira cancelamento automático"), nunca como atribuição dos 2 cancelamentos já ocorridos
- **Aparece na mensagem final:** não (os 2 cancelamentos do dia aparecem apenas na VISÃO como dado objetivo; nenhuma atribuição a anúncio específico)

---

- **Item bloqueado:** Afirmação de que o ADS está cobrindo erosão orgânica especificamente dos dois campeões Full em nível regular (MLB3288536143 e MLB4073003575)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** L04 marcou como hipótese em aberto — sem breakdown de revenue_ads por anúncio, não é possível confirmar onde a receita ADS está concentrada
- **Agregado autorizado:** não
- **Tratamento aplicado:** insight 3 descreve ADS share e eficiência como fato + condição de gatilho, sem afirmar que o ADS está especificamente sobre os campeões em regular; linguagem mantida factual e condicional
- **Aparece na mensagem final:** não (hipótese suprimida; apenas os fatos e a condição de gatilho foram preservados)

---

- **Item bloqueado:** Tratar ADS share de 71% como gatilho ativo de escalonamento a Himmel hoje
- **Origem do bloqueio:** L02 Tática / L04 Granular / L05 Condensadora
- **Motivo:** É o primeiro ponto da nova série pós-recuo de 23/05 — o gatilho exige segundo ponto consecutivo em 25/05 com qualidade dos campeões estagnada
- **Agregado autorizado:** não aplicável (não é item bloqueado de produto — é bloqueio de interpretação)
- **Tratamento aplicado:** insight 3 e prioridade 3 explicitam que o gatilho é condicional ao segundo dia; nenhuma instrução de acionar Himmel hoje foi incluída
- **Aparece na mensagem final:** não (ADS share aparece como dado + condição futura; acionamento de Himmel só aparece nas condições de escalonamento da prioridade 3, como condicional)

---

- **Item bloqueado:** Afirmação de que o Kit 6 Canecas Porcelana Tulipa (MLB6167272090) está em ruptura ou pausado
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Anúncio ausente do top pelo segundo ciclo consecutivo é hipótese, não fato confirmável com o pacote disponível
- **Agregado autorizado:** não
- **Tratamento aplicado:** produto omitido integralmente da mensagem Slack
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- **Metadados internos (`padrao`, `base`, `classificacao`) removidos** — campos são internos de pipeline; não pertencem à comunicação com Yasmin
- **Insight 1 (risco latente) — nuance preservada com "sugere"** — classificação "risco latente" convertida para linguagem de indício: "isso sugere que a conta está vendendo cada vez mais por um anúncio que o ML vem reduzindo em aparecimento orgânico"; tese e concentração de 47 pedidos mantidas como fatos
- **Insight 2 (risco latente) — prospectivo preservado** — cobertura de ~2,8 dias e risco de Buy Box apresentados como consequências futuras condicionais ("se romper, perde a Buy Box"), não como fatos consumados
- **Insight 3 (hipótese) — condicionais preservados** — share de 71% apresentado como fato; a hipótese de que ADS está compensando erosão orgânica (bloqueada) foi suprimida; apenas o gatilho condicional (segundo dia consecutivo acima de 65%) foi preservado
- **`health` → "qualidade em [faixa]"** — `health` 0,71 e 0,75 traduzidos para "qualidade em regular" (faixa 0,70-0,84); valores numéricos omitidos conforme regra; limiares de cruzamento traduzidos para nomes de faixa: "≤ 0,69" → "cair para preocupante"; "≥ 0,85" → "chegar em bom"
- **`ETA` → "previsão de chegada"** — substituição aplicada na prioridade 1: "ETA ≤ 48h" → "chegada prevista em até 48h"
- **Modalidade de envio omitida da seção VISÃO** — `fulfillment_mix_yesterday_top10` cobre apenas o top 10 (~47 pedidos resolvidos de 99); sem cobertura total do dia, dado não é objetivo e pertence à análise; omitido conforme regra
- **Top Produtos — 5 primeiros do ranking exibidos; sem faturamento por produto** — pacote não fornece receita validada por variação; formato "nome — pedidos" aplicado
- **IMB501P (Potes Vidro 5 Peças — Tampa Preta)** — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico); `confirmed_variation_attributes: ["Tampa Preta"]` incluído conforme regra
- **KIT4YW1050 (Kit 4 Potes 1050ml)** — usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico); `confirmed_variation_attributes: []`, nenhum atributo a acrescentar
- **IMB501V (Potes Vidro 5 Peças — Tampa Vermelha)** — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico); `confirmed_variation_attributes: ["Tampa Vermelha"]` incluído conforme regra
- **CLR002 (Kit 6 Canecas Lisas 200ml)** — usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico); `confirmed_variation_attributes: []`, nenhum atributo a acrescentar
- **IMB501C (Potes Vidro 5 Peças — Tampa Cinza)** — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico); `confirmed_variation_attributes: ["Tampa Cinza"]` incluído conforme regra
- **MLB3288536143 na Análise — referência agregada ao bloco com 3 variações** — L05 usa o título ML genérico "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" para se referir ao anúncio com 3 SKUs filhos; L06 usa "Potes Vidro 5 Peças (Tampa Preta, Vermelha e Cinza)" na análise e "Potes Vidro 5 Peças" na prioridade 3 — denominador comum dos três `slack_short_name`, preservando os atributos de cor onde analiticamente relevante; nenhum atributo inferido além dos `confirmed_variation_attributes`
- **MLB6582645908 na Análise/Prioridade 2** — L05 usa "Kit 6 Canecas Porcelana 250ml Canelada Colorida" e "Kit 6 Canecas Porcelana 250ml Canelada Colorida Café Chá Colorida Canelada"; L06 usa `slack_short_name` "Kit 6 Canecas 250ml" (mapeamento canônico via KIT 6CAN250... aguarde — verificando: o produto K6CAN250 tem `slack_short_name: "Kit 6 Canecas 250ml"` e `platform_item_id: MLB6582645908`); denominação padronizada com o Top Produtos
- **MLB6232315532 na Análise/Prioridade 1** — L05 usa "Kit De 6 Canecas De Porcelana Lisa Reta 200 Ml" e forma longa; L06 usa `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico via CLR002); denominação padronizada com o Top Produtos
- **MLB4073003575 na Prioridade 3** — L05 usa "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo"; L06 usa `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico via KIT4YW1050); denominação padronizada com o Top Produtos
- **"Cluster de canecas" → "grupo de canecas"** — termo "cluster" traduzido para linguagem natural conforme glossário
- **"Exposição orgânica" → "aparecimento orgânico"** — simplificação de expressão técnica para linguagem operacional direta
- **"Pace" → "ritmo"** — tradução de anglicismo não listado no glossário mas fora do vocabulário natural; aplicado em prioridade 1
- **Responsável fixo Yasmin atribuído nas 3 prioridades** — L05 não atribui responsável; L06 atribui "Yasmin:" no início de cada prioridade conforme regra
- **"escalar_se: não aplicável" na prioridade 2** — linha "Escalar se" omitida da prioridade 2 conforme instrução de não preencher por obrigação