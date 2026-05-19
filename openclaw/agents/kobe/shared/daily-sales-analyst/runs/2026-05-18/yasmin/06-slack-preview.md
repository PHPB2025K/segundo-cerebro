<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 18/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 4.184,38
• Pedidos: 96 pedidos
• Ticket médio: R$ 43,59
• Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 35 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 16 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 9 pedidos
• Suporte Gamer 2 Controles e Headset Mesa Organizador — 4 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 4 pedidos
• Kit 6 Canequinhas 100ml — 3 pedidos
• Kit 6 Xícaras Porcelana Paris 170ml — 3 pedidos
• Kit 4 Potes de Vidro 320ml Hermético — 3 pedidos
• Kit 4 Potes de Vidro 640ml Hermético — 3 pedidos
• Kit 6 Canequinhas 100ml (variação adicional) — 3 pedidos

🔍 ANÁLISE DA CONTA
• O desvio de -14,6% vs últimos 7 dias parece queda, mas é artefato: a janela foi inflada pelo domingo excepcional de 04/05. Quando comparado com os mesmos domingos históricos, hoje está +3% acima da média. A conta não caiu — está dentro do patamar esperado.
• O risco de concentração é mais estreito do que parece: os Conjuntos de Potes Redondos dependem de um único anúncio no ML. Qualquer evento sobre esse listing — queda de ranking, penalidade, suspensão — afeta as três cores ao mesmo tempo e derruba mais de 60% do volume da conta de uma vez. Não é risco distribuído por família; é ponto único de falha.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar posição e saúde do anúncio dos Conjuntos de Potes Redondos diretamente no painel ML — essa checagem não pôde ser feita pelo dado automatizado. O anúncio responde por mais de 60% do volume em ponto único de falha; confirmar que a posição está estável é o dado que falta para validar que o dia foi normal. Confirmar se posição dos últimos 7 dias está estável; se posição em queda em 2 ou mais dias, alinhar com Himmel sobre ADS ML.
• Yasmin: registrar a concentração de hoje dos Conjuntos de Potes Redondos (62,5% do volume) como referência e comparar com o próximo domingo. Próximo domingo abaixo de 55% enfraquece a hipótese de dependência crônica; acima de 60% pela segunda vez consecutiva, sinalizar para Kobe que o mix estrutural precisa de avaliação.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: MLBs e IDs técnicos de listing (MLB3288536143 e demais)
- Origem do bloqueio: Condensadora
- Motivo: dados internos, não devem aparecer nominalmente na mensagem
- Agregado autorizado: não aplicável — bloqueio de IDs técnicos, não de produto
- Tratamento aplicado: omitidos em toda a mensagem; produtos referenciados apenas por nome legível
- Aparece na mensagem final: não

- Item bloqueado: Raw SKUs (IMB501P_T, KITIMB501P_T, etc.)
- Origem do bloqueio: Condensadora
- Motivo: usar apenas nomes legíveis de produto
- Agregado autorizado: não aplicável
- Tratamento aplicado: omitidos; produtos citados por display_name
- Aparece na mensagem final: não

- Item bloqueado: Desvio de -14,6% vs 7d como sinal de deterioração
- Origem do bloqueio: Condensadora
- Motivo: é artefato do pico de 04/05 e induziria leitura errada
- Agregado autorizado: não se aplica — dado não entra; a correção pelo par sazonal (+3%) é o que vai para Slack
- Tratamento aplicado: mencionado na análise com correção explícita, não como sinal de queda
- Aparece na mensagem final: sim, como inversão negativa corrigida (padrão C da Condensadora)

- Item bloqueado: Proporção interna de cores da família (58% preta, 27% cinza, 15% vermelha)
- Origem do bloqueio: Condensadora
- Motivo: granularidade excessiva para Slack; ponto relevante é o ponto único de falha, não a distribuição de cor
- Agregado autorizado: não
- Tratamento aplicado: omitida; análise referencia o anúncio como ponto único de falha sem detalhar proporções de cor
- Aparece na mensagem final: não

