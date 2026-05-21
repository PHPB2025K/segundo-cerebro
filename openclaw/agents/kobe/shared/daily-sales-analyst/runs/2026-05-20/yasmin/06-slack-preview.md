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
• Suporte Gamer 2 Controles e Headset Mesa PS5/PS4 Preto — 3 pedidos
• Kit 4 Potes de Vidro 320ml Tampa Hermético 4 Travas — 3 pedidos
• Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
• O volume está -20,9% vs 7 dias, mas esse número distorce a leitura — a média de 7 dias foi inflada pelo pico de 29/04 (134 pedidos). O controle correto é o mesmo dia da semana: -1,6%. O GMV acima de R$ 5.000 não vem de mais alcance, vem de ticket maior. Os pedidos estão no mesmo patamar dos últimos 60 dias enquanto o GMV cresceu +34,2% no mesmo período. É expansão via mix qualificado, não fraqueza de demanda.
• O resultado parece positivo, mas o patamar de R$ 5.000+ depende de ADS — 59,8% do GMV veio de campanha (R$ 3.041 dos R$ 5.087). Isso roda sobre uma base orgânica com dois campeões em Full com health penalizada, abaixo do threshold do ML, o que já significa perda de exposição orgânica ativa nesses anúncios. Enquanto Himmel entrega ROAS alto, o orgânico não se recupera no mesmo ritmo. O patamar atual não é orgânico conquistado.
• O único ponto que exige ação hoje é o estoque do Kit 06 Canequinhas com Suporte Acrílico em fulfillment: 4 unidades disponíveis, 3 pedidos ontem — cobertura de cerca de 1 dia. Se zerar sem reposição ou pausa manual, o ML continua aceitando pedidos e os próximos viram cancelamentos automáticos que começam a mover a taxa de cancelamento, hoje em zero. Os 3 cancelamentos do dia não têm distribuição por anúncio disponível — não dá para descartar que parte já veio desse item.

🎯 PRIORIDADES DO DIA
• Yasmin: confirmar estoque físico real e reposição do Kit 06 Canequinhas com Suporte Acrílico junto à expedição. Com 4 unidades em fulfillment e 3 pedidos ontem, o horizonte de ruptura é de aproximadamente 1 dia — ruptura sem pausa manual gera cancelamentos automáticos que impactam reputação, hoje em zero. Confirmar/refutar: reposição em 24h = risco neutralizado; sem reposição e anúncio ainda ativo amanhã = registrar como fonte de novos cancelamentos. Escalar se anúncio zerar com pedidos sendo aceitos — alinhar pausa manual antes que o ML gere cancelamentos automáticos.
• Yasmin: checar a direção do health dos dois campeões em Full com penalização — Kit 4 Potes 1050ml Retangular (health 0,75) e potes redondos Tampa Vermelha em fulfillment (health 0,71). A tese da conta é ADS compensando orgânico degradado; saber se o health está caindo, estável ou subindo é o dado que falta para decidir se a dependência de ADS vai se aprofundar. Confirmar/refutar: health estável ou subindo nos dois = manter observação sem ação; health caindo em um ou nos dois = Yasmin alinha com Himmel sobre cobertura preventiva antes da próxima semana. Escalar se health cair por 2 ciclos consecutivos em ambos.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** `Kit 6 Tigelas de Vidro 250ml` (display_name interno do TL6250 / MLB6167272090)
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** display_name incorreto — produto real confirmado por raw_title e ml_snapshot é `Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara`; categorias e materiais completamente distintos (canecas de porcelana ≠ tigelas de vidro)
- **Agregado autorizado:** não — a Condensadora não autorizou agregado; a Granular resolveu com nome correto por raw_title
- **Tratamento aplicado:** substituído pelo nome correto conforme resolução da Granular: `Kit 6 Canecas Porcelana Tulipa Lisa 250ml`
- **Aparece na mensagem final:** sim, como `Kit 6 Canecas Porcelana Tulipa Lisa 250ml` (nome correto, não o alias bloqueado)

---

- **Item bloqueado:** Suporte Gamer SPC0111 / MLB6661811594 como insight ou sinal analítico
- **Origem do bloqueio:** Condensadora
- **Motivo:** 3 pedidos com mapeamento de confiança média e histórico de 32 unidades totais é microamostra insuficiente para qualquer leitura
- **Agregado autorizado:** não
- **Tratamento aplicado:** produto mantido apenas no ranking Top Produtos (3 pedidos, posição decrescente correta), sem menção em análise ou prioridades
- **Aparece na mensagem final:** sim, apenas no ranking de Top Produtos como linha de pedidos — sem análise associada

