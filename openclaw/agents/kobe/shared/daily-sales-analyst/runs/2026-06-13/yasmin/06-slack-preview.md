<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 13/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.421,27
- Pedidos: 117
- Ticket médio: R$ 46,34
- Cancelamentos: 4

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes Vidro 5 Peças — Tampa Preta — 37 pedidos
- Potes Vidro 5 Peças — Tampa Cinza — 13 pedidos
- Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
- Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo — 8 pedidos
- Kit 10 Potes 520ml — 6 pedidos

🔍 ANÁLISE DA CONTA
- O Kit 3 Potes Vidro Hermético Tampa Azul-petróleo (Full) fechou o sábado com 4 unidades e a leitura desta manhã ainda aparece ativo, sem restock. Sem ação antes de segunda, pode pausar automaticamente — e em Full, pausa com pedidos em aberto vira cancelamento prospectivo, pressionando o cancellations_rate (hoje em zero). Esse é o único caminho que pode comprometer o Platinum sem o Faturamento cair.
- Os 51,3% do dia atribuídos aos Potes de Vidro 5 Peças escondem a concentração real: 42,7% dependem de um único anúncio Full — as variações Tampa Preta e Tampa Cinza no mesmo anúncio — com qualidade do anúncio em regular no 18º+ ciclo seguido. A Tampa Vermelha fica em um anúncio separado, Cross-Docking, e não carrega esse risco de perda de posição gradual.
- O ADS respondeu por 62,3% do Faturamento — mas não é aumento de campanha. É o quarto sábado seguido com o mesmo padrão: quando o Faturamento comprime, a proporção do ADS sobe naturalmente. A campanha está eficiente — ROAS 14,34x, ACOS 4,4%. A leitura de quanto as vendas orgânicas sustentam a conta só vale em dias com Faturamento ≥ R$ 6.000,00.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar agora o Kit 3 Potes Vidro Hermético Tampa Azul-petróleo (Full, 4 unidades) e decidir — repor ao CD do ML ou pausar de forma controlada antes da abertura de segunda. Por quê: pausa automática em Full com pedidos em aberto gera cancelamentos prospectivos e é o único caminho que pode mover o cancellations_rate de zero — critério qualitativo do Platinum que não depende de queda no Faturamento. Confirmar/refutar por: estoque acima de 15 unidades na próxima leitura = risco neutralizado; anúncio pausado com pedidos novos = acompanhar cancellations_rate no ciclo seguinte. Escalar se: cancellations_rate sair de zero na leitura de amanhã.
- Yasmin: confirmar se há reposição a caminho do CD do ML para o Kit 4 Potes 1050ml (Full gold_pro, 11 unidades, quarto ciclo sem restock desde 09/06). Por quê: ao ritmo atual, a cobertura é de ~2,2 dias — sem restock até terça, entra no mesmo nível de urgência do Kit 3 Potes; e em anúncio gold_pro com qualidade do anúncio em regular, recuperar posição depois de uma pausa é mais lento. Confirmar/refutar por: estoque acima de 20 unidades na próxima leitura = restock suficiente; estoque abaixo de 5 unidades em qualquer leitura das próximas 48h = urgência equivalente ao Kit 3 Potes. Escalar se: estoque abaixo de 5 amanhã ou prazo de reposição não confirmado pela operação.
- Yasmin: registrar o ADS de ontem (62,3% do Faturamento, ROAS 14,34x, ACOS 4,4%) como ponto de série com contexto "sábado, Faturamento R$ 5.421,27, volume abaixo da média" — e não acionar Himmel agora. Por quê: a série que define dependência de mídia paga só vale em dias com Faturamento ≥ R$ 6.000,00; tocar em campanha eficiente pelo motivo errado quebra o que está funcionando. Confirmar/refutar por: dois dos próximos três dias úteis com Faturamento ≥ R$ 6.000,00 e ADS abaixo de 45% = conta sustenta resultado sem depender de campanha; dois pontos acima de 55% = recolocar discussão com Himmel. Escalar se: ADS acima de 55% em dois dos próximos três dias úteis com Faturamento ≥ R$ 6.000,00.

Dia analisado: 13/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos. `o_que_nao_pode_ir_para_slack` da L05 está vazio — todos os produtos e insights do dia foram autorizados para Slack sem restrição.

---

### Decisões de formatação

**Metadados internos**
- Campos `padrao`, `base` e `classificacao` da L05 removidos de todos os insights — são metadados de pipeline, não vão para Slack.

