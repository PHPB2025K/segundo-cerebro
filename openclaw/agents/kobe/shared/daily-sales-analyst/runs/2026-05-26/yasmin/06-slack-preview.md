<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 26/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 7.394,36
- Pedidos: 143 pedidos
- Ticket médio: R$ 51,71
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 40 pedidos
- Kit 4 Potes 1050ml — 21 pedidos
- Kit 6 Canecas Lisas 200ml — 15 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 12 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 12 pedidos

🔍 ANÁLISE DA CONTA
- O faturamento de R$ 7.394,36 é o segundo maior numa terça da série e bate +57% acima da média do mês — mas o resultado é real e frágil ao mesmo tempo: 94% do volume dos produtos mais vendidos rodou via Full, e o ADS carregou 61% do faturamento. Por baixo, os dois campeões são anúncios Clássico com qualidade do anúncio em regular há sete ciclos seguidos (Potes Vidro 5 Peças em regular e Kit 4 Potes 1050ml em regular), e o ADS está cobrindo o que o orgânico perdeu.
- O risco silencioso do dia não é a Tulipa — é o Kit 6 Canecas Lisas 200ml, único Catálogo Full do top 10, que entrou pela primeira vez na zona crítica: 31 unidades depois de 15 pedidos no dia, cobertura prospectiva de ~2 dias. Ruptura em Catálogo derruba a Buy Box e a recuperação é lenta, e a reposição depende de lead time até o CD do ML — checar antes do fim do dia.
- Sétimo ciclo seguido com a qualidade dos dois campeões em Full no mesmo patamar — sem queda, sem recuperação. O gatilho para acionar o Himmel (cair abaixo de 0,68 em qualquer um dos dois) não foi atingido; a decisão certa hoje é continuar observando, sem mexer em ADS nem pausar anúncio.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar status e reposição do Kit 6 Canecas Tulipa 250ml — anúncio segue ativo em Full com 2 unidades depois dos 4 pedidos do dia; risco de cancelamento automático amanhã que entra direto na janela do MercadoLíder Platinum (gap de R$ 42.460,66, progresso 85,7%, prazo estimado ~10 dias). Confirmar/refutar por: reposição confirmada chegando ao CD em 24h = risco resolvido; sem reposição confirmada = decidir entre cancelamento controlado dos pedidos excedentes ou pausa preventiva antes do ML cancelar automático. Escalar se: cancelamento automático for registrado no dia ou o indicador de cancelamentos da reputação sair de zero.
- Yasmin: checar cobertura e reposição em trânsito do Kit 6 Canecas Lisas 200ml (único Catálogo Full do top 10) — 31 unidades depois de 15 pedidos, cobertura prospectiva ~2 dias. Ruptura em Catálogo derruba Buy Box e recupera devagar; a reposição depende de lead time até o CD do ML, não da expedição da Budamix. Confirmar/refutar por: reposição confirmada chegando ao CD em até 2 dias = risco resolvido; estoque caindo abaixo de 10 unidades sem reposição confirmada = elevar para prioridade emergencial amanhã. Escalar se: estoque cair abaixo de 10 unidades sem reposição em trânsito, ou anúncio entrar em ruptura com perda de Buy Box.
- Yasmin: seguir observando a qualidade dos dois campeões em Full (Potes Vidro 5 Peças e Kit 4 Potes 1050ml) — sem ação com o Himmel hoje; o gatilho é qualquer um dos dois cair abaixo de 0,68. Mexer em ADS que está cobrindo a lacuna orgânica antes de confirmar queda colapsaria o faturamento. Confirmar/refutar por: próximo ciclo com qualquer um abaixo de 0,68 = acionar alinhamento com o Himmel sobre cobertura preventiva; estabilidade mantida = seguir observação. Escalar se: qualquer um dos dois cair abaixo de 0,68, ou o ADS carregar acima de 65% do faturamento com ACOS acima de 12% por dois ciclos seguidos.

Dia analisado: 26/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atribuição dos 3 cancelamentos do dia a um anúncio específico (MLB4676726433 ou Kit 6 Canecas Tulipa 250ml)
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Granular declarou inconclusivo por falta de breakdown order_id↔platform_item_id; atribuição seria hipótese não sustentada
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados como dado objetivo (3 cancelamentos) na VISÃO, sem atribuição a anúncio específico; sinal não mencionado na análise
- **Aparece na mensagem final:** sim, apenas o número agregado "Cancelamentos: 3" na VISÃO — sem atribuição de origem

---

- **Item bloqueado:** Afirmação de que o ADS está priorizando os campeões com nível de qualidade regular
- **Origem do bloqueio:** L04 Granular / L05 Condensadora
- **Motivo:** Pendência estrutural recorrente — sem breakdown de ADS por platform_item_id, hipótese de dependência circular não é confirmável
- **Agregado autorizado:** não
- **Tratamento aplicado:** análise menciona que "ADS está cobrindo o que o orgânico perdeu" (relação causal geral confirmada) sem afirmar que os anúncios específicos com qualidade degradada são os priorizados
- **Aparece na mensagem final:** não — a atribuição direta está ausente; apenas o fato de que ADS cobre lacuna orgânica

