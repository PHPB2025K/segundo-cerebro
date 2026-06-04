<!-- llm_used=true model=claude-sonnet-4-6 fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE BUDAMIX STORE — 01/06/2026 (Ontem)

📊 VISÃO SHOPEE BUDAMIX STORE
- Faturamento: R$ 3.092,25
- Pedidos: 68
- Ticket médio: R$ 45,47
- Cancelamentos: 7

🏆 TOP PRODUTOS SHOPEE BUDAMIX STORE
- Jarra Medidora 500ml — 19 pedidos
- Kit 6 Canecas Tulipa 250ml — 15 pedidos
- Potes Vidro 5 Peças — Tampa Preta — 15 pedidos
- Pote Vidro 520ml — Quadrado — 5 pedidos
- Kit 2 Potes 800ml — Quadrado — 4 pedidos

🔍 ANÁLISE DA CONTA
- O faturamento de R$ 3.092,25 parece dia normal, mas os três produtos que geraram 72% dele — Jarra Medidora 500ml, Kit 6 Canecas Tulipa 250ml e Potes Vidro 5 Peças — Tampa Preta — encerraram em estoque zero. Sem Vendedor Indicado, fora do Shopee Mall e com Programa de Frete Grátis em 0%, a conta não tem amortecedor de visibilidade ativo: se a reposição atrasar, a posição orgânica desses anúncios pode começar a eroder a partir de amanhã.
- O dia rendeu pelo ticket, não pelo volume: 68 pedidos ficaram 6% abaixo dos mesmos dias da semana anteriores, mas o ticket de R$ 45,47 — 15% acima do baseline 60d — sustentou o faturamento. Para uma conta com papel Volume/Giro, o motor de escala não performou no dia, ainda que o resultado financeiro tenha se sustentado.
- Saúde da Loja e Shopee Ads estão indisponíveis, e Programa de Afiliados Shopee e Cashback em Moedas Shopee não estão acessíveis via Open API por limitação estrutural — a conta está em zona cega: os 7 cancelamentos (~10%) e o anúncio banido não identificado ficam sem contexto oficial, e qualquer decisão sobre Shopee Ads está bloqueada até o desbloqueio do escopo de acesso.

🎯 PRIORIDADES DO DIA
- Lucas: verificar estoque dos três campeões (Jarra Medidora 500ml, Kit 6 Canecas Tulipa 250ml e Potes Vidro 5 Peças — Tampa Preta) junto ao CD e providenciar reposição para D+1. Os três responderam por 72% do faturamento de ontem e encerraram em estoque zero — sem booster de visibilidade ativo na conta, rebaixamento orgânico acumula a partir de amanhã se permanecerem zerados. Confirmar/refutar por: reposição confirmada até amanhã = risco operacional neutralizado; qualquer dos três permanecendo zerado mais um dia = avaliar erosão de posição em D+2; somando ≤5 pedidos combinados em qualquer dos próximos 2 dias = ruptura efetiva confirmada. Escalar se: dois ou mais permanecerem zerados após D+2 — levar ao Pedro como questão de gestão estrutural de estoque.
- Lucas: identificar o anúncio banido no Seller Center e verificar se gerou pedidos no dia 01/06. O pacote registra 1 banimento sem expor qual item — se gerou pedidos, eles entram como cancelamentos prospectivos pressionando a taxa do vendedor, risco que cruza com os 7 cancelamentos do dia sem contexto oficial disponível. Confirmar/refutar por: anúncio banido sem pedidos no dia = risco nulo; com pedidos = Lucas registra volume e inicia controle preventivo de cancelamentos. Escalar se: volume relevante de pedidos concentrado no anúncio banido.
- Lucas: registrar este dia como ponto zero da série de observação da conta — ticket R$ 45,47, 68 pedidos, composição do top 3: Jarra Medidora 500ml (19 pedidos), Kit 6 Canecas Tulipa 250ml (15), Potes Vidro 5 Peças — Tampa Preta (15). É a primeira leitura estruturada após período sem dados — sem essa base, os próximos dias rodam sem referência comparável. Confirmar/refutar por: ticket ≥ R$ 48,00 por 3 dias seguidos = sinal de migração de mix, tese da conta precisa refinamento; ticket abaixo de R$ 42,00 por 2 dias = normalização, sustenta papel atual.

Dia analisado: 01/06/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Identidade do anúncio banido e se gerou pedidos no dia 01/06
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** `banned_ids` não exposto no pacote; `top_items_details.items` veio vazio — identificação não determinável
- **Agregado autorizado:** não
- **Tratamento aplicado:** citado apenas como "anúncio banido não identificado" sem nomear item ou atribuir pedidos
- **Aparece na mensagem final:** sim, como "o anúncio banido não identificado"

---

- **Item bloqueado:** Fôlego em dias ou horas por campeão e priorização diferenciada entre os três produtos zerados
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** `top_items_details.items` veio vazio mesmo com `status='ok'` — `available_quantity` por item ausente; ritmo de venda por `platform_item_id` não disponível no pacote
- **Agregado autorizado:** não — apenas afirmação binária "estoque zero"
- **Tratamento aplicado:** nenhum cálculo de fôlego incluído; condição descrita como "estoque zero" sem priorizar urgência entre os três
- **Aparece na mensagem final:** não (o bloqueio foi respeitado; apenas "estoque zero" aparece como condição)

