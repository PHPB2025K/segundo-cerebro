<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 4.622,03
• Pedidos: 84 pedidos
• Ticket médio: R$ 55,02
• Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Preta — 20 pedidos
• Kit 4 Potes 1050ml — 11 pedidos
• Potes Vidro 5 Peças — Tampa Vermelha — 10 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 7 pedidos
• Kit 6 Canecas Tulipa 250ml — 6 pedidos

🔍 ANÁLISE DA CONTA
• O Kit 6 Canecas Tulipa 250ml em Full está com 2 unidades pós-baixa — ciclo anterior tinha 7 após os mesmos 6 pedidos, então o ritmo segue em ~6/dia e a cobertura prospectiva é menor que 12h. Sem reposição no CD do ML, o próximo pedido pode virar cancelamento automático, pressionando a reputação verde e a elegibilidade MercadoLíder Gold no meio do ETA de Platinum (13,8 dias).
• O mix de modalidade de envio do dia pareceu inverter — Cross-Docking em 52,9% do top 10 contra 73,7% Full na janela de 30 dias — mas não é erosão do canal Full. O cluster de Potes Vidro 5 Peças (Tampa Preta, Vermelha e Cinza) carregou 44% do volume, com a variação Cross-Docking Tampa Preta liderando sobre a Tampa Vermelha em Full. A janela de 7 dias segue em 74,9% Full: o padrão mensal está intacto e o dia foi desvio produto-específico.
• ADS respondeu por 69,9% do GMV com ROAS 10,87x e ACOS 4,57% — segundo ciclo consecutivo acima de 65% sem mudança de campanha. A eficiência sustenta o resultado, mas com só dois pontos ainda não dá para cravar dependência estrutural. O ciclo de 23/05 é o terceiro ponto: share acima de 65% abre conversa com Kobe; abaixo de 50% derruba a hipótese.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar o estoque atual do Kit 6 Canecas Tulipa 250ml em Full e acionar reposição no CD do ML. Único risco do dia com potencial de virar cancelamento automático em horas, pressionando reputação verde e elegibilidade MercadoLíder Gold no meio do ETA de Platinum. Confirmar/refutar por: estoque acima de 15 unidades pós-reposição com anúncio ativo nas próximas 24h neutraliza o risco; sem reposição confirmada em 24h, registrar como variável confundidora para os próximos ciclos. Escalar se: anúncio aparecer pausado ou cancelamento automático registrado no painel.
• Yasmin: verificar a direção do nível de qualidade dos dois campeões em Full — Kit 4 Potes 1050ml em Padrão inferior (0,75) e Potes Vidro 5 Peças — Tampa Vermelha em Padrão inferior (0,71). Com dois snapshots idênticos, a direção ainda não está confirmada — não mexer enquanto isso não estiver claro. Confirmar/refutar por: valores estáveis ou em recuperação no próximo ciclo mantêm observação; qualquer um caindo abaixo dos pontos atuais abre alinhamento com Himmel ainda nesta semana. Escalar se: ambos caindo simultaneamente — Yasmin alinha com Himmel sobre cobertura preventiva.
• Yasmin: registrar ADS share de 69,9% como segundo ponto consecutivo acima de 65% e não mexer nas campanhas. ROAS 10,87x e ACOS 4,57% estão fora da zona de intervenção — mexer agora introduz ruído na série antes do terceiro ponto. Confirmar/refutar por: share acima de 65% no ciclo de 23/05 confirma dependência estrutural e abre discussão com Kobe; share abaixo de 50% refuta. Escalar se: terceiro ponto consecutivo acima de 65% — Yasmin abre conversa com Kobe sobre estratégia de redução de dependência.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

Sem bloqueios recebidos. O campo `o_que_nao_pode_ir_para_slack` da L05 está vazio. Nenhum item foi bloqueado pela L04 (campo `bloqueios_para_slack` também vazio). Todos os 10 produtos do top têm identidade confirmada pela L04 com risco de identificação nível baixo.

---

### Decisões de formatação

