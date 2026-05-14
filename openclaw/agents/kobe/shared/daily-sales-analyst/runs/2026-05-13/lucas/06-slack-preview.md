<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — SHOPEE — 13/05/2026 (Ontem)

📊 VISÃO SHOPEE
- Total Shopee: R$ 5.964,55 — 119 pedidos — ticket médio R$ 50,12 — 9 cancelamentos
- Budamix Store: R$ 3.285,11 — 75 pedidos — 5 cancelamentos
- Budamix Oficial (Conta 2): R$ 852,36 — 13 pedidos — 3 cancelamentos
- Budamix Shop (Conta 3): R$ 1.827,08 — 31 pedidos — 1 cancelamento

🏆 TOP PRODUTOS SHOPEE
- Store — item líder: 31 pedidos
- Store — segundo item: 26 pedidos
- Store — terceiro item: 15 pedidos
- Conta 2 — item líder: 5 pedidos
- Conta 2 — segundo item: 4 pedidos
- Conta 3 — item líder: 12 pedidos
- Conta 3 — segundo item: 9 pedidos
- Conta 3 — terceiro item: 5 pedidos

🔍 ANÁLISE DA CONTA
- A Budamix Oficial (Conta 2) não tem apenas queda de demanda — tem execução comprometida: colapso de volume em todas as janelas combinado com taxa de cancelamento de 23% (3 em 13 pedidos) é padrão de algo bloqueando ou revertendo pedidos na conta, não de demanda baixa. Tratar como "dia fraco" distorce a ação necessária.
- A Budamix Store (Conta 1) parece estar segurando o resultado, mas o GMV está sendo sustentado por ticket anomalamente elevado (R$ 43,80 vs banda histórica de R$ 35–39) enquanto o volume de pedidos cai há pelo menos 60 dias. Se o ticket reverter para a banda, o GMV cai estruturalmente — o resultado de hoje mascara erosão em curso, não estabilidade.
- A Budamix Shop (Conta 3) manteve volume, mas o mix migrou para produtos de menor valor: ticket comprimido de R$ 67–72 histórico para R$ 58,94, com itens de menor preço liderando. Pedidos estáveis com GMV em queda é deterioração silenciosa de composição — não é dia neutro.

🎯 PRIORIDADES DO DIA
- Lucas: verificar Conta 2 (Budamix Oficial) na plataforma Shopee — checar se há campanha pausada, limitação de exposição, listing com problema ou restrição de loja. A combinação de colapso de volume e cancelamento de 23% aponta para causa operacional ou de plataforma, não demanda pura. Confirmar/refutar: volume acima de 20 pedidos amanhã sem intervenção indica evento pontual; abaixo de 18 pelo segundo dia seguido com exposição normal, escalar para Himmel sobre exposição de campanha.
- Lucas: acompanhar ticket médio de Conta 1 (Budamix Store) nos próximos 2 dias. O GMV está sustentado por ticket fora da banda histórica — reversão expõe a erosão de volume sem compensação. Confirmar/refutar: ticket abaixo de R$ 39 por 2 dias seguidos com pedidos abaixo de 70 confirma erosão estrutural; ticket acima de R$ 40 por mais um dia sustenta acomodação. Escalar se erosão for confirmada.

Dia analisado: 13/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** todos os produtos nominais das 3 contas Shopee (Jarra Medidora, Conjunto Potes, Canecas Tulipa, etc.)
- **Origem do bloqueio:** Condensadora
- **Motivo:** Granular usou fallback determinístico — sem validação de identidade de produto; Condensadora explicitou "usar apenas agregados"
- **Agregado autorizado:** sim — Condensadora autorizou agregados do tipo "o produto líder", "o item de maior valor da conta"
- **Tratamento aplicado:** substituídos por agregados posicionais com indicação de conta ("Store — item líder", "Conta 2 — segundo item", etc.)
- **Aparece na mensagem final:** sim, como agregados posicionais por conta

---

### Decisões de formatação

- Remoção de metadados internos (`— base: Operacional + Tática`, `— base: Estratégica + Operacional`, `— base: Operacional + Granular (fallback)`) dos 3 insights — conteúdo e tese preservados integralmente
- Substituição de todos os produtos nominais por agregados posicionais em Top Produtos — bloqueio da Condensadora; agregado posicional autorizado explicitamente
- Faturamento por produto omitido em Top Produtos — dado não disponível no pacote (apenas quantity por produto); omissão registrada para QA
- Indicação de conta em todos os itens de Top Produtos — cada produto vendeu em conta única; regra Shopee exige identificação de conta quando produto vendeu em menos de 2 contas
- Cancelamentos incluídos em VISÃO SHOPEE para as 3 contas e total — relevantes e disponíveis no pacote; apresentados como dado objetivo sem análise
- Linguagem de hipótese preservada na análise de Conta 2 ("padrão de algo bloqueando", "aponta para causa operacional") — confiança média declarada pela Condensadora; diagnóstico de Conta 2 não foi marcado como fato confirmado
- Padrão numérico aplicado: vírgula decimal (R$ 43,80; R$ 58,94; R$ 50,12), ponto separador de milhar (R$ 5.964,55; R$ 3.285,11; R$ 1.827,08), pedidos sem separador (119 pedidos, 75 pedidos)
- Condições de confirmação/refutação e escalonamento preservadas integralmente em Prioridades — vieram da Condensadora e são estruturalmente necessárias para ação correta de Lucas