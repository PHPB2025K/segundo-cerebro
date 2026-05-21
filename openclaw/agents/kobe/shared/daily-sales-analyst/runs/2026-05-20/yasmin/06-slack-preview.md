<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 5.087,71
- Pedidos: 91 pedidos
- Ticket médio: R$ 55,91
- Cancelamentos: 3
- Itens vendidos: 97

🏆 TOP PRODUTOS MERCADO LIVRE
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 23 pedidos
- Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
- Kit 6 Canequinhas 100ml — 8 pedidos
- Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Vermelha — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
- Suporte Gamer 2 Controles E Headset Mesa Organizador Ps5 Ps4 Preto — 3 pedidos
- Kit 4 Potes de Vidro 320ml Tampa Hermético 4 Travas — 3 pedidos
- Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
- O anúncio de potes redondos com tampa vermelha (5º do dia, fulfillment) tem health=0,71 — mas o risco não é de queda em ranking de categoria, é de perda de Buy Box. O anúncio é de Catálogo, e penalização de health em catálogo pressiona o slot principal de conversão diretamente, com recuperação mais lenta e menos previsível do que em anúncio Clássico. A urgência real é maior do que uma leitura de erosão orgânica sugere.
- O Kit 06 Canequinhas com Suporte Acrílico terminou o dia com estoque zerado e anúncio ainda ativo — o snapshot de 21/05 às 16h confirma que a situação não foi resolvida. Com cancellations_rate em zero e reputação 5_green/gold, qualquer pedido adicional sem estoque gera cancelamento desnecessário que começa a erodir o único indicador limpo da conta.
- O GMV do dia ficou bem acima da banda histórica (+32% vs mesmas quartas), mas o volume de pedidos foi praticamente igual ao bimestre — o crescimento é inteiramente pelo ticket. Sessenta por cento do GMV veio de ADS com ROAS de 11,6x. A conta está crescendo, mas sobre base concentrada e com orgânico ainda não validado: quando o ADS performa bem o número parece robusto; sem ele, o piso é desconhecido.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar situação do Kit 06 Canequinhas com Suporte Acrílico (MLB4410218897) e decidir entre reposição emergencial no CD do ML ou pausa controlada do anúncio. Estoque zerado com anúncio ativo — o snapshot de 21/05 às 16h não mostrou resolução; qualquer pedido adicional gera cancelamento que contamina o cancellations_rate hoje em zero. Confirmar/refutar: reposição ou pausa efetivada = risco neutralizado; cancelamento no próximo ciclo sem ação = risco materializado. Escalar se: cancelamento registrado sem ação → registrar como variável confundidora para a série de reputação.
- Yasmin: checar a direção — estável, caindo ou recuperando — do health dos dois anúncios com penalização ativa: Kit 4 Potes 1050ml (health=0,75, Clássico) e potes redondos com tampa vermelha (health=0,71, Catálogo). Primeira leitura disponível para ambos — o de catálogo tem mecanismo de dano mais grave via Buy Box. Confirmar/refutar: health estável ou em recuperação em ambos por 2 ciclos = observar sem ação; health caindo em ao menos um por 2 dias consecutivos = acionar Himmel. Escalar se: health caindo em qualquer um por 2 dias → alinhar com Himmel sobre cobertura preventiva de ADS.
- Yasmin: iniciar reposição das canecas porcelana tulipa (MLB6167272090, fulfillment, Catálogo) — available_quantity=21 com cobertura de aproximadamente 4 dias ao ritmo atual; janela para reposição em fulfillment fecha em torno de 22/05 para garantir continuidade antes de 25/05. Ruptura em Catálogo impacta Buy Box diretamente. Confirmar/refutar: reposição iniciada até 22/05 = risco controlado; estoque chegando a zero sem reposição = perda de Buy Box em catálogo ativo.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** TL6250 / MLB6167272090 — alias interno "Kit 6 Tigelas de Vidro 250ml"
- **Origem do bloqueio:** Granular (confiança alta) → confirmado pela Condensadora
- **Motivo:** Alias descreve categoria radicalmente diferente do produto real. "Tigelas de Vidro" (utensílios de mesa) vs produto real "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Xícara" (xícaras de café/bebida em porcelana). Raw_title do pedido e title da API ML convergem contradizendo o alias.
- **Agregado autorizado:** sim — uso do título correto: "Kit 6 Canecas Porcelana Tulipa Lisa 250ml"
- **Tratamento aplicado:** substituído pelo título correto conforme fonte primária (top_items_details + raw_title)
- **Aparece na mensagem final:** sim, como "Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos"

---

- **Item bloqueado:** Origem dos 3 cancelamentos do dia (breakdown por anúncio)
- **Origem do bloqueio:** Condensadora
- **Motivo:** Pacote não contém breakdown de cancelamentos por platform_item_id — hipótese de concentração no MLB4410218897 é plausível mas não evidenciada
- **Agregado autorizado:** não — dado ausente, não fabricar inferência
- **Tratamento aplicado:** omitido da mensagem; cancelamentos aparecem apenas como contagem objetiva na seção VISÃO (3 cancelamentos)
- **Aparece na mensagem final:** não (exceto contagem agregada em VISÃO)

