<!-- llm_used=true model=claude-opus-4-7 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 22/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 4.622,03
- Pedidos: 84
- Ticket médio: R$ 55,02
- Cancelamentos: 1

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Preta — 20 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 11 pedidos
- Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha — 10 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças — Tampa Cinza — 7 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 6 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades — 4 pedidos
- Kit de 6 Canecas de Porcelana Lisa Reta Para Chá e Café Colorida 200ml Caneca Colorida — 3 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades — 3 pedidos
- Kit 10 Potes Herméticos 320ml Azul-petróleo 10 Unidades — 2 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 2 pedidos

🔍 ANÁLISE DA CONTA
- O faturamento parece saudável (R$ 4.622,03, acima das médias de 30d e 60d), mas é o segundo dia seguido em que ADS carrega ~70% do GMV. Tirando ADS, o orgânico sustenta sozinho só ~R$ 1.393,00 — bem abaixo da média de 30d da conta. Não é ganho de demanda, é patamar mediado por mídia paga.
- Os dois campeões em Full seguem com health abaixo de 0,85: Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo em 0,75 e Jogo Potes de Vidro 5 Peças Claro — Tampa Vermelha (este em Catálogo) em 0,71. Segundo ciclo idêntico. O pacote só traz valor pontual, então não dá pra cravar se está caindo — o que dá pra dizer é que a penalização orgânica persiste no vetor que carrega ~74% do volume da conta, e em Catálogo o dano é perda de Buy Box, mais grave que ranking comum.
- O risco operacional real do dia não está no agregado: é o Kit 6 Canecas Porcelana Tulipa Lisa 250ml em Full, com 9 unidades pós-baixa e ritmo de ~6 pedidos/dia — cobertura prospectiva de ~1,5 dia. Sem reposição encaminhada, há ruptura em Full em D+1 ou D+2, o que dispara cancelamento automático ML e pressiona a reputação (hoje em cancellations_rate zero).

🎯 PRIORIDADES DO DIA
- Yasmin: checar a direção da health dos dois campeões em Full com penalização (Kit 4 Potes 1050ml Azul-petróleo em 0,75 e Jogo Potes 5 Peças Claro — Tampa Vermelha, Catálogo, em 0,71), comparando com o valor pontual de 22/05 registrado na memória. Segundo ciclo idêntico já é padrão, mas só a direção define se a erosão orgânica está acelerando ou contida — em Catálogo a consequência é perda de Buy Box. Confirmar/refutar em 24h: health estável ou subindo = manter observação; health caindo em qualquer um = alinhar com Himmel sobre cobertura ADS preventiva no item afetado. Escalar se health cair em qualquer um OU permanecer abaixo de 0,80 por mais 2 dias combinada com terceiro ciclo de ADS share ≥60% — aí abrir conversa com Kobe antes da janela Platinum fechar.
- Yasmin: verificar se a reposição do Kit 6 Canecas Porcelana Tulipa Lisa 250ml em Full já foi encaminhada (9 unidades pós-baixa, ritmo ~6 pedidos/dia). Único risco operacional imediato do dia; ruptura em Full em D+1 ou D+2 dispara cancelamento automático ML. Confirmar/refutar em 24h: reposição encaminhada = risco neutralizado; sem reposição = considerar pausa controlada do anúncio antes do cancelamento automático ML. Escalar se sem reposição em 24h, registrar como variável confundidora para a leitura dos próximos dias.
- Yasmin: registrar o ADS share do dia (69,9%, R$ 3.228,78 de R$ 4.622,03, ROAS 10,87x, ACOS 4,57%) como segundo ponto da série iniciada em 22/05, sem acionar Himmel para mexer em verba ou segmentação. Campanha eficiente em zona dominante, mas precisa do terceiro ciclo para confirmar dependência estrutural; mexer agora introduz variável num sistema sem leitura fechada e compromete o ritmo rumo ao Platinum. Confirmar/refutar no próximo ciclo: terceiro dia consecutivo com share ≥60% = risco confirmado como tese estrutural; share caindo para <60% sem alteração de spend = orgânico está reagindo e a tese de dependência enfraquece. Escalar se terceiro ciclo confirmado com health mantida em penalização — aí abrir conversa com Kobe sobre dependência estrutural antes da janela Platinum fechar.

