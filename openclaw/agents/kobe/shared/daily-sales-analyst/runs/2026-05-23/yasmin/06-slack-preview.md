<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 23/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.124,32
• Pedidos: 91
• Ticket médio: R$ 56,31
• Cancelamentos: 0

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 18 pedidos
• Kit 4 Potes 1050ml — 11 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 11 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 11 pedidos
• Kit 6 Canecas Tulipa 250ml — 9 pedidos

🔍 ANÁLISE DA CONTA
• O Kit 6 Canecas Tulipa 250ml em Full fechou o dia com 2 unidades no CD do ML depois de 9 pedidos, e o anúncio seguia ativo no snapshot desta manhã — a partir de agora, qualquer pedido novo entra sem cobertura e vira cancelamento automático, justamente na janela apertada de fechamento da Platinum.
• Não é uma família distribuída carregando o dia — é um único anúncio com nível de qualidade em Padrão inferior (0,71) há três ciclos sem mexer que sozinho fez 44% dos pedidos; sem o detalhamento de ADS por anúncio, ainda não dá pra dizer se esse volume é orgânico recuperando ou ADS segurando o que o ranking perdeu.
• Os 91 pedidos parecem fracos comparados à semana, mas o GMV ficou acima das bandas de 30 e 60 dias com ticket em alta consistente — é o terceiro ciclo confirmando que a conta cresce por valor médio, não por alcance. O salto da modalidade Full no top do dia (88%) é composição dos campeões, não mudança no perfil da conta.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar hoje no painel ML o estoque atual e o status do Kit 6 Canecas Tulipa 250ml em Full — confirmar se há reposição em trânsito para o CD do ML; se não houver, avaliar cancelamento controlado dos pedidos novos antes do ML cancelar automaticamente. Cobertura de horas no ritmo recente — qualquer cancelamento automático pressiona a reputação verde e o nível MercadoLíder Gold e atrapalha o pace da Platinum. Confirmar/refutar no próximo pacote: anúncio pausado, estoque zerado com pedidos pendentes ou cancellations_rate saindo do zero = ruptura confirmada; estoque recomposto e anúncio ativo = risco neutralizado. Escalar se houver pedidos confirmados sem cobertura e sem reposição em trânsito — alinhar com Himmel sobre pausa preventiva do anúncio até a reposição chegar.
• Yasmin: checar no painel ML a direção do nível de qualidade dos dois campeões em Full em Padrão inferior — Potes Vidro 5 Peças (em 0,71 há três ciclos) e Kit 4 Potes 1050ml (em 0,75 há três ciclos) — registrar se está estável, caindo ou em recuperação. Três leituras idênticas não distinguem piso estabilizado de degradação lenta; a quarta define a direção. Confirmar/refutar: Potes Vidro 5 Peças abaixo de 0,69 (Básico) ou Kit 4 Potes abaixo de 0,72 = degradação acelerando; estável ou em alta = piso confirmado, sem ação. Escalar se Potes Vidro 5 Peças atingir Básico — alinhar com Himmel sobre cobertura ADS preventiva e levar a Kobe a discussão de dependência estrutural.
• Yasmin: registrar o ADS share do dia (49,5%) como segundo ponto da nova série pós-22/05 e cobrar do pacote o breakdown de receita de ADS por anúncio. Sem esse dado, não dá pra confirmar se ADS está segurando o anúncio em Padrão inferior ou se o orgânico está crescendo de verdade — é a informação que falta para fechar a tese. Confirmar/refutar no próximo ciclo: ADS share ≤ 55% = hipótese de orgânico em expansão se fortalece; ≥ 65% = gatilho de escalonamento a Kobe volta a estar vivo. Escalar se terceiro ciclo consecutivo com ADS share ≥ 65% — levar a Kobe a discussão de dependência estrutural de mídia paga.

Dia analisado: 23/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos.

L05 `o_que_nao_pode_ir_para_slack: []` e L04 `bloqueios_para_slack: []` — nenhum item bloqueado neste ciclo. Todos os dez produtos do top_products têm risco de identificação baixo conforme declarado pela L04 (cluster IMB501 resolvido como título enxuto + atributo confirmado por SKU; KIT6YW1050 e KIT10YW1050 com mapping_status mapped_generic_sku e confiança suficiente para uso no Slack).

