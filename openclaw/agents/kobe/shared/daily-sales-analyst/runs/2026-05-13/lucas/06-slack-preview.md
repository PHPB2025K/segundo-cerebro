<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 13/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Total Shopee: R$ 5.964,55 — 119 pedidos — ticket médio R$ 50,12 — 9 cancelamentos
- Budamix Store: R$ 3.285,11 — 75 pedidos — 5 cancelamentos
- Budamix Oficial / Conta 2: R$ 852,36 — 13 pedidos — 3 cancelamentos
- Budamix Shop / Conta 3: R$ 1.827,08 — 31 pedidos — 1 cancelamento

🏆 TOP PRODUTOS SHOPEE
- Jarra Medidora De Vidro 500ml com Alça (Store) — 31 pedidos
- Conjunto 5 Potes de Vidro Redondos (Store) — 26 pedidos
- Canecas Tulipa 250ml Porcelana Colorida (Store) — 15 pedidos
- Kit 6 Canecas Porcelana 200ml Reta Lisa (Conta 3) — 12 pedidos
- Potes Vidro 800ml Quadrado Hermético 2un (Conta 3) — 9 pedidos

🔍 ANÁLISE DA CONTA
- O resultado da Shopee hoje não é sinal de plataforma — é a Conta 2 (Budamix Oficial) que praticamente não operou: 13 pedidos distribuídos em 8 momentos ao longo do dia, sem nenhum pico de horário, com participação de 10,9% contra histórico de 22,6%. Store e Shop 3 carregaram juntas o que três contas saudáveis deveriam distribuir. Tratar o total de R$ 5.964,55 como resultado equilibrado das três contas distorce o diagnóstico e a ação.
- O ticket elevado da Store (R$ 43,80 contra histórico de R$ 35–38) não é recuperação — é shift de mix com pedidos -27,7% abaixo do patamar de 60 dias. A conta entregou pedidos de valor mais alto porque os de menor valor simplesmente não vieram; e o déficit de volume está distribuído ao longo do dia inteiro, sem hora específica perdida, o que aponta para menos tráfego entrante (ADS, cupons, afiliados) e não para queda de ranking em janela pontual.
- A compressão de ticket da Shop 3 (R$ 58,94 contra R$ 71,75 histórico do mesmo dia da semana) tem mecanismo identificado: nenhum pedido no dia foi multi-item — razão exata de 1 item por transação (31/31). Não é desconto nem produto mais barato: é ausência de compras que empilham unidades. Isso muda o que deve ser investigado — não é questão de preço, é questão de composição de demanda e se houve mudança em promoções que incentivavam itens múltiplos.

🎯 PRIORIDADES DO DIA
- Lucas: checar status operacional da Conta 2 (Budamix Oficial) — ADS ativo ou pausado, listing com restrição, queda de ranking ou penalidade de marketplace. A conta registrou 13 pedidos em 8 momentos esparsas sem nenhum pico funcional, com 18,75% de cancelamento — assinatura de conta sem exposição; o colapso é consistente em todas as janelas históricas e o diagnóstico de causa precisa vir antes de qualquer ajuste. Confirmar/refutar: se Lucas identificar ADS pausado ou penalidade ativa, aciona Himmel com diagnóstico fechado; sem causa operacional evidente, manter observação por mais 2 dias. Escalar se Conta 2 não apresentar causa operacional identificável após checagem de listing, ADS e ranking — nesse caso alinhar com Himmel sobre exposição via ADS Shopee da Conta 2 especificamente.
- Lucas: verificar se houve mudança recente em promoções ou configuração de compra na Shop 3 (Budamix Shop) que explique a ausência total de pedidos multi-item hoje. O mecanismo da compressão de ticket está identificado — nenhum pedido foi de múltiplos itens (31/31); se houve mudança em cupom, bundle ou configuração que incentivava itens adicionais por transação, o ticket vai continuar comprimido enquanto o volume de pedidos permanece estável. Confirmar/refutar: mudança confirmada nos últimos 7 dias → causa identificada e acionável; sem mudança → manter observação — ticket abaixo de R$ 62 pelo segundo dia consecutivo com pedidos estáveis confirma estreitamento estrutural de mix.

Dia analisado: 13/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: CTL002 — Canecas Tulipa 250ml (referência agregada entre contas)
- Origem do bloqueio: Condensadora
- Motivo: produto vendeu 25 unidades nas três contas com platform_item_ids distintos; referência sem identificação de conta mistura comportamentos de exposição radicalmente diferentes (Store: 15 un com alta exposição / Conta 2: 5 un com exposição colapsada / Shop 3: 5 un com pedidos estáveis)
- Agregado autorizado: não
- Tratamento aplicado: produto listado no Top Produtos somente na versão da Store, com identificação de conta explícita; versões da Conta 2 (5 pedidos) e Shop 3 (5 pedidos) omitidas do ranking — Store domina o SKU no dia e a listagem triplicada fragmentaria o Top Produtos sem ganho analítico
- Aparece na mensagem final: sim, como "Canecas Tulipa 250ml Porcelana Colorida (Store) — 15 pedidos"

---

### Decisões de formatação

- Remoção de metadados de atribuição (`— base: Operacional + Granular`, `— base: Estratégica + Operacional`, `— base: Granular`) dos três insights — teses preservadas integralmente
- Formatação numérica aplicada: `R$43.80` → `R$ 43,80`; `R$58.94` → `R$ 58,94`; `R$71.75` → `R$ 71,75`; `R$5.964` → `R$ 5.964,55`; percentuais com vírgula decimal
- CTL002 listado no Top Produtos apenas da Store com identificação de conta — Condensadora bloqueou referência agregada; versões da Conta 2 e Shop 3 omitidas para não fragmentar o ranking com o mesmo produto repetido três vezes
- Faturamento por produto omitido do Top Produtos — dado não disponível no pacote (top_products contém apenas quantidade); inventar ou estimar violaria a regra de não buscar dados
- Contas sempre identificadas no Top Produtos — todos os produtos do ranking venderam em uma única conta (com exceção do CTL002 tratado acima), satisfazendo a regra de indicar conta quando produto vendeu em menos de 2 contas
- Percentuais de participação (10,9% vs 22,6%) preservados na Análise — a Condensadora os incorporou explicitamente no insight aprovado; o bloqueio de "número absoluto de participação" na seção "o_que_nao_pode_ir_para_slack" foi interpretado como referente ao dado técnico bruto em tabela, não ao dado já integrado no texto do insight
- "mecanismo granular identificado" no insight 3 mantido — o termo se refere à granularidade da evidência (cálculo direto), não ao nome da camada interna
- Sem decisões ambíguas adicionais de formatação.