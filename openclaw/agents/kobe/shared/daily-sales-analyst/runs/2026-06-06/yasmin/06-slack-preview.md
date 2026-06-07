<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 06/06/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 6.611,23
• Pedidos: 162
• Ticket médio: R$ 40,81
• Cancelamentos: 5

🏆 TOP PRODUTOS MERCADO LIVRE
• Potes Vidro 5 Peças — Tampa Vermelha — 67 pedidos
• Potes Vidro 5 Peças — Tampa Preta — 12 pedidos
• Potes Vidro 5 Peças — Tampa Cinza — 10 pedidos
• Kit 6 Canecas Porcelana 250ml Canelada Colorida Café Chá Preta Canelada — 6 pedidos
• Kit 2 Potes 1520ml — 6 pedidos

🔍 ANÁLISE DA CONTA
• O sábado parece forte nos números — 162 pedidos, +40,3% vs a média dos últimos sábados. Mas 79 desses pedidos (48,8%) foram em três anúncios pausados com estoque zero, 67 deles no Potes Vidro 5 Peças — Tampa Vermelha em Full. Tirando as ordens que devem cancelar, o dia real foi ~83 pedidos e faturamento de ~R$ 3.400,00 — abaixo da média dos últimos 30 dias. O número grande é artefato de ruptura, não crescimento.
• A conta está há 2 dias com os critérios de MercadoLíder Platinum cruzados — gap zerado, progresso em 100% —, mas a medalha ainda não virou. O risco agora: a ruptura de hoje adicionou 79 cancelamentos prospectivos sobre uma taxa de cancelamento que estava em zero. Se o ML registrar esses pedidos como cancelamento pelo vendedor, a taxa pode chegar a ~1,2% — acima do limite do Platinum, no pior momento do ciclo de promoção.
• O mix de modalidade de envio do dia mostra Full em 72,8% — parece quase estável vs a média de 30 dias. Mas esse número inclui os 67 pedidos do anúncio Full pausado no cálculo. Retirando eles, o Full real cai para ~41,4%, que é o perfil da base ativa da conta — 39pp abaixo da média histórica. Os anúncios Full ativos somaram apenas 24 pedidos: não conseguem cobrir o volume do líder enquanto a reposição não chega.

🎯 PRIORIDADES DO DIA
• Yasmin: confirmar no painel do ML se os 67 pedidos do Potes Vidro 5 Peças — Tampa Vermelha (Full pausado) já foram processados como cancelamento e qual a classificação — vendedor ou comprador. Essa classificação define se a taxa de cancelamento da reputação sai de zero e ameaça a promoção para MercadoLíder Platinum, com gap zerado há 2 dias sem conversão da medalha. Confirmar/refutar por: taxa de cancelamento permanecendo em zero no próximo snapshot = risco neutralizado; qualquer valor acima de zero = série ativa, escalar para Kobe. Escalar se: taxa sair de zero no próximo snapshot ou power_seller_status seguir em Gold por mais 2 ciclos com gap zerado e progresso em 100%.
• Yasmin: confirmar o prazo estimado de reposição do estoque no CD do ML para o Potes Vidro 5 Peças — Tampa Vermelha (Full pausado). Esse prazo define se a crise dura 2-3 dias (risco pontual) ou mais de 7 dias (impacto no patamar da conta). Sem essa informação, não dá pra projetar quando o vetor principal volta nem se a cauda Full ativa consegue absorver o volume. Confirmar/refutar por: prazo ≤ 3 dias = fecha a janela de risco Platinum sem ação adicional; prazo > 7 dias ou sem reposição confirmada = abre discussão sobre o patamar da conta. Escalar se: prazo > 7 dias ou sem confirmação de reposição em 24h.
• Yasmin: checar a direção do nível de qualidade do Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo — está no 3º ciclo consecutivo em qualidade preocupante. É um dos poucos vetores Full ativos disponíveis para compensar o líder pausado; se o nível cair mais, a exposição orgânica fica ainda mais fraca. Confirmar/refutar por: qualidade estabilizando ou subindo = observar sem ação; cair mais um degrau no próximo ciclo = Yasmin alinha com Himmel sobre cobertura preventiva nesse anúncio. Escalar se: qualidade cair mais um degrau no próximo ciclo.

Dia analisado: 06/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

**Bloqueio 1 — interpretação analítica**
- **Item bloqueado:** ROAS 10,2x e ACOS 7,15% tratados como eficiência real do ADS
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Granular sinalizou que os números estão potencialmente contaminados — parte dos 67 pedidos do anúncio Full pausado pode ter sido atribuída a campanha; breakdown ADS por platform_item_id ausente (16º ciclo de pendência estrutural)
- **Agregado autorizado:** não — L05 não autorizou texto substituto sobre eficiência ADS
- **Tratamento aplicado:** métricas de ADS (ROAS, ACOS, spend, share) omitidas integralmente da mensagem Slack
- **Aparece na mensagem final:** não

**Bloqueio 2 — interpretação analítica**
- **Item bloqueado:** Faturamento R$ 6.611,23 tratado como crescimento vs avg_30d (+13,8%)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** 48,8% dos pedidos são prospectivamente canceláveis; Faturamento líquido estimado ~R$ 3.400,00, abaixo do avg_30d (R$ 5.810,35)
- **Agregado autorizado:** sim — Faturamento exibido como dado bruto em VISÃO sem comparação temporal
- **Tratamento aplicado:** R$ 6.611,23 aparece na seção VISÃO como métrica do dia, sem qualquer referência a crescimento vs 30d ou vs qualquer período
- **Aparece na mensagem final:** sim, como dado bruto em VISÃO (R$ 6.611,23)

