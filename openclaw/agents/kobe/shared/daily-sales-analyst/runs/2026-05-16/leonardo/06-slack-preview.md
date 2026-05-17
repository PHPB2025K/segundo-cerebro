<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 16/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 1.238,10
- Pedidos: 36 pedidos
- Ticket médio: R$ 34,39
- Cancelamentos: 0
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Jarra Medidora de Vidro 500ml — 11 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 6 pedidos
- Suporte Controle Gamer — 5 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 4 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 3 pedidos
- Kit 6 Canequinhas 100ml — 2 pedidos
- Saco Plástico PP 78 Unidades (1kg) 40 x 70cm — 2 pedidos
- Kit Conjunto 3 Potes Vidro Hermético 320ml, 520ml, 800ml Tampa 4 Travas — 1 pedido
- Kit 2 Potes de Vidro 320ml Retangular — 1 pedido

🔍 ANÁLISE DA CONTA
- O crescimento de volume é real e consistente nas três janelas históricas, mas não se traduziu em crescimento proporcional de GMV — porque os ASINs que lideram o volume têm ticket abaixo da média da conta. A concentração por pedidos no top 3 é 61,1%, enquanto a concentração por GMV é 57,9%: os produtos que ganham tração unitária têm ticket menor. A conta cresce por quantidade, ainda não por qualidade de mix.
- O risco de concentração está subestimado quando lido por produto individual. Não é um líder isolado com cauda distribuída — são duas famílias: Jarra Medidora (30,6% do volume) e o grupo de Potes Redondos Vidro somando as duas variações de tampa (25,0%), sustentando juntas 55,6% do dia. Qualquer evento simultâneo de Buy Box, estoque ou listing nessas duas famílias elimina mais da metade do volume da conta.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box nos ASINs líderes das duas famílias dominantes — Jarra Medidora e grupo de Potes Redondos Vidro. O crescimento de volume é confirmado em três janelas históricas, mas a saúde estrutural depende de Buy Box ativa nas famílias que concentram 55,6% do dia. Confirmar/refutar: Buy Box igual ou acima de 85% nos ASINs líderes das duas famílias confirma base apta para eventual aceleração; abaixo disso, qualquer movimentação de tráfego pago fica suspensa. Escalar se Buy Box comprometida nas duas famílias principais: alinhar com Pedro antes de qualquer ação de tráfego pago.
- Leonardo: registrar ticket médio e concentração das duas famílias líderes nos próximos 2 dias como dado observacional. O ticket de hoje tem hipótese de mix plausível, mas uma única leitura não distingue evento pontual de compressão estrutural. Confirmar/refutar: ticket acima de R$ 40,00 amanhã confirma evento contextual; ticket abaixo de R$ 38,00 por mais 2 dias seguidos transforma hipótese em risco ativo. Escalar se ticket abaixo de R$ 38,00 por 3 ou mais dias consecutivos: acionar Pedro para discussão de mix no catálogo.

Dia analisado: 16/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: TL6250 — display_name `Kit 6 Tigelas de Vidro 250ml`
- Origem do bloqueio: Granular / Condensadora
- Motivo: divergência de naming — raw_title do pedido real é `Budamix Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas Café Chá Xícara Presente Casa Cozinha`; display_name aponta categoria errada
- Agregado autorizado: não — mas a Condensadora autorizou uso do título real do pedido
- Tratamento aplicado: substituído pelo título real do pedido: `Kit 6 Canecas Porcelana Tulipa Lisa 250ml`
- Aparece na mensagem final: sim, como `Kit 6 Canecas Porcelana Tulipa Lisa 250ml`

---

- Item bloqueado: TL250P — display_name `Tigela de Vidro 250ml`
- Origem do bloqueio: Granular / Condensadora
- Motivo: divergência de naming — raw_title do pedido real é `Budamix Kit 6 Canecas de Porcelana Tulipa 250ml para Café e Chá Empilhável`; display_name aponta categoria errada
- Agregado autorizado: não — Condensadora autorizou uso do título real ou omissão
- Tratamento aplicado: omitido da mensagem final (1 pedido, cauda de ranking, sem título seguro para Slack que não gere confusão)
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Estratégica + Granular`) de ambos os insights da Condensadora — metadados internos não pertencem ao Slack
- TL6250 substituído pelo título real do pedido (`Kit 6 Canecas Porcelana Tulipa Lisa 250ml`) em vez do display_name bloqueado — autorizado pela Condensadora
- TL250P omitido do Top Produtos — 1 pedido, display_name bloqueado, título real não incluso no ranking de forma destacável sem risco; omissão preferida à citação com nome errado
- ASIN não exibido para nenhum produto — todos os top ASINs têm título real identificável e a Granular não marcou risco médio de identificação nos líderes; exibição de ASIN seria desnecessária e poluiria o Slack
- Faturamento total apresentado com duas casas decimais: R$ 1.238,10 — padrão numérico obrigatório
- Seção VISÃO sem comparações temporais — dados objetivos do dia apenas; comparações ficam na análise
- Prioridades com atribuição a Leonardo (Amazon) conforme responsável do canal
- Escalonamento via Pedro preservado nas duas prioridades — veio explicitamente das Prioridades Condensadas, não foi adicionado pela Slack Writer
- Kit 6 Canequinhas 100ml: display_name `Kit 6 Canequinhas 100ml` usado — raw_title confirma produto de canecas/canequinhas com suporte madeira/alumínio; não há divergência bloqueante; confidence high
- Kit Conjunto 3 Potes e Kit 2 Potes: títulos encurtados do raw_title usados conforme display_name validado; confidence medium mas sem bloqueio ativo da Granular/Condensadora para esses itens — mantidos com títulos curtos legíveis