---

- **Item bloqueado:** Concentração ou pulverização dos 7 cancelamentos por anúncio e comparação com taxa oficial do vendedor
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** `metrics.cancelamentos` é total agregado da conta sem breakdown por `platform_item_id`; `shop_performance.cancellation_rate_seller_pct` indisponível (HTTP 404)
- **Agregado autorizado:** não
- **Tratamento aplicado:** cancelamentos citados apenas como total do dia ("7 cancelamentos, ~10%") sem caracterizar distribuição nem comparar com taxa oficial
- **Aparece na mensagem final:** sim, como "7 cancelamentos (~10%)" — apenas o total bruto

---

- **Item bloqueado:** Modalidade de envio dos 68 pedidos do dia em específico (Shopee Full / SLS / Drop-off)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** `metrics.fulfillment` veio com contadores zerados; `fulfillment_mix_yesterday_top10` unavailable — atribuição por pedido não determinável
- **Agregado autorizado:** não
- **Tratamento aplicado:** modalidade de envio omitida da seção `📊 VISÃO SHOPEE BUDAMIX STORE`; não introduzida em nenhuma outra seção por ausência de autorização da Condensadora
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Comparação cross-account ou citação nominal de canibalização com outras contas Shopee Budamix
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** função exclusiva da L06b Consolidadora; mensagem individual não tem base de dados das outras contas
- **Agregado autorizado:** não aplicável
- **Tratamento aplicado:** nenhuma referência às outras contas Shopee; VISÃO e TOP PRODUTOS exibem apenas dados desta conta
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- `padrao`, `base` e `classificacao` — removidos da mensagem; são metadados internos de pipeline, não aparecem no Slack

- Insight 1 (`classificacao: "risco latente"`) — preservada nuance com "parece dia normal", "pode começar a eroder", "se a reposição atrasar"; não transformado em certeza

- Insight 3 (`classificacao: "risco latente"`) — preservada incerteza via "zona cega" e "ficam sem contexto oficial"; afirmação de bloqueio do Shopee Ads mantida como fato (bloqueio é confirmado, não hipótese); sem hedging excessivo nos fatos técnicos confirmados

- Insight 2 (`classificacao: "fato"`) — escrito diretamente, sem hedging adicional

- CK4742 — usado `slack_short_name` "Jarra Medidora 500ml" (mapeamento canônico)

- CTL002 — `slack_short_name` é null; `display_short` = "Jogo com 6 Canecas Tulipa 250ml Porcelana Colorida para Mesa e Cozinha" (equivalente ao `raw_title`, sem simplificação aplicada); `display_name` = "Kit 6 Canecas Tulipa 250ml" é a forma simplificada real disponível no pacote — usado `display_name` "Kit 6 Canecas Tulipa 250ml" como representação mais fiel ao espírito de encurtamento; decisão registrada: `display_short` não aplicou simplificação para este SKU (fallback automático; sem mapeamento manual para SKU CTL002)

- IMB501P — usado `slack_short_name` "Potes Vidro 5 Peças — Tampa Preta" (mapeamento canônico); atributo "Tampa Preta" mantido conforme `confirmed_variation_attributes` e codificação de sufixo SKU

- KIT2YW520SQ — usado `slack_short_name` "Pote Vidro 520ml — Quadrado" (mapeamento canônico)

- KIT2YW800SQ — usado `slack_short_name` "Kit 2 Potes 800ml — Quadrado" (mapeamento canônico)

- Nomes de produtos nas seções `🔍 ANÁLISE DA CONTA` e `🎯 PRIORIDADES DO DIA` — todos traduzidos para os mesmos short names usados no TOP PRODUTOS; L05 usava "Jarra Medidora de Vidro 500ml", "Kit 6 Canecas Tulipa 250ml" e "Conjunto 5 Potes de Vidro Redondos Tampa Preta" — substituídos por "Jarra Medidora 500ml", "Kit 6 Canecas Tulipa 250ml" e "Potes Vidro 5 Peças — Tampa Preta" respectivamente

- "R$ 3.092" da L05 (insight 1) — corrigido para R$ 3.092,25 com centavos obrigatórios; correção permitida por regra explícita de padrão numérico

- Modalidade de envio omitida da seção VISÃO por cobertura parcial; `fulfillment_mix_yesterday_top10` indisponível e `metrics.fulfillment` com contadores zerados — não citada em nenhuma seção

- Atribuição de Lucas como responsável em todas as 3 prioridades; L05 não atribui responsável — atribuição feita aqui conforme regra da seção

- "neste ciclo" (linguagem de pipeline) substituído por "no dia" ou omitido nas prioridades

- `item_ids` Shopee (23993264258, 45554989236, 22393168887 e outros) — nenhum exibido na mensagem final

- Escalar para Himmel não incluído — L05 não trouxe acionamento de Himmel nas prioridades condensadas (Shopee Ads está bloqueado tecnicamente, sem base para acionar)

- Prioridade 3 sem linha "Escalar se" — L05 marcou explicitamente "não aplicável"

- `alertas_de_confianca.nivel` = "media" — mantidas ressalvas pontuais (zona cega, contexto oficial indisponível) sem tratar o relatório inteiro como inconclusivo; 3 insights apresentados conforme entregue pela Condensadora