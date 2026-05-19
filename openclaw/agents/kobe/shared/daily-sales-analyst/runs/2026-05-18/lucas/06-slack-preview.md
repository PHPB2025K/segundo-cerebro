<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 18/05/2026 (Ontem)

📊 VISÃO SHOPEE

• Shopee consolidado: R$ 4.741,73 — 83 pedidos — ticket médio R$ 57,13
• Budamix Store: R$ 2.497,44 — 59 pedidos
• Budamix Oficial (Conta 2): R$ 1.543,19 — 15 pedidos
• Budamix Shop (Conta 3): R$ 701,10 — 9 pedidos
• Cancelamentos: 4 (3 na Store, 1 na Conta 2)

🏆 TOP PRODUTOS SHOPEE

• Conjunto 5 Potes de Vidro Redondos Tampa Preta (Store) — 27 pedidos
• Jarra Medidora de Vidro 500ml (Store) — 18 pedidos
• Kit 6 Canecas Tulipa 250ml — 15 pedidos
• Kit 2 Potes de Vidro 800ml Quadrado — 4 pedidos
• Kit 4 Potes de Vidro 800ml Quadrado (Conta 2) — 4 pedidos
• Kit de Potes Quadrados (Conta 2) — 3 pedidos

🔍 ANÁLISE DAS CONTAS

⚫ *Consolidado (3 contas):* A Shopee fechou o dia com 83 pedidos e R$ 4.741,73, mas o número esconde três dinâmicas independentes: a Store sustenta 71% do volume via dois produtos em trajetória de queda gradual, enquanto Shop 3 e Oficial 2 mostram sinais distintos de colapso de exposição — tratá-las como "canal em queda" sem separar as causas garante que ao menos uma delas fique sem investigação urgente.

🟠 *Budamix Store (Shopee 1):* A Store entregou 59 pedidos com ticket de R$ 42,33, sustentada em 76% pelo Conjunto 5 Potes Redondos Tampa Preta (27 pedidos) e pela Jarra Medidora 500ml (18 pedidos), sem nenhum segundo vetor capaz de absorver queda em qualquer um dos dois — a conta principal do canal opera como um sistema de ponto único de falha num contexto de declínio acumulado de -37,6% em pedidos vs 60d, onde o ticket crescente (+12,4% vs 60d) ainda amortece o GMV mas não reverte a trajetória de volume.

🟠 *Budamix Oficial (Shopee 2):* Com 15 pedidos e ticket de R$ 102,88 — quase o dobro do histórico de R$ 60-62 — a Oficial 2 entregou R$ 1.543,19 de GMV apesar de volume colapsado (-56,2% vs mesmo dia da semana), o que tem base estrutural no portfólio da conta: kits maiores como o Kit 4 Potes 800ml Quadrado e o kit de potes quadrados puxam o ticket base acima da Store; o risco operacional não respondido é a ausência total de pedidos após as 17h num dia já comprimido, padrão consistente com ADS pausado ou exposição cortada na janela tarde/noite dessa conta específica.

🟠 *Budamix Shop (Shopee 3):* A Shop 3 registrou 9 pedidos — abaixo do mínimo histórico dos mesmos dias da semana (18 pedidos em 04/05) — espalhados difusamente em 9 horas distintas sem nenhuma janela de concentração, padrão que não ocorre em conta com ADS ativo e listing saudável; o Kit 6 Canecas Tulipa 250ml respondeu por 44% dos pedidos da conta, o que significa que qualquer verificação de exposição ou ADS da Shop 3 é na prática uma verificação sobre esse produto naquela conta — e esse mesmo SKU compete simultaneamente na Store (7 pedidos) e na Oficial 2 (4 pedidos), criando superfície real de canibalização.

🎯 PRIORIDADES DO DIA

• [URGENTE — Shop 3 + Oficial 2] Lucas aciona Himmel para verificar status de ADS e exposição da Shop 3 e, na mesma conversa, checar se a Oficial 2 teve ADS pausado ou exposição reduzida após as 17h — os dois padrões (distribuição completamente difusa na Shop 3; zero pedidos após 17h na Oficial 2) são consistentes com causa operacional específica de cada conta, não sazonalidade. Se Himmel confirmar normalidade nas duas, causa é de demanda e Lucas trata como variação; se houver problema em qualquer uma, Himmel e Lucas alinham correção imediata. Escalar se a Shop 3 registrar menos de 15 pedidos pelo segundo dia consecutivo.
• [HOJE — Store] Lucas confirma presencialmente estoque disponível e listing ativo dos dois produtos líderes da Store: Conjunto 5 Potes Redondos Tampa Preta e Jarra Medidora 500ml — os dois concentram 76% dos pedidos da conta principal e não há dado de cobertura futura no pacote. Se estoque e listing estiverem saudáveis, a queda da Store é de tráfego e Lucas aguarda 1-2 dias antes de qualquer ação em ADS; se houver ruptura ou problema de listing, ação imediata.
• [OBSERVAR — Oficial 2] Registrar ticket médio e distribuição horária da Oficial 2 nos próximos 2 dias. Ticket retornando à faixa de R$ 55-70 = ruído de mix; ticket acima de R$ 90 com volume abaixo de 20 pedidos = confirma estrutura diferenciada e justifica revisão da estratégia de exposição.
• [NÃO FAZER] Não acionar Himmel para aumentar verba ou alterar segmentação de ADS na Store ou na Oficial 2 antes de concluir as verificações acima — a queda é sustentada nas três contas mas sem causa identificada; escalar verba sobre tendência descendente sem diagnóstico de causa é intervenção cega que consome budget sem endereçar o problema real.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: `ITEM:57356981475` — produto sem SKU interno mapeado via platform_item_id, raw_title "Conjunto 5 Potes Vidro Kit Vasilhas Marmita Armazenamento De Alimentos Tigelas Bowls"
- Origem do bloqueio: Condensadora
- Motivo: confiança média (mapped_platform_item_id sem SKU), sem relevância de volume (1 pedido), citação nominal proibida
- Agregado autorizado: não
- Tratamento aplicado: omitido do Top Produtos
- Aparece na mensagem final: não

