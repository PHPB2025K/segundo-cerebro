<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 27/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 7.150,57
• Pedidos: 133
• Ticket médio: R$ 53,76
• Cancelamentos: 6

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 39 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 14 pedidos
• Kit 4 Potes 1050ml — 13 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 11 pedidos
• Kit 6 Canecas Lisas 200ml — 11 pedidos

🔍 ANÁLISE DA CONTA
• O Kit 10 Potes 1050ml — 10 un está em Full com Frete Grátis com 4 unidades no CD do ML pós-baixa de 5 pedidos — cobertura abaixo de 1 dia. O perfil é o mesmo do dia 25/05, quando o anúncio entrou em ruptura e esteve associado a 3 cancelamentos. Os cancelamentos do dia dobraram (de 3 para 6) exatamente no ciclo em que ele volta para essa zona, o que sugere que o risco está ativo. A urgência é checar reposição antes que vire cancelamento automático: a taxa de cancelamento está em 0% e o limite para virar MercadoLíder Platinum é 0,5% — com 9 dias até a janela de promoção, cada cancelamento automático conta.
• O faturamento rompeu para cima em todos os períodos de comparação: +27% vs média dos últimos 30 dias, +41% vs a mesma quarta-feira. O crescimento é real. A ressalva: 67,3% do faturamento veio de ADS — segundo ciclo consecutivo acima de 65% — e os Potes Vidro 5 Peças e o Kit 4 Potes 1050ml seguem com qualidade do anúncio em regular há 8 ciclos sem recuperação. O orgânico dos campeões não acompanhou o crescimento: quem está carregando é a campanha, não o ranking.
• A migração dos Potes Vidro 5 Peças para Full está confirmada — as três variações (Tampa Preta, Cinza e Vermelha) operam agora inteiramente no CD do ML. O anúncio entregou 48% dos pedidos do dia, todos em Full. Isso muda a leitura do canal: campeões respondem 100% em Full enquanto a base ativa da conta é 40,7% Full. Qualquer falha de reposição no topo tem impacto direto, sem amortecimento.

🎯 PRIORIDADES DO DIA
• Yasmin: checar agora se há reposição em trânsito ao CD do ML para o Kit 10 Potes 1050ml — 10 un (4 unidades pós-baixa, Full com Frete Grátis, perfil de ruptura idêntico ao de 25/05). É o candidato mais direto para explicar a duplicação dos cancelamentos (3→6) e o vetor mais provável de afetar a taxa de cancelamento antes da virada para MercadoLíder Platinum, que está a 9 dias. Como saber se deu certo: reposição confirmada em trânsito nas próximas 24h = risco neutralizado; anúncio pausado ou sem reposição confirmada = monitorar a taxa de cancelamento da reputação nos próximos 5 ciclos. Escalar se: próximo ciclo mostrar taxa de cancelamento acima de 0% na reputação oficial — abrir alinhamento direto com Kobe sobre o risco de não se qualificar para Platinum.
• Yasmin: registrar o percentual do faturamento via ADS hoje (67,3%) e comparar com amanhã antes de qualquer ação sobre as campanhas. Hoje é o segundo ciclo seguido acima de 65% (22/05 foi 69,9%); se amanhã fechar acima de 65% também, é hora de conversar com Himmel sobre cobertura e composição das campanhas. Mexer agora é precipitado — o portfolio está eficiente (ROAS 10,38x, ACOS 9,63%). Como saber se deu certo: percentual via ADS ≥ 65% amanhã = Yasmin abre conversa com Himmel nos próximos 1–2 dias; percentual via ADS abaixo de 60% = sinal de dependência enfraquece, observar mais 3 ciclos.
• Yasmin: observar o Kit 6 Canecas Tulipa 250ml no próximo ciclo — 16 unidades pós-baixa de 6 pedidos, cobertura ~2,7 dias. Saiu da zona crítica imediata, mas o padrão de reposição parcial é recorrente e em Full a ruptura ocorre sem aviso. Como saber se deu certo: estoque acima de 10 unidades no próximo ciclo = monitoramento passivo; estoque de 5 unidades ou menos = ação imediata no mesmo nível do Kit 10 Potes 1050ml.

