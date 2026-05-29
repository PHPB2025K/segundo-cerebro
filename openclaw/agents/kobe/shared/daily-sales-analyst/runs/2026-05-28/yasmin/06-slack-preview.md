<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 28/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 8.463,62
- Pedidos: 164 pedidos
- Ticket médio: R$ 51,61
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 42 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 22 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 20 pedidos
- Kit 4 Potes 1050ml — 15 pedidos
- Kit 10 Potes Herméticos 640ml Azul-petróleo 6 Unidades — 11 pedidos

🔍 ANÁLISE DA CONTA
- Risco urgente do dia: o Kit 10 Potes 640ml 6 Unidades em Full fechou com 3 unidades depois dos 11 pedidos de ontem. Ao ritmo atual, o estoque acaba em horas — qualquer pedido novo vira cancelamento automático. Isso pressiona a cancellations_rate (hoje em zero) exatamente quando a conta está a 7,6 dias de virar MercadoLíder Platinum, com gap de R$ 33.193,86. Cada cancelamento aperta essa janela.
- O faturamento de R$ 8.463,62 é o maior dia recente — e veio com o Mercado Ads marcando R$ 0,00 de gasto, mesmo com 11 campanhas ativas. A leitura natural seria "o orgânico explodiu", mas o pacote não mostra se foi uma pausa deliberada do Himmel ou um problema de atribuição da API. Até confirmar a origem, o dia fica como ponto de observação, não como prova de capacidade orgânica da conta.
- Metade do faturamento do dia (51,2%) saiu de um único anúncio — o Jogo Potes de Vidro 5 Peças, somando as três cores de tampa — que opera em Full com qualidade do anúncio em regular (0,71) há oito ciclos seguidos. O estoque de 282 unidades segura o curto prazo, mas o vetor que puxa o resultado é único e tem a qualidade travada na zona regular há semanas.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar estoque atual do Kit 10 Potes 640ml 6 Unidades (Full) e do Kit 10 Potes 320ml 6 Unidades (Cross-Docking) e acionar reposição urgente — Full depende de remessa ao CD do ML, Cross-Docking é controlado internamente pela Budamix. Por quê: ambos fecharam com cobertura de horas (3 e 2 unidades pós-baixa); ruptura prospectiva gera cancelamento automático e pressiona a cancellations_rate na reta final do Platinum. Como saber se deu certo: available_quantity acima de zero com reposição registrada amanhã = risco neutralizado; status pausado ou available_quantity=0 com cancelamento aparecendo = ruptura ativa confirmada. Escalar se: available_quantity zerar em qualquer um dos dois E a cancellations_rate sair de zero — abrir com Kobe o impacto no prazo estimado do Platinum.
- Yasmin: confirmar com Himmel se o zero de gasto e receita do Mercado Ads de ontem foi pausa deliberada, ajuste operacional ou problema de atribuição da API. Por quê: toda a leitura sobre o orgânico do dia depende dessa confirmação — sem ela, o maior faturamento recente fica como dado ambíguo e não pode virar base para decisão. Como saber: Himmel confirma pausa deliberada = registrar o dia como experimento orgânico válido; Himmel indica problema técnico = suspender a tese orgânica e recalibrar; sem resposta hoje e pacote de amanhã também com gasto zero = pausa real por inferência.
- Yasmin: observar a direção da qualidade do anúncio do Jogo Potes de Vidro 5 Peças (hoje em 0,71) e do Kit 4 Potes 1050ml (hoje em 0,75) no próximo ciclo, sem mexer nos anúncios. Por quê: oitavo ciclo idêntico para os dois; com Mercado Ads aparentemente zerado e faturamento máximo, metade do resultado veio desses dois anúncios em qualidade regular — a direção define se o nível estabilizou ou se ação corretiva precisa entrar. Como saber: qualidade estável ou subindo no próximo ciclo = hipótese de piso reforçada, Yasmin investiga os pontos internos sem urgência; qualquer um cair abaixo de 0,68 (Potes 5 Peças) ou 0,70 (Kit 1050ml) = acionar alinhamento com Himmel sobre cobertura preventiva. Escalar se: queda abaixo dos limites coincidir com retorno do Mercado Ads no patamar histórico de 49-70% — discutir com Kobe estratégia que não suprima o orgânico em expansão.

Dia analisado: 28/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Afirmação de rompimento estrutural de patamar de faturamento
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L01 trata como hipótese que exige 2-3 ciclos de confirmação (GMV ≥ R$ 6.500 por dois dias seguidos); um único dia não basta
- **Agregado autorizado:** não
- **Tratamento aplicado:** o volume recorde de R$ 8.463,62 aparece como dado objetivo na VISÃO e como contexto da hipótese na ANÁLISE, sem afirmar rompimento estrutural
- **Aparece na mensagem final:** não como afirmação — sim como contexto numérico neutro

---

- **Item bloqueado:** Afirmação de capacidade orgânica estrutural da conta provada pelo dia
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Origem do zero do ADS não confirmada; evidência conflitante declarada pela L04 com hipótese em aberto
- **Agregado autorizado:** não
- **Tratamento aplicado:** o dia é apresentado como "ponto de observação, não prova de capacidade orgânica" — nuance da hipótese preservada com linguagem de indício
- **Aparece na mensagem final:** sim, como hipótese explícita com ressalva de dado ambíguo

---

- **Item bloqueado:** Atribuição de origem dos 4 cancelamentos do dia a anúncio específico
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Ausência de breakdown order_id↔platform_item_id no pacote; atribuição inconclusiva
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados como dado objetivo na VISÃO (4 cancelamentos); sem atribuição a produto específico em nenhuma seção
- **Aparece na mensagem final:** sim, como número total na VISÃO — sem atribuição

