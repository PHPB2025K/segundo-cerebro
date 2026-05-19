<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 18/05/2026 (Ontem)

📊 VISÃO SHOPEE
• Consolidado: 84 pedidos — R$ 4.768,84 — ticket médio R$ 56,77
• Budamix Store: 59 pedidos — R$ 2.497,44 — 3 cancelamentos
• Budamix Oficial (Conta 2): 16 pedidos — R$ 1.570,30
• Budamix Shop (Conta 3): 9 pedidos — R$ 701,10

🏆 TOP PRODUTOS SHOPEE
• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 27 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 18 pedidos
• Kit 6 Canecas Tulipa 250ml — 15 pedidos (Store 7 + Conta 2: 4 + Conta 3: 4)
• Kit 4 Potes de Vidro 800ml Quadrado (Conta 2) — 4 pedidos
• Conjunto 5 Potes de Vidro Redondos Tampa Cinza (Conta 2) — 3 pedidos
• Kit 6 Canecas Retas 200ml (Conta 3) — 2 pedidos
• Kit 2 Potes de Vidro 800ml Quadrado — 2 pedidos (Store 2 + Conta 3: 2 — consolidado cross-conta)

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee entregou 84 pedidos e R$ 4.768,84, mas o resultado esconde três dinâmicas distintas que não podem ser tratadas como uma só: a Store sustenta o volume com dois produtos e ticket em alta, a Oficial colapsa em pedidos mas segura GMV via ticket elevado, e a Shop está em ausência de mecanismo de geração de demanda — não em queda de demanda passageira. O risco real não está no consolidado; está localizado na Conta 3, e a ação deve ser cirúrgica.

🟠 *Budamix Store (Shopee 1):* A Store explica 70% dos pedidos e 52% do GMV da plataforma, mas opera com dois produtos respondendo por 76% do volume — Tampa Preta (27 pedidos) e Jarra Medidora (18 pedidos) — sem segundo vetor estabelecido, e em trajetória de queda de patamar consistente em múltiplas janelas (-27% vs 30d, -36% vs 60d); o ticket subindo (+8,5% vs 30d) amortece o GMV mas não inverte a direção, e em cenário de concentração extrema qualquer oscilação nos dois campeões se traduz diretamente em colapso de resultado sem amortecimento de cauda.

🟠 *Budamix Oficial (Shopee 2):* A Conta 2 entregou o ticket mais alto das três (R$ 98,14 vs média 30d de R$ 60,05), parcialmente sustentado por comportamento multi-item no Kit 6 Canecas Tulipa (4 pedidos, 7 itens), mas o volume colapsou -47% vs 30d e a conta ficou completamente inativa das 18h às 23h — se esse padrão noturno for recorrente e não anomalia de ontem, a hipótese de transição de perfil (menos compradores, maior valor) se fortalece; se for anomalia, há queda de exposição noturna que precisa ser verificada antes de qualquer intervenção.

🟠 *Budamix Shop (Shopee 3):* A Conta 3 é o sinal mais urgente do pacote: 9 pedidos distribuídos em 9 horas distintas, 1 por hora, sem cluster em nenhuma janela — nem o Kit 6 Canecas Tulipa (4 pedidos, líder da conta) gerou concentração horária, o que distingue ausência de mecanismo ativo de geração de pedidos de queda de demanda normal; com -62% vs mesmo dia da semana e -66% vs 30d tanto em pedidos quanto em GMV, a conta não está oscilando dentro de uma banda — está operando sem tração real, e isso exige checagem de exposição antes de qualquer outra ação.

🎯 PRIORIDADES DO DIA
• Lucas: checar exposição dos produtos líderes da Budamix Shop (Conta 3) — listagens, posicionamento e visibilidade na plataforma. A conta não gerou tração em nenhum horário do dia (9 pedidos em 9 horas distintas, 1 por hora). Se exposição estiver comprometida, alinhar com Himmel exclusivamente para Conta 3. Se exposição estiver normal, observar por mais 2 dias antes de qualquer movimento. Escalar para Kobe se Conta 3 ficar abaixo de 12 pedidos/dia com mesma distribuição pulverizada por 2 dias consecutivos.
• Lucas: verificar se a inatividade da Budamix Oficial das 18h às 23h é padrão recorrente nos últimos 3–5 dias ou anomalia de ontem. Se for anomalia, checar exposição noturna desta conta. Se for padrão, sustenta leitura de transição de perfil e mantém observação sem intervenção.
• Lucas: não ajustar ADS em nenhuma das três contas hoje — sem causa confirmada e com base de memória qualitativa zero, qualquer ajuste seria agir no escuro.
• Lucas: não testar produtos secundários nem dispersar exposição para cauda do catálogo — com concentração top3 entre 69–89% nas três contas em trajetória descendente, dispersar foco dos campeões reduz exposição dos únicos produtos que ainda sustentam o GMV.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** SKU 098 pelo display_name "Pote de Vidro Hermético 800ml"
  - Origem do bloqueio: Condensadora (via Granular)
  - Motivo: display_name diverge do produto real (raw_title: "Kit 9 Potes Vidro Quadrados Hermético") — usar o nome exibido descreveria produto diferente do vendido
  - Agregado autorizado: não
  - Tratamento aplicado: omitido do ranking de Top Produtos
  - Aparece na mensagem final: não

