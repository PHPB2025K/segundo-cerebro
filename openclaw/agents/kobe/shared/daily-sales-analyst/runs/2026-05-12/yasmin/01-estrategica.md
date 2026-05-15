<!-- llm_used=true model=sonnet fallback=false -->
### Qualidade da base

`weekly.md` e `monthly.md` estão carregados mas são templates sem entradas reais — nenhuma tese semanal ou mensal acumulada existe. As janelas numéricas (7d, 30d, 60d) têm dados completos e íntegros, o que sustenta leitura temporal. Ausência de memória qualitativa significa que não há hipóteses anteriores para confirmar ou refutar — a leitura de hoje serve como ponto de partida, não como confirmação de tese. Confiança na classificação final: média.

---

### Leitura temporal

- **vs 60d (+20% GMV, +12.6% pedidos):** A conta está acima do patamar do bimestre em volume e faturamento — sinal consistente de ganho real de patamar nos últimos 30–45 dias.
- **vs 30d (GMV +0.6%, pedidos -8.7%, ticket +10.3%):** O faturamento segura a média mensal mesmo com menos pedidos — o ticket está compensando o volume, não o volume sustentando o GMV. Sinaliza possível mix shift para itens de maior valor (Potes de Vidro dominam o topo).
- **vs 7d (GMV +24.5%, pedidos +14.8%):** Os últimos 7 dias estavam abaixo da média de 30d; hoje recuperou em direção à banda mensal. Não é aceleração — é retorno ao patamar.
- **vs mesmos dias da semana (-30.9% pedidos, -19.8% GMV):** A comparação está fortemente contaminada pelo dia 28/04 (199 pedidos, R$ 7.546 — provável evento ou campanha pontual). Excluindo o outlier, as outras 3 terças têm média de ~109 pedidos e ~R$ 4.273; contra esse benchmark limpo, o dia registra -16,7% em pedidos e -4,5% em GMV — fraqueza real mas moderada.

---

### Leitura estratégica

- **Patamar ganho, sustentado por ticket — não por volume:** A conta está num nível genuinamente superior ao de 60 dias atrás, mas a composição desse resultado mudou: o GMV segura pela alta do ticket enquanto o volume de pedidos recua contra a média de 30d. Se o ticket reverter — por pressão competitiva no produto líder, hipótese ainda não testada — o GMV cai sem a proteção do volume.
- **Concentração em um único anúncio, não em três produtos:** Os três SKUs do topo (variantes de cor do Jogo Potes Vidro 5 Peças) compartilham o mesmo `platform_item_id` (MLB3288536143) e respondem por 55% dos itens vendidos. A conta não distribui risco entre três produtos — ela concentra em um único listing em três variações. Qualquer oscilação de ranking, competitividade de preço ou problema operacional nesse anúncio move toda a conta.
- **Ausência de segundo vetor:** Os produtos de 4 a 10 somam individualmente 3–6 unidades. Não há candidato emergente na cauda capaz de assumir papel de segundo pilar. A conta opera sem rede de segurança de mix — padrão que, sem memória prévia, não é possível datar, mas que a magnitude da concentração sugere ser crônico.

---

### Tese da conta

**Vulnerável.** O GMV do dia é aceitável — alinha com a média de 30d e supera o patamar de 60d — mas a estrutura que sustenta esse número é frágil: um único anúncio concentra 55% do volume, e o canal mantém faturamento por ticket crescente, não por expansão de alcance. A conta está saudável no número, vulnerável na estrutura. Sem memória semanal ou mensal acumulada para ancorar, a classificação é fundamentada nos dados numéricos disponíveis, mas com confiança média — "inconclusiva" seria honesta se a janela temporal não entregasse o sinal de patamar em 60d tão consistente.

---

### Risco estrutural principal

- **Risco:** Dependência de um único anúncio (MLB3288536143 — Jogo Potes Vidro 5 Peças) que concentra 55% dos itens vendidos, distribuído apenas em variantes de cor do mesmo produto, sem segundo vetor real na cauda.
- **Por que importa:** Qualquer degradação de ranking, perda de competitividade de preço ou problema operacional nesse listing (estoque, reputação da oferta, concorrente com Full + preço inferior) colapsa o GMV da conta sem mecanismo de compensação. O ticket em alta pode mascarar erosão de volume por um período — até o ponto em que a redução de pedidos deixa de ser absorvida pela alta do ticket médio.
- **Histórico:** `weekly.md` e `monthly.md` são templates sem entradas — não é possível confirmar se esse padrão é crônico ou recente. Dado o nível de concentração observado, a hipótese mais provável é padrão crônico, mas permanece não confirmada.
- **Sinal de confirmação:** Concentração top 3 acima de 55% confirmada por 3 semanas consecutivas valida padrão estrutural crônico; queda de pedidos do MLB3288536143 por 2 dias seguidos sem resposta de outra linha confirma ausência de segundo vetor real.

---

### Sinais a observar

1. **Ticket acima de R$ 43 com pedidos abaixo de 85 por 3 dias consecutivos:** Consolidaria a divergência ticket/volume como tendência — e indicaria que o GMV passou a depender exclusivamente do preço médio do anúncio líder, aumentando exposição a qualquer pressão competitiva sobre ele.
2. **Concentração top 3 acima de 55% pelo segundo ciclo semanal:** Confirmaria a dependência de um único listing como padrão estrutural crônico, elevando a classificação de risco de hipótese para fato observado.
3. **Pedidos abaixo de 85 por 2 terças consecutivas (excluindo dias com evento identificado):** Indicaria que a fraqueza moderada desta terça não é ruído dentro da banda, mas início de desaceleração real no patamar atual — sinal relevante dado que o mesmo-dia-da-semana já mostrou tendência de queda excluindo o outlier de 28/04.