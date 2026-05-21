<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.087,71
• Pedidos: 91 pedidos
• Ticket médio: R$ 55,91
• Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 23 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
• Kit 6 Canequinhas 100ml — 8 pedidos
• Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
• Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
• Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
• Suporte Gamer 2 Controles e Headset Mesa Organizador PS5 PS4 Preto — 3 pedidos
• Kit 4 Potes de Vidro 320ml Hermético 4 Travas — 3 pedidos
• Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
• O GMV do dia (R$ 5.087) parece saudável, mas cerca de 60% desse resultado veio de campanha de ADS sobre anúncios que estão perdendo posição orgânica — dois dos campeões em Full têm health abaixo do limiar de penalização do ML, e sem histórico de direção, não dá para saber se a erosão está acelerando ou estabilizada. A campanha está eficiente, mas pode estar compensando perda de exposição orgânica que ainda não aparece no número agregado.
• A queda de pedidos em relação à semana (-20,9%) parece deterioração, mas o controle correto é o dia da semana: 91 pedidos está dentro da banda histórica de quartas (-1,6% vs média). O que mudou de verdade é o ticket — R$ 55,91 contra R$ 41,53 histórico do mesmo dia da semana — e o GMV subiu +32,4% por isso. Não é queda, é acomodação com mix mais caro.
• O único ponto que exige ação hoje é o anúncio de canequinhas acrílico: estoque em cobertura crítica, anúncio ativo, 3 pedidos gerados ontem — o ML continuará recebendo pedidos enquanto o anúncio não for pausado ou o estoque não for reposto. Janela de 24h antes de gerar cancelamento prospectivo que contamina a reputação.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar e repor estoque do anúncio de canequinhas acrílico (cobertura crítica com anúncio ativo). Risco imediato: novos pedidos sem reposição geram cancelamento que afeta reputação. Confirmar/refutar: anúncio pausado ou reabastecido em 24h = risco neutralizado; ruptura ou cancelamento registrado = registrar data como variável confundidora na reputação. Escalar se cancelamento for confirmado.
• Yasmin: investigar causa do health penalizado na variante Tampa Vermelha da família de potes redondos (anúncio em catálogo Full, health=0.71 — abaixo do limiar de penalização ML). Ruptura e inatividade foram descartadas. Causa ainda desconhecida — pode ser listing, SLA ou reclamação. Confirmar/refutar: causa identificável = ação específica; causa não identificável = alinhar com Himmel sobre cobertura ADS preventiva nesse anúncio antes que o health caia mais. Escalar se health desse anúncio cair abaixo de 0.65 no próximo ciclo.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: SKUs crus (IMB501PT, KIT4YW1050, MLB4410218897, etc.)
- Origem do bloqueio: Condensadora
- Motivo: exposição de código interno sem valor operacional para o destinatário
- Agregado autorizado: sim, nomes descritivos dos produtos
- Tratamento aplicado: substituído por nome descritivo em todos os casos
- Aparece na mensagem final: não (substituído por nome descritivo)

- Item bloqueado: afirmação de estoque zerado no anúncio de canequinhas acrílico
- Origem do bloqueio: Condensadora
- Motivo: ambiguidade temporal no snapshot — available_quantity=3 pode ser pré ou pós-processamento dos 3 pedidos de ontem
- Agregado autorizado: sim, "estoque em cobertura crítica"
- Tratamento aplicado: substituído por "estoque em cobertura crítica"
- Aparece na mensagem final: sim, como "estoque em cobertura crítica"

- Item bloqueado: causa do health=0.71 na variante Tampa Vermelha
- Origem do bloqueio: Condensadora / Granular
- Motivo: inconclusivo por falta de dado no pacote — reclamação, atraso ou listing não determinável
- Agregado autorizado: não
- Tratamento aplicado: preservado como "causa ainda desconhecida — pode ser listing, SLA ou reclamação" (hipótese, não fato)
- Aparece na mensagem final: sim, como hipótese aberta

- Item bloqueado: direção do health do Kit 4 Potes 1050ml (MLB4073003575)
- Origem do bloqueio: Condensadora / Granular
- Motivo: ponto zero sem histórico anterior — direção indeterminável
- Agregado autorizado: não
- Tratamento aplicado: omitido da análise e prioridades como afirmação de direção; mencionado apenas como referência de health no contexto da prioridade de investigação
- Aparece na mensagem final: não como afirmação de direção

- Item bloqueado: display_name interno "Kit 6 Tigelas de Vidro 250ml" para TL6250
- Origem do bloqueio: Granular / Condensadora
- Motivo: divergência confirmada — título real do anúncio é "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"
- Agregado autorizado: sim, título real do anúncio
- Tratamento aplicado: substituído por "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"
- Aparece na mensagem final: sim, com título real

- Item bloqueado: afirmação de que Tampa Preta e Tampa Vermelha compartilham listing ou estão no mesmo anúncio
- Origem do bloqueio: Condensadora
- Motivo: estrutura de variação da família IMB501 não confirmada pelo pacote
- Agregado autorizado: sim, "variantes da mesma família de potes redondos"
- Tratamento aplicado: usado "variante Tampa Vermelha da família de potes redondos"
- Aparece na mensagem final: sim, como formulação agregada autorizada

- Item bloqueado: afirmação de que 78% da base ativa tem health saudável ou desconhecido como indicação de saúde
- Origem do bloqueio: Condensadora
- Motivo: ausência de dado não é evidência de saúde — é cegueira estrutural
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem
- Aparece na mensagem final: não

---

### Decisões de formatação

- Uso de "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" no lugar de "Kit 6 Tigelas de Vidro 250ml" — divergência TL6250 resolvida pela Granular; fonte primária (título real do anúncio) prevalece sobre display_name interno
- Remoção de todas as referências a bases internas ("Estratégica", "Granular", "Condensadora", "base: ...") — metadados internos removidos conforme regra; teses preservadas integralmente
- Preservação de linguagem de hipótese/indício em toda referência ao health dos anúncios penalizados — confiança média da Condensadora exige ressalva; "pode estar compensando", "causa ainda desconhecida", "pode ser listing, SLA ou reclamação"
- Uso de "estoque em cobertura crítica" no lugar de "estoque zerado" — ambiguidade temporal do snapshot preservada conforme bloqueio da Condensadora
- Uso de "variante Tampa Vermelha da família de potes redondos" no lugar de citação de estrutura de listing — formulação agregada autorizada pela Condensadora
- Uso do título real "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" no Top Produtos, encurtado para caber no formato Slack sem perder identidade do produto
- Produto "Suporte Gamer 2 Controles e Headset Mesa Organizador PS5 PS4 Preto" mantido com título descritivo completo — confidence=medium, sem alias revisado, título real preservado como fonte primária
- Ranking Top Produtos mantido em ordem decrescente por pedidos: 23, 13, 8, 5, 5, 5, 3, 3, 3, 3 — produtos com mesmo volume (5 pedidos e 3 pedidos) mantidos na ordem do ranking validado do pacote
- Dois insights de análise que envolvem confiança média preservados com linguagem de indício ("pode estar", "não dá para saber", "causa ainda desconhecida") — confiança limitada da Condensadora refletida em todos os pontos pertinentes
- Prioridades formatadas com ação + evidência + sinal de confirmação/refutação + condição de escalonamento — estrutura completa conforme regra da camada, preservando todos os elementos entregues pela Condensadora
- Himmel não acionado diretamente — mencionado como "alinhar com Himmel" via Yasmin, conforme regra de acionamento do contexto de responsáveis