- **Item bloqueado:** Atribuição de cancelamentos a produto específico
  - Origem do bloqueio: Condensadora (via Granular)
  - Motivo: pacote não discrimina produto por cancelamento; qualquer atribuição seria invenção
  - Agregado autorizado: não
  - Tratamento aplicado: cancelamentos mencionados apenas como total numérico na VISÃO (3 cancelamentos na Store), sem atribuição de produto
  - Aparece na mensagem final: sim, apenas como número absoluto sem atribuição

- **Item bloqueado:** FITA500M (fita adesiva industrial)
  - Origem do bloqueio: Condensadora
  - Motivo: produto fora da categoria principal, 1 pedido com mapeamento por fallback de confiança média
  - Agregado autorizado: não
  - Tratamento aplicado: omitido
  - Aparece na mensagem final: não

- **Item bloqueado:** ITEM:57356981475
  - Origem do bloqueio: Condensadora
  - Motivo: 1 pedido sem raw_sku, mapeado apenas por platform_item_id com confiança média
  - Agregado autorizado: não
  - Tratamento aplicado: omitido
  - Aparece na mensagem final: não

- **Item bloqueado:** Referência à inatividade da Conta 2 como janela de 7–9 horas
  - Origem do bloqueio: Granular (correção de premissa da Operacional)
  - Motivo: janela real confirmada é 18h–23h (6 horas); inflada para 9h cria percepção de gravidade maior do que os dados sustentam
  - Agregado autorizado: sim — janela correta de 6 horas
  - Tratamento aplicado: substituído por "das 18h às 23h"
  - Aparece na mensagem final: sim, com janela correta

- **Item bloqueado:** SKUs técnicos, platform_item_ids e shop_ids
  - Origem do bloqueio: regra estrutural da Slack Writer
  - Motivo: IDs técnicos não devem aparecer na mensagem final
  - Tratamento aplicado: omitidos de toda a mensagem
  - Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Operacional`, `— base: Granular`, etc.) de todos os insights — motivo: regra de fidelidade da Slack Writer; metadados de pipeline não vão para Slack
- Seção renomeada de `🔍 ANÁLISE DA CONTA` para `🔍 ANÁLISE DAS CONTAS` no corpo — motivo: addendum v3.1 instrui usar plural quando 6B existir com 3 contas consolidadas
- Insights da ANÁLISE DAS CONTAS reproduzidos integralmente da 6B com ajuste mínimo: SKUs técnicos (IMB501P, CK4742) substituídos por nomes comerciais ("Tampa Preta", "Jarra Medidora") nas linhas da Store — motivo: regra de proibição de SKU cru visível; os nomes comerciais são suficientes para identificação pelo destinatário
- Kit 2 Potes de Vidro 800ml Quadrado consolidado cross-conta (Store 2 + Conta 3: 2 = 4 pedidos totais) — motivo: regra de consolidação de variação equivalente nas 3 contas; mesmo SKU KIT2YW800SQ confirmado nas duas contas
- CTL002 apresentado como linha consolidada cross-conta nas 3 contas (15 pedidos total) com detalhamento por conta — motivo: regra de consolidação cross-conta para variação equivalente; produto aparece com relevância top3 nas 3 contas simultaneamente, detalhamento por conta preserva rastreabilidade
- Produtos omitidos do ranking por bloqueio (SKU 098, FITA500M, ITEM:57356981475): registrado em Respeito de bloqueios; sem impacto no ranking restante além da posição
- Prioridades reproduzidas diretamente das `priority_lines` da 6B com atribuição a Lucas — motivo: destinatário da mensagem é Lucas (Shopee); Himmel mencionado apenas como alinhamento via Lucas, conforme regra de governança
- Não foi adicionado nenhum escalonamento para Pedro ou Kobe nas prioridades, exceto o gatilho já presente na 6B (Conta 3 abaixo de 12 pedidos/dia por 2 dias) — motivo: regra de não adicionar escalonamento que não veio da Condensadora
- Condensadora entregou 3 insights e 4 prioridades; todos foram preservados sem corte — motivo: nenhum estava bloqueado e todos estavam dentro do limite de 3 insights da análise