- **Metadados `padrao`, `base`, `classificacao` removidos da mensagem** — são campos internos de pipeline; ausentes da mensagem final conforme regra.
- **Insight 1 (risco latente) — linguagem prospectiva preservada** — "pode virar cancelamento automático" em vez de afirmação categórica; framing exclusivamente prospectivo (pedidos futuros, não pedidos do dia analisado já processados), conforme regra de estoque POST-baixa.
- **Insight 2 (fato) — escrito como fato** — classificação `fato` da L05 autoriza afirmação direta; "o padrão mensal está intacto" sem qualificador de indício.
- **Insight 3 (hipótese) — nuance preservada** — "ainda não dá para cravar dependência estrutural" e "derruba a hipótese" mantêm o caráter hipotético; proibido transformar em fato.
- **Confiança media — sem ressalva global explícita** — nível `media` não exige disclaimer de "leitura limitada" (reservado para `baixa`); nuances individuais por classificação de insight foram suficientes.
- **Modalidade de envio omitida da seção VISÃO** — `fulfillment_mix_yesterday_top10` cobre apenas 68 dos 84 pedidos do dia (~81%), referente ao top 10 de anúncios, não à totalidade; L05 não autorizou exibição com cobertura explícita nesta seção; tratado exclusivamente na Análise da Conta via insight 2.
- **Top Produtos: exatamente os 5 primeiros do `top_products`** — sem produto bloqueado no ranking; nenhum ajuste de posição necessário.
- **IMB501P — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta"** (mapeamento canônico).
- **KIT4YW1050 — usado `slack_short_name` "Kit 4 Potes 1050ml"** (mapeamento canônico).
- **IMB501V — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Vermelha"** (mapeamento canônico; title ML público genérico "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" não usada; atributo "Tampa Vermelha" confirmado por SKU autoritativo IMB501V — caso de título enxuto, não divergência).
- **IMB501C — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Cinza"** (mapeamento canônico).
- **TL6250 — usado `slack_short_name` "Kit 6 Canecas Tulipa 250ml"** (mapeamento canônico; em Top Produtos, Análise e Prioridades).
- **Análise da Conta — referência ao cluster IMB501** — L05 escreveu "cluster IMB501 (Tampa Preta, Vermelha e Cinza)"; na mensagem Slack traduzido para "cluster de Potes Vidro 5 Peças (Tampa Preta, Vermelha e Cinza)" — agrega pelo nome curto canônico sem fragmentar em três bullets; divergência de denominação registrada: L05 usou "cluster IMB501", L06 usou "cluster de Potes Vidro 5 Peças", motivo: padronização com slack_short_name (IMB501P/V/C compartilham a família "Potes Vidro 5 Peças").
- **Prioridades — tradução de nomes de produto da L05** — L05 escreveu "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" → L06 escreveu "Kit 6 Canecas Tulipa 250ml" (slack_short_name TL6250); L05 escreveu "Kit 4 Potes 1050ml Tampa Azul-petróleo" → L06 escreveu "Kit 4 Potes 1050ml" (slack_short_name KIT4YW1050); L05 escreveu "Jogo Potes de Vidro 5 Peças Tampa Vermelha" → L06 escreveu "Potes Vidro 5 Peças — Tampa Vermelha" (slack_short_name IMB501V).
- **Responsável fixo Yasmin atribuído em todas as 3 prioridades** — L05 não atribui responsável; L06 atribui conforme regra de pipeline ML.
- **Escalonamento preservado em todas as prioridades** — condições de confirmação/refutação e `escalar_se` mantidos integralmente conforme L05; alternativas operacionais (Himmel, Kobe) mantidas onde a L05 as incluiu.
- **Faturamento por produto omitido no Top Produtos** — `top_products` não traz campo de receita validada por variação; formato "nome — pedidos" aplicado a todos os 5 itens conforme regra.
- **1 cancelamento incluído na VISÃO** — dado objetivo de `metrics.cancelamentos`; L05 não bloqueou; L04 registrou como "sinal irrelevante operacionalmente" mas na VISÃO é dado factual, não interpretação.