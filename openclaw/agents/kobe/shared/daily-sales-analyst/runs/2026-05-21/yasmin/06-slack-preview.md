<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 21/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 6.082,82
- Pedidos: 100
- Ticket médio: R$ 60,83
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Kit 5 Potes de Vidro Redondos — Tampa Preta — 31 pedidos
- Kit 10 Potes Herméticos 1050ml — 10 Unidades — 16 pedidos
- Kit 5 Potes de Vidro Redondos — Tampa Cinza — 13 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml — 8 pedidos
- Kit 5 Potes de Vidro Redondos — Tampa Vermelha — 8 pedidos
- Kit 6 Canecas Porcelana Tulipa 250ml — 5 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira — 3 pedidos
- Kit 10 Potes Herméticos 520ml — 2 pedidos
- Kit 10 Potes Herméticos 1050ml — 6 Unidades — 2 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml — 2 pedidos

🔍 ANÁLISE DA CONTA
- A reputação está verde e o índice de cancelamentos marca zero — mas esse número ainda não capturou o que aconteceu ontem: o Kit Canequinhas entrou em ruptura efetiva, com 3 pedidos registrados contra 2 unidades disponíveis no CD do ML. Em Full, o cancelamento é processado pelo próprio ML. O impacto na reputação aparece no próximo ciclo, não neste. Ler o dia como reputação limpa sem ressalva é leitura errada.
- O mix de fulfillment do dia parece ter invertido o padrão histórico — 80,0% Cross-docking ontem contra 73,6% Full nos últimos 30 dias. Mas não é o canal que mudou: os três produtos mais vendidos são todos Cross-docking por natureza e concentraram 60,0% do volume. O padrão Full da conta segue intacto na série mensal; o dia foi produto-específico, não erosão sistêmica.
- O GMV de R$ 6.082,82 com volume plano e zero de investimento em Mercado Ads poderia indicar orgânico forte — mas o zero de ADS ainda não tem causa confirmada. Se foi pausa deliberada, o resultado é leitura válida de músculo orgânico. Se foi falha técnica, o dia está contaminado. Qualquer conclusão sobre força orgânica ou sobre o ticket elevado (R$ 60,83, +37,1% vs últimos 30 dias) fica suspensa até a confirmação com Himmel.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar o status dos pedidos do Kit Canequinhas no CD do ML e acionar reposição urgente. O item opera em Full — reposição exige envio físico ao CD do Mercado Livre, não ajuste na expedição Budamix. A janela de cancelamento automático pelo ML já está aberta, com impacto prospectivo no cancellations_rate, hoje em 0%. Confirmar/refutar por: cancelamentos do item aparecendo no próximo pacote confirmam impacto na reputação; reposição confirmada e pedidos atendidos em 24h = risco neutralizado. Escalar se: cancelamentos registrados no próximo ciclo — risco de reputação se materializou.
- Yasmin: confirmar com Himmel se o zero de ADS em 21/05 foi pausa deliberada ou falha técnica de veiculação. Sem essa confirmação, o resultado do dia não é interpretável e nenhuma decisão sobre campanha ou leitura de série orgânica pode ser tomada com segurança. Confirmar/refutar por: pausa intencional = registrar dia como ponto zero da série orgânica e observar por 3 dias; falha técnica = marcar dia como contaminado e aguardar ciclo limpo. Escalar se: Himmel identificar falha técnica com campanhas desconfiguradas — alinhar imediatamente com Himmel para reativação controlada.
- Yasmin: o Kit 6 Canecas Tulipa Lisa está com cobertura estimada de ~4 dias em Full (19 unidades, 5 pedidos/dia). É o próximo item a entrar em ruptura após o Canequinhas. Avaliar reposição em conjunto com o Canequinhas — em Full, o prazo operacional efetivo é mais estreito que o número de dias sugere. Confirmar/refutar por: estoque abaixo de 10 unidades no próximo ciclo confirma urgência; item saindo do top 10 antes de zerar indica queda de giro, rever urgência.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** `Leitura de 'orgânico forte confirmado' ou 'musculatura orgânica validada' para 21/05/2026`
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Zero de ADS com causa desconhecida — interpretação de orgânico puro é hipótese não validada; afirmar como fato induziria decisão errada sobre campanhas.
- **Agregado autorizado:** não
- **Tratamento aplicado:** preservada como hipótese com linguagem condicional ("poderia indicar orgânico forte — mas o zero de ADS ainda não tem causa confirmada"; "fica suspensa até a confirmação")
- **Aparece na mensagem final:** sim, como hipótese condicional no terceiro bullet da análise

