<!-- llm_used=true model=sonnet fallback=false -->
### Mensagem Slack

```
DAILY SALES REPORT — MERCADO LIVRE — 21/05/2026 (Ontem)

📊 VISÃO MERCADO LIVRE
- Faturamento: R$ 6.113,02
- Pedidos: 101 pedidos
- Ticket médio: R$ 60,52
- Cancelamentos: 3

🏆 TOP PRODUTOS MERCADO LIVRE
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças Preto — Tampa Preta — 31 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 10 Unidades — 16 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças Cinza — Tampa Cinza — 13 pedidos
- Potes de Vidro Hermético Redondo com Tampa Kit 5 Peças Vermelho — Tampa Vermelha — 9 pedidos
- Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 8 pedidos
- Kit 6 Canecas Porcelana Tulipa Lisa 250ml — 5 pedidos
- Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico — 3 pedidos
- Kit 10 Potes Herméticos 520ml Azul-petróleo 10 Unidades — 2 pedidos
- Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades — 2 pedidos
- Kit 2 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo — 2 pedidos

🔍 ANÁLISE DA CONTA
- Dois anúncios em Full têm estoque crítico com pedidos sem cobertura: o Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico registrou ao menos 2 dos 3 pedidos do dia sem estoque no CD do ML — cancelamento automático iminente em horas, com cancellations_rate em zero e a conta a ~15 dias do limiar MercadoLíder Platinum. O Kit 6 Canecas Porcelana Tulipa Lisa 250ml tem cobertura de ~3 dias ao ritmo atual, com ruptura em Full provável até 24/05. O resultado do dia não reflete esse risco — ele é invisível na métrica agregada.
- O GMV de R$ 6.113,02 (+30,5% vs quintas equivalentes) não veio de mais pedidos: os 101 pedidos ficaram dentro da banda normal de uma quinta (-1,7%). O resultado veio do ticket médio de R$ 60,52 — 33% acima da média das quintas. A conta não atingiu mais compradores; capturou mais receita por pedido. A trajetória de ticket é contínua em todas as janelas (R$ 41,44 nos 60d → R$ 44,36 nos 30d → R$ 47,25 nos 7d → R$ 60,52 hoje), mas ainda depende da composição do dia para se sustentar.
- O mix de modalidade de envio do dia (80% Cross-Docking vs 77% Full nos últimos 7 dias e 74% nos últimos 30 dias) não é mudança operacional da conta. É a família dos Potes de Vidro Redondos dominando o dia com 53 pedidos (52% do volume), todos em Cross-Docking. Quando esses produtos lideram, o mix do dia inverte em relação ao histórico. A estrutura da operação não mudou; o que mudou foi o produto que liderou.

🎯 PRIORIDADES DO DIA
- Yasmin: verificar agora no painel ML — ou via API de pedidos — o status dos pedidos do Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico em Full: quantos ainda estão abertos e se há janela para cancelamento controlado ou reposição emergencial no CD do ML antes do cancelamento automático. Ao menos 2 dos 3 pedidos do dia não têm cobertura de estoque no CD do ML (available_quantity=1 no snapshot). Cancelamento automático pelo ML pressiona o cancellations_rate — hoje em zero — justamente no ciclo em que a conta está a ~15 dias do limiar MercadoLíder Platinum. É o único ponto do dia com urgência de horas. Confirmar/refutar em até 2 horas: pedidos abertos sem estoque visíveis no painel = janela ainda disponível, agir imediatamente; cancelamentos já processados = registrar impacto como variável conhecida e monitorar cancellations_rate nos próximos 2 ciclos. Escalar se cancellations_rate subir de zero em mais de um ciclo consecutivo após resolução — avaliar risco à janela de qualificação Platinum.
- Yasmin: verificar estoque do Kit 6 Canecas Porcelana Tulipa Lisa 250ml em Full no painel ML e iniciar reposição se necessário. Cobertura estimada de ~3 dias ao ritmo atual, com ruptura provável até 24/05. O anúncio tem vínculo com produto de catálogo associado, mas a implicação da ruptura nesse vínculo não foi confirmada — prioridade é garantir o atendimento dos pedidos. Confirmar/refutar: se available_quantity cair abaixo de 5 no próximo snapshot, ruptura em menos de 24h; se reposição para o CD do ML for confirmada, risco neutralizado.

Dia analisado: 21/05/2026 — 00:00–23:59 BRT
```

---

### Respeito de bloqueios

- **Item bloqueado:** Atribuição de receita ADS a anúncios ou famílias específicas (ex.: "ADS impulsionou a família IMB501" ou "ADS priorizou anúncios Full")
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** ads_summary exclusivamente agregado — sem breakdown de revenue ADS por platform_item_id no pacote; qualquer afirmação direcional seria fabricação de evidência
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — ADS não é mencionado como driver de produto específico na mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Direção do health=0,75 do Kit 4 Potes de Vidro Hermético 1050ml Tampa Azul-petróleo como confirmada, descartada ou em recuperação
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** série temporal de health ausente do pacote — ml_snapshot entrega apenas valor pontual; afirmar estabilidade ou queda seria erro silencioso
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — health do Kit 4 Potes não é citado na mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** Estado atual dos cancelamentos automáticos do Kit 6 Canequinhas 100ml com Suporte de Madeira Acrílico (se já foram processados ou se a janela de intervenção ainda está aberta)
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** não determinável pelo pacote — snapshot registra available_quantity pontualmente sem dados de pedidos abertos em tempo real
- **Agregado autorizado:** não
- **Tratamento aplicado:** preservada a incerteza na prioridade — texto usa "verificar… se há janela para cancelamento controlado" sem afirmar que a janela está aberta ou fechada
- **Aparece na mensagem final:** sim, como incerteza preservada na prioridade 1