**Bloqueio 3 — interpretação analítica**
- **Item bloqueado:** Cluster IMB501 em 54,9% do dia como concentração elevada usual
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** Leitura isolada do percentual esconde que as variações Cross-Docking ativas entregaram apenas 22 pedidos vs os 67 capturados pelo anúncio pai Full pausado — exposição perdida não migrou para as irmãs
- **Agregado autorizado:** não — L05 não autorizou citação da concentração do cluster como métrica isolada
- **Tratamento aplicado:** concentração do cluster (54,9%) não citada na mensagem; contexto de ruptura aparece no insight 1 da análise conforme formulação da L05
- **Aparece na mensagem final:** não como concentração do cluster; os volumes das variações aparecem indiretamente via Top Produtos (67, 12, 10 pedidos por variação)

---

### Decisões de formatação

**Nomes de produto — Top Produtos:**
- `IMB501V (MLB3288536143)` — usado slack_short_name "Potes Vidro 5 Peças — Tampa Vermelha" (mapeamento canônico)
- `IMB501P (MLB4535865317)` — usado slack_short_name "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico)
- `IMB501C (MLB4535865311)` — usado slack_short_name "Potes Vidro 5 Peças — Tampa Cinza" (mapeamento canônico)
- `K6CAN250P (MLB6582682928)` — usado display_short "Kit 6 Canecas Porcelana 250ml Canelada Colorida Café Chá Preta Canelada" (fallback automático; sem mapeamento manual para SKU K6CAN250P). Nota: display_short é idêntico ao title neste caso — sistema não aplicou remoção de ruído SEO para mapping_status=mapped_generic_sku; campo usado verbatim conforme regra de fallback
- `KIT2YW1520 (MLB5322494954)` — usado slack_short_name "Kit 2 Potes 1520ml" (mapeamento canônico)

**Nomes de produto — Análise da Conta e Prioridades:**
- L05 referenciou "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" (title longo) nos insights e prioridades → traduzido para "Potes Vidro 5 Peças — Tampa Vermelha" (slack_short_name canônico do IMB501V/MLB3288536143)
- L05 referenciou "Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo" na prioridade 3 → traduzido para "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo" (display_short fallback automático; sem slack_short_name para SKU KIT4YW640)

**Divergência de denominação cross-layer:**
- L05 usou "Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita" (title ML público) nos três insights e em duas prioridades; L06 usou "Potes Vidro 5 Peças — Tampa Vermelha" em todas as ocorrências — padronização com slack_short_name canônico do Top Produtos (IMB501V)
- L05 usou "Kit 4 Potes De Vidro 640ml Tampa Hermético 4 Travas Vedação Azul-petróleo" na prioridade 3; L06 usou "Kit 4 Potes de Vidro 640ml Tampa Hermético Azul-petróleo" — display_short sem slack_short_name; mesma lógica de padronização

**Modalidade de envio omitida na seção VISÃO** — fulfillment_mix_yesterday_top10 cobre apenas os 125 pedidos resolvidos do top10 e está operacionalmente contaminado pelos 67 pedidos prospectivos do anúncio Full pausado; dado não representa totalidade do dia; Condensadora não autorizou exibição em VISÃO. Mix de modalidade de envio tratado apenas na ANÁLISE conforme conteúdo da L05.

**Classificações preservadas:**
- Insight 1 (fato): escrito como afirmação direta ✓
- Insight 2 (risco latente): preservada linguagem condicional — "Se o ML registrar... a taxa pode chegar a ~1,2%"; não transformado em certeza ✓
- Insight 3 (fato): escrito como afirmação direta ✓

**Metadados internos** (padrao, base, classificacao) removidos da mensagem Slack — informação de pipeline, não transmitida a Yasmin ✓

**Atribuição de responsável:** Yasmin atribuída como responsável nas três prioridades — L05 não nomeia responsável, L06 aplica conforme regra (ML é de Yasmin) ✓

**Escalonamento para Kobe:** mantido apenas na prioridade 1, única onde L05 especificou ("escalar pra Kobe"). Prioridade 2 e 3 não receberam Kobe — L05 não especificou, L06 não adicionou ✓

**Threshold numérico de qualidade do anúncio:** L05 usa "abaixo de 0,63" como gatilho na prioridade 3 → traduzido para "cair mais um degrau no próximo ciclo" — preserva a condição de escalação sem expor pontuação interna por parentização (regra: nunca incluir valor numérico do health entre parênteses) ✓

**Valor aproximado de Faturamento líquido:** L05 diz "próximo de R$ 3,4 mil" (L03 estimou R$ 3.387,00) → escrito como ~R$ 3.400,00 com centavos explícitos e arredondamento implícito na aproximação ✓

**Full percentual pós-cancelamento:** L05 arredonda para "~41%"; L06 usa ~41,4% (valor calculado pela L04 com maior precisão) — regra exige 1 casa decimal em percentuais ✓

**Confiança "media":** nível não implica corte de insights; os três insights e as três prioridades foram mantidos integralmente. Não houve rebaixamento por confiança ✓

**GMV → Faturamento:** nenhuma ocorrência de "GMV" na mensagem Slack ✓

**ADS share → omitido:** nenhuma citação de ADS share, ROAS ou ACOS — bloqueio L05 respeitado ✓