Dia analisado: 27/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** `avg_acos_pct=44,85%` citado como sinal de campanha ineficiente; uso da expressão `ADS share` solta no texto
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Divergência declarada pela L04 — portfolio está eficiente (ACOS calculado total 9,63%, ROAS 10,38x); o 44,85% é média simples entre 11 campanhas que indica heterogeneidade, não ineficiência acionável. Sem breakdown por platform_item_id, citar como problema induziria Yasmin ao erro. "ADS share" é termo técnico proibido no Slack (tabela de tradução obrigatória).
- **Agregado autorizado:** sim — "percentual do faturamento via ADS", ROAS 10,38x e ACOS 9,63% (portfolio calculado)
- **Tratamento aplicado:** `avg_acos_pct=44,85%` omitido integralmente. Eficiência do portfolio comunicada via ROAS e ACOS calculado total. "ADS share" traduzido para "percentual do faturamento via ADS" e "X% do faturamento veio de ADS" em todas as ocorrências.
- **Aparece na mensagem final:** não — o valor 44,85% não aparece; a expressão "ADS share" não aparece.

---

- **Item bloqueado:** Atribuição nominal dos 6 cancelamentos do dia ao `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades` (MLB4676726433)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 marcou hipótese em aberto — o anúncio entregou 5 pedidos no dia, portanto no máximo 5 dos 6 cancelamentos poderiam vir dele; sem breakdown order_id↔platform_item_id, atribuição é circunstancial.
- **Agregado autorizado:** sim — "candidato mais direto para explicar a duplicação dos cancelamentos"
- **Tratamento aplicado:** Na ANÁLISE: "esteve associado a 3 cancelamentos (episódio 25/05)" e "sugere que o risco está ativo". Na PRIORIDADE: "É o candidato mais direto para explicar a duplicação dos cancelamentos (3→6)". Não afirmado que o produto causou os 6 cancelamentos.
- **Aparece na mensagem final:** sim, como candidato hipotético — linguagem de indício preservada em todas as menções.

---

- **Item bloqueado:** Afirmação de que a qualidade do anúncio do `Jogo Potes De Vidro 5 Peças Claro` (MLB3288536143) e do `Kit 4 Potes De Vidro Hermético 1050ml` (MLB4073003575) está "caindo"
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** L04 confirmou 8º ciclo idêntico (0,71 e 0,75) sem worsening — direção não é observável pela série interna do ML.
- **Agregado autorizado:** sim — "qualidade do anúncio em regular há 8 ciclos sem recuperação"
- **Tratamento aplicado:** Escrito como "seguem com qualidade do anúncio em regular há 8 ciclos sem recuperação" — sem afirmar direção de queda.
- **Aparece na mensagem final:** sim, na forma autorizada pela Condensadora.

---

### Decisões de formatação

**Top Produtos — nomes canônicos usados:**
- IMB501P — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- IMB501C — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- KIT4YW1050 — usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico)
- IMB501V — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- CLR002 — usado `slack_short_name` "Kit 6 Canecas Lisas 200ml" (mapeamento canônico)

**Análise e Prioridades — nomes canônicos usados:**
- `Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades` (MLB4676726433, KIT10YW1050) — usado `slack_short_name` "Kit 10 Potes 1050ml — 10 un" (mapeamento canônico) em ANÁLISE e PRIORIDADES
- `Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita` (MLB3288536143, listing-pai) — usado "Potes Vidro 5 Peças" (sem cor) em ANÁLISE, pois os insights 2 e 3 da L05 se referem ao listing-pai na análise de qualidade do anúncio e migração de modalidade de envio; nenhum `slack_short_name` exclusivo existe para o aggregate — decisão: usar prefixo comum dos três `slack_short_names` (Tampa Preta/Cinza/Vermelha) para manter leitura consistente. No Top Produtos, cada variação mantém o `slack_short_name` com cor.
- `Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo` (MLB4073003575) — usado `slack_short_name` "Kit 4 Potes 1050ml" (mapeamento canônico) em ANÁLISE
- `Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara` (MLB6167272090, TL6250) — usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico) em PRIORIDADES