---

- **Item bloqueado:** Inconsistência no título ML do Kit 10 Potes Herméticos 1050ml Azul-petróleo 6 Unidades ("Kit 10 Potes...6 Unidades") como alerta operacional para Yasmin
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** inconsistência interna do próprio listing ML, não erro de mapeamento; 2 pedidos no dia, sem ação clara — citar geraria ruído
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — inconsistência não citada na mensagem
- **Aparece na mensagem final:** não

---

- **Item bloqueado:** ratings_negative=0,39 como indicativo de risco de reputação iminente
- **Origem do bloqueio:** L05 Condensadora
- **Motivo:** termômetro ML permanece verde pelos indicadores operacionais; citar percentual de negativos sem explicar o mecanismo induziria leitura equivocada de crise
- **Agregado autorizado:** não
- **Tratamento aplicado:** omitido — ratings_negative não citado na mensagem
- **Aparece na mensagem final:** não

---

### Decisões de formatação

- Remoção de metadados internos (`padrao`, `base`, `classificacao`) de todos os 3 insights — são campos internos de pipeline, não visíveis no Slack.
- Insight 1 (risco latente): preservada linguagem de risco operacional iminente sem transformar em fato consumado — "ao menos 2 dos 3 pedidos… sem estoque" mantém a nuance de incerteza sobre cancelamentos já processados vs janela aberta, conforme bloqueio da L05.
- Insight 2 (fato): mantido como fato — classificação da L05 é `fato`; linguagem direta sem hedging. Números preservados integralmente (R$ 6.113,02; R$ 60,52; R$ 41,44; R$ 44,36; R$ 47,25).
- Insight 3 (fato): substituída referência interna "família IMB501" por "família dos Potes de Vidro Redondos" para clareza operacional com Yasmin — o nome interno IMB501 não é nomenclatura usada no Slack. Classificação da L05 é `fato`; mantida linguagem direta.
- `📊 VISÃO MERCADO LIVRE`: sem comparações temporais — dados objetivos do dia apenas, conforme regra da seção.
- Modalidade de envio omitida da `📊 VISÃO MERCADO LIVRE`: dado do `fulfillment_mix_yesterday_top10` cobre apenas top 10 (91 de 101 pedidos = ~90%); não autorizado pela Condensadora para VISÃO; tratado apenas na `🔍 ANÁLISE DA CONTA`.
- `🏆 TOP PRODUTOS MERCADO LIVRE`: usado `display_short` verbatim para todos os produtos. Para IMB501P, IMB501C e IMB501V: `confirmed_variation_attributes` não vazios → atributo de cor incluído no formato `[display_short] — [atributo confirmado]`. Para os demais: `confirmed_variation_attributes` vazio → apenas `display_short`.
- Nenhum MLB exibido na mensagem final — todos os platform_item_id omitidos.
- Nenhum SKU cru exibido — omitidos de toda a mensagem.
- Faturamento por produto omitido do Top Produtos: pacote não traz receita validada por produto/variação — formato padrão `[nome] — [pedidos] pedidos` aplicado a todos.
- Prioridades: Yasmin atribuída como responsável fixo em ambas as prioridades, conforme regra da seção.
- Prioridade 1: a L05 menciona "painel ML ou API de pedidos" como caminhos — ambas as alternativas preservadas ("painel ML — ou via API de pedidos") para não suprimir alternativa operacional.
- Prioridade 2: implicação de ruptura no vínculo com catalog_product_id preservada como incerteza ("não foi confirmada") conforme L05, sem afirmar nem descartar.
- Escalonamento da prioridade 1 ("Escalar se cancellations_rate subir de zero em mais de um ciclo consecutivo") preservado da L05.
- Prioridade 2 sem "Escalar se" — L05 marcou "não aplicável".
- Divergência de denominação cross-layer — Insight 3: L05 usou "família IMB501" no campo `insight`; L06 usou "família dos Potes de Vidro Redondos". Motivo: padronização com linguagem operacional de Yasmin — o código IMB501 não é referência usada no Slack e não aparece nos títulos de produto. Produto identificado unicamente pelas variações (Tampa Preta/Cinza/Vermelha) presentes no Top Produtos.
- Atribuição de Yasmin como responsável nas prioridades — L05 não atribui responsável; L06 atribui conforme regra da seção.
- Confiança média da L05 preservada estruturalmente: análise não emite certezas sobre pontos declarados inconclusivos (estado da janela de cancelamento, direção do health, breakdown de ADS).