---

- **Item bloqueado:** Concentração dos 3 cancelamentos em produto específico
- **Origem do bloqueio:** Granular + Condensadora
- **Motivo:** breakdown por anúncio ausente do pacote; distribuição inconclusiva
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados como total (3) com ressalva de que a distribuição por anúncio não está disponível no pacote
- **Aparece na mensagem final:** sim, como dado objetivo em VISÃO e como contexto de incerteza em ANÁLISE — sem atribuição a produto específico

---

- **Item bloqueado:** Afirmação sobre priorização de ADS de Himmel no campeão Cross-docking (MLB4535865317)
- **Origem do bloqueio:** Condensadora
- **Motivo:** breakdown de receita ADS por anúncio ausente; hipótese plausível mas não confirmada
- **Agregado autorizado:** não
- **Tratamento aplicado:** citado como hipótese não confirmável — não entrou nominalmente em análise nem em prioridades
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Direção do health dos anúncios penalizados como fato
- **Origem do bloqueio:** Condensadora
- **Motivo:** pacote contém apenas ponto único sem série temporal; direção não é determinável
- **Agregado autorizado:** não
- **Tratamento aplicado:** prioridade formulada como checagem a realizar ("checar a direção"), não como fato estabelecido
- **Aparece na mensagem final:** sim, como ação de verificação — não como afirmação de direção

---

- **Item bloqueado:** Leitura de -20,9% em pedidos vs 7 dias como deterioração
- **Origem do bloqueio:** Condensadora
- **Motivo:** artefato do outlier de 29/04; não reflete tendência real
- **Agregado autorizado:** não aplicável — a Condensadora forneceu a leitura correta substituta
- **Tratamento aplicado:** dado usado como ponto de partida para explicar a inversão correta, preservando exatamente a tese da Condensadora
- **Aparece na mensagem final:** sim, como contexto de inversão corrigida — não como sinal de deterioração

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional`, `— base: Tática + Granular`, `Padrão B/C/E`) — metadados de pipeline não pertencem ao Slack
- Nome correto aplicado para TL6250/MLB6167272090: `Kit 6 Canecas Porcelana Tulipa Lisa 250ml` no lugar de `Kit 6 Tigelas de Vidro 250ml` — divergência resolvida pela Granular com confiança alta; raw_title prevalece
- Prioridades formuladas com ação + por quê + sinal de confirmação/refutação + condição de escalonamento — todos os elementos presentes na Condensadora foram preservados
- Ranking Top Produtos em ordem decrescente por pedidos: 23 / 13 / 8 / 5 / 5 / 5 / 3 / 3 / 3 / 3 — ordem correta mantida; empates (5/5/5 e 3/3/3/3) preservados na sequência em que aparecem no pacote validado
- Faturamento por produto omitido de Top Produtos — pacote não traz receita validada por produto/variação; proibido calcular ou estimar
- Suporte Gamer incluído no ranking com nome ligeiramente encurtado (`Suporte Gamer 2 Controles e Headset Mesa PS5/PS4 Preto`) para legibilidade; sem alterar identidade do produto
- Kit 4 Potes 320ml: display_name truncado no pacote (`Azul-pet...`) — usado nome sem truncamento mas mantendo apenas o atributo identificável sem expandir além do que o pacote confirma: `Kit 4 Potes de Vidro 320ml Tampa Hermético 4 Travas`
- Quebra de frase em insight 1 não necessária — texto da Condensadora já estava direto e coerente; preservado sem reescrita
- SKUs crus e platform_item_ids omitidos integralmente da mensagem final — regra aplicada a todos os 10 produtos do top10
- Referências internas substituídas: nenhuma camada citada pelo nome na mensagem final
- Confiança média da Condensadora preservada via linguagem de indício nos alertas: "não dá para descartar", "sugere", "parece"; nenhum insight convertido em certeza
- `Kit 06 Canequinhas com Suporte Acrílico` usado como nome de produto no lugar do display_name completo `Kit 06 Canequinhas De 100 Ml Com Suporte De Madeira Acrílico` — encurtamento para legibilidade mantendo identidade sem ambiguidade; mesma referência usada de forma consistente em análise e prioridades
- Anúncio da Tampa Vermelha referenciado como "potes redondos Tampa Vermelha em fulfillment" em prioridades — linguagem operacional clara sem usar MLB nem SKU, alinhado com o tratamento da Condensadora