---

- **Item bloqueado:** Códigos MLB (platform_item_id) visíveis na mensagem
- **Origem do bloqueio:** L05 Condensadora / regra estrutural L06
- **Motivo:** Usar nome comercial; MLB só em rastreabilidade técnica interna
- **Agregado autorizado:** não aplicável (regra de formatação)
- **Tratamento aplicado:** todos os MLB substituídos por nomes comerciais (`slack_short_name` ou agregado descritivo) em todas as seções
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- **Remoção de metadados internos (`padrao`, `base`, `classificacao`)** — campos são metadados de pipeline, não vão para o Slack; classificações de hipótese/risco latente preservadas via linguagem de indício ("real e frágil", "risco silencioso")
- **Preservação de nuance por `classificacao: "risco latente"` (insights 1 e 2)** — linguagem usada: "resultado é real e frágil", "risco silencioso", "entrou pela primeira vez na zona crítica"; não afirmado como fato consumado
- **Preservação de classificação `fato` (insight 3)** — sétimo ciclo idêntico e decisão de não acionar Himmel escritos como fato direto, sem linguagem de indício
- **Confiança média** — não há ressalva explícita de "sem base suficiente" porque a L05 declarou confiança média com base robusta; os pontos inconclusivos específicos já estão refletidos nos bloqueios acima
- **Tradução de termos técnicos:**
  - `health` → "qualidade do anúncio" / "regular" (faixa 0,70–0,84); sem pontuação numérica (0,71 / 0,75) no texto da análise, apenas nas prioridades onde o gatilho numérico é operacionalmente necessário para Yasmin saber quando agir
  - `ETA` → "prazo estimado"
  - `ADS share` → "o ADS carregou X% do faturamento"
  - `GMV` → "Faturamento" (em todos os casos)
  - `cancellations_rate` → "indicador de cancelamentos da reputação"
  - `fulfillment` → "Full" (modalidade de envio; palavra "fulfillment" ausente do Slack)
  - `Buy Box` → mantido (termo ML conhecido)
  - `available_quantity` → "unidades" / "unidades depois dos X pedidos"
  - Referência a "dependência circular" / "erosão orgânica" → substituída por linguagem direta: "o ADS está cobrindo o que o orgânico perdeu"
- **Nomes de produto — mapeamento canônico:**
  - `IMB501P` → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
  - `KIT4YW1050` → usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico)
  - `CLR002` → usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)
  - `IMB501C` → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
  - `IMB501V` → usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
  - `TL6250` → usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico) — mencionado na análise e prioridades; **não** aparece no Top 5 (6º lugar no ranking = fora dos 5 exibidos)
  - `MLB6232315532` (Kit 6 Canecas Lisas 200ml) nas seções de análise e prioridades: nome já mapeado via `slack_short_name` "Kit 6 Canecas Lisas 200ml" — consistente com Top Produtos
- **Divergência de denominação cross-layer:** L05 escreveu nos insights "Jogo Potes de Vidro 5 Peças" e "Kit 4 Potes 1050ml" e "Kit 6 Canecas Lisas 200ml"; L06 usou respectivamente "Potes Vidro 5 Peças" (com atributo de tampa quando necessário para distinguir variação) e "Kit 4 Potes 1050ml" e "Kit 6 Canecas Lisas 200ml" — padronização com `slack_short_name` canônico
- **Top Produtos — 5 primeiros do ranking:** posições 1–5 são IMB501P (40), KIT4YW1050 (21), CLR002 (15), IMB501C (12), IMB501V (12); exibidos exatamente nessa ordem; produtos 6–10 não aparecem no Top Produtos mas podem ser citados na análise e prioridades (TL6250 e MLB6232315532)
- **Modalidade de envio ausente da VISÃO MERCADO LIVRE** — dado `fulfillment_mix_yesterday_top10` cobre apenas top 10 (71 pedidos dos 143), não representa totalidade do dia; omitida da VISÃO e tratada apenas na análise onde a Condensadora a trouxe com contexto de cobertura parcial
- **Atribuição de Yasmin como responsável** em todas as prioridades — L05 não atribui responsável; L06 aplica conforme regra
- **Quebras de frase aplicadas:** insight 1 da L05 era uma frase muito longa; dividido em duas cláusulas com ponto e vírgula + parágrafo, mantendo todos os termos analíticos intactos
- **Valor R$ 7.394 da L05** — a L05 usou "R$ 7.394" (sem centavos) no texto do insight; na mensagem Slack escrito como "R$ 7.394,36" (regra de centavos obrigatórios) usando o valor validado do pacote L00; gap de Platinum escrito como "R$ 42.460,66" consistente com o dado do snapshot