---

- **Item bloqueado:** `Reputação limpa sem ressalva sobre ruptura do Canequinhas`
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** cancellations_rate=0 é métrica de janela longa que não capturou os pedidos sem cobertura de 21/05/2026; citar reputação como limpa sem ressalva esconde o risco ativo.
- **Agregado autorizado:** não
- **Tratamento aplicado:** ressalva explícita incluída no primeiro bullet da análise; a métrica zero é citada apenas como ponto de partida do risco, não como confirmação de saúde
- **Aparece na mensagem final:** sim, com ressalva obrigatória: "esse número ainda não capturou o que aconteceu ontem"

---

- **Item bloqueado:** `Atributo 'Retangular' como característica confirmada do Kit 4 Potes 1050ml ou do Kit 2 Potes 1050ml`
- **Origem do bloqueio:** L05 Condensadora (com base em L04 Granular)
- **Motivo:** 'Retangular' presente apenas no display_name interno, sem confirmação por título ML real nem por confirmed_variation_attributes; uso externo é dado interno não validado.
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — os dois produtos aparecem em Top Produtos sem o atributo 'Retangular', usando apenas título ML simplificado: "Kit 4 Potes de Vidro Hermético 1050ml" e "Kit 2 Potes de Vidro Hermético 1050ml"
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** `display_name 'Kit 10 Potes Herméticos 1050ml Refratário 4 Travas' como identificador sem diferenciador de quantidade`
- **Origem do bloqueio:** L05 Condensadora (com base em L04 Granular — display_name duplicado para KIT10YW1050 e KIT6YW1050)
- **Motivo:** KIT10YW1050 (10 unidades) e KIT6YW1050 (6 unidades) compartilham display_name idêntico; uso sem diferenciador produz identificação incorreta.
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** títulos ML reais usados com diferenciador explícito de quantidade — "Kit 10 Potes Herméticos 1050ml — 10 Unidades" e "Kit 10 Potes Herméticos 1050ml — 6 Unidades"
- **Aparece na mensagem final:** sim, como dois itens distintos com diferenciador de quantidade em Top Produtos

---

- **Item bloqueado:** `MLB... IDs (platform_item_id) no corpo da mensagem Slack`
- **Origem do bloqueio:** L05 Condensadora (regra ML de pipeline)
- **Motivo:** IDs técnicos não pertencem à comunicação final.
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhum platform_item_id mencionado em qualquer seção da mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** `Direção do health do Kit 4 Potes 1050ml (queda, estabilização ou recuperação)`
- **Origem do bloqueio:** L05 Condensadora (com base em L04 Granular)
- **Motivo:** apenas leitura pontual health=0,75 disponível; série temporal ausente do pacote; afirmar direção seria invenção.
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido integralmente — o item não aparece na análise nem nas prioridades com qualquer afirmação direcional de health; o Kit 4 Potes aparece apenas no ranking de Top Produtos com volume de pedidos
- **Aparece na mensagem final:** não (exceto como entrada neutra em Top Produtos)

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) — são campos de pipeline; não citados na mensagem final; a classificação de cada insight foi preservada via linguagem de nuance (fato: afirmativo direto; hipótese: condicional; risco latente: alerta com ressalva).

- Preservação de classificação `risco latente` no insight 1 — linguagem de alerta mantida; não convertida em certeza nem suavizada; a construção "ler o dia como reputação limpa sem ressalva é leitura errada" foi preservada do L05 por ser o núcleo do risco.

- Preservação de classificação `hipótese` no insight 3 — linguagem condicional mantida ("poderia indicar", "fica suspensa"); proibição de transformar em fato respeitada; bloqueio de "orgânico forte confirmado" integrado diretamente na construção do insight.

- Classificação `fato` no insight 2 preservada — afirmação direta sobre mix produto-específico sem qualificação de incerteza; o "parece ter invertido" do L05 é estrutura retórica que configura o contraste, não marcador de incerteza sobre o fato final.

