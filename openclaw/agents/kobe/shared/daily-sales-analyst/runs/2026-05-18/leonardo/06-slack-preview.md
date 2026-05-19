<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — AMAZON — 18/05/2026 (Ontem)

📊 VISÃO AMAZON
- Faturamento: R$ 1.839,70
- Pedidos válidos: 45
- Ticket médio: R$ 40,88
- Cancelamentos: 2
- Fulfillment: 100% FBA

🏆 TOP PRODUTOS AMAZON
- Conjunto 5 Potes de Vidro Redondos Tampa Preta — 12 pedidos
- Jarra Medidora de Vidro 500ml — 12 pedidos
- Conjunto 5 Potes de Vidro Redondos Tampa Cinza — 3 pedidos
- Kit 6 Canecas Porcelana Tulipa 250ml Branco — 3 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas — 2 pedidos
- Suporte Controle Gamer — 2 pedidos
- Kit 6 Xícaras Porcelana Paris 170ml — 2 pedidos
- Kit 6 Canequinhas 100ml — 1 pedido
- Kit 6 Canecas 250ml — 1 pedido

🔍 ANÁLISE DA CONTA
- O dia teve volume real acima do padrão histórico, mas a leitura positiva tem um limite claro: Buy Box e cobertura FBA dos dois ASINs que sustentam 53% do resultado são desconhecidos. O patamar de crescimento não está operacionalmente ancorado enquanto essa verificação não for feita diretamente na plataforma.
- A concentração da conta é mais profunda do que dois produtos independentes: o grupo de potes redondos (Tampa Preta + Tampa Cinza) soma 33% do dia sozinho, e junto com a Jarra Medidora 500ml chega a 60% do volume total. O risco não se divide entre dois vetores — qualquer disrução no fulfillment do grupo de potes redondos afeta as duas variações ao mesmo tempo.

🎯 PRIORIDADES DO DIA
- Leonardo: checar Buy Box e cobertura FBA dos dois ASINs líderes (Potes Redondos e Jarra Medidora) diretamente na plataforma Amazon. Eles sustentam 60% do volume do dia — sem essa verificação, não dá para saber se o crescimento está sobre base operacional saudável. Confirmar/refutar: se Buy Box ativa e FBA sem alerta de cobertura crítica nos dois, a base está saudável e a conversa sobre ADS com Pedro passa a ser pertinente. Escalar se: Buy Box degradada ou cobertura FBA crítica em qualquer um dos dois — resolver operacional antes de qualquer movimento em tráfego pago; se tudo estiver íntegro e o volume se mantiver acima de 35 pedidos por mais 2 dias, acionar Pedro para avaliação de ADS com diagnóstico fechado.

Dia analisado: 18/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- Item bloqueado: `TL250B — display_name "Tigela de Vidro 250ml"`
- Origem do bloqueio: Granular + Condensadora
- Motivo: display_name incorreto no mapeamento — produto real é canecas de porcelana (linha Tulipa 250ml), não tigela de vidro
- Agregado autorizado: não — Granular autorizou uso do título real do pedido se necessário citar
- Tratamento aplicado: substituído por título real derivado do raw_title: "Kit 6 Canecas Porcelana Tulipa 250ml Branco"
- Aparece na mensagem final: sim, como título real "Kit 6 Canecas Porcelana Tulipa 250ml Branco"

---

- Item bloqueado: `TL6250 — display_name "Kit 6 Tigelas de Vidro 250ml"`
- Origem do bloqueio: Granular + Condensadora
- Motivo: display_name incorreto — produto real é canecas de porcelana coloridas (linha Tulipa Lisa 250ml), não tigelas de vidro
- Agregado autorizado: não — mesma orientação do TL250B: usar título real do pedido
- Tratamento aplicado: substituído por título real derivado do raw_title: "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas"
- Aparece na mensagem final: sim, como título real "Kit 6 Canecas Porcelana Tulipa Lisa 250ml Coloridas"

---

- Item bloqueado: `JMOCE — Jogo da Memória Infantil MDF Oceano 16 Peças`
- Origem do bloqueio: Condensadora
- Motivo: confidence medium, mapping_status mapped_generic_sku — Condensadora indicou não citar nominalmente como produto confiável
- Agregado autorizado: não
- Tratamento aplicado: omitido do ranking
- Aparece na mensagem final: não

---

### Decisões de formatação

- Remoção de metadados internos nos insights ("— base: Tática + Granular", "— base: Granular + Estratégica") — campo de auditoria interna, não vai ao Slack
- Remoção de "o pacote não contém esses dados" do insight 1 — referência interna ao pipeline; a tese ("são desconhecidos") foi preservada integralmente
- Substituição de "por Leonardo diretamente na plataforma" por "diretamente na plataforma" no insight 1 — elimina referência ao nome do destinatário dentro da análise (o destinatário já recebe a mensagem); tese não alterada
- TL250B: citado com título real do pedido em vez de display_name bloqueado — orientação explícita da Granular; nenhum ASIN adicionado pois o título derivado do raw_title é suficientemente identificável; decisão registrada por cautela
- TL6250: mesmo tratamento do TL250B — título real derivado do raw_title, sem ASIN, título identificável sem ambiguidade
- JMOCE omitido do ranking — bloqueio da Condensadora sem agregado autorizado; item com 1 pedido; ranking restante permanece em ordem decrescente por pedidos sem lacuna visível
- ASINs omitidos de todos os produtos no ranking — os cinco primeiros têm confidence high com título de pedido claro e sem ambiguidade de título igual para produtos distintos; JMOCE (único com confidence medium) foi omitido do ranking integralmente; nenhum item apresenta condição que exija ASIN visível
- Produtos TL250B e IMB501C empatados em 3 pedidos — mantida a ordem original do pacote de dados (TL250B na posição 3, IMB501C na posição 4)
- Seção VISÃO sem comparações temporais — comparações pertencem à análise; apenas dados objetivos do dia nesta seção
- Confiança média preservada na análise — dois insights entregues pela Condensadora, ambos com ressalva operacional (lacuna de Buy Box/FBA); não convertidos em certeza