- Item bloqueado: Produto do cancelamento único
- Origem do bloqueio: Condensadora
- Motivo: não identificado no pacote; 1 cancelamento em 96 pedidos sem padrão relevante
- Agregado autorizado: não
- Tratamento aplicado: cancelamento exibido apenas como número absoluto na VISÃO, sem associação a produto
- Aparece na mensagem final: apenas o total (1 cancelamento) na seção VISÃO

- Item bloqueado: Taxa de cancelamento (~1%) como dado isolado
- Origem do bloqueio: Condensadora
- Motivo: operacionalmente irrelevante e desnecessário no Slack
- Agregado autorizado: não
- Tratamento aplicado: omitida a taxa percentual; exibido apenas o número absoluto
- Aparece na mensagem final: não (apenas número absoluto)

- Item bloqueado: Ausência de weekly.md e monthly.md preenchidos
- Origem do bloqueio: Condensadora
- Motivo: limitação interna de memória, não informação para o responsável da conta
- Agregado autorizado: não
- Tratamento aplicado: omitido
- Aparece na mensagem final: não

- Item bloqueado: Produtos confidence medium com MLBs específicos (SPC0111, KIT4YW320, KIT4YW640, 914C_BAV)
- Origem do bloqueio: Condensadora
- Motivo: baixo volume, risco contido, nível de detalhe de MLB inadequado para mensagem
- Agregado autorizado: produtos podem aparecer por nome sem MLB
- Tratamento aplicado: produtos citados por nome legível sem MLB; incluídos no Top Produtos por ordem de volume
- Aparece na mensagem final: sim, por nome legível sem ID técnico

---

### Decisões de formatação

- Remoção de todos os MLBs e raw SKUs da mensagem final — bloqueio da Condensadora; nenhum ID técnico visível
- Preservação da inversão negativa no insight 1 (parece queda, mas não é) — padrão C da Condensadora mantido integralmente; conectivo "mas" preservado
- Preservação do alerta de ponto único de falha no insight 2 — linguagem direta da Condensadora mantida sem suavização; "não é risco distribuído por família; é ponto único de falha" reproduzido fielmente
- Proporção interna de cores (58%/27%/15%) omitida da análise — bloqueio da Condensadora; o ponto único de falha é citado sem granularidade de cor
- Prioridade 1 mantida com sinal de confirmação e condição de escalonamento (alinhar com Himmel) — vindos diretamente das Prioridades Condensadas
- Prioridade 2 mantida com sinal de confirmação e condição de escalonamento (sinalizar para Kobe) — vindos diretamente das Prioridades Condensadas
- Top Produtos em ordem decrescente por pedidos — ranking respeitado; Tampa Preta (35) > Tampa Cinza (16) > Tampa Vermelha (9) > demais com 4 e 3 pedidos
- Variações IMB501 mantidas separadas por cor — regra de variação vendável; "Conjunto 5 Potes de Vidro Redondos" não consolidado como linha única
- 914C e 914C_BAV mantidos como linhas separadas — SKUs distintos no pacote validado com platform_item_id idêntico (MLB4410218897); sem autorização explícita da Condensadora para consolidar; decisão: manter separados com nome legível, sem IDs técnicos; registrado aqui para QA validar se consolidação seria mais precisa
- Desvio vs 7d apresentado como artefato corrigido, não como sinal negativo — seguindo instrução explícita da Condensadora de não usar o -14,6% como sinal de deterioração
- Confiança alta da Condensadora: nenhuma ressalva de confiança baixa inserida; linguagem sem hedge desnecessário
- Seção VISÃO sem comparações temporais — padrão numérico obrigatório; dados objetivos do dia apenas
- Full ML: dado de fulfillment não disponível (todos categorizados como "other") — omitido da VISÃO por ausência de dado válido; não inferido