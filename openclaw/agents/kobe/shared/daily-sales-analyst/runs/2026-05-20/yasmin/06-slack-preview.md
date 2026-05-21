<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 20/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
• Faturamento: R$ 5.087,71
• Pedidos: 91
• Ticket médio: R$ 55,91
• Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta — 23 pedidos
• Kit 4 Potes de Vidro 1050ml Retangular — 13 pedidos
• Kit 6 Canequinhas 100ml com Suporte de Madeira — 8 pedidos
• Kit 10 Potes Herméticos 1050ml Refratário 4 Travas — 5 pedidos
• Jogo Potes de Vidro 5 Peças Claro — 5 pedidos
• Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
• Kit 2 Potes de Vidro 1050ml Retangular — 3 pedidos
• Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4 Preto — 3 pedidos
• Kit 4 Potes de Vidro 320ml Tampa Hermético — 3 pedidos
• Kit 06 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos

🔍 ANÁLISE DA CONTA
• O dia parece fraco olhando para os últimos 7 dias (−20,9% de pedidos), mas a comparação correta é com os mesmos dias da semana — e aí o resultado é forte: GMV +32,4% acima da banda sazonal. O ganho veio inteiramente do ticket médio (R$55,91 vs R$41,53 nos mesmos dias da semana), não de volume. A conta cresceu por mix de produtos mais caros, não por mais alcance.
• Dois anúncios ativos estão em ruptura iminente: o de canequinhas com suporte de madeira acrílico (3 unidades restantes, ativo — cada pedido novo hoje é um cancelamento prospectivo que compromete a reputação) e o de canecas de porcelana tulipa em catálogo Full (21 unidades, ritmo de 5 pedidos/dia, ~4 dias de cobertura). O segundo é estruturalmente mais grave: catálogo Full não recupera posição no Buy Box automaticamente após a ruptura — o impacto dura além do dia da falta.
• O mix de fulfillment do dia (56,3% Full vs 73,9% no padrão de 30 dias) não sinaliza mudança no perfil da conta — foi causado por um único produto em Cross-docking que liderou com 23 pedidos. Sem ele, o mix do dia seria ~81% Full, acima do próprio histórico. Cross-docking aqui é modalidade operacional normal, não sinal de problema.

🎯 PRIORIDADES DO DIA
• Yasmin: verificar o anúncio de canequinhas com suporte de madeira acrílico (3 unidades em estoque, ativo) e executar pausa preventiva ou confirmar reposição emergencial em 24h. Cada pedido gerado hoje é cancelamento prospectivo que compromete a taxa de cancelamentos da reputação, atualmente zerada. Confirmar/refutar: pausa executada ou reposição confirmada em 24h = risco neutralizado; anúncio seguir ativo sem estoque por mais um ciclo = cancelamento prospectivo já em curso. Escalar se: cancelamento confirmado no painel ML.
• Yasmin: confirmar reposição do anúncio de canecas de porcelana tulipa (catálogo Full, 21 unidades) com chegada ao CD do ML em até 3 dias. Ao ritmo de 5 pedidos/dia a cobertura é de ~4 dias — catálogo Full não recupera posição no Buy Box automaticamente após ruptura. A janela para agir sem impacto na posição é hoje. Confirmar/refutar: reposição confirmada com ETA ≤3 dias = risco encaminhado; sem confirmação = ruptura prospectiva em curso. Escalar se: sem reposição confirmada em 24h — alertar Trader sobre ruptura prospectiva em catálogo Full.

Dia analisado: 20/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atributo "Tampa Vermelha" na identificação do anúncio de potes de vidro 5 peças (IMB501V / MLB3288536143)
- **Origem do bloqueio:** Granular (L04) + Condensadora (L05)
- **Motivo:** Título ML primário ("Jogo Potes De Vidro 5 Peças Claro Mantimentos Marmita") não confirma o atributo de cor da tampa; display_name interno adiciona "Tampa Vermelha" por inferência de família SKU, não por confirmação explícita; risco de identificação médio declarado pela L04
- **Agregado autorizado:** sim — uso do título ML sem o atributo de cor adicionado
- **Tratamento aplicado:** substituído por "Jogo Potes de Vidro 5 Peças Claro" (baseado no título ML)
- **Aparece na mensagem final:** sim, como "Jogo Potes de Vidro 5 Peças Claro"

---