---

### Decisões de formatação

**Tradução de nomes de produto — Top Produtos (slack_short_name, mapeamento canônico):**
- IMB501P — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- KIT4YW1050 — usado slack_short_name "Kit 4 Potes 1050ml" (mapeamento canônico)
- IMB501V — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- IMB501C — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- TL6250 — usado slack_short_name "Kit 6 Canecas Tulipa 250ml" (mapeamento canônico)

**Tradução de nomes de produto — Análise e Prioridades:**
- L05 insight 0 usou "Kit 6 Canecas Porcelana Tulipa 250ml" (título longo) → L06 Slack: "Kit 6 Canecas Tulipa 250ml" (slack_short_name TL6250, mapeamento canônico)
- L05 prioridade 1 usou "Conjunto 5 Potes" → L06 Slack: "Potes Vidro 5 Peças" (agregado pelo anúncio MLB3288536143; nome derivado do padrão dos slack_short_names IMB501P/V/C, referência ao nível do anúncio único em Padrão inferior — não atribui variação específica porque a prioridade fala do anúncio inteiro)
- L05 prioridade 1 usou "Kit 4 Potes 1050ml" → L06 Slack: "Kit 4 Potes 1050ml" (coincide com slack_short_name KIT4YW1050, mapeamento canônico — sem divergência)

**Remoção de metadados internos:**
- `padrao`, `base` e `classificacao` não citados na mensagem — são metadados de pipeline interno

**Preservação de nuance classificatória:**
- Insights 1 e 2 (classificacao: risco latente) — escritos com linguagem prospectiva e condicional: "a partir de agora, qualquer pedido novo entra sem cobertura e vira cancelamento automático" (prospectivo) e "ainda não dá pra dizer se esse volume é orgânico recuperando ou ADS segurando" (incerteza explícita); nenhum transformado em fato
- Insight 3 (classificacao: fato) — escrito como fato direto: "é o terceiro ciclo confirmando"

**Produto não nomeado no insight 2:**
- L05 deixou o anúncio campeão sem nome no insight 2 ("um único anúncio em Padrão inferior") — decisão preservada na mensagem Slack; o produto é nomeado na prioridade correspondente onde a ação exige identificação

**Correção obrigatória — reputação vs medalha:**
- L05 prioridade 1 usou "reputação verde Gold" (forma composta proibida) → L06 Slack: "reputação verde e nível MercadoLíder Gold" — eixos separados conforme regra obrigatória

**Terminologia técnica — nível de qualidade:**
- "health=0,71" e "health=0,75" traduzidos para "nível de qualidade em Padrão inferior (0,71)" e "(0,75)" conforme vocabulário obrigatório ML; termo "health" não aparece na mensagem

**Terminologia técnica — modalidade de envio:**
- Palavra "fulfillment" não usada em nenhum ponto da mensagem; modalidade referenciada como "Full" e "Cross-Docking" conforme vocabulário aprovado
- Insight 3 usa "modalidade Full" como qualificador ao mencionar o mix do top do dia

**Omissão de modalidade de envio na seção VISÃO:**
- fulfillment_mix_yesterday_top10 cobre 49 pedidos resolvidos de um total de 91 (~54% de cobertura) — não representa dado objetivo da totalidade do dia; omitido da seção VISÃO conforme regra; mix de modalidade de envio aparece apenas na ANÁLISE via insight 3 da Condensadora

**Atribuição de responsável:**
- Yasmin atribuída explicitamente como responsável em todas as três prioridades (responsável fixo ML)

**Escalonamento preservado:**
- Himmel (pausa preventiva de anúncio) e Kobe (dependência estrutural de ADS) mantidos conforme L05; nenhum escalonamento adicionado além do que a Condensadora trouxe

**Faturamento por produto — Top Produtos:**
- Não incluído em nenhum item do Top Produtos; pacote não traz receita validada por variação