Dia analisado: 22/05/2026 — 00:00–23:59 BRT
```

### Respeito de bloqueios

- **Item bloqueado:** Afirmar que a health dos campeões em Full está "caindo" ou "estável".
  - **Origem do bloqueio:** L05 Condensadora
  - **Motivo:** confiança baixa / dado ausente — pacote só traz valor pontual, sem série temporal D-7 a D-1
  - **Agregado autorizado:** sim, "penalização orgânica persiste no vetor que carrega ~74% do volume da conta" / "permaneceu abaixo de 0,85 no snapshot pontual"
  - **Tratamento aplicado:** substituído por linguagem de indício ("não dá pra cravar se está caindo", "persiste")
  - **Aparece na mensagem final:** não, como afirmação direcional; sim, como ressalva explícita

- **Item bloqueado:** Afirmar que Himmel deslocou foco de ADS para Cross-Docking ou para os campeões em Full com health degradada.
  - **Origem do bloqueio:** L05 Condensadora
  - **Motivo:** dado ausente — não há breakdown de revenue_ads por platform_item_id
  - **Agregado autorizado:** não
  - **Tratamento aplicado:** omitido — nenhuma afirmação sobre alocação ADS por item na mensagem
  - **Aparece na mensagem final:** não

- **Item bloqueado:** Citar "mix de modalidade de envio mudou para Cross-Docking" ou tratar os 47,1% Full do top10 como mudança estrutural.
  - **Origem do bloqueio:** L05 Condensadora
  - **Motivo:** divergência resolvida — fulfillment_mix_30d/7d (~74% Full) prevalece como referência estrutural
  - **Agregado autorizado:** não
  - **Tratamento aplicado:** omitido — modalidade de envio não citada na VISÃO nem na ANÁLISE
  - **Aparece na mensagem final:** não

- **Item bloqueado:** Usar o display_name "Kit 10 Potes Herméticos 1050ml Refratário 4 Travas" sem diferenciar quantidade (6 Unidades vs 10 Unidades).
  - **Origem do bloqueio:** L05 Condensadora
  - **Motivo:** colisão de display_name entre MLB4676726433 e MLB4676751119
  - **Agregado autorizado:** sim, diferenciar por quantidade no título ML
  - **Tratamento aplicado:** usado display_short da L00 que já diferencia ("10 Unidades" vs "6 Unidades")
  - **Aparece na mensagem final:** sim, como "Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades" e "Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades"

- **Item bloqueado:** Citar quais são os 5 anúncios em low_health fora do top 10.
  - **Origem do bloqueio:** L05 Condensadora
  - **Motivo:** dado ausente — account_overview entrega só contador, não IDs
  - **Agregado autorizado:** sim, "cauda de 5 anúncios em penalização orgânica fora dos campeões"
  - **Tratamento aplicado:** omitido da mensagem final por opção editorial (não citado, nem como agregado, para preservar foco nos 3 insights centrais)
  - **Aparece na mensagem final:** não

- **Item bloqueado:** Citar platform_item_id (MLB...) na mensagem.
  - **Origem do bloqueio:** L05 Condensadora
  - **Motivo:** regra ML — nenhum MLB visível no Slack
  - **Agregado autorizado:** sim, substituir por nome comercial
  - **Tratamento aplicado:** substituído por nome comercial em todas as citações (Análise, Prioridades, Top Produtos)
  - **Aparece na mensagem final:** não como MLB; sim como nome comercial

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) — metadados de pipeline, não vão para Slack.
- Preservação de ressalva por classificação `risco latente` nos 3 insights — uso de "parece", "não dá pra cravar", "indício" para manter nuance.
- Substituição de referência interna por linguagem externa — "L04 confirma..." vira afirmação direta sem citar camadas.
- Cabeçalho sem nome de Pedro e sem nome de Yasmin, conforme regra estrutural.
- Atribuição de Yasmin como responsável fixa nas 3 prioridades (L05 não atribui responsável — L06 atribui).
- Omissão de modalidade de envio na seção VISÃO MERCADO LIVRE — `fulfillment_mix_yesterday_top10` cobre só ~80% dos pedidos (68 de 84) e a L05 marcou bloqueio sobre tratar isso como dado estrutural.
- Cancelamentos incluídos na VISÃO (1) por estar disponível e relevante para contexto (relacionado à ressalva de reputação na análise).
- Top Produtos sem faturamento por produto — pacote não traz receita validada por variação, então formato é "[nome] — [pedidos] pedidos" conforme regra dura.
- Consolidação por variação (não por família) na família IMB501 — Tampa Preta, Tampa Vermelha e Tampa Cinza aparecem separadas, cada uma com seu volume.
- Uso de `display_short` da L00 verbatim para todos os 10 itens, conforme regra única.
- Inclusão de `confirmed_variation_attributes` no nome final dos 3 itens IMB501 (Tampa Preta, Tampa Vermelha, Tampa Cinza) no formato `[display_short] — [atributo confirmado]`.
- Quebra de frases longas no insight 2 e insight 3 da Análise para melhorar legibilidade, sem mudar tese nem classificação.
- Diferenciação de Catálogo (perda de Buy Box) vs Clássico (ranking de categoria) preservada no insight 2, conforme L05.
- Terminologia "modalidade de envio" usada (não "fulfillment") quando referência a Full/Cross-Docking, conforme regra.
- Risco prospectivo preservado no insight 3 (cobertura ~1,5 dia, ruptura em D+1/D+2), sem cair em formulação retrospectiva ("pedidos sem cobertura").
- Vocabulário ML preservado: "reputação" como métrica separada, "MercadoLíder Platinum" por extenso, "Catálogo", "Buy Box", "health", "Cross-Docking", "Full".
- Sem decisões ambíguas de divergência cross-layer — nomes usados na Análise/Prioridades batem com os usados no Top Produtos (Kit 4 Potes 1050ml Azul-petróleo / Jogo Potes 5 Peças Claro — Tampa Vermelha / Kit 6 Canecas Porcelana Tulipa Lisa 250ml).