---

- Item bloqueado: `FITA500M` — Kit 6/12 Rolos De Fita Adesiva Transparente 45mm X 500 Metros
- Origem do bloqueio: Condensadora
- Motivo: confiança média (mapped_generic_sku com short_title_fallback), sem relevância de volume (1 pedido), citação nominal proibida
- Agregado autorizado: não
- Tratamento aplicado: omitido do Top Produtos
- Aparece na mensagem final: não

---

- Item bloqueado: `SKU 098` com display_name "Pote de Vidro Hermético 800ml"
- Origem do bloqueio: Condensadora (divergência confirmada entre raw_title e display_name)
- Motivo: display_name descreve produto estruturalmente diferente do raw_title do pedido real; citar com display_name seria erro de identificação
- Agregado autorizado: sim — "kit de potes quadrados" ou referência ao portfólio de kits maiores da Conta 2
- Tratamento aplicado: substituído por "Kit de Potes Quadrados" no Top Produtos e por "kit de potes quadrados" na análise (via 06b)
- Aparece na mensagem final: sim, como agregado "Kit de Potes Quadrados (Conta 2)"

---

- Item bloqueado: dados de fulfillment das três contas Shopee (shopee_full = 0 em todas com pedidos registrados)
- Origem do bloqueio: Condensadora
- Motivo: dado estruturalmente ausente no pacote — campos zerados não significam ausência de Shopee Full, significam dado não capturado
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem; não citado nem como "sem Shopee Full"
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de IDs técnicos SKU `KIT4YW800SQ` e `(SKU 098)` da linha de análise da Oficial 2 (06b) — regra de proibição de IDs técnicos visíveis; produto referenciado por nome descritivo sem mudar a tese analítica
- Remoção de `+19,5% vs 7d` da linha de análise da Oficial 2 no parágrafo 🟠 — dado de comparação temporal redundante dado o contexto já presente na linha; não altera tese; optou-se por manter apenas a comparação de maior impacto analítico (-56,2% vs mesmo dia da semana) que permanece intacta
- Seção de análise com header `🔍 ANÁLISE DAS CONTAS` — conforme addendum v3.1 regra 7.6: quando 06b existe, usar esse header com quatro blocos ⚫/🟠
- Parágrafos de análise mantidos como bloco corrido, não convertidos em bullets — conforme regra 7.6 ("parágrafos curtos e densos, não lista longa")
- `ITEM:57356981475` e `FITA500M` omitidos do Top Produtos — bloqueio da Condensadora, sem agregado autorizado, 1 pedido cada
- `CTL002` consolidado das três contas (Store: 7, Oficial 2: 4, Shop 3: 4 = 15 pedidos) sem indicação de conta — produto vendeu em 3 contas; regra exige indicação apenas quando vendido em menos de 2 contas ou quando a Condensadora citou conta específica como relevante no Top Produtos (a Condensadora cita Shop 3 no contexto analítico, não como instrução de formatação de ranking)
- `IMB501P` e `CK4742` com indicação `(Store)` — exclusivos da Store (venderam em 1 conta)
- `KIT4YW800SQ` com indicação `(Conta 2)` — exclusivo da Conta 2 (vendeu em 1 conta)
- `Kit de Potes Quadrados` com indicação `(Conta 2)` — exclusivo da Conta 2 (vendeu em 1 conta); nome segue formulação autorizada pela Condensadora
- `KIT2YW800SQ` consolidado de Store (2) + Shop 3 (2) = 4 pedidos, sem indicação de conta — vendeu em 2 contas, regra não exige indicação
- Ranking Top Produtos em ordem decrescente de pedidos consolidados: 27, 18, 15, 4, 4, 3 — sem inversão de posição
- Ressalvas de hipótese preservadas na íntegra: "padrão consistente com ADS pausado ou exposição cortada", "padrão que não ocorre em conta com ADS ativo e listing saudável" — linguagem de indício mantida, não convertida em fato
- Prioridade `[NÃO FAZER]` incluída — veio explicitamente da 06b como priority_line e instrução operacional relevante para Lucas
- Nenhum insight criado fora da 06b; nenhum produto bloqueado reintroduzido; nenhuma comparação temporal incluída na seção VISÃO