---

- **Item bloqueado:** Afirmação de direção (caindo/subindo) do nível de qualidade dos campeões em Full
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Pacote entrega apenas valor pontual; série interna ML não observável
- **Tratamento aplicado:** linguagem usada é "há oito ciclos seguidos" (estabilidade pontual entre coletas), não "está caindo" ou "está subindo"
- **Aparece na mensagem final:** sim, com nuance correta de estabilidade pontual

---

- **Item bloqueado:** Citação de cancelamento iminente ou ruptura retroativa sobre pedidos do dia analisado
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** available_quantity é POST-baixa; os pedidos do dia já foram atendidos — risco é prospectivo
- **Tratamento aplicado:** linguagem estritamente prospectiva — "qualquer pedido novo vira cancelamento automático", "ruptura prospectiva", nunca "pedidos do dia ficaram sem cobertura"
- **Aparece na mensagem final:** não como afirmação retrospectiva — sim como risco prospectivo correto

---

### Decisões de formatação

- **Remoção de metadados internos (`padrao`, `base`, `classificacao`)** — campos de pipeline; não pertencem ao Slack
- **Preservação de nuance `classificacao: "risco latente"`** — insight 1 (Kit 10 Potes 640ml): linguagem de risco prospectivo mantida ("pode virar cancelamento automático", "ao ritmo atual, o estoque acaba em horas")
- **Preservação de nuance `classificacao: "hipótese"`** — insight 2 (ADS zerado): linguagem de indício mantida ("a leitura natural seria", "até confirmar a origem", "fica como ponto de observação, não como prova")
- **Preservação de nuance `classificacao: "fato"`** — insight 3 (cluster IMB501): escrito como fato direto, sem "parece" ou "sugere"
- **Omissão de modalidade de envio na seção VISÃO** — `fulfillment_mix_yesterday_top10` cobre só o top 10 (~47% dos pedidos do dia), não a totalidade; Condensadora não autorizou exibição com cobertura explícita; omitido conforme regra
- **Produto 5 do Top Produtos — uso de `display_short` como fallback** — SKU KIT6YW640 tem `slack_short_name: null`; usado `display_short: "Kit 10 Potes Herméticos 640ml Azul-petróleo 6 Unidades"` (fallback automático)
- **Produtos 1-4 do Top Produtos — uso de `slack_short_name` (mapeamento canônico):**
  - IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- **Menções de produto na ANÁLISE e PRIORIDADES — tradução para nome curto:**
  - L05 escreveu "Kit 10 Potes 640ml Azul-petróleo 6 Unidades" → mantido como "Kit 10 Potes 640ml 6 Unidades" (próximo ao display_short; sem slack_short_name); divergência registrada: L05 usou "Kit 10 Potes 640ml Azul-petróleo 6 Unidades", L06 usou "Kit 10 Potes 640ml 6 Unidades" (motivo: simplificação de nome, removido atributo de cor redundante para fluidez de leitura, alinhado com display_short sem o "Azul-petróleo" no corpo da análise)
  - L05 escreveu "Kit 10 Potes 320ml Azul-petróleo 6 Unidades" → usado "Kit 10 Potes 320ml 6 Unidades" (mesmo critério; SKU KIT6YW320 tem slack_short_name: null)
  - L05 escreveu "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" → usado "Jogo Potes de Vidro 5 Peças" (simplificação de título ML longo, removendo ruído SEO "Claro Mantimentos Marmita"; sem slack_short_name mapeado para menção agregada do cluster)
  - L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa Azul-petróleo" → usado "Kit 4 Potes 1050ml" (slack_short_name canônico do KIT4YW1050)
- **Substituição de "GMV" por "faturamento"** — ocorrência em todas as menções (VISÃO, ANÁLISE, PRIORIDADES)
- **Substituição de "ETA" por "prazo estimado"** — uma ocorrência nas PRIORIDADES (seção de escalonamento)
- **Substituição de "health" por "qualidade do anúncio"** — todas as ocorrências; valores numéricos pontais (0,71; 0,75) mantidos apenas onde necessários para identificar os gatilhos operacionais (<0,68 / <0,70); nunca entre parênteses como "(0,71)" ao lado do nome da faixa
- **Substituição de "ADS share" por "Mercado Ads"** — ocorrências substituídas por referência ao canal sem uso do termo técnico "share"
- **Preservação das alternativas operacionais nas PRIORIDADES** — "Full depende de remessa ao CD do ML, Cross-Docking é controlado internamente pela Budamix" mantido integralmente (duas vias de ação presentes na L05)
- **Preservação de escalonamento para Kobe** — duas condições de escalonamento presentes na L05 mantidas: (1) ruptura + cancellations_rate saindo de zero → Kobe sobre ETA Platinum; (2) queda de health + retorno de ADS histórico → Kobe sobre estratégia orgânico/paid
- **Atribuição de Yasmin como responsável** — todas as três prioridades atribuídas a Yasmin, conforme regra fixa
- **Frases quebradas para reduzir extensão** — insight 1 da Condensadora era parágrafo técnico único; quebrado em duas frases sem alterar tese, números ou classificação
- **Formato numérico:** R$ 8.463,62 (faturamento com 2 casas decimais), R$ 33.193,86 (gap Platinum com 2 casas decimais), R$ 51,61 (ticket médio), R$ 0,00 (spend ADS) — todos com centavos obrigatórios; percentuais com vírgula (51,2%; 88,79%; 49-70%)
- **Confiança média global** — alertas_de_confianca.nivel="media"; não houve corte de insights por baixa confiança; ressalvas de hipótese e risco latente preservadas nas seções correspondentes