**Divergência de denominação cross-layer registrada:**
- L05 escreveu "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" nos insights 2 e 3. L06 traduziu para "Potes Vidro 5 Peças" (aggregate, sem cor) — motivo: análise refere-se ao listing-pai (health compartilhado, logistic_type compartilhado por arquitetura ML).
- L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" no insight 2. L06 traduziu para "Kit 4 Potes 1050ml" — padronização com `slack_short_name` canônico.
- L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" na prioridade 3. L06 traduziu para "Kit 6 Canecas Tulipa 250ml" — padronização com `slack_short_name` canônico.
- L05 escreveu "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" no insight 1 e prioridade 1. L06 traduziu para "Kit 10 Potes 1050ml — 10 un" — padronização com `slack_short_name` canônico.

**Preservação de classificações:**
- Insight 1 (risco latente) — linguagem de indício preservada em todas as ocorrências: "sugere que o risco está ativo", "esteve associado", "candidato mais direto", "vetor mais provável". Não afirmado como fato.
- Insight 2 (fato) — escrito como fato direto; ressalva interna ao insight (orgânico não acompanhou) mantida como afirmação direta, não hipótese.
- Insight 3 (fato) — escrito como fato confirmado: "está confirmada".

**Remoção de metadados internos:**
- Campos `padrao`, `base` e `classificacao` da L05 não aparecem na mensagem Slack.

**Terminologia substituída (tabela de tradução obrigatória):**
- "patamar" → "crescimento é real" (insight 2)
- "ADS share" → "percentual do faturamento via ADS" / "X% do faturamento veio de ADS"
- "elegibilidade" → "qualificação para Platinum" / "virar MercadoLíder Platinum"
- "threshold" → "limite"
- "janelas" (temporais) → "períodos de comparação"
- "dependência estrutural" → "sinal de dependência"
- "gatilho documentado de alinhamento com Himmel" → "é hora de conversar com Himmel"
- "mix de campanhas" → "composição das campanhas"
- "health" → "qualidade do anúncio" + nome da faixa (regular) — sem pontuação numérica entre parênteses

**Qualidade do anúncio — formato aplicado:**
- MLB3288536143: `health=0,71` → faixa 0,70–0,84 → "qualidade do anúncio em regular" (sem número)
- MLB4073003575: `health=0,75` → faixa 0,70–0,84 → "qualidade do anúncio em regular" (sem número)

**Modalidade de envio na VISÃO:**
- Omitida — `fulfillment_mix_yesterday_top10` cobre apenas 54 de 133 ordens do dia (~41%), não representa a totalidade. Condensadora não autorizou exibição com ressalva de cobertura explícita. Modalidade de envio tratada apenas na ANÁLISE, onde a migração do IMB501 é contexto analítico da L05.

**Comparações temporais:**
- Mantidas exclusivamente na ANÁLISE DA CONTA. VISÃO mostra apenas dados objetivos do dia sem comparação.

**Atribuição de responsável:**
- Yasmin atribuída como responsável nas três prioridades, conforme regra fixa da L06 para Mercado Livre.

**Produtos citados fora do Top 5 visível:**
- Kit 10 Potes 1050ml — 10 un (posição 7 no top 10, 5 pedidos) — citado em ANÁLISE e PRIORIDADES por relevância analítica (risco de ruptura e impacto em Platinum). Autorizado pelas regras de cardinalidade diferente entre Top Produtos e Análise/Prioridades.
- Kit 6 Canecas Tulipa 250ml (posição 6 no top 10, 6 pedidos) — citado em PRIORIDADES por monitoramento preventivo. Autorizado pela mesma regra.