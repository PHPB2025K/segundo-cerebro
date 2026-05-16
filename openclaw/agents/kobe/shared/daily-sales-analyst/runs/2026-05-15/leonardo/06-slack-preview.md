<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 15/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 878,00
- Pedidos: 27 pedidos
- Ticket médio: R$ 32,52
- Cancelamentos: 0
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Jarra Medidora de Vidro 500ml — 7 pedidos
- Suporte Controle Gamer — 5 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 4 pedidos
- Kit 6 Xícaras Porcelana Paris 170ml — 1 pedido
- Kit 2 Potes de Vidro 1050ml Retangular — 1 pedido

🔍 ANÁLISE DA CONTA
- Parece dia fraco pelo GMV, mas a operação está íntegra — FBA 100%, zero cancelamentos, volume dentro da banda histórica. O que caiu foi o valor capturado por pedido, não a demanda. A leitura correta é compressão de ticket, não perda de canal.
- A explicação mais coerente para o ticket comprimido é que um único ASIN de menor valor liderou com quase 26% dos pedidos e pode ter arrastado o ticket médio da conta — mas isso é hipótese, não fato confirmado. Sem receita por produto no pacote e sem histórico qualitativo acumulado da conta, não é possível classificar como tendência nova ou patamar recente.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box e cobertura FBA dos ASINs líderes diretamente no Seller Central. A operação parece saudável, mas o ticket comprimido levanta hipótese de mix shift — validar os pré-requisitos agora evita retrabalho se o sinal se confirmar nos próximos dias e for necessário acionar Pedro. Confirmar/refutar por: Buy Box acima de 85% nos ASINs líderes e FBA sem ruptura confirmam que os pré-requisitos para eventual ação de ADS estão íntegros. Escalar se: Buy Box abaixo de 85% em qualquer ASIN líder ou ruptura de FBA identificada — acionar Pedro imediatamente.

Dia analisado: 15/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: TL250P / TL6250 — "Tigela de Vidro 250ml" / "Kit 6 Tigelas de Vidro 250ml" (display_name do sistema)
- Origem do bloqueio: Granular + Condensadora
- Motivo: erro de mapeamento confirmado — display_name do sistema diverge do raw_title do pedido real; produto correto é "Canecas de Porcelana Tulipa 250ml", não "Tigela de Vidro"
- Agregado autorizado: não — nenhum agregado autorizado pela Condensadora para esses SKUs
- Tratamento aplicado: omitidos do Top Produtos
- Aparece na mensagem final: não

- Item bloqueado: mix shift como fato consumado
- Origem do bloqueio: Condensadora
- Motivo: hipótese coerente mas sem confirmação granular direta (sem receita por ASIN no pacote)
- Agregado autorizado: sim — linguagem de hipótese/indício autorizada
- Tratamento aplicado: preservada como hipótese com ressalva explícita ("mas isso é hipótese, não fato confirmado")
- Aparece na mensagem final: sim, como hipótese

- Item bloqueado: compressão de ticket como tendência confirmada
- Origem do bloqueio: Condensadora
- Motivo: weekly e monthly sem histórico — sem base para afirmar se é deterioração nova ou patamar recente
- Agregado autorizado: sim — linguagem de indício autorizada
- Tratamento aplicado: preservada a ressalva de inconclusividade temporal
- Aparece na mensagem final: sim, com ressalva

- Item bloqueado: 14,8% do volume sem produto identificado (4 pedidos)
- Origem do bloqueio: Condensadora
- Motivo: detalhe interno de qualidade de dados, não deve aparecer no Slack
- Agregado autorizado: não
- Tratamento aplicado: omitido da mensagem
- Aparece na mensagem final: não

---

### Decisões de formatação

- Top Produtos limitado a 5 itens — ranking seguro do pacote; TL250P e TL6250 omitidos por bloqueio de mapeamento; SPC013 e KJP0041 (confiança medium, mapped_generic_sku) omitidos por não comporem o top 5 seguro após bloqueios
- TL250P e TL6250 omitidos do ranking — bloqueio da Condensadora por erro de mapeamento confirmado pela Granular; nenhum agregado autorizado; itens simplesmente não aparecem
- ASINs não exibidos na mensagem — nenhum ASIN dos 5 produtos selecionados apresentou título ambíguo entre si nem foi marcado com risco médio de identificação pela Granular que exigisse ASIN explícito; os títulos são suficientemente distintos
- Mix shift preservado como hipótese — "pode ter arrastado" e "hipótese, não fato confirmado" mantidos conforme classificação da Condensadora; não elevado para conclusão
- Ressalva de memória vazia preservada — "sem histórico qualitativo acumulado da conta" reflete o alerta da Condensadora sobre weekly/monthly vazios; mantida na análise para não induzir Leonardo a tratar a leitura como tendência confirmada
- Remoção de metadados internos — "base: Estratégica + Granular", "base: Operacional + Granular" removidos dos insights; tese preservada integralmente
- Nenhum insight de enchimento adicionado — Condensadora entregou 2 insights; usados os 2, sem complementação
- Prioridade única preservada na íntegra — Condensadora entregou 1 prioridade; estrutura ação + evidência + sinal de confirmação/refutação + gatilho de escalonamento mantida conforme regra 7.2
- Seção VISÃO sem comparação temporal — dados objetivos do dia apenas; comparações pertencem à análise e vieram da Condensadora
- FBA informado na VISÃO como dado objetivo — 100% FBA é dado estrutural do dia, não análise