---

- **Item bloqueado:** Concentração de revenue_ads por anúncio
- **Origem do bloqueio:** Condensadora
- **Motivo:** ads_summary contém apenas totais agregados — breakdown por anúncio ausente; hipótese de ADS amplificando anúncio Cross-Docking não confirmável
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido; ADS aparece apenas como share total (60% do GMV, ROAS 11,6x) na análise da conta, conforme Condensadora
- **Aparece na mensagem final:** não (breakdown por anúncio ausente; totais presentes na análise conforme aprovado)

---

- **Item bloqueado:** Direção e causa do health=0,71 do MLB3288536143 (potes tampa vermelha)
- **Origem do bloqueio:** Condensadora
- **Motivo:** Pacote contém apenas valor pontual — série histórica, claims e causa ausentes; comunicar como tendência confirmada seria fabricar evidência
- **Agregado autorizado:** sim — comunicar como valor pontual com linguagem de indício, sem afirmar direção
- **Tratamento aplicado:** preservada linguagem de indício; health=0,71 citado como valor atual sem afirmar trajetória
- **Aparece na mensagem final:** sim, como valor pontual com ressalva de que é primeira leitura

---

- **Item bloqueado:** Confirmação de que ação sobre MLB4410218897 foi tomada ou risco neutralizado
- **Origem do bloqueio:** Condensadora
- **Motivo:** Snapshot de 21/05 às 16:33 BRT mostra status=active e available_quantity=3 — ação não refletida até coleta; comunicar como risco resolvido seria impreciso
- **Agregado autorizado:** sim — comunicar como risco ainda em aberto no horário do snapshot
- **Tratamento aplicado:** preservada linguagem de risco em aberto; "snapshot de 21/05 às 16h confirma que a situação não foi resolvida"
- **Aparece na mensagem final:** sim, como risco ainda em aberto

---

### Decisões de formatação

- Remoção de metadados internos ("base: Granular + Operacional", "padrão: E", etc.) de todos os insights — motivo: são referências de pipeline interno, proibidas no Slack
- Preservação de linguagem de indício no insight 3 ("parece robusto", "piso é desconhecido") — motivo: Condensadora classificou como hipótese/risco latente, não fato; proibido transformar em certeza
- Preservação do conectivo "mas" nos três insights — motivo: conectivo de contraste carrega a inversão analítica central de cada insight; troca por "e" ou "e também" destruiria a tese
- Uso do título correto "Kit 6 Canecas Porcelana Tulipa Lisa 250ml" no Top Produtos, substituindo alias bloqueado "Kit 6 Tigelas de Vidro 250ml" — motivo: bloqueio de identidade confirmado pela Granular com confiança alta; fonte primária é top_items_details.title + raw_title
- Uso de "Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico" no Top Produtos para MLB4410218897 — motivo: título real do anúncio via top_items_details sem SKU cru visível; display_name interno preservado sem o código "914C_BAV"
- Omissão de "Kit 6 Tigelas de Vidro 250ml" como nome alternativo — motivo: bloqueio ativo; apenas título correto permitido
- Quebra de "Sessenta por cento do GMV veio de ADS com ROAS de 11,6x" em frase separada dentro do mesmo bullet — motivo: frase longa; quebra mantém todos os termos analíticos e a tese intacta
- Preservação de "health=0,75" e "health=0,71" como valores numéricos explícitos nas prioridades — motivo: métricas concretas que ajudam Yasmin a identificar qual anúncio checar sem recorrer a identificadores opacos; Condensadora as incluiu nas prioridades
- Omissão do breakdown de cancelamentos por anúncio — motivo: bloqueio ativo; contagem de 3 cancelamentos mantida apenas na VISÃO como dado objetivo
- Omissão do breakdown de ADS por anúncio — motivo: bloqueio ativo; share total e ROAS mantidos na análise conforme Condensadora
- Inclusão de MLB4410218897 e MLB6167272090 nas prioridades com identificadores de anúncio — motivo: Condensadora incluiu explicitamente; ajuda Yasmin a localizar o anúncio correto; SKU interno não exposto, apenas o platform_item_id
- Ordenação do Top Produtos em ordem decrescente por pedidos (23, 13, 8, 5, 5, 5, 3, 3, 3, 3) — motivo: regra obrigatória de ranking decrescente; produtos com 5 pedidos preservados em três linhas distintas (variações e produtos diferentes)
- Prioridades formatadas com estrutura completa: ação + por quê + confirmar/refutar + escalar se — motivo: Condensadora trouxe todos esses elementos para as 3 prioridades; regra de preservação de condições de confirmação/refutação e escalonamento