- **Item bloqueado:** Afirmação de que o campeão de volume em Cross-docking (potes de vidro redondos tampa preta, 23 pedidos) foi impulsionado por ADS Himmel
- **Origem do bloqueio:** Condensadora (L05)
- **Motivo:** Hipótese em aberto; pacote ml_snapshot v1 não disponibiliza breakdown de receita ADS por platform_item_id; correlação plausível mas não confirmada
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — ADS share mencionado na análise apenas como dado contextual (inserido via insight 3 sobre mix de fulfillment), sem afirmar causalidade
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Direção do health dos anúncios Full em zona crítica (caindo / estável / recuperando)
- **Origem do bloqueio:** Condensadora (L05) / Granular (L04)
- **Motivo:** ml_snapshot v1 entrega apenas valores pontuais de health; sem série temporal (D-1, D-2), não é possível classificar tendência para nenhum dos anúncios afetados
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — health não mencionado na mensagem; o risco operacional foi comunicado via impacto de ruptura (estoque crítico), não via tendência de health
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Códigos MLB internos (MLB4073003575, MLB3288536143, MLB4410218897, MLB6167272090) no corpo da mensagem
- **Origem do bloqueio:** Condensadora (L05)
- **Motivo:** Identificadores técnicos internos; não adequados para comunicação operacional no Slack
- **Agregado autorizado:** não aplicável — substituição por descrição operacional do produto
- **Tratamento aplicado:** substituídos por descrições de produto em linguagem operacional
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Afirmação isolada de que "4 dos 10 produtos do top10 estão em zona crítica de health"
- **Origem do bloqueio:** Condensadora (L05)
- **Motivo:** Dois anúncios em penalização ativa (0,71 e 0,75) e dois no limiar (0,85) representam níveis distintos; sem série temporal para nenhum deles; apresentar sem ressalva de confiança induziria alarme sem base confirmada para ação imediata
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido como afirmação consolidada; o risco dos dois casos mais graves (0,75 e 0,71) foi absorvido contextualmente no insight 2 sobre ruptura de estoque, sem citar health explicitamente
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) dos três insights da Condensadora — motivo: campos de pipeline interno, sem lugar na comunicação para o destinatário
- Substituição do display_name "Conjunto 5 Potes de Vidro Redondos Tampa Vermelha" por "Jogo Potes de Vidro 5 Peças Claro" em Top Produtos — motivo: bloqueio de atributo "Tampa Vermelha" pela L04/Condensadora; título ML primário usado como base
- Faturamento por produto omitido em todos os itens do Top Produtos — motivo: pacote não traz receita validada por produto/variação; proibido calcular ou estimar; formato aplicado: `[nome] — [pedidos] pedidos`
- Display name truncado de KIT4YW320 ("Kit Conjunto 4 Potes De Vidro 320ml Tampa Hermético 4 Travas Azul-pet...") encurtado para "Kit 4 Potes de Vidro 320ml Tampa Hermético" — motivo: remoção de truncamento técnico (`...`); produto identificável sem o sufixo de cor; sem risco de ambiguidade com outros produtos da lista
- Sem comparação temporal na seção VISÃO MERCADO LIVRE — motivo: regra estrutural; comparações pertencem à análise
- Fulfillment (Full/Cross-docking) omitido da seção VISÃO — motivo: dado disponível cobre apenas top 10 itens (71 de 91 pedidos), não a totalidade do dia; número parcial não representa dado objetivo da plataforma sem ressalva de cobertura; cobertura de 78% não justifica apresentação como métrica total na VISÃO
- Insight 2 mantido com linguagem de risco latente ("ruptura iminente", "estruturalmente mais grave", "impacto dura além do dia") — motivo: Condensadora classificou como risco latente, não fato; linguagem preserva a nuance sem transformar em certeza
- Insight 1 mantido com marcador de aparência enganosa ("parece fraco", "mas a comparação correta é") — motivo: padrão C de inversão negativa da Condensadora; suavizar ou remover o contraste mudaria a tese
- Prioridades formatadas com ação + motivo + sinal de confirmação/refutação + condição de escalada — motivo: elementos presentes na Condensadora; preservados por instrução estrutural de fidelidade à fonte
- Produto SPC0111 mantido no ranking como "Suporte Gamer 2 Controles e Headset Mesa Organizador PS5/PS4 Preto" — motivo: confidence medium mas display_name coincide com título ML; sem bloqueio declarado pela Condensadora; produto identificável sem risco de ambiguidade relevante para o responsável
- Condensadora entregou 3 insights; todos os 3 incluídos — não houve caso de dia sem insight