- Fulfillment omitido da seção VISÃO — dado disponível é `fulfillment_mix_yesterday_top10` com cobertura de ~90 pedidos do top 10, não de todos os 100 pedidos do dia; Condensadora não autorizou exibição com ressalva de cobertura explícita na seção VISÃO; mix de fulfillment tratado apenas na análise com base nos dados da Condensadora.

- Atribuição de Yasmin como responsável em todas as prioridades — L05 não atribui responsável; Yasmin é a focal point ML definida pelo pipeline.

- Simplificação de título ML — IMB501P: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Preto" → "Kit 5 Potes de Vidro Redondos — Tampa Preta"; removidos "Hermético", "Redondo Com Tampa" (redundante com formato); confirmed_variation_attributes ["Tampa Preta"] adicionado como sufixo confirmado.

- Simplificação de título ML — IMB501C: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Cinza" → "Kit 5 Potes de Vidro Redondos — Tampa Cinza"; mesma regra; confirmed_variation_attributes ["Tampa Cinza"] adicionado.

- Simplificação de título ML — IMB501V: "Potes De Vidro Hermético Redondo Com Tampa Kit 5 Peças Vermelho" → "Kit 5 Potes de Vidro Redondos — Tampa Vermelha"; confirmed_variation_attributes ["Tampa Vermelha"] adicionado.

- Simplificação de título ML — KIT10YW1050: "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" → "Kit 10 Potes Herméticos 1050ml — 10 Unidades"; removidos "Refratário", "4 Travas", "Budamix Azul-petróleo" (SEO); "10 Unidades" mantido como diferenciador obrigatório por divergência de display_name com KIT6YW1050.

- Simplificação de título ML — KIT6YW1050: "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas Budamix Azul-petróleo 6 Unidades" → "Kit 10 Potes Herméticos 1050ml — 6 Unidades"; título ML é internamente contraditório (diz "Kit 10 Potes" mas diferenciador é "6 Unidades"); quantidade "10 Potes" preservada por regra de não alterar quantidade do título ML; "6 Unidades" mantido como diferenciador obrigatório.

- Simplificação de título ML — KIT4YW1050: "Kit 4 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 4 Potes de Vidro Hermético 1050ml"; removidos "Tampa 4 Travas Vedação Azul-petróleo" (SEO de diferenciação de fechamento); atributo "Retangular" bloqueado, não incluído.

- Simplificação de título ML — KIT2YW1050: "Kit 2 Potes De Vidro Hermético 1050ml Tampa 4 Travas Vedação Azul-petróleo" → "Kit 2 Potes de Vidro Hermético 1050ml"; mesma regra; atributo "Retangular" bloqueado, não incluído.

- Simplificação de título ML — TL6250: "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" → "Kit 6 Canecas Porcelana Tulipa 250ml"; removidos "Lisa" (genérico), "Coloridas Xícara" (SEO); mantidos tipo, quantidade, material, dimensão.

- Simplificação de título ML — 914C_BAV: "Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico" → "Kit 6 Canequinhas 100ml com Suporte de Madeira"; "06" normalizado para "6"; "Acrílico" removido por ser qualificador genérico do suporte sem confirmação em confirmed_variation_attributes; confirmed_variation_attributes vazio.

- Simplificação de título ML — KIT10YW520: "Kit 10 Potes Herméticos 520ml Refratário 4 Travas Budamix Azul-petróleo 10 Unidades" → "Kit 10 Potes Herméticos 520ml"; removidos termos SEO; dimensão "520ml" mantida como diferenciador crítico vs KIT10YW1050.

- Percentuais formatados com 1 casa decimal conforme padrão numérico obrigatório: "80%" e "73%" do L05 convertidos para "80,0%" e "73,6%" (valor exato do pacote); "+37%" do L05 convertido para "+37,1%" (valor exato de ticket_vs_30d_pct=37.1); "60%" preservado como "60,0%".

- Ausência de faturamento por produto em Top Produtos — pacote não entrega campo de receita validada por produto/variação; proibição de estimativa (ticket médio × pedidos) aplicada; formato "nome — pedidos pedidos" adotado para todos os itens.

- Nenhum produto bloqueado em Top Produtos — L04 declarou risco de identificação médio sem bloqueios para Slack; todos os 10 itens do ranking aparecem na mensagem com títulos ML corretos.