**Preservação de nuance por classificação**
- Insight 1 (classificacao: "risco latente"): mantida linguagem de possibilidade — "pode pausar automaticamente", "pode comprometer", "pode mover". Risco real, mas ainda prospectivo; proibido escrever como fato consumado.
- Insights 2 e 3 (classificacao: "fato"): escritos como afirmações diretas, sem "parece" ou "sugere".

**Confiança alta**
- `alertas_de_confianca.nivel = "alta"` — sem ressalva geral necessária. Todos os 3 insights apresentados com convicção proporcional à classificação de cada um.

**Nomes de produto — Top Produtos (5 primeiros):**
- IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- KIT4YW640 — usado display_short "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo" (fallback automático; sem mapeamento manual para SKU KIT4YW640)
- KIT10YW520 — usado slack_short_name "Kit 10 Potes 520ml" (mapeamento canônico)

**Nomes de produto — Análise e Prioridades (divergência cross-layer):**
- L05 escreveu "Kit 3 Potes Vidro Hermético Vedação Tampa 4 Travas Marmita Azul-petróleo"; L06 usou "Kit 3 Potes Vidro Hermético Tampa Azul-petróleo" — display_short do SKU KIT3S099 (fallback automático; slack_short_name null). Ruído SEO ("Vedação", "4 Travas", "Marmita") removido conforme regra do display_short.
- L05 escreveu "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita (Tampa Preta + Tampa Cinza no mesmo MLB)"; L06 usou "as variações Tampa Preta e Tampa Cinza no mesmo anúncio" com referência coletiva anterior a "Potes de Vidro 5 Peças" — combinação dos slack_short_names canônicos de IMB501P e IMB501C, evitando o título longo com ruído SEO ("Mantimentos Marmita").
- L05 escreveu "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo"; L06 usou "Kit 4 Potes 1050ml" — slack_short_name canônico do SKU KIT4YW1050.

**Terminologia e jargão traduzidos**
- "health" → "qualidade do anúncio em regular" (sem valor numérico, conforme regra obrigatória)
- "available_quantity" → "estoque" / "estoque acima/abaixo de X unidades"
- "snapshot" → "leitura" (em todo lugar visível na mensagem)
- "denominador comprimido" → "volume abaixo da média" (jargão técnico sem entrada no glossário; traduzido para linguagem operacional)
- "autonomia orgânica como fato" → "conta sustenta resultado sem depender de campanha"
- "ADS share" → nunca escrito; usado "ADS respondeu por X% do Faturamento" e "proporção do ADS"
- "GMV" → "Faturamento" em toda a mensagem

**Formatação numérica**
- ACOS: L05 escreveu "4,41%"; L06 aplicou regra de 1 casa decimal → "4,4%"
- ROAS: 14,34x mantido (multiplicador, não percentual; regra de 1 casa aplica-se apenas a %)
- Valores monetários: todos com 2 casas decimais — R$ 5.421,27 (corrigido do "R$ 5.421" da L05), R$ 6.000,00, R$ 46,34
- L05 escreveu "R$ 5.421" sem centavos em dois pontos; L06 corrigiu para R$ 5.421,27 por regra obrigatória de centavos

**Modalidade de envio omitida da VISÃO**
- `fulfillment_mix_yesterday_top10` cobre apenas 56 dos 117 pedidos do dia (~47,9%); não representa dado objetivo da plataforma sem ressalva — omitido da seção VISÃO conforme regra. Mix aparece apenas na ANÁLISE onde a L05 trouxe explicitamente.

**Faturamento por produto omitido do Top Produtos**
- Pacote L00 não traz receita validada por produto/variação. Proibido calcular, estimar ou aproximar. Formato aplicado: `[nome] — [pedidos] pedidos`.

**Atribuição de responsável**
- Yasmin atribuída como responsável em todas as 3 prioridades, conforme regra fixa (ML é dela).

**Escalonamento**
- Prioridade 1: escalar se cancellations_rate sair de zero → preservado da L05.
- Prioridade 2: escalar se estoque < 5 ou prazo de reposição não confirmado → preservado da L05.
- Prioridade 3: escalar se ADS > 55% em dois dos próximos três dias úteis com Faturamento ≥ R$ 6.000,00 → preservado da L05; a discussão com Himmel foi preservada como aparece na L05 (condição de escalonamento, não adicionada de camadas anteriores).

**Alternativas operacionais**
- Prioridade 1: "repor ao CD do ML ou pausar de forma controlada" — ambas as alternativas da L05 preservadas (regra de alternativas operacionais explícitas).